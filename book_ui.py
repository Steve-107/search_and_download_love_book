# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'book_ui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BookUI(object):
    def setupUi(self, BookUI):
        BookUI.setObjectName("BookUI")
        BookUI.resize(1340, 827)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(BookUI)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.groupBox = QtWidgets.QGroupBox(BookUI)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_13.setContentsMargins(-1, 5, -1, -1)
        self.horizontalLayout_13.setSpacing(10)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setMaximumSize(QtCore.QSize(41, 16777215))
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.lineEdit_type = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_type.setMinimumSize(QtCore.QSize(170, 25))
        self.lineEdit_type.setMaximumSize(QtCore.QSize(130, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.lineEdit_type.setFont(font)
        self.lineEdit_type.setObjectName("lineEdit_type")
        self.horizontalLayout_3.addWidget(self.lineEdit_type)
        self.pushButton_moreType = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_moreType.setMinimumSize(QtCore.QSize(50, 0))
        self.pushButton_moreType.setMaximumSize(QtCore.QSize(41, 33))
        self.pushButton_moreType.setStyleSheet("QPushButton {\n"
"    border-radius: 2px;\n"
"    color: white;\n"
"    padding: 3px 10px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-size: 14px;\n"
"    margin: 4px 1px;\n"
"    background-color: white;\n"
"    color: black;\n"
"    border: 1px solid #37a;\n"
"    \n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #37a;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #06AD56;\n"
"}")
        self.pushButton_moreType.setObjectName("pushButton_moreType")
        self.horizontalLayout_3.addWidget(self.pushButton_moreType)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setMaximumSize(QtCore.QSize(41, 16777215))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.lineEdit_score = QtWidgets.QComboBox(self.groupBox)
        self.lineEdit_score.setMinimumSize(QtCore.QSize(70, 25))
        self.lineEdit_score.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_score.setFont(font)
        self.lineEdit_score.setEditable(True)
        self.lineEdit_score.setObjectName("lineEdit_score")
        self.lineEdit_score.addItem("")
        self.lineEdit_score.addItem("")
        self.lineEdit_score.addItem("")
        self.lineEdit_score.addItem("")
        self.lineEdit_score.addItem("")
        self.lineEdit_score.addItem("")
        self.lineEdit_score.addItem("")
        self.lineEdit_score.addItem("")
        self.horizontalLayout_4.addWidget(self.lineEdit_score)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setMaximumSize(QtCore.QSize(31, 16777215))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setMaximumSize(QtCore.QSize(41, 16777215))
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.lineEdit_person = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_person.setMinimumSize(QtCore.QSize(90, 25))
        self.lineEdit_person.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.lineEdit_person.setFont(font)
        self.lineEdit_person.setObjectName("lineEdit_person")
        self.horizontalLayout_5.addWidget(self.lineEdit_person)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setMaximumSize(QtCore.QSize(31, 16777215))
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        spacerItem = QtWidgets.QSpacerItem(168, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.pushButton_search = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.pushButton_search.setFont(font)
        self.pushButton_search.setStyleSheet("QPushButton {\n"
"    border-radius: 4px;\n"
"    color: white;\n"
"    padding: 5px 50px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-size: 16px;\n"
"    margin: 4px 1px;\n"
"    background-color: white;\n"
"    color: black;\n"
"    border: 1px solid #37a;\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #37a;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #06AD56;\n"
"}")
        self.pushButton_search.setObjectName("pushButton_search")
        self.horizontalLayout_6.addWidget(self.pushButton_search)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_6)
        self.verticalLayout_6.addWidget(self.groupBox)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget_list = QtWidgets.QTableWidget(BookUI)
        self.tableWidget_list.setMinimumSize(QtCore.QSize(0, 300))
        self.tableWidget_list.setMaximumSize(QtCore.QSize(16777215, 5555))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tableWidget_list.setFont(font)
        self.tableWidget_list.setColumnCount(5)
        self.tableWidget_list.setObjectName("tableWidget_list")
        self.tableWidget_list.setRowCount(0)
        self.tableWidget_list.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_list.verticalHeader().setVisible(True)
        self.verticalLayout.addWidget(self.tableWidget_list)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_listPage = QtWidgets.QLabel(BookUI)
        self.label_listPage.setMinimumSize(QtCore.QSize(40, 0))
        self.label_listPage.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_listPage.setFont(font)
        self.label_listPage.setObjectName("label_listPage")
        self.horizontalLayout.addWidget(self.label_listPage)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.lineEdit_jumpPage = QtWidgets.QLineEdit(BookUI)
        self.lineEdit_jumpPage.setMaximumSize(QtCore.QSize(50, 23))
        self.lineEdit_jumpPage.setText("")
        self.lineEdit_jumpPage.setObjectName("lineEdit_jumpPage")
        self.horizontalLayout.addWidget(self.lineEdit_jumpPage)
        self.pushButton_jump = QtWidgets.QPushButton(BookUI)
        self.pushButton_jump.setMaximumSize(QtCore.QSize(50, 30))
        self.pushButton_jump.setStyleSheet("QPushButton {\n"
"    border-radius: 4px;\n"
"    color: white;\n"
"    padding: 20px 50px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-size: 14px;\n"
"    margin: 4px 1px;\n"
"    background-color: white;\n"
"    color: black;\n"
"    border: 1px solid #37a;\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #37a;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #06AD56;\n"
"}")
        self.pushButton_jump.setObjectName("pushButton_jump")
        self.horizontalLayout.addWidget(self.pushButton_jump)
        self.pushButton_firstPage = QtWidgets.QPushButton(BookUI)
        self.pushButton_firstPage.setMaximumSize(QtCore.QSize(50, 30))
        self.pushButton_firstPage.setStyleSheet("QPushButton {\n"
"    border-radius: 4px;\n"
"    color: white;\n"
"    padding: 20px 50px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-size: 14px;\n"
"    margin: 4px 1px;\n"
"    background-color: white;\n"
"    color: black;\n"
"    border: 1px solid #37a;\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #37a;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #06AD56;\n"
"}")
        self.pushButton_firstPage.setObjectName("pushButton_firstPage")
        self.horizontalLayout.addWidget(self.pushButton_firstPage)
        self.pushButton_prePage = QtWidgets.QPushButton(BookUI)
        self.pushButton_prePage.setMaximumSize(QtCore.QSize(50, 30))
        self.pushButton_prePage.setStyleSheet("QPushButton {\n"
"    border-radius: 4px;\n"
"    color: white;\n"
"    padding: 20px 50px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-size: 14px;\n"
"    margin: 4px 1px;\n"
"    background-color: white;\n"
"    color: black;\n"
"    border: 1px solid #37a;\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #37a;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #06AD56;\n"
"}")
        self.pushButton_prePage.setObjectName("pushButton_prePage")
        self.horizontalLayout.addWidget(self.pushButton_prePage)
        self.pushButton_nextPage = QtWidgets.QPushButton(BookUI)
        self.pushButton_nextPage.setMaximumSize(QtCore.QSize(50, 30))
        self.pushButton_nextPage.setStyleSheet("QPushButton {\n"
"    border-radius: 4px;\n"
"    color: white;\n"
"    padding: 20px 50px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-size: 14px;\n"
"    margin: 4px 1px;\n"
"    background-color: white;\n"
"    color: black;\n"
"    border: 1px solid #37a;\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #37a;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #06AD56;\n"
"}")
        self.pushButton_nextPage.setObjectName("pushButton_nextPage")
        self.horizontalLayout.addWidget(self.pushButton_nextPage)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_6.addLayout(self.verticalLayout)
        self.tabWidget = QtWidgets.QTabWidget(BookUI)
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 9999))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(9)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("QTabWidget::pane {\n"
"        border: none;\n"
"        border-top: 1px solid rgb(0, 160, 230);\n"
"\n"
"        background: transparent;\n"
"}\n"
"QTabWidget::tab-bar {  \n"
"        border: none;    \n"
"}\n"
"QTabBar::tab {\n"
"        border: none;\n"
"        border-top-left-radius: 4px;\n"
"        border-top-right-radius: 4px;\n"
"        color: rgb(0, 0, 0);\n"
"        background: rgb(255, 255, 255, 30);\n"
"        height: 28px;\n"
"        min-width: 85px;\n"
"        margin-right: 5px;\n"
"        padding-left: 5px;\n"
"        padding-right: 5px;\n"
"}\n"
"QTabBar::tab:hover {\n"
"   background: rgb(0, 0, 255, 40);\n"
"}\n"
"QTabBar::tab:selected {\n"
"        color: white;\n"
"        background: rgb(0, 160, 230);\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_contentBrief = QtWidgets.QWidget()
        self.tab_contentBrief.setObjectName("tab_contentBrief")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_contentBrief)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textBrowser_contentBrief = QtWidgets.QTextBrowser(self.tab_contentBrief)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(11)
        font.setKerning(True)
        self.textBrowser_contentBrief.setFont(font)
        self.textBrowser_contentBrief.setObjectName("textBrowser_contentBrief")
        self.verticalLayout_2.addWidget(self.textBrowser_contentBrief)
        self.tabWidget.addTab(self.tab_contentBrief, "")
        self.tab_authorBrief = QtWidgets.QWidget()
        self.tab_authorBrief.setObjectName("tab_authorBrief")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_authorBrief)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textBrowser_authorBrief = QtWidgets.QTextBrowser(self.tab_authorBrief)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(11)
        self.textBrowser_authorBrief.setFont(font)
        self.textBrowser_authorBrief.setStyleSheet("")
        self.textBrowser_authorBrief.setObjectName("textBrowser_authorBrief")
        self.verticalLayout_3.addWidget(self.textBrowser_authorBrief)
        self.tabWidget.addTab(self.tab_authorBrief, "")
        self.tab_hotComment = QtWidgets.QWidget()
        self.tab_hotComment.setObjectName("tab_hotComment")
        self.tabWidget.addTab(self.tab_hotComment, "")
        self.verticalLayout_6.addWidget(self.tabWidget)
        self.horizontalLayout_12.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.groupBox_bookMsg = QtWidgets.QGroupBox(BookUI)
        self.groupBox_bookMsg.setMinimumSize(QtCore.QSize(401, 300))
        self.groupBox_bookMsg.setMaximumSize(QtCore.QSize(452, 350))
        self.groupBox_bookMsg.setObjectName("groupBox_bookMsg")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_bookMsg)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_score = QtWidgets.QLabel(self.groupBox_bookMsg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_score.sizePolicy().hasHeightForWidth())
        self.label_score.setSizePolicy(sizePolicy)
        self.label_score.setMinimumSize(QtCore.QSize(72, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        self.label_score.setFont(font)
        self.label_score.setStyleSheet("QLabel\n"
"{\n"
"    rgb(73, 73, 73);\n"
"}")
        self.label_score.setText("")
        self.label_score.setObjectName("label_score")
        self.horizontalLayout_2.addWidget(self.label_score)
        self.label_person = QtWidgets.QLabel(self.groupBox_bookMsg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_person.sizePolicy().hasHeightForWidth())
        self.label_person.setSizePolicy(sizePolicy)
        self.label_person.setMinimumSize(QtCore.QSize(131, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.label_person.setFont(font)
        self.label_person.setStyleSheet("QLabel\n"
"{\n"
"    \n"
"    color: rgb(51, 119, 170);\n"
"}")
        self.label_person.setText("")
        self.label_person.setObjectName("label_person")
        self.horizontalLayout_2.addWidget(self.label_person)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)
        self.label_book_pic = QtWidgets.QLabel(self.groupBox_bookMsg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_book_pic.sizePolicy().hasHeightForWidth())
        self.label_book_pic.setSizePolicy(sizePolicy)
        self.label_book_pic.setMinimumSize(QtCore.QSize(200, 296))
        self.label_book_pic.setMaximumSize(QtCore.QSize(200, 296))
        self.label_book_pic.setBaseSize(QtCore.QSize(135, 198))
        self.label_book_pic.setText("")
        self.label_book_pic.setObjectName("label_book_pic")
        self.gridLayout.addWidget(self.label_book_pic, 0, 0, 2, 1)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.groupBox_bookMsg)
        self.label_4.setMinimumSize(QtCore.QSize(60, 20))
        self.label_4.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(102, 102, 102);")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        self.label_author = QtWidgets.QLabel(self.groupBox_bookMsg)
        self.label_author.setMinimumSize(QtCore.QSize(150, 20))
        self.label_author.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_author.setFont(font)
        self.label_author.setText("")
        self.label_author.setObjectName("label_author")
        self.horizontalLayout_7.addWidget(self.label_author)
        self.verticalLayout_8.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_bookMsg)
        self.label_9.setMinimumSize(QtCore.QSize(60, 20))
        self.label_9.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(102, 102, 102);")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_8.addWidget(self.label_9)
        self.label_pageNum = QtWidgets.QLabel(self.groupBox_bookMsg)
        self.label_pageNum.setMinimumSize(QtCore.QSize(150, 20))
        self.label_pageNum.setMaximumSize(QtCore.QSize(16555, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_pageNum.setFont(font)
        self.label_pageNum.setText("")
        self.label_pageNum.setObjectName("label_pageNum")
        self.horizontalLayout_8.addWidget(self.label_pageNum)
        self.verticalLayout_8.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_bookMsg)
        self.label_10.setMinimumSize(QtCore.QSize(60, 20))
        self.label_10.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(102, 102, 102);")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_9.addWidget(self.label_10)
        self.label_publisher = QtWidgets.QLabel(self.groupBox_bookMsg)
        self.label_publisher.setMinimumSize(QtCore.QSize(150, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_publisher.setFont(font)
        self.label_publisher.setText("")
        self.label_publisher.setObjectName("label_publisher")
        self.horizontalLayout_9.addWidget(self.label_publisher)
        self.verticalLayout_8.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox_bookMsg)
        self.label_11.setMinimumSize(QtCore.QSize(60, 20))
        self.label_11.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(102, 102, 102);")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_10.addWidget(self.label_11)
        self.label_publicYear = QtWidgets.QLabel(self.groupBox_bookMsg)
        self.label_publicYear.setMinimumSize(QtCore.QSize(150, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_publicYear.setFont(font)
        self.label_publicYear.setText("")
        self.label_publicYear.setObjectName("label_publicYear")
        self.horizontalLayout_10.addWidget(self.label_publicYear)
        self.verticalLayout_8.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox_bookMsg)
        self.label_12.setMinimumSize(QtCore.QSize(60, 20))
        self.label_12.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(102, 102, 102);")
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_11.addWidget(self.label_12)
        self.label_price = QtWidgets.QLabel(self.groupBox_bookMsg)
        self.label_price.setMinimumSize(QtCore.QSize(150, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_price.setFont(font)
        self.label_price.setText("")
        self.label_price.setObjectName("label_price")
        self.horizontalLayout_11.addWidget(self.label_price)
        self.verticalLayout_8.addLayout(self.horizontalLayout_11)
        self.gridLayout.addLayout(self.verticalLayout_8, 1, 1, 1, 1)
        self.verticalLayout_7.addWidget(self.groupBox_bookMsg)
        self.groupBox_5 = QtWidgets.QGroupBox(BookUI)
        self.groupBox_5.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.textBrowser_dir = QtWidgets.QTextBrowser(self.groupBox_5)
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(11)
        self.textBrowser_dir.setFont(font)
        self.textBrowser_dir.setObjectName("textBrowser_dir")
        self.verticalLayout_4.addWidget(self.textBrowser_dir)
        self.verticalLayout_7.addWidget(self.groupBox_5)
        self.verticalLayout_7.setStretch(1, 1)
        self.horizontalLayout_12.addLayout(self.verticalLayout_7)
        self.horizontalLayout_12.setStretch(0, 1)

        self.retranslateUi(BookUI)
        self.lineEdit_score.setCurrentIndex(2)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(BookUI)

    def retranslateUi(self, BookUI):
        _translate = QtCore.QCoreApplication.translate
        BookUI.setWindowTitle(_translate("BookUI", "豆瓣书籍"))
        self.groupBox.setTitle(_translate("BookUI", "搜索栏"))
        self.label.setText(_translate("BookUI", "类型："))
        self.lineEdit_type.setText(_translate("BookUI", "文学"))
        self.pushButton_moreType.setText(_translate("BookUI", "展开"))
        self.label_5.setText(_translate("BookUI", "评分："))
        self.lineEdit_score.setItemText(0, _translate("BookUI", "6.0"))
        self.lineEdit_score.setItemText(1, _translate("BookUI", "6.5"))
        self.lineEdit_score.setItemText(2, _translate("BookUI", "7.0"))
        self.lineEdit_score.setItemText(3, _translate("BookUI", "7.5"))
        self.lineEdit_score.setItemText(4, _translate("BookUI", "8.0"))
        self.lineEdit_score.setItemText(5, _translate("BookUI", "8.5"))
        self.lineEdit_score.setItemText(6, _translate("BookUI", "9.0"))
        self.lineEdit_score.setItemText(7, _translate("BookUI", "9.5"))
        self.label_6.setText(_translate("BookUI", "以上"))
        self.label_7.setText(_translate("BookUI", "人数："))
        self.lineEdit_person.setText(_translate("BookUI", "500"))
        self.label_8.setText(_translate("BookUI", "以上"))
        self.pushButton_search.setText(_translate("BookUI", "搜索"))
        self.label_listPage.setText(_translate("BookUI", "第 1 页"))
        self.pushButton_jump.setText(_translate("BookUI", "调转"))
        self.pushButton_firstPage.setText(_translate("BookUI", "首页"))
        self.pushButton_prePage.setText(_translate("BookUI", "上页"))
        self.pushButton_nextPage.setText(_translate("BookUI", "下页"))
        self.textBrowser_contentBrief.setHtml(_translate("BookUI", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'宋体\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_contentBrief), _translate("BookUI", "内容简介"))
        self.textBrowser_authorBrief.setHtml(_translate("BookUI", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'宋体\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-size:9pt;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_authorBrief), _translate("BookUI", "作者简介"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_hotComment), _translate("BookUI", "热门短评"))
        self.groupBox_bookMsg.setTitle(_translate("BookUI", "书籍详情"))
        self.label_4.setText(_translate("BookUI", "作  者:"))
        self.label_9.setText(_translate("BookUI", "页  数:"))
        self.label_10.setText(_translate("BookUI", "出版社:"))
        self.label_11.setText(_translate("BookUI", "出版年:"))
        self.label_12.setText(_translate("BookUI", "出  价:"))
        self.groupBox_5.setTitle(_translate("BookUI", "目录"))
        self.textBrowser_dir.setHtml(_translate("BookUI", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun-ExtB\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))

