from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import lxml.html
import requests
import random


class DoubanBook:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')  # 设置为无头模式，即不显示浏览器
        # 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
        chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
        # 不加载图片,加快访问速度
        chrome_options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
        try:
            self.browser = webdriver.Chrome(
                executable_path='./chromedriver.exe',
                chrome_options=chrome_options)  # 设置chromedriver路径
            self.wait = WebDriverWait(self.browser, 20)  # 超时时长为10s
        except Exception as e:
            print(e)

    def parser(self, url, param):
        self.browser.get(url)
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, param)))
        html = self.browser.page_source
        doc = lxml.html.fromstring(html)
        return doc

    def get_book_all_type(self):  # 获取豆瓣所有书籍分类
        print('enter get')
        try:
            doc = self.parser('https://book.douban.com/tag/?view=cloud', '#content')
            all_type = doc.xpath('//*[@id="content"]/div/div[1]/div[2]/div/table/tbody/tr/td/*/text()')
            return all_type
        except Exception as err:
            print(err)

    def get_hot_comments(self, book_id):  # 获取某本书热短评
        try:
            url = 'https://book.douban.com/subject/{}/comments'.format(book_id)
            # print('url = ' + url)
            doc = self.parser(url, '#comments')
            # print('all doc = ')
            all_people = doc.xpath('//*[@id="comments"]/div[1]/ul/li/div[2]/h3/span[2]/a/text()')
            # print('all person = ')
            # print(all_people)
            people_num = len(all_people)
            all_comments = []
            for i in range(1, people_num+1):
                one_msg = []
                head_pic = doc.xpath('//*[@id="comments"]/div[1]/ul/li[{}]/div[1]/a/img/@src'.format(i))
                name = doc.xpath('//*[@id="comments"]/div[1]/ul/li[{}]/div[2]/h3/span[2]/a/text()'.format(i))
                comments = doc.xpath('//*[@id="comments"]/div[1]/ul/li[{}]/div[2]/p/span/text()'.format(i))
                like = doc.xpath('//*[@id="comments"]/div[1]/ul/li[{}]/div[2]/h3/span[1]/span/text()'.format(i))
                time = doc.xpath('//*[@id="comments"]/div[1]/ul/li[{}]/div[2]/h3/span[2]/span[2]/text()'.format(i))
                # print(head_pic)
                # print(name)
                # print(comments)
                # print(like)
                # print(time)
                one_msg.append(head_pic)
                one_msg.append(name)
                one_msg.append(time)
                one_msg.append(like)
                one_msg.append(comments)
                all_comments.append(one_msg)
            # print(all_comments)
            return all_comments

        except Exception as err:
            print(err)

    def get_book_list(self, book_type, page): # 返回某个类型的每页book list msg
        url = 'https://book.douban.com/tag/{}?start={}&type=T'.format(book_type, page)
        doc = self.parser(url, '#subject_list')
        book_list = []
        for i in range(1, 21):
            one_book_msg = []
            book_id = doc.xpath('//*[@id="subject_list"]/ul/li[{}]/div[1]/a/@onclick'.format(i))
            if not book_id:
                return one_book_msg
            book_id = str(book_id[0])
            book_id = book_id[book_id.index('subject_id:') + len('subject_id') + 2: book_id.index('from')-2]
            book_name = doc.xpath('//*[@id="subject_list"]/ul/li[{}]/div[2]/h2/a/text() '.format(i))
            if book_name:
                book_name = str(book_name[0]).replace(' ', '').replace('\n', '')
            score = doc.xpath('//*[@id="subject_list"]/ul/li[{}]/div[2]/div[2]/span[2]/text()'.format(i))
            if score:
                score = str(score[0])
            else:
                score = 0
            person_num = doc.xpath('//*[@id="subject_list"]/ul/li[{}]/div[2]/div[2]/span[3]/text()'.format(i))
            if person_num:
                person_num = str(person_num[0]).replace(' ', '').replace('\n', '')[1:-4]
            else:
                person_num = 0
            brief_msg = doc.xpath('//*[@id="subject_list"]/ul/li[{}]/div[2]/div[1]/text()'.format(i))
            if brief_msg:
                brief_msg = str(brief_msg[0]).replace(' ', '').replace('\n', '')
            one_book_msg.append(book_id)
            one_book_msg.append(book_name)
            one_book_msg.append(score)
            one_book_msg.append(person_num)
            one_book_msg.append(brief_msg)
            book_list.append(one_book_msg)
        return book_list

    def get_book_info(self, book_id):  # 返回book封面和页数
        url = 'https://book.douban.com/subject/{}/'.format(book_id)
        doc = self.parser(url, '#info')
        book_msg = []
        book_info = doc.xpath('//*[@id="info"]/text()')
        book_pic = doc.xpath('//*[@id="mainpic"]/a/img/@src')
        if book_pic:
            book_msg.append(book_pic[0])
        else:
            book_msg
        info_num = len(book_info)
        for i in range(0, info_num):
            page_num = str(book_info[i]).replace(' ', '')
            if page_num.isdigit() or page_num.find('页') != -1:
                book_msg.append(page_num)
                break
        return book_msg

    def get_book_content_brief(self, book_id):  # 获取内容简介
        url = 'https://book.douban.com/subject/{}/'.format(book_id)
        doc = self.parser(url, '#link-report')
        content_brief_short = doc.xpath('//*[@id="link-report"]/div[1]/div/p/text()')
        content_brief_full = doc.xpath('//*[@id="link-report"]/span[2]/div/div/p/text()')
        if len(content_brief_full):
            return content_brief_full
        elif len(content_brief_short):
            return content_brief_short
        else:
            return ""

    def get_book_author_brief(self, book_id):  # 获取作者简介
        url = 'https://book.douban.com/subject/{}/'.format(book_id)
        doc = self.parser(url, '#link-report')
        author_brief_short = doc.xpath('//*[@id="content"]/div/div[1]/div[3]/div[2]/div/div/p/text()')
        author_brief_full = doc.xpath('//*[@id="content"]/div/div[1]/div[3]/div[3]/span[2]/div/p/text()')
        author_brief = doc.xpath('//*[@id="content"]/div/div[1]/div[3]/div[3]/div/div/p/text()')
        brief1 = doc.xpath('//*[@id="content"]/div/div[1]/div[3]/div[2]/span[2]/div/p/text()')
        if len(author_brief_full):
            return author_brief_full
        elif len(author_brief_short):
            return author_brief_short
        elif len(author_brief):
            return author_brief
        elif len(brief1):
            return brief1
        else:
            return []

    def get_book_dir(self, book_id):  # 获取目录
        url = 'https://book.douban.com/subject/{}/'.format(book_id)
        doc = self.parser(url, '#dir_{}_short'.format(book_id))
        dir_short = doc.xpath('//*[@id="dir_{}_short"]/text()'.format(book_id))
        dir_full = doc.xpath('//*[@id="dir_{}_full"]/text()'.format(book_id))
        if len(dir_full):
            return dir_full
        elif len(dir_short):
            return dir_short
        else:
            return []

    def get_chrome_browser(self):  # 获取 browser
        return self.browser


