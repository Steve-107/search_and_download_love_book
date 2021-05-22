import sys
import webbrowser
from PyQt5 import QtWidgets, QtCore
from book_ui import Ui_BookUI
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from book import *
from PyQt5.QtWidgets import *
import requests
import _thread
from requests import Response
from sheetstyle import *
from PyQt5.QtWebEngineWidgets import *
import time
from selenium import webdriver
from threading import Timer
import os


class MyForm(QtWidgets.QWidget, Ui_BookUI):
    signal_set_book_info = QtCore.pyqtSignal(Response, str, str)
    signal_set_book_dir = QtCore.pyqtSignal(list)
    signal_set_book_content_brief = QtCore.pyqtSignal(list)
    signal_set_book_author_brief = QtCore.pyqtSignal(list)
    signal_set_book_hot_comments = QtCore.pyqtSignal(list)
    signal_set_book_type = QtCore.pyqtSignal(list)
    signal_set_book_load_msg = QtCore.pyqtSignal(list, list)
    html = None
    show_all_type_widget = QWidget
    radio_btn_list = []
    load_line_btn_list = []
    search_null_time = 0
    check_book_name = ''
    browser_wait_timeout = 5
    timeout_flag = False

    def __init__(self):
        super(MyForm, self).__init__()
        self.setupUi(self)

    def closeEvent(self, evnt):
        my_book.browser.quit()
        os.system('taskkill /im chromedriver.exe /F')
        os.system('taskkill /im chrome.exe /F')
        super(MyForm, self).closeEvent(evnt)


def init_ui():
    header = ['书名', '评分', '同类排名', '评分人数', '书籍信息']
    my_form.tableWidget_list.setHorizontalHeaderLabels(header)
    my_form.tableWidget_list.setColumnWidth(0, 230)
    my_form.label_listPage.hide()
    my_form.setWindowIcon(QIcon("./book.ico"))


def filter_book_list(book_list):  # 过滤不满足我们设定的评分和人数的book
    after_list = []
    list_num = len(book_list)
    for i in range(0, list_num):
        if float(book_list[i][2]) >= float(my_form.lineEdit_score.currentText()) and int(book_list[i][3]) >= int(my_form.lineEdit_person.text()):
            after_list.append(book_list[i])
    return after_list


def search_book_list(book_type, page, is_next_page_search):  # 搜索要求的一页（每页20个item）
    try:
        my_form.tableWidget_list.setRowCount(0)
        if not book_type or not page:
            return
        set_enable(False)       # 设置不可点击
        my_form.tableWidget_list.clearContents()
        book_list = my_book.get_book_list(book_type, (page-1)*20)
        book_list = filter_book_list(book_list)
        row_num = len(book_list)
        # 设置页数
        my_form.label_listPage.setText("    第 " + str(page) + " 页")
        my_form.label_listPage.show()
        QApplication.processEvents()
        if not row_num:
            time.sleep(1)
            my_form.search_null_time += 1
            if my_form.search_null_time == 30:
                QMessageBox.about(my_form, '搜索结果', "未搜到符合要求的内容!    ")
                set_enable(True)  # 设置可点击
                my_form.search_null_time = 0
                return
            print('第{}次 search'.format(my_form.search_null_time))
            if is_next_page_search:
                search_book_list(book_type, page + my_form.search_null_time, True)
            else:
                search_book_list(book_type, page - my_form.search_null_time, False)
            # QMessageBox.about(my_form, '搜索结果', "未搜到内容!   ")
            # my_form.label_listPage.hide()
        else:
            my_form.search_null_time = 0
            my_form.tableWidget_list.setRowCount(row_num)
            for row in range(0, row_num):
                for col in range(1, 6):
                    if col < 3:
                        item = QTableWidgetItem(book_list[row][col])
                        if col == 1:
                            item.setWhatsThis(book_list[row][0])  # 设置book_id
                    elif col == 3:
                        item = QTableWidgetItem(str(row+1 + (page-1)*row_num))
                    else:
                        item = QTableWidgetItem(book_list[row][col - 1])
                    my_form.tableWidget_list.setItem(row, col - 1, item)
                    my_form.tableWidget_list.item(row, 0).setForeground(QColor(51, 119, 170))
                    my_form.tableWidget_list.item(row, col-1).setTextAlignment(Qt.AlignCenter)
            set_enable(True)  # 设置可点击
    except Exception as e:
        print(e)


def get_book_info(book_id, book_name):  # 获取书籍的其他信息
    try:
        book_info = my_book.get_book_info(book_id)
        if not book_info:
            return
        url = str(book_info[0])
        req = requests.get(url)
        my_form.signal_set_book_info.emit(req, "" if not len(book_info[1]) else book_info[1], book_name)
    except Exception as e:
        print(e)


def show_book_info(req, page_num, book_name):
    try:
        pic = QPixmap()
        pic.loadFromData(req.content)
        my_form.label_book_pic.setPixmap(pic)
        my_form.label_book_pic.setScaledContents(True)
        my_form.label_pageNum.setText(page_num)

    except Exception as e:
        print(e)


def get_book_dir(book_id):  # 获取目录
    try:
        book_dir = my_book.get_book_dir(book_id)
        if not book_dir:
            return
        my_form.signal_set_book_dir.emit(book_dir)
    except Exception as e:
        print(e)


def show_book_dir(book_dir):
    try:
        num = len(book_dir)
        for i in range(0, num-2):
            my_form.textBrowser_dir.append(book_dir[i])
    except Exception as e:
        print(e)


def get_book_content_brief(book_id):  # 获取内容简介
    try:
        book_content = my_book.get_book_content_brief(book_id)
        if not book_content:
            return
        my_form.signal_set_book_content_brief.emit(book_content)
    except Exception as e:
        print(e)


def show_book_content_brief(book_content):
    try:
        text = "<html><body>"
        text += "<style type='text/css'>p { margin-bottom:20px; }</style><br>"
        for dir_line in book_content:
            text += "<p>{}</p>".format(dir_line)
        text += "</body></html>"
        my_form.textBrowser_contentBrief.setHtml(text)
    except Exception as e:
        print(e)


def get_book_author_brief(book_id):  # 获取作者简介
    try:
        book_author_brief = my_book.get_book_author_brief(book_id)
        if not book_author_brief:
            print('check_book_name = ' + my_form.check_book_name)
            _thread.start_new_thread(get_book_load_msg, (my_form.check_book_name,))
            return
        my_form.signal_set_book_author_brief.emit(book_author_brief)
    except Exception as e:
        _thread.start_new_thread(get_book_load_msg, (my_form.check_book_name,))
        print(e)


def show_book_author_brief(book_author_brief):
    try:
        text = "<html><body>"
        text += "<style type='text/css'>p { margin-bottom:20px; }</style><br>"
        for dir_line in book_author_brief:
            text += "<p>{}</p>".format(dir_line)
        text += "</body></html>"
        my_form.textBrowser_authorBrief.setHtml(text)
        print('check_book_name = '+ my_form.check_book_name)
        _thread.start_new_thread(get_book_load_msg, (my_form.check_book_name,))
    except Exception as e:
        print(e)


def show_book_other_info(table_row):  # 解析tabelWidget第5列的信息
    info = my_form.tableWidget_list.item(table_row, 4).text().split('/')
    book_person = my_form.tableWidget_list.item(table_row, 3).text()
    book_score = my_form.tableWidget_list.item(table_row, 1).text()
    num = len(info)
    money = info[num-1]
    public_year = info[num-2]
    publisher = info[num-3]
    author = ""
    for i in range(0, num-3):
        author += info[i]
    my_form.label_author.setText(author)
    my_form.label_publisher.setText(publisher)
    my_form.label_publicYear.setText(public_year)
    my_form.label_price.setText(money)
    my_form.label_score.setText(book_score)
    my_form.label_person.setText(book_person+'人评分')


def get_book_hot_comments(book_id):  # 获取热门短片
    try:
        book_hot_comments = my_book.get_hot_comments(book_id)
        if not book_hot_comments:
            return
        my_form.signal_set_book_hot_comments.emit(book_hot_comments)
    except Exception as e:
        print(e)


def show_book_hot_comment(book_hot_comments):  # 通过加载sheetstyle.py的css和html字符串变量设置UI
    try:
        hot_comments_html = comments_css
        for one_comment in book_hot_comments:
            head_pic = "" if not len(one_comment[0]) else one_comment[0][0]
            name = "" if not len(one_comment[1]) else one_comment[1][0]
            time = "" if not len(one_comment[2]) else one_comment[2][0]
            like = "" if not len(one_comment[3]) else one_comment[3][0]
            comments = "" if not len(one_comment[4]) else one_comment[4][0]
            temp = comments_html.format(head_pic, name, time, like, comments)
            hot_comments_html += temp
        # print(hot_comments_html)
        count = my_form.tabWidget.count()
        while count > 2:
            my_form.tabWidget.removeTab(count-1)
            count -= 1
        tab_hot_comment = QWidget()
        my_form.tabWidget.addTab(tab_hot_comment, "热门短评")
        browser = QWebEngineView()
        layout = QHBoxLayout(tab_hot_comment)
        browser.setHtml(hot_comments_html)
        layout.addWidget(browser)
        my_form.tabWidget.setCurrentIndex(2)
        QApplication.processEvents()

    except Exception as e:
        print(e)


def show_book_msg(row):  # 点击tableWidget cell后进入各个线程获取书本各信息，并果通过信号发给show api显示UI
    try:
        my_form.textBrowser_contentBrief.clear()
        my_form.textBrowser_dir.clear()
        my_form.textBrowser_authorBrief.clear()
        my_form.label_book_pic.clear()
        book_id = my_form.tableWidget_list.item(row, 0).whatsThis()  # 获取book_id

        set_enable(False)
        my_form.check_book_name = my_form.tableWidget_list.item(row, 0).text()
        get_book_hot_comments(book_id)
        _thread.start_new_thread(get_book_dir, (book_id,))
        _thread.start_new_thread(get_book_info, (book_id, my_form.tableWidget_list.item(row, 0).text()))
        _thread.start_new_thread(get_book_content_brief, (book_id,))
        _thread.start_new_thread(get_book_author_brief, (book_id,))
        show_book_other_info(row)

        my_form.update()

    except Exception as e:
        print(e)


def get_all_book_type(): # 获取豆瓣所有书本类型
    my_form.pushButton_moreType.setEnabled(False)
    try:
        all_type = my_book.get_book_all_type()
        my_form.signal_set_book_type.emit(all_type)
    except Exception as err:
        print(err)


def raido_btn_click_slot():  # 展开项里点击了某个数本类型后的事件
    for btn in my_form.radio_btn_list:
        if btn.isChecked():
            text = btn.text()
            my_form.lineEdit_type.setText(text[:text.index('(')])
    my_form.show_all_type_widget.hide()
    clear_type_btn_checked(my_form.radio_btn_list)
    my_form.pushButton_search.click()


def clear_type_btn_checked(btn_list):
    for btn in btn_list:
        if btn.isChecked():
            btn.setChecked(False)


def show_all_book_type(all_type):  # 书本所有类型GUI
    try:
        if not len(all_type):
            return
        my_form.show_all_type_widget = QWidget()
        my_form.show_all_type_widget.setWindowIcon(QIcon("./book.ico"))
        layout = QGridLayout(my_form.show_all_type_widget)
        type_num = len(all_type)
        for i in range(0, type_num):
            if i % 2 == 0:
                radio_btn = QPushButton(all_type[i] + all_type[i+1])
                my_form.radio_btn_list.append(radio_btn)
                radio_btn.setCheckable(True)
                radio_btn.clicked.connect(raido_btn_click_slot)
                radio_btn.setStyleSheet(book_type_style)
                layout.addWidget(radio_btn, int(i/12), int(i/2 % 6))
        my_form.pushButton_moreType.setEnabled(True)
        my_form.pushButton_search.click()

    except Exception as err:
        print(err)


def show_all_type_widget():
    try:
        desktop_center = QDesktopWidget().availableGeometry().center()
        qr = my_form.show_all_type_widget.frameGeometry()
        qr.moveCenter(desktop_center)
        my_form.show_all_type_widget.setWindowTitle('选择类型')
        my_form.show_all_type_widget.show()
        my_form.pushButton_moreType.setEnabled(True)
    except Exception as err:
        print(err)


def signal_init():
    # 搜索按钮
    my_form.pushButton_search.clicked.connect(lambda: search_book_list(my_form.lineEdit_type.text(), 1, True))
    # 跳转按钮
    my_form.pushButton_jump.clicked.connect(lambda: search_book_list(my_form.lineEdit_type.text(),
                                                                     0 if not my_form.lineEdit_jumpPage.text()
                                                                     else int(my_form.lineEdit_jumpPage.text()), True))
    # list 单元格点击信号
    my_form.tableWidget_list.cellClicked.connect(lambda: show_book_msg(my_form.tableWidget_list.currentRow()))
    # 首页
    my_form.pushButton_firstPage.clicked.connect(my_form.pushButton_search.clicked)
    # 前一页
    my_form.pushButton_prePage.clicked.connect(lambda: search_book_list(my_form.lineEdit_type.text(),
                                              int(my_form.label_listPage.text()[my_form.label_listPage.text().index('第') + 2:
                                              my_form.label_listPage.text().index('页')-1]) - 1, False))
    # 后一页
    my_form.pushButton_nextPage.clicked.connect(lambda: search_book_list(my_form.lineEdit_type.text(),
                                              int(my_form.label_listPage.text()[my_form.label_listPage.text().index('第') + 2:
                                              my_form.label_listPage.text().index('页')-1]) + 1, True))

    # 展开
    my_form.pushButton_moreType.clicked.connect(show_all_type_widget)
    my_form.signal_set_book_info.connect(show_book_info)
    my_form.signal_set_book_dir.connect(show_book_dir)
    my_form.signal_set_book_content_brief.connect(show_book_content_brief)
    my_form.signal_set_book_author_brief.connect(show_book_author_brief)
    my_form.signal_set_book_hot_comments.connect(show_book_hot_comment)
    my_form.signal_set_book_type.connect(show_all_book_type)
    my_form.signal_set_book_load_msg.connect(show_book_load_msg)


def set_enable(flag):
    my_form.groupBox.setEnabled(flag)
    my_form.tableWidget_list.setEnabled(flag)
    my_form.pushButton_jump.setEnabled(flag)
    my_form.pushButton_nextPage.setEnabled(flag)
    my_form.pushButton_firstPage.setEnabled(flag)
    my_form.pushButton_prePage.setEnabled(flag)
    if flag:
        my_form.setCursor(Qt.ArrowCursor)  # 设置鼠标arrow状态
    else:
        my_form.setCursor(Qt.BusyCursor)  # 设置鼠标busy状态


def get_book_load_msg(book_name):
    print('book_name = {}'.format(book_name))
    browser = my_book.get_chrome_browser()
    browser.get('https://www.jiumodiary.com/')
    browser.find_element_by_id('SearchWord').send_keys(book_name)
    time.sleep(1)
    browser.find_element_by_id('SearchButton').click()  # 成功
    resource_name = []
    resource_href = []
    my_form.timeout_flag = False
    timer = Timer(my_form.browser_wait_timeout, timer_func)  # 首次启动
    timer.start()
    while not len(resource_name):
        if my_form.timeout_flag:
            my_form.signal_set_book_load_msg.emit(resource_name, resource_href)
            return
        html = browser.page_source
        doc = lxml.html.fromstring(html)
        resource_name = doc.xpath('//*[@id="result-ul"]/div/a/@data-title')
    resource_href = doc.xpath('//*[@id="result-ul"]/div/a/@data-href')
    my_form.signal_set_book_load_msg.emit(resource_name, resource_href)


def timer_func():
    my_form.timeout_flag = True


def show_book_load_msg(name_list, href_list):
    tab_load = QWidget()
    my_form.tabWidget.addTab(tab_load, "下载信息")
    if len(name_list) != len(href_list):
        set_enable(True)
        my_form.is_showed_load_msg = True
        return
    layout = QVBoxLayout(tab_load)
    layout.setSpacing(0)
    load_num = len(name_list)
    my_form.load_line_btn_list.clear()
    for i in range(0, load_num):
        line_btn = QPushButton(name_list[i])
        my_form.load_line_btn_list.append(line_btn)
        line_btn.setCheckable(True)
        line_btn.setToolTip(href_list[i])
        line_btn.clicked.connect(load_line_btn_clicked_slot)
        line_btn.setStyleSheet(load_msg_style)
        layout.addWidget(line_btn)
    my_form.is_showed_load_msg = True
    set_enable(True)


def load_line_btn_clicked_slot():
    print("enter click slot")
    for btn in my_form.load_line_btn_list:
        if btn.isChecked():
            print("enter cheked")
            browser = webdriver.Chrome()
            browser.get(btn.toolTip())
    clear_type_btn_checked(my_form.load_line_btn_list)


if __name__ == '__main__':
    try:
        app = QtWidgets.QApplication(sys.argv)
        my_form = MyForm()
        my_book = DoubanBook()
        init_ui()
        signal_init()
        my_form.show()
        _thread.start_new_thread(get_all_book_type, ())
        sys.exit(app.exec_())
    except Exception as e:
        print(e)