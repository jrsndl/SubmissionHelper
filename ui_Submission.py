# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'submission.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import ui_images_rc

class Ui_submission(object):
    def setupUi(self, submission):
        if not submission.objectName():
            submission.setObjectName(u"submission")
        submission.resize(1297, 615)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(submission.sizePolicy().hasHeightForWidth())
        submission.setSizePolicy(sizePolicy)
        submission.setMinimumSize(QSize(800, 600))
        submission.setAcceptDrops(True)
        icon = QIcon()
        icon.addFile(u":/images/folder.png", QSize(), QIcon.Normal, QIcon.Off)
        submission.setWindowIcon(icon)
        submission.setAutoFillBackground(False)
        submission.setStyleSheet(u"QLabel\n"
"{\n"
"    font-size: 10pt;\n"
"}\n"
"\n"
"QCheckBox\n"
"{\n"
"    font-size: 10pt;\n"
"}\n"
"\n"
"QRadioButton\n"
"{\n"
"    font-size: 10pt;\n"
"}\n"
"\n"
"\n"
"\n"
"QListView:item:hover\n"
"{\n"
" border-style: none; \n"
" background-color: #4d4d4d;\n"
"}\n"
"\n"
"QGroupBox\n"
"{\n"
"    font-weight: bold;\n"
"    border: 1px solid gray; \n"
"    border-radius: 8px;\n"
"    margin-top: 6px;\n"
"   /* border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;*/\n"
"}\n"
"\n"
"QGroupBox::title\n"
"{\n"
"   /* background-color: transparent;*/\n"
"   /* subcontrol-position: top left;*/\n"
"    \n"
"    subcontrol-origin: margin;\n"
"    padding:0px 5px;\n"
"}\n"
"\n"
"\n"
"QToolTip\n"
"{\n"
"     border: 0px solid black;\n"
"     background-color: #ffa02f;\n"
"     padding: 0px;\n"
"     border-radius: 2px;\n"
"     opacity: 100;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"	font-size: 10pt;\n"
"\n"
"}\n"
"\n"
"QWidget:item:h"
                        "over\n"
"{\n"
"    background-color: gray;\n"
"}\n"
"\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    background: #444;\n"
"    border: 1px solid #000;\n"
"    background-color: QLinearGradient(\n"
"        x1:0, y1:0,\n"
"        x2:0, y2:1,\n"
"        stop:1 #212121,\n"
"        stop:0.4 #343434/*,\n"
"        stop:0.2 #343434,\n"
"        stop:0.1 #ffaa00*/\n"
"    );\n"
"    margin-bottom:-1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"QMenu\n"
"{\n"
"    border: 1px solid #000;\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 2px 20px 2px 20px;\n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #404040;\n"
"    b"
                        "ackground-color: #323232;\n"
"}\n"
"\n"
"QAbstractItemView\n"
"{\n"
"   /* background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0.1 #646464, stop: 1 #5d5d5d);*/\n"
"  background-color: #4d4d4d\n"
"}\n"
"\n"
"QTextWidget\n"
"{\n"
"    background-color: #4d4d4d\n"
"}\n"
"\n"
"QWidget:focus\n"
"{\n"
"    /*border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);*/\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 2;\n"
"    padding-left: 16px;\n"
"\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    bo"
                        "rder-style: solid;\n"
"    border-radius: 4;\n"
"    padding: 3px;\n"
"    font-size: 16px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"	outline: 0;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"}\n"
"\n"
"QPushButton:checked\n"
"{\n"
"	\n"
"	background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #946223, stop: 0.1 #905f22, stop: 0.5 #885a20, stop: 0.9 #80551e, stop: 1 #7d531e);\n"
"}\n"
"\n"
"QPushButton:focus\n"
"{\n"
"\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #ffaa00;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 2;\n"
"	padding-left: 16px;\n"
"\n"
"\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton"
                        ":hover\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 3px;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: #ffaa00;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    border: 2px solid darkgray;\n"
"    /*selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);*/\n"
"    selection-background-color: #ffa02f;\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 15px;\n"
"\n"
"     border-left-width: 0px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-ra"
                        "dius: 3px;\n"
" }\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"     image: url(:images/down_arrow.png);\n"
"}\n"
"\n"
"/*\n"
"QComboBox::up-arrow\n"
"{\n"
"     image: url(:images/up_arrow.png);\n"
"}\n"
"*/\n"
"QGroupBox:focus\n"
"{\n"
"  border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QTextEdit:focus\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"     border:  solid #222222;\n"
"     background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"     height: 7px;\n"
"     margin: 0px 16px 0 16px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"      border: 1"
                        "px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #121212, stop: 0.2 #282828, stop"
                        ": 1 #484848);\n"
"      width: 7px;\n"
"      margin: 16px 0 16px 0;\n"
"      border: 1px solid #222222;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      height: 14px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d7801a, stop: 1 #ffa02f);\n"
"      height: 14px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollB"
                        "ar::down-arrow:vertical\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    /*           table headers */\n"
"\n"
"    /*background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);*/\n"
"    background-color: #242424;\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QCheckBox:disabled\n"
"{\n"
"color: #414141;\n"
"}\n"
"\n"
"QDockWidget::title\n"
"{\n"
"    text-align: center;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #24"
                        "2424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button, QDockWidget::float-button\n"
"{\n"
"    text-align: center;\n"
"    spacing: 1px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button:hover, QDockWidget::float-button:hover\n"
"{\n"
"    background: #242424;\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed, QDockWidget::float-button:pressed\n"
"{\n"
"    padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #4c4c4c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d7801a, stop:0."
                        "5 #b56c17 stop:1 #ffa02f);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QToolBar::handle\n"
"{\n"
"     spacing: 3px; /* spacing between items in the tool bar */\n"
"     background: url(:images/handle.png);\n"
"}\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 2px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QProgressBar\n"
"{\n"
"    border: 2px solid grey;\n"
"    border-radius: 3px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: #d7801a;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #444;\n"
"    border-bottom-style: none;\n"
"    background-color: #323232"
                        ";\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 3px;\n"
"    padding-bottom: 2px;\n"
"    margin-right: -1px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #444;\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabBar::tab:last\n"
"{\n"
"    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:first:!selected\n"
"{\n"
" margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */\n"
"\n"
"\n"
"    border-top-left-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    border-bottom-style: solid;\n"
"    margin-top: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    margin-bottom: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover\n"
"{\n"
"    /*bord"
                        "er-top: 2px solid #ffaa00;\n"
"    padding-bottom: 3px;*/\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 #ffaa00);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked\n"
"{\n"
"    background-color: qradialgradient(\n"
"        cx: 0.5, cy: 0.5,\n"
"        fx: 0.5, fy: 0.5,\n"
"        radius: 1.0,\n"
"        stop: 0.25 #ffaa00,\n"
"        stop: 0.3 #323232\n"
"    );\n"
"}\n"
"\n"
"QRadioButton::indicator\n"
"{\n"
"    border-radius: 1px;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover, QCheckBox::indicator:hover\n"
"{\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    borde"
                        "r: 1px solid #b1b1b1;\n"
"    width: 9px;\n"
"    height: 9px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(:images/checkbox_checked.png);\n"
"    /*color: #ffaa00;*/\n"
"    /*background-color:#ffaa00;*/\n"
"}\n"
"\n"
"QRadioButton::indicator:disabled\n"
"{\n"
"    border: 1px solid #444;\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled\n"
"{\n"
"    border: 1px solid #444;\n"
"    /*image:url(:images/checkbox.png);*/\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:disabled\n"
"{\n"
"    border: 1px solid #444;\n"
"    image:url(:images/checkbox_disabled.png);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QSpinBox\n"
"{\n"
"    selection-background-color: #ffaa00;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius:2;\n"
"}\n"
"QAbstractSpinBox\n"
"{\n"
"    selection-background-color: #ffaa00;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, sto"
                        "p: 0 #646464, stop: 1 #5d5d5d);\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius:2;\n"
"}\n"
"\n"
"QSpinBox::up-arrow\n"
"{\n"
"	background-image: url(:images/up_arrow.png);\n"
"    width: 7px; height: 5px;\n"
"}\n"
"QAbstractSpinBox::up-arrow\n"
"{\n"
"	background-image: url(:images/up_arrow.png);\n"
"    width: 7px; height: 5px;\n"
"}\n"
"\n"
"QSpinBox::down-arrow\n"
"{\n"
"	background-image: url(:images/down_arrow.png);\n"
"     width: 7px; height: 5px;\n"
"}\n"
"QAbstractSpinBox::down-arrow\n"
"{\n"
"	background-image: url(:images/down_arrow.png);\n"
"     width: 7px; height: 5px;\n"
"}\n"
"\n"
"QSpinBox::up-button \n"
"{\n"
"    border-width: 0px;\n"
"}\n"
"QAbstractSpinBox::up-button \n"
"{\n"
"    border-width: 0px;\n"
"}\n"
"QSpinBox::down-button \n"
"{\n"
"    border-width: 0px;\n"
"}\n"
"QAbstractSpinBox::down-button \n"
"{\n"
"    border-width: 0px;\n"
"}\n"
"\n"
"QDoubleSpinBox\n"
"{\n"
"    selection-background-color: #ffaa00;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0,"
                        " y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius:2;\n"
"}\n"
"\n"
"QDoubleSpinBox::up-arrow\n"
"{\n"
"	background-image: url(:images/up_arrow.png);\n"
"    width: 7px; height: 5px;\n"
"\n"
"}\n"
"\n"
"QDoubleSpinBox::down-arrow\n"
"{\n"
"	background-image: url(:images/down_arrow.png);\n"
"     width: 7px; height: 5px;\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button \n"
"{\n"
"    border-width: 0px;\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button \n"
"{\n"
"    border-width: 0px;\n"
"}\n"
"\n"
"QCalendarWidget::prevmonth\n"
"{\n"
"	background-image: url(:images/left_arrow.png);\n"
"}\n"
"QCalendarWidget::nextmonth\n"
"{\n"
"	background-image: url(:images/right_arrow.png);\n"
"}\n"
"QCalendarWidget\n"
"{\n"
"	 background-color: #242424;\n"
"    color: white;\n"
"}\n"
"\n"
"")
        submission.setDocumentMode(False)
        submission.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QWidget(submission)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(800, 580))
        self.centralwidget.setMaximumSize(QSize(16000, 16777215))
        self.verticalLayout_50 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.TopTab = QTabWidget(self.centralwidget)
        self.TopTab.setObjectName(u"TopTab")
        sizePolicy.setHeightForWidth(self.TopTab.sizePolicy().hasHeightForWidth())
        self.TopTab.setSizePolicy(sizePolicy)
        self.TopTab.setMinimumSize(QSize(780, 340))
        self.TopTab.setMaximumSize(QSize(16777215, 350))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_50 = QHBoxLayout(self.tab)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.groupBox.setMinimumSize(QSize(600, 60))
        self.groupBox.setMaximumSize(QSize(16777215, 60))
        self.groupBox.setBaseSize(QSize(631, 70))
        self.groupBox.setFlat(False)
        self.verticalLayout_7 = QVBoxLayout(self.groupBox)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.package_folder = QLineEdit(self.groupBox)
        self.package_folder.setObjectName(u"package_folder")
        sizePolicy1.setHeightForWidth(self.package_folder.sizePolicy().hasHeightForWidth())
        self.package_folder.setSizePolicy(sizePolicy1)
        self.package_folder.setMinimumSize(QSize(250, 25))
        self.package_folder.setMaximumSize(QSize(16000, 16777215))
        self.package_folder.setDragEnabled(True)

        self.horizontalLayout_4.addWidget(self.package_folder)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.package_explore = QPushButton(self.groupBox)
        self.package_explore.setObjectName(u"package_explore")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.package_explore.sizePolicy().hasHeightForWidth())
        self.package_explore.setSizePolicy(sizePolicy2)
        self.package_explore.setMinimumSize(QSize(20, 25))
        self.package_explore.setAutoFillBackground(False)
        icon1 = QIcon()
        icon1.addFile(u":/images/system-search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.package_explore.setIcon(icon1)
        self.package_explore.setFlat(True)

        self.horizontalLayout_5.addWidget(self.package_explore)

        self.package_browse = QPushButton(self.groupBox)
        self.package_browse.setObjectName(u"package_browse")
        sizePolicy2.setHeightForWidth(self.package_browse.sizePolicy().hasHeightForWidth())
        self.package_browse.setSizePolicy(sizePolicy2)
        self.package_browse.setMinimumSize(QSize(60, 25))
        self.package_browse.setMaximumSize(QSize(60, 24))
        self.package_browse.setAutoFillBackground(False)
        self.package_browse.setIcon(icon)
        self.package_browse.setFlat(True)

        self.horizontalLayout_5.addWidget(self.package_browse)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_5)


        self.verticalLayout_7.addLayout(self.horizontalLayout_4)


        self.verticalLayout_33.addWidget(self.groupBox)

        self.groupBox_8 = QGroupBox(self.tab)
        self.groupBox_8.setObjectName(u"groupBox_8")
        sizePolicy1.setHeightForWidth(self.groupBox_8.sizePolicy().hasHeightForWidth())
        self.groupBox_8.setSizePolicy(sizePolicy1)
        self.groupBox_8.setMinimumSize(QSize(600, 190))
        self.horizontalLayout_92 = QHBoxLayout(self.groupBox_8)
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.verticalLayout_53 = QVBoxLayout()
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.label_10 = QLabel(self.groupBox_8)
        self.label_10.setObjectName(u"label_10")
        sizePolicy2.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy2)
        self.label_10.setMinimumSize(QSize(75, 25))
        self.label_10.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_46.addWidget(self.label_10)

        self.name_template = QLineEdit(self.groupBox_8)
        self.name_template.setObjectName(u"name_template")
        sizePolicy1.setHeightForWidth(self.name_template.sizePolicy().hasHeightForWidth())
        self.name_template.setSizePolicy(sizePolicy1)
        self.name_template.setMinimumSize(QSize(230, 25))
        self.name_template.setMaximumSize(QSize(16000, 25))

        self.horizontalLayout_46.addWidget(self.name_template)


        self.horizontalLayout_49.addLayout(self.horizontalLayout_46)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_37 = QLabel(self.groupBox_8)
        self.label_37.setObjectName(u"label_37")
        sizePolicy2.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy2)
        self.label_37.setMinimumSize(QSize(75, 25))
        self.label_37.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_16.addWidget(self.label_37)

        self.name_date_regex = QLineEdit(self.groupBox_8)
        self.name_date_regex.setObjectName(u"name_date_regex")
        sizePolicy1.setHeightForWidth(self.name_date_regex.sizePolicy().hasHeightForWidth())
        self.name_date_regex.setSizePolicy(sizePolicy1)
        self.name_date_regex.setMinimumSize(QSize(125, 25))
        self.name_date_regex.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_16.addWidget(self.name_date_regex)


        self.horizontalLayout_49.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_76 = QLabel(self.groupBox_8)
        self.label_76.setObjectName(u"label_76")
        sizePolicy2.setHeightForWidth(self.label_76.sizePolicy().hasHeightForWidth())
        self.label_76.setSizePolicy(sizePolicy2)
        self.label_76.setMinimumSize(QSize(90, 25))
        self.label_76.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_19.addWidget(self.label_76)

        self.name_version_regex = QLineEdit(self.groupBox_8)
        self.name_version_regex.setObjectName(u"name_version_regex")
        sizePolicy2.setHeightForWidth(self.name_version_regex.sizePolicy().hasHeightForWidth())
        self.name_version_regex.setSizePolicy(sizePolicy2)
        self.name_version_regex.setMinimumSize(QSize(100, 25))
        self.name_version_regex.setMaximumSize(QSize(150, 16777215))
        self.name_version_regex.setReadOnly(False)

        self.horizontalLayout_19.addWidget(self.name_version_regex)


        self.horizontalLayout_49.addLayout(self.horizontalLayout_19)


        self.verticalLayout_53.addLayout(self.horizontalLayout_49)

        self.horizontalLayout_74 = QHBoxLayout()
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.groupBox_9 = QGroupBox(self.groupBox_8)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.verticalLayout = QVBoxLayout(self.groupBox_9)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.name_version_per_date = QCheckBox(self.groupBox_9)
        self.name_version_per_date.setObjectName(u"name_version_per_date")
        sizePolicy2.setHeightForWidth(self.name_version_per_date.sizePolicy().hasHeightForWidth())
        self.name_version_per_date.setSizePolicy(sizePolicy2)
        self.name_version_per_date.setMinimumSize(QSize(80, 25))
        self.name_version_per_date.setChecked(True)

        self.horizontalLayout_17.addWidget(self.name_version_per_date)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.name_version_leading_zeroes = QLabel(self.groupBox_9)
        self.name_version_leading_zeroes.setObjectName(u"name_version_leading_zeroes")
        sizePolicy2.setHeightForWidth(self.name_version_leading_zeroes.sizePolicy().hasHeightForWidth())
        self.name_version_leading_zeroes.setSizePolicy(sizePolicy2)
        self.name_version_leading_zeroes.setMinimumSize(QSize(100, 25))

        self.horizontalLayout.addWidget(self.name_version_leading_zeroes)

        self.name_version_zeroes = QSpinBox(self.groupBox_9)
        self.name_version_zeroes.setObjectName(u"name_version_zeroes")
        sizePolicy2.setHeightForWidth(self.name_version_zeroes.sizePolicy().hasHeightForWidth())
        self.name_version_zeroes.setSizePolicy(sizePolicy2)
        self.name_version_zeroes.setMinimumSize(QSize(40, 25))
        self.name_version_zeroes.setValue(3)

        self.horizontalLayout.addWidget(self.name_version_zeroes)


        self.horizontalLayout_17.addLayout(self.horizontalLayout)

        self.name_version_use_letters = QCheckBox(self.groupBox_9)
        self.name_version_use_letters.setObjectName(u"name_version_use_letters")
        sizePolicy2.setHeightForWidth(self.name_version_use_letters.sizePolicy().hasHeightForWidth())
        self.name_version_use_letters.setSizePolicy(sizePolicy2)
        self.name_version_use_letters.setMinimumSize(QSize(70, 25))
        self.name_version_use_letters.setChecked(True)

        self.horizontalLayout_17.addWidget(self.name_version_use_letters)

        self.name_version_letters_uppercase = QCheckBox(self.groupBox_9)
        self.name_version_letters_uppercase.setObjectName(u"name_version_letters_uppercase")
        sizePolicy2.setHeightForWidth(self.name_version_letters_uppercase.sizePolicy().hasHeightForWidth())
        self.name_version_letters_uppercase.setSizePolicy(sizePolicy2)
        self.name_version_letters_uppercase.setMinimumSize(QSize(90, 25))
        self.name_version_letters_uppercase.setChecked(True)

        self.horizontalLayout_17.addWidget(self.name_version_letters_uppercase)


        self.verticalLayout.addLayout(self.horizontalLayout_17)


        self.horizontalLayout_74.addWidget(self.groupBox_9)

        self.groupBox_20 = QGroupBox(self.groupBox_8)
        self.groupBox_20.setObjectName(u"groupBox_20")
        self.verticalLayout_32 = QVBoxLayout(self.groupBox_20)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.name_from_template = QRadioButton(self.groupBox_20)
        self.name_from_template.setObjectName(u"name_from_template")
        self.name_from_template.setMinimumSize(QSize(80, 25))
        self.name_from_template.setChecked(True)

        self.horizontalLayout_6.addWidget(self.name_from_template)

        self.name_from_folder = QRadioButton(self.groupBox_20)
        self.name_from_folder.setObjectName(u"name_from_folder")
        self.name_from_folder.setMinimumSize(QSize(80, 25))

        self.horizontalLayout_6.addWidget(self.name_from_folder)


        self.verticalLayout_32.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_74.addWidget(self.groupBox_20)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_74.addItem(self.horizontalSpacer_6)


        self.verticalLayout_53.addLayout(self.horizontalLayout_74)

        self.horizontalLayout_82 = QHBoxLayout()
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.name_rename = QPushButton(self.groupBox_8)
        self.name_rename.setObjectName(u"name_rename")
        sizePolicy2.setHeightForWidth(self.name_rename.sizePolicy().hasHeightForWidth())
        self.name_rename.setSizePolicy(sizePolicy2)
        self.name_rename.setMinimumSize(QSize(120, 25))

        self.horizontalLayout_82.addWidget(self.name_rename)

        self.name_rename_auto = QCheckBox(self.groupBox_8)
        self.name_rename_auto.setObjectName(u"name_rename_auto")
        sizePolicy2.setHeightForWidth(self.name_rename_auto.sizePolicy().hasHeightForWidth())
        self.name_rename_auto.setSizePolicy(sizePolicy2)
        self.name_rename_auto.setMinimumSize(QSize(120, 25))
        self.name_rename_auto.setCheckable(True)
        self.name_rename_auto.setChecked(True)

        self.horizontalLayout_82.addWidget(self.name_rename_auto)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_82.addItem(self.horizontalSpacer_8)


        self.verticalLayout_53.addLayout(self.horizontalLayout_82)

        self.horizontalLayout_78 = QHBoxLayout()
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.label_36 = QLabel(self.groupBox_8)
        self.label_36.setObjectName(u"label_36")
        sizePolicy2.setHeightForWidth(self.label_36.sizePolicy().hasHeightForWidth())
        self.label_36.setSizePolicy(sizePolicy2)
        self.label_36.setMinimumSize(QSize(55, 25))
        self.label_36.setMaximumSize(QSize(55, 16777215))

        self.horizontalLayout_40.addWidget(self.label_36)

        self.name_preview = QLineEdit(self.groupBox_8)
        self.name_preview.setObjectName(u"name_preview")
        self.name_preview.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.name_preview.sizePolicy().hasHeightForWidth())
        self.name_preview.setSizePolicy(sizePolicy1)
        self.name_preview.setMinimumSize(QSize(200, 25))
        self.name_preview.setMaximumSize(QSize(16000, 16777215))
        self.name_preview.setReadOnly(True)

        self.horizontalLayout_40.addWidget(self.name_preview)


        self.horizontalLayout_78.addLayout(self.horizontalLayout_40)


        self.verticalLayout_53.addLayout(self.horizontalLayout_78)


        self.horizontalLayout_92.addLayout(self.verticalLayout_53)


        self.verticalLayout_33.addWidget(self.groupBox_8)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_33.addItem(self.verticalSpacer)


        self.horizontalLayout_50.addLayout(self.verticalLayout_33)

        self.TopTab.addTab(self.tab, "")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.horizontalLayout_24 = QHBoxLayout(self.tab_10)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.scrollArea = QScrollArea(self.tab_10)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy3)
        self.scrollArea.setMinimumSize(QSize(500, 250))
        self.scrollArea.setMaximumSize(QSize(16777215, 350))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1196, 1070))
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy4)
        self.scrollAreaWidgetContents.setMinimumSize(QSize(500, 0))
        self.verticalLayout_31 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.hl_parse001 = QHBoxLayout()
        self.hl_parse001.setObjectName(u"hl_parse001")
        self.label_18 = QLabel(self.scrollAreaWidgetContents)
        self.label_18.setObjectName(u"label_18")
        sizePolicy2.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy2)
        self.label_18.setMinimumSize(QSize(50, 25))

        self.hl_parse001.addWidget(self.label_18)

        self.parse_name_01 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_name_01.setObjectName(u"parse_name_01")
        sizePolicy1.setHeightForWidth(self.parse_name_01.sizePolicy().hasHeightForWidth())
        self.parse_name_01.setSizePolicy(sizePolicy1)
        self.parse_name_01.setMinimumSize(QSize(30, 25))
        self.parse_name_01.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse001.addWidget(self.parse_name_01)

        self.label_20 = QLabel(self.scrollAreaWidgetContents)
        self.label_20.setObjectName(u"label_20")
        sizePolicy2.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy2)
        self.label_20.setMinimumSize(QSize(50, 25))

        self.hl_parse001.addWidget(self.label_20)

        self.parse_pattern_01 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_pattern_01.setObjectName(u"parse_pattern_01")
        sizePolicy1.setHeightForWidth(self.parse_pattern_01.sizePolicy().hasHeightForWidth())
        self.parse_pattern_01.setSizePolicy(sizePolicy1)
        self.parse_pattern_01.setMinimumSize(QSize(100, 25))

        self.hl_parse001.addWidget(self.parse_pattern_01)

        self.label_19 = QLabel(self.scrollAreaWidgetContents)
        self.label_19.setObjectName(u"label_19")
        sizePolicy2.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy2)
        self.label_19.setMinimumSize(QSize(50, 25))

        self.hl_parse001.addWidget(self.label_19)

        self.parse_repl_01 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_repl_01.setObjectName(u"parse_repl_01")
        sizePolicy1.setHeightForWidth(self.parse_repl_01.sizePolicy().hasHeightForWidth())
        self.parse_repl_01.setSizePolicy(sizePolicy1)
        self.parse_repl_01.setMinimumSize(QSize(80, 25))
        self.parse_repl_01.setMaximumSize(QSize(1600, 16777215))

        self.hl_parse001.addWidget(self.parse_repl_01)

        self.label_21 = QLabel(self.scrollAreaWidgetContents)
        self.label_21.setObjectName(u"label_21")
        sizePolicy2.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy2)
        self.label_21.setMinimumSize(QSize(50, 25))

        self.hl_parse001.addWidget(self.label_21)

        self.parse_source_01 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_source_01.setObjectName(u"parse_source_01")
        sizePolicy1.setHeightForWidth(self.parse_source_01.sizePolicy().hasHeightForWidth())
        self.parse_source_01.setSizePolicy(sizePolicy1)
        self.parse_source_01.setMinimumSize(QSize(30, 25))
        self.parse_source_01.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse001.addWidget(self.parse_source_01)

        self.label_77 = QLabel(self.scrollAreaWidgetContents)
        self.label_77.setObjectName(u"label_77")
        sizePolicy2.setHeightForWidth(self.label_77.sizePolicy().hasHeightForWidth())
        self.label_77.setSizePolicy(sizePolicy2)
        self.label_77.setMinimumSize(QSize(40, 25))

        self.hl_parse001.addWidget(self.label_77)

        self.parse_filter_01 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_filter_01.setObjectName(u"parse_filter_01")
        sizePolicy1.setHeightForWidth(self.parse_filter_01.sizePolicy().hasHeightForWidth())
        self.parse_filter_01.setSizePolicy(sizePolicy1)
        self.parse_filter_01.setMinimumSize(QSize(30, 25))
        self.parse_filter_01.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse001.addWidget(self.parse_filter_01)


        self.verticalLayout_30.addLayout(self.hl_parse001)

        self.hl_parse002 = QHBoxLayout()
        self.hl_parse002.setObjectName(u"hl_parse002")
        self.label_170 = QLabel(self.scrollAreaWidgetContents)
        self.label_170.setObjectName(u"label_170")
        sizePolicy2.setHeightForWidth(self.label_170.sizePolicy().hasHeightForWidth())
        self.label_170.setSizePolicy(sizePolicy2)
        self.label_170.setMinimumSize(QSize(50, 25))

        self.hl_parse002.addWidget(self.label_170)

        self.parse_name_02 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_name_02.setObjectName(u"parse_name_02")
        sizePolicy1.setHeightForWidth(self.parse_name_02.sizePolicy().hasHeightForWidth())
        self.parse_name_02.setSizePolicy(sizePolicy1)
        self.parse_name_02.setMinimumSize(QSize(30, 25))
        self.parse_name_02.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse002.addWidget(self.parse_name_02)

        self.label_171 = QLabel(self.scrollAreaWidgetContents)
        self.label_171.setObjectName(u"label_171")
        sizePolicy2.setHeightForWidth(self.label_171.sizePolicy().hasHeightForWidth())
        self.label_171.setSizePolicy(sizePolicy2)
        self.label_171.setMinimumSize(QSize(50, 25))

        self.hl_parse002.addWidget(self.label_171)

        self.parse_pattern_02 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_pattern_02.setObjectName(u"parse_pattern_02")
        sizePolicy1.setHeightForWidth(self.parse_pattern_02.sizePolicy().hasHeightForWidth())
        self.parse_pattern_02.setSizePolicy(sizePolicy1)
        self.parse_pattern_02.setMinimumSize(QSize(100, 25))

        self.hl_parse002.addWidget(self.parse_pattern_02)

        self.label_172 = QLabel(self.scrollAreaWidgetContents)
        self.label_172.setObjectName(u"label_172")
        sizePolicy2.setHeightForWidth(self.label_172.sizePolicy().hasHeightForWidth())
        self.label_172.setSizePolicy(sizePolicy2)
        self.label_172.setMinimumSize(QSize(50, 25))

        self.hl_parse002.addWidget(self.label_172)

        self.parse_repl_02 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_repl_02.setObjectName(u"parse_repl_02")
        sizePolicy1.setHeightForWidth(self.parse_repl_02.sizePolicy().hasHeightForWidth())
        self.parse_repl_02.setSizePolicy(sizePolicy1)
        self.parse_repl_02.setMinimumSize(QSize(80, 25))
        self.parse_repl_02.setMaximumSize(QSize(1600, 16777215))

        self.hl_parse002.addWidget(self.parse_repl_02)

        self.label_173 = QLabel(self.scrollAreaWidgetContents)
        self.label_173.setObjectName(u"label_173")
        sizePolicy2.setHeightForWidth(self.label_173.sizePolicy().hasHeightForWidth())
        self.label_173.setSizePolicy(sizePolicy2)
        self.label_173.setMinimumSize(QSize(50, 25))

        self.hl_parse002.addWidget(self.label_173)

        self.parse_source_02 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_source_02.setObjectName(u"parse_source_02")
        sizePolicy1.setHeightForWidth(self.parse_source_02.sizePolicy().hasHeightForWidth())
        self.parse_source_02.setSizePolicy(sizePolicy1)
        self.parse_source_02.setMinimumSize(QSize(30, 25))
        self.parse_source_02.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse002.addWidget(self.parse_source_02)

        self.label_174 = QLabel(self.scrollAreaWidgetContents)
        self.label_174.setObjectName(u"label_174")
        sizePolicy2.setHeightForWidth(self.label_174.sizePolicy().hasHeightForWidth())
        self.label_174.setSizePolicy(sizePolicy2)
        self.label_174.setMinimumSize(QSize(40, 25))

        self.hl_parse002.addWidget(self.label_174)

        self.parse_filter_02 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_filter_02.setObjectName(u"parse_filter_02")
        sizePolicy1.setHeightForWidth(self.parse_filter_02.sizePolicy().hasHeightForWidth())
        self.parse_filter_02.setSizePolicy(sizePolicy1)
        self.parse_filter_02.setMinimumSize(QSize(30, 25))
        self.parse_filter_02.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse002.addWidget(self.parse_filter_02)


        self.verticalLayout_30.addLayout(self.hl_parse002)

        self.hl_parse003 = QHBoxLayout()
        self.hl_parse003.setObjectName(u"hl_parse003")
        self.label_22 = QLabel(self.scrollAreaWidgetContents)
        self.label_22.setObjectName(u"label_22")
        sizePolicy2.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy2)
        self.label_22.setMinimumSize(QSize(50, 25))

        self.hl_parse003.addWidget(self.label_22)

        self.parse_name_03 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_name_03.setObjectName(u"parse_name_03")
        sizePolicy1.setHeightForWidth(self.parse_name_03.sizePolicy().hasHeightForWidth())
        self.parse_name_03.setSizePolicy(sizePolicy1)
        self.parse_name_03.setMinimumSize(QSize(30, 25))
        self.parse_name_03.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse003.addWidget(self.parse_name_03)

        self.label_38 = QLabel(self.scrollAreaWidgetContents)
        self.label_38.setObjectName(u"label_38")
        sizePolicy2.setHeightForWidth(self.label_38.sizePolicy().hasHeightForWidth())
        self.label_38.setSizePolicy(sizePolicy2)
        self.label_38.setMinimumSize(QSize(50, 25))

        self.hl_parse003.addWidget(self.label_38)

        self.parse_pattern_03 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_pattern_03.setObjectName(u"parse_pattern_03")
        sizePolicy1.setHeightForWidth(self.parse_pattern_03.sizePolicy().hasHeightForWidth())
        self.parse_pattern_03.setSizePolicy(sizePolicy1)
        self.parse_pattern_03.setMinimumSize(QSize(100, 25))

        self.hl_parse003.addWidget(self.parse_pattern_03)

        self.label_39 = QLabel(self.scrollAreaWidgetContents)
        self.label_39.setObjectName(u"label_39")
        sizePolicy2.setHeightForWidth(self.label_39.sizePolicy().hasHeightForWidth())
        self.label_39.setSizePolicy(sizePolicy2)
        self.label_39.setMinimumSize(QSize(50, 25))

        self.hl_parse003.addWidget(self.label_39)

        self.parse_repl_03 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_repl_03.setObjectName(u"parse_repl_03")
        sizePolicy1.setHeightForWidth(self.parse_repl_03.sizePolicy().hasHeightForWidth())
        self.parse_repl_03.setSizePolicy(sizePolicy1)
        self.parse_repl_03.setMinimumSize(QSize(80, 25))
        self.parse_repl_03.setMaximumSize(QSize(1600, 16777215))

        self.hl_parse003.addWidget(self.parse_repl_03)

        self.label_40 = QLabel(self.scrollAreaWidgetContents)
        self.label_40.setObjectName(u"label_40")
        sizePolicy2.setHeightForWidth(self.label_40.sizePolicy().hasHeightForWidth())
        self.label_40.setSizePolicy(sizePolicy2)
        self.label_40.setMinimumSize(QSize(50, 25))

        self.hl_parse003.addWidget(self.label_40)

        self.parse_source_03 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_source_03.setObjectName(u"parse_source_03")
        sizePolicy1.setHeightForWidth(self.parse_source_03.sizePolicy().hasHeightForWidth())
        self.parse_source_03.setSizePolicy(sizePolicy1)
        self.parse_source_03.setMinimumSize(QSize(30, 25))
        self.parse_source_03.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse003.addWidget(self.parse_source_03)

        self.label_78 = QLabel(self.scrollAreaWidgetContents)
        self.label_78.setObjectName(u"label_78")
        sizePolicy2.setHeightForWidth(self.label_78.sizePolicy().hasHeightForWidth())
        self.label_78.setSizePolicy(sizePolicy2)
        self.label_78.setMinimumSize(QSize(40, 25))

        self.hl_parse003.addWidget(self.label_78)

        self.parse_filter_03 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_filter_03.setObjectName(u"parse_filter_03")
        sizePolicy1.setHeightForWidth(self.parse_filter_03.sizePolicy().hasHeightForWidth())
        self.parse_filter_03.setSizePolicy(sizePolicy1)
        self.parse_filter_03.setMinimumSize(QSize(30, 25))
        self.parse_filter_03.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse003.addWidget(self.parse_filter_03)


        self.verticalLayout_30.addLayout(self.hl_parse003)

        self.hl_parse004 = QHBoxLayout()
        self.hl_parse004.setObjectName(u"hl_parse004")
        self.label_175 = QLabel(self.scrollAreaWidgetContents)
        self.label_175.setObjectName(u"label_175")
        sizePolicy2.setHeightForWidth(self.label_175.sizePolicy().hasHeightForWidth())
        self.label_175.setSizePolicy(sizePolicy2)
        self.label_175.setMinimumSize(QSize(50, 25))

        self.hl_parse004.addWidget(self.label_175)

        self.parse_name_04 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_name_04.setObjectName(u"parse_name_04")
        sizePolicy1.setHeightForWidth(self.parse_name_04.sizePolicy().hasHeightForWidth())
        self.parse_name_04.setSizePolicy(sizePolicy1)
        self.parse_name_04.setMinimumSize(QSize(30, 25))
        self.parse_name_04.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse004.addWidget(self.parse_name_04)

        self.label_176 = QLabel(self.scrollAreaWidgetContents)
        self.label_176.setObjectName(u"label_176")
        sizePolicy2.setHeightForWidth(self.label_176.sizePolicy().hasHeightForWidth())
        self.label_176.setSizePolicy(sizePolicy2)
        self.label_176.setMinimumSize(QSize(50, 25))

        self.hl_parse004.addWidget(self.label_176)

        self.parse_pattern_04 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_pattern_04.setObjectName(u"parse_pattern_04")
        sizePolicy1.setHeightForWidth(self.parse_pattern_04.sizePolicy().hasHeightForWidth())
        self.parse_pattern_04.setSizePolicy(sizePolicy1)
        self.parse_pattern_04.setMinimumSize(QSize(100, 25))

        self.hl_parse004.addWidget(self.parse_pattern_04)

        self.label_177 = QLabel(self.scrollAreaWidgetContents)
        self.label_177.setObjectName(u"label_177")
        sizePolicy2.setHeightForWidth(self.label_177.sizePolicy().hasHeightForWidth())
        self.label_177.setSizePolicy(sizePolicy2)
        self.label_177.setMinimumSize(QSize(50, 25))

        self.hl_parse004.addWidget(self.label_177)

        self.parse_repl_04 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_repl_04.setObjectName(u"parse_repl_04")
        sizePolicy1.setHeightForWidth(self.parse_repl_04.sizePolicy().hasHeightForWidth())
        self.parse_repl_04.setSizePolicy(sizePolicy1)
        self.parse_repl_04.setMinimumSize(QSize(80, 25))
        self.parse_repl_04.setMaximumSize(QSize(1600, 16777215))

        self.hl_parse004.addWidget(self.parse_repl_04)

        self.label_178 = QLabel(self.scrollAreaWidgetContents)
        self.label_178.setObjectName(u"label_178")
        sizePolicy2.setHeightForWidth(self.label_178.sizePolicy().hasHeightForWidth())
        self.label_178.setSizePolicy(sizePolicy2)
        self.label_178.setMinimumSize(QSize(50, 25))

        self.hl_parse004.addWidget(self.label_178)

        self.parse_source_04 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_source_04.setObjectName(u"parse_source_04")
        sizePolicy1.setHeightForWidth(self.parse_source_04.sizePolicy().hasHeightForWidth())
        self.parse_source_04.setSizePolicy(sizePolicy1)
        self.parse_source_04.setMinimumSize(QSize(30, 25))
        self.parse_source_04.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse004.addWidget(self.parse_source_04)

        self.label_179 = QLabel(self.scrollAreaWidgetContents)
        self.label_179.setObjectName(u"label_179")
        sizePolicy2.setHeightForWidth(self.label_179.sizePolicy().hasHeightForWidth())
        self.label_179.setSizePolicy(sizePolicy2)
        self.label_179.setMinimumSize(QSize(40, 25))

        self.hl_parse004.addWidget(self.label_179)

        self.parse_filter_04 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_filter_04.setObjectName(u"parse_filter_04")
        sizePolicy1.setHeightForWidth(self.parse_filter_04.sizePolicy().hasHeightForWidth())
        self.parse_filter_04.setSizePolicy(sizePolicy1)
        self.parse_filter_04.setMinimumSize(QSize(30, 25))
        self.parse_filter_04.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse004.addWidget(self.parse_filter_04)


        self.verticalLayout_30.addLayout(self.hl_parse004)

        self.hl_parse005 = QHBoxLayout()
        self.hl_parse005.setObjectName(u"hl_parse005")
        self.label_41 = QLabel(self.scrollAreaWidgetContents)
        self.label_41.setObjectName(u"label_41")
        sizePolicy2.setHeightForWidth(self.label_41.sizePolicy().hasHeightForWidth())
        self.label_41.setSizePolicy(sizePolicy2)
        self.label_41.setMinimumSize(QSize(50, 25))

        self.hl_parse005.addWidget(self.label_41)

        self.parse_name_05 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_name_05.setObjectName(u"parse_name_05")
        sizePolicy1.setHeightForWidth(self.parse_name_05.sizePolicy().hasHeightForWidth())
        self.parse_name_05.setSizePolicy(sizePolicy1)
        self.parse_name_05.setMinimumSize(QSize(30, 25))
        self.parse_name_05.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse005.addWidget(self.parse_name_05)

        self.label_42 = QLabel(self.scrollAreaWidgetContents)
        self.label_42.setObjectName(u"label_42")
        sizePolicy2.setHeightForWidth(self.label_42.sizePolicy().hasHeightForWidth())
        self.label_42.setSizePolicy(sizePolicy2)
        self.label_42.setMinimumSize(QSize(50, 25))

        self.hl_parse005.addWidget(self.label_42)

        self.parse_pattern_05 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_pattern_05.setObjectName(u"parse_pattern_05")
        sizePolicy1.setHeightForWidth(self.parse_pattern_05.sizePolicy().hasHeightForWidth())
        self.parse_pattern_05.setSizePolicy(sizePolicy1)
        self.parse_pattern_05.setMinimumSize(QSize(100, 25))

        self.hl_parse005.addWidget(self.parse_pattern_05)

        self.label_43 = QLabel(self.scrollAreaWidgetContents)
        self.label_43.setObjectName(u"label_43")
        sizePolicy2.setHeightForWidth(self.label_43.sizePolicy().hasHeightForWidth())
        self.label_43.setSizePolicy(sizePolicy2)
        self.label_43.setMinimumSize(QSize(50, 25))

        self.hl_parse005.addWidget(self.label_43)

        self.parse_repl_05 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_repl_05.setObjectName(u"parse_repl_05")
        sizePolicy1.setHeightForWidth(self.parse_repl_05.sizePolicy().hasHeightForWidth())
        self.parse_repl_05.setSizePolicy(sizePolicy1)
        self.parse_repl_05.setMinimumSize(QSize(80, 25))
        self.parse_repl_05.setMaximumSize(QSize(1600, 16777215))

        self.hl_parse005.addWidget(self.parse_repl_05)

        self.label_44 = QLabel(self.scrollAreaWidgetContents)
        self.label_44.setObjectName(u"label_44")
        sizePolicy2.setHeightForWidth(self.label_44.sizePolicy().hasHeightForWidth())
        self.label_44.setSizePolicy(sizePolicy2)
        self.label_44.setMinimumSize(QSize(50, 25))

        self.hl_parse005.addWidget(self.label_44)

        self.parse_source_05 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_source_05.setObjectName(u"parse_source_05")
        sizePolicy1.setHeightForWidth(self.parse_source_05.sizePolicy().hasHeightForWidth())
        self.parse_source_05.setSizePolicy(sizePolicy1)
        self.parse_source_05.setMinimumSize(QSize(30, 25))
        self.parse_source_05.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse005.addWidget(self.parse_source_05)

        self.label_79 = QLabel(self.scrollAreaWidgetContents)
        self.label_79.setObjectName(u"label_79")
        sizePolicy2.setHeightForWidth(self.label_79.sizePolicy().hasHeightForWidth())
        self.label_79.setSizePolicy(sizePolicy2)
        self.label_79.setMinimumSize(QSize(40, 25))

        self.hl_parse005.addWidget(self.label_79)

        self.parse_filter_05 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_filter_05.setObjectName(u"parse_filter_05")
        sizePolicy1.setHeightForWidth(self.parse_filter_05.sizePolicy().hasHeightForWidth())
        self.parse_filter_05.setSizePolicy(sizePolicy1)
        self.parse_filter_05.setMinimumSize(QSize(30, 25))
        self.parse_filter_05.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse005.addWidget(self.parse_filter_05)


        self.verticalLayout_30.addLayout(self.hl_parse005)

        self.hl_parse006 = QHBoxLayout()
        self.hl_parse006.setObjectName(u"hl_parse006")
        self.label_180 = QLabel(self.scrollAreaWidgetContents)
        self.label_180.setObjectName(u"label_180")
        sizePolicy2.setHeightForWidth(self.label_180.sizePolicy().hasHeightForWidth())
        self.label_180.setSizePolicy(sizePolicy2)
        self.label_180.setMinimumSize(QSize(50, 25))

        self.hl_parse006.addWidget(self.label_180)

        self.parse_name_06 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_name_06.setObjectName(u"parse_name_06")
        sizePolicy1.setHeightForWidth(self.parse_name_06.sizePolicy().hasHeightForWidth())
        self.parse_name_06.setSizePolicy(sizePolicy1)
        self.parse_name_06.setMinimumSize(QSize(30, 25))
        self.parse_name_06.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse006.addWidget(self.parse_name_06)

        self.label_181 = QLabel(self.scrollAreaWidgetContents)
        self.label_181.setObjectName(u"label_181")
        sizePolicy2.setHeightForWidth(self.label_181.sizePolicy().hasHeightForWidth())
        self.label_181.setSizePolicy(sizePolicy2)
        self.label_181.setMinimumSize(QSize(50, 25))

        self.hl_parse006.addWidget(self.label_181)

        self.parse_pattern_06 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_pattern_06.setObjectName(u"parse_pattern_06")
        sizePolicy1.setHeightForWidth(self.parse_pattern_06.sizePolicy().hasHeightForWidth())
        self.parse_pattern_06.setSizePolicy(sizePolicy1)
        self.parse_pattern_06.setMinimumSize(QSize(100, 25))

        self.hl_parse006.addWidget(self.parse_pattern_06)

        self.label_182 = QLabel(self.scrollAreaWidgetContents)
        self.label_182.setObjectName(u"label_182")
        sizePolicy2.setHeightForWidth(self.label_182.sizePolicy().hasHeightForWidth())
        self.label_182.setSizePolicy(sizePolicy2)
        self.label_182.setMinimumSize(QSize(50, 25))

        self.hl_parse006.addWidget(self.label_182)

        self.parse_repl_06 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_repl_06.setObjectName(u"parse_repl_06")
        sizePolicy1.setHeightForWidth(self.parse_repl_06.sizePolicy().hasHeightForWidth())
        self.parse_repl_06.setSizePolicy(sizePolicy1)
        self.parse_repl_06.setMinimumSize(QSize(80, 25))
        self.parse_repl_06.setMaximumSize(QSize(1600, 16777215))

        self.hl_parse006.addWidget(self.parse_repl_06)

        self.label_183 = QLabel(self.scrollAreaWidgetContents)
        self.label_183.setObjectName(u"label_183")
        sizePolicy2.setHeightForWidth(self.label_183.sizePolicy().hasHeightForWidth())
        self.label_183.setSizePolicy(sizePolicy2)
        self.label_183.setMinimumSize(QSize(50, 25))

        self.hl_parse006.addWidget(self.label_183)

        self.parse_source_06 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_source_06.setObjectName(u"parse_source_06")
        sizePolicy1.setHeightForWidth(self.parse_source_06.sizePolicy().hasHeightForWidth())
        self.parse_source_06.setSizePolicy(sizePolicy1)
        self.parse_source_06.setMinimumSize(QSize(30, 25))
        self.parse_source_06.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse006.addWidget(self.parse_source_06)

        self.label_184 = QLabel(self.scrollAreaWidgetContents)
        self.label_184.setObjectName(u"label_184")
        sizePolicy2.setHeightForWidth(self.label_184.sizePolicy().hasHeightForWidth())
        self.label_184.setSizePolicy(sizePolicy2)
        self.label_184.setMinimumSize(QSize(40, 25))

        self.hl_parse006.addWidget(self.label_184)

        self.parse_filter_06 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_filter_06.setObjectName(u"parse_filter_06")
        sizePolicy1.setHeightForWidth(self.parse_filter_06.sizePolicy().hasHeightForWidth())
        self.parse_filter_06.setSizePolicy(sizePolicy1)
        self.parse_filter_06.setMinimumSize(QSize(30, 25))
        self.parse_filter_06.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse006.addWidget(self.parse_filter_06)


        self.verticalLayout_30.addLayout(self.hl_parse006)

        self.hl_parse007 = QHBoxLayout()
        self.hl_parse007.setObjectName(u"hl_parse007")
        self.label_47 = QLabel(self.scrollAreaWidgetContents)
        self.label_47.setObjectName(u"label_47")
        sizePolicy2.setHeightForWidth(self.label_47.sizePolicy().hasHeightForWidth())
        self.label_47.setSizePolicy(sizePolicy2)
        self.label_47.setMinimumSize(QSize(50, 25))

        self.hl_parse007.addWidget(self.label_47)

        self.parse_name_07 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_name_07.setObjectName(u"parse_name_07")
        sizePolicy1.setHeightForWidth(self.parse_name_07.sizePolicy().hasHeightForWidth())
        self.parse_name_07.setSizePolicy(sizePolicy1)
        self.parse_name_07.setMinimumSize(QSize(30, 25))
        self.parse_name_07.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse007.addWidget(self.parse_name_07)

        self.label_48 = QLabel(self.scrollAreaWidgetContents)
        self.label_48.setObjectName(u"label_48")
        sizePolicy2.setHeightForWidth(self.label_48.sizePolicy().hasHeightForWidth())
        self.label_48.setSizePolicy(sizePolicy2)
        self.label_48.setMinimumSize(QSize(50, 25))

        self.hl_parse007.addWidget(self.label_48)

        self.parse_pattern_07 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_pattern_07.setObjectName(u"parse_pattern_07")
        sizePolicy1.setHeightForWidth(self.parse_pattern_07.sizePolicy().hasHeightForWidth())
        self.parse_pattern_07.setSizePolicy(sizePolicy1)
        self.parse_pattern_07.setMinimumSize(QSize(100, 25))

        self.hl_parse007.addWidget(self.parse_pattern_07)

        self.label_49 = QLabel(self.scrollAreaWidgetContents)
        self.label_49.setObjectName(u"label_49")
        sizePolicy2.setHeightForWidth(self.label_49.sizePolicy().hasHeightForWidth())
        self.label_49.setSizePolicy(sizePolicy2)
        self.label_49.setMinimumSize(QSize(50, 25))

        self.hl_parse007.addWidget(self.label_49)

        self.parse_repl_07 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_repl_07.setObjectName(u"parse_repl_07")
        sizePolicy1.setHeightForWidth(self.parse_repl_07.sizePolicy().hasHeightForWidth())
        self.parse_repl_07.setSizePolicy(sizePolicy1)
        self.parse_repl_07.setMinimumSize(QSize(80, 25))
        self.parse_repl_07.setMaximumSize(QSize(1600, 16777215))

        self.hl_parse007.addWidget(self.parse_repl_07)

        self.label_50 = QLabel(self.scrollAreaWidgetContents)
        self.label_50.setObjectName(u"label_50")
        sizePolicy2.setHeightForWidth(self.label_50.sizePolicy().hasHeightForWidth())
        self.label_50.setSizePolicy(sizePolicy2)
        self.label_50.setMinimumSize(QSize(50, 25))

        self.hl_parse007.addWidget(self.label_50)

        self.parse_source_07 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_source_07.setObjectName(u"parse_source_07")
        sizePolicy1.setHeightForWidth(self.parse_source_07.sizePolicy().hasHeightForWidth())
        self.parse_source_07.setSizePolicy(sizePolicy1)
        self.parse_source_07.setMinimumSize(QSize(30, 25))
        self.parse_source_07.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse007.addWidget(self.parse_source_07)

        self.label_80 = QLabel(self.scrollAreaWidgetContents)
        self.label_80.setObjectName(u"label_80")
        sizePolicy2.setHeightForWidth(self.label_80.sizePolicy().hasHeightForWidth())
        self.label_80.setSizePolicy(sizePolicy2)
        self.label_80.setMinimumSize(QSize(40, 25))

        self.hl_parse007.addWidget(self.label_80)

        self.parse_filter_07 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_filter_07.setObjectName(u"parse_filter_07")
        sizePolicy1.setHeightForWidth(self.parse_filter_07.sizePolicy().hasHeightForWidth())
        self.parse_filter_07.setSizePolicy(sizePolicy1)
        self.parse_filter_07.setMinimumSize(QSize(30, 25))
        self.parse_filter_07.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse007.addWidget(self.parse_filter_07)


        self.verticalLayout_30.addLayout(self.hl_parse007)

        self.hl_parse008 = QHBoxLayout()
        self.hl_parse008.setObjectName(u"hl_parse008")
        self.label_185 = QLabel(self.scrollAreaWidgetContents)
        self.label_185.setObjectName(u"label_185")
        sizePolicy2.setHeightForWidth(self.label_185.sizePolicy().hasHeightForWidth())
        self.label_185.setSizePolicy(sizePolicy2)
        self.label_185.setMinimumSize(QSize(50, 25))

        self.hl_parse008.addWidget(self.label_185)

        self.parse_name_08 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_name_08.setObjectName(u"parse_name_08")
        sizePolicy1.setHeightForWidth(self.parse_name_08.sizePolicy().hasHeightForWidth())
        self.parse_name_08.setSizePolicy(sizePolicy1)
        self.parse_name_08.setMinimumSize(QSize(30, 25))
        self.parse_name_08.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse008.addWidget(self.parse_name_08)

        self.label_186 = QLabel(self.scrollAreaWidgetContents)
        self.label_186.setObjectName(u"label_186")
        sizePolicy2.setHeightForWidth(self.label_186.sizePolicy().hasHeightForWidth())
        self.label_186.setSizePolicy(sizePolicy2)
        self.label_186.setMinimumSize(QSize(50, 25))

        self.hl_parse008.addWidget(self.label_186)

        self.parse_pattern_08 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_pattern_08.setObjectName(u"parse_pattern_08")
        sizePolicy1.setHeightForWidth(self.parse_pattern_08.sizePolicy().hasHeightForWidth())
        self.parse_pattern_08.setSizePolicy(sizePolicy1)
        self.parse_pattern_08.setMinimumSize(QSize(100, 25))

        self.hl_parse008.addWidget(self.parse_pattern_08)

        self.label_187 = QLabel(self.scrollAreaWidgetContents)
        self.label_187.setObjectName(u"label_187")
        sizePolicy2.setHeightForWidth(self.label_187.sizePolicy().hasHeightForWidth())
        self.label_187.setSizePolicy(sizePolicy2)
        self.label_187.setMinimumSize(QSize(50, 25))

        self.hl_parse008.addWidget(self.label_187)

        self.parse_repl_08 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_repl_08.setObjectName(u"parse_repl_08")
        sizePolicy1.setHeightForWidth(self.parse_repl_08.sizePolicy().hasHeightForWidth())
        self.parse_repl_08.setSizePolicy(sizePolicy1)
        self.parse_repl_08.setMinimumSize(QSize(80, 25))
        self.parse_repl_08.setMaximumSize(QSize(1600, 16777215))

        self.hl_parse008.addWidget(self.parse_repl_08)

        self.label_188 = QLabel(self.scrollAreaWidgetContents)
        self.label_188.setObjectName(u"label_188")
        sizePolicy2.setHeightForWidth(self.label_188.sizePolicy().hasHeightForWidth())
        self.label_188.setSizePolicy(sizePolicy2)
        self.label_188.setMinimumSize(QSize(50, 25))

        self.hl_parse008.addWidget(self.label_188)

        self.parse_source_08 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_source_08.setObjectName(u"parse_source_08")
        sizePolicy1.setHeightForWidth(self.parse_source_08.sizePolicy().hasHeightForWidth())
        self.parse_source_08.setSizePolicy(sizePolicy1)
        self.parse_source_08.setMinimumSize(QSize(30, 25))
        self.parse_source_08.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse008.addWidget(self.parse_source_08)

        self.label_189 = QLabel(self.scrollAreaWidgetContents)
        self.label_189.setObjectName(u"label_189")
        sizePolicy2.setHeightForWidth(self.label_189.sizePolicy().hasHeightForWidth())
        self.label_189.setSizePolicy(sizePolicy2)
        self.label_189.setMinimumSize(QSize(40, 25))

        self.hl_parse008.addWidget(self.label_189)

        self.parse_filter_08 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_filter_08.setObjectName(u"parse_filter_08")
        sizePolicy1.setHeightForWidth(self.parse_filter_08.sizePolicy().hasHeightForWidth())
        self.parse_filter_08.setSizePolicy(sizePolicy1)
        self.parse_filter_08.setMinimumSize(QSize(30, 25))
        self.parse_filter_08.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse008.addWidget(self.parse_filter_08)


        self.verticalLayout_30.addLayout(self.hl_parse008)

        self.hl_parse009 = QHBoxLayout()
        self.hl_parse009.setObjectName(u"hl_parse009")
        self.label_55 = QLabel(self.scrollAreaWidgetContents)
        self.label_55.setObjectName(u"label_55")
        sizePolicy2.setHeightForWidth(self.label_55.sizePolicy().hasHeightForWidth())
        self.label_55.setSizePolicy(sizePolicy2)
        self.label_55.setMinimumSize(QSize(50, 25))

        self.hl_parse009.addWidget(self.label_55)

        self.parse_name_09 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_name_09.setObjectName(u"parse_name_09")
        sizePolicy1.setHeightForWidth(self.parse_name_09.sizePolicy().hasHeightForWidth())
        self.parse_name_09.setSizePolicy(sizePolicy1)
        self.parse_name_09.setMinimumSize(QSize(30, 25))
        self.parse_name_09.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse009.addWidget(self.parse_name_09)

        self.label_56 = QLabel(self.scrollAreaWidgetContents)
        self.label_56.setObjectName(u"label_56")
        sizePolicy2.setHeightForWidth(self.label_56.sizePolicy().hasHeightForWidth())
        self.label_56.setSizePolicy(sizePolicy2)
        self.label_56.setMinimumSize(QSize(50, 25))

        self.hl_parse009.addWidget(self.label_56)

        self.parse_pattern_09 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_pattern_09.setObjectName(u"parse_pattern_09")
        sizePolicy1.setHeightForWidth(self.parse_pattern_09.sizePolicy().hasHeightForWidth())
        self.parse_pattern_09.setSizePolicy(sizePolicy1)
        self.parse_pattern_09.setMinimumSize(QSize(100, 25))

        self.hl_parse009.addWidget(self.parse_pattern_09)

        self.label_57 = QLabel(self.scrollAreaWidgetContents)
        self.label_57.setObjectName(u"label_57")
        sizePolicy2.setHeightForWidth(self.label_57.sizePolicy().hasHeightForWidth())
        self.label_57.setSizePolicy(sizePolicy2)
        self.label_57.setMinimumSize(QSize(50, 25))

        self.hl_parse009.addWidget(self.label_57)

        self.parse_repl_09 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_repl_09.setObjectName(u"parse_repl_09")
        sizePolicy1.setHeightForWidth(self.parse_repl_09.sizePolicy().hasHeightForWidth())
        self.parse_repl_09.setSizePolicy(sizePolicy1)
        self.parse_repl_09.setMinimumSize(QSize(80, 25))
        self.parse_repl_09.setMaximumSize(QSize(1600, 16777215))

        self.hl_parse009.addWidget(self.parse_repl_09)

        self.label_58 = QLabel(self.scrollAreaWidgetContents)
        self.label_58.setObjectName(u"label_58")
        sizePolicy2.setHeightForWidth(self.label_58.sizePolicy().hasHeightForWidth())
        self.label_58.setSizePolicy(sizePolicy2)
        self.label_58.setMinimumSize(QSize(50, 25))

        self.hl_parse009.addWidget(self.label_58)

        self.parse_source_09 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_source_09.setObjectName(u"parse_source_09")
        sizePolicy1.setHeightForWidth(self.parse_source_09.sizePolicy().hasHeightForWidth())
        self.parse_source_09.setSizePolicy(sizePolicy1)
        self.parse_source_09.setMinimumSize(QSize(30, 25))
        self.parse_source_09.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse009.addWidget(self.parse_source_09)

        self.label_81 = QLabel(self.scrollAreaWidgetContents)
        self.label_81.setObjectName(u"label_81")
        sizePolicy2.setHeightForWidth(self.label_81.sizePolicy().hasHeightForWidth())
        self.label_81.setSizePolicy(sizePolicy2)
        self.label_81.setMinimumSize(QSize(40, 25))

        self.hl_parse009.addWidget(self.label_81)

        self.parse_filter_09 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_filter_09.setObjectName(u"parse_filter_09")
        sizePolicy1.setHeightForWidth(self.parse_filter_09.sizePolicy().hasHeightForWidth())
        self.parse_filter_09.setSizePolicy(sizePolicy1)
        self.parse_filter_09.setMinimumSize(QSize(30, 25))
        self.parse_filter_09.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse009.addWidget(self.parse_filter_09)


        self.verticalLayout_30.addLayout(self.hl_parse009)

        self.hl_parse010 = QHBoxLayout()
        self.hl_parse010.setObjectName(u"hl_parse010")
        self.label_190 = QLabel(self.scrollAreaWidgetContents)
        self.label_190.setObjectName(u"label_190")
        sizePolicy2.setHeightForWidth(self.label_190.sizePolicy().hasHeightForWidth())
        self.label_190.setSizePolicy(sizePolicy2)
        self.label_190.setMinimumSize(QSize(50, 25))

        self.hl_parse010.addWidget(self.label_190)

        self.parse_name_10 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_name_10.setObjectName(u"parse_name_10")
        sizePolicy1.setHeightForWidth(self.parse_name_10.sizePolicy().hasHeightForWidth())
        self.parse_name_10.setSizePolicy(sizePolicy1)
        self.parse_name_10.setMinimumSize(QSize(30, 25))
        self.parse_name_10.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse010.addWidget(self.parse_name_10)

        self.label_191 = QLabel(self.scrollAreaWidgetContents)
        self.label_191.setObjectName(u"label_191")
        sizePolicy2.setHeightForWidth(self.label_191.sizePolicy().hasHeightForWidth())
        self.label_191.setSizePolicy(sizePolicy2)
        self.label_191.setMinimumSize(QSize(50, 25))

        self.hl_parse010.addWidget(self.label_191)

        self.parse_pattern_10 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_pattern_10.setObjectName(u"parse_pattern_10")
        sizePolicy1.setHeightForWidth(self.parse_pattern_10.sizePolicy().hasHeightForWidth())
        self.parse_pattern_10.setSizePolicy(sizePolicy1)
        self.parse_pattern_10.setMinimumSize(QSize(100, 25))

        self.hl_parse010.addWidget(self.parse_pattern_10)

        self.label_192 = QLabel(self.scrollAreaWidgetContents)
        self.label_192.setObjectName(u"label_192")
        sizePolicy2.setHeightForWidth(self.label_192.sizePolicy().hasHeightForWidth())
        self.label_192.setSizePolicy(sizePolicy2)
        self.label_192.setMinimumSize(QSize(50, 25))

        self.hl_parse010.addWidget(self.label_192)

        self.parse_repl_10 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_repl_10.setObjectName(u"parse_repl_10")
        sizePolicy1.setHeightForWidth(self.parse_repl_10.sizePolicy().hasHeightForWidth())
        self.parse_repl_10.setSizePolicy(sizePolicy1)
        self.parse_repl_10.setMinimumSize(QSize(80, 25))
        self.parse_repl_10.setMaximumSize(QSize(1600, 16777215))

        self.hl_parse010.addWidget(self.parse_repl_10)

        self.label_193 = QLabel(self.scrollAreaWidgetContents)
        self.label_193.setObjectName(u"label_193")
        sizePolicy2.setHeightForWidth(self.label_193.sizePolicy().hasHeightForWidth())
        self.label_193.setSizePolicy(sizePolicy2)
        self.label_193.setMinimumSize(QSize(50, 25))

        self.hl_parse010.addWidget(self.label_193)

        self.parse_source_10 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_source_10.setObjectName(u"parse_source_10")
        sizePolicy1.setHeightForWidth(self.parse_source_10.sizePolicy().hasHeightForWidth())
        self.parse_source_10.setSizePolicy(sizePolicy1)
        self.parse_source_10.setMinimumSize(QSize(30, 25))
        self.parse_source_10.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse010.addWidget(self.parse_source_10)

        self.label_194 = QLabel(self.scrollAreaWidgetContents)
        self.label_194.setObjectName(u"label_194")
        sizePolicy2.setHeightForWidth(self.label_194.sizePolicy().hasHeightForWidth())
        self.label_194.setSizePolicy(sizePolicy2)
        self.label_194.setMinimumSize(QSize(40, 25))

        self.hl_parse010.addWidget(self.label_194)

        self.parse_filter_10 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_filter_10.setObjectName(u"parse_filter_10")
        sizePolicy1.setHeightForWidth(self.parse_filter_10.sizePolicy().hasHeightForWidth())
        self.parse_filter_10.setSizePolicy(sizePolicy1)
        self.parse_filter_10.setMinimumSize(QSize(30, 25))
        self.parse_filter_10.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse010.addWidget(self.parse_filter_10)


        self.verticalLayout_30.addLayout(self.hl_parse010)

        self.hl_parse011 = QHBoxLayout()
        self.hl_parse011.setObjectName(u"hl_parse011")
        self.label_59 = QLabel(self.scrollAreaWidgetContents)
        self.label_59.setObjectName(u"label_59")
        sizePolicy2.setHeightForWidth(self.label_59.sizePolicy().hasHeightForWidth())
        self.label_59.setSizePolicy(sizePolicy2)
        self.label_59.setMinimumSize(QSize(50, 25))

        self.hl_parse011.addWidget(self.label_59)

        self.parse_name_11 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_name_11.setObjectName(u"parse_name_11")
        sizePolicy1.setHeightForWidth(self.parse_name_11.sizePolicy().hasHeightForWidth())
        self.parse_name_11.setSizePolicy(sizePolicy1)
        self.parse_name_11.setMinimumSize(QSize(30, 25))
        self.parse_name_11.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse011.addWidget(self.parse_name_11)

        self.label_60 = QLabel(self.scrollAreaWidgetContents)
        self.label_60.setObjectName(u"label_60")
        sizePolicy2.setHeightForWidth(self.label_60.sizePolicy().hasHeightForWidth())
        self.label_60.setSizePolicy(sizePolicy2)
        self.label_60.setMinimumSize(QSize(50, 25))

        self.hl_parse011.addWidget(self.label_60)

        self.parse_pattern_11 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_pattern_11.setObjectName(u"parse_pattern_11")
        sizePolicy1.setHeightForWidth(self.parse_pattern_11.sizePolicy().hasHeightForWidth())
        self.parse_pattern_11.setSizePolicy(sizePolicy1)
        self.parse_pattern_11.setMinimumSize(QSize(100, 25))

        self.hl_parse011.addWidget(self.parse_pattern_11)

        self.label_61 = QLabel(self.scrollAreaWidgetContents)
        self.label_61.setObjectName(u"label_61")
        sizePolicy2.setHeightForWidth(self.label_61.sizePolicy().hasHeightForWidth())
        self.label_61.setSizePolicy(sizePolicy2)
        self.label_61.setMinimumSize(QSize(50, 25))

        self.hl_parse011.addWidget(self.label_61)

        self.parse_repl_11 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_repl_11.setObjectName(u"parse_repl_11")
        sizePolicy1.setHeightForWidth(self.parse_repl_11.sizePolicy().hasHeightForWidth())
        self.parse_repl_11.setSizePolicy(sizePolicy1)
        self.parse_repl_11.setMinimumSize(QSize(80, 25))
        self.parse_repl_11.setMaximumSize(QSize(1600, 16777215))

        self.hl_parse011.addWidget(self.parse_repl_11)

        self.label_62 = QLabel(self.scrollAreaWidgetContents)
        self.label_62.setObjectName(u"label_62")
        sizePolicy2.setHeightForWidth(self.label_62.sizePolicy().hasHeightForWidth())
        self.label_62.setSizePolicy(sizePolicy2)
        self.label_62.setMinimumSize(QSize(50, 25))

        self.hl_parse011.addWidget(self.label_62)

        self.parse_source_11 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_source_11.setObjectName(u"parse_source_11")
        sizePolicy1.setHeightForWidth(self.parse_source_11.sizePolicy().hasHeightForWidth())
        self.parse_source_11.setSizePolicy(sizePolicy1)
        self.parse_source_11.setMinimumSize(QSize(30, 25))
        self.parse_source_11.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse011.addWidget(self.parse_source_11)

        self.label_82 = QLabel(self.scrollAreaWidgetContents)
        self.label_82.setObjectName(u"label_82")
        sizePolicy2.setHeightForWidth(self.label_82.sizePolicy().hasHeightForWidth())
        self.label_82.setSizePolicy(sizePolicy2)
        self.label_82.setMinimumSize(QSize(40, 25))

        self.hl_parse011.addWidget(self.label_82)

        self.parse_filter_11 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_filter_11.setObjectName(u"parse_filter_11")
        sizePolicy1.setHeightForWidth(self.parse_filter_11.sizePolicy().hasHeightForWidth())
        self.parse_filter_11.setSizePolicy(sizePolicy1)
        self.parse_filter_11.setMinimumSize(QSize(30, 25))
        self.parse_filter_11.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse011.addWidget(self.parse_filter_11)


        self.verticalLayout_30.addLayout(self.hl_parse011)

        self.hl_parse012 = QHBoxLayout()
        self.hl_parse012.setObjectName(u"hl_parse012")
        self.label_195 = QLabel(self.scrollAreaWidgetContents)
        self.label_195.setObjectName(u"label_195")
        sizePolicy2.setHeightForWidth(self.label_195.sizePolicy().hasHeightForWidth())
        self.label_195.setSizePolicy(sizePolicy2)
        self.label_195.setMinimumSize(QSize(50, 25))

        self.hl_parse012.addWidget(self.label_195)

        self.parse_name_12 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_name_12.setObjectName(u"parse_name_12")
        sizePolicy1.setHeightForWidth(self.parse_name_12.sizePolicy().hasHeightForWidth())
        self.parse_name_12.setSizePolicy(sizePolicy1)
        self.parse_name_12.setMinimumSize(QSize(30, 25))
        self.parse_name_12.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse012.addWidget(self.parse_name_12)

        self.label_196 = QLabel(self.scrollAreaWidgetContents)
        self.label_196.setObjectName(u"label_196")
        sizePolicy2.setHeightForWidth(self.label_196.sizePolicy().hasHeightForWidth())
        self.label_196.setSizePolicy(sizePolicy2)
        self.label_196.setMinimumSize(QSize(50, 25))

        self.hl_parse012.addWidget(self.label_196)

        self.parse_pattern_12 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_pattern_12.setObjectName(u"parse_pattern_12")
        sizePolicy1.setHeightForWidth(self.parse_pattern_12.sizePolicy().hasHeightForWidth())
        self.parse_pattern_12.setSizePolicy(sizePolicy1)
        self.parse_pattern_12.setMinimumSize(QSize(100, 25))

        self.hl_parse012.addWidget(self.parse_pattern_12)

        self.label_197 = QLabel(self.scrollAreaWidgetContents)
        self.label_197.setObjectName(u"label_197")
        sizePolicy2.setHeightForWidth(self.label_197.sizePolicy().hasHeightForWidth())
        self.label_197.setSizePolicy(sizePolicy2)
        self.label_197.setMinimumSize(QSize(50, 25))

        self.hl_parse012.addWidget(self.label_197)

        self.parse_repl_12 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_repl_12.setObjectName(u"parse_repl_12")
        sizePolicy1.setHeightForWidth(self.parse_repl_12.sizePolicy().hasHeightForWidth())
        self.parse_repl_12.setSizePolicy(sizePolicy1)
        self.parse_repl_12.setMinimumSize(QSize(80, 25))
        self.parse_repl_12.setMaximumSize(QSize(1600, 16777215))

        self.hl_parse012.addWidget(self.parse_repl_12)

        self.label_198 = QLabel(self.scrollAreaWidgetContents)
        self.label_198.setObjectName(u"label_198")
        sizePolicy2.setHeightForWidth(self.label_198.sizePolicy().hasHeightForWidth())
        self.label_198.setSizePolicy(sizePolicy2)
        self.label_198.setMinimumSize(QSize(50, 25))

        self.hl_parse012.addWidget(self.label_198)

        self.parse_source_12 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_source_12.setObjectName(u"parse_source_12")
        sizePolicy1.setHeightForWidth(self.parse_source_12.sizePolicy().hasHeightForWidth())
        self.parse_source_12.setSizePolicy(sizePolicy1)
        self.parse_source_12.setMinimumSize(QSize(30, 25))
        self.parse_source_12.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse012.addWidget(self.parse_source_12)

        self.label_199 = QLabel(self.scrollAreaWidgetContents)
        self.label_199.setObjectName(u"label_199")
        sizePolicy2.setHeightForWidth(self.label_199.sizePolicy().hasHeightForWidth())
        self.label_199.setSizePolicy(sizePolicy2)
        self.label_199.setMinimumSize(QSize(40, 25))

        self.hl_parse012.addWidget(self.label_199)

        self.parse_filter_12 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_filter_12.setObjectName(u"parse_filter_12")
        sizePolicy1.setHeightForWidth(self.parse_filter_12.sizePolicy().hasHeightForWidth())
        self.parse_filter_12.setSizePolicy(sizePolicy1)
        self.parse_filter_12.setMinimumSize(QSize(30, 25))
        self.parse_filter_12.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse012.addWidget(self.parse_filter_12)


        self.verticalLayout_30.addLayout(self.hl_parse012)

        self.hl_parse013 = QHBoxLayout()
        self.hl_parse013.setObjectName(u"hl_parse013")
        self.label_63 = QLabel(self.scrollAreaWidgetContents)
        self.label_63.setObjectName(u"label_63")
        sizePolicy2.setHeightForWidth(self.label_63.sizePolicy().hasHeightForWidth())
        self.label_63.setSizePolicy(sizePolicy2)
        self.label_63.setMinimumSize(QSize(50, 25))

        self.hl_parse013.addWidget(self.label_63)

        self.parse_name_13 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_name_13.setObjectName(u"parse_name_13")
        sizePolicy1.setHeightForWidth(self.parse_name_13.sizePolicy().hasHeightForWidth())
        self.parse_name_13.setSizePolicy(sizePolicy1)
        self.parse_name_13.setMinimumSize(QSize(30, 25))
        self.parse_name_13.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse013.addWidget(self.parse_name_13)

        self.label_64 = QLabel(self.scrollAreaWidgetContents)
        self.label_64.setObjectName(u"label_64")
        sizePolicy2.setHeightForWidth(self.label_64.sizePolicy().hasHeightForWidth())
        self.label_64.setSizePolicy(sizePolicy2)
        self.label_64.setMinimumSize(QSize(50, 25))

        self.hl_parse013.addWidget(self.label_64)

        self.parse_pattern_13 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_pattern_13.setObjectName(u"parse_pattern_13")
        sizePolicy1.setHeightForWidth(self.parse_pattern_13.sizePolicy().hasHeightForWidth())
        self.parse_pattern_13.setSizePolicy(sizePolicy1)
        self.parse_pattern_13.setMinimumSize(QSize(100, 25))

        self.hl_parse013.addWidget(self.parse_pattern_13)

        self.label_65 = QLabel(self.scrollAreaWidgetContents)
        self.label_65.setObjectName(u"label_65")
        sizePolicy2.setHeightForWidth(self.label_65.sizePolicy().hasHeightForWidth())
        self.label_65.setSizePolicy(sizePolicy2)
        self.label_65.setMinimumSize(QSize(50, 25))

        self.hl_parse013.addWidget(self.label_65)

        self.parse_repl_13 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_repl_13.setObjectName(u"parse_repl_13")
        sizePolicy1.setHeightForWidth(self.parse_repl_13.sizePolicy().hasHeightForWidth())
        self.parse_repl_13.setSizePolicy(sizePolicy1)
        self.parse_repl_13.setMinimumSize(QSize(80, 25))
        self.parse_repl_13.setMaximumSize(QSize(1600, 16777215))

        self.hl_parse013.addWidget(self.parse_repl_13)

        self.label_66 = QLabel(self.scrollAreaWidgetContents)
        self.label_66.setObjectName(u"label_66")
        sizePolicy2.setHeightForWidth(self.label_66.sizePolicy().hasHeightForWidth())
        self.label_66.setSizePolicy(sizePolicy2)
        self.label_66.setMinimumSize(QSize(50, 25))

        self.hl_parse013.addWidget(self.label_66)

        self.parse_source_13 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_source_13.setObjectName(u"parse_source_13")
        sizePolicy1.setHeightForWidth(self.parse_source_13.sizePolicy().hasHeightForWidth())
        self.parse_source_13.setSizePolicy(sizePolicy1)
        self.parse_source_13.setMinimumSize(QSize(30, 25))
        self.parse_source_13.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse013.addWidget(self.parse_source_13)

        self.label_83 = QLabel(self.scrollAreaWidgetContents)
        self.label_83.setObjectName(u"label_83")
        sizePolicy2.setHeightForWidth(self.label_83.sizePolicy().hasHeightForWidth())
        self.label_83.setSizePolicy(sizePolicy2)
        self.label_83.setMinimumSize(QSize(40, 25))

        self.hl_parse013.addWidget(self.label_83)

        self.parse_filter_13 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_filter_13.setObjectName(u"parse_filter_13")
        sizePolicy1.setHeightForWidth(self.parse_filter_13.sizePolicy().hasHeightForWidth())
        self.parse_filter_13.setSizePolicy(sizePolicy1)
        self.parse_filter_13.setMinimumSize(QSize(30, 25))
        self.parse_filter_13.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse013.addWidget(self.parse_filter_13)


        self.verticalLayout_30.addLayout(self.hl_parse013)

        self.hl_parse014 = QHBoxLayout()
        self.hl_parse014.setObjectName(u"hl_parse014")
        self.label_200 = QLabel(self.scrollAreaWidgetContents)
        self.label_200.setObjectName(u"label_200")
        sizePolicy2.setHeightForWidth(self.label_200.sizePolicy().hasHeightForWidth())
        self.label_200.setSizePolicy(sizePolicy2)
        self.label_200.setMinimumSize(QSize(50, 25))

        self.hl_parse014.addWidget(self.label_200)

        self.parse_name_14 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_name_14.setObjectName(u"parse_name_14")
        sizePolicy1.setHeightForWidth(self.parse_name_14.sizePolicy().hasHeightForWidth())
        self.parse_name_14.setSizePolicy(sizePolicy1)
        self.parse_name_14.setMinimumSize(QSize(30, 25))
        self.parse_name_14.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse014.addWidget(self.parse_name_14)

        self.label_201 = QLabel(self.scrollAreaWidgetContents)
        self.label_201.setObjectName(u"label_201")
        sizePolicy2.setHeightForWidth(self.label_201.sizePolicy().hasHeightForWidth())
        self.label_201.setSizePolicy(sizePolicy2)
        self.label_201.setMinimumSize(QSize(50, 25))

        self.hl_parse014.addWidget(self.label_201)

        self.parse_pattern_14 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_pattern_14.setObjectName(u"parse_pattern_14")
        sizePolicy1.setHeightForWidth(self.parse_pattern_14.sizePolicy().hasHeightForWidth())
        self.parse_pattern_14.setSizePolicy(sizePolicy1)
        self.parse_pattern_14.setMinimumSize(QSize(100, 25))

        self.hl_parse014.addWidget(self.parse_pattern_14)

        self.label_202 = QLabel(self.scrollAreaWidgetContents)
        self.label_202.setObjectName(u"label_202")
        sizePolicy2.setHeightForWidth(self.label_202.sizePolicy().hasHeightForWidth())
        self.label_202.setSizePolicy(sizePolicy2)
        self.label_202.setMinimumSize(QSize(50, 25))

        self.hl_parse014.addWidget(self.label_202)

        self.parse_repl_14 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_repl_14.setObjectName(u"parse_repl_14")
        sizePolicy1.setHeightForWidth(self.parse_repl_14.sizePolicy().hasHeightForWidth())
        self.parse_repl_14.setSizePolicy(sizePolicy1)
        self.parse_repl_14.setMinimumSize(QSize(80, 25))
        self.parse_repl_14.setMaximumSize(QSize(1600, 16777215))

        self.hl_parse014.addWidget(self.parse_repl_14)

        self.label_203 = QLabel(self.scrollAreaWidgetContents)
        self.label_203.setObjectName(u"label_203")
        sizePolicy2.setHeightForWidth(self.label_203.sizePolicy().hasHeightForWidth())
        self.label_203.setSizePolicy(sizePolicy2)
        self.label_203.setMinimumSize(QSize(50, 25))

        self.hl_parse014.addWidget(self.label_203)

        self.parse_source_14 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_source_14.setObjectName(u"parse_source_14")
        sizePolicy1.setHeightForWidth(self.parse_source_14.sizePolicy().hasHeightForWidth())
        self.parse_source_14.setSizePolicy(sizePolicy1)
        self.parse_source_14.setMinimumSize(QSize(30, 25))
        self.parse_source_14.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse014.addWidget(self.parse_source_14)

        self.label_204 = QLabel(self.scrollAreaWidgetContents)
        self.label_204.setObjectName(u"label_204")
        sizePolicy2.setHeightForWidth(self.label_204.sizePolicy().hasHeightForWidth())
        self.label_204.setSizePolicy(sizePolicy2)
        self.label_204.setMinimumSize(QSize(40, 25))

        self.hl_parse014.addWidget(self.label_204)

        self.parse_filter_14 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_filter_14.setObjectName(u"parse_filter_14")
        sizePolicy1.setHeightForWidth(self.parse_filter_14.sizePolicy().hasHeightForWidth())
        self.parse_filter_14.setSizePolicy(sizePolicy1)
        self.parse_filter_14.setMinimumSize(QSize(30, 25))
        self.parse_filter_14.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse014.addWidget(self.parse_filter_14)


        self.verticalLayout_30.addLayout(self.hl_parse014)

        self.hl_parse015 = QHBoxLayout()
        self.hl_parse015.setObjectName(u"hl_parse015")
        self.label_205 = QLabel(self.scrollAreaWidgetContents)
        self.label_205.setObjectName(u"label_205")
        sizePolicy2.setHeightForWidth(self.label_205.sizePolicy().hasHeightForWidth())
        self.label_205.setSizePolicy(sizePolicy2)
        self.label_205.setMinimumSize(QSize(50, 25))

        self.hl_parse015.addWidget(self.label_205)

        self.parse_name_15 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_name_15.setObjectName(u"parse_name_15")
        sizePolicy1.setHeightForWidth(self.parse_name_15.sizePolicy().hasHeightForWidth())
        self.parse_name_15.setSizePolicy(sizePolicy1)
        self.parse_name_15.setMinimumSize(QSize(30, 25))
        self.parse_name_15.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse015.addWidget(self.parse_name_15)

        self.label_206 = QLabel(self.scrollAreaWidgetContents)
        self.label_206.setObjectName(u"label_206")
        sizePolicy2.setHeightForWidth(self.label_206.sizePolicy().hasHeightForWidth())
        self.label_206.setSizePolicy(sizePolicy2)
        self.label_206.setMinimumSize(QSize(50, 25))

        self.hl_parse015.addWidget(self.label_206)

        self.parse_pattern_15 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_pattern_15.setObjectName(u"parse_pattern_15")
        sizePolicy1.setHeightForWidth(self.parse_pattern_15.sizePolicy().hasHeightForWidth())
        self.parse_pattern_15.setSizePolicy(sizePolicy1)
        self.parse_pattern_15.setMinimumSize(QSize(100, 25))

        self.hl_parse015.addWidget(self.parse_pattern_15)

        self.label_207 = QLabel(self.scrollAreaWidgetContents)
        self.label_207.setObjectName(u"label_207")
        sizePolicy2.setHeightForWidth(self.label_207.sizePolicy().hasHeightForWidth())
        self.label_207.setSizePolicy(sizePolicy2)
        self.label_207.setMinimumSize(QSize(50, 25))

        self.hl_parse015.addWidget(self.label_207)

        self.parse_repl_15 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_repl_15.setObjectName(u"parse_repl_15")
        sizePolicy1.setHeightForWidth(self.parse_repl_15.sizePolicy().hasHeightForWidth())
        self.parse_repl_15.setSizePolicy(sizePolicy1)
        self.parse_repl_15.setMinimumSize(QSize(80, 25))
        self.parse_repl_15.setMaximumSize(QSize(1600, 16777215))

        self.hl_parse015.addWidget(self.parse_repl_15)

        self.label_208 = QLabel(self.scrollAreaWidgetContents)
        self.label_208.setObjectName(u"label_208")
        sizePolicy2.setHeightForWidth(self.label_208.sizePolicy().hasHeightForWidth())
        self.label_208.setSizePolicy(sizePolicy2)
        self.label_208.setMinimumSize(QSize(50, 25))

        self.hl_parse015.addWidget(self.label_208)

        self.parse_source_15 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_source_15.setObjectName(u"parse_source_15")
        sizePolicy1.setHeightForWidth(self.parse_source_15.sizePolicy().hasHeightForWidth())
        self.parse_source_15.setSizePolicy(sizePolicy1)
        self.parse_source_15.setMinimumSize(QSize(30, 25))
        self.parse_source_15.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse015.addWidget(self.parse_source_15)

        self.label_209 = QLabel(self.scrollAreaWidgetContents)
        self.label_209.setObjectName(u"label_209")
        sizePolicy2.setHeightForWidth(self.label_209.sizePolicy().hasHeightForWidth())
        self.label_209.setSizePolicy(sizePolicy2)
        self.label_209.setMinimumSize(QSize(40, 25))

        self.hl_parse015.addWidget(self.label_209)

        self.parse_filter_15 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_filter_15.setObjectName(u"parse_filter_15")
        sizePolicy1.setHeightForWidth(self.parse_filter_15.sizePolicy().hasHeightForWidth())
        self.parse_filter_15.setSizePolicy(sizePolicy1)
        self.parse_filter_15.setMinimumSize(QSize(30, 25))
        self.parse_filter_15.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse015.addWidget(self.parse_filter_15)


        self.verticalLayout_30.addLayout(self.hl_parse015)

        self.hl_parse016 = QHBoxLayout()
        self.hl_parse016.setObjectName(u"hl_parse016")
        self.label_67 = QLabel(self.scrollAreaWidgetContents)
        self.label_67.setObjectName(u"label_67")
        sizePolicy2.setHeightForWidth(self.label_67.sizePolicy().hasHeightForWidth())
        self.label_67.setSizePolicy(sizePolicy2)
        self.label_67.setMinimumSize(QSize(50, 25))

        self.hl_parse016.addWidget(self.label_67)

        self.parse_name_16 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_name_16.setObjectName(u"parse_name_16")
        sizePolicy1.setHeightForWidth(self.parse_name_16.sizePolicy().hasHeightForWidth())
        self.parse_name_16.setSizePolicy(sizePolicy1)
        self.parse_name_16.setMinimumSize(QSize(30, 25))
        self.parse_name_16.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse016.addWidget(self.parse_name_16)

        self.label_68 = QLabel(self.scrollAreaWidgetContents)
        self.label_68.setObjectName(u"label_68")
        sizePolicy2.setHeightForWidth(self.label_68.sizePolicy().hasHeightForWidth())
        self.label_68.setSizePolicy(sizePolicy2)
        self.label_68.setMinimumSize(QSize(50, 25))

        self.hl_parse016.addWidget(self.label_68)

        self.parse_pattern_16 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_pattern_16.setObjectName(u"parse_pattern_16")
        sizePolicy1.setHeightForWidth(self.parse_pattern_16.sizePolicy().hasHeightForWidth())
        self.parse_pattern_16.setSizePolicy(sizePolicy1)
        self.parse_pattern_16.setMinimumSize(QSize(100, 25))

        self.hl_parse016.addWidget(self.parse_pattern_16)

        self.label_69 = QLabel(self.scrollAreaWidgetContents)
        self.label_69.setObjectName(u"label_69")
        sizePolicy2.setHeightForWidth(self.label_69.sizePolicy().hasHeightForWidth())
        self.label_69.setSizePolicy(sizePolicy2)
        self.label_69.setMinimumSize(QSize(50, 25))

        self.hl_parse016.addWidget(self.label_69)

        self.parse_repl_16 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_repl_16.setObjectName(u"parse_repl_16")
        sizePolicy1.setHeightForWidth(self.parse_repl_16.sizePolicy().hasHeightForWidth())
        self.parse_repl_16.setSizePolicy(sizePolicy1)
        self.parse_repl_16.setMinimumSize(QSize(80, 25))
        self.parse_repl_16.setMaximumSize(QSize(1600, 16777215))

        self.hl_parse016.addWidget(self.parse_repl_16)

        self.label_70 = QLabel(self.scrollAreaWidgetContents)
        self.label_70.setObjectName(u"label_70")
        sizePolicy2.setHeightForWidth(self.label_70.sizePolicy().hasHeightForWidth())
        self.label_70.setSizePolicy(sizePolicy2)
        self.label_70.setMinimumSize(QSize(50, 25))

        self.hl_parse016.addWidget(self.label_70)

        self.parse_source_16 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_source_16.setObjectName(u"parse_source_16")
        sizePolicy1.setHeightForWidth(self.parse_source_16.sizePolicy().hasHeightForWidth())
        self.parse_source_16.setSizePolicy(sizePolicy1)
        self.parse_source_16.setMinimumSize(QSize(30, 25))
        self.parse_source_16.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse016.addWidget(self.parse_source_16)

        self.label_84 = QLabel(self.scrollAreaWidgetContents)
        self.label_84.setObjectName(u"label_84")
        sizePolicy2.setHeightForWidth(self.label_84.sizePolicy().hasHeightForWidth())
        self.label_84.setSizePolicy(sizePolicy2)
        self.label_84.setMinimumSize(QSize(40, 25))

        self.hl_parse016.addWidget(self.label_84)

        self.parse_filter_16 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_filter_16.setObjectName(u"parse_filter_16")
        sizePolicy1.setHeightForWidth(self.parse_filter_16.sizePolicy().hasHeightForWidth())
        self.parse_filter_16.setSizePolicy(sizePolicy1)
        self.parse_filter_16.setMinimumSize(QSize(30, 25))
        self.parse_filter_16.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse016.addWidget(self.parse_filter_16)


        self.verticalLayout_30.addLayout(self.hl_parse016)

        self.hl_parse017 = QHBoxLayout()
        self.hl_parse017.setObjectName(u"hl_parse017")
        self.label_210 = QLabel(self.scrollAreaWidgetContents)
        self.label_210.setObjectName(u"label_210")
        sizePolicy2.setHeightForWidth(self.label_210.sizePolicy().hasHeightForWidth())
        self.label_210.setSizePolicy(sizePolicy2)
        self.label_210.setMinimumSize(QSize(50, 25))

        self.hl_parse017.addWidget(self.label_210)

        self.parse_name_17 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_name_17.setObjectName(u"parse_name_17")
        sizePolicy1.setHeightForWidth(self.parse_name_17.sizePolicy().hasHeightForWidth())
        self.parse_name_17.setSizePolicy(sizePolicy1)
        self.parse_name_17.setMinimumSize(QSize(30, 25))
        self.parse_name_17.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse017.addWidget(self.parse_name_17)

        self.label_211 = QLabel(self.scrollAreaWidgetContents)
        self.label_211.setObjectName(u"label_211")
        sizePolicy2.setHeightForWidth(self.label_211.sizePolicy().hasHeightForWidth())
        self.label_211.setSizePolicy(sizePolicy2)
        self.label_211.setMinimumSize(QSize(50, 25))

        self.hl_parse017.addWidget(self.label_211)

        self.parse_pattern_17 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_pattern_17.setObjectName(u"parse_pattern_17")
        sizePolicy1.setHeightForWidth(self.parse_pattern_17.sizePolicy().hasHeightForWidth())
        self.parse_pattern_17.setSizePolicy(sizePolicy1)
        self.parse_pattern_17.setMinimumSize(QSize(100, 25))

        self.hl_parse017.addWidget(self.parse_pattern_17)

        self.label_212 = QLabel(self.scrollAreaWidgetContents)
        self.label_212.setObjectName(u"label_212")
        sizePolicy2.setHeightForWidth(self.label_212.sizePolicy().hasHeightForWidth())
        self.label_212.setSizePolicy(sizePolicy2)
        self.label_212.setMinimumSize(QSize(50, 25))

        self.hl_parse017.addWidget(self.label_212)

        self.parse_repl_17 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_repl_17.setObjectName(u"parse_repl_17")
        sizePolicy1.setHeightForWidth(self.parse_repl_17.sizePolicy().hasHeightForWidth())
        self.parse_repl_17.setSizePolicy(sizePolicy1)
        self.parse_repl_17.setMinimumSize(QSize(80, 25))
        self.parse_repl_17.setMaximumSize(QSize(1600, 16777215))

        self.hl_parse017.addWidget(self.parse_repl_17)

        self.label_213 = QLabel(self.scrollAreaWidgetContents)
        self.label_213.setObjectName(u"label_213")
        sizePolicy2.setHeightForWidth(self.label_213.sizePolicy().hasHeightForWidth())
        self.label_213.setSizePolicy(sizePolicy2)
        self.label_213.setMinimumSize(QSize(50, 25))

        self.hl_parse017.addWidget(self.label_213)

        self.parse_source_17 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_source_17.setObjectName(u"parse_source_17")
        sizePolicy1.setHeightForWidth(self.parse_source_17.sizePolicy().hasHeightForWidth())
        self.parse_source_17.setSizePolicy(sizePolicy1)
        self.parse_source_17.setMinimumSize(QSize(30, 25))
        self.parse_source_17.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse017.addWidget(self.parse_source_17)

        self.label_214 = QLabel(self.scrollAreaWidgetContents)
        self.label_214.setObjectName(u"label_214")
        sizePolicy2.setHeightForWidth(self.label_214.sizePolicy().hasHeightForWidth())
        self.label_214.setSizePolicy(sizePolicy2)
        self.label_214.setMinimumSize(QSize(40, 25))

        self.hl_parse017.addWidget(self.label_214)

        self.parse_filter_17 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_filter_17.setObjectName(u"parse_filter_17")
        sizePolicy1.setHeightForWidth(self.parse_filter_17.sizePolicy().hasHeightForWidth())
        self.parse_filter_17.setSizePolicy(sizePolicy1)
        self.parse_filter_17.setMinimumSize(QSize(30, 25))
        self.parse_filter_17.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse017.addWidget(self.parse_filter_17)


        self.verticalLayout_30.addLayout(self.hl_parse017)

        self.hl_parse018 = QHBoxLayout()
        self.hl_parse018.setObjectName(u"hl_parse018")
        self.label_71 = QLabel(self.scrollAreaWidgetContents)
        self.label_71.setObjectName(u"label_71")
        sizePolicy2.setHeightForWidth(self.label_71.sizePolicy().hasHeightForWidth())
        self.label_71.setSizePolicy(sizePolicy2)
        self.label_71.setMinimumSize(QSize(50, 25))

        self.hl_parse018.addWidget(self.label_71)

        self.parse_name_18 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_name_18.setObjectName(u"parse_name_18")
        sizePolicy1.setHeightForWidth(self.parse_name_18.sizePolicy().hasHeightForWidth())
        self.parse_name_18.setSizePolicy(sizePolicy1)
        self.parse_name_18.setMinimumSize(QSize(30, 25))
        self.parse_name_18.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse018.addWidget(self.parse_name_18)

        self.label_72 = QLabel(self.scrollAreaWidgetContents)
        self.label_72.setObjectName(u"label_72")
        sizePolicy2.setHeightForWidth(self.label_72.sizePolicy().hasHeightForWidth())
        self.label_72.setSizePolicy(sizePolicy2)
        self.label_72.setMinimumSize(QSize(50, 25))

        self.hl_parse018.addWidget(self.label_72)

        self.parse_pattern_18 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_pattern_18.setObjectName(u"parse_pattern_18")
        sizePolicy1.setHeightForWidth(self.parse_pattern_18.sizePolicy().hasHeightForWidth())
        self.parse_pattern_18.setSizePolicy(sizePolicy1)
        self.parse_pattern_18.setMinimumSize(QSize(100, 25))

        self.hl_parse018.addWidget(self.parse_pattern_18)

        self.label_73 = QLabel(self.scrollAreaWidgetContents)
        self.label_73.setObjectName(u"label_73")
        sizePolicy2.setHeightForWidth(self.label_73.sizePolicy().hasHeightForWidth())
        self.label_73.setSizePolicy(sizePolicy2)
        self.label_73.setMinimumSize(QSize(50, 25))

        self.hl_parse018.addWidget(self.label_73)

        self.parse_repl_18 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_repl_18.setObjectName(u"parse_repl_18")
        sizePolicy1.setHeightForWidth(self.parse_repl_18.sizePolicy().hasHeightForWidth())
        self.parse_repl_18.setSizePolicy(sizePolicy1)
        self.parse_repl_18.setMinimumSize(QSize(80, 25))
        self.parse_repl_18.setMaximumSize(QSize(1600, 16777215))

        self.hl_parse018.addWidget(self.parse_repl_18)

        self.label_74 = QLabel(self.scrollAreaWidgetContents)
        self.label_74.setObjectName(u"label_74")
        sizePolicy2.setHeightForWidth(self.label_74.sizePolicy().hasHeightForWidth())
        self.label_74.setSizePolicy(sizePolicy2)
        self.label_74.setMinimumSize(QSize(50, 25))

        self.hl_parse018.addWidget(self.label_74)

        self.parse_source_18 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_source_18.setObjectName(u"parse_source_18")
        sizePolicy1.setHeightForWidth(self.parse_source_18.sizePolicy().hasHeightForWidth())
        self.parse_source_18.setSizePolicy(sizePolicy1)
        self.parse_source_18.setMinimumSize(QSize(30, 25))
        self.parse_source_18.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse018.addWidget(self.parse_source_18)

        self.label_85 = QLabel(self.scrollAreaWidgetContents)
        self.label_85.setObjectName(u"label_85")
        sizePolicy2.setHeightForWidth(self.label_85.sizePolicy().hasHeightForWidth())
        self.label_85.setSizePolicy(sizePolicy2)
        self.label_85.setMinimumSize(QSize(40, 25))

        self.hl_parse018.addWidget(self.label_85)

        self.parse_filter_18 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_filter_18.setObjectName(u"parse_filter_18")
        sizePolicy1.setHeightForWidth(self.parse_filter_18.sizePolicy().hasHeightForWidth())
        self.parse_filter_18.setSizePolicy(sizePolicy1)
        self.parse_filter_18.setMinimumSize(QSize(30, 25))
        self.parse_filter_18.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse018.addWidget(self.parse_filter_18)


        self.verticalLayout_30.addLayout(self.hl_parse018)

        self.hl_parse019 = QHBoxLayout()
        self.hl_parse019.setObjectName(u"hl_parse019")
        self.label_215 = QLabel(self.scrollAreaWidgetContents)
        self.label_215.setObjectName(u"label_215")
        sizePolicy2.setHeightForWidth(self.label_215.sizePolicy().hasHeightForWidth())
        self.label_215.setSizePolicy(sizePolicy2)
        self.label_215.setMinimumSize(QSize(50, 25))

        self.hl_parse019.addWidget(self.label_215)

        self.parse_name_19 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_name_19.setObjectName(u"parse_name_19")
        sizePolicy1.setHeightForWidth(self.parse_name_19.sizePolicy().hasHeightForWidth())
        self.parse_name_19.setSizePolicy(sizePolicy1)
        self.parse_name_19.setMinimumSize(QSize(30, 25))
        self.parse_name_19.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse019.addWidget(self.parse_name_19)

        self.label_216 = QLabel(self.scrollAreaWidgetContents)
        self.label_216.setObjectName(u"label_216")
        sizePolicy2.setHeightForWidth(self.label_216.sizePolicy().hasHeightForWidth())
        self.label_216.setSizePolicy(sizePolicy2)
        self.label_216.setMinimumSize(QSize(50, 25))

        self.hl_parse019.addWidget(self.label_216)

        self.parse_pattern_19 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_pattern_19.setObjectName(u"parse_pattern_19")
        sizePolicy1.setHeightForWidth(self.parse_pattern_19.sizePolicy().hasHeightForWidth())
        self.parse_pattern_19.setSizePolicy(sizePolicy1)
        self.parse_pattern_19.setMinimumSize(QSize(100, 25))

        self.hl_parse019.addWidget(self.parse_pattern_19)

        self.label_217 = QLabel(self.scrollAreaWidgetContents)
        self.label_217.setObjectName(u"label_217")
        sizePolicy2.setHeightForWidth(self.label_217.sizePolicy().hasHeightForWidth())
        self.label_217.setSizePolicy(sizePolicy2)
        self.label_217.setMinimumSize(QSize(50, 25))

        self.hl_parse019.addWidget(self.label_217)

        self.parse_repl_19 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_repl_19.setObjectName(u"parse_repl_19")
        sizePolicy1.setHeightForWidth(self.parse_repl_19.sizePolicy().hasHeightForWidth())
        self.parse_repl_19.setSizePolicy(sizePolicy1)
        self.parse_repl_19.setMinimumSize(QSize(80, 25))
        self.parse_repl_19.setMaximumSize(QSize(1600, 16777215))

        self.hl_parse019.addWidget(self.parse_repl_19)

        self.label_218 = QLabel(self.scrollAreaWidgetContents)
        self.label_218.setObjectName(u"label_218")
        sizePolicy2.setHeightForWidth(self.label_218.sizePolicy().hasHeightForWidth())
        self.label_218.setSizePolicy(sizePolicy2)
        self.label_218.setMinimumSize(QSize(50, 25))

        self.hl_parse019.addWidget(self.label_218)

        self.parse_source_19 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_source_19.setObjectName(u"parse_source_19")
        sizePolicy1.setHeightForWidth(self.parse_source_19.sizePolicy().hasHeightForWidth())
        self.parse_source_19.setSizePolicy(sizePolicy1)
        self.parse_source_19.setMinimumSize(QSize(30, 25))
        self.parse_source_19.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse019.addWidget(self.parse_source_19)

        self.label_219 = QLabel(self.scrollAreaWidgetContents)
        self.label_219.setObjectName(u"label_219")
        sizePolicy2.setHeightForWidth(self.label_219.sizePolicy().hasHeightForWidth())
        self.label_219.setSizePolicy(sizePolicy2)
        self.label_219.setMinimumSize(QSize(40, 25))

        self.hl_parse019.addWidget(self.label_219)

        self.parse_filter_19 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_filter_19.setObjectName(u"parse_filter_19")
        sizePolicy1.setHeightForWidth(self.parse_filter_19.sizePolicy().hasHeightForWidth())
        self.parse_filter_19.setSizePolicy(sizePolicy1)
        self.parse_filter_19.setMinimumSize(QSize(30, 25))
        self.parse_filter_19.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse019.addWidget(self.parse_filter_19)


        self.verticalLayout_30.addLayout(self.hl_parse019)

        self.hl_parse020 = QHBoxLayout()
        self.hl_parse020.setObjectName(u"hl_parse020")
        self.label_87 = QLabel(self.scrollAreaWidgetContents)
        self.label_87.setObjectName(u"label_87")
        sizePolicy2.setHeightForWidth(self.label_87.sizePolicy().hasHeightForWidth())
        self.label_87.setSizePolicy(sizePolicy2)
        self.label_87.setMinimumSize(QSize(50, 25))

        self.hl_parse020.addWidget(self.label_87)

        self.parse_name_20 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_name_20.setObjectName(u"parse_name_20")
        sizePolicy1.setHeightForWidth(self.parse_name_20.sizePolicy().hasHeightForWidth())
        self.parse_name_20.setSizePolicy(sizePolicy1)
        self.parse_name_20.setMinimumSize(QSize(30, 25))
        self.parse_name_20.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse020.addWidget(self.parse_name_20)

        self.label_114 = QLabel(self.scrollAreaWidgetContents)
        self.label_114.setObjectName(u"label_114")
        sizePolicy2.setHeightForWidth(self.label_114.sizePolicy().hasHeightForWidth())
        self.label_114.setSizePolicy(sizePolicy2)
        self.label_114.setMinimumSize(QSize(50, 25))

        self.hl_parse020.addWidget(self.label_114)

        self.parse_pattern_20 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_pattern_20.setObjectName(u"parse_pattern_20")
        sizePolicy1.setHeightForWidth(self.parse_pattern_20.sizePolicy().hasHeightForWidth())
        self.parse_pattern_20.setSizePolicy(sizePolicy1)
        self.parse_pattern_20.setMinimumSize(QSize(100, 25))

        self.hl_parse020.addWidget(self.parse_pattern_20)

        self.label_115 = QLabel(self.scrollAreaWidgetContents)
        self.label_115.setObjectName(u"label_115")
        sizePolicy2.setHeightForWidth(self.label_115.sizePolicy().hasHeightForWidth())
        self.label_115.setSizePolicy(sizePolicy2)
        self.label_115.setMinimumSize(QSize(50, 25))

        self.hl_parse020.addWidget(self.label_115)

        self.parse_repl_20 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_repl_20.setObjectName(u"parse_repl_20")
        sizePolicy1.setHeightForWidth(self.parse_repl_20.sizePolicy().hasHeightForWidth())
        self.parse_repl_20.setSizePolicy(sizePolicy1)
        self.parse_repl_20.setMinimumSize(QSize(80, 25))
        self.parse_repl_20.setMaximumSize(QSize(1600, 16777215))

        self.hl_parse020.addWidget(self.parse_repl_20)

        self.label_116 = QLabel(self.scrollAreaWidgetContents)
        self.label_116.setObjectName(u"label_116")
        sizePolicy2.setHeightForWidth(self.label_116.sizePolicy().hasHeightForWidth())
        self.label_116.setSizePolicy(sizePolicy2)
        self.label_116.setMinimumSize(QSize(50, 25))

        self.hl_parse020.addWidget(self.label_116)

        self.parse_source_20 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_source_20.setObjectName(u"parse_source_20")
        sizePolicy1.setHeightForWidth(self.parse_source_20.sizePolicy().hasHeightForWidth())
        self.parse_source_20.setSizePolicy(sizePolicy1)
        self.parse_source_20.setMinimumSize(QSize(30, 25))
        self.parse_source_20.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse020.addWidget(self.parse_source_20)

        self.label_117 = QLabel(self.scrollAreaWidgetContents)
        self.label_117.setObjectName(u"label_117")
        sizePolicy2.setHeightForWidth(self.label_117.sizePolicy().hasHeightForWidth())
        self.label_117.setSizePolicy(sizePolicy2)
        self.label_117.setMinimumSize(QSize(40, 25))

        self.hl_parse020.addWidget(self.label_117)

        self.parse_filter_20 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_filter_20.setObjectName(u"parse_filter_20")
        sizePolicy1.setHeightForWidth(self.parse_filter_20.sizePolicy().hasHeightForWidth())
        self.parse_filter_20.setSizePolicy(sizePolicy1)
        self.parse_filter_20.setMinimumSize(QSize(30, 25))
        self.parse_filter_20.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse020.addWidget(self.parse_filter_20)


        self.verticalLayout_30.addLayout(self.hl_parse020)

        self.hl_parse021 = QHBoxLayout()
        self.hl_parse021.setObjectName(u"hl_parse021")
        self.label_220 = QLabel(self.scrollAreaWidgetContents)
        self.label_220.setObjectName(u"label_220")
        sizePolicy2.setHeightForWidth(self.label_220.sizePolicy().hasHeightForWidth())
        self.label_220.setSizePolicy(sizePolicy2)
        self.label_220.setMinimumSize(QSize(50, 25))

        self.hl_parse021.addWidget(self.label_220)

        self.parse_name_21 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_name_21.setObjectName(u"parse_name_21")
        sizePolicy1.setHeightForWidth(self.parse_name_21.sizePolicy().hasHeightForWidth())
        self.parse_name_21.setSizePolicy(sizePolicy1)
        self.parse_name_21.setMinimumSize(QSize(30, 25))
        self.parse_name_21.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse021.addWidget(self.parse_name_21)

        self.label_221 = QLabel(self.scrollAreaWidgetContents)
        self.label_221.setObjectName(u"label_221")
        sizePolicy2.setHeightForWidth(self.label_221.sizePolicy().hasHeightForWidth())
        self.label_221.setSizePolicy(sizePolicy2)
        self.label_221.setMinimumSize(QSize(50, 25))

        self.hl_parse021.addWidget(self.label_221)

        self.parse_pattern_21 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_pattern_21.setObjectName(u"parse_pattern_21")
        sizePolicy1.setHeightForWidth(self.parse_pattern_21.sizePolicy().hasHeightForWidth())
        self.parse_pattern_21.setSizePolicy(sizePolicy1)
        self.parse_pattern_21.setMinimumSize(QSize(100, 25))

        self.hl_parse021.addWidget(self.parse_pattern_21)

        self.label_222 = QLabel(self.scrollAreaWidgetContents)
        self.label_222.setObjectName(u"label_222")
        sizePolicy2.setHeightForWidth(self.label_222.sizePolicy().hasHeightForWidth())
        self.label_222.setSizePolicy(sizePolicy2)
        self.label_222.setMinimumSize(QSize(50, 25))

        self.hl_parse021.addWidget(self.label_222)

        self.parse_repl_21 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_repl_21.setObjectName(u"parse_repl_21")
        sizePolicy1.setHeightForWidth(self.parse_repl_21.sizePolicy().hasHeightForWidth())
        self.parse_repl_21.setSizePolicy(sizePolicy1)
        self.parse_repl_21.setMinimumSize(QSize(80, 25))
        self.parse_repl_21.setMaximumSize(QSize(1600, 16777215))

        self.hl_parse021.addWidget(self.parse_repl_21)

        self.label_223 = QLabel(self.scrollAreaWidgetContents)
        self.label_223.setObjectName(u"label_223")
        sizePolicy2.setHeightForWidth(self.label_223.sizePolicy().hasHeightForWidth())
        self.label_223.setSizePolicy(sizePolicy2)
        self.label_223.setMinimumSize(QSize(50, 25))

        self.hl_parse021.addWidget(self.label_223)

        self.parse_source_21 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_source_21.setObjectName(u"parse_source_21")
        sizePolicy1.setHeightForWidth(self.parse_source_21.sizePolicy().hasHeightForWidth())
        self.parse_source_21.setSizePolicy(sizePolicy1)
        self.parse_source_21.setMinimumSize(QSize(30, 25))
        self.parse_source_21.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse021.addWidget(self.parse_source_21)

        self.label_224 = QLabel(self.scrollAreaWidgetContents)
        self.label_224.setObjectName(u"label_224")
        sizePolicy2.setHeightForWidth(self.label_224.sizePolicy().hasHeightForWidth())
        self.label_224.setSizePolicy(sizePolicy2)
        self.label_224.setMinimumSize(QSize(40, 25))

        self.hl_parse021.addWidget(self.label_224)

        self.parse_filter_21 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_filter_21.setObjectName(u"parse_filter_21")
        sizePolicy1.setHeightForWidth(self.parse_filter_21.sizePolicy().hasHeightForWidth())
        self.parse_filter_21.setSizePolicy(sizePolicy1)
        self.parse_filter_21.setMinimumSize(QSize(30, 25))
        self.parse_filter_21.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse021.addWidget(self.parse_filter_21)


        self.verticalLayout_30.addLayout(self.hl_parse021)

        self.hl_parse022 = QHBoxLayout()
        self.hl_parse022.setObjectName(u"hl_parse022")
        self.label_118 = QLabel(self.scrollAreaWidgetContents)
        self.label_118.setObjectName(u"label_118")
        sizePolicy2.setHeightForWidth(self.label_118.sizePolicy().hasHeightForWidth())
        self.label_118.setSizePolicy(sizePolicy2)
        self.label_118.setMinimumSize(QSize(50, 25))

        self.hl_parse022.addWidget(self.label_118)

        self.parse_name_22 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_name_22.setObjectName(u"parse_name_22")
        sizePolicy1.setHeightForWidth(self.parse_name_22.sizePolicy().hasHeightForWidth())
        self.parse_name_22.setSizePolicy(sizePolicy1)
        self.parse_name_22.setMinimumSize(QSize(30, 25))
        self.parse_name_22.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse022.addWidget(self.parse_name_22)

        self.label_119 = QLabel(self.scrollAreaWidgetContents)
        self.label_119.setObjectName(u"label_119")
        sizePolicy2.setHeightForWidth(self.label_119.sizePolicy().hasHeightForWidth())
        self.label_119.setSizePolicy(sizePolicy2)
        self.label_119.setMinimumSize(QSize(50, 25))

        self.hl_parse022.addWidget(self.label_119)

        self.parse_pattern_22 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_pattern_22.setObjectName(u"parse_pattern_22")
        sizePolicy1.setHeightForWidth(self.parse_pattern_22.sizePolicy().hasHeightForWidth())
        self.parse_pattern_22.setSizePolicy(sizePolicy1)
        self.parse_pattern_22.setMinimumSize(QSize(100, 25))

        self.hl_parse022.addWidget(self.parse_pattern_22)

        self.label_120 = QLabel(self.scrollAreaWidgetContents)
        self.label_120.setObjectName(u"label_120")
        sizePolicy2.setHeightForWidth(self.label_120.sizePolicy().hasHeightForWidth())
        self.label_120.setSizePolicy(sizePolicy2)
        self.label_120.setMinimumSize(QSize(50, 25))

        self.hl_parse022.addWidget(self.label_120)

        self.parse_repl_22 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_repl_22.setObjectName(u"parse_repl_22")
        sizePolicy1.setHeightForWidth(self.parse_repl_22.sizePolicy().hasHeightForWidth())
        self.parse_repl_22.setSizePolicy(sizePolicy1)
        self.parse_repl_22.setMinimumSize(QSize(80, 25))
        self.parse_repl_22.setMaximumSize(QSize(1600, 16777215))

        self.hl_parse022.addWidget(self.parse_repl_22)

        self.label_121 = QLabel(self.scrollAreaWidgetContents)
        self.label_121.setObjectName(u"label_121")
        sizePolicy2.setHeightForWidth(self.label_121.sizePolicy().hasHeightForWidth())
        self.label_121.setSizePolicy(sizePolicy2)
        self.label_121.setMinimumSize(QSize(50, 25))

        self.hl_parse022.addWidget(self.label_121)

        self.parse_source_22 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_source_22.setObjectName(u"parse_source_22")
        sizePolicy1.setHeightForWidth(self.parse_source_22.sizePolicy().hasHeightForWidth())
        self.parse_source_22.setSizePolicy(sizePolicy1)
        self.parse_source_22.setMinimumSize(QSize(30, 25))
        self.parse_source_22.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse022.addWidget(self.parse_source_22)

        self.label_122 = QLabel(self.scrollAreaWidgetContents)
        self.label_122.setObjectName(u"label_122")
        sizePolicy2.setHeightForWidth(self.label_122.sizePolicy().hasHeightForWidth())
        self.label_122.setSizePolicy(sizePolicy2)
        self.label_122.setMinimumSize(QSize(40, 25))

        self.hl_parse022.addWidget(self.label_122)

        self.parse_filter_22 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_filter_22.setObjectName(u"parse_filter_22")
        sizePolicy1.setHeightForWidth(self.parse_filter_22.sizePolicy().hasHeightForWidth())
        self.parse_filter_22.setSizePolicy(sizePolicy1)
        self.parse_filter_22.setMinimumSize(QSize(30, 25))
        self.parse_filter_22.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse022.addWidget(self.parse_filter_22)


        self.verticalLayout_30.addLayout(self.hl_parse022)

        self.hl_parse023 = QHBoxLayout()
        self.hl_parse023.setObjectName(u"hl_parse023")
        self.label_225 = QLabel(self.scrollAreaWidgetContents)
        self.label_225.setObjectName(u"label_225")
        sizePolicy2.setHeightForWidth(self.label_225.sizePolicy().hasHeightForWidth())
        self.label_225.setSizePolicy(sizePolicy2)
        self.label_225.setMinimumSize(QSize(50, 25))

        self.hl_parse023.addWidget(self.label_225)

        self.parse_name_23 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_name_23.setObjectName(u"parse_name_23")
        sizePolicy1.setHeightForWidth(self.parse_name_23.sizePolicy().hasHeightForWidth())
        self.parse_name_23.setSizePolicy(sizePolicy1)
        self.parse_name_23.setMinimumSize(QSize(30, 25))
        self.parse_name_23.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse023.addWidget(self.parse_name_23)

        self.label_226 = QLabel(self.scrollAreaWidgetContents)
        self.label_226.setObjectName(u"label_226")
        sizePolicy2.setHeightForWidth(self.label_226.sizePolicy().hasHeightForWidth())
        self.label_226.setSizePolicy(sizePolicy2)
        self.label_226.setMinimumSize(QSize(50, 25))

        self.hl_parse023.addWidget(self.label_226)

        self.parse_pattern_23 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_pattern_23.setObjectName(u"parse_pattern_23")
        sizePolicy1.setHeightForWidth(self.parse_pattern_23.sizePolicy().hasHeightForWidth())
        self.parse_pattern_23.setSizePolicy(sizePolicy1)
        self.parse_pattern_23.setMinimumSize(QSize(100, 25))

        self.hl_parse023.addWidget(self.parse_pattern_23)

        self.label_227 = QLabel(self.scrollAreaWidgetContents)
        self.label_227.setObjectName(u"label_227")
        sizePolicy2.setHeightForWidth(self.label_227.sizePolicy().hasHeightForWidth())
        self.label_227.setSizePolicy(sizePolicy2)
        self.label_227.setMinimumSize(QSize(50, 25))

        self.hl_parse023.addWidget(self.label_227)

        self.parse_repl_23 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_repl_23.setObjectName(u"parse_repl_23")
        sizePolicy1.setHeightForWidth(self.parse_repl_23.sizePolicy().hasHeightForWidth())
        self.parse_repl_23.setSizePolicy(sizePolicy1)
        self.parse_repl_23.setMinimumSize(QSize(80, 25))
        self.parse_repl_23.setMaximumSize(QSize(1600, 16777215))

        self.hl_parse023.addWidget(self.parse_repl_23)

        self.label_228 = QLabel(self.scrollAreaWidgetContents)
        self.label_228.setObjectName(u"label_228")
        sizePolicy2.setHeightForWidth(self.label_228.sizePolicy().hasHeightForWidth())
        self.label_228.setSizePolicy(sizePolicy2)
        self.label_228.setMinimumSize(QSize(50, 25))

        self.hl_parse023.addWidget(self.label_228)

        self.parse_source_23 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_source_23.setObjectName(u"parse_source_23")
        sizePolicy1.setHeightForWidth(self.parse_source_23.sizePolicy().hasHeightForWidth())
        self.parse_source_23.setSizePolicy(sizePolicy1)
        self.parse_source_23.setMinimumSize(QSize(30, 25))
        self.parse_source_23.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse023.addWidget(self.parse_source_23)

        self.label_229 = QLabel(self.scrollAreaWidgetContents)
        self.label_229.setObjectName(u"label_229")
        sizePolicy2.setHeightForWidth(self.label_229.sizePolicy().hasHeightForWidth())
        self.label_229.setSizePolicy(sizePolicy2)
        self.label_229.setMinimumSize(QSize(40, 25))

        self.hl_parse023.addWidget(self.label_229)

        self.parse_filter_23 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_filter_23.setObjectName(u"parse_filter_23")
        sizePolicy1.setHeightForWidth(self.parse_filter_23.sizePolicy().hasHeightForWidth())
        self.parse_filter_23.setSizePolicy(sizePolicy1)
        self.parse_filter_23.setMinimumSize(QSize(30, 25))
        self.parse_filter_23.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse023.addWidget(self.parse_filter_23)


        self.verticalLayout_30.addLayout(self.hl_parse023)

        self.hl_parse024 = QHBoxLayout()
        self.hl_parse024.setObjectName(u"hl_parse024")
        self.label_123 = QLabel(self.scrollAreaWidgetContents)
        self.label_123.setObjectName(u"label_123")
        sizePolicy2.setHeightForWidth(self.label_123.sizePolicy().hasHeightForWidth())
        self.label_123.setSizePolicy(sizePolicy2)
        self.label_123.setMinimumSize(QSize(50, 25))

        self.hl_parse024.addWidget(self.label_123)

        self.parse_name_24 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_name_24.setObjectName(u"parse_name_24")
        sizePolicy1.setHeightForWidth(self.parse_name_24.sizePolicy().hasHeightForWidth())
        self.parse_name_24.setSizePolicy(sizePolicy1)
        self.parse_name_24.setMinimumSize(QSize(30, 25))
        self.parse_name_24.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse024.addWidget(self.parse_name_24)

        self.label_124 = QLabel(self.scrollAreaWidgetContents)
        self.label_124.setObjectName(u"label_124")
        sizePolicy2.setHeightForWidth(self.label_124.sizePolicy().hasHeightForWidth())
        self.label_124.setSizePolicy(sizePolicy2)
        self.label_124.setMinimumSize(QSize(50, 25))

        self.hl_parse024.addWidget(self.label_124)

        self.parse_pattern_24 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_pattern_24.setObjectName(u"parse_pattern_24")
        sizePolicy1.setHeightForWidth(self.parse_pattern_24.sizePolicy().hasHeightForWidth())
        self.parse_pattern_24.setSizePolicy(sizePolicy1)
        self.parse_pattern_24.setMinimumSize(QSize(100, 25))

        self.hl_parse024.addWidget(self.parse_pattern_24)

        self.label_125 = QLabel(self.scrollAreaWidgetContents)
        self.label_125.setObjectName(u"label_125")
        sizePolicy2.setHeightForWidth(self.label_125.sizePolicy().hasHeightForWidth())
        self.label_125.setSizePolicy(sizePolicy2)
        self.label_125.setMinimumSize(QSize(50, 25))

        self.hl_parse024.addWidget(self.label_125)

        self.parse_repl_24 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_repl_24.setObjectName(u"parse_repl_24")
        sizePolicy1.setHeightForWidth(self.parse_repl_24.sizePolicy().hasHeightForWidth())
        self.parse_repl_24.setSizePolicy(sizePolicy1)
        self.parse_repl_24.setMinimumSize(QSize(80, 25))
        self.parse_repl_24.setMaximumSize(QSize(1600, 16777215))

        self.hl_parse024.addWidget(self.parse_repl_24)

        self.label_126 = QLabel(self.scrollAreaWidgetContents)
        self.label_126.setObjectName(u"label_126")
        sizePolicy2.setHeightForWidth(self.label_126.sizePolicy().hasHeightForWidth())
        self.label_126.setSizePolicy(sizePolicy2)
        self.label_126.setMinimumSize(QSize(50, 25))

        self.hl_parse024.addWidget(self.label_126)

        self.parse_source_24 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_source_24.setObjectName(u"parse_source_24")
        sizePolicy1.setHeightForWidth(self.parse_source_24.sizePolicy().hasHeightForWidth())
        self.parse_source_24.setSizePolicy(sizePolicy1)
        self.parse_source_24.setMinimumSize(QSize(30, 25))
        self.parse_source_24.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse024.addWidget(self.parse_source_24)

        self.label_127 = QLabel(self.scrollAreaWidgetContents)
        self.label_127.setObjectName(u"label_127")
        sizePolicy2.setHeightForWidth(self.label_127.sizePolicy().hasHeightForWidth())
        self.label_127.setSizePolicy(sizePolicy2)
        self.label_127.setMinimumSize(QSize(40, 25))

        self.hl_parse024.addWidget(self.label_127)

        self.parse_filter_24 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_filter_24.setObjectName(u"parse_filter_24")
        sizePolicy1.setHeightForWidth(self.parse_filter_24.sizePolicy().hasHeightForWidth())
        self.parse_filter_24.setSizePolicy(sizePolicy1)
        self.parse_filter_24.setMinimumSize(QSize(30, 25))
        self.parse_filter_24.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse024.addWidget(self.parse_filter_24)


        self.verticalLayout_30.addLayout(self.hl_parse024)

        self.hl_parse025 = QHBoxLayout()
        self.hl_parse025.setObjectName(u"hl_parse025")
        self.label_230 = QLabel(self.scrollAreaWidgetContents)
        self.label_230.setObjectName(u"label_230")
        sizePolicy2.setHeightForWidth(self.label_230.sizePolicy().hasHeightForWidth())
        self.label_230.setSizePolicy(sizePolicy2)
        self.label_230.setMinimumSize(QSize(50, 25))

        self.hl_parse025.addWidget(self.label_230)

        self.parse_name_25 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_name_25.setObjectName(u"parse_name_25")
        sizePolicy1.setHeightForWidth(self.parse_name_25.sizePolicy().hasHeightForWidth())
        self.parse_name_25.setSizePolicy(sizePolicy1)
        self.parse_name_25.setMinimumSize(QSize(30, 25))
        self.parse_name_25.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse025.addWidget(self.parse_name_25)

        self.label_231 = QLabel(self.scrollAreaWidgetContents)
        self.label_231.setObjectName(u"label_231")
        sizePolicy2.setHeightForWidth(self.label_231.sizePolicy().hasHeightForWidth())
        self.label_231.setSizePolicy(sizePolicy2)
        self.label_231.setMinimumSize(QSize(50, 25))

        self.hl_parse025.addWidget(self.label_231)

        self.parse_pattern_25 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_pattern_25.setObjectName(u"parse_pattern_25")
        sizePolicy1.setHeightForWidth(self.parse_pattern_25.sizePolicy().hasHeightForWidth())
        self.parse_pattern_25.setSizePolicy(sizePolicy1)
        self.parse_pattern_25.setMinimumSize(QSize(100, 25))

        self.hl_parse025.addWidget(self.parse_pattern_25)

        self.label_232 = QLabel(self.scrollAreaWidgetContents)
        self.label_232.setObjectName(u"label_232")
        sizePolicy2.setHeightForWidth(self.label_232.sizePolicy().hasHeightForWidth())
        self.label_232.setSizePolicy(sizePolicy2)
        self.label_232.setMinimumSize(QSize(50, 25))

        self.hl_parse025.addWidget(self.label_232)

        self.parse_repl_25 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_repl_25.setObjectName(u"parse_repl_25")
        sizePolicy1.setHeightForWidth(self.parse_repl_25.sizePolicy().hasHeightForWidth())
        self.parse_repl_25.setSizePolicy(sizePolicy1)
        self.parse_repl_25.setMinimumSize(QSize(80, 25))
        self.parse_repl_25.setMaximumSize(QSize(1600, 16777215))

        self.hl_parse025.addWidget(self.parse_repl_25)

        self.label_233 = QLabel(self.scrollAreaWidgetContents)
        self.label_233.setObjectName(u"label_233")
        sizePolicy2.setHeightForWidth(self.label_233.sizePolicy().hasHeightForWidth())
        self.label_233.setSizePolicy(sizePolicy2)
        self.label_233.setMinimumSize(QSize(50, 25))

        self.hl_parse025.addWidget(self.label_233)

        self.parse_source_25 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_source_25.setObjectName(u"parse_source_25")
        sizePolicy1.setHeightForWidth(self.parse_source_25.sizePolicy().hasHeightForWidth())
        self.parse_source_25.setSizePolicy(sizePolicy1)
        self.parse_source_25.setMinimumSize(QSize(30, 25))
        self.parse_source_25.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse025.addWidget(self.parse_source_25)

        self.label_234 = QLabel(self.scrollAreaWidgetContents)
        self.label_234.setObjectName(u"label_234")
        sizePolicy2.setHeightForWidth(self.label_234.sizePolicy().hasHeightForWidth())
        self.label_234.setSizePolicy(sizePolicy2)
        self.label_234.setMinimumSize(QSize(40, 25))

        self.hl_parse025.addWidget(self.label_234)

        self.parse_filter_25 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_filter_25.setObjectName(u"parse_filter_25")
        sizePolicy1.setHeightForWidth(self.parse_filter_25.sizePolicy().hasHeightForWidth())
        self.parse_filter_25.setSizePolicy(sizePolicy1)
        self.parse_filter_25.setMinimumSize(QSize(30, 25))
        self.parse_filter_25.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse025.addWidget(self.parse_filter_25)


        self.verticalLayout_30.addLayout(self.hl_parse025)

        self.hl_parse026 = QHBoxLayout()
        self.hl_parse026.setObjectName(u"hl_parse026")
        self.label_128 = QLabel(self.scrollAreaWidgetContents)
        self.label_128.setObjectName(u"label_128")
        sizePolicy2.setHeightForWidth(self.label_128.sizePolicy().hasHeightForWidth())
        self.label_128.setSizePolicy(sizePolicy2)
        self.label_128.setMinimumSize(QSize(50, 25))

        self.hl_parse026.addWidget(self.label_128)

        self.parse_name_26 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_name_26.setObjectName(u"parse_name_26")
        sizePolicy1.setHeightForWidth(self.parse_name_26.sizePolicy().hasHeightForWidth())
        self.parse_name_26.setSizePolicy(sizePolicy1)
        self.parse_name_26.setMinimumSize(QSize(30, 25))
        self.parse_name_26.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse026.addWidget(self.parse_name_26)

        self.label_129 = QLabel(self.scrollAreaWidgetContents)
        self.label_129.setObjectName(u"label_129")
        sizePolicy2.setHeightForWidth(self.label_129.sizePolicy().hasHeightForWidth())
        self.label_129.setSizePolicy(sizePolicy2)
        self.label_129.setMinimumSize(QSize(50, 25))

        self.hl_parse026.addWidget(self.label_129)

        self.parse_pattern_26 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_pattern_26.setObjectName(u"parse_pattern_26")
        sizePolicy1.setHeightForWidth(self.parse_pattern_26.sizePolicy().hasHeightForWidth())
        self.parse_pattern_26.setSizePolicy(sizePolicy1)
        self.parse_pattern_26.setMinimumSize(QSize(100, 25))

        self.hl_parse026.addWidget(self.parse_pattern_26)

        self.label_130 = QLabel(self.scrollAreaWidgetContents)
        self.label_130.setObjectName(u"label_130")
        sizePolicy2.setHeightForWidth(self.label_130.sizePolicy().hasHeightForWidth())
        self.label_130.setSizePolicy(sizePolicy2)
        self.label_130.setMinimumSize(QSize(50, 25))

        self.hl_parse026.addWidget(self.label_130)

        self.parse_repl_26 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_repl_26.setObjectName(u"parse_repl_26")
        sizePolicy1.setHeightForWidth(self.parse_repl_26.sizePolicy().hasHeightForWidth())
        self.parse_repl_26.setSizePolicy(sizePolicy1)
        self.parse_repl_26.setMinimumSize(QSize(80, 25))
        self.parse_repl_26.setMaximumSize(QSize(1600, 16777215))

        self.hl_parse026.addWidget(self.parse_repl_26)

        self.label_131 = QLabel(self.scrollAreaWidgetContents)
        self.label_131.setObjectName(u"label_131")
        sizePolicy2.setHeightForWidth(self.label_131.sizePolicy().hasHeightForWidth())
        self.label_131.setSizePolicy(sizePolicy2)
        self.label_131.setMinimumSize(QSize(50, 25))

        self.hl_parse026.addWidget(self.label_131)

        self.parse_source_26 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_source_26.setObjectName(u"parse_source_26")
        sizePolicy1.setHeightForWidth(self.parse_source_26.sizePolicy().hasHeightForWidth())
        self.parse_source_26.setSizePolicy(sizePolicy1)
        self.parse_source_26.setMinimumSize(QSize(30, 25))
        self.parse_source_26.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse026.addWidget(self.parse_source_26)

        self.label_132 = QLabel(self.scrollAreaWidgetContents)
        self.label_132.setObjectName(u"label_132")
        sizePolicy2.setHeightForWidth(self.label_132.sizePolicy().hasHeightForWidth())
        self.label_132.setSizePolicy(sizePolicy2)
        self.label_132.setMinimumSize(QSize(40, 25))

        self.hl_parse026.addWidget(self.label_132)

        self.parse_filter_26 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_filter_26.setObjectName(u"parse_filter_26")
        sizePolicy1.setHeightForWidth(self.parse_filter_26.sizePolicy().hasHeightForWidth())
        self.parse_filter_26.setSizePolicy(sizePolicy1)
        self.parse_filter_26.setMinimumSize(QSize(30, 25))
        self.parse_filter_26.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse026.addWidget(self.parse_filter_26)


        self.verticalLayout_30.addLayout(self.hl_parse026)

        self.hl_parse027 = QHBoxLayout()
        self.hl_parse027.setObjectName(u"hl_parse027")
        self.label_235 = QLabel(self.scrollAreaWidgetContents)
        self.label_235.setObjectName(u"label_235")
        sizePolicy2.setHeightForWidth(self.label_235.sizePolicy().hasHeightForWidth())
        self.label_235.setSizePolicy(sizePolicy2)
        self.label_235.setMinimumSize(QSize(50, 25))

        self.hl_parse027.addWidget(self.label_235)

        self.parse_name_27 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_name_27.setObjectName(u"parse_name_27")
        sizePolicy1.setHeightForWidth(self.parse_name_27.sizePolicy().hasHeightForWidth())
        self.parse_name_27.setSizePolicy(sizePolicy1)
        self.parse_name_27.setMinimumSize(QSize(30, 25))
        self.parse_name_27.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse027.addWidget(self.parse_name_27)

        self.label_236 = QLabel(self.scrollAreaWidgetContents)
        self.label_236.setObjectName(u"label_236")
        sizePolicy2.setHeightForWidth(self.label_236.sizePolicy().hasHeightForWidth())
        self.label_236.setSizePolicy(sizePolicy2)
        self.label_236.setMinimumSize(QSize(50, 25))

        self.hl_parse027.addWidget(self.label_236)

        self.parse_pattern_27 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_pattern_27.setObjectName(u"parse_pattern_27")
        sizePolicy1.setHeightForWidth(self.parse_pattern_27.sizePolicy().hasHeightForWidth())
        self.parse_pattern_27.setSizePolicy(sizePolicy1)
        self.parse_pattern_27.setMinimumSize(QSize(100, 25))

        self.hl_parse027.addWidget(self.parse_pattern_27)

        self.label_237 = QLabel(self.scrollAreaWidgetContents)
        self.label_237.setObjectName(u"label_237")
        sizePolicy2.setHeightForWidth(self.label_237.sizePolicy().hasHeightForWidth())
        self.label_237.setSizePolicy(sizePolicy2)
        self.label_237.setMinimumSize(QSize(50, 25))

        self.hl_parse027.addWidget(self.label_237)

        self.parse_repl_27 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_repl_27.setObjectName(u"parse_repl_27")
        sizePolicy1.setHeightForWidth(self.parse_repl_27.sizePolicy().hasHeightForWidth())
        self.parse_repl_27.setSizePolicy(sizePolicy1)
        self.parse_repl_27.setMinimumSize(QSize(80, 25))
        self.parse_repl_27.setMaximumSize(QSize(1600, 16777215))

        self.hl_parse027.addWidget(self.parse_repl_27)

        self.label_238 = QLabel(self.scrollAreaWidgetContents)
        self.label_238.setObjectName(u"label_238")
        sizePolicy2.setHeightForWidth(self.label_238.sizePolicy().hasHeightForWidth())
        self.label_238.setSizePolicy(sizePolicy2)
        self.label_238.setMinimumSize(QSize(50, 25))

        self.hl_parse027.addWidget(self.label_238)

        self.parse_source_27 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_source_27.setObjectName(u"parse_source_27")
        sizePolicy1.setHeightForWidth(self.parse_source_27.sizePolicy().hasHeightForWidth())
        self.parse_source_27.setSizePolicy(sizePolicy1)
        self.parse_source_27.setMinimumSize(QSize(30, 25))
        self.parse_source_27.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse027.addWidget(self.parse_source_27)

        self.label_239 = QLabel(self.scrollAreaWidgetContents)
        self.label_239.setObjectName(u"label_239")
        sizePolicy2.setHeightForWidth(self.label_239.sizePolicy().hasHeightForWidth())
        self.label_239.setSizePolicy(sizePolicy2)
        self.label_239.setMinimumSize(QSize(40, 25))

        self.hl_parse027.addWidget(self.label_239)

        self.parse_filter_27 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_filter_27.setObjectName(u"parse_filter_27")
        sizePolicy1.setHeightForWidth(self.parse_filter_27.sizePolicy().hasHeightForWidth())
        self.parse_filter_27.setSizePolicy(sizePolicy1)
        self.parse_filter_27.setMinimumSize(QSize(30, 25))
        self.parse_filter_27.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse027.addWidget(self.parse_filter_27)


        self.verticalLayout_30.addLayout(self.hl_parse027)

        self.hl_parse028 = QHBoxLayout()
        self.hl_parse028.setObjectName(u"hl_parse028")
        self.label_133 = QLabel(self.scrollAreaWidgetContents)
        self.label_133.setObjectName(u"label_133")
        sizePolicy2.setHeightForWidth(self.label_133.sizePolicy().hasHeightForWidth())
        self.label_133.setSizePolicy(sizePolicy2)
        self.label_133.setMinimumSize(QSize(50, 25))

        self.hl_parse028.addWidget(self.label_133)

        self.parse_name_28 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_name_28.setObjectName(u"parse_name_28")
        sizePolicy1.setHeightForWidth(self.parse_name_28.sizePolicy().hasHeightForWidth())
        self.parse_name_28.setSizePolicy(sizePolicy1)
        self.parse_name_28.setMinimumSize(QSize(30, 25))
        self.parse_name_28.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse028.addWidget(self.parse_name_28)

        self.label_144 = QLabel(self.scrollAreaWidgetContents)
        self.label_144.setObjectName(u"label_144")
        sizePolicy2.setHeightForWidth(self.label_144.sizePolicy().hasHeightForWidth())
        self.label_144.setSizePolicy(sizePolicy2)
        self.label_144.setMinimumSize(QSize(50, 25))

        self.hl_parse028.addWidget(self.label_144)

        self.parse_pattern_28 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_pattern_28.setObjectName(u"parse_pattern_28")
        sizePolicy1.setHeightForWidth(self.parse_pattern_28.sizePolicy().hasHeightForWidth())
        self.parse_pattern_28.setSizePolicy(sizePolicy1)
        self.parse_pattern_28.setMinimumSize(QSize(100, 25))

        self.hl_parse028.addWidget(self.parse_pattern_28)

        self.label_145 = QLabel(self.scrollAreaWidgetContents)
        self.label_145.setObjectName(u"label_145")
        sizePolicy2.setHeightForWidth(self.label_145.sizePolicy().hasHeightForWidth())
        self.label_145.setSizePolicy(sizePolicy2)
        self.label_145.setMinimumSize(QSize(50, 25))

        self.hl_parse028.addWidget(self.label_145)

        self.parse_repl_28 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_repl_28.setObjectName(u"parse_repl_28")
        sizePolicy1.setHeightForWidth(self.parse_repl_28.sizePolicy().hasHeightForWidth())
        self.parse_repl_28.setSizePolicy(sizePolicy1)
        self.parse_repl_28.setMinimumSize(QSize(80, 25))
        self.parse_repl_28.setMaximumSize(QSize(1600, 16777215))

        self.hl_parse028.addWidget(self.parse_repl_28)

        self.label_146 = QLabel(self.scrollAreaWidgetContents)
        self.label_146.setObjectName(u"label_146")
        sizePolicy2.setHeightForWidth(self.label_146.sizePolicy().hasHeightForWidth())
        self.label_146.setSizePolicy(sizePolicy2)
        self.label_146.setMinimumSize(QSize(50, 25))

        self.hl_parse028.addWidget(self.label_146)

        self.parse_source_28 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_source_28.setObjectName(u"parse_source_28")
        sizePolicy1.setHeightForWidth(self.parse_source_28.sizePolicy().hasHeightForWidth())
        self.parse_source_28.setSizePolicy(sizePolicy1)
        self.parse_source_28.setMinimumSize(QSize(30, 25))
        self.parse_source_28.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse028.addWidget(self.parse_source_28)

        self.label_147 = QLabel(self.scrollAreaWidgetContents)
        self.label_147.setObjectName(u"label_147")
        sizePolicy2.setHeightForWidth(self.label_147.sizePolicy().hasHeightForWidth())
        self.label_147.setSizePolicy(sizePolicy2)
        self.label_147.setMinimumSize(QSize(40, 25))

        self.hl_parse028.addWidget(self.label_147)

        self.parse_filter_28 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_filter_28.setObjectName(u"parse_filter_28")
        sizePolicy1.setHeightForWidth(self.parse_filter_28.sizePolicy().hasHeightForWidth())
        self.parse_filter_28.setSizePolicy(sizePolicy1)
        self.parse_filter_28.setMinimumSize(QSize(30, 25))
        self.parse_filter_28.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse028.addWidget(self.parse_filter_28)


        self.verticalLayout_30.addLayout(self.hl_parse028)

        self.hl_parse029 = QHBoxLayout()
        self.hl_parse029.setObjectName(u"hl_parse029")
        self.label_240 = QLabel(self.scrollAreaWidgetContents)
        self.label_240.setObjectName(u"label_240")
        sizePolicy2.setHeightForWidth(self.label_240.sizePolicy().hasHeightForWidth())
        self.label_240.setSizePolicy(sizePolicy2)
        self.label_240.setMinimumSize(QSize(50, 25))

        self.hl_parse029.addWidget(self.label_240)

        self.parse_name_29 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_name_29.setObjectName(u"parse_name_29")
        sizePolicy1.setHeightForWidth(self.parse_name_29.sizePolicy().hasHeightForWidth())
        self.parse_name_29.setSizePolicy(sizePolicy1)
        self.parse_name_29.setMinimumSize(QSize(30, 25))
        self.parse_name_29.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse029.addWidget(self.parse_name_29)

        self.label_241 = QLabel(self.scrollAreaWidgetContents)
        self.label_241.setObjectName(u"label_241")
        sizePolicy2.setHeightForWidth(self.label_241.sizePolicy().hasHeightForWidth())
        self.label_241.setSizePolicy(sizePolicy2)
        self.label_241.setMinimumSize(QSize(50, 25))

        self.hl_parse029.addWidget(self.label_241)

        self.parse_pattern_29 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_pattern_29.setObjectName(u"parse_pattern_29")
        sizePolicy1.setHeightForWidth(self.parse_pattern_29.sizePolicy().hasHeightForWidth())
        self.parse_pattern_29.setSizePolicy(sizePolicy1)
        self.parse_pattern_29.setMinimumSize(QSize(100, 25))

        self.hl_parse029.addWidget(self.parse_pattern_29)

        self.label_242 = QLabel(self.scrollAreaWidgetContents)
        self.label_242.setObjectName(u"label_242")
        sizePolicy2.setHeightForWidth(self.label_242.sizePolicy().hasHeightForWidth())
        self.label_242.setSizePolicy(sizePolicy2)
        self.label_242.setMinimumSize(QSize(50, 25))

        self.hl_parse029.addWidget(self.label_242)

        self.parse_repl_29 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_repl_29.setObjectName(u"parse_repl_29")
        sizePolicy1.setHeightForWidth(self.parse_repl_29.sizePolicy().hasHeightForWidth())
        self.parse_repl_29.setSizePolicy(sizePolicy1)
        self.parse_repl_29.setMinimumSize(QSize(80, 25))
        self.parse_repl_29.setMaximumSize(QSize(1600, 16777215))

        self.hl_parse029.addWidget(self.parse_repl_29)

        self.label_243 = QLabel(self.scrollAreaWidgetContents)
        self.label_243.setObjectName(u"label_243")
        sizePolicy2.setHeightForWidth(self.label_243.sizePolicy().hasHeightForWidth())
        self.label_243.setSizePolicy(sizePolicy2)
        self.label_243.setMinimumSize(QSize(50, 25))

        self.hl_parse029.addWidget(self.label_243)

        self.parse_source_29 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_source_29.setObjectName(u"parse_source_29")
        sizePolicy1.setHeightForWidth(self.parse_source_29.sizePolicy().hasHeightForWidth())
        self.parse_source_29.setSizePolicy(sizePolicy1)
        self.parse_source_29.setMinimumSize(QSize(30, 25))
        self.parse_source_29.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse029.addWidget(self.parse_source_29)

        self.label_244 = QLabel(self.scrollAreaWidgetContents)
        self.label_244.setObjectName(u"label_244")
        sizePolicy2.setHeightForWidth(self.label_244.sizePolicy().hasHeightForWidth())
        self.label_244.setSizePolicy(sizePolicy2)
        self.label_244.setMinimumSize(QSize(40, 25))

        self.hl_parse029.addWidget(self.label_244)

        self.parse_filter_29 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_filter_29.setObjectName(u"parse_filter_29")
        sizePolicy1.setHeightForWidth(self.parse_filter_29.sizePolicy().hasHeightForWidth())
        self.parse_filter_29.setSizePolicy(sizePolicy1)
        self.parse_filter_29.setMinimumSize(QSize(30, 25))
        self.parse_filter_29.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse029.addWidget(self.parse_filter_29)


        self.verticalLayout_30.addLayout(self.hl_parse029)

        self.hl_parse030 = QHBoxLayout()
        self.hl_parse030.setObjectName(u"hl_parse030")
        self.label_148 = QLabel(self.scrollAreaWidgetContents)
        self.label_148.setObjectName(u"label_148")
        sizePolicy2.setHeightForWidth(self.label_148.sizePolicy().hasHeightForWidth())
        self.label_148.setSizePolicy(sizePolicy2)
        self.label_148.setMinimumSize(QSize(50, 25))

        self.hl_parse030.addWidget(self.label_148)

        self.parse_name_30 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_name_30.setObjectName(u"parse_name_30")
        sizePolicy1.setHeightForWidth(self.parse_name_30.sizePolicy().hasHeightForWidth())
        self.parse_name_30.setSizePolicy(sizePolicy1)
        self.parse_name_30.setMinimumSize(QSize(30, 25))
        self.parse_name_30.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse030.addWidget(self.parse_name_30)

        self.label_149 = QLabel(self.scrollAreaWidgetContents)
        self.label_149.setObjectName(u"label_149")
        sizePolicy2.setHeightForWidth(self.label_149.sizePolicy().hasHeightForWidth())
        self.label_149.setSizePolicy(sizePolicy2)
        self.label_149.setMinimumSize(QSize(50, 25))

        self.hl_parse030.addWidget(self.label_149)

        self.parse_pattern_30 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_pattern_30.setObjectName(u"parse_pattern_30")
        sizePolicy1.setHeightForWidth(self.parse_pattern_30.sizePolicy().hasHeightForWidth())
        self.parse_pattern_30.setSizePolicy(sizePolicy1)
        self.parse_pattern_30.setMinimumSize(QSize(100, 25))

        self.hl_parse030.addWidget(self.parse_pattern_30)

        self.label_150 = QLabel(self.scrollAreaWidgetContents)
        self.label_150.setObjectName(u"label_150")
        sizePolicy2.setHeightForWidth(self.label_150.sizePolicy().hasHeightForWidth())
        self.label_150.setSizePolicy(sizePolicy2)
        self.label_150.setMinimumSize(QSize(50, 25))

        self.hl_parse030.addWidget(self.label_150)

        self.parse_repl_30 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_repl_30.setObjectName(u"parse_repl_30")
        sizePolicy1.setHeightForWidth(self.parse_repl_30.sizePolicy().hasHeightForWidth())
        self.parse_repl_30.setSizePolicy(sizePolicy1)
        self.parse_repl_30.setMinimumSize(QSize(80, 25))
        self.parse_repl_30.setMaximumSize(QSize(1600, 16777215))

        self.hl_parse030.addWidget(self.parse_repl_30)

        self.label_151 = QLabel(self.scrollAreaWidgetContents)
        self.label_151.setObjectName(u"label_151")
        sizePolicy2.setHeightForWidth(self.label_151.sizePolicy().hasHeightForWidth())
        self.label_151.setSizePolicy(sizePolicy2)
        self.label_151.setMinimumSize(QSize(50, 25))

        self.hl_parse030.addWidget(self.label_151)

        self.parse_source_30 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_source_30.setObjectName(u"parse_source_30")
        sizePolicy1.setHeightForWidth(self.parse_source_30.sizePolicy().hasHeightForWidth())
        self.parse_source_30.setSizePolicy(sizePolicy1)
        self.parse_source_30.setMinimumSize(QSize(30, 25))
        self.parse_source_30.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse030.addWidget(self.parse_source_30)

        self.label_152 = QLabel(self.scrollAreaWidgetContents)
        self.label_152.setObjectName(u"label_152")
        sizePolicy2.setHeightForWidth(self.label_152.sizePolicy().hasHeightForWidth())
        self.label_152.setSizePolicy(sizePolicy2)
        self.label_152.setMinimumSize(QSize(40, 25))

        self.hl_parse030.addWidget(self.label_152)

        self.parse_filter_30 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_filter_30.setObjectName(u"parse_filter_30")
        sizePolicy1.setHeightForWidth(self.parse_filter_30.sizePolicy().hasHeightForWidth())
        self.parse_filter_30.setSizePolicy(sizePolicy1)
        self.parse_filter_30.setMinimumSize(QSize(30, 25))
        self.parse_filter_30.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse030.addWidget(self.parse_filter_30)


        self.verticalLayout_30.addLayout(self.hl_parse030)

        self.hl_parse031 = QHBoxLayout()
        self.hl_parse031.setObjectName(u"hl_parse031")
        self.label_153 = QLabel(self.scrollAreaWidgetContents)
        self.label_153.setObjectName(u"label_153")
        sizePolicy2.setHeightForWidth(self.label_153.sizePolicy().hasHeightForWidth())
        self.label_153.setSizePolicy(sizePolicy2)
        self.label_153.setMinimumSize(QSize(50, 25))

        self.hl_parse031.addWidget(self.label_153)

        self.parse_name_31 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_name_31.setObjectName(u"parse_name_31")
        sizePolicy1.setHeightForWidth(self.parse_name_31.sizePolicy().hasHeightForWidth())
        self.parse_name_31.setSizePolicy(sizePolicy1)
        self.parse_name_31.setMinimumSize(QSize(30, 25))
        self.parse_name_31.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse031.addWidget(self.parse_name_31)

        self.label_154 = QLabel(self.scrollAreaWidgetContents)
        self.label_154.setObjectName(u"label_154")
        sizePolicy2.setHeightForWidth(self.label_154.sizePolicy().hasHeightForWidth())
        self.label_154.setSizePolicy(sizePolicy2)
        self.label_154.setMinimumSize(QSize(50, 25))

        self.hl_parse031.addWidget(self.label_154)

        self.parse_pattern_31 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_pattern_31.setObjectName(u"parse_pattern_31")
        sizePolicy1.setHeightForWidth(self.parse_pattern_31.sizePolicy().hasHeightForWidth())
        self.parse_pattern_31.setSizePolicy(sizePolicy1)
        self.parse_pattern_31.setMinimumSize(QSize(100, 25))

        self.hl_parse031.addWidget(self.parse_pattern_31)

        self.label_155 = QLabel(self.scrollAreaWidgetContents)
        self.label_155.setObjectName(u"label_155")
        sizePolicy2.setHeightForWidth(self.label_155.sizePolicy().hasHeightForWidth())
        self.label_155.setSizePolicy(sizePolicy2)
        self.label_155.setMinimumSize(QSize(50, 25))

        self.hl_parse031.addWidget(self.label_155)

        self.parse_repl_31 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_repl_31.setObjectName(u"parse_repl_31")
        sizePolicy1.setHeightForWidth(self.parse_repl_31.sizePolicy().hasHeightForWidth())
        self.parse_repl_31.setSizePolicy(sizePolicy1)
        self.parse_repl_31.setMinimumSize(QSize(80, 25))
        self.parse_repl_31.setMaximumSize(QSize(1600, 16777215))

        self.hl_parse031.addWidget(self.parse_repl_31)

        self.label_156 = QLabel(self.scrollAreaWidgetContents)
        self.label_156.setObjectName(u"label_156")
        sizePolicy2.setHeightForWidth(self.label_156.sizePolicy().hasHeightForWidth())
        self.label_156.setSizePolicy(sizePolicy2)
        self.label_156.setMinimumSize(QSize(50, 25))

        self.hl_parse031.addWidget(self.label_156)

        self.parse_source_31 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_source_31.setObjectName(u"parse_source_31")
        sizePolicy1.setHeightForWidth(self.parse_source_31.sizePolicy().hasHeightForWidth())
        self.parse_source_31.setSizePolicy(sizePolicy1)
        self.parse_source_31.setMinimumSize(QSize(30, 25))
        self.parse_source_31.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse031.addWidget(self.parse_source_31)

        self.label_157 = QLabel(self.scrollAreaWidgetContents)
        self.label_157.setObjectName(u"label_157")
        sizePolicy2.setHeightForWidth(self.label_157.sizePolicy().hasHeightForWidth())
        self.label_157.setSizePolicy(sizePolicy2)
        self.label_157.setMinimumSize(QSize(40, 25))

        self.hl_parse031.addWidget(self.label_157)

        self.parse_filter_31 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_filter_31.setObjectName(u"parse_filter_31")
        sizePolicy1.setHeightForWidth(self.parse_filter_31.sizePolicy().hasHeightForWidth())
        self.parse_filter_31.setSizePolicy(sizePolicy1)
        self.parse_filter_31.setMinimumSize(QSize(30, 25))
        self.parse_filter_31.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse031.addWidget(self.parse_filter_31)


        self.verticalLayout_30.addLayout(self.hl_parse031)

        self.hl_parse032 = QHBoxLayout()
        self.hl_parse032.setObjectName(u"hl_parse032")
        self.label_165 = QLabel(self.scrollAreaWidgetContents)
        self.label_165.setObjectName(u"label_165")
        sizePolicy2.setHeightForWidth(self.label_165.sizePolicy().hasHeightForWidth())
        self.label_165.setSizePolicy(sizePolicy2)
        self.label_165.setMinimumSize(QSize(50, 25))

        self.hl_parse032.addWidget(self.label_165)

        self.parse_name_32 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_name_32.setObjectName(u"parse_name_32")
        sizePolicy1.setHeightForWidth(self.parse_name_32.sizePolicy().hasHeightForWidth())
        self.parse_name_32.setSizePolicy(sizePolicy1)
        self.parse_name_32.setMinimumSize(QSize(30, 25))
        self.parse_name_32.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse032.addWidget(self.parse_name_32)

        self.label_166 = QLabel(self.scrollAreaWidgetContents)
        self.label_166.setObjectName(u"label_166")
        sizePolicy2.setHeightForWidth(self.label_166.sizePolicy().hasHeightForWidth())
        self.label_166.setSizePolicy(sizePolicy2)
        self.label_166.setMinimumSize(QSize(50, 25))

        self.hl_parse032.addWidget(self.label_166)

        self.parse_pattern_32 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_pattern_32.setObjectName(u"parse_pattern_32")
        sizePolicy1.setHeightForWidth(self.parse_pattern_32.sizePolicy().hasHeightForWidth())
        self.parse_pattern_32.setSizePolicy(sizePolicy1)
        self.parse_pattern_32.setMinimumSize(QSize(100, 25))

        self.hl_parse032.addWidget(self.parse_pattern_32)

        self.label_167 = QLabel(self.scrollAreaWidgetContents)
        self.label_167.setObjectName(u"label_167")
        sizePolicy2.setHeightForWidth(self.label_167.sizePolicy().hasHeightForWidth())
        self.label_167.setSizePolicy(sizePolicy2)
        self.label_167.setMinimumSize(QSize(50, 25))

        self.hl_parse032.addWidget(self.label_167)

        self.parse_repl_32 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_repl_32.setObjectName(u"parse_repl_32")
        sizePolicy1.setHeightForWidth(self.parse_repl_32.sizePolicy().hasHeightForWidth())
        self.parse_repl_32.setSizePolicy(sizePolicy1)
        self.parse_repl_32.setMinimumSize(QSize(80, 25))
        self.parse_repl_32.setMaximumSize(QSize(1600, 16777215))

        self.hl_parse032.addWidget(self.parse_repl_32)

        self.label_168 = QLabel(self.scrollAreaWidgetContents)
        self.label_168.setObjectName(u"label_168")
        sizePolicy2.setHeightForWidth(self.label_168.sizePolicy().hasHeightForWidth())
        self.label_168.setSizePolicy(sizePolicy2)
        self.label_168.setMinimumSize(QSize(50, 25))

        self.hl_parse032.addWidget(self.label_168)

        self.parse_source_32 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_source_32.setObjectName(u"parse_source_32")
        sizePolicy1.setHeightForWidth(self.parse_source_32.sizePolicy().hasHeightForWidth())
        self.parse_source_32.setSizePolicy(sizePolicy1)
        self.parse_source_32.setMinimumSize(QSize(30, 25))
        self.parse_source_32.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse032.addWidget(self.parse_source_32)

        self.label_169 = QLabel(self.scrollAreaWidgetContents)
        self.label_169.setObjectName(u"label_169")
        sizePolicy2.setHeightForWidth(self.label_169.sizePolicy().hasHeightForWidth())
        self.label_169.setSizePolicy(sizePolicy2)
        self.label_169.setMinimumSize(QSize(40, 25))

        self.hl_parse032.addWidget(self.label_169)

        self.parse_filter_32 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_filter_32.setObjectName(u"parse_filter_32")
        sizePolicy1.setHeightForWidth(self.parse_filter_32.sizePolicy().hasHeightForWidth())
        self.parse_filter_32.setSizePolicy(sizePolicy1)
        self.parse_filter_32.setMinimumSize(QSize(30, 25))
        self.parse_filter_32.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse032.addWidget(self.parse_filter_32)


        self.verticalLayout_30.addLayout(self.hl_parse032)


        self.verticalLayout_31.addLayout(self.verticalLayout_30)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_24.addWidget(self.scrollArea)

        self.TopTab.addTab(self.tab_10, "")
        self.tab_13 = QWidget()
        self.tab_13.setObjectName(u"tab_13")
        self.verticalLayout_52 = QVBoxLayout(self.tab_13)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_46 = QVBoxLayout()
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.horizontalLayout_137 = QHBoxLayout()
        self.horizontalLayout_137.setObjectName(u"horizontalLayout_137")
        self.verticalLayout_44 = QVBoxLayout()
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.horizontalLayout_71 = QHBoxLayout()
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.horizontalLayout_62 = QHBoxLayout()
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.label_86 = QLabel(self.tab_13)
        self.label_86.setObjectName(u"label_86")
        sizePolicy2.setHeightForWidth(self.label_86.sizePolicy().hasHeightForWidth())
        self.label_86.setSizePolicy(sizePolicy2)
        self.label_86.setMinimumSize(QSize(85, 25))

        self.horizontalLayout_62.addWidget(self.label_86)

        self.side_folder = QLineEdit(self.tab_13)
        self.side_folder.setObjectName(u"side_folder")
        sizePolicy1.setHeightForWidth(self.side_folder.sizePolicy().hasHeightForWidth())
        self.side_folder.setSizePolicy(sizePolicy1)
        self.side_folder.setMinimumSize(QSize(100, 25))

        self.horizontalLayout_62.addWidget(self.side_folder)


        self.horizontalLayout_71.addLayout(self.horizontalLayout_62)

        self.horizontalLayout_61 = QHBoxLayout()
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.package_explore_2 = QPushButton(self.tab_13)
        self.package_explore_2.setObjectName(u"package_explore_2")
        sizePolicy2.setHeightForWidth(self.package_explore_2.sizePolicy().hasHeightForWidth())
        self.package_explore_2.setSizePolicy(sizePolicy2)
        self.package_explore_2.setMinimumSize(QSize(30, 25))
        self.package_explore_2.setAutoFillBackground(False)
        self.package_explore_2.setIcon(icon1)
        self.package_explore_2.setFlat(True)

        self.horizontalLayout_61.addWidget(self.package_explore_2)

        self.package_browse_2 = QPushButton(self.tab_13)
        self.package_browse_2.setObjectName(u"package_browse_2")
        sizePolicy2.setHeightForWidth(self.package_browse_2.sizePolicy().hasHeightForWidth())
        self.package_browse_2.setSizePolicy(sizePolicy2)
        self.package_browse_2.setMinimumSize(QSize(30, 25))
        self.package_browse_2.setMaximumSize(QSize(20, 24))
        self.package_browse_2.setAutoFillBackground(False)
        self.package_browse_2.setIcon(icon)
        self.package_browse_2.setFlat(True)

        self.horizontalLayout_61.addWidget(self.package_browse_2)


        self.horizontalLayout_71.addLayout(self.horizontalLayout_61)


        self.verticalLayout_44.addLayout(self.horizontalLayout_71)

        self.horizontalLayout_136 = QHBoxLayout()
        self.horizontalLayout_136.setObjectName(u"horizontalLayout_136")
        self.horizontalLayout_85 = QHBoxLayout()
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.label_92 = QLabel(self.tab_13)
        self.label_92.setObjectName(u"label_92")
        sizePolicy2.setHeightForWidth(self.label_92.sizePolicy().hasHeightForWidth())
        self.label_92.setSizePolicy(sizePolicy2)
        self.label_92.setMinimumSize(QSize(85, 25))
        self.label_92.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_85.addWidget(self.label_92)

        self.side_exclude = QLineEdit(self.tab_13)
        self.side_exclude.setObjectName(u"side_exclude")
        sizePolicy1.setHeightForWidth(self.side_exclude.sizePolicy().hasHeightForWidth())
        self.side_exclude.setSizePolicy(sizePolicy1)
        self.side_exclude.setMinimumSize(QSize(80, 25))

        self.horizontalLayout_85.addWidget(self.side_exclude)


        self.horizontalLayout_136.addLayout(self.horizontalLayout_85)

        self.horizontalLayout_83 = QHBoxLayout()
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.label_93 = QLabel(self.tab_13)
        self.label_93.setObjectName(u"label_93")
        sizePolicy2.setHeightForWidth(self.label_93.sizePolicy().hasHeightForWidth())
        self.label_93.setSizePolicy(sizePolicy2)
        self.label_93.setMinimumSize(QSize(60, 25))
        self.label_93.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_83.addWidget(self.label_93)

        self.side_include = QLineEdit(self.tab_13)
        self.side_include.setObjectName(u"side_include")
        sizePolicy1.setHeightForWidth(self.side_include.sizePolicy().hasHeightForWidth())
        self.side_include.setSizePolicy(sizePolicy1)
        self.side_include.setMinimumSize(QSize(80, 25))

        self.horizontalLayout_83.addWidget(self.side_include)


        self.horizontalLayout_136.addLayout(self.horizontalLayout_83)


        self.verticalLayout_44.addLayout(self.horizontalLayout_136)


        self.horizontalLayout_137.addLayout(self.verticalLayout_44)

        self.side_copy = QPushButton(self.tab_13)
        self.side_copy.setObjectName(u"side_copy")
        sizePolicy2.setHeightForWidth(self.side_copy.sizePolicy().hasHeightForWidth())
        self.side_copy.setSizePolicy(sizePolicy2)
        self.side_copy.setMinimumSize(QSize(150, 60))

        self.horizontalLayout_137.addWidget(self.side_copy)

        self.verticalLayout_43 = QVBoxLayout()
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.side_copywithgo = QCheckBox(self.tab_13)
        self.side_copywithgo.setObjectName(u"side_copywithgo")

        self.verticalLayout_43.addWidget(self.side_copywithgo)

        self.horizontalLayout_84 = QHBoxLayout()
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.side_sub_only = QRadioButton(self.tab_13)
        self.side_sub_only.setObjectName(u"side_sub_only")
        self.side_sub_only.setMinimumSize(QSize(120, 25))

        self.horizontalLayout_84.addWidget(self.side_sub_only)

        self.side_log_only = QRadioButton(self.tab_13)
        self.side_log_only.setObjectName(u"side_log_only")
        self.side_log_only.setMinimumSize(QSize(80, 25))

        self.horizontalLayout_84.addWidget(self.side_log_only)

        self.side_all = QRadioButton(self.tab_13)
        self.side_all.setObjectName(u"side_all")
        self.side_all.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_84.addWidget(self.side_all)


        self.verticalLayout_43.addLayout(self.horizontalLayout_84)


        self.horizontalLayout_137.addLayout(self.verticalLayout_43)


        self.verticalLayout_46.addLayout(self.horizontalLayout_137)

        self.line = QFrame(self.tab_13)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_46.addWidget(self.line)

        self.horizontalLayout_89 = QHBoxLayout()
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.horizontalLayout_86 = QHBoxLayout()
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.label_95 = QLabel(self.tab_13)
        self.label_95.setObjectName(u"label_95")
        sizePolicy2.setHeightForWidth(self.label_95.sizePolicy().hasHeightForWidth())
        self.label_95.setSizePolicy(sizePolicy2)
        self.label_95.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_86.addWidget(self.label_95)

        self.side_pattern_1 = QLineEdit(self.tab_13)
        self.side_pattern_1.setObjectName(u"side_pattern_1")
        sizePolicy1.setHeightForWidth(self.side_pattern_1.sizePolicy().hasHeightForWidth())
        self.side_pattern_1.setSizePolicy(sizePolicy1)
        self.side_pattern_1.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_86.addWidget(self.side_pattern_1)


        self.horizontalLayout_89.addLayout(self.horizontalLayout_86)

        self.horizontalLayout_87 = QHBoxLayout()
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.label_94 = QLabel(self.tab_13)
        self.label_94.setObjectName(u"label_94")
        sizePolicy2.setHeightForWidth(self.label_94.sizePolicy().hasHeightForWidth())
        self.label_94.setSizePolicy(sizePolicy2)
        self.label_94.setMinimumSize(QSize(30, 25))

        self.horizontalLayout_87.addWidget(self.label_94)

        self.side_repl_1 = QLineEdit(self.tab_13)
        self.side_repl_1.setObjectName(u"side_repl_1")
        sizePolicy1.setHeightForWidth(self.side_repl_1.sizePolicy().hasHeightForWidth())
        self.side_repl_1.setSizePolicy(sizePolicy1)
        self.side_repl_1.setMinimumSize(QSize(50, 25))
        self.side_repl_1.setMaximumSize(QSize(1600, 16777215))

        self.horizontalLayout_87.addWidget(self.side_repl_1)


        self.horizontalLayout_89.addLayout(self.horizontalLayout_87)

        self.horizontalLayout_88 = QHBoxLayout()
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.label_96 = QLabel(self.tab_13)
        self.label_96.setObjectName(u"label_96")
        sizePolicy2.setHeightForWidth(self.label_96.sizePolicy().hasHeightForWidth())
        self.label_96.setSizePolicy(sizePolicy2)
        self.label_96.setMinimumSize(QSize(75, 25))

        self.horizontalLayout_88.addWidget(self.label_96)

        self.side_match_1 = QLineEdit(self.tab_13)
        self.side_match_1.setObjectName(u"side_match_1")
        sizePolicy1.setHeightForWidth(self.side_match_1.sizePolicy().hasHeightForWidth())
        self.side_match_1.setSizePolicy(sizePolicy1)
        self.side_match_1.setMinimumSize(QSize(50, 25))
        self.side_match_1.setMaximumSize(QSize(1600, 16777215))

        self.horizontalLayout_88.addWidget(self.side_match_1)


        self.horizontalLayout_89.addLayout(self.horizontalLayout_88)

        self.horizontalLayout_90 = QHBoxLayout()
        self.horizontalLayout_90.setObjectName(u"horizontalLayout_90")
        self.label_97 = QLabel(self.tab_13)
        self.label_97.setObjectName(u"label_97")
        sizePolicy2.setHeightForWidth(self.label_97.sizePolicy().hasHeightForWidth())
        self.label_97.setSizePolicy(sizePolicy2)
        self.label_97.setMinimumSize(QSize(30, 25))

        self.horizontalLayout_90.addWidget(self.label_97)

        self.side_dest_1 = QLineEdit(self.tab_13)
        self.side_dest_1.setObjectName(u"side_dest_1")
        sizePolicy1.setHeightForWidth(self.side_dest_1.sizePolicy().hasHeightForWidth())
        self.side_dest_1.setSizePolicy(sizePolicy1)
        self.side_dest_1.setMinimumSize(QSize(50, 25))
        self.side_dest_1.setMaximumSize(QSize(1600, 16777215))

        self.horizontalLayout_90.addWidget(self.side_dest_1)


        self.horizontalLayout_89.addLayout(self.horizontalLayout_90)

        self.horizontalLayout_93 = QHBoxLayout()
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.label_98 = QLabel(self.tab_13)
        self.label_98.setObjectName(u"label_98")
        sizePolicy2.setHeightForWidth(self.label_98.sizePolicy().hasHeightForWidth())
        self.label_98.setSizePolicy(sizePolicy2)
        self.label_98.setMinimumSize(QSize(35, 25))

        self.horizontalLayout_93.addWidget(self.label_98)

        self.side_filter_1 = QLineEdit(self.tab_13)
        self.side_filter_1.setObjectName(u"side_filter_1")
        sizePolicy1.setHeightForWidth(self.side_filter_1.sizePolicy().hasHeightForWidth())
        self.side_filter_1.setSizePolicy(sizePolicy1)
        self.side_filter_1.setMinimumSize(QSize(50, 25))
        self.side_filter_1.setMaximumSize(QSize(1600, 16777215))

        self.horizontalLayout_93.addWidget(self.side_filter_1)


        self.horizontalLayout_89.addLayout(self.horizontalLayout_93)


        self.verticalLayout_46.addLayout(self.horizontalLayout_89)

        self.horizontalLayout_94 = QHBoxLayout()
        self.horizontalLayout_94.setObjectName(u"horizontalLayout_94")
        self.horizontalLayout_95 = QHBoxLayout()
        self.horizontalLayout_95.setObjectName(u"horizontalLayout_95")
        self.label_99 = QLabel(self.tab_13)
        self.label_99.setObjectName(u"label_99")
        sizePolicy2.setHeightForWidth(self.label_99.sizePolicy().hasHeightForWidth())
        self.label_99.setSizePolicy(sizePolicy2)
        self.label_99.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_95.addWidget(self.label_99)

        self.side_pattern_2 = QLineEdit(self.tab_13)
        self.side_pattern_2.setObjectName(u"side_pattern_2")
        sizePolicy1.setHeightForWidth(self.side_pattern_2.sizePolicy().hasHeightForWidth())
        self.side_pattern_2.setSizePolicy(sizePolicy1)
        self.side_pattern_2.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_95.addWidget(self.side_pattern_2)


        self.horizontalLayout_94.addLayout(self.horizontalLayout_95)

        self.horizontalLayout_96 = QHBoxLayout()
        self.horizontalLayout_96.setObjectName(u"horizontalLayout_96")
        self.label_100 = QLabel(self.tab_13)
        self.label_100.setObjectName(u"label_100")
        sizePolicy2.setHeightForWidth(self.label_100.sizePolicy().hasHeightForWidth())
        self.label_100.setSizePolicy(sizePolicy2)
        self.label_100.setMinimumSize(QSize(30, 25))

        self.horizontalLayout_96.addWidget(self.label_100)

        self.side_repl_2 = QLineEdit(self.tab_13)
        self.side_repl_2.setObjectName(u"side_repl_2")
        sizePolicy1.setHeightForWidth(self.side_repl_2.sizePolicy().hasHeightForWidth())
        self.side_repl_2.setSizePolicy(sizePolicy1)
        self.side_repl_2.setMinimumSize(QSize(50, 25))
        self.side_repl_2.setMaximumSize(QSize(1600, 16777215))

        self.horizontalLayout_96.addWidget(self.side_repl_2)


        self.horizontalLayout_94.addLayout(self.horizontalLayout_96)

        self.horizontalLayout_97 = QHBoxLayout()
        self.horizontalLayout_97.setObjectName(u"horizontalLayout_97")
        self.label_101 = QLabel(self.tab_13)
        self.label_101.setObjectName(u"label_101")
        sizePolicy2.setHeightForWidth(self.label_101.sizePolicy().hasHeightForWidth())
        self.label_101.setSizePolicy(sizePolicy2)
        self.label_101.setMinimumSize(QSize(75, 25))

        self.horizontalLayout_97.addWidget(self.label_101)

        self.side_match_2 = QLineEdit(self.tab_13)
        self.side_match_2.setObjectName(u"side_match_2")
        sizePolicy1.setHeightForWidth(self.side_match_2.sizePolicy().hasHeightForWidth())
        self.side_match_2.setSizePolicy(sizePolicy1)
        self.side_match_2.setMinimumSize(QSize(50, 25))
        self.side_match_2.setMaximumSize(QSize(1600, 16777215))

        self.horizontalLayout_97.addWidget(self.side_match_2)


        self.horizontalLayout_94.addLayout(self.horizontalLayout_97)

        self.horizontalLayout_98 = QHBoxLayout()
        self.horizontalLayout_98.setObjectName(u"horizontalLayout_98")
        self.label_102 = QLabel(self.tab_13)
        self.label_102.setObjectName(u"label_102")
        sizePolicy2.setHeightForWidth(self.label_102.sizePolicy().hasHeightForWidth())
        self.label_102.setSizePolicy(sizePolicy2)
        self.label_102.setMinimumSize(QSize(30, 25))

        self.horizontalLayout_98.addWidget(self.label_102)

        self.side_dest_2 = QLineEdit(self.tab_13)
        self.side_dest_2.setObjectName(u"side_dest_2")
        sizePolicy1.setHeightForWidth(self.side_dest_2.sizePolicy().hasHeightForWidth())
        self.side_dest_2.setSizePolicy(sizePolicy1)
        self.side_dest_2.setMinimumSize(QSize(50, 25))
        self.side_dest_2.setMaximumSize(QSize(1600, 16777215))

        self.horizontalLayout_98.addWidget(self.side_dest_2)


        self.horizontalLayout_94.addLayout(self.horizontalLayout_98)

        self.horizontalLayout_99 = QHBoxLayout()
        self.horizontalLayout_99.setObjectName(u"horizontalLayout_99")
        self.label_103 = QLabel(self.tab_13)
        self.label_103.setObjectName(u"label_103")
        sizePolicy2.setHeightForWidth(self.label_103.sizePolicy().hasHeightForWidth())
        self.label_103.setSizePolicy(sizePolicy2)
        self.label_103.setMinimumSize(QSize(35, 25))

        self.horizontalLayout_99.addWidget(self.label_103)

        self.side_filter_2 = QLineEdit(self.tab_13)
        self.side_filter_2.setObjectName(u"side_filter_2")
        sizePolicy1.setHeightForWidth(self.side_filter_2.sizePolicy().hasHeightForWidth())
        self.side_filter_2.setSizePolicy(sizePolicy1)
        self.side_filter_2.setMinimumSize(QSize(50, 25))
        self.side_filter_2.setMaximumSize(QSize(1600, 16777215))

        self.horizontalLayout_99.addWidget(self.side_filter_2)


        self.horizontalLayout_94.addLayout(self.horizontalLayout_99)


        self.verticalLayout_46.addLayout(self.horizontalLayout_94)

        self.horizontalLayout_100 = QHBoxLayout()
        self.horizontalLayout_100.setObjectName(u"horizontalLayout_100")
        self.horizontalLayout_101 = QHBoxLayout()
        self.horizontalLayout_101.setObjectName(u"horizontalLayout_101")
        self.label_104 = QLabel(self.tab_13)
        self.label_104.setObjectName(u"label_104")
        sizePolicy2.setHeightForWidth(self.label_104.sizePolicy().hasHeightForWidth())
        self.label_104.setSizePolicy(sizePolicy2)
        self.label_104.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_101.addWidget(self.label_104)

        self.side_pattern_3 = QLineEdit(self.tab_13)
        self.side_pattern_3.setObjectName(u"side_pattern_3")
        sizePolicy1.setHeightForWidth(self.side_pattern_3.sizePolicy().hasHeightForWidth())
        self.side_pattern_3.setSizePolicy(sizePolicy1)
        self.side_pattern_3.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_101.addWidget(self.side_pattern_3)


        self.horizontalLayout_100.addLayout(self.horizontalLayout_101)

        self.horizontalLayout_102 = QHBoxLayout()
        self.horizontalLayout_102.setObjectName(u"horizontalLayout_102")
        self.label_105 = QLabel(self.tab_13)
        self.label_105.setObjectName(u"label_105")
        sizePolicy2.setHeightForWidth(self.label_105.sizePolicy().hasHeightForWidth())
        self.label_105.setSizePolicy(sizePolicy2)
        self.label_105.setMinimumSize(QSize(30, 25))

        self.horizontalLayout_102.addWidget(self.label_105)

        self.side_repl_3 = QLineEdit(self.tab_13)
        self.side_repl_3.setObjectName(u"side_repl_3")
        sizePolicy1.setHeightForWidth(self.side_repl_3.sizePolicy().hasHeightForWidth())
        self.side_repl_3.setSizePolicy(sizePolicy1)
        self.side_repl_3.setMinimumSize(QSize(50, 25))
        self.side_repl_3.setMaximumSize(QSize(1600, 16777215))

        self.horizontalLayout_102.addWidget(self.side_repl_3)


        self.horizontalLayout_100.addLayout(self.horizontalLayout_102)

        self.horizontalLayout_103 = QHBoxLayout()
        self.horizontalLayout_103.setObjectName(u"horizontalLayout_103")
        self.label_106 = QLabel(self.tab_13)
        self.label_106.setObjectName(u"label_106")
        sizePolicy2.setHeightForWidth(self.label_106.sizePolicy().hasHeightForWidth())
        self.label_106.setSizePolicy(sizePolicy2)
        self.label_106.setMinimumSize(QSize(75, 25))

        self.horizontalLayout_103.addWidget(self.label_106)

        self.side_match_3 = QLineEdit(self.tab_13)
        self.side_match_3.setObjectName(u"side_match_3")
        sizePolicy1.setHeightForWidth(self.side_match_3.sizePolicy().hasHeightForWidth())
        self.side_match_3.setSizePolicy(sizePolicy1)
        self.side_match_3.setMinimumSize(QSize(50, 25))
        self.side_match_3.setMaximumSize(QSize(1600, 16777215))

        self.horizontalLayout_103.addWidget(self.side_match_3)


        self.horizontalLayout_100.addLayout(self.horizontalLayout_103)

        self.horizontalLayout_104 = QHBoxLayout()
        self.horizontalLayout_104.setObjectName(u"horizontalLayout_104")
        self.label_107 = QLabel(self.tab_13)
        self.label_107.setObjectName(u"label_107")
        sizePolicy2.setHeightForWidth(self.label_107.sizePolicy().hasHeightForWidth())
        self.label_107.setSizePolicy(sizePolicy2)
        self.label_107.setMinimumSize(QSize(30, 25))

        self.horizontalLayout_104.addWidget(self.label_107)

        self.side_dest_3 = QLineEdit(self.tab_13)
        self.side_dest_3.setObjectName(u"side_dest_3")
        sizePolicy1.setHeightForWidth(self.side_dest_3.sizePolicy().hasHeightForWidth())
        self.side_dest_3.setSizePolicy(sizePolicy1)
        self.side_dest_3.setMinimumSize(QSize(50, 25))
        self.side_dest_3.setMaximumSize(QSize(1600, 16777215))

        self.horizontalLayout_104.addWidget(self.side_dest_3)


        self.horizontalLayout_100.addLayout(self.horizontalLayout_104)

        self.horizontalLayout_105 = QHBoxLayout()
        self.horizontalLayout_105.setObjectName(u"horizontalLayout_105")
        self.label_108 = QLabel(self.tab_13)
        self.label_108.setObjectName(u"label_108")
        sizePolicy2.setHeightForWidth(self.label_108.sizePolicy().hasHeightForWidth())
        self.label_108.setSizePolicy(sizePolicy2)
        self.label_108.setMinimumSize(QSize(35, 25))

        self.horizontalLayout_105.addWidget(self.label_108)

        self.side_filter_3 = QLineEdit(self.tab_13)
        self.side_filter_3.setObjectName(u"side_filter_3")
        sizePolicy1.setHeightForWidth(self.side_filter_3.sizePolicy().hasHeightForWidth())
        self.side_filter_3.setSizePolicy(sizePolicy1)
        self.side_filter_3.setMinimumSize(QSize(50, 25))
        self.side_filter_3.setMaximumSize(QSize(1600, 16777215))

        self.horizontalLayout_105.addWidget(self.side_filter_3)


        self.horizontalLayout_100.addLayout(self.horizontalLayout_105)


        self.verticalLayout_46.addLayout(self.horizontalLayout_100)

        self.horizontalLayout_106 = QHBoxLayout()
        self.horizontalLayout_106.setObjectName(u"horizontalLayout_106")
        self.horizontalLayout_107 = QHBoxLayout()
        self.horizontalLayout_107.setObjectName(u"horizontalLayout_107")
        self.label_109 = QLabel(self.tab_13)
        self.label_109.setObjectName(u"label_109")
        sizePolicy2.setHeightForWidth(self.label_109.sizePolicy().hasHeightForWidth())
        self.label_109.setSizePolicy(sizePolicy2)
        self.label_109.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_107.addWidget(self.label_109)

        self.side_pattern_4 = QLineEdit(self.tab_13)
        self.side_pattern_4.setObjectName(u"side_pattern_4")
        sizePolicy1.setHeightForWidth(self.side_pattern_4.sizePolicy().hasHeightForWidth())
        self.side_pattern_4.setSizePolicy(sizePolicy1)
        self.side_pattern_4.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_107.addWidget(self.side_pattern_4)


        self.horizontalLayout_106.addLayout(self.horizontalLayout_107)

        self.horizontalLayout_108 = QHBoxLayout()
        self.horizontalLayout_108.setObjectName(u"horizontalLayout_108")
        self.label_110 = QLabel(self.tab_13)
        self.label_110.setObjectName(u"label_110")
        sizePolicy2.setHeightForWidth(self.label_110.sizePolicy().hasHeightForWidth())
        self.label_110.setSizePolicy(sizePolicy2)
        self.label_110.setMinimumSize(QSize(30, 25))

        self.horizontalLayout_108.addWidget(self.label_110)

        self.side_repl_4 = QLineEdit(self.tab_13)
        self.side_repl_4.setObjectName(u"side_repl_4")
        sizePolicy1.setHeightForWidth(self.side_repl_4.sizePolicy().hasHeightForWidth())
        self.side_repl_4.setSizePolicy(sizePolicy1)
        self.side_repl_4.setMinimumSize(QSize(50, 25))
        self.side_repl_4.setMaximumSize(QSize(1600, 16777215))

        self.horizontalLayout_108.addWidget(self.side_repl_4)


        self.horizontalLayout_106.addLayout(self.horizontalLayout_108)

        self.horizontalLayout_109 = QHBoxLayout()
        self.horizontalLayout_109.setObjectName(u"horizontalLayout_109")
        self.label_111 = QLabel(self.tab_13)
        self.label_111.setObjectName(u"label_111")
        sizePolicy2.setHeightForWidth(self.label_111.sizePolicy().hasHeightForWidth())
        self.label_111.setSizePolicy(sizePolicy2)
        self.label_111.setMinimumSize(QSize(75, 25))

        self.horizontalLayout_109.addWidget(self.label_111)

        self.side_match_4 = QLineEdit(self.tab_13)
        self.side_match_4.setObjectName(u"side_match_4")
        sizePolicy1.setHeightForWidth(self.side_match_4.sizePolicy().hasHeightForWidth())
        self.side_match_4.setSizePolicy(sizePolicy1)
        self.side_match_4.setMinimumSize(QSize(50, 25))
        self.side_match_4.setMaximumSize(QSize(1600, 16777215))

        self.horizontalLayout_109.addWidget(self.side_match_4)


        self.horizontalLayout_106.addLayout(self.horizontalLayout_109)

        self.horizontalLayout_110 = QHBoxLayout()
        self.horizontalLayout_110.setObjectName(u"horizontalLayout_110")
        self.label_112 = QLabel(self.tab_13)
        self.label_112.setObjectName(u"label_112")
        sizePolicy2.setHeightForWidth(self.label_112.sizePolicy().hasHeightForWidth())
        self.label_112.setSizePolicy(sizePolicy2)
        self.label_112.setMinimumSize(QSize(30, 25))

        self.horizontalLayout_110.addWidget(self.label_112)

        self.side_dest_4 = QLineEdit(self.tab_13)
        self.side_dest_4.setObjectName(u"side_dest_4")
        sizePolicy1.setHeightForWidth(self.side_dest_4.sizePolicy().hasHeightForWidth())
        self.side_dest_4.setSizePolicy(sizePolicy1)
        self.side_dest_4.setMinimumSize(QSize(50, 25))
        self.side_dest_4.setMaximumSize(QSize(1600, 16777215))

        self.horizontalLayout_110.addWidget(self.side_dest_4)


        self.horizontalLayout_106.addLayout(self.horizontalLayout_110)

        self.horizontalLayout_111 = QHBoxLayout()
        self.horizontalLayout_111.setObjectName(u"horizontalLayout_111")
        self.label_113 = QLabel(self.tab_13)
        self.label_113.setObjectName(u"label_113")
        sizePolicy2.setHeightForWidth(self.label_113.sizePolicy().hasHeightForWidth())
        self.label_113.setSizePolicy(sizePolicy2)
        self.label_113.setMinimumSize(QSize(35, 25))

        self.horizontalLayout_111.addWidget(self.label_113)

        self.side_filter_4 = QLineEdit(self.tab_13)
        self.side_filter_4.setObjectName(u"side_filter_4")
        sizePolicy1.setHeightForWidth(self.side_filter_4.sizePolicy().hasHeightForWidth())
        self.side_filter_4.setSizePolicy(sizePolicy1)
        self.side_filter_4.setMinimumSize(QSize(50, 25))
        self.side_filter_4.setMaximumSize(QSize(1600, 16777215))

        self.horizontalLayout_111.addWidget(self.side_filter_4)


        self.horizontalLayout_106.addLayout(self.horizontalLayout_111)


        self.verticalLayout_46.addLayout(self.horizontalLayout_106)

        self.horizontalLayout_138 = QHBoxLayout()
        self.horizontalLayout_138.setObjectName(u"horizontalLayout_138")
        self.horizontalLayout_140 = QHBoxLayout()
        self.horizontalLayout_140.setObjectName(u"horizontalLayout_140")
        self.label_134 = QLabel(self.tab_13)
        self.label_134.setObjectName(u"label_134")
        sizePolicy2.setHeightForWidth(self.label_134.sizePolicy().hasHeightForWidth())
        self.label_134.setSizePolicy(sizePolicy2)
        self.label_134.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_140.addWidget(self.label_134)

        self.side_pattern_5 = QLineEdit(self.tab_13)
        self.side_pattern_5.setObjectName(u"side_pattern_5")
        sizePolicy1.setHeightForWidth(self.side_pattern_5.sizePolicy().hasHeightForWidth())
        self.side_pattern_5.setSizePolicy(sizePolicy1)
        self.side_pattern_5.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_140.addWidget(self.side_pattern_5)


        self.horizontalLayout_138.addLayout(self.horizontalLayout_140)

        self.horizontalLayout_141 = QHBoxLayout()
        self.horizontalLayout_141.setObjectName(u"horizontalLayout_141")
        self.label_135 = QLabel(self.tab_13)
        self.label_135.setObjectName(u"label_135")
        sizePolicy2.setHeightForWidth(self.label_135.sizePolicy().hasHeightForWidth())
        self.label_135.setSizePolicy(sizePolicy2)
        self.label_135.setMinimumSize(QSize(30, 25))

        self.horizontalLayout_141.addWidget(self.label_135)

        self.side_repl_5 = QLineEdit(self.tab_13)
        self.side_repl_5.setObjectName(u"side_repl_5")
        sizePolicy1.setHeightForWidth(self.side_repl_5.sizePolicy().hasHeightForWidth())
        self.side_repl_5.setSizePolicy(sizePolicy1)
        self.side_repl_5.setMinimumSize(QSize(50, 25))
        self.side_repl_5.setMaximumSize(QSize(1600, 16777215))

        self.horizontalLayout_141.addWidget(self.side_repl_5)


        self.horizontalLayout_138.addLayout(self.horizontalLayout_141)

        self.horizontalLayout_142 = QHBoxLayout()
        self.horizontalLayout_142.setObjectName(u"horizontalLayout_142")
        self.label_136 = QLabel(self.tab_13)
        self.label_136.setObjectName(u"label_136")
        sizePolicy2.setHeightForWidth(self.label_136.sizePolicy().hasHeightForWidth())
        self.label_136.setSizePolicy(sizePolicy2)
        self.label_136.setMinimumSize(QSize(75, 25))

        self.horizontalLayout_142.addWidget(self.label_136)

        self.side_match_5 = QLineEdit(self.tab_13)
        self.side_match_5.setObjectName(u"side_match_5")
        sizePolicy1.setHeightForWidth(self.side_match_5.sizePolicy().hasHeightForWidth())
        self.side_match_5.setSizePolicy(sizePolicy1)
        self.side_match_5.setMinimumSize(QSize(50, 25))
        self.side_match_5.setMaximumSize(QSize(1600, 16777215))

        self.horizontalLayout_142.addWidget(self.side_match_5)


        self.horizontalLayout_138.addLayout(self.horizontalLayout_142)

        self.horizontalLayout_143 = QHBoxLayout()
        self.horizontalLayout_143.setObjectName(u"horizontalLayout_143")
        self.label_137 = QLabel(self.tab_13)
        self.label_137.setObjectName(u"label_137")
        sizePolicy2.setHeightForWidth(self.label_137.sizePolicy().hasHeightForWidth())
        self.label_137.setSizePolicy(sizePolicy2)
        self.label_137.setMinimumSize(QSize(30, 25))

        self.horizontalLayout_143.addWidget(self.label_137)

        self.side_dest_5 = QLineEdit(self.tab_13)
        self.side_dest_5.setObjectName(u"side_dest_5")
        sizePolicy1.setHeightForWidth(self.side_dest_5.sizePolicy().hasHeightForWidth())
        self.side_dest_5.setSizePolicy(sizePolicy1)
        self.side_dest_5.setMinimumSize(QSize(50, 25))
        self.side_dest_5.setMaximumSize(QSize(1600, 16777215))

        self.horizontalLayout_143.addWidget(self.side_dest_5)


        self.horizontalLayout_138.addLayout(self.horizontalLayout_143)

        self.horizontalLayout_144 = QHBoxLayout()
        self.horizontalLayout_144.setObjectName(u"horizontalLayout_144")
        self.label_138 = QLabel(self.tab_13)
        self.label_138.setObjectName(u"label_138")
        sizePolicy2.setHeightForWidth(self.label_138.sizePolicy().hasHeightForWidth())
        self.label_138.setSizePolicy(sizePolicy2)
        self.label_138.setMinimumSize(QSize(35, 25))

        self.horizontalLayout_144.addWidget(self.label_138)

        self.side_filter_5 = QLineEdit(self.tab_13)
        self.side_filter_5.setObjectName(u"side_filter_5")
        sizePolicy1.setHeightForWidth(self.side_filter_5.sizePolicy().hasHeightForWidth())
        self.side_filter_5.setSizePolicy(sizePolicy1)
        self.side_filter_5.setMinimumSize(QSize(50, 25))
        self.side_filter_5.setMaximumSize(QSize(1600, 16777215))

        self.horizontalLayout_144.addWidget(self.side_filter_5)


        self.horizontalLayout_138.addLayout(self.horizontalLayout_144)


        self.verticalLayout_46.addLayout(self.horizontalLayout_138)

        self.horizontalLayout_145 = QHBoxLayout()
        self.horizontalLayout_145.setObjectName(u"horizontalLayout_145")
        self.horizontalLayout_146 = QHBoxLayout()
        self.horizontalLayout_146.setObjectName(u"horizontalLayout_146")
        self.label_139 = QLabel(self.tab_13)
        self.label_139.setObjectName(u"label_139")
        sizePolicy2.setHeightForWidth(self.label_139.sizePolicy().hasHeightForWidth())
        self.label_139.setSizePolicy(sizePolicy2)
        self.label_139.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_146.addWidget(self.label_139)

        self.side_pattern_6 = QLineEdit(self.tab_13)
        self.side_pattern_6.setObjectName(u"side_pattern_6")
        sizePolicy1.setHeightForWidth(self.side_pattern_6.sizePolicy().hasHeightForWidth())
        self.side_pattern_6.setSizePolicy(sizePolicy1)
        self.side_pattern_6.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_146.addWidget(self.side_pattern_6)


        self.horizontalLayout_145.addLayout(self.horizontalLayout_146)

        self.horizontalLayout_147 = QHBoxLayout()
        self.horizontalLayout_147.setObjectName(u"horizontalLayout_147")
        self.label_140 = QLabel(self.tab_13)
        self.label_140.setObjectName(u"label_140")
        sizePolicy2.setHeightForWidth(self.label_140.sizePolicy().hasHeightForWidth())
        self.label_140.setSizePolicy(sizePolicy2)
        self.label_140.setMinimumSize(QSize(30, 25))

        self.horizontalLayout_147.addWidget(self.label_140)

        self.side_repl_6 = QLineEdit(self.tab_13)
        self.side_repl_6.setObjectName(u"side_repl_6")
        sizePolicy1.setHeightForWidth(self.side_repl_6.sizePolicy().hasHeightForWidth())
        self.side_repl_6.setSizePolicy(sizePolicy1)
        self.side_repl_6.setMinimumSize(QSize(50, 25))
        self.side_repl_6.setMaximumSize(QSize(1600, 16777215))

        self.horizontalLayout_147.addWidget(self.side_repl_6)


        self.horizontalLayout_145.addLayout(self.horizontalLayout_147)

        self.horizontalLayout_148 = QHBoxLayout()
        self.horizontalLayout_148.setObjectName(u"horizontalLayout_148")
        self.label_141 = QLabel(self.tab_13)
        self.label_141.setObjectName(u"label_141")
        sizePolicy2.setHeightForWidth(self.label_141.sizePolicy().hasHeightForWidth())
        self.label_141.setSizePolicy(sizePolicy2)
        self.label_141.setMinimumSize(QSize(75, 25))

        self.horizontalLayout_148.addWidget(self.label_141)

        self.side_match_6 = QLineEdit(self.tab_13)
        self.side_match_6.setObjectName(u"side_match_6")
        sizePolicy1.setHeightForWidth(self.side_match_6.sizePolicy().hasHeightForWidth())
        self.side_match_6.setSizePolicy(sizePolicy1)
        self.side_match_6.setMinimumSize(QSize(50, 25))
        self.side_match_6.setMaximumSize(QSize(1600, 16777215))

        self.horizontalLayout_148.addWidget(self.side_match_6)


        self.horizontalLayout_145.addLayout(self.horizontalLayout_148)

        self.horizontalLayout_149 = QHBoxLayout()
        self.horizontalLayout_149.setObjectName(u"horizontalLayout_149")
        self.label_142 = QLabel(self.tab_13)
        self.label_142.setObjectName(u"label_142")
        sizePolicy2.setHeightForWidth(self.label_142.sizePolicy().hasHeightForWidth())
        self.label_142.setSizePolicy(sizePolicy2)
        self.label_142.setMinimumSize(QSize(30, 25))

        self.horizontalLayout_149.addWidget(self.label_142)

        self.side_dest_6 = QLineEdit(self.tab_13)
        self.side_dest_6.setObjectName(u"side_dest_6")
        sizePolicy1.setHeightForWidth(self.side_dest_6.sizePolicy().hasHeightForWidth())
        self.side_dest_6.setSizePolicy(sizePolicy1)
        self.side_dest_6.setMinimumSize(QSize(50, 25))
        self.side_dest_6.setMaximumSize(QSize(1600, 16777215))

        self.horizontalLayout_149.addWidget(self.side_dest_6)


        self.horizontalLayout_145.addLayout(self.horizontalLayout_149)

        self.horizontalLayout_150 = QHBoxLayout()
        self.horizontalLayout_150.setObjectName(u"horizontalLayout_150")
        self.label_143 = QLabel(self.tab_13)
        self.label_143.setObjectName(u"label_143")
        sizePolicy2.setHeightForWidth(self.label_143.sizePolicy().hasHeightForWidth())
        self.label_143.setSizePolicy(sizePolicy2)
        self.label_143.setMinimumSize(QSize(35, 25))

        self.horizontalLayout_150.addWidget(self.label_143)

        self.side_filter_6 = QLineEdit(self.tab_13)
        self.side_filter_6.setObjectName(u"side_filter_6")
        sizePolicy1.setHeightForWidth(self.side_filter_6.sizePolicy().hasHeightForWidth())
        self.side_filter_6.setSizePolicy(sizePolicy1)
        self.side_filter_6.setMinimumSize(QSize(50, 25))
        self.side_filter_6.setMaximumSize(QSize(1600, 16777215))

        self.horizontalLayout_150.addWidget(self.side_filter_6)


        self.horizontalLayout_145.addLayout(self.horizontalLayout_150)


        self.verticalLayout_46.addLayout(self.horizontalLayout_145)

        self.verticalSpacer_4 = QSpacerItem(20, 18, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_46.addItem(self.verticalSpacer_4)


        self.verticalLayout_52.addLayout(self.verticalLayout_46)

        self.TopTab.addTab(self.tab_13, "")
        self.tab_17 = QWidget()
        self.tab_17.setObjectName(u"tab_17")
        self.verticalLayout_66 = QVBoxLayout(self.tab_17)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.verticalLayout_65 = QVBoxLayout()
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.horizontalLayout_135 = QHBoxLayout()
        self.horizontalLayout_135.setObjectName(u"horizontalLayout_135")
        self.label_246 = QLabel(self.tab_17)
        self.label_246.setObjectName(u"label_246")
        sizePolicy2.setHeightForWidth(self.label_246.sizePolicy().hasHeightForWidth())
        self.label_246.setSizePolicy(sizePolicy2)
        self.label_246.setMinimumSize(QSize(40, 25))

        self.horizontalLayout_135.addWidget(self.label_246)

        self.rename_filter_01 = QLineEdit(self.tab_17)
        self.rename_filter_01.setObjectName(u"rename_filter_01")
        sizePolicy1.setHeightForWidth(self.rename_filter_01.sizePolicy().hasHeightForWidth())
        self.rename_filter_01.setSizePolicy(sizePolicy1)
        self.rename_filter_01.setMinimumSize(QSize(30, 25))
        self.rename_filter_01.setMaximumSize(QSize(16000, 16777215))

        self.horizontalLayout_135.addWidget(self.rename_filter_01)

        self.label_35 = QLabel(self.tab_17)
        self.label_35.setObjectName(u"label_35")
        sizePolicy2.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy2)
        self.label_35.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_135.addWidget(self.label_35)

        self.rename_source_01 = QSpinBox(self.tab_17)
        self.rename_source_01.setObjectName(u"rename_source_01")
        sizePolicy2.setHeightForWidth(self.rename_source_01.sizePolicy().hasHeightForWidth())
        self.rename_source_01.setSizePolicy(sizePolicy2)
        self.rename_source_01.setMinimumSize(QSize(30, 25))
        self.rename_source_01.setMaximum(9)
        self.rename_source_01.setValue(0)

        self.horizontalLayout_135.addWidget(self.rename_source_01)

        self.label_245 = QLabel(self.tab_17)
        self.label_245.setObjectName(u"label_245")
        sizePolicy2.setHeightForWidth(self.label_245.sizePolicy().hasHeightForWidth())
        self.label_245.setSizePolicy(sizePolicy2)
        self.label_245.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_135.addWidget(self.label_245)

        self.rename_pattern_01 = QLineEdit(self.tab_17)
        self.rename_pattern_01.setObjectName(u"rename_pattern_01")
        sizePolicy1.setHeightForWidth(self.rename_pattern_01.sizePolicy().hasHeightForWidth())
        self.rename_pattern_01.setSizePolicy(sizePolicy1)
        self.rename_pattern_01.setMinimumSize(QSize(100, 25))

        self.horizontalLayout_135.addWidget(self.rename_pattern_01)

        self.label_247 = QLabel(self.tab_17)
        self.label_247.setObjectName(u"label_247")
        sizePolicy2.setHeightForWidth(self.label_247.sizePolicy().hasHeightForWidth())
        self.label_247.setSizePolicy(sizePolicy2)
        self.label_247.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_135.addWidget(self.label_247)

        self.rename_repl_01 = QLineEdit(self.tab_17)
        self.rename_repl_01.setObjectName(u"rename_repl_01")
        sizePolicy1.setHeightForWidth(self.rename_repl_01.sizePolicy().hasHeightForWidth())
        self.rename_repl_01.setSizePolicy(sizePolicy1)
        self.rename_repl_01.setMinimumSize(QSize(80, 25))
        self.rename_repl_01.setMaximumSize(QSize(1600, 16777215))

        self.horizontalLayout_135.addWidget(self.rename_repl_01)


        self.verticalLayout_65.addLayout(self.horizontalLayout_135)

        self.horizontalLayout_153 = QHBoxLayout()
        self.horizontalLayout_153.setObjectName(u"horizontalLayout_153")
        self.label_248 = QLabel(self.tab_17)
        self.label_248.setObjectName(u"label_248")
        sizePolicy2.setHeightForWidth(self.label_248.sizePolicy().hasHeightForWidth())
        self.label_248.setSizePolicy(sizePolicy2)
        self.label_248.setMinimumSize(QSize(40, 25))

        self.horizontalLayout_153.addWidget(self.label_248)

        self.rename_filter_02 = QLineEdit(self.tab_17)
        self.rename_filter_02.setObjectName(u"rename_filter_02")
        sizePolicy1.setHeightForWidth(self.rename_filter_02.sizePolicy().hasHeightForWidth())
        self.rename_filter_02.setSizePolicy(sizePolicy1)
        self.rename_filter_02.setMinimumSize(QSize(30, 25))
        self.rename_filter_02.setMaximumSize(QSize(16000, 16777215))

        self.horizontalLayout_153.addWidget(self.rename_filter_02)

        self.label_249 = QLabel(self.tab_17)
        self.label_249.setObjectName(u"label_249")
        sizePolicy2.setHeightForWidth(self.label_249.sizePolicy().hasHeightForWidth())
        self.label_249.setSizePolicy(sizePolicy2)
        self.label_249.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_153.addWidget(self.label_249)

        self.rename_source_02 = QSpinBox(self.tab_17)
        self.rename_source_02.setObjectName(u"rename_source_02")
        sizePolicy2.setHeightForWidth(self.rename_source_02.sizePolicy().hasHeightForWidth())
        self.rename_source_02.setSizePolicy(sizePolicy2)
        self.rename_source_02.setMinimumSize(QSize(30, 25))
        self.rename_source_02.setMaximum(9)
        self.rename_source_02.setValue(0)

        self.horizontalLayout_153.addWidget(self.rename_source_02)

        self.label_250 = QLabel(self.tab_17)
        self.label_250.setObjectName(u"label_250")
        sizePolicy2.setHeightForWidth(self.label_250.sizePolicy().hasHeightForWidth())
        self.label_250.setSizePolicy(sizePolicy2)
        self.label_250.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_153.addWidget(self.label_250)

        self.rename_pattern_02 = QLineEdit(self.tab_17)
        self.rename_pattern_02.setObjectName(u"rename_pattern_02")
        sizePolicy1.setHeightForWidth(self.rename_pattern_02.sizePolicy().hasHeightForWidth())
        self.rename_pattern_02.setSizePolicy(sizePolicy1)
        self.rename_pattern_02.setMinimumSize(QSize(100, 25))

        self.horizontalLayout_153.addWidget(self.rename_pattern_02)

        self.label_251 = QLabel(self.tab_17)
        self.label_251.setObjectName(u"label_251")
        sizePolicy2.setHeightForWidth(self.label_251.sizePolicy().hasHeightForWidth())
        self.label_251.setSizePolicy(sizePolicy2)
        self.label_251.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_153.addWidget(self.label_251)

        self.rename_repl_02 = QLineEdit(self.tab_17)
        self.rename_repl_02.setObjectName(u"rename_repl_02")
        sizePolicy1.setHeightForWidth(self.rename_repl_02.sizePolicy().hasHeightForWidth())
        self.rename_repl_02.setSizePolicy(sizePolicy1)
        self.rename_repl_02.setMinimumSize(QSize(80, 25))
        self.rename_repl_02.setMaximumSize(QSize(1600, 16777215))

        self.horizontalLayout_153.addWidget(self.rename_repl_02)


        self.verticalLayout_65.addLayout(self.horizontalLayout_153)

        self.horizontalLayout_154 = QHBoxLayout()
        self.horizontalLayout_154.setObjectName(u"horizontalLayout_154")
        self.label_252 = QLabel(self.tab_17)
        self.label_252.setObjectName(u"label_252")
        sizePolicy2.setHeightForWidth(self.label_252.sizePolicy().hasHeightForWidth())
        self.label_252.setSizePolicy(sizePolicy2)
        self.label_252.setMinimumSize(QSize(40, 25))

        self.horizontalLayout_154.addWidget(self.label_252)

        self.rename_filter_03 = QLineEdit(self.tab_17)
        self.rename_filter_03.setObjectName(u"rename_filter_03")
        sizePolicy1.setHeightForWidth(self.rename_filter_03.sizePolicy().hasHeightForWidth())
        self.rename_filter_03.setSizePolicy(sizePolicy1)
        self.rename_filter_03.setMinimumSize(QSize(30, 25))
        self.rename_filter_03.setMaximumSize(QSize(16000, 16777215))

        self.horizontalLayout_154.addWidget(self.rename_filter_03)

        self.label_253 = QLabel(self.tab_17)
        self.label_253.setObjectName(u"label_253")
        sizePolicy2.setHeightForWidth(self.label_253.sizePolicy().hasHeightForWidth())
        self.label_253.setSizePolicy(sizePolicy2)
        self.label_253.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_154.addWidget(self.label_253)

        self.rename_source_03 = QSpinBox(self.tab_17)
        self.rename_source_03.setObjectName(u"rename_source_03")
        sizePolicy2.setHeightForWidth(self.rename_source_03.sizePolicy().hasHeightForWidth())
        self.rename_source_03.setSizePolicy(sizePolicy2)
        self.rename_source_03.setMinimumSize(QSize(30, 25))
        self.rename_source_03.setMaximum(9)
        self.rename_source_03.setValue(0)

        self.horizontalLayout_154.addWidget(self.rename_source_03)

        self.label_254 = QLabel(self.tab_17)
        self.label_254.setObjectName(u"label_254")
        sizePolicy2.setHeightForWidth(self.label_254.sizePolicy().hasHeightForWidth())
        self.label_254.setSizePolicy(sizePolicy2)
        self.label_254.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_154.addWidget(self.label_254)

        self.rename_pattern_03 = QLineEdit(self.tab_17)
        self.rename_pattern_03.setObjectName(u"rename_pattern_03")
        sizePolicy1.setHeightForWidth(self.rename_pattern_03.sizePolicy().hasHeightForWidth())
        self.rename_pattern_03.setSizePolicy(sizePolicy1)
        self.rename_pattern_03.setMinimumSize(QSize(100, 25))

        self.horizontalLayout_154.addWidget(self.rename_pattern_03)

        self.label_255 = QLabel(self.tab_17)
        self.label_255.setObjectName(u"label_255")
        sizePolicy2.setHeightForWidth(self.label_255.sizePolicy().hasHeightForWidth())
        self.label_255.setSizePolicy(sizePolicy2)
        self.label_255.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_154.addWidget(self.label_255)

        self.rename_repl_03 = QLineEdit(self.tab_17)
        self.rename_repl_03.setObjectName(u"rename_repl_03")
        sizePolicy1.setHeightForWidth(self.rename_repl_03.sizePolicy().hasHeightForWidth())
        self.rename_repl_03.setSizePolicy(sizePolicy1)
        self.rename_repl_03.setMinimumSize(QSize(80, 25))
        self.rename_repl_03.setMaximumSize(QSize(1600, 16777215))

        self.horizontalLayout_154.addWidget(self.rename_repl_03)


        self.verticalLayout_65.addLayout(self.horizontalLayout_154)

        self.horizontalLayout_155 = QHBoxLayout()
        self.horizontalLayout_155.setObjectName(u"horizontalLayout_155")
        self.label_256 = QLabel(self.tab_17)
        self.label_256.setObjectName(u"label_256")
        sizePolicy2.setHeightForWidth(self.label_256.sizePolicy().hasHeightForWidth())
        self.label_256.setSizePolicy(sizePolicy2)
        self.label_256.setMinimumSize(QSize(40, 25))

        self.horizontalLayout_155.addWidget(self.label_256)

        self.rename_filter_04 = QLineEdit(self.tab_17)
        self.rename_filter_04.setObjectName(u"rename_filter_04")
        sizePolicy1.setHeightForWidth(self.rename_filter_04.sizePolicy().hasHeightForWidth())
        self.rename_filter_04.setSizePolicy(sizePolicy1)
        self.rename_filter_04.setMinimumSize(QSize(30, 25))
        self.rename_filter_04.setMaximumSize(QSize(16000, 16777215))

        self.horizontalLayout_155.addWidget(self.rename_filter_04)

        self.label_257 = QLabel(self.tab_17)
        self.label_257.setObjectName(u"label_257")
        sizePolicy2.setHeightForWidth(self.label_257.sizePolicy().hasHeightForWidth())
        self.label_257.setSizePolicy(sizePolicy2)
        self.label_257.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_155.addWidget(self.label_257)

        self.rename_source_04 = QSpinBox(self.tab_17)
        self.rename_source_04.setObjectName(u"rename_source_04")
        sizePolicy2.setHeightForWidth(self.rename_source_04.sizePolicy().hasHeightForWidth())
        self.rename_source_04.setSizePolicy(sizePolicy2)
        self.rename_source_04.setMinimumSize(QSize(30, 25))
        self.rename_source_04.setMaximum(9)
        self.rename_source_04.setValue(0)

        self.horizontalLayout_155.addWidget(self.rename_source_04)

        self.label_258 = QLabel(self.tab_17)
        self.label_258.setObjectName(u"label_258")
        sizePolicy2.setHeightForWidth(self.label_258.sizePolicy().hasHeightForWidth())
        self.label_258.setSizePolicy(sizePolicy2)
        self.label_258.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_155.addWidget(self.label_258)

        self.rename_pattern_04 = QLineEdit(self.tab_17)
        self.rename_pattern_04.setObjectName(u"rename_pattern_04")
        sizePolicy1.setHeightForWidth(self.rename_pattern_04.sizePolicy().hasHeightForWidth())
        self.rename_pattern_04.setSizePolicy(sizePolicy1)
        self.rename_pattern_04.setMinimumSize(QSize(100, 25))

        self.horizontalLayout_155.addWidget(self.rename_pattern_04)

        self.label_259 = QLabel(self.tab_17)
        self.label_259.setObjectName(u"label_259")
        sizePolicy2.setHeightForWidth(self.label_259.sizePolicy().hasHeightForWidth())
        self.label_259.setSizePolicy(sizePolicy2)
        self.label_259.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_155.addWidget(self.label_259)

        self.rename_repl_04 = QLineEdit(self.tab_17)
        self.rename_repl_04.setObjectName(u"rename_repl_04")
        sizePolicy1.setHeightForWidth(self.rename_repl_04.sizePolicy().hasHeightForWidth())
        self.rename_repl_04.setSizePolicy(sizePolicy1)
        self.rename_repl_04.setMinimumSize(QSize(80, 25))
        self.rename_repl_04.setMaximumSize(QSize(1600, 16777215))

        self.horizontalLayout_155.addWidget(self.rename_repl_04)


        self.verticalLayout_65.addLayout(self.horizontalLayout_155)

        self.horizontalLayout_156 = QHBoxLayout()
        self.horizontalLayout_156.setObjectName(u"horizontalLayout_156")
        self.label_260 = QLabel(self.tab_17)
        self.label_260.setObjectName(u"label_260")
        sizePolicy2.setHeightForWidth(self.label_260.sizePolicy().hasHeightForWidth())
        self.label_260.setSizePolicy(sizePolicy2)
        self.label_260.setMinimumSize(QSize(40, 25))

        self.horizontalLayout_156.addWidget(self.label_260)

        self.rename_filter_05 = QLineEdit(self.tab_17)
        self.rename_filter_05.setObjectName(u"rename_filter_05")
        sizePolicy1.setHeightForWidth(self.rename_filter_05.sizePolicy().hasHeightForWidth())
        self.rename_filter_05.setSizePolicy(sizePolicy1)
        self.rename_filter_05.setMinimumSize(QSize(30, 25))
        self.rename_filter_05.setMaximumSize(QSize(16000, 16777215))

        self.horizontalLayout_156.addWidget(self.rename_filter_05)

        self.label_261 = QLabel(self.tab_17)
        self.label_261.setObjectName(u"label_261")
        sizePolicy2.setHeightForWidth(self.label_261.sizePolicy().hasHeightForWidth())
        self.label_261.setSizePolicy(sizePolicy2)
        self.label_261.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_156.addWidget(self.label_261)

        self.rename_source_05 = QSpinBox(self.tab_17)
        self.rename_source_05.setObjectName(u"rename_source_05")
        sizePolicy2.setHeightForWidth(self.rename_source_05.sizePolicy().hasHeightForWidth())
        self.rename_source_05.setSizePolicy(sizePolicy2)
        self.rename_source_05.setMinimumSize(QSize(30, 25))
        self.rename_source_05.setMaximum(9)
        self.rename_source_05.setValue(0)

        self.horizontalLayout_156.addWidget(self.rename_source_05)

        self.label_262 = QLabel(self.tab_17)
        self.label_262.setObjectName(u"label_262")
        sizePolicy2.setHeightForWidth(self.label_262.sizePolicy().hasHeightForWidth())
        self.label_262.setSizePolicy(sizePolicy2)
        self.label_262.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_156.addWidget(self.label_262)

        self.rename_pattern_05 = QLineEdit(self.tab_17)
        self.rename_pattern_05.setObjectName(u"rename_pattern_05")
        sizePolicy1.setHeightForWidth(self.rename_pattern_05.sizePolicy().hasHeightForWidth())
        self.rename_pattern_05.setSizePolicy(sizePolicy1)
        self.rename_pattern_05.setMinimumSize(QSize(100, 25))

        self.horizontalLayout_156.addWidget(self.rename_pattern_05)

        self.label_263 = QLabel(self.tab_17)
        self.label_263.setObjectName(u"label_263")
        sizePolicy2.setHeightForWidth(self.label_263.sizePolicy().hasHeightForWidth())
        self.label_263.setSizePolicy(sizePolicy2)
        self.label_263.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_156.addWidget(self.label_263)

        self.rename_repl_05 = QLineEdit(self.tab_17)
        self.rename_repl_05.setObjectName(u"rename_repl_05")
        sizePolicy1.setHeightForWidth(self.rename_repl_05.sizePolicy().hasHeightForWidth())
        self.rename_repl_05.setSizePolicy(sizePolicy1)
        self.rename_repl_05.setMinimumSize(QSize(80, 25))
        self.rename_repl_05.setMaximumSize(QSize(1600, 16777215))

        self.horizontalLayout_156.addWidget(self.rename_repl_05)


        self.verticalLayout_65.addLayout(self.horizontalLayout_156)

        self.horizontalLayout_157 = QHBoxLayout()
        self.horizontalLayout_157.setObjectName(u"horizontalLayout_157")
        self.label_264 = QLabel(self.tab_17)
        self.label_264.setObjectName(u"label_264")
        sizePolicy2.setHeightForWidth(self.label_264.sizePolicy().hasHeightForWidth())
        self.label_264.setSizePolicy(sizePolicy2)
        self.label_264.setMinimumSize(QSize(40, 25))

        self.horizontalLayout_157.addWidget(self.label_264)

        self.rename_filter_06 = QLineEdit(self.tab_17)
        self.rename_filter_06.setObjectName(u"rename_filter_06")
        sizePolicy1.setHeightForWidth(self.rename_filter_06.sizePolicy().hasHeightForWidth())
        self.rename_filter_06.setSizePolicy(sizePolicy1)
        self.rename_filter_06.setMinimumSize(QSize(30, 25))
        self.rename_filter_06.setMaximumSize(QSize(16000, 16777215))

        self.horizontalLayout_157.addWidget(self.rename_filter_06)

        self.label_265 = QLabel(self.tab_17)
        self.label_265.setObjectName(u"label_265")
        sizePolicy2.setHeightForWidth(self.label_265.sizePolicy().hasHeightForWidth())
        self.label_265.setSizePolicy(sizePolicy2)
        self.label_265.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_157.addWidget(self.label_265)

        self.rename_source_06 = QSpinBox(self.tab_17)
        self.rename_source_06.setObjectName(u"rename_source_06")
        sizePolicy2.setHeightForWidth(self.rename_source_06.sizePolicy().hasHeightForWidth())
        self.rename_source_06.setSizePolicy(sizePolicy2)
        self.rename_source_06.setMinimumSize(QSize(30, 25))
        self.rename_source_06.setMaximum(9)
        self.rename_source_06.setValue(0)

        self.horizontalLayout_157.addWidget(self.rename_source_06)

        self.label_266 = QLabel(self.tab_17)
        self.label_266.setObjectName(u"label_266")
        sizePolicy2.setHeightForWidth(self.label_266.sizePolicy().hasHeightForWidth())
        self.label_266.setSizePolicy(sizePolicy2)
        self.label_266.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_157.addWidget(self.label_266)

        self.rename_pattern_06 = QLineEdit(self.tab_17)
        self.rename_pattern_06.setObjectName(u"rename_pattern_06")
        sizePolicy1.setHeightForWidth(self.rename_pattern_06.sizePolicy().hasHeightForWidth())
        self.rename_pattern_06.setSizePolicy(sizePolicy1)
        self.rename_pattern_06.setMinimumSize(QSize(100, 25))

        self.horizontalLayout_157.addWidget(self.rename_pattern_06)

        self.label_267 = QLabel(self.tab_17)
        self.label_267.setObjectName(u"label_267")
        sizePolicy2.setHeightForWidth(self.label_267.sizePolicy().hasHeightForWidth())
        self.label_267.setSizePolicy(sizePolicy2)
        self.label_267.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_157.addWidget(self.label_267)

        self.rename_repl_06 = QLineEdit(self.tab_17)
        self.rename_repl_06.setObjectName(u"rename_repl_06")
        sizePolicy1.setHeightForWidth(self.rename_repl_06.sizePolicy().hasHeightForWidth())
        self.rename_repl_06.setSizePolicy(sizePolicy1)
        self.rename_repl_06.setMinimumSize(QSize(80, 25))
        self.rename_repl_06.setMaximumSize(QSize(1600, 16777215))

        self.horizontalLayout_157.addWidget(self.rename_repl_06)


        self.verticalLayout_65.addLayout(self.horizontalLayout_157)

        self.horizontalLayout_158 = QHBoxLayout()
        self.horizontalLayout_158.setObjectName(u"horizontalLayout_158")
        self.label_268 = QLabel(self.tab_17)
        self.label_268.setObjectName(u"label_268")
        sizePolicy2.setHeightForWidth(self.label_268.sizePolicy().hasHeightForWidth())
        self.label_268.setSizePolicy(sizePolicy2)
        self.label_268.setMinimumSize(QSize(40, 25))

        self.horizontalLayout_158.addWidget(self.label_268)

        self.rename_filter_07 = QLineEdit(self.tab_17)
        self.rename_filter_07.setObjectName(u"rename_filter_07")
        sizePolicy1.setHeightForWidth(self.rename_filter_07.sizePolicy().hasHeightForWidth())
        self.rename_filter_07.setSizePolicy(sizePolicy1)
        self.rename_filter_07.setMinimumSize(QSize(30, 25))
        self.rename_filter_07.setMaximumSize(QSize(16000, 16777215))

        self.horizontalLayout_158.addWidget(self.rename_filter_07)

        self.label_269 = QLabel(self.tab_17)
        self.label_269.setObjectName(u"label_269")
        sizePolicy2.setHeightForWidth(self.label_269.sizePolicy().hasHeightForWidth())
        self.label_269.setSizePolicy(sizePolicy2)
        self.label_269.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_158.addWidget(self.label_269)

        self.rename_source_07 = QSpinBox(self.tab_17)
        self.rename_source_07.setObjectName(u"rename_source_07")
        sizePolicy2.setHeightForWidth(self.rename_source_07.sizePolicy().hasHeightForWidth())
        self.rename_source_07.setSizePolicy(sizePolicy2)
        self.rename_source_07.setMinimumSize(QSize(30, 25))
        self.rename_source_07.setMaximum(9)
        self.rename_source_07.setValue(0)

        self.horizontalLayout_158.addWidget(self.rename_source_07)

        self.label_270 = QLabel(self.tab_17)
        self.label_270.setObjectName(u"label_270")
        sizePolicy2.setHeightForWidth(self.label_270.sizePolicy().hasHeightForWidth())
        self.label_270.setSizePolicy(sizePolicy2)
        self.label_270.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_158.addWidget(self.label_270)

        self.rename_pattern_07 = QLineEdit(self.tab_17)
        self.rename_pattern_07.setObjectName(u"rename_pattern_07")
        sizePolicy1.setHeightForWidth(self.rename_pattern_07.sizePolicy().hasHeightForWidth())
        self.rename_pattern_07.setSizePolicy(sizePolicy1)
        self.rename_pattern_07.setMinimumSize(QSize(100, 25))

        self.horizontalLayout_158.addWidget(self.rename_pattern_07)

        self.label_271 = QLabel(self.tab_17)
        self.label_271.setObjectName(u"label_271")
        sizePolicy2.setHeightForWidth(self.label_271.sizePolicy().hasHeightForWidth())
        self.label_271.setSizePolicy(sizePolicy2)
        self.label_271.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_158.addWidget(self.label_271)

        self.rename_repl_07 = QLineEdit(self.tab_17)
        self.rename_repl_07.setObjectName(u"rename_repl_07")
        sizePolicy1.setHeightForWidth(self.rename_repl_07.sizePolicy().hasHeightForWidth())
        self.rename_repl_07.setSizePolicy(sizePolicy1)
        self.rename_repl_07.setMinimumSize(QSize(80, 25))
        self.rename_repl_07.setMaximumSize(QSize(1600, 16777215))

        self.horizontalLayout_158.addWidget(self.rename_repl_07)


        self.verticalLayout_65.addLayout(self.horizontalLayout_158)

        self.horizontalLayout_159 = QHBoxLayout()
        self.horizontalLayout_159.setObjectName(u"horizontalLayout_159")
        self.label_272 = QLabel(self.tab_17)
        self.label_272.setObjectName(u"label_272")
        sizePolicy2.setHeightForWidth(self.label_272.sizePolicy().hasHeightForWidth())
        self.label_272.setSizePolicy(sizePolicy2)
        self.label_272.setMinimumSize(QSize(40, 25))

        self.horizontalLayout_159.addWidget(self.label_272)

        self.rename_filter_08 = QLineEdit(self.tab_17)
        self.rename_filter_08.setObjectName(u"rename_filter_08")
        sizePolicy1.setHeightForWidth(self.rename_filter_08.sizePolicy().hasHeightForWidth())
        self.rename_filter_08.setSizePolicy(sizePolicy1)
        self.rename_filter_08.setMinimumSize(QSize(30, 25))
        self.rename_filter_08.setMaximumSize(QSize(16000, 16777215))

        self.horizontalLayout_159.addWidget(self.rename_filter_08)

        self.label_273 = QLabel(self.tab_17)
        self.label_273.setObjectName(u"label_273")
        sizePolicy2.setHeightForWidth(self.label_273.sizePolicy().hasHeightForWidth())
        self.label_273.setSizePolicy(sizePolicy2)
        self.label_273.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_159.addWidget(self.label_273)

        self.rename_source_08 = QSpinBox(self.tab_17)
        self.rename_source_08.setObjectName(u"rename_source_08")
        sizePolicy2.setHeightForWidth(self.rename_source_08.sizePolicy().hasHeightForWidth())
        self.rename_source_08.setSizePolicy(sizePolicy2)
        self.rename_source_08.setMinimumSize(QSize(30, 25))
        self.rename_source_08.setMaximum(9)
        self.rename_source_08.setValue(0)

        self.horizontalLayout_159.addWidget(self.rename_source_08)

        self.label_274 = QLabel(self.tab_17)
        self.label_274.setObjectName(u"label_274")
        sizePolicy2.setHeightForWidth(self.label_274.sizePolicy().hasHeightForWidth())
        self.label_274.setSizePolicy(sizePolicy2)
        self.label_274.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_159.addWidget(self.label_274)

        self.rename_pattern_08 = QLineEdit(self.tab_17)
        self.rename_pattern_08.setObjectName(u"rename_pattern_08")
        sizePolicy1.setHeightForWidth(self.rename_pattern_08.sizePolicy().hasHeightForWidth())
        self.rename_pattern_08.setSizePolicy(sizePolicy1)
        self.rename_pattern_08.setMinimumSize(QSize(100, 25))

        self.horizontalLayout_159.addWidget(self.rename_pattern_08)

        self.label_275 = QLabel(self.tab_17)
        self.label_275.setObjectName(u"label_275")
        sizePolicy2.setHeightForWidth(self.label_275.sizePolicy().hasHeightForWidth())
        self.label_275.setSizePolicy(sizePolicy2)
        self.label_275.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_159.addWidget(self.label_275)

        self.rename_repl_08 = QLineEdit(self.tab_17)
        self.rename_repl_08.setObjectName(u"rename_repl_08")
        sizePolicy1.setHeightForWidth(self.rename_repl_08.sizePolicy().hasHeightForWidth())
        self.rename_repl_08.setSizePolicy(sizePolicy1)
        self.rename_repl_08.setMinimumSize(QSize(80, 25))
        self.rename_repl_08.setMaximumSize(QSize(1600, 16777215))

        self.horizontalLayout_159.addWidget(self.rename_repl_08)


        self.verticalLayout_65.addLayout(self.horizontalLayout_159)

        self.horizontalLayout_160 = QHBoxLayout()
        self.horizontalLayout_160.setObjectName(u"horizontalLayout_160")
        self.Rename_go = QPushButton(self.tab_17)
        self.Rename_go.setObjectName(u"Rename_go")
        sizePolicy3.setHeightForWidth(self.Rename_go.sizePolicy().hasHeightForWidth())
        self.Rename_go.setSizePolicy(sizePolicy3)
        self.Rename_go.setMinimumSize(QSize(150, 25))
        self.Rename_go.setMaximumSize(QSize(16777215, 16000))

        self.horizontalLayout_160.addWidget(self.Rename_go)

        self.rename_reload_after = QCheckBox(self.tab_17)
        self.rename_reload_after.setObjectName(u"rename_reload_after")

        self.horizontalLayout_160.addWidget(self.rename_reload_after)


        self.verticalLayout_65.addLayout(self.horizontalLayout_160)


        self.verticalLayout_66.addLayout(self.verticalLayout_65)

        self.TopTab.addTab(self.tab_17, "")
        self.tab_23 = QWidget()
        self.tab_23.setObjectName(u"tab_23")
        self.verticalLayout_76 = QVBoxLayout(self.tab_23)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.verticalLayout_75 = QVBoxLayout()
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.horizontalLayout_192 = QHBoxLayout()
        self.horizontalLayout_192.setObjectName(u"horizontalLayout_192")
        self.groupBox_29 = QGroupBox(self.tab_23)
        self.groupBox_29.setObjectName(u"groupBox_29")
        sizePolicy2.setHeightForWidth(self.groupBox_29.sizePolicy().hasHeightForWidth())
        self.groupBox_29.setSizePolicy(sizePolicy2)
        self.groupBox_29.setMinimumSize(QSize(320, 55))
        self.groupBox_29.setMaximumSize(QSize(320, 55))
        self.groupBox_29.setBaseSize(QSize(350, 70))
        self.groupBox_29.setFlat(False)
        self.horizontalLayout_174 = QHBoxLayout(self.groupBox_29)
        self.horizontalLayout_174.setObjectName(u"horizontalLayout_174")
        self.horizontalLayout_163 = QHBoxLayout()
        self.horizontalLayout_163.setObjectName(u"horizontalLayout_163")
        self.data_enable = QCheckBox(self.groupBox_29)
        self.data_enable.setObjectName(u"data_enable")
        sizePolicy2.setHeightForWidth(self.data_enable.sizePolicy().hasHeightForWidth())
        self.data_enable.setSizePolicy(sizePolicy2)
        self.data_enable.setMinimumSize(QSize(90, 25))
        self.data_enable.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_163.addWidget(self.data_enable)

        self.label_321 = QLabel(self.groupBox_29)
        self.label_321.setObjectName(u"label_321")
        sizePolicy2.setHeightForWidth(self.label_321.sizePolicy().hasHeightForWidth())
        self.label_321.setSizePolicy(sizePolicy2)
        self.label_321.setMinimumSize(QSize(90, 25))
        self.label_321.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_163.addWidget(self.label_321)

        self.name_date_prefix = QLineEdit(self.groupBox_29)
        self.name_date_prefix.setObjectName(u"name_date_prefix")
        sizePolicy2.setHeightForWidth(self.name_date_prefix.sizePolicy().hasHeightForWidth())
        self.name_date_prefix.setSizePolicy(sizePolicy2)
        self.name_date_prefix.setMinimumSize(QSize(100, 25))
        self.name_date_prefix.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_163.addWidget(self.name_date_prefix)


        self.horizontalLayout_174.addLayout(self.horizontalLayout_163)


        self.horizontalLayout_192.addWidget(self.groupBox_29)

        self.groupBox_25 = QGroupBox(self.tab_23)
        self.groupBox_25.setObjectName(u"groupBox_25")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.groupBox_25.sizePolicy().hasHeightForWidth())
        self.groupBox_25.setSizePolicy(sizePolicy5)
        self.groupBox_25.setMinimumSize(QSize(400, 55))
        self.groupBox_25.setMaximumSize(QSize(16777215, 55))
        self.groupBox_25.setBaseSize(QSize(350, 70))
        self.groupBox_25.setFlat(False)
        self.verticalLayout_60 = QVBoxLayout(self.groupBox_25)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.horizontalLayout_162 = QHBoxLayout()
        self.horizontalLayout_162.setObjectName(u"horizontalLayout_162")
        self.data_csv_path = QLineEdit(self.groupBox_25)
        self.data_csv_path.setObjectName(u"data_csv_path")
        sizePolicy5.setHeightForWidth(self.data_csv_path.sizePolicy().hasHeightForWidth())
        self.data_csv_path.setSizePolicy(sizePolicy5)
        self.data_csv_path.setMinimumSize(QSize(100, 25))
        self.data_csv_path.setMaximumSize(QSize(16777215, 16777215))
        self.data_csv_path.setDragEnabled(True)

        self.horizontalLayout_162.addWidget(self.data_csv_path)

        self.data_csv_browse = QPushButton(self.groupBox_25)
        self.data_csv_browse.setObjectName(u"data_csv_browse")
        sizePolicy2.setHeightForWidth(self.data_csv_browse.sizePolicy().hasHeightForWidth())
        self.data_csv_browse.setSizePolicy(sizePolicy2)
        self.data_csv_browse.setMinimumSize(QSize(30, 25))
        self.data_csv_browse.setMaximumSize(QSize(60, 25))
        self.data_csv_browse.setAutoFillBackground(False)
        self.data_csv_browse.setIcon(icon)
        self.data_csv_browse.setFlat(True)

        self.horizontalLayout_162.addWidget(self.data_csv_browse)

        self.data_csv_latest = QCheckBox(self.groupBox_25)
        self.data_csv_latest.setObjectName(u"data_csv_latest")
        self.data_csv_latest.setMinimumSize(QSize(120, 25))
        self.data_csv_latest.setMaximumSize(QSize(120, 25))

        self.horizontalLayout_162.addWidget(self.data_csv_latest)


        self.verticalLayout_60.addLayout(self.horizontalLayout_162)


        self.horizontalLayout_192.addWidget(self.groupBox_25)


        self.verticalLayout_75.addLayout(self.horizontalLayout_192)

        self.groupBox_26 = QGroupBox(self.tab_23)
        self.groupBox_26.setObjectName(u"groupBox_26")
        sizePolicy6 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.groupBox_26.sizePolicy().hasHeightForWidth())
        self.groupBox_26.setSizePolicy(sizePolicy6)
        self.groupBox_26.setMinimumSize(QSize(350, 50))
        self.groupBox_26.setMaximumSize(QSize(16777215, 50))
        self.verticalLayout_74 = QVBoxLayout(self.groupBox_26)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.horizontalLayout_180 = QHBoxLayout()
        self.horizontalLayout_180.setObjectName(u"horizontalLayout_180")
        self.horizontalLayout_115 = QHBoxLayout()
        self.horizontalLayout_115.setObjectName(u"horizontalLayout_115")
        self.horizontalLayout_114 = QHBoxLayout()
        self.horizontalLayout_114.setObjectName(u"horizontalLayout_114")
        self.data_package1_chbx = QCheckBox(self.groupBox_26)
        self.data_package1_chbx.setObjectName(u"data_package1_chbx")
        self.data_package1_chbx.setMinimumSize(QSize(80, 25))
        self.data_package1_chbx.setMaximumSize(QSize(80, 16777215))
        self.data_package1_chbx.setChecked(True)

        self.horizontalLayout_114.addWidget(self.data_package1_chbx)

        self.data_package1 = QLineEdit(self.groupBox_26)
        self.data_package1.setObjectName(u"data_package1")
        sizePolicy1.setHeightForWidth(self.data_package1.sizePolicy().hasHeightForWidth())
        self.data_package1.setSizePolicy(sizePolicy1)
        self.data_package1.setMinimumSize(QSize(50, 25))
        self.data_package1.setMaximumSize(QSize(400, 16777215))
        self.data_package1.setReadOnly(False)

        self.horizontalLayout_114.addWidget(self.data_package1)


        self.horizontalLayout_115.addLayout(self.horizontalLayout_114)

        self.horizontalLayout_177 = QHBoxLayout()
        self.horizontalLayout_177.setObjectName(u"horizontalLayout_177")
        self.label_309 = QLabel(self.groupBox_26)
        self.label_309.setObjectName(u"label_309")
        sizePolicy2.setHeightForWidth(self.label_309.sizePolicy().hasHeightForWidth())
        self.label_309.setSizePolicy(sizePolicy2)
        self.label_309.setMinimumSize(QSize(40, 25))
        self.label_309.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_177.addWidget(self.label_309)

        self.data_data1 = QLineEdit(self.groupBox_26)
        self.data_data1.setObjectName(u"data_data1")
        sizePolicy1.setHeightForWidth(self.data_data1.sizePolicy().hasHeightForWidth())
        self.data_data1.setSizePolicy(sizePolicy1)
        self.data_data1.setMinimumSize(QSize(50, 25))
        self.data_data1.setMaximumSize(QSize(400, 16777215))
        self.data_data1.setReadOnly(False)

        self.horizontalLayout_177.addWidget(self.data_data1)


        self.horizontalLayout_115.addLayout(self.horizontalLayout_177)


        self.horizontalLayout_180.addLayout(self.horizontalLayout_115)

        self.horizontalLayout_116 = QHBoxLayout()
        self.horizontalLayout_116.setObjectName(u"horizontalLayout_116")
        self.horizontalLayout_117 = QHBoxLayout()
        self.horizontalLayout_117.setObjectName(u"horizontalLayout_117")
        self.data_package2_chbx = QCheckBox(self.groupBox_26)
        self.data_package2_chbx.setObjectName(u"data_package2_chbx")
        self.data_package2_chbx.setMinimumSize(QSize(80, 25))
        self.data_package2_chbx.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_117.addWidget(self.data_package2_chbx)

        self.data_package2 = QLineEdit(self.groupBox_26)
        self.data_package2.setObjectName(u"data_package2")
        sizePolicy1.setHeightForWidth(self.data_package2.sizePolicy().hasHeightForWidth())
        self.data_package2.setSizePolicy(sizePolicy1)
        self.data_package2.setMinimumSize(QSize(50, 25))
        self.data_package2.setMaximumSize(QSize(400, 16777215))
        self.data_package2.setReadOnly(False)

        self.horizontalLayout_117.addWidget(self.data_package2)


        self.horizontalLayout_116.addLayout(self.horizontalLayout_117)

        self.horizontalLayout_178 = QHBoxLayout()
        self.horizontalLayout_178.setObjectName(u"horizontalLayout_178")
        self.label_310 = QLabel(self.groupBox_26)
        self.label_310.setObjectName(u"label_310")
        sizePolicy2.setHeightForWidth(self.label_310.sizePolicy().hasHeightForWidth())
        self.label_310.setSizePolicy(sizePolicy2)
        self.label_310.setMinimumSize(QSize(40, 25))
        self.label_310.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_178.addWidget(self.label_310)

        self.data_data2 = QLineEdit(self.groupBox_26)
        self.data_data2.setObjectName(u"data_data2")
        sizePolicy1.setHeightForWidth(self.data_data2.sizePolicy().hasHeightForWidth())
        self.data_data2.setSizePolicy(sizePolicy1)
        self.data_data2.setMinimumSize(QSize(50, 25))
        self.data_data2.setMaximumSize(QSize(400, 16777215))
        self.data_data2.setReadOnly(False)

        self.horizontalLayout_178.addWidget(self.data_data2)


        self.horizontalLayout_116.addLayout(self.horizontalLayout_178)


        self.horizontalLayout_180.addLayout(self.horizontalLayout_116)

        self.horizontalLayout_175 = QHBoxLayout()
        self.horizontalLayout_175.setObjectName(u"horizontalLayout_175")
        self.horizontalLayout_176 = QHBoxLayout()
        self.horizontalLayout_176.setObjectName(u"horizontalLayout_176")
        self.data_package3_chbx = QCheckBox(self.groupBox_26)
        self.data_package3_chbx.setObjectName(u"data_package3_chbx")
        self.data_package3_chbx.setMinimumSize(QSize(80, 25))
        self.data_package3_chbx.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_176.addWidget(self.data_package3_chbx)

        self.data_package3 = QLineEdit(self.groupBox_26)
        self.data_package3.setObjectName(u"data_package3")
        sizePolicy1.setHeightForWidth(self.data_package3.sizePolicy().hasHeightForWidth())
        self.data_package3.setSizePolicy(sizePolicy1)
        self.data_package3.setMinimumSize(QSize(50, 25))
        self.data_package3.setMaximumSize(QSize(400, 16777215))
        self.data_package3.setReadOnly(False)

        self.horizontalLayout_176.addWidget(self.data_package3)


        self.horizontalLayout_175.addLayout(self.horizontalLayout_176)

        self.horizontalLayout_179 = QHBoxLayout()
        self.horizontalLayout_179.setObjectName(u"horizontalLayout_179")
        self.label_311 = QLabel(self.groupBox_26)
        self.label_311.setObjectName(u"label_311")
        sizePolicy2.setHeightForWidth(self.label_311.sizePolicy().hasHeightForWidth())
        self.label_311.setSizePolicy(sizePolicy2)
        self.label_311.setMinimumSize(QSize(40, 25))
        self.label_311.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_179.addWidget(self.label_311)

        self.data_data3 = QLineEdit(self.groupBox_26)
        self.data_data3.setObjectName(u"data_data3")
        sizePolicy1.setHeightForWidth(self.data_data3.sizePolicy().hasHeightForWidth())
        self.data_data3.setSizePolicy(sizePolicy1)
        self.data_data3.setMinimumSize(QSize(50, 25))
        self.data_data3.setMaximumSize(QSize(400, 16777215))
        self.data_data3.setReadOnly(False)

        self.horizontalLayout_179.addWidget(self.data_data3)


        self.horizontalLayout_175.addLayout(self.horizontalLayout_179)


        self.horizontalLayout_180.addLayout(self.horizontalLayout_175)


        self.verticalLayout_74.addLayout(self.horizontalLayout_180)


        self.verticalLayout_75.addWidget(self.groupBox_26)

        self.data_table = QTableWidget(self.tab_23)
        self.data_table.setObjectName(u"data_table")
        sizePolicy.setHeightForWidth(self.data_table.sizePolicy().hasHeightForWidth())
        self.data_table.setSizePolicy(sizePolicy)
        self.data_table.setMinimumSize(QSize(600, 100))
        self.data_table.setMaximumSize(QSize(16000, 16000))

        self.verticalLayout_75.addWidget(self.data_table)


        self.verticalLayout_76.addLayout(self.verticalLayout_75)

        self.TopTab.addTab(self.tab_23, "")
        self.tab_11 = QWidget()
        self.tab_11.setObjectName(u"tab_11")
        self.verticalLayout_124 = QVBoxLayout(self.tab_11)
        self.verticalLayout_124.setObjectName(u"verticalLayout_124")
        self.horizontalLayout_218 = QHBoxLayout()
        self.horizontalLayout_218.setObjectName(u"horizontalLayout_218")
        self.verticalLayout_93 = QVBoxLayout()
        self.verticalLayout_93.setObjectName(u"verticalLayout_93")
        self.horizontalLayout_216 = QHBoxLayout()
        self.horizontalLayout_216.setObjectName(u"horizontalLayout_216")
        self.groupBox_35 = QGroupBox(self.tab_11)
        self.groupBox_35.setObjectName(u"groupBox_35")
        self.verticalLayout_38 = QVBoxLayout(self.groupBox_35)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.horizontalLayout_76 = QHBoxLayout()
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.ftrack_use = QCheckBox(self.groupBox_35)
        self.ftrack_use.setObjectName(u"ftrack_use")
        self.ftrack_use.setMinimumSize(QSize(90, 25))
        self.ftrack_use.setMaximumSize(QSize(90, 16777215))
        self.ftrack_use.setChecked(False)

        self.horizontalLayout_76.addWidget(self.ftrack_use)

        self.label_319 = QLabel(self.groupBox_35)
        self.label_319.setObjectName(u"label_319")
        sizePolicy2.setHeightForWidth(self.label_319.sizePolicy().hasHeightForWidth())
        self.label_319.setSizePolicy(sizePolicy2)
        self.label_319.setMinimumSize(QSize(60, 25))
        self.label_319.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_76.addWidget(self.label_319)

        self.ftrack_project = QLineEdit(self.groupBox_35)
        self.ftrack_project.setObjectName(u"ftrack_project")
        sizePolicy1.setHeightForWidth(self.ftrack_project.sizePolicy().hasHeightForWidth())
        self.ftrack_project.setSizePolicy(sizePolicy1)
        self.ftrack_project.setMinimumSize(QSize(200, 25))
        self.ftrack_project.setMaximumSize(QSize(2000, 16777215))

        self.horizontalLayout_76.addWidget(self.ftrack_project)


        self.verticalLayout_38.addLayout(self.horizontalLayout_76)


        self.horizontalLayout_216.addWidget(self.groupBox_35)

        self.groupBox_22 = QGroupBox(self.tab_11)
        self.groupBox_22.setObjectName(u"groupBox_22")
        self.verticalLayout_59 = QVBoxLayout(self.groupBox_22)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.horizontalLayout_129 = QHBoxLayout()
        self.horizontalLayout_129.setObjectName(u"horizontalLayout_129")
        self.horizontalLayout_73 = QHBoxLayout()
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.label_158 = QLabel(self.groupBox_22)
        self.label_158.setObjectName(u"label_158")
        sizePolicy2.setHeightForWidth(self.label_158.sizePolicy().hasHeightForWidth())
        self.label_158.setSizePolicy(sizePolicy2)
        self.label_158.setMinimumSize(QSize(40, 25))
        self.label_158.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_73.addWidget(self.label_158)

        self.ftrack_shot = QLineEdit(self.groupBox_22)
        self.ftrack_shot.setObjectName(u"ftrack_shot")
        sizePolicy2.setHeightForWidth(self.ftrack_shot.sizePolicy().hasHeightForWidth())
        self.ftrack_shot.setSizePolicy(sizePolicy2)
        self.ftrack_shot.setMinimumSize(QSize(150, 25))
        self.ftrack_shot.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_73.addWidget(self.ftrack_shot)


        self.horizontalLayout_129.addLayout(self.horizontalLayout_73)

        self.horizontalLayout_75 = QHBoxLayout()
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.label_159 = QLabel(self.groupBox_22)
        self.label_159.setObjectName(u"label_159")
        sizePolicy2.setHeightForWidth(self.label_159.sizePolicy().hasHeightForWidth())
        self.label_159.setSizePolicy(sizePolicy2)
        self.label_159.setMinimumSize(QSize(40, 25))
        self.label_159.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_75.addWidget(self.label_159)

        self.ftrack_task = QLineEdit(self.groupBox_22)
        self.ftrack_task.setObjectName(u"ftrack_task")
        sizePolicy2.setHeightForWidth(self.ftrack_task.sizePolicy().hasHeightForWidth())
        self.ftrack_task.setSizePolicy(sizePolicy2)
        self.ftrack_task.setMinimumSize(QSize(150, 25))
        self.ftrack_task.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_75.addWidget(self.ftrack_task)


        self.horizontalLayout_129.addLayout(self.horizontalLayout_75)

        self.horizontalLayout_80 = QHBoxLayout()
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.label_318 = QLabel(self.groupBox_22)
        self.label_318.setObjectName(u"label_318")
        sizePolicy2.setHeightForWidth(self.label_318.sizePolicy().hasHeightForWidth())
        self.label_318.setSizePolicy(sizePolicy2)
        self.label_318.setMinimumSize(QSize(70, 25))
        self.label_318.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_80.addWidget(self.label_318)

        self.ftrack_include_2 = QLineEdit(self.groupBox_22)
        self.ftrack_include_2.setObjectName(u"ftrack_include_2")
        sizePolicy2.setHeightForWidth(self.ftrack_include_2.sizePolicy().hasHeightForWidth())
        self.ftrack_include_2.setSizePolicy(sizePolicy2)
        self.ftrack_include_2.setMinimumSize(QSize(150, 25))
        self.ftrack_include_2.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_80.addWidget(self.ftrack_include_2)


        self.horizontalLayout_129.addLayout(self.horizontalLayout_80)


        self.verticalLayout_59.addLayout(self.horizontalLayout_129)


        self.horizontalLayout_216.addWidget(self.groupBox_22)


        self.verticalLayout_93.addLayout(self.horizontalLayout_216)

        self.ftrack_table = QTableWidget(self.tab_11)
        self.ftrack_table.setObjectName(u"ftrack_table")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.ftrack_table.sizePolicy().hasHeightForWidth())
        self.ftrack_table.setSizePolicy(sizePolicy7)
        self.ftrack_table.setMinimumSize(QSize(400, 100))
        self.ftrack_table.setMaximumSize(QSize(16000, 16000))

        self.verticalLayout_93.addWidget(self.ftrack_table)


        self.horizontalLayout_218.addLayout(self.verticalLayout_93)

        self.verticalLayout_123 = QVBoxLayout()
        self.verticalLayout_123.setObjectName(u"verticalLayout_123")
        self.groupBox_23 = QGroupBox(self.tab_11)
        self.groupBox_23.setObjectName(u"groupBox_23")
        sizePolicy8 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.groupBox_23.sizePolicy().hasHeightForWidth())
        self.groupBox_23.setSizePolicy(sizePolicy8)
        self.horizontalLayout_215 = QHBoxLayout(self.groupBox_23)
        self.horizontalLayout_215.setObjectName(u"horizontalLayout_215")
        self.ftrack_do_op = QCheckBox(self.groupBox_23)
        self.ftrack_do_op.setObjectName(u"ftrack_do_op")
        sizePolicy2.setHeightForWidth(self.ftrack_do_op.sizePolicy().hasHeightForWidth())
        self.ftrack_do_op.setSizePolicy(sizePolicy2)
        self.ftrack_do_op.setMinimumSize(QSize(280, 25))
        self.ftrack_do_op.setMaximumSize(QSize(280, 16777215))
        self.ftrack_do_op.setChecked(False)

        self.horizontalLayout_215.addWidget(self.ftrack_do_op)


        self.verticalLayout_123.addWidget(self.groupBox_23)

        self.groupBox_21 = QGroupBox(self.tab_11)
        self.groupBox_21.setObjectName(u"groupBox_21")
        sizePolicy8.setHeightForWidth(self.groupBox_21.sizePolicy().hasHeightForWidth())
        self.groupBox_21.setSizePolicy(sizePolicy8)
        self.verticalLayout_64 = QVBoxLayout(self.groupBox_21)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.ftrack_do_notes = QCheckBox(self.groupBox_21)
        self.ftrack_do_notes.setObjectName(u"ftrack_do_notes")
        self.ftrack_do_notes.setMinimumSize(QSize(120, 25))
        self.ftrack_do_notes.setMaximumSize(QSize(120, 16777215))
        self.ftrack_do_notes.setChecked(False)

        self.verticalLayout_18.addWidget(self.ftrack_do_notes)

        self.horizontalLayout_77 = QHBoxLayout()
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.ftrack_label_use = QCheckBox(self.groupBox_21)
        self.ftrack_label_use.setObjectName(u"ftrack_label_use")
        self.ftrack_label_use.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.ftrack_label_use.sizePolicy().hasHeightForWidth())
        self.ftrack_label_use.setSizePolicy(sizePolicy2)
        self.ftrack_label_use.setMinimumSize(QSize(80, 25))
        self.ftrack_label_use.setCheckable(True)

        self.horizontalLayout_77.addWidget(self.ftrack_label_use)

        self.ftrack_label = QLineEdit(self.groupBox_21)
        self.ftrack_label.setObjectName(u"ftrack_label")
        self.ftrack_label.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.ftrack_label.sizePolicy().hasHeightForWidth())
        self.ftrack_label.setSizePolicy(sizePolicy2)
        self.ftrack_label.setMinimumSize(QSize(200, 25))
        self.ftrack_label.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_77.addWidget(self.ftrack_label)


        self.verticalLayout_18.addLayout(self.horizontalLayout_77)

        self.horizontalLayout_79 = QHBoxLayout()
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.ftrack_version_use = QCheckBox(self.groupBox_21)
        self.ftrack_version_use.setObjectName(u"ftrack_version_use")
        sizePolicy2.setHeightForWidth(self.ftrack_version_use.sizePolicy().hasHeightForWidth())
        self.ftrack_version_use.setSizePolicy(sizePolicy2)
        self.ftrack_version_use.setMinimumSize(QSize(80, 25))

        self.horizontalLayout_79.addWidget(self.ftrack_version_use)

        self.ftrack_version = QLineEdit(self.groupBox_21)
        self.ftrack_version.setObjectName(u"ftrack_version")
        sizePolicy2.setHeightForWidth(self.ftrack_version.sizePolicy().hasHeightForWidth())
        self.ftrack_version.setSizePolicy(sizePolicy2)
        self.ftrack_version.setMinimumSize(QSize(200, 25))
        self.ftrack_version.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_79.addWidget(self.ftrack_version)


        self.verticalLayout_18.addLayout(self.horizontalLayout_79)

        self.horizontalLayout_81 = QHBoxLayout()
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.label_91 = QLabel(self.groupBox_21)
        self.label_91.setObjectName(u"label_91")
        sizePolicy2.setHeightForWidth(self.label_91.sizePolicy().hasHeightForWidth())
        self.label_91.setSizePolicy(sizePolicy2)
        self.label_91.setMinimumSize(QSize(80, 25))

        self.horizontalLayout_81.addWidget(self.label_91)

        self.ftrack_note_pattern = QLineEdit(self.groupBox_21)
        self.ftrack_note_pattern.setObjectName(u"ftrack_note_pattern")
        sizePolicy2.setHeightForWidth(self.ftrack_note_pattern.sizePolicy().hasHeightForWidth())
        self.ftrack_note_pattern.setSizePolicy(sizePolicy2)
        self.ftrack_note_pattern.setMinimumSize(QSize(200, 25))
        self.ftrack_note_pattern.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_81.addWidget(self.ftrack_note_pattern)


        self.verticalLayout_18.addLayout(self.horizontalLayout_81)

        self.horizontalLayout_72 = QHBoxLayout()
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.label_160 = QLabel(self.groupBox_21)
        self.label_160.setObjectName(u"label_160")
        sizePolicy2.setHeightForWidth(self.label_160.sizePolicy().hasHeightForWidth())
        self.label_160.setSizePolicy(sizePolicy2)
        self.label_160.setMinimumSize(QSize(80, 25))

        self.horizontalLayout_72.addWidget(self.label_160)

        self.ftrack_note_repl = QLineEdit(self.groupBox_21)
        self.ftrack_note_repl.setObjectName(u"ftrack_note_repl")
        sizePolicy2.setHeightForWidth(self.ftrack_note_repl.sizePolicy().hasHeightForWidth())
        self.ftrack_note_repl.setSizePolicy(sizePolicy2)
        self.ftrack_note_repl.setMinimumSize(QSize(200, 25))
        self.ftrack_note_repl.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_72.addWidget(self.ftrack_note_repl)


        self.verticalLayout_18.addLayout(self.horizontalLayout_72)


        self.verticalLayout_64.addLayout(self.verticalLayout_18)


        self.verticalLayout_123.addWidget(self.groupBox_21)

        self.groupBox_37 = QGroupBox(self.tab_11)
        self.groupBox_37.setObjectName(u"groupBox_37")
        sizePolicy8.setHeightForWidth(self.groupBox_37.sizePolicy().hasHeightForWidth())
        self.groupBox_37.setSizePolicy(sizePolicy8)
        self.verticalLayout_58 = QVBoxLayout(self.groupBox_37)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.horizontalLayout_217 = QHBoxLayout()
        self.horizontalLayout_217.setObjectName(u"horizontalLayout_217")
        self.ftrack_export = QPushButton(self.groupBox_37)
        self.ftrack_export.setObjectName(u"ftrack_export")
        sizePolicy2.setHeightForWidth(self.ftrack_export.sizePolicy().hasHeightForWidth())
        self.ftrack_export.setSizePolicy(sizePolicy2)
        self.ftrack_export.setMinimumSize(QSize(80, 30))
        self.ftrack_export.setMaximumSize(QSize(80, 30))

        self.horizontalLayout_217.addWidget(self.ftrack_export)

        self.ftrack_path = QLineEdit(self.groupBox_37)
        self.ftrack_path.setObjectName(u"ftrack_path")
        sizePolicy1.setHeightForWidth(self.ftrack_path.sizePolicy().hasHeightForWidth())
        self.ftrack_path.setSizePolicy(sizePolicy1)
        self.ftrack_path.setMinimumSize(QSize(200, 25))
        self.ftrack_path.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_217.addWidget(self.ftrack_path)


        self.verticalLayout_58.addLayout(self.horizontalLayout_217)


        self.verticalLayout_123.addWidget(self.groupBox_37)


        self.horizontalLayout_218.addLayout(self.verticalLayout_123)


        self.verticalLayout_124.addLayout(self.horizontalLayout_218)

        self.TopTab.addTab(self.tab_11, "")
        self.tab_16 = QWidget()
        self.tab_16.setObjectName(u"tab_16")
        self.horizontalLayout_173 = QHBoxLayout(self.tab_16)
        self.horizontalLayout_173.setObjectName(u"horizontalLayout_173")
        self.scrollArea_4 = QScrollArea(self.tab_16)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        sizePolicy.setHeightForWidth(self.scrollArea_4.sizePolicy().hasHeightForWidth())
        self.scrollArea_4.setSizePolicy(sizePolicy)
        self.scrollArea_4.setMinimumSize(QSize(800, 150))
        self.scrollArea_4.setMaximumSize(QSize(6000, 450))
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1196, 469))
        self.verticalLayout_62 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.verticalLayout_61 = QVBoxLayout()
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.horizontalLayout_151 = QHBoxLayout()
        self.horizontalLayout_151.setObjectName(u"horizontalLayout_151")
        self.groupBox_11 = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_11.setObjectName(u"groupBox_11")
        sizePolicy1.setHeightForWidth(self.groupBox_11.sizePolicy().hasHeightForWidth())
        self.groupBox_11.setSizePolicy(sizePolicy1)
        self.groupBox_11.setMinimumSize(QSize(400, 55))
        self.groupBox_11.setMaximumSize(QSize(750, 55))
        self.groupBox_11.setBaseSize(QSize(350, 70))
        self.groupBox_11.setFlat(False)
        self.verticalLayout_54 = QVBoxLayout(self.groupBox_11)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.horizontalLayout_127 = QHBoxLayout()
        self.horizontalLayout_127.setObjectName(u"horizontalLayout_127")
        self.horizontalLayout_122 = QHBoxLayout()
        self.horizontalLayout_122.setObjectName(u"horizontalLayout_122")
        self.vendor_csv_path_detect = QCheckBox(self.groupBox_11)
        self.vendor_csv_path_detect.setObjectName(u"vendor_csv_path_detect")
        sizePolicy2.setHeightForWidth(self.vendor_csv_path_detect.sizePolicy().hasHeightForWidth())
        self.vendor_csv_path_detect.setSizePolicy(sizePolicy2)
        self.vendor_csv_path_detect.setMinimumSize(QSize(100, 25))
        self.vendor_csv_path_detect.setMaximumSize(QSize(100, 25))
        self.vendor_csv_path_detect.setChecked(False)

        self.horizontalLayout_122.addWidget(self.vendor_csv_path_detect)

        self.vendor_csv_path = QLineEdit(self.groupBox_11)
        self.vendor_csv_path.setObjectName(u"vendor_csv_path")
        sizePolicy5.setHeightForWidth(self.vendor_csv_path.sizePolicy().hasHeightForWidth())
        self.vendor_csv_path.setSizePolicy(sizePolicy5)
        self.vendor_csv_path.setMinimumSize(QSize(100, 25))
        self.vendor_csv_path.setMaximumSize(QSize(16000, 16777215))
        self.vendor_csv_path.setDragEnabled(True)

        self.horizontalLayout_122.addWidget(self.vendor_csv_path)


        self.horizontalLayout_127.addLayout(self.horizontalLayout_122)

        self.horizontalLayout_123 = QHBoxLayout()
        self.horizontalLayout_123.setObjectName(u"horizontalLayout_123")
        self.vendor_csv_explore = QPushButton(self.groupBox_11)
        self.vendor_csv_explore.setObjectName(u"vendor_csv_explore")
        sizePolicy2.setHeightForWidth(self.vendor_csv_explore.sizePolicy().hasHeightForWidth())
        self.vendor_csv_explore.setSizePolicy(sizePolicy2)
        self.vendor_csv_explore.setMinimumSize(QSize(20, 25))
        self.vendor_csv_explore.setMaximumSize(QSize(25, 25))
        self.vendor_csv_explore.setAutoFillBackground(False)
        self.vendor_csv_explore.setIcon(icon1)
        self.vendor_csv_explore.setFlat(True)

        self.horizontalLayout_123.addWidget(self.vendor_csv_explore)

        self.vendor_csv_browse = QPushButton(self.groupBox_11)
        self.vendor_csv_browse.setObjectName(u"vendor_csv_browse")
        sizePolicy2.setHeightForWidth(self.vendor_csv_browse.sizePolicy().hasHeightForWidth())
        self.vendor_csv_browse.setSizePolicy(sizePolicy2)
        self.vendor_csv_browse.setMinimumSize(QSize(30, 25))
        self.vendor_csv_browse.setMaximumSize(QSize(60, 25))
        self.vendor_csv_browse.setAutoFillBackground(False)
        self.vendor_csv_browse.setIcon(icon)
        self.vendor_csv_browse.setFlat(True)

        self.horizontalLayout_123.addWidget(self.vendor_csv_browse)


        self.horizontalLayout_127.addLayout(self.horizontalLayout_123)


        self.verticalLayout_54.addLayout(self.horizontalLayout_127)


        self.horizontalLayout_151.addWidget(self.groupBox_11)

        self.groupBox_12 = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_12.setObjectName(u"groupBox_12")
        sizePolicy6.setHeightForWidth(self.groupBox_12.sizePolicy().hasHeightForWidth())
        self.groupBox_12.setSizePolicy(sizePolicy6)
        self.groupBox_12.setMinimumSize(QSize(350, 50))
        self.groupBox_12.setMaximumSize(QSize(16777215, 50))
        self.verticalLayout_51 = QVBoxLayout(self.groupBox_12)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.horizontalLayout_126 = QHBoxLayout()
        self.horizontalLayout_126.setObjectName(u"horizontalLayout_126")
        self.horizontalLayout_124 = QHBoxLayout()
        self.horizontalLayout_124.setObjectName(u"horizontalLayout_124")
        self.label_163 = QLabel(self.groupBox_12)
        self.label_163.setObjectName(u"label_163")
        sizePolicy2.setHeightForWidth(self.label_163.sizePolicy().hasHeightForWidth())
        self.label_163.setSizePolicy(sizePolicy2)
        self.label_163.setMinimumSize(QSize(60, 25))
        self.label_163.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_124.addWidget(self.label_163)

        self.vendor_csv_package_key = QLineEdit(self.groupBox_12)
        self.vendor_csv_package_key.setObjectName(u"vendor_csv_package_key")
        sizePolicy5.setHeightForWidth(self.vendor_csv_package_key.sizePolicy().hasHeightForWidth())
        self.vendor_csv_package_key.setSizePolicy(sizePolicy5)
        self.vendor_csv_package_key.setMinimumSize(QSize(50, 25))
        self.vendor_csv_package_key.setMaximumSize(QSize(400, 16777215))
        self.vendor_csv_package_key.setReadOnly(False)

        self.horizontalLayout_124.addWidget(self.vendor_csv_package_key)


        self.horizontalLayout_126.addLayout(self.horizontalLayout_124)

        self.horizontalLayout_125 = QHBoxLayout()
        self.horizontalLayout_125.setObjectName(u"horizontalLayout_125")
        self.label_164 = QLabel(self.groupBox_12)
        self.label_164.setObjectName(u"label_164")
        sizePolicy2.setHeightForWidth(self.label_164.sizePolicy().hasHeightForWidth())
        self.label_164.setSizePolicy(sizePolicy2)
        self.label_164.setMinimumSize(QSize(60, 25))
        self.label_164.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_125.addWidget(self.label_164)

        self.vendor_csv_vendor_key = QLineEdit(self.groupBox_12)
        self.vendor_csv_vendor_key.setObjectName(u"vendor_csv_vendor_key")
        sizePolicy5.setHeightForWidth(self.vendor_csv_vendor_key.sizePolicy().hasHeightForWidth())
        self.vendor_csv_vendor_key.setSizePolicy(sizePolicy5)
        self.vendor_csv_vendor_key.setMinimumSize(QSize(50, 25))
        self.vendor_csv_vendor_key.setMaximumSize(QSize(400, 16777215))
        self.vendor_csv_vendor_key.setReadOnly(False)

        self.horizontalLayout_125.addWidget(self.vendor_csv_vendor_key)


        self.horizontalLayout_126.addLayout(self.horizontalLayout_125)


        self.verticalLayout_51.addLayout(self.horizontalLayout_126)


        self.horizontalLayout_151.addWidget(self.groupBox_12)


        self.verticalLayout_61.addLayout(self.horizontalLayout_151)

        self.groupBox_24 = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_24.setObjectName(u"groupBox_24")
        sizePolicy1.setHeightForWidth(self.groupBox_24.sizePolicy().hasHeightForWidth())
        self.groupBox_24.setSizePolicy(sizePolicy1)
        self.groupBox_24.setMinimumSize(QSize(350, 50))
        self.groupBox_24.setMaximumSize(QSize(16777215, 50))
        self.verticalLayout_55 = QVBoxLayout(self.groupBox_24)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.horizontalLayout_172 = QHBoxLayout()
        self.horizontalLayout_172.setObjectName(u"horizontalLayout_172")
        self.horizontalLayout_171 = QHBoxLayout()
        self.horizontalLayout_171.setObjectName(u"horizontalLayout_171")
        self.vendor_csv_ignore = QCheckBox(self.groupBox_24)
        self.vendor_csv_ignore.setObjectName(u"vendor_csv_ignore")
        sizePolicy2.setHeightForWidth(self.vendor_csv_ignore.sizePolicy().hasHeightForWidth())
        self.vendor_csv_ignore.setSizePolicy(sizePolicy2)
        self.vendor_csv_ignore.setMinimumSize(QSize(160, 25))

        self.horizontalLayout_171.addWidget(self.vendor_csv_ignore)

        self.vendor_csv_ftrack = QCheckBox(self.groupBox_24)
        self.vendor_csv_ftrack.setObjectName(u"vendor_csv_ftrack")
        sizePolicy2.setHeightForWidth(self.vendor_csv_ftrack.sizePolicy().hasHeightForWidth())
        self.vendor_csv_ftrack.setSizePolicy(sizePolicy2)
        self.vendor_csv_ftrack.setMinimumSize(QSize(170, 25))

        self.horizontalLayout_171.addWidget(self.vendor_csv_ftrack)


        self.horizontalLayout_172.addLayout(self.horizontalLayout_171)

        self.horizontalLayout_152 = QHBoxLayout()
        self.horizontalLayout_152.setObjectName(u"horizontalLayout_152")
        self.vendor_csv_skip = QCheckBox(self.groupBox_24)
        self.vendor_csv_skip.setObjectName(u"vendor_csv_skip")
        self.vendor_csv_skip.setMinimumSize(QSize(70, 25))
        self.vendor_csv_skip.setMaximumSize(QSize(70, 25))

        self.horizontalLayout_152.addWidget(self.vendor_csv_skip)

        self.vendor_csv_skip_by = QLineEdit(self.groupBox_24)
        self.vendor_csv_skip_by.setObjectName(u"vendor_csv_skip_by")
        sizePolicy5.setHeightForWidth(self.vendor_csv_skip_by.sizePolicy().hasHeightForWidth())
        self.vendor_csv_skip_by.setSizePolicy(sizePolicy5)
        self.vendor_csv_skip_by.setMinimumSize(QSize(50, 25))
        self.vendor_csv_skip_by.setMaximumSize(QSize(200, 25))
        self.vendor_csv_skip_by.setReadOnly(False)

        self.horizontalLayout_152.addWidget(self.vendor_csv_skip_by)

        self.label_308 = QLabel(self.groupBox_24)
        self.label_308.setObjectName(u"label_308")
        sizePolicy2.setHeightForWidth(self.label_308.sizePolicy().hasHeightForWidth())
        self.label_308.setSizePolicy(sizePolicy2)
        self.label_308.setMinimumSize(QSize(60, 25))
        self.label_308.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_152.addWidget(self.label_308)

        self.vendor_csv_skip_what = QLineEdit(self.groupBox_24)
        self.vendor_csv_skip_what.setObjectName(u"vendor_csv_skip_what")
        sizePolicy5.setHeightForWidth(self.vendor_csv_skip_what.sizePolicy().hasHeightForWidth())
        self.vendor_csv_skip_what.setSizePolicy(sizePolicy5)
        self.vendor_csv_skip_what.setMinimumSize(QSize(100, 25))
        self.vendor_csv_skip_what.setMaximumSize(QSize(16000, 16777215))
        self.vendor_csv_skip_what.setDragEnabled(True)

        self.horizontalLayout_152.addWidget(self.vendor_csv_skip_what)


        self.horizontalLayout_172.addLayout(self.horizontalLayout_152)


        self.verticalLayout_55.addLayout(self.horizontalLayout_172)


        self.verticalLayout_61.addWidget(self.groupBox_24)

        self.horizontalLayout_128 = QHBoxLayout()
        self.horizontalLayout_128.setObjectName(u"horizontalLayout_128")
        self.verticalLayout_56 = QVBoxLayout()
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.label_30 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_30.setObjectName(u"label_30")
        sizePolicy2.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy2)
        self.label_30.setMinimumSize(QSize(150, 20))
        self.label_30.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_56.addWidget(self.label_30)

        self.vendor_csv_prefs_spreadsheet = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.vendor_csv_prefs_spreadsheet.setObjectName(u"vendor_csv_prefs_spreadsheet")
        sizePolicy9 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.vendor_csv_prefs_spreadsheet.sizePolicy().hasHeightForWidth())
        self.vendor_csv_prefs_spreadsheet.setSizePolicy(sizePolicy9)
        self.vendor_csv_prefs_spreadsheet.setMinimumSize(QSize(150, 300))
        self.vendor_csv_prefs_spreadsheet.setMaximumSize(QSize(16777215, 400))

        self.verticalLayout_56.addWidget(self.vendor_csv_prefs_spreadsheet)


        self.horizontalLayout_128.addLayout(self.verticalLayout_56)

        self.verticalLayout_57 = QVBoxLayout()
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.label_31 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_31.setObjectName(u"label_31")
        sizePolicy2.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy2)
        self.label_31.setMinimumSize(QSize(150, 20))
        self.label_31.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_57.addWidget(self.label_31)

        self.vendor_csv_prefs_repres = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.vendor_csv_prefs_repres.setObjectName(u"vendor_csv_prefs_repres")
        sizePolicy9.setHeightForWidth(self.vendor_csv_prefs_repres.sizePolicy().hasHeightForWidth())
        self.vendor_csv_prefs_repres.setSizePolicy(sizePolicy9)
        self.vendor_csv_prefs_repres.setMinimumSize(QSize(150, 300))
        self.vendor_csv_prefs_repres.setMaximumSize(QSize(16777215, 400))

        self.verticalLayout_57.addWidget(self.vendor_csv_prefs_repres)


        self.horizontalLayout_128.addLayout(self.verticalLayout_57)


        self.verticalLayout_61.addLayout(self.horizontalLayout_128)


        self.verticalLayout_62.addLayout(self.verticalLayout_61)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout_173.addWidget(self.scrollArea_4)

        self.TopTab.addTab(self.tab_16, "")
        self.tab_26 = QWidget()
        self.tab_26.setObjectName(u"tab_26")
        self.verticalLayout_122 = QVBoxLayout(self.tab_26)
        self.verticalLayout_122.setObjectName(u"verticalLayout_122")
        self.verticalLayout_121 = QVBoxLayout()
        self.verticalLayout_121.setObjectName(u"verticalLayout_121")
        self.groupBox_36 = QGroupBox(self.tab_26)
        self.groupBox_36.setObjectName(u"groupBox_36")
        sizePolicy5.setHeightForWidth(self.groupBox_36.sizePolicy().hasHeightForWidth())
        self.groupBox_36.setSizePolicy(sizePolicy5)
        self.groupBox_36.setMinimumSize(QSize(400, 55))
        self.groupBox_36.setMaximumSize(QSize(16777215, 55))
        self.groupBox_36.setBaseSize(QSize(350, 70))
        self.groupBox_36.setFlat(False)
        self.verticalLayout_120 = QVBoxLayout(self.groupBox_36)
        self.verticalLayout_120.setObjectName(u"verticalLayout_120")
        self.horizontalLayout_214 = QHBoxLayout()
        self.horizontalLayout_214.setObjectName(u"horizontalLayout_214")
        self.replace_enable = QCheckBox(self.groupBox_36)
        self.replace_enable.setObjectName(u"replace_enable")
        sizePolicy2.setHeightForWidth(self.replace_enable.sizePolicy().hasHeightForWidth())
        self.replace_enable.setSizePolicy(sizePolicy2)
        self.replace_enable.setMinimumSize(QSize(70, 25))
        self.replace_enable.setMaximumSize(QSize(70, 25))

        self.horizontalLayout_214.addWidget(self.replace_enable)

        self.replace_csv_path = QLineEdit(self.groupBox_36)
        self.replace_csv_path.setObjectName(u"replace_csv_path")
        sizePolicy5.setHeightForWidth(self.replace_csv_path.sizePolicy().hasHeightForWidth())
        self.replace_csv_path.setSizePolicy(sizePolicy5)
        self.replace_csv_path.setMinimumSize(QSize(100, 25))
        self.replace_csv_path.setMaximumSize(QSize(16777215, 16777215))
        self.replace_csv_path.setDragEnabled(True)

        self.horizontalLayout_214.addWidget(self.replace_csv_path)

        self.data_csv_browse_2 = QPushButton(self.groupBox_36)
        self.data_csv_browse_2.setObjectName(u"data_csv_browse_2")
        sizePolicy2.setHeightForWidth(self.data_csv_browse_2.sizePolicy().hasHeightForWidth())
        self.data_csv_browse_2.setSizePolicy(sizePolicy2)
        self.data_csv_browse_2.setMinimumSize(QSize(30, 25))
        self.data_csv_browse_2.setMaximumSize(QSize(60, 25))
        self.data_csv_browse_2.setAutoFillBackground(False)
        self.data_csv_browse_2.setIcon(icon)
        self.data_csv_browse_2.setFlat(True)

        self.horizontalLayout_214.addWidget(self.data_csv_browse_2)

        self.replace_withgo = QCheckBox(self.groupBox_36)
        self.replace_withgo.setObjectName(u"replace_withgo")
        sizePolicy2.setHeightForWidth(self.replace_withgo.sizePolicy().hasHeightForWidth())
        self.replace_withgo.setSizePolicy(sizePolicy2)
        self.replace_withgo.setMinimumSize(QSize(120, 25))
        self.replace_withgo.setMaximumSize(QSize(120, 25))

        self.horizontalLayout_214.addWidget(self.replace_withgo)

        self.replace_button = QPushButton(self.groupBox_36)
        self.replace_button.setObjectName(u"replace_button")
        sizePolicy2.setHeightForWidth(self.replace_button.sizePolicy().hasHeightForWidth())
        self.replace_button.setSizePolicy(sizePolicy2)
        self.replace_button.setMinimumSize(QSize(100, 30))
        self.replace_button.setMaximumSize(QSize(100, 30))

        self.horizontalLayout_214.addWidget(self.replace_button)


        self.verticalLayout_120.addLayout(self.horizontalLayout_214)


        self.verticalLayout_121.addWidget(self.groupBox_36)

        self.replace_table = QTableWidget(self.tab_26)
        self.replace_table.setObjectName(u"replace_table")
        sizePolicy.setHeightForWidth(self.replace_table.sizePolicy().hasHeightForWidth())
        self.replace_table.setSizePolicy(sizePolicy)
        self.replace_table.setMinimumSize(QSize(600, 100))
        self.replace_table.setMaximumSize(QSize(16000, 16000))

        self.verticalLayout_121.addWidget(self.replace_table)


        self.verticalLayout_122.addLayout(self.verticalLayout_121)

        self.TopTab.addTab(self.tab_26, "")
        self.tab_18 = QWidget()
        self.tab_18.setObjectName(u"tab_18")
        self.verticalLayout_35 = QVBoxLayout(self.tab_18)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_34 = QVBoxLayout()
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.thumbs_make_on_go = QCheckBox(self.tab_18)
        self.thumbs_make_on_go.setObjectName(u"thumbs_make_on_go")
        sizePolicy2.setHeightForWidth(self.thumbs_make_on_go.sizePolicy().hasHeightForWidth())
        self.thumbs_make_on_go.setSizePolicy(sizePolicy2)
        self.thumbs_make_on_go.setMinimumSize(QSize(130, 25))
        self.thumbs_make_on_go.setMaximumSize(QSize(150, 25))
        self.thumbs_make_on_go.setChecked(False)

        self.horizontalLayout_2.addWidget(self.thumbs_make_on_go)

        self.thumbs_convert_now = QPushButton(self.tab_18)
        self.thumbs_convert_now.setObjectName(u"thumbs_convert_now")
        sizePolicy1.setHeightForWidth(self.thumbs_convert_now.sizePolicy().hasHeightForWidth())
        self.thumbs_convert_now.setSizePolicy(sizePolicy1)
        self.thumbs_convert_now.setMinimumSize(QSize(200, 25))
        self.thumbs_convert_now.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_2.addWidget(self.thumbs_convert_now)

        self.thumbs_skip_existing = QCheckBox(self.tab_18)
        self.thumbs_skip_existing.setObjectName(u"thumbs_skip_existing")
        self.thumbs_skip_existing.setChecked(True)

        self.horizontalLayout_2.addWidget(self.thumbs_skip_existing)


        self.verticalLayout_34.addLayout(self.horizontalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_161 = QHBoxLayout()
        self.horizontalLayout_161.setObjectName(u"horizontalLayout_161")
        self.label_34 = QLabel(self.tab_18)
        self.label_34.setObjectName(u"label_34")
        sizePolicy2.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy2)
        self.label_34.setMinimumSize(QSize(25, 25))
        self.label_34.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_161.addWidget(self.label_34)

        self.thumbs_if_01 = QLineEdit(self.tab_18)
        self.thumbs_if_01.setObjectName(u"thumbs_if_01")
        sizePolicy1.setHeightForWidth(self.thumbs_if_01.sizePolicy().hasHeightForWidth())
        self.thumbs_if_01.setSizePolicy(sizePolicy1)
        self.thumbs_if_01.setMinimumSize(QSize(75, 25))
        self.thumbs_if_01.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_161.addWidget(self.thumbs_if_01)

        self.label_276 = QLabel(self.tab_18)
        self.label_276.setObjectName(u"label_276")
        sizePolicy2.setHeightForWidth(self.label_276.sizePolicy().hasHeightForWidth())
        self.label_276.setSizePolicy(sizePolicy2)
        self.label_276.setMinimumSize(QSize(75, 25))

        self.horizontalLayout_161.addWidget(self.label_276)

        self.thumbs_exe_01 = QLineEdit(self.tab_18)
        self.thumbs_exe_01.setObjectName(u"thumbs_exe_01")
        sizePolicy1.setHeightForWidth(self.thumbs_exe_01.sizePolicy().hasHeightForWidth())
        self.thumbs_exe_01.setSizePolicy(sizePolicy1)
        self.thumbs_exe_01.setMinimumSize(QSize(100, 25))
        self.thumbs_exe_01.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_161.addWidget(self.thumbs_exe_01)

        self.label_277 = QLabel(self.tab_18)
        self.label_277.setObjectName(u"label_277")
        sizePolicy2.setHeightForWidth(self.label_277.sizePolicy().hasHeightForWidth())
        self.label_277.setSizePolicy(sizePolicy2)
        self.label_277.setMinimumSize(QSize(75, 25))

        self.horizontalLayout_161.addWidget(self.label_277)

        self.thumbs_args_01 = QLineEdit(self.tab_18)
        self.thumbs_args_01.setObjectName(u"thumbs_args_01")
        sizePolicy1.setHeightForWidth(self.thumbs_args_01.sizePolicy().hasHeightForWidth())
        self.thumbs_args_01.setSizePolicy(sizePolicy1)
        self.thumbs_args_01.setMinimumSize(QSize(150, 25))
        self.thumbs_args_01.setMaximumSize(QSize(4096, 16777215))

        self.horizontalLayout_161.addWidget(self.thumbs_args_01)

        self.label_278 = QLabel(self.tab_18)
        self.label_278.setObjectName(u"label_278")
        sizePolicy2.setHeightForWidth(self.label_278.sizePolicy().hasHeightForWidth())
        self.label_278.setSizePolicy(sizePolicy2)
        self.label_278.setMinimumSize(QSize(75, 25))

        self.horizontalLayout_161.addWidget(self.label_278)

        self.thumbs_name_01 = QLineEdit(self.tab_18)
        self.thumbs_name_01.setObjectName(u"thumbs_name_01")
        sizePolicy1.setHeightForWidth(self.thumbs_name_01.sizePolicy().hasHeightForWidth())
        self.thumbs_name_01.setSizePolicy(sizePolicy1)
        self.thumbs_name_01.setMinimumSize(QSize(100, 25))
        self.thumbs_name_01.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_161.addWidget(self.thumbs_name_01)


        self.verticalLayout_3.addLayout(self.horizontalLayout_161)

        self.horizontalLayout_164 = QHBoxLayout()
        self.horizontalLayout_164.setObjectName(u"horizontalLayout_164")
        self.label_280 = QLabel(self.tab_18)
        self.label_280.setObjectName(u"label_280")
        sizePolicy2.setHeightForWidth(self.label_280.sizePolicy().hasHeightForWidth())
        self.label_280.setSizePolicy(sizePolicy2)
        self.label_280.setMinimumSize(QSize(25, 25))
        self.label_280.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_164.addWidget(self.label_280)

        self.thumbs_if_02 = QLineEdit(self.tab_18)
        self.thumbs_if_02.setObjectName(u"thumbs_if_02")
        sizePolicy1.setHeightForWidth(self.thumbs_if_02.sizePolicy().hasHeightForWidth())
        self.thumbs_if_02.setSizePolicy(sizePolicy1)
        self.thumbs_if_02.setMinimumSize(QSize(75, 25))
        self.thumbs_if_02.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_164.addWidget(self.thumbs_if_02)

        self.label_281 = QLabel(self.tab_18)
        self.label_281.setObjectName(u"label_281")
        sizePolicy2.setHeightForWidth(self.label_281.sizePolicy().hasHeightForWidth())
        self.label_281.setSizePolicy(sizePolicy2)
        self.label_281.setMinimumSize(QSize(75, 25))

        self.horizontalLayout_164.addWidget(self.label_281)

        self.thumbs_exe_02 = QLineEdit(self.tab_18)
        self.thumbs_exe_02.setObjectName(u"thumbs_exe_02")
        sizePolicy1.setHeightForWidth(self.thumbs_exe_02.sizePolicy().hasHeightForWidth())
        self.thumbs_exe_02.setSizePolicy(sizePolicy1)
        self.thumbs_exe_02.setMinimumSize(QSize(100, 25))
        self.thumbs_exe_02.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_164.addWidget(self.thumbs_exe_02)

        self.label_282 = QLabel(self.tab_18)
        self.label_282.setObjectName(u"label_282")
        sizePolicy2.setHeightForWidth(self.label_282.sizePolicy().hasHeightForWidth())
        self.label_282.setSizePolicy(sizePolicy2)
        self.label_282.setMinimumSize(QSize(75, 25))

        self.horizontalLayout_164.addWidget(self.label_282)

        self.thumbs_args_02 = QLineEdit(self.tab_18)
        self.thumbs_args_02.setObjectName(u"thumbs_args_02")
        sizePolicy1.setHeightForWidth(self.thumbs_args_02.sizePolicy().hasHeightForWidth())
        self.thumbs_args_02.setSizePolicy(sizePolicy1)
        self.thumbs_args_02.setMinimumSize(QSize(150, 25))
        self.thumbs_args_02.setMaximumSize(QSize(4096, 16777215))

        self.horizontalLayout_164.addWidget(self.thumbs_args_02)

        self.label_283 = QLabel(self.tab_18)
        self.label_283.setObjectName(u"label_283")
        sizePolicy2.setHeightForWidth(self.label_283.sizePolicy().hasHeightForWidth())
        self.label_283.setSizePolicy(sizePolicy2)
        self.label_283.setMinimumSize(QSize(75, 25))

        self.horizontalLayout_164.addWidget(self.label_283)

        self.thumbs_name_02 = QLineEdit(self.tab_18)
        self.thumbs_name_02.setObjectName(u"thumbs_name_02")
        sizePolicy1.setHeightForWidth(self.thumbs_name_02.sizePolicy().hasHeightForWidth())
        self.thumbs_name_02.setSizePolicy(sizePolicy1)
        self.thumbs_name_02.setMinimumSize(QSize(100, 25))
        self.thumbs_name_02.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_164.addWidget(self.thumbs_name_02)


        self.verticalLayout_3.addLayout(self.horizontalLayout_164)

        self.horizontalLayout_165 = QHBoxLayout()
        self.horizontalLayout_165.setObjectName(u"horizontalLayout_165")
        self.label_284 = QLabel(self.tab_18)
        self.label_284.setObjectName(u"label_284")
        sizePolicy2.setHeightForWidth(self.label_284.sizePolicy().hasHeightForWidth())
        self.label_284.setSizePolicy(sizePolicy2)
        self.label_284.setMinimumSize(QSize(25, 25))
        self.label_284.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_165.addWidget(self.label_284)

        self.thumbs_if_03 = QLineEdit(self.tab_18)
        self.thumbs_if_03.setObjectName(u"thumbs_if_03")
        sizePolicy1.setHeightForWidth(self.thumbs_if_03.sizePolicy().hasHeightForWidth())
        self.thumbs_if_03.setSizePolicy(sizePolicy1)
        self.thumbs_if_03.setMinimumSize(QSize(75, 25))
        self.thumbs_if_03.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_165.addWidget(self.thumbs_if_03)

        self.label_285 = QLabel(self.tab_18)
        self.label_285.setObjectName(u"label_285")
        sizePolicy2.setHeightForWidth(self.label_285.sizePolicy().hasHeightForWidth())
        self.label_285.setSizePolicy(sizePolicy2)
        self.label_285.setMinimumSize(QSize(75, 25))

        self.horizontalLayout_165.addWidget(self.label_285)

        self.thumbs_exe_03 = QLineEdit(self.tab_18)
        self.thumbs_exe_03.setObjectName(u"thumbs_exe_03")
        sizePolicy1.setHeightForWidth(self.thumbs_exe_03.sizePolicy().hasHeightForWidth())
        self.thumbs_exe_03.setSizePolicy(sizePolicy1)
        self.thumbs_exe_03.setMinimumSize(QSize(100, 25))
        self.thumbs_exe_03.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_165.addWidget(self.thumbs_exe_03)

        self.label_286 = QLabel(self.tab_18)
        self.label_286.setObjectName(u"label_286")
        sizePolicy2.setHeightForWidth(self.label_286.sizePolicy().hasHeightForWidth())
        self.label_286.setSizePolicy(sizePolicy2)
        self.label_286.setMinimumSize(QSize(75, 25))

        self.horizontalLayout_165.addWidget(self.label_286)

        self.thumbs_args_03 = QLineEdit(self.tab_18)
        self.thumbs_args_03.setObjectName(u"thumbs_args_03")
        sizePolicy1.setHeightForWidth(self.thumbs_args_03.sizePolicy().hasHeightForWidth())
        self.thumbs_args_03.setSizePolicy(sizePolicy1)
        self.thumbs_args_03.setMinimumSize(QSize(150, 25))
        self.thumbs_args_03.setMaximumSize(QSize(4096, 16777215))

        self.horizontalLayout_165.addWidget(self.thumbs_args_03)

        self.label_287 = QLabel(self.tab_18)
        self.label_287.setObjectName(u"label_287")
        sizePolicy2.setHeightForWidth(self.label_287.sizePolicy().hasHeightForWidth())
        self.label_287.setSizePolicy(sizePolicy2)
        self.label_287.setMinimumSize(QSize(75, 25))

        self.horizontalLayout_165.addWidget(self.label_287)

        self.thumbs_name_03 = QLineEdit(self.tab_18)
        self.thumbs_name_03.setObjectName(u"thumbs_name_03")
        sizePolicy1.setHeightForWidth(self.thumbs_name_03.sizePolicy().hasHeightForWidth())
        self.thumbs_name_03.setSizePolicy(sizePolicy1)
        self.thumbs_name_03.setMinimumSize(QSize(100, 25))
        self.thumbs_name_03.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_165.addWidget(self.thumbs_name_03)


        self.verticalLayout_3.addLayout(self.horizontalLayout_165)

        self.horizontalLayout_166 = QHBoxLayout()
        self.horizontalLayout_166.setObjectName(u"horizontalLayout_166")
        self.label_288 = QLabel(self.tab_18)
        self.label_288.setObjectName(u"label_288")
        sizePolicy2.setHeightForWidth(self.label_288.sizePolicy().hasHeightForWidth())
        self.label_288.setSizePolicy(sizePolicy2)
        self.label_288.setMinimumSize(QSize(25, 25))
        self.label_288.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_166.addWidget(self.label_288)

        self.thumbs_if_04 = QLineEdit(self.tab_18)
        self.thumbs_if_04.setObjectName(u"thumbs_if_04")
        sizePolicy1.setHeightForWidth(self.thumbs_if_04.sizePolicy().hasHeightForWidth())
        self.thumbs_if_04.setSizePolicy(sizePolicy1)
        self.thumbs_if_04.setMinimumSize(QSize(75, 25))
        self.thumbs_if_04.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_166.addWidget(self.thumbs_if_04)

        self.label_289 = QLabel(self.tab_18)
        self.label_289.setObjectName(u"label_289")
        sizePolicy2.setHeightForWidth(self.label_289.sizePolicy().hasHeightForWidth())
        self.label_289.setSizePolicy(sizePolicy2)
        self.label_289.setMinimumSize(QSize(75, 25))

        self.horizontalLayout_166.addWidget(self.label_289)

        self.thumbs_exe_04 = QLineEdit(self.tab_18)
        self.thumbs_exe_04.setObjectName(u"thumbs_exe_04")
        sizePolicy1.setHeightForWidth(self.thumbs_exe_04.sizePolicy().hasHeightForWidth())
        self.thumbs_exe_04.setSizePolicy(sizePolicy1)
        self.thumbs_exe_04.setMinimumSize(QSize(100, 25))
        self.thumbs_exe_04.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_166.addWidget(self.thumbs_exe_04)

        self.label_290 = QLabel(self.tab_18)
        self.label_290.setObjectName(u"label_290")
        sizePolicy2.setHeightForWidth(self.label_290.sizePolicy().hasHeightForWidth())
        self.label_290.setSizePolicy(sizePolicy2)
        self.label_290.setMinimumSize(QSize(75, 25))

        self.horizontalLayout_166.addWidget(self.label_290)

        self.thumbs_args_04 = QLineEdit(self.tab_18)
        self.thumbs_args_04.setObjectName(u"thumbs_args_04")
        sizePolicy1.setHeightForWidth(self.thumbs_args_04.sizePolicy().hasHeightForWidth())
        self.thumbs_args_04.setSizePolicy(sizePolicy1)
        self.thumbs_args_04.setMinimumSize(QSize(150, 25))
        self.thumbs_args_04.setMaximumSize(QSize(4096, 16777215))

        self.horizontalLayout_166.addWidget(self.thumbs_args_04)

        self.label_291 = QLabel(self.tab_18)
        self.label_291.setObjectName(u"label_291")
        sizePolicy2.setHeightForWidth(self.label_291.sizePolicy().hasHeightForWidth())
        self.label_291.setSizePolicy(sizePolicy2)
        self.label_291.setMinimumSize(QSize(75, 25))

        self.horizontalLayout_166.addWidget(self.label_291)

        self.thumbs_name_04 = QLineEdit(self.tab_18)
        self.thumbs_name_04.setObjectName(u"thumbs_name_04")
        sizePolicy1.setHeightForWidth(self.thumbs_name_04.sizePolicy().hasHeightForWidth())
        self.thumbs_name_04.setSizePolicy(sizePolicy1)
        self.thumbs_name_04.setMinimumSize(QSize(100, 25))
        self.thumbs_name_04.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_166.addWidget(self.thumbs_name_04)


        self.verticalLayout_3.addLayout(self.horizontalLayout_166)

        self.horizontalLayout_167 = QHBoxLayout()
        self.horizontalLayout_167.setObjectName(u"horizontalLayout_167")
        self.label_292 = QLabel(self.tab_18)
        self.label_292.setObjectName(u"label_292")
        sizePolicy2.setHeightForWidth(self.label_292.sizePolicy().hasHeightForWidth())
        self.label_292.setSizePolicy(sizePolicy2)
        self.label_292.setMinimumSize(QSize(25, 25))
        self.label_292.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_167.addWidget(self.label_292)

        self.thumbs_if_05 = QLineEdit(self.tab_18)
        self.thumbs_if_05.setObjectName(u"thumbs_if_05")
        sizePolicy1.setHeightForWidth(self.thumbs_if_05.sizePolicy().hasHeightForWidth())
        self.thumbs_if_05.setSizePolicy(sizePolicy1)
        self.thumbs_if_05.setMinimumSize(QSize(75, 25))
        self.thumbs_if_05.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_167.addWidget(self.thumbs_if_05)

        self.label_293 = QLabel(self.tab_18)
        self.label_293.setObjectName(u"label_293")
        sizePolicy2.setHeightForWidth(self.label_293.sizePolicy().hasHeightForWidth())
        self.label_293.setSizePolicy(sizePolicy2)
        self.label_293.setMinimumSize(QSize(75, 25))

        self.horizontalLayout_167.addWidget(self.label_293)

        self.thumbs_exe_05 = QLineEdit(self.tab_18)
        self.thumbs_exe_05.setObjectName(u"thumbs_exe_05")
        sizePolicy1.setHeightForWidth(self.thumbs_exe_05.sizePolicy().hasHeightForWidth())
        self.thumbs_exe_05.setSizePolicy(sizePolicy1)
        self.thumbs_exe_05.setMinimumSize(QSize(100, 25))
        self.thumbs_exe_05.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_167.addWidget(self.thumbs_exe_05)

        self.label_294 = QLabel(self.tab_18)
        self.label_294.setObjectName(u"label_294")
        sizePolicy2.setHeightForWidth(self.label_294.sizePolicy().hasHeightForWidth())
        self.label_294.setSizePolicy(sizePolicy2)
        self.label_294.setMinimumSize(QSize(75, 25))

        self.horizontalLayout_167.addWidget(self.label_294)

        self.thumbs_args_05 = QLineEdit(self.tab_18)
        self.thumbs_args_05.setObjectName(u"thumbs_args_05")
        sizePolicy1.setHeightForWidth(self.thumbs_args_05.sizePolicy().hasHeightForWidth())
        self.thumbs_args_05.setSizePolicy(sizePolicy1)
        self.thumbs_args_05.setMinimumSize(QSize(150, 25))
        self.thumbs_args_05.setMaximumSize(QSize(4096, 16777215))

        self.horizontalLayout_167.addWidget(self.thumbs_args_05)

        self.label_295 = QLabel(self.tab_18)
        self.label_295.setObjectName(u"label_295")
        sizePolicy2.setHeightForWidth(self.label_295.sizePolicy().hasHeightForWidth())
        self.label_295.setSizePolicy(sizePolicy2)
        self.label_295.setMinimumSize(QSize(75, 25))

        self.horizontalLayout_167.addWidget(self.label_295)

        self.thumbs_name_05 = QLineEdit(self.tab_18)
        self.thumbs_name_05.setObjectName(u"thumbs_name_05")
        sizePolicy1.setHeightForWidth(self.thumbs_name_05.sizePolicy().hasHeightForWidth())
        self.thumbs_name_05.setSizePolicy(sizePolicy1)
        self.thumbs_name_05.setMinimumSize(QSize(100, 25))
        self.thumbs_name_05.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_167.addWidget(self.thumbs_name_05)


        self.verticalLayout_3.addLayout(self.horizontalLayout_167)

        self.horizontalLayout_168 = QHBoxLayout()
        self.horizontalLayout_168.setObjectName(u"horizontalLayout_168")
        self.label_296 = QLabel(self.tab_18)
        self.label_296.setObjectName(u"label_296")
        sizePolicy2.setHeightForWidth(self.label_296.sizePolicy().hasHeightForWidth())
        self.label_296.setSizePolicy(sizePolicy2)
        self.label_296.setMinimumSize(QSize(25, 25))
        self.label_296.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_168.addWidget(self.label_296)

        self.thumbs_if_06 = QLineEdit(self.tab_18)
        self.thumbs_if_06.setObjectName(u"thumbs_if_06")
        sizePolicy1.setHeightForWidth(self.thumbs_if_06.sizePolicy().hasHeightForWidth())
        self.thumbs_if_06.setSizePolicy(sizePolicy1)
        self.thumbs_if_06.setMinimumSize(QSize(75, 25))
        self.thumbs_if_06.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_168.addWidget(self.thumbs_if_06)

        self.label_297 = QLabel(self.tab_18)
        self.label_297.setObjectName(u"label_297")
        sizePolicy2.setHeightForWidth(self.label_297.sizePolicy().hasHeightForWidth())
        self.label_297.setSizePolicy(sizePolicy2)
        self.label_297.setMinimumSize(QSize(75, 25))

        self.horizontalLayout_168.addWidget(self.label_297)

        self.thumbs_exe_06 = QLineEdit(self.tab_18)
        self.thumbs_exe_06.setObjectName(u"thumbs_exe_06")
        sizePolicy1.setHeightForWidth(self.thumbs_exe_06.sizePolicy().hasHeightForWidth())
        self.thumbs_exe_06.setSizePolicy(sizePolicy1)
        self.thumbs_exe_06.setMinimumSize(QSize(100, 25))
        self.thumbs_exe_06.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_168.addWidget(self.thumbs_exe_06)

        self.label_298 = QLabel(self.tab_18)
        self.label_298.setObjectName(u"label_298")
        sizePolicy2.setHeightForWidth(self.label_298.sizePolicy().hasHeightForWidth())
        self.label_298.setSizePolicy(sizePolicy2)
        self.label_298.setMinimumSize(QSize(75, 25))

        self.horizontalLayout_168.addWidget(self.label_298)

        self.thumbs_args_06 = QLineEdit(self.tab_18)
        self.thumbs_args_06.setObjectName(u"thumbs_args_06")
        sizePolicy1.setHeightForWidth(self.thumbs_args_06.sizePolicy().hasHeightForWidth())
        self.thumbs_args_06.setSizePolicy(sizePolicy1)
        self.thumbs_args_06.setMinimumSize(QSize(150, 25))
        self.thumbs_args_06.setMaximumSize(QSize(4096, 16777215))

        self.horizontalLayout_168.addWidget(self.thumbs_args_06)

        self.label_299 = QLabel(self.tab_18)
        self.label_299.setObjectName(u"label_299")
        sizePolicy2.setHeightForWidth(self.label_299.sizePolicy().hasHeightForWidth())
        self.label_299.setSizePolicy(sizePolicy2)
        self.label_299.setMinimumSize(QSize(75, 25))

        self.horizontalLayout_168.addWidget(self.label_299)

        self.thumbs_name_06 = QLineEdit(self.tab_18)
        self.thumbs_name_06.setObjectName(u"thumbs_name_06")
        sizePolicy1.setHeightForWidth(self.thumbs_name_06.sizePolicy().hasHeightForWidth())
        self.thumbs_name_06.setSizePolicy(sizePolicy1)
        self.thumbs_name_06.setMinimumSize(QSize(100, 25))
        self.thumbs_name_06.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_168.addWidget(self.thumbs_name_06)


        self.verticalLayout_3.addLayout(self.horizontalLayout_168)

        self.horizontalLayout_169 = QHBoxLayout()
        self.horizontalLayout_169.setObjectName(u"horizontalLayout_169")
        self.label_300 = QLabel(self.tab_18)
        self.label_300.setObjectName(u"label_300")
        sizePolicy2.setHeightForWidth(self.label_300.sizePolicy().hasHeightForWidth())
        self.label_300.setSizePolicy(sizePolicy2)
        self.label_300.setMinimumSize(QSize(25, 25))
        self.label_300.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_169.addWidget(self.label_300)

        self.thumbs_if_07 = QLineEdit(self.tab_18)
        self.thumbs_if_07.setObjectName(u"thumbs_if_07")
        sizePolicy1.setHeightForWidth(self.thumbs_if_07.sizePolicy().hasHeightForWidth())
        self.thumbs_if_07.setSizePolicy(sizePolicy1)
        self.thumbs_if_07.setMinimumSize(QSize(75, 25))
        self.thumbs_if_07.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_169.addWidget(self.thumbs_if_07)

        self.label_301 = QLabel(self.tab_18)
        self.label_301.setObjectName(u"label_301")
        sizePolicy2.setHeightForWidth(self.label_301.sizePolicy().hasHeightForWidth())
        self.label_301.setSizePolicy(sizePolicy2)
        self.label_301.setMinimumSize(QSize(75, 25))

        self.horizontalLayout_169.addWidget(self.label_301)

        self.thumbs_exe_07 = QLineEdit(self.tab_18)
        self.thumbs_exe_07.setObjectName(u"thumbs_exe_07")
        sizePolicy1.setHeightForWidth(self.thumbs_exe_07.sizePolicy().hasHeightForWidth())
        self.thumbs_exe_07.setSizePolicy(sizePolicy1)
        self.thumbs_exe_07.setMinimumSize(QSize(100, 25))
        self.thumbs_exe_07.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_169.addWidget(self.thumbs_exe_07)

        self.label_302 = QLabel(self.tab_18)
        self.label_302.setObjectName(u"label_302")
        sizePolicy2.setHeightForWidth(self.label_302.sizePolicy().hasHeightForWidth())
        self.label_302.setSizePolicy(sizePolicy2)
        self.label_302.setMinimumSize(QSize(75, 25))

        self.horizontalLayout_169.addWidget(self.label_302)

        self.thumbs_args_07 = QLineEdit(self.tab_18)
        self.thumbs_args_07.setObjectName(u"thumbs_args_07")
        sizePolicy1.setHeightForWidth(self.thumbs_args_07.sizePolicy().hasHeightForWidth())
        self.thumbs_args_07.setSizePolicy(sizePolicy1)
        self.thumbs_args_07.setMinimumSize(QSize(150, 25))
        self.thumbs_args_07.setMaximumSize(QSize(4096, 16777215))

        self.horizontalLayout_169.addWidget(self.thumbs_args_07)

        self.label_303 = QLabel(self.tab_18)
        self.label_303.setObjectName(u"label_303")
        sizePolicy2.setHeightForWidth(self.label_303.sizePolicy().hasHeightForWidth())
        self.label_303.setSizePolicy(sizePolicy2)
        self.label_303.setMinimumSize(QSize(75, 25))

        self.horizontalLayout_169.addWidget(self.label_303)

        self.thumbs_name_07 = QLineEdit(self.tab_18)
        self.thumbs_name_07.setObjectName(u"thumbs_name_07")
        sizePolicy1.setHeightForWidth(self.thumbs_name_07.sizePolicy().hasHeightForWidth())
        self.thumbs_name_07.setSizePolicy(sizePolicy1)
        self.thumbs_name_07.setMinimumSize(QSize(100, 25))
        self.thumbs_name_07.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_169.addWidget(self.thumbs_name_07)


        self.verticalLayout_3.addLayout(self.horizontalLayout_169)

        self.horizontalLayout_170 = QHBoxLayout()
        self.horizontalLayout_170.setObjectName(u"horizontalLayout_170")
        self.label_304 = QLabel(self.tab_18)
        self.label_304.setObjectName(u"label_304")
        sizePolicy2.setHeightForWidth(self.label_304.sizePolicy().hasHeightForWidth())
        self.label_304.setSizePolicy(sizePolicy2)
        self.label_304.setMinimumSize(QSize(25, 25))
        self.label_304.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_170.addWidget(self.label_304)

        self.thumbs_if_08 = QLineEdit(self.tab_18)
        self.thumbs_if_08.setObjectName(u"thumbs_if_08")
        sizePolicy1.setHeightForWidth(self.thumbs_if_08.sizePolicy().hasHeightForWidth())
        self.thumbs_if_08.setSizePolicy(sizePolicy1)
        self.thumbs_if_08.setMinimumSize(QSize(75, 25))
        self.thumbs_if_08.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_170.addWidget(self.thumbs_if_08)

        self.label_305 = QLabel(self.tab_18)
        self.label_305.setObjectName(u"label_305")
        sizePolicy2.setHeightForWidth(self.label_305.sizePolicy().hasHeightForWidth())
        self.label_305.setSizePolicy(sizePolicy2)
        self.label_305.setMinimumSize(QSize(75, 25))

        self.horizontalLayout_170.addWidget(self.label_305)

        self.thumbs_exe_08 = QLineEdit(self.tab_18)
        self.thumbs_exe_08.setObjectName(u"thumbs_exe_08")
        sizePolicy1.setHeightForWidth(self.thumbs_exe_08.sizePolicy().hasHeightForWidth())
        self.thumbs_exe_08.setSizePolicy(sizePolicy1)
        self.thumbs_exe_08.setMinimumSize(QSize(100, 25))
        self.thumbs_exe_08.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_170.addWidget(self.thumbs_exe_08)

        self.label_306 = QLabel(self.tab_18)
        self.label_306.setObjectName(u"label_306")
        sizePolicy2.setHeightForWidth(self.label_306.sizePolicy().hasHeightForWidth())
        self.label_306.setSizePolicy(sizePolicy2)
        self.label_306.setMinimumSize(QSize(75, 25))

        self.horizontalLayout_170.addWidget(self.label_306)

        self.thumbs_args_08 = QLineEdit(self.tab_18)
        self.thumbs_args_08.setObjectName(u"thumbs_args_08")
        sizePolicy1.setHeightForWidth(self.thumbs_args_08.sizePolicy().hasHeightForWidth())
        self.thumbs_args_08.setSizePolicy(sizePolicy1)
        self.thumbs_args_08.setMinimumSize(QSize(150, 25))
        self.thumbs_args_08.setMaximumSize(QSize(4096, 16777215))

        self.horizontalLayout_170.addWidget(self.thumbs_args_08)

        self.label_307 = QLabel(self.tab_18)
        self.label_307.setObjectName(u"label_307")
        sizePolicy2.setHeightForWidth(self.label_307.sizePolicy().hasHeightForWidth())
        self.label_307.setSizePolicy(sizePolicy2)
        self.label_307.setMinimumSize(QSize(75, 25))

        self.horizontalLayout_170.addWidget(self.label_307)

        self.thumbs_name_08 = QLineEdit(self.tab_18)
        self.thumbs_name_08.setObjectName(u"thumbs_name_08")
        sizePolicy1.setHeightForWidth(self.thumbs_name_08.sizePolicy().hasHeightForWidth())
        self.thumbs_name_08.setSizePolicy(sizePolicy1)
        self.thumbs_name_08.setMinimumSize(QSize(100, 25))
        self.thumbs_name_08.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_170.addWidget(self.thumbs_name_08)


        self.verticalLayout_3.addLayout(self.horizontalLayout_170)


        self.verticalLayout_34.addLayout(self.verticalLayout_3)


        self.verticalLayout_35.addLayout(self.verticalLayout_34)

        self.TopTab.addTab(self.tab_18, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout_63 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.scrollArea_2 = QScrollArea(self.tab_2)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        sizePolicy3.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy3)
        self.scrollArea_2.setMaximumSize(QSize(16777215, 16000))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 1201, 289))
        sizePolicy10 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.scrollAreaWidgetContents_3.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_3.setSizePolicy(sizePolicy10)
        self.horizontalLayout_69 = QHBoxLayout(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setMinimumSize(QSize(100, 20))
        self.label_3.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_4.addWidget(self.label_3)

        self.sub_columns = QPlainTextEdit(self.scrollAreaWidgetContents_3)
        self.sub_columns.setObjectName(u"sub_columns")
        sizePolicy9.setHeightForWidth(self.sub_columns.sizePolicy().hasHeightForWidth())
        self.sub_columns.setSizePolicy(sizePolicy9)
        self.sub_columns.setMinimumSize(QSize(150, 100))
        self.sub_columns.setMaximumSize(QSize(16777215, 300))

        self.verticalLayout_4.addWidget(self.sub_columns)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_7.setObjectName(u"label_7")
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)
        self.label_7.setMinimumSize(QSize(80, 25))
        self.label_7.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_7.addWidget(self.label_7)

        self.sub_exclude = QLineEdit(self.scrollAreaWidgetContents_3)
        self.sub_exclude.setObjectName(u"sub_exclude")
        sizePolicy1.setHeightForWidth(self.sub_exclude.sizePolicy().hasHeightForWidth())
        self.sub_exclude.setSizePolicy(sizePolicy1)
        self.sub_exclude.setMinimumSize(QSize(80, 25))

        self.horizontalLayout_7.addWidget(self.sub_exclude)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_8 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_8.setObjectName(u"label_8")
        sizePolicy2.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy2)
        self.label_8.setMinimumSize(QSize(80, 25))
        self.label_8.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_10.addWidget(self.label_8)

        self.sub_include = QLineEdit(self.scrollAreaWidgetContents_3)
        self.sub_include.setObjectName(u"sub_include")
        sizePolicy1.setHeightForWidth(self.sub_include.sizePolicy().hasHeightForWidth())
        self.sub_include.setSizePolicy(sizePolicy1)
        self.sub_include.setMinimumSize(QSize(80, 25))

        self.horizontalLayout_10.addWidget(self.sub_include)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)


        self.verticalLayout_6.addLayout(self.verticalLayout_2)


        self.horizontalLayout_15.addLayout(self.verticalLayout_6)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_4 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)
        self.label_4.setMinimumSize(QSize(100, 20))
        self.label_4.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_22.addWidget(self.label_4)

        self.log_columns = QPlainTextEdit(self.scrollAreaWidgetContents_3)
        self.log_columns.setObjectName(u"log_columns")
        sizePolicy9.setHeightForWidth(self.log_columns.sizePolicy().hasHeightForWidth())
        self.log_columns.setSizePolicy(sizePolicy9)
        self.log_columns.setMinimumSize(QSize(150, 100))
        self.log_columns.setMaximumSize(QSize(16777215, 300))

        self.verticalLayout_22.addWidget(self.log_columns)


        self.verticalLayout_21.addLayout(self.verticalLayout_22)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_9 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_9.setObjectName(u"label_9")
        sizePolicy2.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy2)
        self.label_9.setMinimumSize(QSize(80, 25))
        self.label_9.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_11.addWidget(self.label_9)

        self.log_exclude = QLineEdit(self.scrollAreaWidgetContents_3)
        self.log_exclude.setObjectName(u"log_exclude")
        sizePolicy1.setHeightForWidth(self.log_exclude.sizePolicy().hasHeightForWidth())
        self.log_exclude.setSizePolicy(sizePolicy1)
        self.log_exclude.setMinimumSize(QSize(80, 25))

        self.horizontalLayout_11.addWidget(self.log_exclude)


        self.verticalLayout_23.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_11 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_11.setObjectName(u"label_11")
        sizePolicy2.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy2)
        self.label_11.setMinimumSize(QSize(80, 25))
        self.label_11.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_12.addWidget(self.label_11)

        self.log_include = QLineEdit(self.scrollAreaWidgetContents_3)
        self.log_include.setObjectName(u"log_include")
        sizePolicy1.setHeightForWidth(self.log_include.sizePolicy().hasHeightForWidth())
        self.log_include.setSizePolicy(sizePolicy1)
        self.log_include.setMinimumSize(QSize(80, 25))

        self.horizontalLayout_12.addWidget(self.log_include)


        self.verticalLayout_23.addLayout(self.horizontalLayout_12)


        self.verticalLayout_21.addLayout(self.verticalLayout_23)


        self.horizontalLayout_15.addLayout(self.verticalLayout_21)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_6 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_6.setObjectName(u"label_6")
        sizePolicy2.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy2)
        self.label_6.setMinimumSize(QSize(100, 20))
        self.label_6.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_25.addWidget(self.label_6)

        self.txt_columns = QPlainTextEdit(self.scrollAreaWidgetContents_3)
        self.txt_columns.setObjectName(u"txt_columns")
        sizePolicy9.setHeightForWidth(self.txt_columns.sizePolicy().hasHeightForWidth())
        self.txt_columns.setSizePolicy(sizePolicy9)
        self.txt_columns.setMinimumSize(QSize(150, 100))
        self.txt_columns.setMaximumSize(QSize(16777215, 300))

        self.verticalLayout_25.addWidget(self.txt_columns)


        self.verticalLayout_24.addLayout(self.verticalLayout_25)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_12 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_12.setObjectName(u"label_12")
        sizePolicy2.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy2)
        self.label_12.setMinimumSize(QSize(80, 25))
        self.label_12.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_13.addWidget(self.label_12)

        self.txt_exclude = QLineEdit(self.scrollAreaWidgetContents_3)
        self.txt_exclude.setObjectName(u"txt_exclude")
        sizePolicy1.setHeightForWidth(self.txt_exclude.sizePolicy().hasHeightForWidth())
        self.txt_exclude.setSizePolicy(sizePolicy1)
        self.txt_exclude.setMinimumSize(QSize(80, 25))

        self.horizontalLayout_13.addWidget(self.txt_exclude)


        self.verticalLayout_26.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_13 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_13.setObjectName(u"label_13")
        sizePolicy2.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy2)
        self.label_13.setMinimumSize(QSize(80, 25))
        self.label_13.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_14.addWidget(self.label_13)

        self.txt_include = QLineEdit(self.scrollAreaWidgetContents_3)
        self.txt_include.setObjectName(u"txt_include")
        sizePolicy1.setHeightForWidth(self.txt_include.sizePolicy().hasHeightForWidth())
        self.txt_include.setSizePolicy(sizePolicy1)
        self.txt_include.setMinimumSize(QSize(80, 25))

        self.horizontalLayout_14.addWidget(self.txt_include)


        self.verticalLayout_26.addLayout(self.horizontalLayout_14)


        self.verticalLayout_24.addLayout(self.verticalLayout_26)


        self.horizontalLayout_15.addLayout(self.verticalLayout_24)


        self.horizontalLayout_69.addLayout(self.horizontalLayout_15)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_27.addWidget(self.scrollArea_2)


        self.horizontalLayout_63.addLayout(self.verticalLayout_27)

        self.TopTab.addTab(self.tab_2, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.horizontalLayout_32 = QHBoxLayout(self.tab_5)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.verticalLayout_49 = QVBoxLayout()
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.groupBox_5 = QGroupBox(self.tab_5)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy1.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy1)
        self.groupBox_5.setMinimumSize(QSize(180, 100))
        self.verticalLayout_16 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.text_txt = QCheckBox(self.groupBox_5)
        self.text_txt.setObjectName(u"text_txt")
        self.text_txt.setChecked(True)

        self.horizontalLayout_31.addWidget(self.text_txt)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_9)


        self.verticalLayout_19.addLayout(self.horizontalLayout_31)

        self.horizontalLayout_51 = QHBoxLayout()
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.text_root = QRadioButton(self.groupBox_5)
        self.text_root.setObjectName(u"text_root")
        self.text_root.setMinimumSize(QSize(61, 0))
        self.text_root.setChecked(True)

        self.horizontalLayout_51.addWidget(self.text_root)

        self.text_above = QRadioButton(self.groupBox_5)
        self.text_above.setObjectName(u"text_above")
        self.text_above.setMinimumSize(QSize(161, 0))

        self.horizontalLayout_51.addWidget(self.text_above)

        self.text_custom = QRadioButton(self.groupBox_5)
        self.text_custom.setObjectName(u"text_custom")
        self.text_custom.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_51.addWidget(self.text_custom)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_51.addItem(self.horizontalSpacer_22)


        self.verticalLayout_19.addLayout(self.horizontalLayout_51)

        self.horizontalLayout_52 = QHBoxLayout()
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.label_17 = QLabel(self.groupBox_5)
        self.label_17.setObjectName(u"label_17")
        sizePolicy2.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy2)

        self.horizontalLayout_52.addWidget(self.label_17)

        self.text_custom_path = QLineEdit(self.groupBox_5)
        self.text_custom_path.setObjectName(u"text_custom_path")
        sizePolicy1.setHeightForWidth(self.text_custom_path.sizePolicy().hasHeightForWidth())
        self.text_custom_path.setSizePolicy(sizePolicy1)
        self.text_custom_path.setMinimumSize(QSize(300, 25))

        self.horizontalLayout_52.addWidget(self.text_custom_path)


        self.verticalLayout_19.addLayout(self.horizontalLayout_52)


        self.verticalLayout_16.addLayout(self.verticalLayout_19)


        self.verticalLayout_49.addWidget(self.groupBox_5)

        self.groupBox_6 = QGroupBox(self.tab_5)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_20 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.text_add_titles = QCheckBox(self.groupBox_6)
        self.text_add_titles.setObjectName(u"text_add_titles")
        self.text_add_titles.setChecked(False)

        self.horizontalLayout_21.addWidget(self.text_add_titles)

        self.horizontalSpacer_3 = QSpacerItem(100, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.text_sep_tab = QRadioButton(self.groupBox_6)
        self.text_sep_tab.setObjectName(u"text_sep_tab")
        self.text_sep_tab.setChecked(True)

        self.horizontalLayout_20.addWidget(self.text_sep_tab)

        self.text_sep_fixed = QRadioButton(self.groupBox_6)
        self.text_sep_fixed.setObjectName(u"text_sep_fixed")

        self.horizontalLayout_20.addWidget(self.text_sep_fixed)


        self.horizontalLayout_21.addLayout(self.horizontalLayout_20)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_4)


        self.verticalLayout_20.addLayout(self.horizontalLayout_21)


        self.verticalLayout_49.addWidget(self.groupBox_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_52 = QLabel(self.tab_5)
        self.label_52.setObjectName(u"label_52")
        sizePolicy2.setHeightForWidth(self.label_52.sizePolicy().hasHeightForWidth())
        self.label_52.setSizePolicy(sizePolicy2)

        self.verticalLayout_29.addWidget(self.label_52)

        self.text_header = QPlainTextEdit(self.tab_5)
        self.text_header.setObjectName(u"text_header")
        sizePolicy9.setHeightForWidth(self.text_header.sizePolicy().hasHeightForWidth())
        self.text_header.setSizePolicy(sizePolicy9)
        self.text_header.setMinimumSize(QSize(200, 50))

        self.verticalLayout_29.addWidget(self.text_header)


        self.horizontalLayout_8.addLayout(self.verticalLayout_29)

        self.verticalLayout_45 = QVBoxLayout()
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.label_75 = QLabel(self.tab_5)
        self.label_75.setObjectName(u"label_75")
        sizePolicy2.setHeightForWidth(self.label_75.sizePolicy().hasHeightForWidth())
        self.label_75.setSizePolicy(sizePolicy2)

        self.verticalLayout_45.addWidget(self.label_75)

        self.text_footer = QPlainTextEdit(self.tab_5)
        self.text_footer.setObjectName(u"text_footer")
        sizePolicy9.setHeightForWidth(self.text_footer.sizePolicy().hasHeightForWidth())
        self.text_footer.setSizePolicy(sizePolicy9)
        self.text_footer.setMinimumSize(QSize(200, 50))

        self.verticalLayout_45.addWidget(self.text_footer)


        self.horizontalLayout_8.addLayout(self.verticalLayout_45)


        self.verticalLayout_49.addLayout(self.horizontalLayout_8)


        self.horizontalLayout_32.addLayout(self.verticalLayout_49)

        self.TopTab.addTab(self.tab_5, "")
        self.tab_12 = QWidget()
        self.tab_12.setObjectName(u"tab_12")
        self.verticalLayout_68 = QVBoxLayout(self.tab_12)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.verticalLayout_67 = QVBoxLayout()
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.horizontalLayout_59 = QHBoxLayout()
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.check_sequence_size_consistency = QCheckBox(self.tab_12)
        self.check_sequence_size_consistency.setObjectName(u"check_sequence_size_consistency")
        self.check_sequence_size_consistency.setMinimumSize(QSize(220, 25))

        self.horizontalLayout_59.addWidget(self.check_sequence_size_consistency)

        self.check_sequence_holes = QCheckBox(self.tab_12)
        self.check_sequence_holes.setObjectName(u"check_sequence_holes")
        self.check_sequence_holes.setMinimumSize(QSize(220, 25))

        self.horizontalLayout_59.addWidget(self.check_sequence_holes)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_59.addItem(self.horizontalSpacer)


        self.verticalLayout_67.addLayout(self.horizontalLayout_59)

        self.scrollArea_3 = QScrollArea(self.tab_12)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setMinimumSize(QSize(0, 200))
        self.scrollArea_3.setMaximumSize(QSize(16777215, 160000))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 1194, 2030))
        self.verticalLayout_48 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_63 = QVBoxLayout()
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.groupBox_ch01 = QGroupBox(self.scrollAreaWidgetContents_4)
        self.groupBox_ch01.setObjectName(u"groupBox_ch01")
        sizePolicy1.setHeightForWidth(self.groupBox_ch01.sizePolicy().hasHeightForWidth())
        self.groupBox_ch01.setSizePolicy(sizePolicy1)
        self.groupBox_ch01.setMinimumSize(QSize(600, 90))
        self.groupBox_ch01.setMaximumSize(QSize(16777215, 90))
        self.horizontalLayout_263 = QHBoxLayout(self.groupBox_ch01)
        self.horizontalLayout_263.setObjectName(u"horizontalLayout_263")
        self.verticalLayout_82 = QVBoxLayout()
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.horizontalLayout_264 = QHBoxLayout()
        self.horizontalLayout_264.setObjectName(u"horizontalLayout_264")
        self.horizontalLayout_265 = QHBoxLayout()
        self.horizontalLayout_265.setObjectName(u"horizontalLayout_265")
        self.label_357 = QLabel(self.groupBox_ch01)
        self.label_357.setObjectName(u"label_357")
        sizePolicy2.setHeightForWidth(self.label_357.sizePolicy().hasHeightForWidth())
        self.label_357.setSizePolicy(sizePolicy2)
        self.label_357.setMinimumSize(QSize(15, 25))

        self.horizontalLayout_265.addWidget(self.label_357)

        self.check_if_01 = QLineEdit(self.groupBox_ch01)
        self.check_if_01.setObjectName(u"check_if_01")
        sizePolicy1.setHeightForWidth(self.check_if_01.sizePolicy().hasHeightForWidth())
        self.check_if_01.setSizePolicy(sizePolicy1)
        self.check_if_01.setMinimumSize(QSize(160, 25))

        self.horizontalLayout_265.addWidget(self.check_if_01)


        self.horizontalLayout_264.addLayout(self.horizontalLayout_265)

        self.horizontalLayout_266 = QHBoxLayout()
        self.horizontalLayout_266.setObjectName(u"horizontalLayout_266")
        self.label_358 = QLabel(self.groupBox_ch01)
        self.label_358.setObjectName(u"label_358")
        sizePolicy2.setHeightForWidth(self.label_358.sizePolicy().hasHeightForWidth())
        self.label_358.setSizePolicy(sizePolicy2)
        self.label_358.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_266.addWidget(self.label_358)

        self.check_check_01 = QLineEdit(self.groupBox_ch01)
        self.check_check_01.setObjectName(u"check_check_01")
        sizePolicy1.setHeightForWidth(self.check_check_01.sizePolicy().hasHeightForWidth())
        self.check_check_01.setSizePolicy(sizePolicy1)
        self.check_check_01.setMinimumSize(QSize(160, 25))

        self.horizontalLayout_266.addWidget(self.check_check_01)


        self.horizontalLayout_264.addLayout(self.horizontalLayout_266)


        self.verticalLayout_82.addLayout(self.horizontalLayout_264)

        self.horizontalLayout_267 = QHBoxLayout()
        self.horizontalLayout_267.setObjectName(u"horizontalLayout_267")
        self.horizontalLayout_268 = QHBoxLayout()
        self.horizontalLayout_268.setObjectName(u"horizontalLayout_268")
        self.label_359 = QLabel(self.groupBox_ch01)
        self.label_359.setObjectName(u"label_359")
        sizePolicy2.setHeightForWidth(self.label_359.sizePolicy().hasHeightForWidth())
        self.label_359.setSizePolicy(sizePolicy2)
        self.label_359.setMinimumSize(QSize(50, 25))
        self.label_359.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_268.addWidget(self.label_359)

        self.check_warning_01 = QRadioButton(self.groupBox_ch01)
        self.check_warning_01.setObjectName(u"check_warning_01")
        self.check_warning_01.setMinimumSize(QSize(100, 25))

        self.horizontalLayout_268.addWidget(self.check_warning_01)

        self.check_error_01 = QRadioButton(self.groupBox_ch01)
        self.check_error_01.setObjectName(u"check_error_01")
        self.check_error_01.setMinimumSize(QSize(100, 25))
        self.check_error_01.setChecked(True)

        self.horizontalLayout_268.addWidget(self.check_error_01)


        self.horizontalLayout_267.addLayout(self.horizontalLayout_268)

        self.check_message_01 = QLineEdit(self.groupBox_ch01)
        self.check_message_01.setObjectName(u"check_message_01")
        sizePolicy1.setHeightForWidth(self.check_message_01.sizePolicy().hasHeightForWidth())
        self.check_message_01.setSizePolicy(sizePolicy1)
        self.check_message_01.setMinimumSize(QSize(170, 25))

        self.horizontalLayout_267.addWidget(self.check_message_01)


        self.verticalLayout_82.addLayout(self.horizontalLayout_267)


        self.horizontalLayout_263.addLayout(self.verticalLayout_82)


        self.verticalLayout_63.addWidget(self.groupBox_ch01)

        self.groupBox_ch02 = QGroupBox(self.scrollAreaWidgetContents_4)
        self.groupBox_ch02.setObjectName(u"groupBox_ch02")
        sizePolicy1.setHeightForWidth(self.groupBox_ch02.sizePolicy().hasHeightForWidth())
        self.groupBox_ch02.setSizePolicy(sizePolicy1)
        self.groupBox_ch02.setMinimumSize(QSize(600, 90))
        self.groupBox_ch02.setMaximumSize(QSize(16777215, 90))
        self.horizontalLayout_269 = QHBoxLayout(self.groupBox_ch02)
        self.horizontalLayout_269.setObjectName(u"horizontalLayout_269")
        self.verticalLayout_83 = QVBoxLayout()
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.horizontalLayout_270 = QHBoxLayout()
        self.horizontalLayout_270.setObjectName(u"horizontalLayout_270")
        self.horizontalLayout_271 = QHBoxLayout()
        self.horizontalLayout_271.setObjectName(u"horizontalLayout_271")
        self.label_360 = QLabel(self.groupBox_ch02)
        self.label_360.setObjectName(u"label_360")
        sizePolicy2.setHeightForWidth(self.label_360.sizePolicy().hasHeightForWidth())
        self.label_360.setSizePolicy(sizePolicy2)
        self.label_360.setMinimumSize(QSize(15, 25))

        self.horizontalLayout_271.addWidget(self.label_360)

        self.check_if_02 = QLineEdit(self.groupBox_ch02)
        self.check_if_02.setObjectName(u"check_if_02")
        sizePolicy1.setHeightForWidth(self.check_if_02.sizePolicy().hasHeightForWidth())
        self.check_if_02.setSizePolicy(sizePolicy1)
        self.check_if_02.setMinimumSize(QSize(160, 25))

        self.horizontalLayout_271.addWidget(self.check_if_02)


        self.horizontalLayout_270.addLayout(self.horizontalLayout_271)

        self.horizontalLayout_272 = QHBoxLayout()
        self.horizontalLayout_272.setObjectName(u"horizontalLayout_272")
        self.label_361 = QLabel(self.groupBox_ch02)
        self.label_361.setObjectName(u"label_361")
        sizePolicy2.setHeightForWidth(self.label_361.sizePolicy().hasHeightForWidth())
        self.label_361.setSizePolicy(sizePolicy2)
        self.label_361.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_272.addWidget(self.label_361)

        self.check_check_02 = QLineEdit(self.groupBox_ch02)
        self.check_check_02.setObjectName(u"check_check_02")
        sizePolicy1.setHeightForWidth(self.check_check_02.sizePolicy().hasHeightForWidth())
        self.check_check_02.setSizePolicy(sizePolicy1)
        self.check_check_02.setMinimumSize(QSize(160, 25))

        self.horizontalLayout_272.addWidget(self.check_check_02)


        self.horizontalLayout_270.addLayout(self.horizontalLayout_272)


        self.verticalLayout_83.addLayout(self.horizontalLayout_270)

        self.horizontalLayout_273 = QHBoxLayout()
        self.horizontalLayout_273.setObjectName(u"horizontalLayout_273")
        self.horizontalLayout_274 = QHBoxLayout()
        self.horizontalLayout_274.setObjectName(u"horizontalLayout_274")
        self.label_362 = QLabel(self.groupBox_ch02)
        self.label_362.setObjectName(u"label_362")
        sizePolicy2.setHeightForWidth(self.label_362.sizePolicy().hasHeightForWidth())
        self.label_362.setSizePolicy(sizePolicy2)
        self.label_362.setMinimumSize(QSize(25, 25))
        self.label_362.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_274.addWidget(self.label_362)

        self.check_warning_02 = QRadioButton(self.groupBox_ch02)
        self.check_warning_02.setObjectName(u"check_warning_02")
        self.check_warning_02.setMinimumSize(QSize(100, 25))

        self.horizontalLayout_274.addWidget(self.check_warning_02)

        self.check_error_02 = QRadioButton(self.groupBox_ch02)
        self.check_error_02.setObjectName(u"check_error_02")
        self.check_error_02.setMinimumSize(QSize(100, 25))

        self.horizontalLayout_274.addWidget(self.check_error_02)


        self.horizontalLayout_273.addLayout(self.horizontalLayout_274)

        self.check_message_02 = QLineEdit(self.groupBox_ch02)
        self.check_message_02.setObjectName(u"check_message_02")
        sizePolicy1.setHeightForWidth(self.check_message_02.sizePolicy().hasHeightForWidth())
        self.check_message_02.setSizePolicy(sizePolicy1)
        self.check_message_02.setMinimumSize(QSize(170, 25))

        self.horizontalLayout_273.addWidget(self.check_message_02)


        self.verticalLayout_83.addLayout(self.horizontalLayout_273)


        self.horizontalLayout_269.addLayout(self.verticalLayout_83)


        self.verticalLayout_63.addWidget(self.groupBox_ch02)

        self.groupBox_ch03 = QGroupBox(self.scrollAreaWidgetContents_4)
        self.groupBox_ch03.setObjectName(u"groupBox_ch03")
        sizePolicy1.setHeightForWidth(self.groupBox_ch03.sizePolicy().hasHeightForWidth())
        self.groupBox_ch03.setSizePolicy(sizePolicy1)
        self.groupBox_ch03.setMinimumSize(QSize(600, 90))
        self.groupBox_ch03.setMaximumSize(QSize(16777215, 90))
        self.horizontalLayout_275 = QHBoxLayout(self.groupBox_ch03)
        self.horizontalLayout_275.setObjectName(u"horizontalLayout_275")
        self.verticalLayout_84 = QVBoxLayout()
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.horizontalLayout_276 = QHBoxLayout()
        self.horizontalLayout_276.setObjectName(u"horizontalLayout_276")
        self.horizontalLayout_277 = QHBoxLayout()
        self.horizontalLayout_277.setObjectName(u"horizontalLayout_277")
        self.label_363 = QLabel(self.groupBox_ch03)
        self.label_363.setObjectName(u"label_363")
        sizePolicy2.setHeightForWidth(self.label_363.sizePolicy().hasHeightForWidth())
        self.label_363.setSizePolicy(sizePolicy2)
        self.label_363.setMinimumSize(QSize(15, 25))

        self.horizontalLayout_277.addWidget(self.label_363)

        self.check_if_03 = QLineEdit(self.groupBox_ch03)
        self.check_if_03.setObjectName(u"check_if_03")
        sizePolicy1.setHeightForWidth(self.check_if_03.sizePolicy().hasHeightForWidth())
        self.check_if_03.setSizePolicy(sizePolicy1)
        self.check_if_03.setMinimumSize(QSize(160, 25))

        self.horizontalLayout_277.addWidget(self.check_if_03)


        self.horizontalLayout_276.addLayout(self.horizontalLayout_277)

        self.horizontalLayout_278 = QHBoxLayout()
        self.horizontalLayout_278.setObjectName(u"horizontalLayout_278")
        self.label_364 = QLabel(self.groupBox_ch03)
        self.label_364.setObjectName(u"label_364")
        sizePolicy2.setHeightForWidth(self.label_364.sizePolicy().hasHeightForWidth())
        self.label_364.setSizePolicy(sizePolicy2)
        self.label_364.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_278.addWidget(self.label_364)

        self.check_check_03 = QLineEdit(self.groupBox_ch03)
        self.check_check_03.setObjectName(u"check_check_03")
        sizePolicy1.setHeightForWidth(self.check_check_03.sizePolicy().hasHeightForWidth())
        self.check_check_03.setSizePolicy(sizePolicy1)
        self.check_check_03.setMinimumSize(QSize(160, 25))

        self.horizontalLayout_278.addWidget(self.check_check_03)


        self.horizontalLayout_276.addLayout(self.horizontalLayout_278)


        self.verticalLayout_84.addLayout(self.horizontalLayout_276)

        self.horizontalLayout_279 = QHBoxLayout()
        self.horizontalLayout_279.setObjectName(u"horizontalLayout_279")
        self.horizontalLayout_280 = QHBoxLayout()
        self.horizontalLayout_280.setObjectName(u"horizontalLayout_280")
        self.label_365 = QLabel(self.groupBox_ch03)
        self.label_365.setObjectName(u"label_365")
        sizePolicy2.setHeightForWidth(self.label_365.sizePolicy().hasHeightForWidth())
        self.label_365.setSizePolicy(sizePolicy2)
        self.label_365.setMinimumSize(QSize(25, 25))
        self.label_365.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_280.addWidget(self.label_365)

        self.check_warning_03 = QRadioButton(self.groupBox_ch03)
        self.check_warning_03.setObjectName(u"check_warning_03")
        self.check_warning_03.setMinimumSize(QSize(100, 25))

        self.horizontalLayout_280.addWidget(self.check_warning_03)

        self.check_error_03 = QRadioButton(self.groupBox_ch03)
        self.check_error_03.setObjectName(u"check_error_03")
        self.check_error_03.setMinimumSize(QSize(100, 25))
        self.check_error_03.setChecked(True)

        self.horizontalLayout_280.addWidget(self.check_error_03)


        self.horizontalLayout_279.addLayout(self.horizontalLayout_280)

        self.check_message_03 = QLineEdit(self.groupBox_ch03)
        self.check_message_03.setObjectName(u"check_message_03")
        sizePolicy1.setHeightForWidth(self.check_message_03.sizePolicy().hasHeightForWidth())
        self.check_message_03.setSizePolicy(sizePolicy1)
        self.check_message_03.setMinimumSize(QSize(170, 25))

        self.horizontalLayout_279.addWidget(self.check_message_03)


        self.verticalLayout_84.addLayout(self.horizontalLayout_279)


        self.horizontalLayout_275.addLayout(self.verticalLayout_84)


        self.verticalLayout_63.addWidget(self.groupBox_ch03)

        self.groupBox_ch04 = QGroupBox(self.scrollAreaWidgetContents_4)
        self.groupBox_ch04.setObjectName(u"groupBox_ch04")
        sizePolicy1.setHeightForWidth(self.groupBox_ch04.sizePolicy().hasHeightForWidth())
        self.groupBox_ch04.setSizePolicy(sizePolicy1)
        self.groupBox_ch04.setMinimumSize(QSize(600, 90))
        self.groupBox_ch04.setMaximumSize(QSize(16777215, 90))
        self.horizontalLayout_281 = QHBoxLayout(self.groupBox_ch04)
        self.horizontalLayout_281.setObjectName(u"horizontalLayout_281")
        self.verticalLayout_85 = QVBoxLayout()
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.horizontalLayout_282 = QHBoxLayout()
        self.horizontalLayout_282.setObjectName(u"horizontalLayout_282")
        self.horizontalLayout_283 = QHBoxLayout()
        self.horizontalLayout_283.setObjectName(u"horizontalLayout_283")
        self.label_366 = QLabel(self.groupBox_ch04)
        self.label_366.setObjectName(u"label_366")
        sizePolicy2.setHeightForWidth(self.label_366.sizePolicy().hasHeightForWidth())
        self.label_366.setSizePolicy(sizePolicy2)
        self.label_366.setMinimumSize(QSize(15, 25))

        self.horizontalLayout_283.addWidget(self.label_366)

        self.check_if_04 = QLineEdit(self.groupBox_ch04)
        self.check_if_04.setObjectName(u"check_if_04")
        sizePolicy1.setHeightForWidth(self.check_if_04.sizePolicy().hasHeightForWidth())
        self.check_if_04.setSizePolicy(sizePolicy1)
        self.check_if_04.setMinimumSize(QSize(160, 25))

        self.horizontalLayout_283.addWidget(self.check_if_04)


        self.horizontalLayout_282.addLayout(self.horizontalLayout_283)

        self.horizontalLayout_284 = QHBoxLayout()
        self.horizontalLayout_284.setObjectName(u"horizontalLayout_284")
        self.label_367 = QLabel(self.groupBox_ch04)
        self.label_367.setObjectName(u"label_367")
        sizePolicy2.setHeightForWidth(self.label_367.sizePolicy().hasHeightForWidth())
        self.label_367.setSizePolicy(sizePolicy2)
        self.label_367.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_284.addWidget(self.label_367)

        self.check_check_04 = QLineEdit(self.groupBox_ch04)
        self.check_check_04.setObjectName(u"check_check_04")
        sizePolicy1.setHeightForWidth(self.check_check_04.sizePolicy().hasHeightForWidth())
        self.check_check_04.setSizePolicy(sizePolicy1)
        self.check_check_04.setMinimumSize(QSize(160, 25))

        self.horizontalLayout_284.addWidget(self.check_check_04)


        self.horizontalLayout_282.addLayout(self.horizontalLayout_284)


        self.verticalLayout_85.addLayout(self.horizontalLayout_282)

        self.horizontalLayout_285 = QHBoxLayout()
        self.horizontalLayout_285.setObjectName(u"horizontalLayout_285")
        self.horizontalLayout_286 = QHBoxLayout()
        self.horizontalLayout_286.setObjectName(u"horizontalLayout_286")
        self.label_368 = QLabel(self.groupBox_ch04)
        self.label_368.setObjectName(u"label_368")
        sizePolicy2.setHeightForWidth(self.label_368.sizePolicy().hasHeightForWidth())
        self.label_368.setSizePolicy(sizePolicy2)
        self.label_368.setMinimumSize(QSize(25, 25))
        self.label_368.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_286.addWidget(self.label_368)

        self.check_warning_04 = QRadioButton(self.groupBox_ch04)
        self.check_warning_04.setObjectName(u"check_warning_04")
        self.check_warning_04.setMinimumSize(QSize(100, 25))

        self.horizontalLayout_286.addWidget(self.check_warning_04)

        self.check_error_04 = QRadioButton(self.groupBox_ch04)
        self.check_error_04.setObjectName(u"check_error_04")
        self.check_error_04.setMinimumSize(QSize(100, 25))
        self.check_error_04.setChecked(True)

        self.horizontalLayout_286.addWidget(self.check_error_04)


        self.horizontalLayout_285.addLayout(self.horizontalLayout_286)

        self.check_message_04 = QLineEdit(self.groupBox_ch04)
        self.check_message_04.setObjectName(u"check_message_04")
        sizePolicy1.setHeightForWidth(self.check_message_04.sizePolicy().hasHeightForWidth())
        self.check_message_04.setSizePolicy(sizePolicy1)
        self.check_message_04.setMinimumSize(QSize(170, 25))

        self.horizontalLayout_285.addWidget(self.check_message_04)


        self.verticalLayout_85.addLayout(self.horizontalLayout_285)


        self.horizontalLayout_281.addLayout(self.verticalLayout_85)


        self.verticalLayout_63.addWidget(self.groupBox_ch04)

        self.groupBox_ch05 = QGroupBox(self.scrollAreaWidgetContents_4)
        self.groupBox_ch05.setObjectName(u"groupBox_ch05")
        sizePolicy1.setHeightForWidth(self.groupBox_ch05.sizePolicy().hasHeightForWidth())
        self.groupBox_ch05.setSizePolicy(sizePolicy1)
        self.groupBox_ch05.setMinimumSize(QSize(600, 90))
        self.groupBox_ch05.setMaximumSize(QSize(16777215, 90))
        self.horizontalLayout_287 = QHBoxLayout(self.groupBox_ch05)
        self.horizontalLayout_287.setObjectName(u"horizontalLayout_287")
        self.verticalLayout_86 = QVBoxLayout()
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")
        self.horizontalLayout_288 = QHBoxLayout()
        self.horizontalLayout_288.setObjectName(u"horizontalLayout_288")
        self.horizontalLayout_289 = QHBoxLayout()
        self.horizontalLayout_289.setObjectName(u"horizontalLayout_289")
        self.label_369 = QLabel(self.groupBox_ch05)
        self.label_369.setObjectName(u"label_369")
        sizePolicy2.setHeightForWidth(self.label_369.sizePolicy().hasHeightForWidth())
        self.label_369.setSizePolicy(sizePolicy2)
        self.label_369.setMinimumSize(QSize(15, 25))

        self.horizontalLayout_289.addWidget(self.label_369)

        self.check_if_05 = QLineEdit(self.groupBox_ch05)
        self.check_if_05.setObjectName(u"check_if_05")
        sizePolicy1.setHeightForWidth(self.check_if_05.sizePolicy().hasHeightForWidth())
        self.check_if_05.setSizePolicy(sizePolicy1)
        self.check_if_05.setMinimumSize(QSize(160, 25))

        self.horizontalLayout_289.addWidget(self.check_if_05)


        self.horizontalLayout_288.addLayout(self.horizontalLayout_289)

        self.horizontalLayout_290 = QHBoxLayout()
        self.horizontalLayout_290.setObjectName(u"horizontalLayout_290")
        self.label_370 = QLabel(self.groupBox_ch05)
        self.label_370.setObjectName(u"label_370")
        sizePolicy2.setHeightForWidth(self.label_370.sizePolicy().hasHeightForWidth())
        self.label_370.setSizePolicy(sizePolicy2)
        self.label_370.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_290.addWidget(self.label_370)

        self.check_check_05 = QLineEdit(self.groupBox_ch05)
        self.check_check_05.setObjectName(u"check_check_05")
        sizePolicy1.setHeightForWidth(self.check_check_05.sizePolicy().hasHeightForWidth())
        self.check_check_05.setSizePolicy(sizePolicy1)
        self.check_check_05.setMinimumSize(QSize(160, 25))

        self.horizontalLayout_290.addWidget(self.check_check_05)


        self.horizontalLayout_288.addLayout(self.horizontalLayout_290)


        self.verticalLayout_86.addLayout(self.horizontalLayout_288)

        self.horizontalLayout_291 = QHBoxLayout()
        self.horizontalLayout_291.setObjectName(u"horizontalLayout_291")
        self.horizontalLayout_292 = QHBoxLayout()
        self.horizontalLayout_292.setObjectName(u"horizontalLayout_292")
        self.label_371 = QLabel(self.groupBox_ch05)
        self.label_371.setObjectName(u"label_371")
        sizePolicy2.setHeightForWidth(self.label_371.sizePolicy().hasHeightForWidth())
        self.label_371.setSizePolicy(sizePolicy2)
        self.label_371.setMinimumSize(QSize(25, 25))
        self.label_371.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_292.addWidget(self.label_371)

        self.check_warning_05 = QRadioButton(self.groupBox_ch05)
        self.check_warning_05.setObjectName(u"check_warning_05")
        self.check_warning_05.setMinimumSize(QSize(100, 25))

        self.horizontalLayout_292.addWidget(self.check_warning_05)

        self.check_error_05 = QRadioButton(self.groupBox_ch05)
        self.check_error_05.setObjectName(u"check_error_05")
        self.check_error_05.setMinimumSize(QSize(100, 25))
        self.check_error_05.setChecked(True)

        self.horizontalLayout_292.addWidget(self.check_error_05)


        self.horizontalLayout_291.addLayout(self.horizontalLayout_292)

        self.check_message_05 = QLineEdit(self.groupBox_ch05)
        self.check_message_05.setObjectName(u"check_message_05")
        sizePolicy1.setHeightForWidth(self.check_message_05.sizePolicy().hasHeightForWidth())
        self.check_message_05.setSizePolicy(sizePolicy1)
        self.check_message_05.setMinimumSize(QSize(170, 25))

        self.horizontalLayout_291.addWidget(self.check_message_05)


        self.verticalLayout_86.addLayout(self.horizontalLayout_291)


        self.horizontalLayout_287.addLayout(self.verticalLayout_86)


        self.verticalLayout_63.addWidget(self.groupBox_ch05)

        self.groupBox_ch06 = QGroupBox(self.scrollAreaWidgetContents_4)
        self.groupBox_ch06.setObjectName(u"groupBox_ch06")
        sizePolicy1.setHeightForWidth(self.groupBox_ch06.sizePolicy().hasHeightForWidth())
        self.groupBox_ch06.setSizePolicy(sizePolicy1)
        self.groupBox_ch06.setMinimumSize(QSize(600, 90))
        self.groupBox_ch06.setMaximumSize(QSize(16777215, 90))
        self.horizontalLayout_293 = QHBoxLayout(self.groupBox_ch06)
        self.horizontalLayout_293.setObjectName(u"horizontalLayout_293")
        self.verticalLayout_87 = QVBoxLayout()
        self.verticalLayout_87.setObjectName(u"verticalLayout_87")
        self.horizontalLayout_294 = QHBoxLayout()
        self.horizontalLayout_294.setObjectName(u"horizontalLayout_294")
        self.horizontalLayout_295 = QHBoxLayout()
        self.horizontalLayout_295.setObjectName(u"horizontalLayout_295")
        self.label_372 = QLabel(self.groupBox_ch06)
        self.label_372.setObjectName(u"label_372")
        sizePolicy2.setHeightForWidth(self.label_372.sizePolicy().hasHeightForWidth())
        self.label_372.setSizePolicy(sizePolicy2)
        self.label_372.setMinimumSize(QSize(15, 25))

        self.horizontalLayout_295.addWidget(self.label_372)

        self.check_if_06 = QLineEdit(self.groupBox_ch06)
        self.check_if_06.setObjectName(u"check_if_06")
        sizePolicy1.setHeightForWidth(self.check_if_06.sizePolicy().hasHeightForWidth())
        self.check_if_06.setSizePolicy(sizePolicy1)
        self.check_if_06.setMinimumSize(QSize(160, 25))

        self.horizontalLayout_295.addWidget(self.check_if_06)


        self.horizontalLayout_294.addLayout(self.horizontalLayout_295)

        self.horizontalLayout_296 = QHBoxLayout()
        self.horizontalLayout_296.setObjectName(u"horizontalLayout_296")
        self.label_373 = QLabel(self.groupBox_ch06)
        self.label_373.setObjectName(u"label_373")
        sizePolicy2.setHeightForWidth(self.label_373.sizePolicy().hasHeightForWidth())
        self.label_373.setSizePolicy(sizePolicy2)
        self.label_373.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_296.addWidget(self.label_373)

        self.check_check_06 = QLineEdit(self.groupBox_ch06)
        self.check_check_06.setObjectName(u"check_check_06")
        sizePolicy1.setHeightForWidth(self.check_check_06.sizePolicy().hasHeightForWidth())
        self.check_check_06.setSizePolicy(sizePolicy1)
        self.check_check_06.setMinimumSize(QSize(160, 25))

        self.horizontalLayout_296.addWidget(self.check_check_06)


        self.horizontalLayout_294.addLayout(self.horizontalLayout_296)


        self.verticalLayout_87.addLayout(self.horizontalLayout_294)

        self.horizontalLayout_297 = QHBoxLayout()
        self.horizontalLayout_297.setObjectName(u"horizontalLayout_297")
        self.horizontalLayout_298 = QHBoxLayout()
        self.horizontalLayout_298.setObjectName(u"horizontalLayout_298")
        self.label_374 = QLabel(self.groupBox_ch06)
        self.label_374.setObjectName(u"label_374")
        sizePolicy2.setHeightForWidth(self.label_374.sizePolicy().hasHeightForWidth())
        self.label_374.setSizePolicy(sizePolicy2)
        self.label_374.setMinimumSize(QSize(25, 25))
        self.label_374.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_298.addWidget(self.label_374)

        self.check_warning_06 = QRadioButton(self.groupBox_ch06)
        self.check_warning_06.setObjectName(u"check_warning_06")
        self.check_warning_06.setMinimumSize(QSize(100, 25))

        self.horizontalLayout_298.addWidget(self.check_warning_06)

        self.check_error_06 = QRadioButton(self.groupBox_ch06)
        self.check_error_06.setObjectName(u"check_error_06")
        self.check_error_06.setMinimumSize(QSize(100, 25))
        self.check_error_06.setChecked(True)

        self.horizontalLayout_298.addWidget(self.check_error_06)


        self.horizontalLayout_297.addLayout(self.horizontalLayout_298)

        self.check_message_06 = QLineEdit(self.groupBox_ch06)
        self.check_message_06.setObjectName(u"check_message_06")
        sizePolicy1.setHeightForWidth(self.check_message_06.sizePolicy().hasHeightForWidth())
        self.check_message_06.setSizePolicy(sizePolicy1)
        self.check_message_06.setMinimumSize(QSize(170, 25))

        self.horizontalLayout_297.addWidget(self.check_message_06)


        self.verticalLayout_87.addLayout(self.horizontalLayout_297)


        self.horizontalLayout_293.addLayout(self.verticalLayout_87)


        self.verticalLayout_63.addWidget(self.groupBox_ch06)

        self.groupBox_ch07 = QGroupBox(self.scrollAreaWidgetContents_4)
        self.groupBox_ch07.setObjectName(u"groupBox_ch07")
        sizePolicy1.setHeightForWidth(self.groupBox_ch07.sizePolicy().hasHeightForWidth())
        self.groupBox_ch07.setSizePolicy(sizePolicy1)
        self.groupBox_ch07.setMinimumSize(QSize(600, 90))
        self.groupBox_ch07.setMaximumSize(QSize(16777215, 90))
        self.horizontalLayout_299 = QHBoxLayout(self.groupBox_ch07)
        self.horizontalLayout_299.setObjectName(u"horizontalLayout_299")
        self.verticalLayout_88 = QVBoxLayout()
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.horizontalLayout_300 = QHBoxLayout()
        self.horizontalLayout_300.setObjectName(u"horizontalLayout_300")
        self.horizontalLayout_301 = QHBoxLayout()
        self.horizontalLayout_301.setObjectName(u"horizontalLayout_301")
        self.label_375 = QLabel(self.groupBox_ch07)
        self.label_375.setObjectName(u"label_375")
        sizePolicy2.setHeightForWidth(self.label_375.sizePolicy().hasHeightForWidth())
        self.label_375.setSizePolicy(sizePolicy2)
        self.label_375.setMinimumSize(QSize(15, 25))

        self.horizontalLayout_301.addWidget(self.label_375)

        self.check_if_07 = QLineEdit(self.groupBox_ch07)
        self.check_if_07.setObjectName(u"check_if_07")
        sizePolicy1.setHeightForWidth(self.check_if_07.sizePolicy().hasHeightForWidth())
        self.check_if_07.setSizePolicy(sizePolicy1)
        self.check_if_07.setMinimumSize(QSize(160, 25))

        self.horizontalLayout_301.addWidget(self.check_if_07)


        self.horizontalLayout_300.addLayout(self.horizontalLayout_301)

        self.horizontalLayout_302 = QHBoxLayout()
        self.horizontalLayout_302.setObjectName(u"horizontalLayout_302")
        self.label_376 = QLabel(self.groupBox_ch07)
        self.label_376.setObjectName(u"label_376")
        sizePolicy2.setHeightForWidth(self.label_376.sizePolicy().hasHeightForWidth())
        self.label_376.setSizePolicy(sizePolicy2)
        self.label_376.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_302.addWidget(self.label_376)

        self.check_check_07 = QLineEdit(self.groupBox_ch07)
        self.check_check_07.setObjectName(u"check_check_07")
        sizePolicy1.setHeightForWidth(self.check_check_07.sizePolicy().hasHeightForWidth())
        self.check_check_07.setSizePolicy(sizePolicy1)
        self.check_check_07.setMinimumSize(QSize(160, 25))

        self.horizontalLayout_302.addWidget(self.check_check_07)


        self.horizontalLayout_300.addLayout(self.horizontalLayout_302)


        self.verticalLayout_88.addLayout(self.horizontalLayout_300)

        self.horizontalLayout_303 = QHBoxLayout()
        self.horizontalLayout_303.setObjectName(u"horizontalLayout_303")
        self.horizontalLayout_304 = QHBoxLayout()
        self.horizontalLayout_304.setObjectName(u"horizontalLayout_304")
        self.label_377 = QLabel(self.groupBox_ch07)
        self.label_377.setObjectName(u"label_377")
        sizePolicy2.setHeightForWidth(self.label_377.sizePolicy().hasHeightForWidth())
        self.label_377.setSizePolicy(sizePolicy2)
        self.label_377.setMinimumSize(QSize(25, 25))
        self.label_377.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_304.addWidget(self.label_377)

        self.check_warning_07 = QRadioButton(self.groupBox_ch07)
        self.check_warning_07.setObjectName(u"check_warning_07")
        self.check_warning_07.setMinimumSize(QSize(100, 25))

        self.horizontalLayout_304.addWidget(self.check_warning_07)

        self.check_error_07 = QRadioButton(self.groupBox_ch07)
        self.check_error_07.setObjectName(u"check_error_07")
        self.check_error_07.setMinimumSize(QSize(100, 25))
        self.check_error_07.setChecked(True)

        self.horizontalLayout_304.addWidget(self.check_error_07)


        self.horizontalLayout_303.addLayout(self.horizontalLayout_304)

        self.check_message_07 = QLineEdit(self.groupBox_ch07)
        self.check_message_07.setObjectName(u"check_message_07")
        sizePolicy1.setHeightForWidth(self.check_message_07.sizePolicy().hasHeightForWidth())
        self.check_message_07.setSizePolicy(sizePolicy1)
        self.check_message_07.setMinimumSize(QSize(170, 25))

        self.horizontalLayout_303.addWidget(self.check_message_07)


        self.verticalLayout_88.addLayout(self.horizontalLayout_303)


        self.horizontalLayout_299.addLayout(self.verticalLayout_88)


        self.verticalLayout_63.addWidget(self.groupBox_ch07)

        self.groupBox_ch08 = QGroupBox(self.scrollAreaWidgetContents_4)
        self.groupBox_ch08.setObjectName(u"groupBox_ch08")
        sizePolicy1.setHeightForWidth(self.groupBox_ch08.sizePolicy().hasHeightForWidth())
        self.groupBox_ch08.setSizePolicy(sizePolicy1)
        self.groupBox_ch08.setMinimumSize(QSize(600, 90))
        self.groupBox_ch08.setMaximumSize(QSize(16777215, 90))
        self.horizontalLayout_305 = QHBoxLayout(self.groupBox_ch08)
        self.horizontalLayout_305.setObjectName(u"horizontalLayout_305")
        self.verticalLayout_89 = QVBoxLayout()
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")
        self.horizontalLayout_306 = QHBoxLayout()
        self.horizontalLayout_306.setObjectName(u"horizontalLayout_306")
        self.horizontalLayout_307 = QHBoxLayout()
        self.horizontalLayout_307.setObjectName(u"horizontalLayout_307")
        self.label_378 = QLabel(self.groupBox_ch08)
        self.label_378.setObjectName(u"label_378")
        sizePolicy2.setHeightForWidth(self.label_378.sizePolicy().hasHeightForWidth())
        self.label_378.setSizePolicy(sizePolicy2)
        self.label_378.setMinimumSize(QSize(15, 25))

        self.horizontalLayout_307.addWidget(self.label_378)

        self.check_if_08 = QLineEdit(self.groupBox_ch08)
        self.check_if_08.setObjectName(u"check_if_08")
        sizePolicy1.setHeightForWidth(self.check_if_08.sizePolicy().hasHeightForWidth())
        self.check_if_08.setSizePolicy(sizePolicy1)
        self.check_if_08.setMinimumSize(QSize(160, 25))

        self.horizontalLayout_307.addWidget(self.check_if_08)


        self.horizontalLayout_306.addLayout(self.horizontalLayout_307)

        self.horizontalLayout_308 = QHBoxLayout()
        self.horizontalLayout_308.setObjectName(u"horizontalLayout_308")
        self.label_379 = QLabel(self.groupBox_ch08)
        self.label_379.setObjectName(u"label_379")
        sizePolicy2.setHeightForWidth(self.label_379.sizePolicy().hasHeightForWidth())
        self.label_379.setSizePolicy(sizePolicy2)
        self.label_379.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_308.addWidget(self.label_379)

        self.check_check_08 = QLineEdit(self.groupBox_ch08)
        self.check_check_08.setObjectName(u"check_check_08")
        sizePolicy1.setHeightForWidth(self.check_check_08.sizePolicy().hasHeightForWidth())
        self.check_check_08.setSizePolicy(sizePolicy1)
        self.check_check_08.setMinimumSize(QSize(160, 25))

        self.horizontalLayout_308.addWidget(self.check_check_08)


        self.horizontalLayout_306.addLayout(self.horizontalLayout_308)


        self.verticalLayout_89.addLayout(self.horizontalLayout_306)

        self.horizontalLayout_309 = QHBoxLayout()
        self.horizontalLayout_309.setObjectName(u"horizontalLayout_309")
        self.label_380 = QLabel(self.groupBox_ch08)
        self.label_380.setObjectName(u"label_380")
        sizePolicy2.setHeightForWidth(self.label_380.sizePolicy().hasHeightForWidth())
        self.label_380.setSizePolicy(sizePolicy2)
        self.label_380.setMinimumSize(QSize(25, 25))
        self.label_380.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_309.addWidget(self.label_380)

        self.horizontalLayout_310 = QHBoxLayout()
        self.horizontalLayout_310.setObjectName(u"horizontalLayout_310")
        self.check_warning_08 = QRadioButton(self.groupBox_ch08)
        self.check_warning_08.setObjectName(u"check_warning_08")
        self.check_warning_08.setMinimumSize(QSize(100, 25))

        self.horizontalLayout_310.addWidget(self.check_warning_08)

        self.check_error_08 = QRadioButton(self.groupBox_ch08)
        self.check_error_08.setObjectName(u"check_error_08")
        self.check_error_08.setMinimumSize(QSize(100, 25))
        self.check_error_08.setChecked(True)

        self.horizontalLayout_310.addWidget(self.check_error_08)


        self.horizontalLayout_309.addLayout(self.horizontalLayout_310)

        self.check_message_08 = QLineEdit(self.groupBox_ch08)
        self.check_message_08.setObjectName(u"check_message_08")
        sizePolicy1.setHeightForWidth(self.check_message_08.sizePolicy().hasHeightForWidth())
        self.check_message_08.setSizePolicy(sizePolicy1)
        self.check_message_08.setMinimumSize(QSize(170, 25))

        self.horizontalLayout_309.addWidget(self.check_message_08)


        self.verticalLayout_89.addLayout(self.horizontalLayout_309)


        self.horizontalLayout_305.addLayout(self.verticalLayout_89)


        self.verticalLayout_63.addWidget(self.groupBox_ch08)

        self.groupBox_ch09 = QGroupBox(self.scrollAreaWidgetContents_4)
        self.groupBox_ch09.setObjectName(u"groupBox_ch09")
        sizePolicy1.setHeightForWidth(self.groupBox_ch09.sizePolicy().hasHeightForWidth())
        self.groupBox_ch09.setSizePolicy(sizePolicy1)
        self.groupBox_ch09.setMinimumSize(QSize(600, 90))
        self.groupBox_ch09.setMaximumSize(QSize(16777215, 90))
        self.horizontalLayout_311 = QHBoxLayout(self.groupBox_ch09)
        self.horizontalLayout_311.setObjectName(u"horizontalLayout_311")
        self.verticalLayout_90 = QVBoxLayout()
        self.verticalLayout_90.setObjectName(u"verticalLayout_90")
        self.horizontalLayout_312 = QHBoxLayout()
        self.horizontalLayout_312.setObjectName(u"horizontalLayout_312")
        self.horizontalLayout_313 = QHBoxLayout()
        self.horizontalLayout_313.setObjectName(u"horizontalLayout_313")
        self.label_381 = QLabel(self.groupBox_ch09)
        self.label_381.setObjectName(u"label_381")
        sizePolicy2.setHeightForWidth(self.label_381.sizePolicy().hasHeightForWidth())
        self.label_381.setSizePolicy(sizePolicy2)
        self.label_381.setMinimumSize(QSize(15, 25))

        self.horizontalLayout_313.addWidget(self.label_381)

        self.check_if_09 = QLineEdit(self.groupBox_ch09)
        self.check_if_09.setObjectName(u"check_if_09")
        sizePolicy1.setHeightForWidth(self.check_if_09.sizePolicy().hasHeightForWidth())
        self.check_if_09.setSizePolicy(sizePolicy1)
        self.check_if_09.setMinimumSize(QSize(160, 25))

        self.horizontalLayout_313.addWidget(self.check_if_09)


        self.horizontalLayout_312.addLayout(self.horizontalLayout_313)

        self.horizontalLayout_314 = QHBoxLayout()
        self.horizontalLayout_314.setObjectName(u"horizontalLayout_314")
        self.label_382 = QLabel(self.groupBox_ch09)
        self.label_382.setObjectName(u"label_382")
        sizePolicy2.setHeightForWidth(self.label_382.sizePolicy().hasHeightForWidth())
        self.label_382.setSizePolicy(sizePolicy2)
        self.label_382.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_314.addWidget(self.label_382)

        self.check_check_09 = QLineEdit(self.groupBox_ch09)
        self.check_check_09.setObjectName(u"check_check_09")
        sizePolicy1.setHeightForWidth(self.check_check_09.sizePolicy().hasHeightForWidth())
        self.check_check_09.setSizePolicy(sizePolicy1)
        self.check_check_09.setMinimumSize(QSize(160, 25))

        self.horizontalLayout_314.addWidget(self.check_check_09)


        self.horizontalLayout_312.addLayout(self.horizontalLayout_314)


        self.verticalLayout_90.addLayout(self.horizontalLayout_312)

        self.horizontalLayout_315 = QHBoxLayout()
        self.horizontalLayout_315.setObjectName(u"horizontalLayout_315")
        self.label_383 = QLabel(self.groupBox_ch09)
        self.label_383.setObjectName(u"label_383")
        sizePolicy2.setHeightForWidth(self.label_383.sizePolicy().hasHeightForWidth())
        self.label_383.setSizePolicy(sizePolicy2)
        self.label_383.setMinimumSize(QSize(25, 25))
        self.label_383.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_315.addWidget(self.label_383)

        self.horizontalLayout_316 = QHBoxLayout()
        self.horizontalLayout_316.setObjectName(u"horizontalLayout_316")
        self.check_warning_09 = QRadioButton(self.groupBox_ch09)
        self.check_warning_09.setObjectName(u"check_warning_09")
        self.check_warning_09.setMinimumSize(QSize(100, 25))

        self.horizontalLayout_316.addWidget(self.check_warning_09)

        self.check_error_09 = QRadioButton(self.groupBox_ch09)
        self.check_error_09.setObjectName(u"check_error_09")
        self.check_error_09.setMinimumSize(QSize(100, 25))
        self.check_error_09.setChecked(True)

        self.horizontalLayout_316.addWidget(self.check_error_09)


        self.horizontalLayout_315.addLayout(self.horizontalLayout_316)

        self.check_message_09 = QLineEdit(self.groupBox_ch09)
        self.check_message_09.setObjectName(u"check_message_09")
        sizePolicy1.setHeightForWidth(self.check_message_09.sizePolicy().hasHeightForWidth())
        self.check_message_09.setSizePolicy(sizePolicy1)
        self.check_message_09.setMinimumSize(QSize(170, 25))

        self.horizontalLayout_315.addWidget(self.check_message_09)


        self.verticalLayout_90.addLayout(self.horizontalLayout_315)


        self.horizontalLayout_311.addLayout(self.verticalLayout_90)


        self.verticalLayout_63.addWidget(self.groupBox_ch09)

        self.groupBox_ch10 = QGroupBox(self.scrollAreaWidgetContents_4)
        self.groupBox_ch10.setObjectName(u"groupBox_ch10")
        sizePolicy1.setHeightForWidth(self.groupBox_ch10.sizePolicy().hasHeightForWidth())
        self.groupBox_ch10.setSizePolicy(sizePolicy1)
        self.groupBox_ch10.setMinimumSize(QSize(600, 90))
        self.groupBox_ch10.setMaximumSize(QSize(16777215, 90))
        self.horizontalLayout_371 = QHBoxLayout(self.groupBox_ch10)
        self.horizontalLayout_371.setObjectName(u"horizontalLayout_371")
        self.verticalLayout_100 = QVBoxLayout()
        self.verticalLayout_100.setObjectName(u"verticalLayout_100")
        self.horizontalLayout_372 = QHBoxLayout()
        self.horizontalLayout_372.setObjectName(u"horizontalLayout_372")
        self.horizontalLayout_373 = QHBoxLayout()
        self.horizontalLayout_373.setObjectName(u"horizontalLayout_373")
        self.label_411 = QLabel(self.groupBox_ch10)
        self.label_411.setObjectName(u"label_411")
        sizePolicy2.setHeightForWidth(self.label_411.sizePolicy().hasHeightForWidth())
        self.label_411.setSizePolicy(sizePolicy2)
        self.label_411.setMinimumSize(QSize(15, 25))

        self.horizontalLayout_373.addWidget(self.label_411)

        self.check_if_10 = QLineEdit(self.groupBox_ch10)
        self.check_if_10.setObjectName(u"check_if_10")
        sizePolicy1.setHeightForWidth(self.check_if_10.sizePolicy().hasHeightForWidth())
        self.check_if_10.setSizePolicy(sizePolicy1)
        self.check_if_10.setMinimumSize(QSize(160, 25))

        self.horizontalLayout_373.addWidget(self.check_if_10)


        self.horizontalLayout_372.addLayout(self.horizontalLayout_373)

        self.horizontalLayout_374 = QHBoxLayout()
        self.horizontalLayout_374.setObjectName(u"horizontalLayout_374")
        self.label_412 = QLabel(self.groupBox_ch10)
        self.label_412.setObjectName(u"label_412")
        sizePolicy2.setHeightForWidth(self.label_412.sizePolicy().hasHeightForWidth())
        self.label_412.setSizePolicy(sizePolicy2)
        self.label_412.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_374.addWidget(self.label_412)

        self.check_check_10 = QLineEdit(self.groupBox_ch10)
        self.check_check_10.setObjectName(u"check_check_10")
        sizePolicy1.setHeightForWidth(self.check_check_10.sizePolicy().hasHeightForWidth())
        self.check_check_10.setSizePolicy(sizePolicy1)
        self.check_check_10.setMinimumSize(QSize(160, 25))

        self.horizontalLayout_374.addWidget(self.check_check_10)


        self.horizontalLayout_372.addLayout(self.horizontalLayout_374)


        self.verticalLayout_100.addLayout(self.horizontalLayout_372)

        self.horizontalLayout_375 = QHBoxLayout()
        self.horizontalLayout_375.setObjectName(u"horizontalLayout_375")
        self.label_413 = QLabel(self.groupBox_ch10)
        self.label_413.setObjectName(u"label_413")
        sizePolicy2.setHeightForWidth(self.label_413.sizePolicy().hasHeightForWidth())
        self.label_413.setSizePolicy(sizePolicy2)
        self.label_413.setMinimumSize(QSize(25, 25))
        self.label_413.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_375.addWidget(self.label_413)

        self.horizontalLayout_376 = QHBoxLayout()
        self.horizontalLayout_376.setObjectName(u"horizontalLayout_376")
        self.check_warning_10 = QRadioButton(self.groupBox_ch10)
        self.check_warning_10.setObjectName(u"check_warning_10")
        self.check_warning_10.setMinimumSize(QSize(100, 25))

        self.horizontalLayout_376.addWidget(self.check_warning_10)

        self.check_error_10 = QRadioButton(self.groupBox_ch10)
        self.check_error_10.setObjectName(u"check_error_10")
        self.check_error_10.setMinimumSize(QSize(100, 25))
        self.check_error_10.setChecked(True)

        self.horizontalLayout_376.addWidget(self.check_error_10)


        self.horizontalLayout_375.addLayout(self.horizontalLayout_376)

        self.check_message_10 = QLineEdit(self.groupBox_ch10)
        self.check_message_10.setObjectName(u"check_message_10")
        sizePolicy1.setHeightForWidth(self.check_message_10.sizePolicy().hasHeightForWidth())
        self.check_message_10.setSizePolicy(sizePolicy1)
        self.check_message_10.setMinimumSize(QSize(170, 25))

        self.horizontalLayout_375.addWidget(self.check_message_10)


        self.verticalLayout_100.addLayout(self.horizontalLayout_375)


        self.horizontalLayout_371.addLayout(self.verticalLayout_100)


        self.verticalLayout_63.addWidget(self.groupBox_ch10)

        self.groupBox_ch14 = QGroupBox(self.scrollAreaWidgetContents_4)
        self.groupBox_ch14.setObjectName(u"groupBox_ch14")
        sizePolicy1.setHeightForWidth(self.groupBox_ch14.sizePolicy().hasHeightForWidth())
        self.groupBox_ch14.setSizePolicy(sizePolicy1)
        self.groupBox_ch14.setMinimumSize(QSize(600, 90))
        self.groupBox_ch14.setMaximumSize(QSize(16777215, 90))
        self.horizontalLayout_377 = QHBoxLayout(self.groupBox_ch14)
        self.horizontalLayout_377.setObjectName(u"horizontalLayout_377")
        self.verticalLayout_101 = QVBoxLayout()
        self.verticalLayout_101.setObjectName(u"verticalLayout_101")
        self.horizontalLayout_378 = QHBoxLayout()
        self.horizontalLayout_378.setObjectName(u"horizontalLayout_378")
        self.horizontalLayout_379 = QHBoxLayout()
        self.horizontalLayout_379.setObjectName(u"horizontalLayout_379")
        self.label_414 = QLabel(self.groupBox_ch14)
        self.label_414.setObjectName(u"label_414")
        sizePolicy2.setHeightForWidth(self.label_414.sizePolicy().hasHeightForWidth())
        self.label_414.setSizePolicy(sizePolicy2)
        self.label_414.setMinimumSize(QSize(15, 25))

        self.horizontalLayout_379.addWidget(self.label_414)

        self.check_if_11 = QLineEdit(self.groupBox_ch14)
        self.check_if_11.setObjectName(u"check_if_11")
        sizePolicy1.setHeightForWidth(self.check_if_11.sizePolicy().hasHeightForWidth())
        self.check_if_11.setSizePolicy(sizePolicy1)
        self.check_if_11.setMinimumSize(QSize(160, 25))

        self.horizontalLayout_379.addWidget(self.check_if_11)


        self.horizontalLayout_378.addLayout(self.horizontalLayout_379)

        self.horizontalLayout_380 = QHBoxLayout()
        self.horizontalLayout_380.setObjectName(u"horizontalLayout_380")
        self.label_415 = QLabel(self.groupBox_ch14)
        self.label_415.setObjectName(u"label_415")
        sizePolicy2.setHeightForWidth(self.label_415.sizePolicy().hasHeightForWidth())
        self.label_415.setSizePolicy(sizePolicy2)
        self.label_415.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_380.addWidget(self.label_415)

        self.check_check_11 = QLineEdit(self.groupBox_ch14)
        self.check_check_11.setObjectName(u"check_check_11")
        sizePolicy1.setHeightForWidth(self.check_check_11.sizePolicy().hasHeightForWidth())
        self.check_check_11.setSizePolicy(sizePolicy1)
        self.check_check_11.setMinimumSize(QSize(160, 25))

        self.horizontalLayout_380.addWidget(self.check_check_11)


        self.horizontalLayout_378.addLayout(self.horizontalLayout_380)


        self.verticalLayout_101.addLayout(self.horizontalLayout_378)

        self.horizontalLayout_381 = QHBoxLayout()
        self.horizontalLayout_381.setObjectName(u"horizontalLayout_381")
        self.label_416 = QLabel(self.groupBox_ch14)
        self.label_416.setObjectName(u"label_416")
        sizePolicy2.setHeightForWidth(self.label_416.sizePolicy().hasHeightForWidth())
        self.label_416.setSizePolicy(sizePolicy2)
        self.label_416.setMinimumSize(QSize(25, 25))
        self.label_416.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_381.addWidget(self.label_416)

        self.horizontalLayout_382 = QHBoxLayout()
        self.horizontalLayout_382.setObjectName(u"horizontalLayout_382")
        self.check_warning_11 = QRadioButton(self.groupBox_ch14)
        self.check_warning_11.setObjectName(u"check_warning_11")
        self.check_warning_11.setMinimumSize(QSize(100, 25))

        self.horizontalLayout_382.addWidget(self.check_warning_11)

        self.check_error_11 = QRadioButton(self.groupBox_ch14)
        self.check_error_11.setObjectName(u"check_error_11")
        self.check_error_11.setMinimumSize(QSize(100, 25))
        self.check_error_11.setChecked(True)

        self.horizontalLayout_382.addWidget(self.check_error_11)


        self.horizontalLayout_381.addLayout(self.horizontalLayout_382)

        self.check_message_11 = QLineEdit(self.groupBox_ch14)
        self.check_message_11.setObjectName(u"check_message_11")
        sizePolicy1.setHeightForWidth(self.check_message_11.sizePolicy().hasHeightForWidth())
        self.check_message_11.setSizePolicy(sizePolicy1)
        self.check_message_11.setMinimumSize(QSize(170, 25))

        self.horizontalLayout_381.addWidget(self.check_message_11)


        self.verticalLayout_101.addLayout(self.horizontalLayout_381)


        self.horizontalLayout_377.addLayout(self.verticalLayout_101)


        self.verticalLayout_63.addWidget(self.groupBox_ch14)

        self.groupBox_ch15 = QGroupBox(self.scrollAreaWidgetContents_4)
        self.groupBox_ch15.setObjectName(u"groupBox_ch15")
        sizePolicy1.setHeightForWidth(self.groupBox_ch15.sizePolicy().hasHeightForWidth())
        self.groupBox_ch15.setSizePolicy(sizePolicy1)
        self.groupBox_ch15.setMinimumSize(QSize(600, 90))
        self.groupBox_ch15.setMaximumSize(QSize(16777215, 90))
        self.horizontalLayout_383 = QHBoxLayout(self.groupBox_ch15)
        self.horizontalLayout_383.setObjectName(u"horizontalLayout_383")
        self.verticalLayout_102 = QVBoxLayout()
        self.verticalLayout_102.setObjectName(u"verticalLayout_102")
        self.horizontalLayout_384 = QHBoxLayout()
        self.horizontalLayout_384.setObjectName(u"horizontalLayout_384")
        self.horizontalLayout_385 = QHBoxLayout()
        self.horizontalLayout_385.setObjectName(u"horizontalLayout_385")
        self.label_417 = QLabel(self.groupBox_ch15)
        self.label_417.setObjectName(u"label_417")
        sizePolicy2.setHeightForWidth(self.label_417.sizePolicy().hasHeightForWidth())
        self.label_417.setSizePolicy(sizePolicy2)
        self.label_417.setMinimumSize(QSize(15, 25))

        self.horizontalLayout_385.addWidget(self.label_417)

        self.check_if_12 = QLineEdit(self.groupBox_ch15)
        self.check_if_12.setObjectName(u"check_if_12")
        sizePolicy1.setHeightForWidth(self.check_if_12.sizePolicy().hasHeightForWidth())
        self.check_if_12.setSizePolicy(sizePolicy1)
        self.check_if_12.setMinimumSize(QSize(160, 25))

        self.horizontalLayout_385.addWidget(self.check_if_12)


        self.horizontalLayout_384.addLayout(self.horizontalLayout_385)

        self.horizontalLayout_386 = QHBoxLayout()
        self.horizontalLayout_386.setObjectName(u"horizontalLayout_386")
        self.label_418 = QLabel(self.groupBox_ch15)
        self.label_418.setObjectName(u"label_418")
        sizePolicy2.setHeightForWidth(self.label_418.sizePolicy().hasHeightForWidth())
        self.label_418.setSizePolicy(sizePolicy2)
        self.label_418.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_386.addWidget(self.label_418)

        self.check_check_12 = QLineEdit(self.groupBox_ch15)
        self.check_check_12.setObjectName(u"check_check_12")
        sizePolicy1.setHeightForWidth(self.check_check_12.sizePolicy().hasHeightForWidth())
        self.check_check_12.setSizePolicy(sizePolicy1)
        self.check_check_12.setMinimumSize(QSize(160, 25))

        self.horizontalLayout_386.addWidget(self.check_check_12)


        self.horizontalLayout_384.addLayout(self.horizontalLayout_386)


        self.verticalLayout_102.addLayout(self.horizontalLayout_384)

        self.horizontalLayout_387 = QHBoxLayout()
        self.horizontalLayout_387.setObjectName(u"horizontalLayout_387")
        self.label_419 = QLabel(self.groupBox_ch15)
        self.label_419.setObjectName(u"label_419")
        sizePolicy2.setHeightForWidth(self.label_419.sizePolicy().hasHeightForWidth())
        self.label_419.setSizePolicy(sizePolicy2)
        self.label_419.setMinimumSize(QSize(25, 25))
        self.label_419.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_387.addWidget(self.label_419)

        self.horizontalLayout_388 = QHBoxLayout()
        self.horizontalLayout_388.setObjectName(u"horizontalLayout_388")
        self.check_warning_12 = QRadioButton(self.groupBox_ch15)
        self.check_warning_12.setObjectName(u"check_warning_12")
        self.check_warning_12.setMinimumSize(QSize(100, 25))

        self.horizontalLayout_388.addWidget(self.check_warning_12)

        self.check_error_12 = QRadioButton(self.groupBox_ch15)
        self.check_error_12.setObjectName(u"check_error_12")
        self.check_error_12.setMinimumSize(QSize(100, 25))
        self.check_error_12.setChecked(True)

        self.horizontalLayout_388.addWidget(self.check_error_12)


        self.horizontalLayout_387.addLayout(self.horizontalLayout_388)

        self.check_message_12 = QLineEdit(self.groupBox_ch15)
        self.check_message_12.setObjectName(u"check_message_12")
        sizePolicy1.setHeightForWidth(self.check_message_12.sizePolicy().hasHeightForWidth())
        self.check_message_12.setSizePolicy(sizePolicy1)
        self.check_message_12.setMinimumSize(QSize(170, 25))

        self.horizontalLayout_387.addWidget(self.check_message_12)


        self.verticalLayout_102.addLayout(self.horizontalLayout_387)


        self.horizontalLayout_383.addLayout(self.verticalLayout_102)


        self.verticalLayout_63.addWidget(self.groupBox_ch15)

        self.groupBox_ch16 = QGroupBox(self.scrollAreaWidgetContents_4)
        self.groupBox_ch16.setObjectName(u"groupBox_ch16")
        sizePolicy1.setHeightForWidth(self.groupBox_ch16.sizePolicy().hasHeightForWidth())
        self.groupBox_ch16.setSizePolicy(sizePolicy1)
        self.groupBox_ch16.setMinimumSize(QSize(600, 90))
        self.groupBox_ch16.setMaximumSize(QSize(16777215, 90))
        self.horizontalLayout_389 = QHBoxLayout(self.groupBox_ch16)
        self.horizontalLayout_389.setObjectName(u"horizontalLayout_389")
        self.verticalLayout_103 = QVBoxLayout()
        self.verticalLayout_103.setObjectName(u"verticalLayout_103")
        self.horizontalLayout_390 = QHBoxLayout()
        self.horizontalLayout_390.setObjectName(u"horizontalLayout_390")
        self.horizontalLayout_391 = QHBoxLayout()
        self.horizontalLayout_391.setObjectName(u"horizontalLayout_391")
        self.label_420 = QLabel(self.groupBox_ch16)
        self.label_420.setObjectName(u"label_420")
        sizePolicy2.setHeightForWidth(self.label_420.sizePolicy().hasHeightForWidth())
        self.label_420.setSizePolicy(sizePolicy2)
        self.label_420.setMinimumSize(QSize(15, 25))

        self.horizontalLayout_391.addWidget(self.label_420)

        self.check_if_13 = QLineEdit(self.groupBox_ch16)
        self.check_if_13.setObjectName(u"check_if_13")
        sizePolicy1.setHeightForWidth(self.check_if_13.sizePolicy().hasHeightForWidth())
        self.check_if_13.setSizePolicy(sizePolicy1)
        self.check_if_13.setMinimumSize(QSize(160, 25))

        self.horizontalLayout_391.addWidget(self.check_if_13)


        self.horizontalLayout_390.addLayout(self.horizontalLayout_391)

        self.horizontalLayout_392 = QHBoxLayout()
        self.horizontalLayout_392.setObjectName(u"horizontalLayout_392")
        self.label_421 = QLabel(self.groupBox_ch16)
        self.label_421.setObjectName(u"label_421")
        sizePolicy2.setHeightForWidth(self.label_421.sizePolicy().hasHeightForWidth())
        self.label_421.setSizePolicy(sizePolicy2)
        self.label_421.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_392.addWidget(self.label_421)

        self.check_check_13 = QLineEdit(self.groupBox_ch16)
        self.check_check_13.setObjectName(u"check_check_13")
        sizePolicy1.setHeightForWidth(self.check_check_13.sizePolicy().hasHeightForWidth())
        self.check_check_13.setSizePolicy(sizePolicy1)
        self.check_check_13.setMinimumSize(QSize(160, 25))

        self.horizontalLayout_392.addWidget(self.check_check_13)


        self.horizontalLayout_390.addLayout(self.horizontalLayout_392)


        self.verticalLayout_103.addLayout(self.horizontalLayout_390)

        self.horizontalLayout_393 = QHBoxLayout()
        self.horizontalLayout_393.setObjectName(u"horizontalLayout_393")
        self.label_422 = QLabel(self.groupBox_ch16)
        self.label_422.setObjectName(u"label_422")
        sizePolicy2.setHeightForWidth(self.label_422.sizePolicy().hasHeightForWidth())
        self.label_422.setSizePolicy(sizePolicy2)
        self.label_422.setMinimumSize(QSize(25, 25))
        self.label_422.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_393.addWidget(self.label_422)

        self.horizontalLayout_394 = QHBoxLayout()
        self.horizontalLayout_394.setObjectName(u"horizontalLayout_394")
        self.check_warning_13 = QRadioButton(self.groupBox_ch16)
        self.check_warning_13.setObjectName(u"check_warning_13")
        self.check_warning_13.setMinimumSize(QSize(100, 25))

        self.horizontalLayout_394.addWidget(self.check_warning_13)

        self.check_error_13 = QRadioButton(self.groupBox_ch16)
        self.check_error_13.setObjectName(u"check_error_13")
        self.check_error_13.setMinimumSize(QSize(100, 25))
        self.check_error_13.setChecked(True)

        self.horizontalLayout_394.addWidget(self.check_error_13)


        self.horizontalLayout_393.addLayout(self.horizontalLayout_394)

        self.check_message_13 = QLineEdit(self.groupBox_ch16)
        self.check_message_13.setObjectName(u"check_message_13")
        sizePolicy1.setHeightForWidth(self.check_message_13.sizePolicy().hasHeightForWidth())
        self.check_message_13.setSizePolicy(sizePolicy1)
        self.check_message_13.setMinimumSize(QSize(170, 25))

        self.horizontalLayout_393.addWidget(self.check_message_13)


        self.verticalLayout_103.addLayout(self.horizontalLayout_393)


        self.horizontalLayout_389.addLayout(self.verticalLayout_103)


        self.verticalLayout_63.addWidget(self.groupBox_ch16)

        self.groupBox_ch17 = QGroupBox(self.scrollAreaWidgetContents_4)
        self.groupBox_ch17.setObjectName(u"groupBox_ch17")
        sizePolicy1.setHeightForWidth(self.groupBox_ch17.sizePolicy().hasHeightForWidth())
        self.groupBox_ch17.setSizePolicy(sizePolicy1)
        self.groupBox_ch17.setMinimumSize(QSize(600, 90))
        self.groupBox_ch17.setMaximumSize(QSize(16777215, 90))
        self.horizontalLayout_395 = QHBoxLayout(self.groupBox_ch17)
        self.horizontalLayout_395.setObjectName(u"horizontalLayout_395")
        self.verticalLayout_104 = QVBoxLayout()
        self.verticalLayout_104.setObjectName(u"verticalLayout_104")
        self.horizontalLayout_396 = QHBoxLayout()
        self.horizontalLayout_396.setObjectName(u"horizontalLayout_396")
        self.horizontalLayout_397 = QHBoxLayout()
        self.horizontalLayout_397.setObjectName(u"horizontalLayout_397")
        self.label_423 = QLabel(self.groupBox_ch17)
        self.label_423.setObjectName(u"label_423")
        sizePolicy2.setHeightForWidth(self.label_423.sizePolicy().hasHeightForWidth())
        self.label_423.setSizePolicy(sizePolicy2)
        self.label_423.setMinimumSize(QSize(15, 25))

        self.horizontalLayout_397.addWidget(self.label_423)

        self.check_if_14 = QLineEdit(self.groupBox_ch17)
        self.check_if_14.setObjectName(u"check_if_14")
        sizePolicy1.setHeightForWidth(self.check_if_14.sizePolicy().hasHeightForWidth())
        self.check_if_14.setSizePolicy(sizePolicy1)
        self.check_if_14.setMinimumSize(QSize(160, 25))

        self.horizontalLayout_397.addWidget(self.check_if_14)


        self.horizontalLayout_396.addLayout(self.horizontalLayout_397)

        self.horizontalLayout_398 = QHBoxLayout()
        self.horizontalLayout_398.setObjectName(u"horizontalLayout_398")
        self.label_424 = QLabel(self.groupBox_ch17)
        self.label_424.setObjectName(u"label_424")
        sizePolicy2.setHeightForWidth(self.label_424.sizePolicy().hasHeightForWidth())
        self.label_424.setSizePolicy(sizePolicy2)
        self.label_424.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_398.addWidget(self.label_424)

        self.check_check_14 = QLineEdit(self.groupBox_ch17)
        self.check_check_14.setObjectName(u"check_check_14")
        sizePolicy1.setHeightForWidth(self.check_check_14.sizePolicy().hasHeightForWidth())
        self.check_check_14.setSizePolicy(sizePolicy1)
        self.check_check_14.setMinimumSize(QSize(160, 25))

        self.horizontalLayout_398.addWidget(self.check_check_14)


        self.horizontalLayout_396.addLayout(self.horizontalLayout_398)


        self.verticalLayout_104.addLayout(self.horizontalLayout_396)

        self.horizontalLayout_399 = QHBoxLayout()
        self.horizontalLayout_399.setObjectName(u"horizontalLayout_399")
        self.label_425 = QLabel(self.groupBox_ch17)
        self.label_425.setObjectName(u"label_425")
        sizePolicy2.setHeightForWidth(self.label_425.sizePolicy().hasHeightForWidth())
        self.label_425.setSizePolicy(sizePolicy2)
        self.label_425.setMinimumSize(QSize(25, 25))
        self.label_425.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_399.addWidget(self.label_425)

        self.horizontalLayout_400 = QHBoxLayout()
        self.horizontalLayout_400.setObjectName(u"horizontalLayout_400")
        self.check_warning_14 = QRadioButton(self.groupBox_ch17)
        self.check_warning_14.setObjectName(u"check_warning_14")
        self.check_warning_14.setMinimumSize(QSize(100, 25))

        self.horizontalLayout_400.addWidget(self.check_warning_14)

        self.check_error_14 = QRadioButton(self.groupBox_ch17)
        self.check_error_14.setObjectName(u"check_error_14")
        self.check_error_14.setMinimumSize(QSize(100, 25))
        self.check_error_14.setChecked(True)

        self.horizontalLayout_400.addWidget(self.check_error_14)


        self.horizontalLayout_399.addLayout(self.horizontalLayout_400)

        self.check_message_14 = QLineEdit(self.groupBox_ch17)
        self.check_message_14.setObjectName(u"check_message_14")
        sizePolicy1.setHeightForWidth(self.check_message_14.sizePolicy().hasHeightForWidth())
        self.check_message_14.setSizePolicy(sizePolicy1)
        self.check_message_14.setMinimumSize(QSize(170, 25))

        self.horizontalLayout_399.addWidget(self.check_message_14)


        self.verticalLayout_104.addLayout(self.horizontalLayout_399)


        self.horizontalLayout_395.addLayout(self.verticalLayout_104)


        self.verticalLayout_63.addWidget(self.groupBox_ch17)

        self.groupBox_ch18 = QGroupBox(self.scrollAreaWidgetContents_4)
        self.groupBox_ch18.setObjectName(u"groupBox_ch18")
        sizePolicy1.setHeightForWidth(self.groupBox_ch18.sizePolicy().hasHeightForWidth())
        self.groupBox_ch18.setSizePolicy(sizePolicy1)
        self.groupBox_ch18.setMinimumSize(QSize(600, 90))
        self.groupBox_ch18.setMaximumSize(QSize(16777215, 90))
        self.horizontalLayout_401 = QHBoxLayout(self.groupBox_ch18)
        self.horizontalLayout_401.setObjectName(u"horizontalLayout_401")
        self.verticalLayout_105 = QVBoxLayout()
        self.verticalLayout_105.setObjectName(u"verticalLayout_105")
        self.horizontalLayout_402 = QHBoxLayout()
        self.horizontalLayout_402.setObjectName(u"horizontalLayout_402")
        self.horizontalLayout_403 = QHBoxLayout()
        self.horizontalLayout_403.setObjectName(u"horizontalLayout_403")
        self.label_426 = QLabel(self.groupBox_ch18)
        self.label_426.setObjectName(u"label_426")
        sizePolicy2.setHeightForWidth(self.label_426.sizePolicy().hasHeightForWidth())
        self.label_426.setSizePolicy(sizePolicy2)
        self.label_426.setMinimumSize(QSize(15, 25))

        self.horizontalLayout_403.addWidget(self.label_426)

        self.check_if_15 = QLineEdit(self.groupBox_ch18)
        self.check_if_15.setObjectName(u"check_if_15")
        sizePolicy1.setHeightForWidth(self.check_if_15.sizePolicy().hasHeightForWidth())
        self.check_if_15.setSizePolicy(sizePolicy1)
        self.check_if_15.setMinimumSize(QSize(160, 25))

        self.horizontalLayout_403.addWidget(self.check_if_15)


        self.horizontalLayout_402.addLayout(self.horizontalLayout_403)

        self.horizontalLayout_404 = QHBoxLayout()
        self.horizontalLayout_404.setObjectName(u"horizontalLayout_404")
        self.label_427 = QLabel(self.groupBox_ch18)
        self.label_427.setObjectName(u"label_427")
        sizePolicy2.setHeightForWidth(self.label_427.sizePolicy().hasHeightForWidth())
        self.label_427.setSizePolicy(sizePolicy2)
        self.label_427.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_404.addWidget(self.label_427)

        self.check_check_15 = QLineEdit(self.groupBox_ch18)
        self.check_check_15.setObjectName(u"check_check_15")
        sizePolicy1.setHeightForWidth(self.check_check_15.sizePolicy().hasHeightForWidth())
        self.check_check_15.setSizePolicy(sizePolicy1)
        self.check_check_15.setMinimumSize(QSize(160, 25))

        self.horizontalLayout_404.addWidget(self.check_check_15)


        self.horizontalLayout_402.addLayout(self.horizontalLayout_404)


        self.verticalLayout_105.addLayout(self.horizontalLayout_402)

        self.horizontalLayout_405 = QHBoxLayout()
        self.horizontalLayout_405.setObjectName(u"horizontalLayout_405")
        self.label_428 = QLabel(self.groupBox_ch18)
        self.label_428.setObjectName(u"label_428")
        sizePolicy2.setHeightForWidth(self.label_428.sizePolicy().hasHeightForWidth())
        self.label_428.setSizePolicy(sizePolicy2)
        self.label_428.setMinimumSize(QSize(25, 25))
        self.label_428.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_405.addWidget(self.label_428)

        self.horizontalLayout_406 = QHBoxLayout()
        self.horizontalLayout_406.setObjectName(u"horizontalLayout_406")
        self.check_warning_15 = QRadioButton(self.groupBox_ch18)
        self.check_warning_15.setObjectName(u"check_warning_15")
        self.check_warning_15.setMinimumSize(QSize(100, 25))

        self.horizontalLayout_406.addWidget(self.check_warning_15)

        self.check_error_15 = QRadioButton(self.groupBox_ch18)
        self.check_error_15.setObjectName(u"check_error_15")
        self.check_error_15.setMinimumSize(QSize(100, 25))
        self.check_error_15.setChecked(True)

        self.horizontalLayout_406.addWidget(self.check_error_15)


        self.horizontalLayout_405.addLayout(self.horizontalLayout_406)

        self.check_message_15 = QLineEdit(self.groupBox_ch18)
        self.check_message_15.setObjectName(u"check_message_15")
        sizePolicy1.setHeightForWidth(self.check_message_15.sizePolicy().hasHeightForWidth())
        self.check_message_15.setSizePolicy(sizePolicy1)
        self.check_message_15.setMinimumSize(QSize(170, 25))

        self.horizontalLayout_405.addWidget(self.check_message_15)


        self.verticalLayout_105.addLayout(self.horizontalLayout_405)


        self.horizontalLayout_401.addLayout(self.verticalLayout_105)


        self.verticalLayout_63.addWidget(self.groupBox_ch18)

        self.groupBox_ch19 = QGroupBox(self.scrollAreaWidgetContents_4)
        self.groupBox_ch19.setObjectName(u"groupBox_ch19")
        sizePolicy1.setHeightForWidth(self.groupBox_ch19.sizePolicy().hasHeightForWidth())
        self.groupBox_ch19.setSizePolicy(sizePolicy1)
        self.groupBox_ch19.setMinimumSize(QSize(600, 90))
        self.groupBox_ch19.setMaximumSize(QSize(16777215, 90))
        self.horizontalLayout_407 = QHBoxLayout(self.groupBox_ch19)
        self.horizontalLayout_407.setObjectName(u"horizontalLayout_407")
        self.verticalLayout_106 = QVBoxLayout()
        self.verticalLayout_106.setObjectName(u"verticalLayout_106")
        self.horizontalLayout_408 = QHBoxLayout()
        self.horizontalLayout_408.setObjectName(u"horizontalLayout_408")
        self.horizontalLayout_409 = QHBoxLayout()
        self.horizontalLayout_409.setObjectName(u"horizontalLayout_409")
        self.label_429 = QLabel(self.groupBox_ch19)
        self.label_429.setObjectName(u"label_429")
        sizePolicy2.setHeightForWidth(self.label_429.sizePolicy().hasHeightForWidth())
        self.label_429.setSizePolicy(sizePolicy2)
        self.label_429.setMinimumSize(QSize(15, 25))

        self.horizontalLayout_409.addWidget(self.label_429)

        self.check_if_16 = QLineEdit(self.groupBox_ch19)
        self.check_if_16.setObjectName(u"check_if_16")
        sizePolicy1.setHeightForWidth(self.check_if_16.sizePolicy().hasHeightForWidth())
        self.check_if_16.setSizePolicy(sizePolicy1)
        self.check_if_16.setMinimumSize(QSize(160, 25))

        self.horizontalLayout_409.addWidget(self.check_if_16)


        self.horizontalLayout_408.addLayout(self.horizontalLayout_409)

        self.horizontalLayout_410 = QHBoxLayout()
        self.horizontalLayout_410.setObjectName(u"horizontalLayout_410")
        self.label_430 = QLabel(self.groupBox_ch19)
        self.label_430.setObjectName(u"label_430")
        sizePolicy2.setHeightForWidth(self.label_430.sizePolicy().hasHeightForWidth())
        self.label_430.setSizePolicy(sizePolicy2)
        self.label_430.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_410.addWidget(self.label_430)

        self.check_check_16 = QLineEdit(self.groupBox_ch19)
        self.check_check_16.setObjectName(u"check_check_16")
        sizePolicy1.setHeightForWidth(self.check_check_16.sizePolicy().hasHeightForWidth())
        self.check_check_16.setSizePolicy(sizePolicy1)
        self.check_check_16.setMinimumSize(QSize(160, 25))

        self.horizontalLayout_410.addWidget(self.check_check_16)


        self.horizontalLayout_408.addLayout(self.horizontalLayout_410)


        self.verticalLayout_106.addLayout(self.horizontalLayout_408)

        self.horizontalLayout_411 = QHBoxLayout()
        self.horizontalLayout_411.setObjectName(u"horizontalLayout_411")
        self.label_431 = QLabel(self.groupBox_ch19)
        self.label_431.setObjectName(u"label_431")
        sizePolicy2.setHeightForWidth(self.label_431.sizePolicy().hasHeightForWidth())
        self.label_431.setSizePolicy(sizePolicy2)
        self.label_431.setMinimumSize(QSize(25, 25))
        self.label_431.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_411.addWidget(self.label_431)

        self.horizontalLayout_412 = QHBoxLayout()
        self.horizontalLayout_412.setObjectName(u"horizontalLayout_412")
        self.check_warning_16 = QRadioButton(self.groupBox_ch19)
        self.check_warning_16.setObjectName(u"check_warning_16")
        self.check_warning_16.setMinimumSize(QSize(100, 25))

        self.horizontalLayout_412.addWidget(self.check_warning_16)

        self.check_error_16 = QRadioButton(self.groupBox_ch19)
        self.check_error_16.setObjectName(u"check_error_16")
        self.check_error_16.setMinimumSize(QSize(100, 25))
        self.check_error_16.setChecked(True)

        self.horizontalLayout_412.addWidget(self.check_error_16)


        self.horizontalLayout_411.addLayout(self.horizontalLayout_412)

        self.check_message_16 = QLineEdit(self.groupBox_ch19)
        self.check_message_16.setObjectName(u"check_message_16")
        sizePolicy1.setHeightForWidth(self.check_message_16.sizePolicy().hasHeightForWidth())
        self.check_message_16.setSizePolicy(sizePolicy1)
        self.check_message_16.setMinimumSize(QSize(170, 25))

        self.horizontalLayout_411.addWidget(self.check_message_16)


        self.verticalLayout_106.addLayout(self.horizontalLayout_411)


        self.horizontalLayout_407.addLayout(self.verticalLayout_106)


        self.verticalLayout_63.addWidget(self.groupBox_ch19)

        self.groupBox_ch20 = QGroupBox(self.scrollAreaWidgetContents_4)
        self.groupBox_ch20.setObjectName(u"groupBox_ch20")
        sizePolicy1.setHeightForWidth(self.groupBox_ch20.sizePolicy().hasHeightForWidth())
        self.groupBox_ch20.setSizePolicy(sizePolicy1)
        self.groupBox_ch20.setMinimumSize(QSize(600, 90))
        self.groupBox_ch20.setMaximumSize(QSize(16777215, 90))
        self.horizontalLayout_413 = QHBoxLayout(self.groupBox_ch20)
        self.horizontalLayout_413.setObjectName(u"horizontalLayout_413")
        self.verticalLayout_107 = QVBoxLayout()
        self.verticalLayout_107.setObjectName(u"verticalLayout_107")
        self.horizontalLayout_414 = QHBoxLayout()
        self.horizontalLayout_414.setObjectName(u"horizontalLayout_414")
        self.horizontalLayout_415 = QHBoxLayout()
        self.horizontalLayout_415.setObjectName(u"horizontalLayout_415")
        self.label_432 = QLabel(self.groupBox_ch20)
        self.label_432.setObjectName(u"label_432")
        sizePolicy2.setHeightForWidth(self.label_432.sizePolicy().hasHeightForWidth())
        self.label_432.setSizePolicy(sizePolicy2)
        self.label_432.setMinimumSize(QSize(15, 25))

        self.horizontalLayout_415.addWidget(self.label_432)

        self.check_if_17 = QLineEdit(self.groupBox_ch20)
        self.check_if_17.setObjectName(u"check_if_17")
        sizePolicy1.setHeightForWidth(self.check_if_17.sizePolicy().hasHeightForWidth())
        self.check_if_17.setSizePolicy(sizePolicy1)
        self.check_if_17.setMinimumSize(QSize(160, 25))

        self.horizontalLayout_415.addWidget(self.check_if_17)


        self.horizontalLayout_414.addLayout(self.horizontalLayout_415)

        self.horizontalLayout_416 = QHBoxLayout()
        self.horizontalLayout_416.setObjectName(u"horizontalLayout_416")
        self.label_433 = QLabel(self.groupBox_ch20)
        self.label_433.setObjectName(u"label_433")
        sizePolicy2.setHeightForWidth(self.label_433.sizePolicy().hasHeightForWidth())
        self.label_433.setSizePolicy(sizePolicy2)
        self.label_433.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_416.addWidget(self.label_433)

        self.check_check_17 = QLineEdit(self.groupBox_ch20)
        self.check_check_17.setObjectName(u"check_check_17")
        sizePolicy1.setHeightForWidth(self.check_check_17.sizePolicy().hasHeightForWidth())
        self.check_check_17.setSizePolicy(sizePolicy1)
        self.check_check_17.setMinimumSize(QSize(160, 25))

        self.horizontalLayout_416.addWidget(self.check_check_17)


        self.horizontalLayout_414.addLayout(self.horizontalLayout_416)


        self.verticalLayout_107.addLayout(self.horizontalLayout_414)

        self.horizontalLayout_417 = QHBoxLayout()
        self.horizontalLayout_417.setObjectName(u"horizontalLayout_417")
        self.label_434 = QLabel(self.groupBox_ch20)
        self.label_434.setObjectName(u"label_434")
        sizePolicy2.setHeightForWidth(self.label_434.sizePolicy().hasHeightForWidth())
        self.label_434.setSizePolicy(sizePolicy2)
        self.label_434.setMinimumSize(QSize(25, 25))
        self.label_434.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_417.addWidget(self.label_434)

        self.horizontalLayout_418 = QHBoxLayout()
        self.horizontalLayout_418.setObjectName(u"horizontalLayout_418")
        self.check_warning_17 = QRadioButton(self.groupBox_ch20)
        self.check_warning_17.setObjectName(u"check_warning_17")
        self.check_warning_17.setMinimumSize(QSize(100, 25))

        self.horizontalLayout_418.addWidget(self.check_warning_17)

        self.check_error_17 = QRadioButton(self.groupBox_ch20)
        self.check_error_17.setObjectName(u"check_error_17")
        self.check_error_17.setMinimumSize(QSize(100, 25))
        self.check_error_17.setChecked(True)

        self.horizontalLayout_418.addWidget(self.check_error_17)


        self.horizontalLayout_417.addLayout(self.horizontalLayout_418)

        self.check_message_17 = QLineEdit(self.groupBox_ch20)
        self.check_message_17.setObjectName(u"check_message_17")
        sizePolicy1.setHeightForWidth(self.check_message_17.sizePolicy().hasHeightForWidth())
        self.check_message_17.setSizePolicy(sizePolicy1)
        self.check_message_17.setMinimumSize(QSize(170, 25))

        self.horizontalLayout_417.addWidget(self.check_message_17)


        self.verticalLayout_107.addLayout(self.horizontalLayout_417)


        self.horizontalLayout_413.addLayout(self.verticalLayout_107)


        self.verticalLayout_63.addWidget(self.groupBox_ch20)

        self.groupBox_ch21 = QGroupBox(self.scrollAreaWidgetContents_4)
        self.groupBox_ch21.setObjectName(u"groupBox_ch21")
        sizePolicy1.setHeightForWidth(self.groupBox_ch21.sizePolicy().hasHeightForWidth())
        self.groupBox_ch21.setSizePolicy(sizePolicy1)
        self.groupBox_ch21.setMinimumSize(QSize(600, 90))
        self.groupBox_ch21.setMaximumSize(QSize(16777215, 90))
        self.horizontalLayout_419 = QHBoxLayout(self.groupBox_ch21)
        self.horizontalLayout_419.setObjectName(u"horizontalLayout_419")
        self.verticalLayout_108 = QVBoxLayout()
        self.verticalLayout_108.setObjectName(u"verticalLayout_108")
        self.horizontalLayout_420 = QHBoxLayout()
        self.horizontalLayout_420.setObjectName(u"horizontalLayout_420")
        self.horizontalLayout_421 = QHBoxLayout()
        self.horizontalLayout_421.setObjectName(u"horizontalLayout_421")
        self.label_435 = QLabel(self.groupBox_ch21)
        self.label_435.setObjectName(u"label_435")
        sizePolicy2.setHeightForWidth(self.label_435.sizePolicy().hasHeightForWidth())
        self.label_435.setSizePolicy(sizePolicy2)
        self.label_435.setMinimumSize(QSize(15, 25))

        self.horizontalLayout_421.addWidget(self.label_435)

        self.check_if_18 = QLineEdit(self.groupBox_ch21)
        self.check_if_18.setObjectName(u"check_if_18")
        sizePolicy1.setHeightForWidth(self.check_if_18.sizePolicy().hasHeightForWidth())
        self.check_if_18.setSizePolicy(sizePolicy1)
        self.check_if_18.setMinimumSize(QSize(160, 25))

        self.horizontalLayout_421.addWidget(self.check_if_18)


        self.horizontalLayout_420.addLayout(self.horizontalLayout_421)

        self.horizontalLayout_422 = QHBoxLayout()
        self.horizontalLayout_422.setObjectName(u"horizontalLayout_422")
        self.label_436 = QLabel(self.groupBox_ch21)
        self.label_436.setObjectName(u"label_436")
        sizePolicy2.setHeightForWidth(self.label_436.sizePolicy().hasHeightForWidth())
        self.label_436.setSizePolicy(sizePolicy2)
        self.label_436.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_422.addWidget(self.label_436)

        self.check_check_18 = QLineEdit(self.groupBox_ch21)
        self.check_check_18.setObjectName(u"check_check_18")
        sizePolicy1.setHeightForWidth(self.check_check_18.sizePolicy().hasHeightForWidth())
        self.check_check_18.setSizePolicy(sizePolicy1)
        self.check_check_18.setMinimumSize(QSize(160, 25))

        self.horizontalLayout_422.addWidget(self.check_check_18)


        self.horizontalLayout_420.addLayout(self.horizontalLayout_422)


        self.verticalLayout_108.addLayout(self.horizontalLayout_420)

        self.horizontalLayout_423 = QHBoxLayout()
        self.horizontalLayout_423.setObjectName(u"horizontalLayout_423")
        self.label_437 = QLabel(self.groupBox_ch21)
        self.label_437.setObjectName(u"label_437")
        sizePolicy2.setHeightForWidth(self.label_437.sizePolicy().hasHeightForWidth())
        self.label_437.setSizePolicy(sizePolicy2)
        self.label_437.setMinimumSize(QSize(25, 25))
        self.label_437.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_423.addWidget(self.label_437)

        self.horizontalLayout_424 = QHBoxLayout()
        self.horizontalLayout_424.setObjectName(u"horizontalLayout_424")
        self.check_warning_18 = QRadioButton(self.groupBox_ch21)
        self.check_warning_18.setObjectName(u"check_warning_18")
        self.check_warning_18.setMinimumSize(QSize(100, 25))

        self.horizontalLayout_424.addWidget(self.check_warning_18)

        self.check_error_18 = QRadioButton(self.groupBox_ch21)
        self.check_error_18.setObjectName(u"check_error_18")
        self.check_error_18.setMinimumSize(QSize(100, 25))
        self.check_error_18.setChecked(True)

        self.horizontalLayout_424.addWidget(self.check_error_18)


        self.horizontalLayout_423.addLayout(self.horizontalLayout_424)

        self.check_message_18 = QLineEdit(self.groupBox_ch21)
        self.check_message_18.setObjectName(u"check_message_18")
        sizePolicy1.setHeightForWidth(self.check_message_18.sizePolicy().hasHeightForWidth())
        self.check_message_18.setSizePolicy(sizePolicy1)
        self.check_message_18.setMinimumSize(QSize(170, 25))

        self.horizontalLayout_423.addWidget(self.check_message_18)


        self.verticalLayout_108.addLayout(self.horizontalLayout_423)


        self.horizontalLayout_419.addLayout(self.verticalLayout_108)


        self.verticalLayout_63.addWidget(self.groupBox_ch21)

        self.groupBox_ch11 = QGroupBox(self.scrollAreaWidgetContents_4)
        self.groupBox_ch11.setObjectName(u"groupBox_ch11")
        sizePolicy1.setHeightForWidth(self.groupBox_ch11.sizePolicy().hasHeightForWidth())
        self.groupBox_ch11.setSizePolicy(sizePolicy1)
        self.groupBox_ch11.setMinimumSize(QSize(600, 90))
        self.groupBox_ch11.setMaximumSize(QSize(16777215, 90))
        self.horizontalLayout_425 = QHBoxLayout(self.groupBox_ch11)
        self.horizontalLayout_425.setObjectName(u"horizontalLayout_425")
        self.verticalLayout_109 = QVBoxLayout()
        self.verticalLayout_109.setObjectName(u"verticalLayout_109")
        self.horizontalLayout_426 = QHBoxLayout()
        self.horizontalLayout_426.setObjectName(u"horizontalLayout_426")
        self.horizontalLayout_427 = QHBoxLayout()
        self.horizontalLayout_427.setObjectName(u"horizontalLayout_427")
        self.label_438 = QLabel(self.groupBox_ch11)
        self.label_438.setObjectName(u"label_438")
        sizePolicy2.setHeightForWidth(self.label_438.sizePolicy().hasHeightForWidth())
        self.label_438.setSizePolicy(sizePolicy2)
        self.label_438.setMinimumSize(QSize(15, 25))

        self.horizontalLayout_427.addWidget(self.label_438)

        self.check_if_19 = QLineEdit(self.groupBox_ch11)
        self.check_if_19.setObjectName(u"check_if_19")
        sizePolicy1.setHeightForWidth(self.check_if_19.sizePolicy().hasHeightForWidth())
        self.check_if_19.setSizePolicy(sizePolicy1)
        self.check_if_19.setMinimumSize(QSize(160, 25))

        self.horizontalLayout_427.addWidget(self.check_if_19)


        self.horizontalLayout_426.addLayout(self.horizontalLayout_427)

        self.horizontalLayout_428 = QHBoxLayout()
        self.horizontalLayout_428.setObjectName(u"horizontalLayout_428")
        self.label_439 = QLabel(self.groupBox_ch11)
        self.label_439.setObjectName(u"label_439")
        sizePolicy2.setHeightForWidth(self.label_439.sizePolicy().hasHeightForWidth())
        self.label_439.setSizePolicy(sizePolicy2)
        self.label_439.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_428.addWidget(self.label_439)

        self.check_check_19 = QLineEdit(self.groupBox_ch11)
        self.check_check_19.setObjectName(u"check_check_19")
        sizePolicy1.setHeightForWidth(self.check_check_19.sizePolicy().hasHeightForWidth())
        self.check_check_19.setSizePolicy(sizePolicy1)
        self.check_check_19.setMinimumSize(QSize(160, 25))

        self.horizontalLayout_428.addWidget(self.check_check_19)


        self.horizontalLayout_426.addLayout(self.horizontalLayout_428)


        self.verticalLayout_109.addLayout(self.horizontalLayout_426)

        self.horizontalLayout_429 = QHBoxLayout()
        self.horizontalLayout_429.setObjectName(u"horizontalLayout_429")
        self.label_440 = QLabel(self.groupBox_ch11)
        self.label_440.setObjectName(u"label_440")
        sizePolicy2.setHeightForWidth(self.label_440.sizePolicy().hasHeightForWidth())
        self.label_440.setSizePolicy(sizePolicy2)
        self.label_440.setMinimumSize(QSize(25, 25))
        self.label_440.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_429.addWidget(self.label_440)

        self.horizontalLayout_430 = QHBoxLayout()
        self.horizontalLayout_430.setObjectName(u"horizontalLayout_430")
        self.check_warning_19 = QRadioButton(self.groupBox_ch11)
        self.check_warning_19.setObjectName(u"check_warning_19")
        self.check_warning_19.setMinimumSize(QSize(100, 25))

        self.horizontalLayout_430.addWidget(self.check_warning_19)

        self.check_error_19 = QRadioButton(self.groupBox_ch11)
        self.check_error_19.setObjectName(u"check_error_19")
        self.check_error_19.setMinimumSize(QSize(100, 25))
        self.check_error_19.setChecked(True)

        self.horizontalLayout_430.addWidget(self.check_error_19)


        self.horizontalLayout_429.addLayout(self.horizontalLayout_430)

        self.check_message_19 = QLineEdit(self.groupBox_ch11)
        self.check_message_19.setObjectName(u"check_message_19")
        sizePolicy1.setHeightForWidth(self.check_message_19.sizePolicy().hasHeightForWidth())
        self.check_message_19.setSizePolicy(sizePolicy1)
        self.check_message_19.setMinimumSize(QSize(170, 25))

        self.horizontalLayout_429.addWidget(self.check_message_19)


        self.verticalLayout_109.addLayout(self.horizontalLayout_429)


        self.horizontalLayout_425.addLayout(self.verticalLayout_109)


        self.verticalLayout_63.addWidget(self.groupBox_ch11)

        self.groupBox_ch12 = QGroupBox(self.scrollAreaWidgetContents_4)
        self.groupBox_ch12.setObjectName(u"groupBox_ch12")
        sizePolicy1.setHeightForWidth(self.groupBox_ch12.sizePolicy().hasHeightForWidth())
        self.groupBox_ch12.setSizePolicy(sizePolicy1)
        self.groupBox_ch12.setMinimumSize(QSize(600, 90))
        self.groupBox_ch12.setMaximumSize(QSize(16777215, 90))
        self.horizontalLayout_431 = QHBoxLayout(self.groupBox_ch12)
        self.horizontalLayout_431.setObjectName(u"horizontalLayout_431")
        self.verticalLayout_110 = QVBoxLayout()
        self.verticalLayout_110.setObjectName(u"verticalLayout_110")
        self.horizontalLayout_432 = QHBoxLayout()
        self.horizontalLayout_432.setObjectName(u"horizontalLayout_432")
        self.horizontalLayout_433 = QHBoxLayout()
        self.horizontalLayout_433.setObjectName(u"horizontalLayout_433")
        self.label_441 = QLabel(self.groupBox_ch12)
        self.label_441.setObjectName(u"label_441")
        sizePolicy2.setHeightForWidth(self.label_441.sizePolicy().hasHeightForWidth())
        self.label_441.setSizePolicy(sizePolicy2)
        self.label_441.setMinimumSize(QSize(15, 25))

        self.horizontalLayout_433.addWidget(self.label_441)

        self.check_if_20 = QLineEdit(self.groupBox_ch12)
        self.check_if_20.setObjectName(u"check_if_20")
        sizePolicy1.setHeightForWidth(self.check_if_20.sizePolicy().hasHeightForWidth())
        self.check_if_20.setSizePolicy(sizePolicy1)
        self.check_if_20.setMinimumSize(QSize(160, 25))

        self.horizontalLayout_433.addWidget(self.check_if_20)


        self.horizontalLayout_432.addLayout(self.horizontalLayout_433)

        self.horizontalLayout_434 = QHBoxLayout()
        self.horizontalLayout_434.setObjectName(u"horizontalLayout_434")
        self.label_442 = QLabel(self.groupBox_ch12)
        self.label_442.setObjectName(u"label_442")
        sizePolicy2.setHeightForWidth(self.label_442.sizePolicy().hasHeightForWidth())
        self.label_442.setSizePolicy(sizePolicy2)
        self.label_442.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_434.addWidget(self.label_442)

        self.check_check_20 = QLineEdit(self.groupBox_ch12)
        self.check_check_20.setObjectName(u"check_check_20")
        sizePolicy1.setHeightForWidth(self.check_check_20.sizePolicy().hasHeightForWidth())
        self.check_check_20.setSizePolicy(sizePolicy1)
        self.check_check_20.setMinimumSize(QSize(160, 25))

        self.horizontalLayout_434.addWidget(self.check_check_20)


        self.horizontalLayout_432.addLayout(self.horizontalLayout_434)


        self.verticalLayout_110.addLayout(self.horizontalLayout_432)

        self.horizontalLayout_435 = QHBoxLayout()
        self.horizontalLayout_435.setObjectName(u"horizontalLayout_435")
        self.label_443 = QLabel(self.groupBox_ch12)
        self.label_443.setObjectName(u"label_443")
        sizePolicy2.setHeightForWidth(self.label_443.sizePolicy().hasHeightForWidth())
        self.label_443.setSizePolicy(sizePolicy2)
        self.label_443.setMinimumSize(QSize(25, 25))
        self.label_443.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_435.addWidget(self.label_443)

        self.horizontalLayout_436 = QHBoxLayout()
        self.horizontalLayout_436.setObjectName(u"horizontalLayout_436")
        self.check_warning_20 = QRadioButton(self.groupBox_ch12)
        self.check_warning_20.setObjectName(u"check_warning_20")
        self.check_warning_20.setMinimumSize(QSize(100, 25))

        self.horizontalLayout_436.addWidget(self.check_warning_20)

        self.check_error_20 = QRadioButton(self.groupBox_ch12)
        self.check_error_20.setObjectName(u"check_error_20")
        self.check_error_20.setMinimumSize(QSize(100, 25))
        self.check_error_20.setChecked(True)

        self.horizontalLayout_436.addWidget(self.check_error_20)


        self.horizontalLayout_435.addLayout(self.horizontalLayout_436)

        self.check_message_20 = QLineEdit(self.groupBox_ch12)
        self.check_message_20.setObjectName(u"check_message_20")
        sizePolicy1.setHeightForWidth(self.check_message_20.sizePolicy().hasHeightForWidth())
        self.check_message_20.setSizePolicy(sizePolicy1)
        self.check_message_20.setMinimumSize(QSize(170, 25))

        self.horizontalLayout_435.addWidget(self.check_message_20)


        self.verticalLayout_110.addLayout(self.horizontalLayout_435)


        self.horizontalLayout_431.addLayout(self.verticalLayout_110)


        self.verticalLayout_63.addWidget(self.groupBox_ch12)

        self.groupBox_ch13 = QGroupBox(self.scrollAreaWidgetContents_4)
        self.groupBox_ch13.setObjectName(u"groupBox_ch13")
        sizePolicy1.setHeightForWidth(self.groupBox_ch13.sizePolicy().hasHeightForWidth())
        self.groupBox_ch13.setSizePolicy(sizePolicy1)
        self.groupBox_ch13.setMinimumSize(QSize(600, 90))
        self.groupBox_ch13.setMaximumSize(QSize(16777215, 90))
        self.horizontalLayout_437 = QHBoxLayout(self.groupBox_ch13)
        self.horizontalLayout_437.setObjectName(u"horizontalLayout_437")
        self.verticalLayout_111 = QVBoxLayout()
        self.verticalLayout_111.setObjectName(u"verticalLayout_111")
        self.horizontalLayout_438 = QHBoxLayout()
        self.horizontalLayout_438.setObjectName(u"horizontalLayout_438")
        self.horizontalLayout_439 = QHBoxLayout()
        self.horizontalLayout_439.setObjectName(u"horizontalLayout_439")
        self.label_444 = QLabel(self.groupBox_ch13)
        self.label_444.setObjectName(u"label_444")
        sizePolicy2.setHeightForWidth(self.label_444.sizePolicy().hasHeightForWidth())
        self.label_444.setSizePolicy(sizePolicy2)
        self.label_444.setMinimumSize(QSize(15, 25))

        self.horizontalLayout_439.addWidget(self.label_444)

        self.check_if_21 = QLineEdit(self.groupBox_ch13)
        self.check_if_21.setObjectName(u"check_if_21")
        sizePolicy1.setHeightForWidth(self.check_if_21.sizePolicy().hasHeightForWidth())
        self.check_if_21.setSizePolicy(sizePolicy1)
        self.check_if_21.setMinimumSize(QSize(160, 25))

        self.horizontalLayout_439.addWidget(self.check_if_21)


        self.horizontalLayout_438.addLayout(self.horizontalLayout_439)

        self.horizontalLayout_440 = QHBoxLayout()
        self.horizontalLayout_440.setObjectName(u"horizontalLayout_440")
        self.label_445 = QLabel(self.groupBox_ch13)
        self.label_445.setObjectName(u"label_445")
        sizePolicy2.setHeightForWidth(self.label_445.sizePolicy().hasHeightForWidth())
        self.label_445.setSizePolicy(sizePolicy2)
        self.label_445.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_440.addWidget(self.label_445)

        self.check_check_21 = QLineEdit(self.groupBox_ch13)
        self.check_check_21.setObjectName(u"check_check_21")
        sizePolicy1.setHeightForWidth(self.check_check_21.sizePolicy().hasHeightForWidth())
        self.check_check_21.setSizePolicy(sizePolicy1)
        self.check_check_21.setMinimumSize(QSize(160, 25))

        self.horizontalLayout_440.addWidget(self.check_check_21)


        self.horizontalLayout_438.addLayout(self.horizontalLayout_440)


        self.verticalLayout_111.addLayout(self.horizontalLayout_438)

        self.horizontalLayout_441 = QHBoxLayout()
        self.horizontalLayout_441.setObjectName(u"horizontalLayout_441")
        self.label_446 = QLabel(self.groupBox_ch13)
        self.label_446.setObjectName(u"label_446")
        sizePolicy2.setHeightForWidth(self.label_446.sizePolicy().hasHeightForWidth())
        self.label_446.setSizePolicy(sizePolicy2)
        self.label_446.setMinimumSize(QSize(25, 25))
        self.label_446.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_441.addWidget(self.label_446)

        self.horizontalLayout_442 = QHBoxLayout()
        self.horizontalLayout_442.setObjectName(u"horizontalLayout_442")
        self.check_warning_21 = QRadioButton(self.groupBox_ch13)
        self.check_warning_21.setObjectName(u"check_warning_21")
        self.check_warning_21.setMinimumSize(QSize(100, 25))

        self.horizontalLayout_442.addWidget(self.check_warning_21)

        self.check_error_21 = QRadioButton(self.groupBox_ch13)
        self.check_error_21.setObjectName(u"check_error_21")
        self.check_error_21.setMinimumSize(QSize(100, 25))
        self.check_error_21.setChecked(True)

        self.horizontalLayout_442.addWidget(self.check_error_21)


        self.horizontalLayout_441.addLayout(self.horizontalLayout_442)

        self.check_message_21 = QLineEdit(self.groupBox_ch13)
        self.check_message_21.setObjectName(u"check_message_21")
        sizePolicy1.setHeightForWidth(self.check_message_21.sizePolicy().hasHeightForWidth())
        self.check_message_21.setSizePolicy(sizePolicy1)
        self.check_message_21.setMinimumSize(QSize(170, 25))

        self.horizontalLayout_441.addWidget(self.check_message_21)


        self.verticalLayout_111.addLayout(self.horizontalLayout_441)


        self.horizontalLayout_437.addLayout(self.verticalLayout_111)


        self.verticalLayout_63.addWidget(self.groupBox_ch13)


        self.verticalLayout_48.addLayout(self.verticalLayout_63)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_67.addWidget(self.scrollArea_3)


        self.verticalLayout_68.addLayout(self.verticalLayout_67)

        self.TopTab.addTab(self.tab_12, "")
        self.tab_24 = QWidget()
        self.tab_24.setObjectName(u"tab_24")
        self.verticalLayout_91 = QVBoxLayout(self.tab_24)
        self.verticalLayout_91.setObjectName(u"verticalLayout_91")
        self.horizontalLayout_191 = QHBoxLayout()
        self.horizontalLayout_191.setObjectName(u"horizontalLayout_191")
        self.verticalLayout_92 = QVBoxLayout()
        self.verticalLayout_92.setObjectName(u"verticalLayout_92")
        self.groupBox_27 = QGroupBox(self.tab_24)
        self.groupBox_27.setObjectName(u"groupBox_27")
        self.verticalLayout_79 = QVBoxLayout(self.groupBox_27)
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.verticalLayout_78 = QVBoxLayout()
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.horizontalLayout_181 = QHBoxLayout()
        self.horizontalLayout_181.setObjectName(u"horizontalLayout_181")
        self.label_279 = QLabel(self.groupBox_27)
        self.label_279.setObjectName(u"label_279")
        sizePolicy2.setHeightForWidth(self.label_279.sizePolicy().hasHeightForWidth())
        self.label_279.setSizePolicy(sizePolicy2)
        self.label_279.setMinimumSize(QSize(90, 25))
        self.label_279.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_181.addWidget(self.label_279)

        self.dead_primpool = QLineEdit(self.groupBox_27)
        self.dead_primpool.setObjectName(u"dead_primpool")
        sizePolicy2.setHeightForWidth(self.dead_primpool.sizePolicy().hasHeightForWidth())
        self.dead_primpool.setSizePolicy(sizePolicy2)
        self.dead_primpool.setMinimumSize(QSize(100, 25))
        self.dead_primpool.setMaximumSize(QSize(150, 16777215))
        self.dead_primpool.setReadOnly(False)

        self.horizontalLayout_181.addWidget(self.dead_primpool)


        self.verticalLayout_78.addLayout(self.horizontalLayout_181)

        self.horizontalLayout_182 = QHBoxLayout()
        self.horizontalLayout_182.setObjectName(u"horizontalLayout_182")
        self.label_312 = QLabel(self.groupBox_27)
        self.label_312.setObjectName(u"label_312")
        sizePolicy2.setHeightForWidth(self.label_312.sizePolicy().hasHeightForWidth())
        self.label_312.setSizePolicy(sizePolicy2)
        self.label_312.setMinimumSize(QSize(90, 25))
        self.label_312.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_182.addWidget(self.label_312)

        self.dead_secpool = QLineEdit(self.groupBox_27)
        self.dead_secpool.setObjectName(u"dead_secpool")
        sizePolicy2.setHeightForWidth(self.dead_secpool.sizePolicy().hasHeightForWidth())
        self.dead_secpool.setSizePolicy(sizePolicy2)
        self.dead_secpool.setMinimumSize(QSize(100, 25))
        self.dead_secpool.setMaximumSize(QSize(150, 16777215))
        self.dead_secpool.setReadOnly(False)

        self.horizontalLayout_182.addWidget(self.dead_secpool)


        self.verticalLayout_78.addLayout(self.horizontalLayout_182)

        self.horizontalLayout_183 = QHBoxLayout()
        self.horizontalLayout_183.setObjectName(u"horizontalLayout_183")
        self.label_313 = QLabel(self.groupBox_27)
        self.label_313.setObjectName(u"label_313")
        sizePolicy2.setHeightForWidth(self.label_313.sizePolicy().hasHeightForWidth())
        self.label_313.setSizePolicy(sizePolicy2)
        self.label_313.setMinimumSize(QSize(90, 25))
        self.label_313.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_183.addWidget(self.label_313)

        self.dead_group = QLineEdit(self.groupBox_27)
        self.dead_group.setObjectName(u"dead_group")
        sizePolicy2.setHeightForWidth(self.dead_group.sizePolicy().hasHeightForWidth())
        self.dead_group.setSizePolicy(sizePolicy2)
        self.dead_group.setMinimumSize(QSize(100, 25))
        self.dead_group.setMaximumSize(QSize(150, 16777215))
        self.dead_group.setReadOnly(False)

        self.horizontalLayout_183.addWidget(self.dead_group)


        self.verticalLayout_78.addLayout(self.horizontalLayout_183)

        self.horizontalLayout_184 = QHBoxLayout()
        self.horizontalLayout_184.setObjectName(u"horizontalLayout_184")
        self.label_314 = QLabel(self.groupBox_27)
        self.label_314.setObjectName(u"label_314")
        sizePolicy2.setHeightForWidth(self.label_314.sizePolicy().hasHeightForWidth())
        self.label_314.setSizePolicy(sizePolicy2)
        self.label_314.setMinimumSize(QSize(90, 25))
        self.label_314.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_184.addWidget(self.label_314)

        self.dead_priority = QLineEdit(self.groupBox_27)
        self.dead_priority.setObjectName(u"dead_priority")
        sizePolicy2.setHeightForWidth(self.dead_priority.sizePolicy().hasHeightForWidth())
        self.dead_priority.setSizePolicy(sizePolicy2)
        self.dead_priority.setMinimumSize(QSize(100, 25))
        self.dead_priority.setMaximumSize(QSize(150, 16777215))
        self.dead_priority.setReadOnly(False)

        self.horizontalLayout_184.addWidget(self.dead_priority)


        self.verticalLayout_78.addLayout(self.horizontalLayout_184)

        self.horizontalLayout_185 = QHBoxLayout()
        self.horizontalLayout_185.setObjectName(u"horizontalLayout_185")
        self.label_315 = QLabel(self.groupBox_27)
        self.label_315.setObjectName(u"label_315")
        sizePolicy2.setHeightForWidth(self.label_315.sizePolicy().hasHeightForWidth())
        self.label_315.setSizePolicy(sizePolicy2)
        self.label_315.setMinimumSize(QSize(90, 25))
        self.label_315.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_185.addWidget(self.label_315)

        self.dead_limits = QLineEdit(self.groupBox_27)
        self.dead_limits.setObjectName(u"dead_limits")
        sizePolicy2.setHeightForWidth(self.dead_limits.sizePolicy().hasHeightForWidth())
        self.dead_limits.setSizePolicy(sizePolicy2)
        self.dead_limits.setMinimumSize(QSize(100, 25))
        self.dead_limits.setMaximumSize(QSize(150, 16777215))
        self.dead_limits.setReadOnly(False)

        self.horizontalLayout_185.addWidget(self.dead_limits)


        self.verticalLayout_78.addLayout(self.horizontalLayout_185)

        self.horizontalLayout_186 = QHBoxLayout()
        self.horizontalLayout_186.setObjectName(u"horizontalLayout_186")
        self.label_316 = QLabel(self.groupBox_27)
        self.label_316.setObjectName(u"label_316")
        sizePolicy2.setHeightForWidth(self.label_316.sizePolicy().hasHeightForWidth())
        self.label_316.setSizePolicy(sizePolicy2)
        self.label_316.setMinimumSize(QSize(90, 25))
        self.label_316.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_186.addWidget(self.label_316)

        self.dead_limits_2 = QLineEdit(self.groupBox_27)
        self.dead_limits_2.setObjectName(u"dead_limits_2")
        sizePolicy2.setHeightForWidth(self.dead_limits_2.sizePolicy().hasHeightForWidth())
        self.dead_limits_2.setSizePolicy(sizePolicy2)
        self.dead_limits_2.setMinimumSize(QSize(100, 25))
        self.dead_limits_2.setMaximumSize(QSize(150, 16777215))
        self.dead_limits_2.setReadOnly(False)

        self.horizontalLayout_186.addWidget(self.dead_limits_2)


        self.verticalLayout_78.addLayout(self.horizontalLayout_186)

        self.horizontalLayout_187 = QHBoxLayout()
        self.horizontalLayout_187.setObjectName(u"horizontalLayout_187")
        self.label_317 = QLabel(self.groupBox_27)
        self.label_317.setObjectName(u"label_317")
        sizePolicy2.setHeightForWidth(self.label_317.sizePolicy().hasHeightForWidth())
        self.label_317.setSizePolicy(sizePolicy2)
        self.label_317.setMinimumSize(QSize(90, 25))
        self.label_317.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_187.addWidget(self.label_317)

        self.dead_department = QLineEdit(self.groupBox_27)
        self.dead_department.setObjectName(u"dead_department")
        sizePolicy2.setHeightForWidth(self.dead_department.sizePolicy().hasHeightForWidth())
        self.dead_department.setSizePolicy(sizePolicy2)
        self.dead_department.setMinimumSize(QSize(100, 25))
        self.dead_department.setMaximumSize(QSize(150, 16777215))
        self.dead_department.setReadOnly(False)

        self.horizontalLayout_187.addWidget(self.dead_department)


        self.verticalLayout_78.addLayout(self.horizontalLayout_187)


        self.verticalLayout_79.addLayout(self.verticalLayout_78)


        self.verticalLayout_92.addWidget(self.groupBox_27)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_92.addItem(self.verticalSpacer_7)


        self.horizontalLayout_191.addLayout(self.verticalLayout_92)

        self.verticalLayout_81 = QVBoxLayout()
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.groupBox_28 = QGroupBox(self.tab_24)
        self.groupBox_28.setObjectName(u"groupBox_28")
        sizePolicy.setHeightForWidth(self.groupBox_28.sizePolicy().hasHeightForWidth())
        self.groupBox_28.setSizePolicy(sizePolicy)
        self.groupBox_28.setMinimumSize(QSize(275, 200))
        self.horizontalLayout_188 = QHBoxLayout(self.groupBox_28)
        self.horizontalLayout_188.setObjectName(u"horizontalLayout_188")
        self.verticalLayout_80 = QVBoxLayout()
        self.verticalLayout_80.setObjectName(u"verticalLayout_80")
        self.dead_go_ayon = QCheckBox(self.groupBox_28)
        self.dead_go_ayon.setObjectName(u"dead_go_ayon")
        sizePolicy2.setHeightForWidth(self.dead_go_ayon.sizePolicy().hasHeightForWidth())
        self.dead_go_ayon.setSizePolicy(sizePolicy2)
        self.dead_go_ayon.setMinimumSize(QSize(240, 25))
        self.dead_go_ayon.setMaximumSize(QSize(240, 25))
        self.dead_go_ayon.setChecked(True)

        self.verticalLayout_80.addWidget(self.dead_go_ayon)

        self.horizontalLayout_189 = QHBoxLayout()
        self.horizontalLayout_189.setObjectName(u"horizontalLayout_189")
        self.label_328 = QLabel(self.groupBox_28)
        self.label_328.setObjectName(u"label_328")
        sizePolicy2.setHeightForWidth(self.label_328.sizePolicy().hasHeightForWidth())
        self.label_328.setSizePolicy(sizePolicy2)
        self.label_328.setMinimumSize(QSize(50, 25))
        self.label_328.setMaximumSize(QSize(50, 25))

        self.horizontalLayout_189.addWidget(self.label_328)

        self.dead_ayon_folder = QLineEdit(self.groupBox_28)
        self.dead_ayon_folder.setObjectName(u"dead_ayon_folder")
        sizePolicy2.setHeightForWidth(self.dead_ayon_folder.sizePolicy().hasHeightForWidth())
        self.dead_ayon_folder.setSizePolicy(sizePolicy2)
        self.dead_ayon_folder.setMinimumSize(QSize(150, 25))
        self.dead_ayon_folder.setMaximumSize(QSize(300, 25))
        self.dead_ayon_folder.setDragEnabled(True)

        self.horizontalLayout_189.addWidget(self.dead_ayon_folder)


        self.verticalLayout_80.addLayout(self.horizontalLayout_189)

        self.horizontalLayout_190 = QHBoxLayout()
        self.horizontalLayout_190.setObjectName(u"horizontalLayout_190")
        self.label_329 = QLabel(self.groupBox_28)
        self.label_329.setObjectName(u"label_329")
        sizePolicy2.setHeightForWidth(self.label_329.sizePolicy().hasHeightForWidth())
        self.label_329.setSizePolicy(sizePolicy2)
        self.label_329.setMinimumSize(QSize(50, 25))
        self.label_329.setMaximumSize(QSize(50, 25))

        self.horizontalLayout_190.addWidget(self.label_329)

        self.dead_ayon_task = QLineEdit(self.groupBox_28)
        self.dead_ayon_task.setObjectName(u"dead_ayon_task")
        sizePolicy2.setHeightForWidth(self.dead_ayon_task.sizePolicy().hasHeightForWidth())
        self.dead_ayon_task.setSizePolicy(sizePolicy2)
        self.dead_ayon_task.setMinimumSize(QSize(150, 25))
        self.dead_ayon_task.setMaximumSize(QSize(300, 25))
        self.dead_ayon_task.setDragEnabled(True)

        self.horizontalLayout_190.addWidget(self.dead_ayon_task)


        self.verticalLayout_80.addLayout(self.horizontalLayout_190)


        self.horizontalLayout_188.addLayout(self.verticalLayout_80)


        self.verticalLayout_81.addWidget(self.groupBox_28)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_81.addItem(self.verticalSpacer_2)


        self.horizontalLayout_191.addLayout(self.verticalLayout_81)

        self.horizontalSpacer_31 = QSpacerItem(468, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_191.addItem(self.horizontalSpacer_31)


        self.verticalLayout_91.addLayout(self.horizontalLayout_191)

        self.TopTab.addTab(self.tab_24, "")
        self.tab_25 = QWidget()
        self.tab_25.setObjectName(u"tab_25")
        self.verticalLayout_119 = QVBoxLayout(self.tab_25)
        self.verticalLayout_119.setObjectName(u"verticalLayout_119")
        self.verticalLayout_118 = QVBoxLayout()
        self.verticalLayout_118.setObjectName(u"verticalLayout_118")
        self.horizontalLayout_195 = QHBoxLayout()
        self.horizontalLayout_195.setObjectName(u"horizontalLayout_195")
        self.verticalLayout_116 = QVBoxLayout()
        self.verticalLayout_116.setObjectName(u"verticalLayout_116")
        self.horizontalLayout_194 = QHBoxLayout()
        self.horizontalLayout_194.setObjectName(u"horizontalLayout_194")
        self.groupBox_30 = QGroupBox(self.tab_25)
        self.groupBox_30.setObjectName(u"groupBox_30")
        self.verticalLayout_112 = QVBoxLayout(self.groupBox_30)
        self.verticalLayout_112.setObjectName(u"verticalLayout_112")
        self.verticalLayout_99 = QVBoxLayout()
        self.verticalLayout_99.setObjectName(u"verticalLayout_99")
        self.ayon_do_shotlist = QCheckBox(self.groupBox_30)
        self.ayon_do_shotlist.setObjectName(u"ayon_do_shotlist")
        sizePolicy2.setHeightForWidth(self.ayon_do_shotlist.sizePolicy().hasHeightForWidth())
        self.ayon_do_shotlist.setSizePolicy(sizePolicy2)
        self.ayon_do_shotlist.setMinimumSize(QSize(100, 25))
        self.ayon_do_shotlist.setMaximumSize(QSize(100, 25))

        self.verticalLayout_99.addWidget(self.ayon_do_shotlist)

        self.horizontalLayout_193 = QHBoxLayout()
        self.horizontalLayout_193.setObjectName(u"horizontalLayout_193")
        self.label_322 = QLabel(self.groupBox_30)
        self.label_322.setObjectName(u"label_322")
        sizePolicy2.setHeightForWidth(self.label_322.sizePolicy().hasHeightForWidth())
        self.label_322.setSizePolicy(sizePolicy2)
        self.label_322.setMinimumSize(QSize(50, 25))
        self.label_322.setMaximumSize(QSize(50, 25))

        self.horizontalLayout_193.addWidget(self.label_322)

        self.ayon_project = QLineEdit(self.groupBox_30)
        self.ayon_project.setObjectName(u"ayon_project")
        sizePolicy5.setHeightForWidth(self.ayon_project.sizePolicy().hasHeightForWidth())
        self.ayon_project.setSizePolicy(sizePolicy5)
        self.ayon_project.setMinimumSize(QSize(200, 25))
        self.ayon_project.setMaximumSize(QSize(2000, 25))
        self.ayon_project.setDragEnabled(True)

        self.horizontalLayout_193.addWidget(self.ayon_project)


        self.verticalLayout_99.addLayout(self.horizontalLayout_193)


        self.verticalLayout_112.addLayout(self.verticalLayout_99)


        self.horizontalLayout_194.addWidget(self.groupBox_30)

        self.groupBox_32 = QGroupBox(self.tab_25)
        self.groupBox_32.setObjectName(u"groupBox_32")
        self.verticalLayout_98 = QVBoxLayout(self.groupBox_32)
        self.verticalLayout_98.setObjectName(u"verticalLayout_98")
        self.verticalLayout_96 = QVBoxLayout()
        self.verticalLayout_96.setObjectName(u"verticalLayout_96")
        self.horizontalLayout_68 = QHBoxLayout()
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.ayon_export_csv = QCheckBox(self.groupBox_32)
        self.ayon_export_csv.setObjectName(u"ayon_export_csv")
        sizePolicy2.setHeightForWidth(self.ayon_export_csv.sizePolicy().hasHeightForWidth())
        self.ayon_export_csv.setSizePolicy(sizePolicy2)
        self.ayon_export_csv.setMinimumSize(QSize(100, 25))
        self.ayon_export_csv.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_68.addWidget(self.ayon_export_csv)

        self.ayon_export_excel = QCheckBox(self.groupBox_32)
        self.ayon_export_excel.setObjectName(u"ayon_export_excel")
        sizePolicy2.setHeightForWidth(self.ayon_export_excel.sizePolicy().hasHeightForWidth())
        self.ayon_export_excel.setSizePolicy(sizePolicy2)
        self.ayon_export_excel.setMinimumSize(QSize(100, 25))
        self.ayon_export_excel.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_68.addWidget(self.ayon_export_excel)

        self.ayon_thumbnails = QCheckBox(self.groupBox_32)
        self.ayon_thumbnails.setObjectName(u"ayon_thumbnails")
        sizePolicy2.setHeightForWidth(self.ayon_thumbnails.sizePolicy().hasHeightForWidth())
        self.ayon_thumbnails.setSizePolicy(sizePolicy2)
        self.ayon_thumbnails.setMinimumSize(QSize(100, 25))
        self.ayon_thumbnails.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_68.addWidget(self.ayon_thumbnails)

        self.horizontalLayout_206 = QHBoxLayout()
        self.horizontalLayout_206.setObjectName(u"horizontalLayout_206")
        self.label_323 = QLabel(self.groupBox_32)
        self.label_323.setObjectName(u"label_323")
        sizePolicy2.setHeightForWidth(self.label_323.sizePolicy().hasHeightForWidth())
        self.label_323.setSizePolicy(sizePolicy2)
        self.label_323.setMinimumSize(QSize(90, 25))
        self.label_323.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_206.addWidget(self.label_323)

        self.ayon_prefix = QLineEdit(self.groupBox_32)
        self.ayon_prefix.setObjectName(u"ayon_prefix")
        sizePolicy2.setHeightForWidth(self.ayon_prefix.sizePolicy().hasHeightForWidth())
        self.ayon_prefix.setSizePolicy(sizePolicy2)
        self.ayon_prefix.setMinimumSize(QSize(100, 25))
        self.ayon_prefix.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_206.addWidget(self.ayon_prefix)


        self.horizontalLayout_68.addLayout(self.horizontalLayout_206)


        self.verticalLayout_96.addLayout(self.horizontalLayout_68)

        self.horizontalLayout_112 = QHBoxLayout()
        self.horizontalLayout_112.setObjectName(u"horizontalLayout_112")
        self.label_28 = QLabel(self.groupBox_32)
        self.label_28.setObjectName(u"label_28")
        sizePolicy2.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy2)
        self.label_28.setMinimumSize(QSize(50, 25))
        self.label_28.setMaximumSize(QSize(50, 25))

        self.horizontalLayout_112.addWidget(self.label_28)

        self.ayon_output_folder = QLineEdit(self.groupBox_32)
        self.ayon_output_folder.setObjectName(u"ayon_output_folder")
        sizePolicy5.setHeightForWidth(self.ayon_output_folder.sizePolicy().hasHeightForWidth())
        self.ayon_output_folder.setSizePolicy(sizePolicy5)
        self.ayon_output_folder.setMinimumSize(QSize(420, 25))
        self.ayon_output_folder.setMaximumSize(QSize(420, 16777215))
        self.ayon_output_folder.setDragEnabled(True)

        self.horizontalLayout_112.addWidget(self.ayon_output_folder)

        self.ayon_path_browse_2 = QPushButton(self.groupBox_32)
        self.ayon_path_browse_2.setObjectName(u"ayon_path_browse_2")
        sizePolicy2.setHeightForWidth(self.ayon_path_browse_2.sizePolicy().hasHeightForWidth())
        self.ayon_path_browse_2.setSizePolicy(sizePolicy2)
        self.ayon_path_browse_2.setMinimumSize(QSize(30, 25))
        self.ayon_path_browse_2.setMaximumSize(QSize(60, 25))
        self.ayon_path_browse_2.setAutoFillBackground(False)
        self.ayon_path_browse_2.setIcon(icon)
        self.ayon_path_browse_2.setFlat(True)

        self.horizontalLayout_112.addWidget(self.ayon_path_browse_2)


        self.verticalLayout_96.addLayout(self.horizontalLayout_112)


        self.verticalLayout_98.addLayout(self.verticalLayout_96)


        self.horizontalLayout_194.addWidget(self.groupBox_32)


        self.verticalLayout_116.addLayout(self.horizontalLayout_194)

        self.groupBox_33 = QGroupBox(self.tab_25)
        self.groupBox_33.setObjectName(u"groupBox_33")
        sizePolicy6.setHeightForWidth(self.groupBox_33.sizePolicy().hasHeightForWidth())
        self.groupBox_33.setSizePolicy(sizePolicy6)
        self.groupBox_33.setMinimumSize(QSize(350, 50))
        self.groupBox_33.setMaximumSize(QSize(16777215, 50))
        self.verticalLayout_113 = QVBoxLayout(self.groupBox_33)
        self.verticalLayout_113.setObjectName(u"verticalLayout_113")
        self.horizontalLayout_196 = QHBoxLayout()
        self.horizontalLayout_196.setObjectName(u"horizontalLayout_196")
        self.horizontalLayout_197 = QHBoxLayout()
        self.horizontalLayout_197.setObjectName(u"horizontalLayout_197")
        self.horizontalLayout_198 = QHBoxLayout()
        self.horizontalLayout_198.setObjectName(u"horizontalLayout_198")
        self.ayon_package1_chbx = QCheckBox(self.groupBox_33)
        self.ayon_package1_chbx.setObjectName(u"ayon_package1_chbx")
        self.ayon_package1_chbx.setMinimumSize(QSize(80, 25))
        self.ayon_package1_chbx.setMaximumSize(QSize(80, 16777215))
        self.ayon_package1_chbx.setChecked(True)

        self.horizontalLayout_198.addWidget(self.ayon_package1_chbx)

        self.ayon_package1 = QLineEdit(self.groupBox_33)
        self.ayon_package1.setObjectName(u"ayon_package1")
        sizePolicy1.setHeightForWidth(self.ayon_package1.sizePolicy().hasHeightForWidth())
        self.ayon_package1.setSizePolicy(sizePolicy1)
        self.ayon_package1.setMinimumSize(QSize(50, 25))
        self.ayon_package1.setMaximumSize(QSize(400, 16777215))
        self.ayon_package1.setReadOnly(False)

        self.horizontalLayout_198.addWidget(self.ayon_package1)


        self.horizontalLayout_197.addLayout(self.horizontalLayout_198)

        self.horizontalLayout_199 = QHBoxLayout()
        self.horizontalLayout_199.setObjectName(u"horizontalLayout_199")
        self.label_324 = QLabel(self.groupBox_33)
        self.label_324.setObjectName(u"label_324")
        sizePolicy2.setHeightForWidth(self.label_324.sizePolicy().hasHeightForWidth())
        self.label_324.setSizePolicy(sizePolicy2)
        self.label_324.setMinimumSize(QSize(40, 25))
        self.label_324.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_199.addWidget(self.label_324)

        self.ayon_list1 = QLineEdit(self.groupBox_33)
        self.ayon_list1.setObjectName(u"ayon_list1")
        sizePolicy1.setHeightForWidth(self.ayon_list1.sizePolicy().hasHeightForWidth())
        self.ayon_list1.setSizePolicy(sizePolicy1)
        self.ayon_list1.setMinimumSize(QSize(50, 25))
        self.ayon_list1.setMaximumSize(QSize(400, 16777215))
        self.ayon_list1.setReadOnly(False)

        self.horizontalLayout_199.addWidget(self.ayon_list1)


        self.horizontalLayout_197.addLayout(self.horizontalLayout_199)


        self.horizontalLayout_196.addLayout(self.horizontalLayout_197)

        self.horizontalLayout_200 = QHBoxLayout()
        self.horizontalLayout_200.setObjectName(u"horizontalLayout_200")
        self.horizontalLayout_201 = QHBoxLayout()
        self.horizontalLayout_201.setObjectName(u"horizontalLayout_201")
        self.ayon_package2_chbx = QCheckBox(self.groupBox_33)
        self.ayon_package2_chbx.setObjectName(u"ayon_package2_chbx")
        self.ayon_package2_chbx.setMinimumSize(QSize(80, 25))
        self.ayon_package2_chbx.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_201.addWidget(self.ayon_package2_chbx)

        self.ayon_package2 = QLineEdit(self.groupBox_33)
        self.ayon_package2.setObjectName(u"ayon_package2")
        sizePolicy1.setHeightForWidth(self.ayon_package2.sizePolicy().hasHeightForWidth())
        self.ayon_package2.setSizePolicy(sizePolicy1)
        self.ayon_package2.setMinimumSize(QSize(50, 25))
        self.ayon_package2.setMaximumSize(QSize(400, 16777215))
        self.ayon_package2.setReadOnly(False)

        self.horizontalLayout_201.addWidget(self.ayon_package2)


        self.horizontalLayout_200.addLayout(self.horizontalLayout_201)

        self.horizontalLayout_202 = QHBoxLayout()
        self.horizontalLayout_202.setObjectName(u"horizontalLayout_202")
        self.label_325 = QLabel(self.groupBox_33)
        self.label_325.setObjectName(u"label_325")
        sizePolicy2.setHeightForWidth(self.label_325.sizePolicy().hasHeightForWidth())
        self.label_325.setSizePolicy(sizePolicy2)
        self.label_325.setMinimumSize(QSize(40, 25))
        self.label_325.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_202.addWidget(self.label_325)

        self.ayon_list2 = QLineEdit(self.groupBox_33)
        self.ayon_list2.setObjectName(u"ayon_list2")
        sizePolicy1.setHeightForWidth(self.ayon_list2.sizePolicy().hasHeightForWidth())
        self.ayon_list2.setSizePolicy(sizePolicy1)
        self.ayon_list2.setMinimumSize(QSize(50, 25))
        self.ayon_list2.setMaximumSize(QSize(400, 16777215))
        self.ayon_list2.setReadOnly(False)

        self.horizontalLayout_202.addWidget(self.ayon_list2)


        self.horizontalLayout_200.addLayout(self.horizontalLayout_202)


        self.horizontalLayout_196.addLayout(self.horizontalLayout_200)

        self.horizontalLayout_203 = QHBoxLayout()
        self.horizontalLayout_203.setObjectName(u"horizontalLayout_203")
        self.horizontalLayout_204 = QHBoxLayout()
        self.horizontalLayout_204.setObjectName(u"horizontalLayout_204")
        self.ayon_package3_chbx = QCheckBox(self.groupBox_33)
        self.ayon_package3_chbx.setObjectName(u"ayon_package3_chbx")
        self.ayon_package3_chbx.setMinimumSize(QSize(80, 25))
        self.ayon_package3_chbx.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_204.addWidget(self.ayon_package3_chbx)

        self.ayon_package3 = QLineEdit(self.groupBox_33)
        self.ayon_package3.setObjectName(u"ayon_package3")
        sizePolicy1.setHeightForWidth(self.ayon_package3.sizePolicy().hasHeightForWidth())
        self.ayon_package3.setSizePolicy(sizePolicy1)
        self.ayon_package3.setMinimumSize(QSize(50, 25))
        self.ayon_package3.setMaximumSize(QSize(400, 16777215))
        self.ayon_package3.setReadOnly(False)

        self.horizontalLayout_204.addWidget(self.ayon_package3)


        self.horizontalLayout_203.addLayout(self.horizontalLayout_204)

        self.horizontalLayout_205 = QHBoxLayout()
        self.horizontalLayout_205.setObjectName(u"horizontalLayout_205")
        self.label_326 = QLabel(self.groupBox_33)
        self.label_326.setObjectName(u"label_326")
        sizePolicy2.setHeightForWidth(self.label_326.sizePolicy().hasHeightForWidth())
        self.label_326.setSizePolicy(sizePolicy2)
        self.label_326.setMinimumSize(QSize(40, 25))
        self.label_326.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_205.addWidget(self.label_326)

        self.ayon_list3 = QLineEdit(self.groupBox_33)
        self.ayon_list3.setObjectName(u"ayon_list3")
        sizePolicy1.setHeightForWidth(self.ayon_list3.sizePolicy().hasHeightForWidth())
        self.ayon_list3.setSizePolicy(sizePolicy1)
        self.ayon_list3.setMinimumSize(QSize(50, 25))
        self.ayon_list3.setMaximumSize(QSize(400, 16777215))
        self.ayon_list3.setReadOnly(False)

        self.horizontalLayout_205.addWidget(self.ayon_list3)


        self.horizontalLayout_203.addLayout(self.horizontalLayout_205)


        self.horizontalLayout_196.addLayout(self.horizontalLayout_203)


        self.verticalLayout_113.addLayout(self.horizontalLayout_196)


        self.verticalLayout_116.addWidget(self.groupBox_33)


        self.horizontalLayout_195.addLayout(self.verticalLayout_116)

        self.verticalLayout_117 = QVBoxLayout()
        self.verticalLayout_117.setObjectName(u"verticalLayout_117")
        self.groupBox_34 = QGroupBox(self.tab_25)
        self.groupBox_34.setObjectName(u"groupBox_34")
        self.verticalLayout_115 = QVBoxLayout(self.groupBox_34)
        self.verticalLayout_115.setObjectName(u"verticalLayout_115")
        self.verticalLayout_114 = QVBoxLayout()
        self.verticalLayout_114.setObjectName(u"verticalLayout_114")
        self.horizontalLayout_210 = QHBoxLayout()
        self.horizontalLayout_210.setObjectName(u"horizontalLayout_210")
        self.ayon_filter_assets = QCheckBox(self.groupBox_34)
        self.ayon_filter_assets.setObjectName(u"ayon_filter_assets")
        self.ayon_filter_assets.setMinimumSize(QSize(70, 25))
        self.ayon_filter_assets.setMaximumSize(QSize(70, 25))

        self.horizontalLayout_210.addWidget(self.ayon_filter_assets)

        self.ayon_filter_shots = QCheckBox(self.groupBox_34)
        self.ayon_filter_shots.setObjectName(u"ayon_filter_shots")
        self.ayon_filter_shots.setMinimumSize(QSize(70, 25))
        self.ayon_filter_shots.setMaximumSize(QSize(70, 25))

        self.horizontalLayout_210.addWidget(self.ayon_filter_shots)

        self.ayon_filter_tasks = QCheckBox(self.groupBox_34)
        self.ayon_filter_tasks.setObjectName(u"ayon_filter_tasks")
        self.ayon_filter_tasks.setMinimumSize(QSize(70, 25))
        self.ayon_filter_tasks.setMaximumSize(QSize(70, 25))

        self.horizontalLayout_210.addWidget(self.ayon_filter_tasks)

        self.ayon_filter_other = QCheckBox(self.groupBox_34)
        self.ayon_filter_other.setObjectName(u"ayon_filter_other")
        self.ayon_filter_other.setMinimumSize(QSize(70, 25))
        self.ayon_filter_other.setMaximumSize(QSize(70, 25))

        self.horizontalLayout_210.addWidget(self.ayon_filter_other)

        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_210.addItem(self.horizontalSpacer_29)


        self.verticalLayout_114.addLayout(self.horizontalLayout_210)

        self.horizontalLayout_208 = QHBoxLayout()
        self.horizontalLayout_208.setObjectName(u"horizontalLayout_208")
        self.ayon_filter_tasktype_chbx = QCheckBox(self.groupBox_34)
        self.ayon_filter_tasktype_chbx.setObjectName(u"ayon_filter_tasktype_chbx")
        sizePolicy2.setHeightForWidth(self.ayon_filter_tasktype_chbx.sizePolicy().hasHeightForWidth())
        self.ayon_filter_tasktype_chbx.setSizePolicy(sizePolicy2)
        self.ayon_filter_tasktype_chbx.setMinimumSize(QSize(90, 25))
        self.ayon_filter_tasktype_chbx.setMaximumSize(QSize(90, 25))
        self.ayon_filter_tasktype_chbx.setChecked(False)

        self.horizontalLayout_208.addWidget(self.ayon_filter_tasktype_chbx)

        self.ayon_filter_tasktypes = QLineEdit(self.groupBox_34)
        self.ayon_filter_tasktypes.setObjectName(u"ayon_filter_tasktypes")
        sizePolicy1.setHeightForWidth(self.ayon_filter_tasktypes.sizePolicy().hasHeightForWidth())
        self.ayon_filter_tasktypes.setSizePolicy(sizePolicy1)
        self.ayon_filter_tasktypes.setMinimumSize(QSize(50, 25))
        self.ayon_filter_tasktypes.setMaximumSize(QSize(1000, 25))
        self.ayon_filter_tasktypes.setReadOnly(False)

        self.horizontalLayout_208.addWidget(self.ayon_filter_tasktypes)


        self.verticalLayout_114.addLayout(self.horizontalLayout_208)

        self.horizontalLayout_209 = QHBoxLayout()
        self.horizontalLayout_209.setObjectName(u"horizontalLayout_209")
        self.ayon_filter_assignee_chbx = QCheckBox(self.groupBox_34)
        self.ayon_filter_assignee_chbx.setObjectName(u"ayon_filter_assignee_chbx")
        sizePolicy2.setHeightForWidth(self.ayon_filter_assignee_chbx.sizePolicy().hasHeightForWidth())
        self.ayon_filter_assignee_chbx.setSizePolicy(sizePolicy2)
        self.ayon_filter_assignee_chbx.setMinimumSize(QSize(90, 25))
        self.ayon_filter_assignee_chbx.setMaximumSize(QSize(90, 25))
        self.ayon_filter_assignee_chbx.setChecked(False)

        self.horizontalLayout_209.addWidget(self.ayon_filter_assignee_chbx)

        self.ayon_filter_assignees = QLineEdit(self.groupBox_34)
        self.ayon_filter_assignees.setObjectName(u"ayon_filter_assignees")
        sizePolicy1.setHeightForWidth(self.ayon_filter_assignees.sizePolicy().hasHeightForWidth())
        self.ayon_filter_assignees.setSizePolicy(sizePolicy1)
        self.ayon_filter_assignees.setMinimumSize(QSize(50, 25))
        self.ayon_filter_assignees.setMaximumSize(QSize(1000, 25))
        self.ayon_filter_assignees.setReadOnly(False)

        self.horizontalLayout_209.addWidget(self.ayon_filter_assignees)


        self.verticalLayout_114.addLayout(self.horizontalLayout_209)


        self.verticalLayout_115.addLayout(self.verticalLayout_114)


        self.verticalLayout_117.addWidget(self.groupBox_34)

        self.horizontalLayout_212 = QHBoxLayout()
        self.horizontalLayout_212.setObjectName(u"horizontalLayout_212")
        self.ayon_export_butt = QPushButton(self.tab_25)
        self.ayon_export_butt.setObjectName(u"ayon_export_butt")
        sizePolicy1.setHeightForWidth(self.ayon_export_butt.sizePolicy().hasHeightForWidth())
        self.ayon_export_butt.setSizePolicy(sizePolicy1)
        self.ayon_export_butt.setMinimumSize(QSize(0, 35))
        self.ayon_export_butt.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_212.addWidget(self.ayon_export_butt)

        self.ayon_export_go = QCheckBox(self.tab_25)
        self.ayon_export_go.setObjectName(u"ayon_export_go")
        sizePolicy2.setHeightForWidth(self.ayon_export_go.sizePolicy().hasHeightForWidth())
        self.ayon_export_go.setSizePolicy(sizePolicy2)
        self.ayon_export_go.setMinimumSize(QSize(110, 25))
        self.ayon_export_go.setMaximumSize(QSize(110, 25))

        self.horizontalLayout_212.addWidget(self.ayon_export_go)


        self.verticalLayout_117.addLayout(self.horizontalLayout_212)


        self.horizontalLayout_195.addLayout(self.verticalLayout_117)


        self.verticalLayout_118.addLayout(self.horizontalLayout_195)

        self.ayon_table = QTableWidget(self.tab_25)
        self.ayon_table.setObjectName(u"ayon_table")
        sizePolicy.setHeightForWidth(self.ayon_table.sizePolicy().hasHeightForWidth())
        self.ayon_table.setSizePolicy(sizePolicy)
        self.ayon_table.setMinimumSize(QSize(600, 100))
        self.ayon_table.setMaximumSize(QSize(16000, 16000))

        self.verticalLayout_118.addWidget(self.ayon_table)


        self.verticalLayout_119.addLayout(self.verticalLayout_118)

        self.TopTab.addTab(self.tab_25, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_47 = QVBoxLayout(self.tab_4)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_40 = QVBoxLayout()
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.horizontalLayout_57 = QHBoxLayout()
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.groupBox_14 = QGroupBox(self.tab_4)
        self.groupBox_14.setObjectName(u"groupBox_14")
        sizePolicy11 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.groupBox_14.sizePolicy().hasHeightForWidth())
        self.groupBox_14.setSizePolicy(sizePolicy11)
        self.groupBox_14.setMinimumSize(QSize(0, 50))
        self.groupBox_14.setMaximumSize(QSize(16777215, 50))
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_14)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_45 = QLabel(self.groupBox_14)
        self.label_45.setObjectName(u"label_45")
        sizePolicy2.setHeightForWidth(self.label_45.sizePolicy().hasHeightForWidth())
        self.label_45.setSizePolicy(sizePolicy2)
        self.label_45.setMinimumSize(QSize(80, 25))
        self.label_45.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_36.addWidget(self.label_45)

        self.prefs_frame_rate_txt = QLineEdit(self.groupBox_14)
        self.prefs_frame_rate_txt.setObjectName(u"prefs_frame_rate_txt")
        self.prefs_frame_rate_txt.setMinimumSize(QSize(80, 25))
        self.prefs_frame_rate_txt.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_36.addWidget(self.prefs_frame_rate_txt)

        self.prefs_frame_rate_use_meta = QCheckBox(self.groupBox_14)
        self.prefs_frame_rate_use_meta.setObjectName(u"prefs_frame_rate_use_meta")
        sizePolicy2.setHeightForWidth(self.prefs_frame_rate_use_meta.sizePolicy().hasHeightForWidth())
        self.prefs_frame_rate_use_meta.setSizePolicy(sizePolicy2)
        self.prefs_frame_rate_use_meta.setMinimumSize(QSize(220, 25))
        self.prefs_frame_rate_use_meta.setMaximumSize(QSize(220, 25))
        self.prefs_frame_rate_use_meta.setChecked(True)

        self.horizontalLayout_36.addWidget(self.prefs_frame_rate_use_meta)


        self.verticalLayout_5.addLayout(self.horizontalLayout_36)


        self.horizontalLayout_57.addWidget(self.groupBox_14)

        self.groupBox_15 = QGroupBox(self.tab_4)
        self.groupBox_15.setObjectName(u"groupBox_15")
        sizePolicy11.setHeightForWidth(self.groupBox_15.sizePolicy().hasHeightForWidth())
        self.groupBox_15.setSizePolicy(sizePolicy11)
        self.groupBox_15.setMinimumSize(QSize(0, 50))
        self.groupBox_15.setMaximumSize(QSize(16777215, 50))
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_15)
        self.verticalLayout_11.setSpacing(3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setSpacing(3)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.prefs_tc_from_meta = QRadioButton(self.groupBox_15)
        self.prefs_tc_from_meta.setObjectName(u"prefs_tc_from_meta")
        sizePolicy2.setHeightForWidth(self.prefs_tc_from_meta.sizePolicy().hasHeightForWidth())
        self.prefs_tc_from_meta.setSizePolicy(sizePolicy2)
        self.prefs_tc_from_meta.setChecked(True)

        self.horizontalLayout_37.addWidget(self.prefs_tc_from_meta)

        self.prefs_tc_from_counter = QRadioButton(self.groupBox_15)
        self.prefs_tc_from_counter.setObjectName(u"prefs_tc_from_counter")
        sizePolicy2.setHeightForWidth(self.prefs_tc_from_counter.sizePolicy().hasHeightForWidth())
        self.prefs_tc_from_counter.setSizePolicy(sizePolicy2)

        self.horizontalLayout_37.addWidget(self.prefs_tc_from_counter)


        self.horizontalLayout_38.addLayout(self.horizontalLayout_37)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_46 = QLabel(self.groupBox_15)
        self.label_46.setObjectName(u"label_46")
        sizePolicy2.setHeightForWidth(self.label_46.sizePolicy().hasHeightForWidth())
        self.label_46.setSizePolicy(sizePolicy2)
        self.label_46.setMinimumSize(QSize(80, 25))
        self.label_46.setMaximumSize(QSize(80, 25))

        self.horizontalLayout_9.addWidget(self.label_46)

        self.prefs_tc_default = QLineEdit(self.groupBox_15)
        self.prefs_tc_default.setObjectName(u"prefs_tc_default")
        sizePolicy2.setHeightForWidth(self.prefs_tc_default.sizePolicy().hasHeightForWidth())
        self.prefs_tc_default.setSizePolicy(sizePolicy2)
        self.prefs_tc_default.setMinimumSize(QSize(80, 25))

        self.horizontalLayout_9.addWidget(self.prefs_tc_default)


        self.horizontalLayout_38.addLayout(self.horizontalLayout_9)


        self.verticalLayout_11.addLayout(self.horizontalLayout_38)


        self.horizontalLayout_57.addWidget(self.groupBox_15)

        self.horizontalSpacer_5 = QSpacerItem(13, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_57.addItem(self.horizontalSpacer_5)


        self.verticalLayout_40.addLayout(self.horizontalLayout_57)

        self.horizontalLayout_56 = QHBoxLayout()
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.groupBox_17 = QGroupBox(self.tab_4)
        self.groupBox_17.setObjectName(u"groupBox_17")
        sizePolicy11.setHeightForWidth(self.groupBox_17.sizePolicy().hasHeightForWidth())
        self.groupBox_17.setSizePolicy(sizePolicy11)
        self.groupBox_17.setMinimumSize(QSize(650, 60))
        self.groupBox_17.setMaximumSize(QSize(16777215, 80))
        self.horizontalLayout_30 = QHBoxLayout(self.groupBox_17)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.prefs_size_scan = QCheckBox(self.groupBox_17)
        self.prefs_size_scan.setObjectName(u"prefs_size_scan")
        sizePolicy2.setHeightForWidth(self.prefs_size_scan.sizePolicy().hasHeightForWidth())
        self.prefs_size_scan.setSizePolicy(sizePolicy2)
        self.prefs_size_scan.setMinimumSize(QSize(90, 25))
        self.prefs_size_scan.setMaximumSize(QSize(90, 25))
        self.prefs_size_scan.setChecked(True)

        self.horizontalLayout_22.addWidget(self.prefs_size_scan)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_51 = QLabel(self.groupBox_17)
        self.label_51.setObjectName(u"label_51")
        sizePolicy2.setHeightForWidth(self.label_51.sizePolicy().hasHeightForWidth())
        self.label_51.setSizePolicy(sizePolicy2)
        self.label_51.setMinimumSize(QSize(120, 25))
        self.label_51.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_18.addWidget(self.label_51)

        self.prefs_size_ignore_first = QSpinBox(self.groupBox_17)
        self.prefs_size_ignore_first.setObjectName(u"prefs_size_ignore_first")
        sizePolicy2.setHeightForWidth(self.prefs_size_ignore_first.sizePolicy().hasHeightForWidth())
        self.prefs_size_ignore_first.setSizePolicy(sizePolicy2)
        self.prefs_size_ignore_first.setMinimumSize(QSize(40, 25))
        self.prefs_size_ignore_first.setMaximumSize(QSize(40, 25))
        self.prefs_size_ignore_first.setMaximum(999)
        self.prefs_size_ignore_first.setValue(1)

        self.horizontalLayout_18.addWidget(self.prefs_size_ignore_first)


        self.horizontalLayout_22.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.label_53 = QLabel(self.groupBox_17)
        self.label_53.setObjectName(u"label_53")
        sizePolicy2.setHeightForWidth(self.label_53.sizePolicy().hasHeightForWidth())
        self.label_53.setSizePolicy(sizePolicy2)
        self.label_53.setMinimumSize(QSize(130, 25))
        self.label_53.setMaximumSize(QSize(130, 25))

        self.horizontalLayout_47.addWidget(self.label_53)

        self.prefs_size_neighborhood = QSpinBox(self.groupBox_17)
        self.prefs_size_neighborhood.setObjectName(u"prefs_size_neighborhood")
        sizePolicy2.setHeightForWidth(self.prefs_size_neighborhood.sizePolicy().hasHeightForWidth())
        self.prefs_size_neighborhood.setSizePolicy(sizePolicy2)
        self.prefs_size_neighborhood.setMinimumSize(QSize(40, 25))
        self.prefs_size_neighborhood.setMaximumSize(QSize(40, 25))
        self.prefs_size_neighborhood.setMaximum(999)
        self.prefs_size_neighborhood.setValue(2)

        self.horizontalLayout_47.addWidget(self.prefs_size_neighborhood)


        self.horizontalLayout_22.addLayout(self.horizontalLayout_47)

        self.horizontalLayout_48 = QHBoxLayout()
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.label_54 = QLabel(self.groupBox_17)
        self.label_54.setObjectName(u"label_54")
        sizePolicy2.setHeightForWidth(self.label_54.sizePolicy().hasHeightForWidth())
        self.label_54.setSizePolicy(sizePolicy2)
        self.label_54.setMinimumSize(QSize(75, 25))
        self.label_54.setMaximumSize(QSize(75, 25))

        self.horizontalLayout_48.addWidget(self.label_54)

        self.prefs_size_threshold = QSpinBox(self.groupBox_17)
        self.prefs_size_threshold.setObjectName(u"prefs_size_threshold")
        sizePolicy2.setHeightForWidth(self.prefs_size_threshold.sizePolicy().hasHeightForWidth())
        self.prefs_size_threshold.setSizePolicy(sizePolicy2)
        self.prefs_size_threshold.setMinimumSize(QSize(40, 25))
        self.prefs_size_threshold.setMaximumSize(QSize(40, 25))
        self.prefs_size_threshold.setMinimum(1)
        self.prefs_size_threshold.setMaximum(100)
        self.prefs_size_threshold.setValue(30)

        self.horizontalLayout_48.addWidget(self.prefs_size_threshold)


        self.horizontalLayout_22.addLayout(self.horizontalLayout_48)


        self.horizontalLayout_30.addLayout(self.horizontalLayout_22)


        self.horizontalLayout_56.addWidget(self.groupBox_17)

        self.horizontalSpacer_12 = QSpacerItem(13, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_56.addItem(self.horizontalSpacer_12)


        self.verticalLayout_40.addLayout(self.horizontalLayout_56)

        self.horizontalLayout_58 = QHBoxLayout()
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.groupBox_13 = QGroupBox(self.tab_4)
        self.groupBox_13.setObjectName(u"groupBox_13")
        sizePolicy1.setHeightForWidth(self.groupBox_13.sizePolicy().hasHeightForWidth())
        self.groupBox_13.setSizePolicy(sizePolicy1)
        self.groupBox_13.setMinimumSize(QSize(0, 50))
        self.groupBox_13.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_54 = QHBoxLayout(self.groupBox_13)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.prefs_oiio_custom_ocio = QCheckBox(self.groupBox_13)
        self.prefs_oiio_custom_ocio.setObjectName(u"prefs_oiio_custom_ocio")
        sizePolicy2.setHeightForWidth(self.prefs_oiio_custom_ocio.sizePolicy().hasHeightForWidth())
        self.prefs_oiio_custom_ocio.setSizePolicy(sizePolicy2)
        self.prefs_oiio_custom_ocio.setMinimumSize(QSize(100, 25))
        self.prefs_oiio_custom_ocio.setMaximumSize(QSize(100, 25))
        self.prefs_oiio_custom_ocio.setChecked(False)

        self.horizontalLayout_54.addWidget(self.prefs_oiio_custom_ocio)

        self.prefs_oiio_custom_ocio_path = QLineEdit(self.groupBox_13)
        self.prefs_oiio_custom_ocio_path.setObjectName(u"prefs_oiio_custom_ocio_path")
        sizePolicy1.setHeightForWidth(self.prefs_oiio_custom_ocio_path.sizePolicy().hasHeightForWidth())
        self.prefs_oiio_custom_ocio_path.setSizePolicy(sizePolicy1)
        self.prefs_oiio_custom_ocio_path.setMinimumSize(QSize(200, 25))
        self.prefs_oiio_custom_ocio_path.setMaximumSize(QSize(500, 25))

        self.horizontalLayout_54.addWidget(self.prefs_oiio_custom_ocio_path)


        self.horizontalLayout_58.addWidget(self.groupBox_13)

        self.groupBox_2 = QGroupBox(self.tab_4)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        self.groupBox_2.setMinimumSize(QSize(0, 50))
        self.horizontalLayout_70 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_70.setSpacing(3)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setSpacing(3)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setMinimumSize(QSize(33, 25))
        self.label.setMaximumSize(QSize(33, 25))

        self.horizontalLayout_25.addWidget(self.label)

        self.prefs_counter_start = QSpinBox(self.groupBox_2)
        self.prefs_counter_start.setObjectName(u"prefs_counter_start")
        sizePolicy2.setHeightForWidth(self.prefs_counter_start.sizePolicy().hasHeightForWidth())
        self.prefs_counter_start.setSizePolicy(sizePolicy2)
        self.prefs_counter_start.setMinimumSize(QSize(40, 25))
        self.prefs_counter_start.setMaximumSize(QSize(40, 25))
        self.prefs_counter_start.setValue(1)

        self.horizontalLayout_25.addWidget(self.prefs_counter_start)


        self.horizontalLayout_28.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setMinimumSize(QSize(33, 25))
        self.label_2.setMaximumSize(QSize(33, 25))

        self.horizontalLayout_26.addWidget(self.label_2)

        self.prefs_counter_step = QSpinBox(self.groupBox_2)
        self.prefs_counter_step.setObjectName(u"prefs_counter_step")
        sizePolicy2.setHeightForWidth(self.prefs_counter_step.sizePolicy().hasHeightForWidth())
        self.prefs_counter_step.setSizePolicy(sizePolicy2)
        self.prefs_counter_step.setMinimumSize(QSize(40, 25))
        self.prefs_counter_step.setMaximumSize(QSize(40, 25))
        self.prefs_counter_step.setValue(1)

        self.horizontalLayout_26.addWidget(self.prefs_counter_step)


        self.horizontalLayout_28.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_14 = QLabel(self.groupBox_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(100, 25))
        self.label_14.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_27.addWidget(self.label_14)

        self.prefs_counter_zeroes = QSpinBox(self.groupBox_2)
        self.prefs_counter_zeroes.setObjectName(u"prefs_counter_zeroes")
        sizePolicy2.setHeightForWidth(self.prefs_counter_zeroes.sizePolicy().hasHeightForWidth())
        self.prefs_counter_zeroes.setSizePolicy(sizePolicy2)
        self.prefs_counter_zeroes.setMinimumSize(QSize(40, 25))
        self.prefs_counter_zeroes.setMaximumSize(QSize(40, 25))
        self.prefs_counter_zeroes.setValue(3)

        self.horizontalLayout_27.addWidget(self.prefs_counter_zeroes)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_21)


        self.horizontalLayout_28.addLayout(self.horizontalLayout_27)


        self.horizontalLayout_70.addLayout(self.horizontalLayout_28)


        self.horizontalLayout_58.addWidget(self.groupBox_2)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_58.addItem(self.horizontalSpacer_19)


        self.verticalLayout_40.addLayout(self.horizontalLayout_58)

        self.horizontalLayout_55 = QHBoxLayout()
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.groupBox_19 = QGroupBox(self.tab_4)
        self.groupBox_19.setObjectName(u"groupBox_19")
        sizePolicy11.setHeightForWidth(self.groupBox_19.sizePolicy().hasHeightForWidth())
        self.groupBox_19.setSizePolicy(sizePolicy11)
        self.groupBox_19.setMinimumSize(QSize(650, 60))
        self.groupBox_19.setMaximumSize(QSize(16777215, 80))
        self.verticalLayout_28 = QVBoxLayout(self.groupBox_19)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.horizontalLayout_121 = QHBoxLayout()
        self.horizontalLayout_121.setObjectName(u"horizontalLayout_121")
        self.horizontalLayout_118 = QHBoxLayout()
        self.horizontalLayout_118.setObjectName(u"horizontalLayout_118")
        self.prefs_merge_chbx = QCheckBox(self.groupBox_19)
        self.prefs_merge_chbx.setObjectName(u"prefs_merge_chbx")
        sizePolicy2.setHeightForWidth(self.prefs_merge_chbx.sizePolicy().hasHeightForWidth())
        self.prefs_merge_chbx.setSizePolicy(sizePolicy2)
        self.prefs_merge_chbx.setMinimumSize(QSize(80, 25))
        self.prefs_merge_chbx.setMaximumSize(QSize(80, 25))
        self.prefs_merge_chbx.setChecked(True)

        self.horizontalLayout_118.addWidget(self.prefs_merge_chbx)

        self.prefs_merge_by = QLineEdit(self.groupBox_19)
        self.prefs_merge_by.setObjectName(u"prefs_merge_by")
        self.prefs_merge_by.setMinimumSize(QSize(120, 25))
        self.prefs_merge_by.setMaximumSize(QSize(120, 25))

        self.horizontalLayout_118.addWidget(self.prefs_merge_by)


        self.horizontalLayout_121.addLayout(self.horizontalLayout_118)

        self.prefs_merge_collapse = QCheckBox(self.groupBox_19)
        self.prefs_merge_collapse.setObjectName(u"prefs_merge_collapse")
        sizePolicy2.setHeightForWidth(self.prefs_merge_collapse.sizePolicy().hasHeightForWidth())
        self.prefs_merge_collapse.setSizePolicy(sizePolicy2)
        self.prefs_merge_collapse.setMinimumSize(QSize(110, 25))
        self.prefs_merge_collapse.setMaximumSize(QSize(110, 25))
        self.prefs_merge_collapse.setChecked(True)

        self.horizontalLayout_121.addWidget(self.prefs_merge_collapse)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_88 = QLabel(self.groupBox_19)
        self.label_88.setObjectName(u"label_88")
        sizePolicy2.setHeightForWidth(self.label_88.sizePolicy().hasHeightForWidth())
        self.label_88.setSizePolicy(sizePolicy2)
        self.label_88.setMinimumSize(QSize(70, 25))
        self.label_88.setMaximumSize(QSize(70, 25))

        self.horizontalLayout_23.addWidget(self.label_88)

        self.prefs_merge_sep = QLineEdit(self.groupBox_19)
        self.prefs_merge_sep.setObjectName(u"prefs_merge_sep")
        self.prefs_merge_sep.setMinimumSize(QSize(40, 25))
        self.prefs_merge_sep.setMaximumSize(QSize(40, 25))

        self.horizontalLayout_23.addWidget(self.prefs_merge_sep)


        self.horizontalLayout_121.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_120 = QHBoxLayout()
        self.horizontalLayout_120.setObjectName(u"horizontalLayout_120")
        self.label_89 = QLabel(self.groupBox_19)
        self.label_89.setObjectName(u"label_89")
        sizePolicy2.setHeightForWidth(self.label_89.sizePolicy().hasHeightForWidth())
        self.label_89.setSizePolicy(sizePolicy2)
        self.label_89.setMinimumSize(QSize(50, 25))
        self.label_89.setMaximumSize(QSize(50, 25))

        self.horizontalLayout_120.addWidget(self.label_89)

        self.prefs_merge_sort = QLineEdit(self.groupBox_19)
        self.prefs_merge_sort.setObjectName(u"prefs_merge_sort")
        self.prefs_merge_sort.setMinimumSize(QSize(100, 25))
        self.prefs_merge_sort.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_120.addWidget(self.prefs_merge_sort)


        self.horizontalLayout_121.addLayout(self.horizontalLayout_120)

        self.horizontalLayout_119 = QHBoxLayout()
        self.horizontalLayout_119.setObjectName(u"horizontalLayout_119")
        self.label_162 = QLabel(self.groupBox_19)
        self.label_162.setObjectName(u"label_162")
        sizePolicy2.setHeightForWidth(self.label_162.sizePolicy().hasHeightForWidth())
        self.label_162.setSizePolicy(sizePolicy2)
        self.label_162.setMinimumSize(QSize(50, 25))
        self.label_162.setMaximumSize(QSize(50, 25))

        self.horizontalLayout_119.addWidget(self.label_162)

        self.prefs_merge_order = QLineEdit(self.groupBox_19)
        self.prefs_merge_order.setObjectName(u"prefs_merge_order")
        self.prefs_merge_order.setMinimumSize(QSize(120, 25))
        self.prefs_merge_order.setMaximumSize(QSize(120, 25))

        self.horizontalLayout_119.addWidget(self.prefs_merge_order)


        self.horizontalLayout_121.addLayout(self.horizontalLayout_119)

        self.prefs_merge_hide = QCheckBox(self.groupBox_19)
        self.prefs_merge_hide.setObjectName(u"prefs_merge_hide")
        sizePolicy2.setHeightForWidth(self.prefs_merge_hide.sizePolicy().hasHeightForWidth())
        self.prefs_merge_hide.setSizePolicy(sizePolicy2)
        self.prefs_merge_hide.setMinimumSize(QSize(100, 25))
        self.prefs_merge_hide.setMaximumSize(QSize(100, 25))
        self.prefs_merge_hide.setChecked(True)

        self.horizontalLayout_121.addWidget(self.prefs_merge_hide)


        self.verticalLayout_28.addLayout(self.horizontalLayout_121)


        self.horizontalLayout_55.addWidget(self.groupBox_19)

        self.horizontalSpacer_2 = QSpacerItem(13, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_55.addItem(self.horizontalSpacer_2)


        self.verticalLayout_40.addLayout(self.horizontalLayout_55)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_40.addItem(self.verticalSpacer_5)


        self.verticalLayout_47.addLayout(self.verticalLayout_40)

        self.TopTab.addTab(self.tab_4, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.horizontalLayout_134 = QHBoxLayout(self.tab_9)
        self.horizontalLayout_134.setObjectName(u"horizontalLayout_134")
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.groupBox_4 = QGroupBox(self.tab_9)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy1.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy1)
        self.groupBox_4.setMinimumSize(QSize(180, 50))
        self.horizontalLayout_131 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_131.setObjectName(u"horizontalLayout_131")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.export_sub_excel = QCheckBox(self.groupBox_4)
        self.export_sub_excel.setObjectName(u"export_sub_excel")
        sizePolicy2.setHeightForWidth(self.export_sub_excel.sizePolicy().hasHeightForWidth())
        self.export_sub_excel.setSizePolicy(sizePolicy2)
        self.export_sub_excel.setMinimumSize(QSize(62, 0))
        self.export_sub_excel.setChecked(True)

        self.horizontalLayout_29.addWidget(self.export_sub_excel)

        self.export_sub_csv = QCheckBox(self.groupBox_4)
        self.export_sub_csv.setObjectName(u"export_sub_csv")

        self.horizontalLayout_29.addWidget(self.export_sub_csv)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_7)


        self.verticalLayout_13.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.export_sub_root = QRadioButton(self.groupBox_4)
        self.export_sub_root.setObjectName(u"export_sub_root")
        self.export_sub_root.setMinimumSize(QSize(61, 0))
        self.export_sub_root.setChecked(True)

        self.horizontalLayout_34.addWidget(self.export_sub_root)

        self.export_sub_above = QRadioButton(self.groupBox_4)
        self.export_sub_above.setObjectName(u"export_sub_above")
        self.export_sub_above.setMinimumSize(QSize(161, 0))

        self.horizontalLayout_34.addWidget(self.export_sub_above)

        self.export_sub_custom = QRadioButton(self.groupBox_4)
        self.export_sub_custom.setObjectName(u"export_sub_custom")
        self.export_sub_custom.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_34.addWidget(self.export_sub_custom)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_17)


        self.verticalLayout_13.addLayout(self.horizontalLayout_34)

        self.horizontalLayout_130 = QHBoxLayout()
        self.horizontalLayout_130.setObjectName(u"horizontalLayout_130")
        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.label_15 = QLabel(self.groupBox_4)
        self.label_15.setObjectName(u"label_15")
        sizePolicy2.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy2)
        self.label_15.setMinimumSize(QSize(100, 16))
        self.label_15.setMaximumSize(QSize(100, 16))

        self.horizontalLayout_45.addWidget(self.label_15)

        self.export_sub_custom_path = QLineEdit(self.groupBox_4)
        self.export_sub_custom_path.setObjectName(u"export_sub_custom_path")
        sizePolicy5.setHeightForWidth(self.export_sub_custom_path.sizePolicy().hasHeightForWidth())
        self.export_sub_custom_path.setSizePolicy(sizePolicy5)
        self.export_sub_custom_path.setMinimumSize(QSize(400, 25))
        self.export_sub_custom_path.setMaximumSize(QSize(1500, 25))

        self.horizontalLayout_45.addWidget(self.export_sub_custom_path)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_45.addItem(self.horizontalSpacer_13)


        self.horizontalLayout_130.addLayout(self.horizontalLayout_45)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.label_32 = QLabel(self.groupBox_4)
        self.label_32.setObjectName(u"label_32")
        sizePolicy2.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy2)
        self.label_32.setMinimumSize(QSize(50, 16))
        self.label_32.setMaximumSize(QSize(50, 16))

        self.horizontalLayout_39.addWidget(self.label_32)

        self.export_sub_custom_suffix = QLineEdit(self.groupBox_4)
        self.export_sub_custom_suffix.setObjectName(u"export_sub_custom_suffix")
        sizePolicy2.setHeightForWidth(self.export_sub_custom_suffix.sizePolicy().hasHeightForWidth())
        self.export_sub_custom_suffix.setSizePolicy(sizePolicy2)
        self.export_sub_custom_suffix.setMinimumSize(QSize(150, 25))
        self.export_sub_custom_suffix.setMaximumSize(QSize(150, 25))

        self.horizontalLayout_39.addWidget(self.export_sub_custom_suffix)


        self.horizontalLayout_130.addLayout(self.horizontalLayout_39)


        self.verticalLayout_13.addLayout(self.horizontalLayout_130)


        self.horizontalLayout_131.addLayout(self.verticalLayout_13)


        self.verticalLayout_17.addWidget(self.groupBox_4)

        self.groupBox_10 = QGroupBox(self.tab_9)
        self.groupBox_10.setObjectName(u"groupBox_10")
        sizePolicy1.setHeightForWidth(self.groupBox_10.sizePolicy().hasHeightForWidth())
        self.groupBox_10.setSizePolicy(sizePolicy1)
        self.groupBox_10.setMinimumSize(QSize(180, 50))
        self.horizontalLayout_133 = QHBoxLayout(self.groupBox_10)
        self.horizontalLayout_133.setObjectName(u"horizontalLayout_133")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.export_log_excel = QCheckBox(self.groupBox_10)
        self.export_log_excel.setObjectName(u"export_log_excel")
        sizePolicy2.setHeightForWidth(self.export_log_excel.sizePolicy().hasHeightForWidth())
        self.export_log_excel.setSizePolicy(sizePolicy2)
        self.export_log_excel.setMinimumSize(QSize(62, 0))
        self.export_log_excel.setChecked(False)

        self.horizontalLayout_43.addWidget(self.export_log_excel)

        self.export_log_csv = QCheckBox(self.groupBox_10)
        self.export_log_csv.setObjectName(u"export_log_csv")

        self.horizontalLayout_43.addWidget(self.export_log_csv)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_43.addItem(self.horizontalSpacer_11)


        self.verticalLayout_14.addLayout(self.horizontalLayout_43)

        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.export_log_root = QRadioButton(self.groupBox_10)
        self.export_log_root.setObjectName(u"export_log_root")
        self.export_log_root.setMinimumSize(QSize(61, 0))
        self.export_log_root.setChecked(True)

        self.horizontalLayout_41.addWidget(self.export_log_root)

        self.export_log_above = QRadioButton(self.groupBox_10)
        self.export_log_above.setObjectName(u"export_log_above")
        self.export_log_above.setMinimumSize(QSize(161, 0))

        self.horizontalLayout_41.addWidget(self.export_log_above)

        self.export_log_custom = QRadioButton(self.groupBox_10)
        self.export_log_custom.setObjectName(u"export_log_custom")
        self.export_log_custom.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_41.addWidget(self.export_log_custom)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_41.addItem(self.horizontalSpacer_15)


        self.verticalLayout_14.addLayout(self.horizontalLayout_41)

        self.horizontalLayout_132 = QHBoxLayout()
        self.horizontalLayout_132.setObjectName(u"horizontalLayout_132")
        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.label_16 = QLabel(self.groupBox_10)
        self.label_16.setObjectName(u"label_16")
        sizePolicy2.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy2)
        self.label_16.setMinimumSize(QSize(100, 16))
        self.label_16.setMaximumSize(QSize(100, 16))

        self.horizontalLayout_44.addWidget(self.label_16)

        self.export_log_custom_path = QLineEdit(self.groupBox_10)
        self.export_log_custom_path.setObjectName(u"export_log_custom_path")
        sizePolicy5.setHeightForWidth(self.export_log_custom_path.sizePolicy().hasHeightForWidth())
        self.export_log_custom_path.setSizePolicy(sizePolicy5)
        self.export_log_custom_path.setMinimumSize(QSize(400, 25))
        self.export_log_custom_path.setMaximumSize(QSize(1500, 25))

        self.horizontalLayout_44.addWidget(self.export_log_custom_path)


        self.horizontalLayout_132.addLayout(self.horizontalLayout_44)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_132.addItem(self.horizontalSpacer_14)

        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.label_33 = QLabel(self.groupBox_10)
        self.label_33.setObjectName(u"label_33")
        sizePolicy2.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy2)
        self.label_33.setMinimumSize(QSize(50, 16))
        self.label_33.setMaximumSize(QSize(50, 16))

        self.horizontalLayout_42.addWidget(self.label_33)

        self.export_log_custom_suffix = QLineEdit(self.groupBox_10)
        self.export_log_custom_suffix.setObjectName(u"export_log_custom_suffix")
        sizePolicy2.setHeightForWidth(self.export_log_custom_suffix.sizePolicy().hasHeightForWidth())
        self.export_log_custom_suffix.setSizePolicy(sizePolicy2)
        self.export_log_custom_suffix.setMinimumSize(QSize(150, 25))
        self.export_log_custom_suffix.setMaximumSize(QSize(150, 25))

        self.horizontalLayout_42.addWidget(self.export_log_custom_suffix)


        self.horizontalLayout_132.addLayout(self.horizontalLayout_42)


        self.verticalLayout_14.addLayout(self.horizontalLayout_132)


        self.horizontalLayout_133.addLayout(self.verticalLayout_14)


        self.verticalLayout_17.addWidget(self.groupBox_10)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_3)


        self.horizontalLayout_134.addLayout(self.verticalLayout_17)

        self.TopTab.addTab(self.tab_9, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_95 = QVBoxLayout(self.tab_3)
        self.verticalLayout_95.setObjectName(u"verticalLayout_95")
        self.horizontalLayout_67 = QHBoxLayout()
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.groupBox_31 = QGroupBox(self.tab_3)
        self.groupBox_31.setObjectName(u"groupBox_31")
        self.groupBox_31.setMinimumSize(QSize(0, 270))
        self.groupBox_31.setMaximumSize(QSize(16777215, 270))
        self.verticalLayout_97 = QVBoxLayout(self.groupBox_31)
        self.verticalLayout_97.setObjectName(u"verticalLayout_97")
        self.verticalLayout_94 = QVBoxLayout()
        self.verticalLayout_94.setObjectName(u"verticalLayout_94")
        self.groupBox_3 = QGroupBox(self.groupBox_31)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy6.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy6)
        self.groupBox_3.setMinimumSize(QSize(0, 60))
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)
        self.label_5.setMinimumSize(QSize(100, 25))

        self.horizontalLayout_35.addWidget(self.label_5)

        self.load_preset_combobox = QComboBox(self.groupBox_3)
        self.load_preset_combobox.setObjectName(u"load_preset_combobox")
        sizePolicy1.setHeightForWidth(self.load_preset_combobox.sizePolicy().hasHeightForWidth())
        self.load_preset_combobox.setSizePolicy(sizePolicy1)
        self.load_preset_combobox.setMinimumSize(QSize(50, 25))
        self.load_preset_combobox.setEditable(False)
        self.load_preset_combobox.setInsertPolicy(QComboBox.InsertAtTop)

        self.horizontalLayout_35.addWidget(self.load_preset_combobox)

        self.load_preset_button = QPushButton(self.groupBox_3)
        self.load_preset_button.setObjectName(u"load_preset_button")
        sizePolicy2.setHeightForWidth(self.load_preset_button.sizePolicy().hasHeightForWidth())
        self.load_preset_button.setSizePolicy(sizePolicy2)
        self.load_preset_button.setMinimumSize(QSize(120, 25))

        self.horizontalLayout_35.addWidget(self.load_preset_button)


        self.verticalLayout_9.addLayout(self.horizontalLayout_35)


        self.verticalLayout_94.addWidget(self.groupBox_3)

        self.groupBox_7 = QGroupBox(self.groupBox_31)
        self.groupBox_7.setObjectName(u"groupBox_7")
        sizePolicy6.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy6)
        self.groupBox_7.setMinimumSize(QSize(0, 60))
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_29 = QLabel(self.groupBox_7)
        self.label_29.setObjectName(u"label_29")
        sizePolicy2.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy2)
        self.label_29.setMinimumSize(QSize(100, 25))

        self.horizontalLayout_33.addWidget(self.label_29)

        self.save_preset_name = QLineEdit(self.groupBox_7)
        self.save_preset_name.setObjectName(u"save_preset_name")
        sizePolicy1.setHeightForWidth(self.save_preset_name.sizePolicy().hasHeightForWidth())
        self.save_preset_name.setSizePolicy(sizePolicy1)
        self.save_preset_name.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_33.addWidget(self.save_preset_name)

        self.save_preset_button = QPushButton(self.groupBox_7)
        self.save_preset_button.setObjectName(u"save_preset_button")
        self.save_preset_button.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.save_preset_button.sizePolicy().hasHeightForWidth())
        self.save_preset_button.setSizePolicy(sizePolicy2)
        self.save_preset_button.setMinimumSize(QSize(120, 25))

        self.horizontalLayout_33.addWidget(self.save_preset_button)


        self.verticalLayout_8.addLayout(self.horizontalLayout_33)


        self.verticalLayout_94.addWidget(self.groupBox_7)

        self.preset_explore = QPushButton(self.groupBox_31)
        self.preset_explore.setObjectName(u"preset_explore")
        sizePolicy1.setHeightForWidth(self.preset_explore.sizePolicy().hasHeightForWidth())
        self.preset_explore.setSizePolicy(sizePolicy1)
        self.preset_explore.setMinimumSize(QSize(50, 25))
        self.preset_explore.setIcon(icon1)

        self.verticalLayout_94.addWidget(self.preset_explore)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_94.addItem(self.verticalSpacer_9)


        self.verticalLayout_97.addLayout(self.verticalLayout_94)


        self.horizontalLayout_67.addWidget(self.groupBox_31)

        self.groupBox_18 = QGroupBox(self.tab_3)
        self.groupBox_18.setObjectName(u"groupBox_18")
        sizePolicy8.setHeightForWidth(self.groupBox_18.sizePolicy().hasHeightForWidth())
        self.groupBox_18.setSizePolicy(sizePolicy8)
        self.groupBox_18.setMinimumSize(QSize(300, 270))
        self.groupBox_18.setMaximumSize(QSize(300, 270))
        self.verticalLayout_77 = QVBoxLayout(self.groupBox_18)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.horizontalLayout_66 = QHBoxLayout()
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.preset_mod_package = QCheckBox(self.groupBox_18)
        self.preset_mod_package.setObjectName(u"preset_mod_package")
        sizePolicy2.setHeightForWidth(self.preset_mod_package.sizePolicy().hasHeightForWidth())
        self.preset_mod_package.setSizePolicy(sizePolicy2)
        self.preset_mod_package.setMinimumSize(QSize(100, 25))
        self.preset_mod_package.setMaximumSize(QSize(70, 100))
        self.preset_mod_package.setChecked(True)

        self.verticalLayout_12.addWidget(self.preset_mod_package)

        self.preset_mod_parsing = QCheckBox(self.groupBox_18)
        self.preset_mod_parsing.setObjectName(u"preset_mod_parsing")
        sizePolicy2.setHeightForWidth(self.preset_mod_parsing.sizePolicy().hasHeightForWidth())
        self.preset_mod_parsing.setSizePolicy(sizePolicy2)
        self.preset_mod_parsing.setMinimumSize(QSize(100, 25))
        self.preset_mod_parsing.setMaximumSize(QSize(70, 100))
        self.preset_mod_parsing.setChecked(True)

        self.verticalLayout_12.addWidget(self.preset_mod_parsing)

        self.preset_mod_sidecar = QCheckBox(self.groupBox_18)
        self.preset_mod_sidecar.setObjectName(u"preset_mod_sidecar")
        sizePolicy2.setHeightForWidth(self.preset_mod_sidecar.sizePolicy().hasHeightForWidth())
        self.preset_mod_sidecar.setSizePolicy(sizePolicy2)
        self.preset_mod_sidecar.setMinimumSize(QSize(100, 25))
        self.preset_mod_sidecar.setMaximumSize(QSize(100, 100))
        self.preset_mod_sidecar.setChecked(True)

        self.verticalLayout_12.addWidget(self.preset_mod_sidecar)

        self.preset_mod_rename = QCheckBox(self.groupBox_18)
        self.preset_mod_rename.setObjectName(u"preset_mod_rename")
        sizePolicy2.setHeightForWidth(self.preset_mod_rename.sizePolicy().hasHeightForWidth())
        self.preset_mod_rename.setSizePolicy(sizePolicy2)
        self.preset_mod_rename.setMinimumSize(QSize(100, 25))
        self.preset_mod_rename.setMaximumSize(QSize(70, 100))
        self.preset_mod_rename.setChecked(True)

        self.verticalLayout_12.addWidget(self.preset_mod_rename)

        self.preset_mod_data = QCheckBox(self.groupBox_18)
        self.preset_mod_data.setObjectName(u"preset_mod_data")
        sizePolicy12 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy12.setHorizontalStretch(50)
        sizePolicy12.setVerticalStretch(25)
        sizePolicy12.setHeightForWidth(self.preset_mod_data.sizePolicy().hasHeightForWidth())
        self.preset_mod_data.setSizePolicy(sizePolicy12)
        self.preset_mod_data.setMinimumSize(QSize(100, 25))
        self.preset_mod_data.setMaximumSize(QSize(16777215, 100))
        self.preset_mod_data.setChecked(True)

        self.verticalLayout_12.addWidget(self.preset_mod_data)

        self.preset_mod_ftrack = QCheckBox(self.groupBox_18)
        self.preset_mod_ftrack.setObjectName(u"preset_mod_ftrack")
        sizePolicy2.setHeightForWidth(self.preset_mod_ftrack.sizePolicy().hasHeightForWidth())
        self.preset_mod_ftrack.setSizePolicy(sizePolicy2)
        self.preset_mod_ftrack.setMinimumSize(QSize(100, 25))
        self.preset_mod_ftrack.setMaximumSize(QSize(60, 100))
        self.preset_mod_ftrack.setChecked(True)

        self.verticalLayout_12.addWidget(self.preset_mod_ftrack)

        self.preset_mod_vendor = QCheckBox(self.groupBox_18)
        self.preset_mod_vendor.setObjectName(u"preset_mod_vendor")
        sizePolicy2.setHeightForWidth(self.preset_mod_vendor.sizePolicy().hasHeightForWidth())
        self.preset_mod_vendor.setSizePolicy(sizePolicy2)
        self.preset_mod_vendor.setMinimumSize(QSize(100, 25))
        self.preset_mod_vendor.setMaximumSize(QSize(70, 100))
        self.preset_mod_vendor.setChecked(True)

        self.verticalLayout_12.addWidget(self.preset_mod_vendor)

        self.preset_mod_replace = QCheckBox(self.groupBox_18)
        self.preset_mod_replace.setObjectName(u"preset_mod_replace")
        sizePolicy2.setHeightForWidth(self.preset_mod_replace.sizePolicy().hasHeightForWidth())
        self.preset_mod_replace.setSizePolicy(sizePolicy2)
        self.preset_mod_replace.setMinimumSize(QSize(100, 25))
        self.preset_mod_replace.setMaximumSize(QSize(100, 25))
        self.preset_mod_replace.setChecked(True)

        self.verticalLayout_12.addWidget(self.preset_mod_replace)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_12)


        self.horizontalLayout_66.addLayout(self.verticalLayout_12)

        self.verticalLayout_72 = QVBoxLayout()
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.preset_mod_convert = QCheckBox(self.groupBox_18)
        self.preset_mod_convert.setObjectName(u"preset_mod_convert")
        sizePolicy2.setHeightForWidth(self.preset_mod_convert.sizePolicy().hasHeightForWidth())
        self.preset_mod_convert.setSizePolicy(sizePolicy2)
        self.preset_mod_convert.setMinimumSize(QSize(100, 25))
        self.preset_mod_convert.setMaximumSize(QSize(70, 100))
        self.preset_mod_convert.setChecked(True)

        self.verticalLayout_72.addWidget(self.preset_mod_convert)

        self.preset_mod_spreadsheet = QCheckBox(self.groupBox_18)
        self.preset_mod_spreadsheet.setObjectName(u"preset_mod_spreadsheet")
        sizePolicy2.setHeightForWidth(self.preset_mod_spreadsheet.sizePolicy().hasHeightForWidth())
        self.preset_mod_spreadsheet.setSizePolicy(sizePolicy2)
        self.preset_mod_spreadsheet.setMinimumSize(QSize(100, 25))
        self.preset_mod_spreadsheet.setMaximumSize(QSize(100, 100))
        self.preset_mod_spreadsheet.setChecked(True)

        self.verticalLayout_72.addWidget(self.preset_mod_spreadsheet)

        self.preset_mod_text = QCheckBox(self.groupBox_18)
        self.preset_mod_text.setObjectName(u"preset_mod_text")
        sizePolicy2.setHeightForWidth(self.preset_mod_text.sizePolicy().hasHeightForWidth())
        self.preset_mod_text.setSizePolicy(sizePolicy2)
        self.preset_mod_text.setMinimumSize(QSize(100, 25))
        self.preset_mod_text.setMaximumSize(QSize(50, 100))
        self.preset_mod_text.setChecked(True)

        self.verticalLayout_72.addWidget(self.preset_mod_text)

        self.preset_mod_checks = QCheckBox(self.groupBox_18)
        self.preset_mod_checks.setObjectName(u"preset_mod_checks")
        sizePolicy2.setHeightForWidth(self.preset_mod_checks.sizePolicy().hasHeightForWidth())
        self.preset_mod_checks.setSizePolicy(sizePolicy2)
        self.preset_mod_checks.setMinimumSize(QSize(100, 25))
        self.preset_mod_checks.setMaximumSize(QSize(70, 100))
        self.preset_mod_checks.setChecked(True)

        self.verticalLayout_72.addWidget(self.preset_mod_checks)

        self.preset_mod_deadline = QCheckBox(self.groupBox_18)
        self.preset_mod_deadline.setObjectName(u"preset_mod_deadline")
        sizePolicy2.setHeightForWidth(self.preset_mod_deadline.sizePolicy().hasHeightForWidth())
        self.preset_mod_deadline.setSizePolicy(sizePolicy2)
        self.preset_mod_deadline.setMinimumSize(QSize(100, 25))
        self.preset_mod_deadline.setMaximumSize(QSize(16777215, 100))
        self.preset_mod_deadline.setChecked(True)

        self.verticalLayout_72.addWidget(self.preset_mod_deadline)

        self.preset_mod_ayon = QCheckBox(self.groupBox_18)
        self.preset_mod_ayon.setObjectName(u"preset_mod_ayon")
        sizePolicy2.setHeightForWidth(self.preset_mod_ayon.sizePolicy().hasHeightForWidth())
        self.preset_mod_ayon.setSizePolicy(sizePolicy2)
        self.preset_mod_ayon.setMinimumSize(QSize(100, 25))
        self.preset_mod_ayon.setMaximumSize(QSize(16777215, 100))
        self.preset_mod_ayon.setChecked(True)

        self.verticalLayout_72.addWidget(self.preset_mod_ayon)

        self.preset_mod_preferences = QCheckBox(self.groupBox_18)
        self.preset_mod_preferences.setObjectName(u"preset_mod_preferences")
        sizePolicy2.setHeightForWidth(self.preset_mod_preferences.sizePolicy().hasHeightForWidth())
        self.preset_mod_preferences.setSizePolicy(sizePolicy2)
        self.preset_mod_preferences.setMinimumSize(QSize(100, 25))
        self.preset_mod_preferences.setMaximumSize(QSize(16777215, 100))
        self.preset_mod_preferences.setChecked(True)

        self.verticalLayout_72.addWidget(self.preset_mod_preferences)

        self.preset_mod_exports = QCheckBox(self.groupBox_18)
        self.preset_mod_exports.setObjectName(u"preset_mod_exports")
        sizePolicy2.setHeightForWidth(self.preset_mod_exports.sizePolicy().hasHeightForWidth())
        self.preset_mod_exports.setSizePolicy(sizePolicy2)
        self.preset_mod_exports.setMinimumSize(QSize(100, 25))
        self.preset_mod_exports.setMaximumSize(QSize(16777215, 100))
        self.preset_mod_exports.setChecked(True)

        self.verticalLayout_72.addWidget(self.preset_mod_exports)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_72.addItem(self.verticalSpacer_13)


        self.horizontalLayout_66.addLayout(self.verticalLayout_72)

        self.verticalLayout_73 = QVBoxLayout()
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.preset_mod_log = QCheckBox(self.groupBox_18)
        self.preset_mod_log.setObjectName(u"preset_mod_log")
        sizePolicy2.setHeightForWidth(self.preset_mod_log.sizePolicy().hasHeightForWidth())
        self.preset_mod_log.setSizePolicy(sizePolicy2)
        self.preset_mod_log.setMinimumSize(QSize(100, 25))
        self.preset_mod_log.setMaximumSize(QSize(16777215, 100))
        self.preset_mod_log.setChecked(True)

        self.verticalLayout_73.addWidget(self.preset_mod_log)

        self.preset_mod_help = QCheckBox(self.groupBox_18)
        self.preset_mod_help.setObjectName(u"preset_mod_help")
        sizePolicy2.setHeightForWidth(self.preset_mod_help.sizePolicy().hasHeightForWidth())
        self.preset_mod_help.setSizePolicy(sizePolicy2)
        self.preset_mod_help.setMinimumSize(QSize(60, 25))
        self.preset_mod_help.setMaximumSize(QSize(16777215, 60))
        self.preset_mod_help.setChecked(True)

        self.verticalLayout_73.addWidget(self.preset_mod_help)

        self.preset_mod_submission = QCheckBox(self.groupBox_18)
        self.preset_mod_submission.setObjectName(u"preset_mod_submission")
        sizePolicy2.setHeightForWidth(self.preset_mod_submission.sizePolicy().hasHeightForWidth())
        self.preset_mod_submission.setSizePolicy(sizePolicy2)
        self.preset_mod_submission.setMinimumSize(QSize(80, 25))
        self.preset_mod_submission.setMaximumSize(QSize(80, 25))
        self.preset_mod_submission.setChecked(True)

        self.verticalLayout_73.addWidget(self.preset_mod_submission)

        self.preset_mod_drivelog = QCheckBox(self.groupBox_18)
        self.preset_mod_drivelog.setObjectName(u"preset_mod_drivelog")
        sizePolicy2.setHeightForWidth(self.preset_mod_drivelog.sizePolicy().hasHeightForWidth())
        self.preset_mod_drivelog.setSizePolicy(sizePolicy2)
        self.preset_mod_drivelog.setMinimumSize(QSize(80, 25))
        self.preset_mod_drivelog.setMaximumSize(QSize(80, 25))
        self.preset_mod_drivelog.setChecked(True)

        self.verticalLayout_73.addWidget(self.preset_mod_drivelog)

        self.preset_mod_inspector = QCheckBox(self.groupBox_18)
        self.preset_mod_inspector.setObjectName(u"preset_mod_inspector")
        sizePolicy2.setHeightForWidth(self.preset_mod_inspector.sizePolicy().hasHeightForWidth())
        self.preset_mod_inspector.setSizePolicy(sizePolicy2)
        self.preset_mod_inspector.setMinimumSize(QSize(80, 25))
        self.preset_mod_inspector.setMaximumSize(QSize(80, 25))
        self.preset_mod_inspector.setChecked(True)

        self.verticalLayout_73.addWidget(self.preset_mod_inspector)

        self.preset_mod_files = QCheckBox(self.groupBox_18)
        self.preset_mod_files.setObjectName(u"preset_mod_files")
        sizePolicy2.setHeightForWidth(self.preset_mod_files.sizePolicy().hasHeightForWidth())
        self.preset_mod_files.setSizePolicy(sizePolicy2)
        self.preset_mod_files.setMinimumSize(QSize(80, 25))
        self.preset_mod_files.setMaximumSize(QSize(80, 25))
        self.preset_mod_files.setChecked(True)

        self.verticalLayout_73.addWidget(self.preset_mod_files)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_73.addItem(self.verticalSpacer_8)


        self.horizontalLayout_66.addLayout(self.verticalLayout_73)


        self.verticalLayout_77.addLayout(self.horizontalLayout_66)


        self.horizontalLayout_67.addWidget(self.groupBox_18)


        self.verticalLayout_95.addLayout(self.horizontalLayout_67)

        self.TopTab.addTab(self.tab_3, "")
        self.tab_21 = QWidget()
        self.tab_21.setObjectName(u"tab_21")
        self.verticalLayout_71 = QVBoxLayout(self.tab_21)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.log = QPlainTextEdit(self.tab_21)
        self.log.setObjectName(u"log")

        self.verticalLayout_71.addWidget(self.log)

        self.TopTab.addTab(self.tab_21, "")
        self.tab_14 = QWidget()
        self.tab_14.setObjectName(u"tab_14")
        self.horizontalLayout_91 = QHBoxLayout(self.tab_14)
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.textEdit = QTextEdit(self.tab_14)
        self.textEdit.setObjectName(u"textEdit")

        self.horizontalLayout_91.addWidget(self.textEdit)

        self.TopTab.addTab(self.tab_14, "")

        self.verticalLayout_15.addWidget(self.TopTab)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.BottomTab = QTabWidget(self.centralwidget)
        self.BottomTab.setObjectName(u"BottomTab")
        sizePolicy3.setHeightForWidth(self.BottomTab.sizePolicy().hasHeightForWidth())
        self.BottomTab.setSizePolicy(sizePolicy3)
        self.BottomTab.setMinimumSize(QSize(670, 175))
        self.BottomTab.setMaximumSize(QSize(16777215, 16777215))
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.horizontalLayout_113 = QHBoxLayout(self.tab_6)
        self.horizontalLayout_113.setObjectName(u"horizontalLayout_113")
        self.sub_table = QTableWidget(self.tab_6)
        self.sub_table.setObjectName(u"sub_table")
        sizePolicy.setHeightForWidth(self.sub_table.sizePolicy().hasHeightForWidth())
        self.sub_table.setSizePolicy(sizePolicy)
        self.sub_table.setMinimumSize(QSize(600, 100))
        self.sub_table.setMaximumSize(QSize(16000, 16000))

        self.horizontalLayout_113.addWidget(self.sub_table)

        self.BottomTab.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.verticalLayout_41 = QVBoxLayout(self.tab_7)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.log_table = QTableWidget(self.tab_7)
        self.log_table.setObjectName(u"log_table")
        sizePolicy.setHeightForWidth(self.log_table.sizePolicy().hasHeightForWidth())
        self.log_table.setSizePolicy(sizePolicy)
        self.log_table.setMinimumSize(QSize(600, 100))
        self.log_table.setMaximumSize(QSize(16000, 16000))

        self.verticalLayout_41.addWidget(self.log_table)

        self.BottomTab.addTab(self.tab_7, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.verticalLayout_42 = QVBoxLayout(self.tab_8)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.txt_table = QTextEdit(self.tab_8)
        self.txt_table.setObjectName(u"txt_table")
        sizePolicy.setHeightForWidth(self.txt_table.sizePolicy().hasHeightForWidth())
        self.txt_table.setSizePolicy(sizePolicy)
        self.txt_table.setMinimumSize(QSize(600, 100))

        self.verticalLayout_42.addWidget(self.txt_table)

        self.BottomTab.addTab(self.tab_8, "")
        self.tab_15 = QWidget()
        self.tab_15.setObjectName(u"tab_15")
        self.horizontalLayout_139 = QHBoxLayout(self.tab_15)
        self.horizontalLayout_139.setObjectName(u"horizontalLayout_139")
        self.side_table = QTableWidget(self.tab_15)
        self.side_table.setObjectName(u"side_table")
        sizePolicy.setHeightForWidth(self.side_table.sizePolicy().hasHeightForWidth())
        self.side_table.setSizePolicy(sizePolicy)
        self.side_table.setMinimumSize(QSize(600, 100))
        self.side_table.setMaximumSize(QSize(16000, 16000))

        self.horizontalLayout_139.addWidget(self.side_table)

        self.BottomTab.addTab(self.tab_15, "")
        self.tab_20 = QWidget()
        self.tab_20.setObjectName(u"tab_20")
        self.verticalLayout_70 = QVBoxLayout(self.tab_20)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.verticalLayout_69 = QVBoxLayout()
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.groupBox_16 = QGroupBox(self.tab_20)
        self.groupBox_16.setObjectName(u"groupBox_16")
        sizePolicy1.setHeightForWidth(self.groupBox_16.sizePolicy().hasHeightForWidth())
        self.groupBox_16.setSizePolicy(sizePolicy1)
        self.groupBox_16.setMinimumSize(QSize(375, 55))
        self.groupBox_16.setMaximumSize(QSize(16777215, 55))
        self.horizontalLayout_65 = QHBoxLayout(self.groupBox_16)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_64 = QHBoxLayout()
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_60 = QHBoxLayout()
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.rename_tab_relative = QRadioButton(self.groupBox_16)
        self.rename_tab_relative.setObjectName(u"rename_tab_relative")
        sizePolicy2.setHeightForWidth(self.rename_tab_relative.sizePolicy().hasHeightForWidth())
        self.rename_tab_relative.setSizePolicy(sizePolicy2)
        self.rename_tab_relative.setMinimumSize(QSize(150, 25))
        self.rename_tab_relative.setMaximumSize(QSize(150, 25))

        self.horizontalLayout_60.addWidget(self.rename_tab_relative)

        self.rename_tab_absolute = QRadioButton(self.groupBox_16)
        self.rename_tab_absolute.setObjectName(u"rename_tab_absolute")
        sizePolicy2.setHeightForWidth(self.rename_tab_absolute.sizePolicy().hasHeightForWidth())
        self.rename_tab_absolute.setSizePolicy(sizePolicy2)
        self.rename_tab_absolute.setMinimumSize(QSize(150, 25))
        self.rename_tab_absolute.setMaximumSize(QSize(150, 25))

        self.horizontalLayout_60.addWidget(self.rename_tab_absolute)

        self.rename_tab_names_only = QRadioButton(self.groupBox_16)
        self.rename_tab_names_only.setObjectName(u"rename_tab_names_only")
        sizePolicy2.setHeightForWidth(self.rename_tab_names_only.sizePolicy().hasHeightForWidth())
        self.rename_tab_names_only.setSizePolicy(sizePolicy2)
        self.rename_tab_names_only.setMinimumSize(QSize(150, 25))
        self.rename_tab_names_only.setMaximumSize(QSize(150, 25))

        self.horizontalLayout_60.addWidget(self.rename_tab_names_only)


        self.horizontalLayout_64.addLayout(self.horizontalLayout_60)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_64.addItem(self.horizontalSpacer_23)


        self.horizontalLayout_65.addLayout(self.horizontalLayout_64)


        self.verticalLayout_69.addWidget(self.groupBox_16)

        self.rename_table = QTableWidget(self.tab_20)
        self.rename_table.setObjectName(u"rename_table")
        sizePolicy.setHeightForWidth(self.rename_table.sizePolicy().hasHeightForWidth())
        self.rename_table.setSizePolicy(sizePolicy)
        self.rename_table.setMinimumSize(QSize(600, 30))
        self.rename_table.setMaximumSize(QSize(16000, 16000))

        self.verticalLayout_69.addWidget(self.rename_table)


        self.verticalLayout_70.addLayout(self.verticalLayout_69)

        self.BottomTab.addTab(self.tab_20, "")
        self.tab_19 = QWidget()
        self.tab_19.setObjectName(u"tab_19")
        self.verticalLayout_39 = QVBoxLayout(self.tab_19)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_36 = QVBoxLayout()
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.horizontalLayout_53 = QHBoxLayout()
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.label_23 = QLabel(self.tab_19)
        self.label_23.setObjectName(u"label_23")
        sizePolicy2.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy2)
        self.label_23.setMinimumSize(QSize(50, 25))
        self.label_23.setMaximumSize(QSize(50, 25))

        self.horizontalLayout_53.addWidget(self.label_23)

        self.tree_filter_file = QLineEdit(self.tab_19)
        self.tree_filter_file.setObjectName(u"tree_filter_file")
        sizePolicy1.setHeightForWidth(self.tree_filter_file.sizePolicy().hasHeightForWidth())
        self.tree_filter_file.setSizePolicy(sizePolicy1)
        self.tree_filter_file.setMinimumSize(QSize(200, 25))
        self.tree_filter_file.setMaximumSize(QSize(16000, 25))

        self.horizontalLayout_53.addWidget(self.tree_filter_file)

        self.label_24 = QLabel(self.tab_19)
        self.label_24.setObjectName(u"label_24")
        sizePolicy2.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy2)
        self.label_24.setMinimumSize(QSize(50, 25))
        self.label_24.setMaximumSize(QSize(50, 25))

        self.horizontalLayout_53.addWidget(self.label_24)

        self.tree_filter_key = QLineEdit(self.tab_19)
        self.tree_filter_key.setObjectName(u"tree_filter_key")
        sizePolicy1.setHeightForWidth(self.tree_filter_key.sizePolicy().hasHeightForWidth())
        self.tree_filter_key.setSizePolicy(sizePolicy1)
        self.tree_filter_key.setMinimumSize(QSize(200, 25))
        self.tree_filter_key.setMaximumSize(QSize(16000, 25))

        self.horizontalLayout_53.addWidget(self.tree_filter_key)

        self.label_25 = QLabel(self.tab_19)
        self.label_25.setObjectName(u"label_25")
        sizePolicy2.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy2)
        self.label_25.setMinimumSize(QSize(50, 25))
        self.label_25.setMaximumSize(QSize(50, 25))

        self.horizontalLayout_53.addWidget(self.label_25)

        self.tree_filter_value = QLineEdit(self.tab_19)
        self.tree_filter_value.setObjectName(u"tree_filter_value")
        sizePolicy1.setHeightForWidth(self.tree_filter_value.sizePolicy().hasHeightForWidth())
        self.tree_filter_value.setSizePolicy(sizePolicy1)
        self.tree_filter_value.setMinimumSize(QSize(200, 25))
        self.tree_filter_value.setMaximumSize(QSize(16000, 25))

        self.horizontalLayout_53.addWidget(self.tree_filter_value)


        self.verticalLayout_36.addLayout(self.horizontalLayout_53)

        self.data_tree = QTreeWidget(self.tab_19)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(2, u"3");
        __qtreewidgetitem.setText(1, u"2");
        __qtreewidgetitem.setText(0, u"1");
        self.data_tree.setHeaderItem(__qtreewidgetitem)
        self.data_tree.setObjectName(u"data_tree")
        self.data_tree.setColumnCount(3)

        self.verticalLayout_36.addWidget(self.data_tree)


        self.verticalLayout_39.addLayout(self.verticalLayout_36)

        self.BottomTab.addTab(self.tab_19, "")
        self.tab_22 = QWidget()
        self.tab_22.setObjectName(u"tab_22")
        self.verticalLayout_37 = QVBoxLayout(self.tab_22)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.file_table = QTableWidget(self.tab_22)
        self.file_table.setObjectName(u"file_table")
        sizePolicy.setHeightForWidth(self.file_table.sizePolicy().hasHeightForWidth())
        self.file_table.setSizePolicy(sizePolicy)
        self.file_table.setMinimumSize(QSize(600, 100))
        self.file_table.setMaximumSize(QSize(16000, 16000))

        self.verticalLayout_37.addWidget(self.file_table)

        self.BottomTab.addTab(self.tab_22, "")

        self.verticalLayout_10.addWidget(self.BottomTab)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.write_button = QPushButton(self.centralwidget)
        self.write_button.setObjectName(u"write_button")
        sizePolicy1.setHeightForWidth(self.write_button.sizePolicy().hasHeightForWidth())
        self.write_button.setSizePolicy(sizePolicy1)
        self.write_button.setMinimumSize(QSize(350, 40))
        self.write_button.setMaximumSize(QSize(16777215, 40))
        self.write_button.setBaseSize(QSize(520, 51))
        self.write_button.setAutoFillBackground(False)
        self.write_button.setStyleSheet(u"")
        self.write_button.setFlat(True)

        self.horizontalLayout_3.addWidget(self.write_button)

        self.publish_local_button = QPushButton(self.centralwidget)
        self.publish_local_button.setObjectName(u"publish_local_button")
        self.publish_local_button.setMinimumSize(QSize(180, 40))
        self.publish_local_button.setMaximumSize(QSize(180, 40))

        self.horizontalLayout_3.addWidget(self.publish_local_button)

        self.publish_farm_button = QPushButton(self.centralwidget)
        self.publish_farm_button.setObjectName(u"publish_farm_button")
        self.publish_farm_button.setMinimumSize(QSize(180, 40))
        self.publish_farm_button.setMaximumSize(QSize(180, 70))

        self.horizontalLayout_3.addWidget(self.publish_farm_button)

        self.reload = QPushButton(self.centralwidget)
        self.reload.setObjectName(u"reload")
        sizePolicy2.setHeightForWidth(self.reload.sizePolicy().hasHeightForWidth())
        self.reload.setSizePolicy(sizePolicy2)
        self.reload.setMinimumSize(QSize(70, 40))
        self.reload.setMaximumSize(QSize(70, 40))
        self.reload.setBaseSize(QSize(520, 51))
        self.reload.setAutoFillBackground(False)
        self.reload.setFlat(True)

        self.horizontalLayout_3.addWidget(self.reload)


        self.verticalLayout_10.addLayout(self.horizontalLayout_3)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(0, 12))
        self.progressBar.setMaximumSize(QSize(16777215, 12))
        font = QFont()
        font.setPointSize(10)
        self.progressBar.setFont(font)
        self.progressBar.setValue(0)

        self.verticalLayout_10.addWidget(self.progressBar)


        self.verticalLayout_15.addLayout(self.verticalLayout_10)


        self.verticalLayout_50.addLayout(self.verticalLayout_15)

        submission.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(submission)
        self.statusBar.setObjectName(u"statusBar")
        sizePolicy13 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.statusBar.sizePolicy().hasHeightForWidth())
        self.statusBar.setSizePolicy(sizePolicy13)
        submission.setStatusBar(self.statusBar)

        self.retranslateUi(submission)

        self.TopTab.setCurrentIndex(13)
        self.package_explore.setDefault(True)
        self.package_browse.setDefault(True)
        self.package_explore_2.setDefault(True)
        self.package_browse_2.setDefault(True)
        self.data_csv_browse.setDefault(True)
        self.vendor_csv_explore.setDefault(True)
        self.vendor_csv_browse.setDefault(True)
        self.data_csv_browse_2.setDefault(True)
        self.ayon_path_browse_2.setDefault(True)
        self.BottomTab.setCurrentIndex(0)
        self.write_button.setDefault(True)
        self.reload.setDefault(True)


        QMetaObject.connectSlotsByName(submission)
    # setupUi

    def retranslateUi(self, submission):
        submission.setWindowTitle(QCoreApplication.translate("submission", u"Submission Helper 2.0", None))
#if QT_CONFIG(tooltip)
        submission.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.TopTab.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.groupBox.setToolTip(QCoreApplication.translate("submission", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox.setTitle(QCoreApplication.translate("submission", u"Package Folder:", None))
#if QT_CONFIG(tooltip)
        self.package_folder.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>Expects path to folder containing media files.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.package_folder.setText("")
#if QT_CONFIG(tooltip)
        self.package_explore.setToolTip(QCoreApplication.translate("submission", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Opens video directory with system file manager (Explorer, Finder...).</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.package_explore.setText("")
#if QT_CONFIG(tooltip)
        self.package_browse.setToolTip(QCoreApplication.translate("submission", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:11px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Browse for video file.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.package_browse.setText("")
        self.groupBox_8.setTitle(QCoreApplication.translate("submission", u"Package Name:", None))
        self.label_10.setText(QCoreApplication.translate("submission", u"Template:", None))
#if QT_CONFIG(tooltip)
        self.name_template.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>Template for naming the package. <br/><br/>Keywords:<br/>{package_version} : detects consecutive versions one folder up from package folder<br/>{yy}: year<br/>{mm}: month<br/>{dd}: day</p><p><br/></p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.name_template.setText(QCoreApplication.translate("submission", u"sub_{yy}{mm}{dd}_{package_version}", None))
        self.label_37.setText(QCoreApplication.translate("submission", u"Date Regex:", None))
#if QT_CONFIG(tooltip)
        self.name_date_regex.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>Renamer checks all folders one folder above the package folder<br/>and detects current date stamp in it by using Date Regex</p><p><br/>Keywords:<br/>{yy}: year<br/>{mm}: month<br/>{dd}: day</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.name_date_regex.setText(QCoreApplication.translate("submission", u"sub_{yy}{mm}{dd}", None))
        self.label_76.setText(QCoreApplication.translate("submission", u"Version Regex:", None))
#if QT_CONFIG(tooltip)
        self.name_version_regex.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>Renamer checks all folders one folder above the package folder<br/>and detects version in it by using Version Regex</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.name_version_regex.setText(QCoreApplication.translate("submission", u"_(\\d{3})$", None))
        self.name_version_regex.setPlaceholderText(QCoreApplication.translate("submission", u"preview", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("submission", u"Version", None))
#if QT_CONFIG(tooltip)
        self.name_version_per_date.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>Each date, versions start from A or 1.<br/>If unchecked, package versions are contunuous, not depending on date.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.name_version_per_date.setText(QCoreApplication.translate("submission", u"Per Date", None))
        self.name_version_leading_zeroes.setText(QCoreApplication.translate("submission", u"Leading Zeroes:", None))
#if QT_CONFIG(tooltip)
        self.name_version_zeroes.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>For numbered versions, use leading zeroes</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.name_version_use_letters.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>Use letters instead of numbers for versioning</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.name_version_use_letters.setText(QCoreApplication.translate("submission", u"Letter", None))
#if QT_CONFIG(tooltip)
        self.name_version_letters_uppercase.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>If using letters for versioning, use upper case instead of lower case letters</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.name_version_letters_uppercase.setText(QCoreApplication.translate("submission", u"Upper Case", None))
        self.groupBox_20.setTitle(QCoreApplication.translate("submission", u"Name From", None))
        self.name_from_template.setText(QCoreApplication.translate("submission", u"Template", None))
        self.name_from_folder.setText(QCoreApplication.translate("submission", u"Folder", None))
        self.name_rename.setText(QCoreApplication.translate("submission", u"Rename", None))
        self.name_rename_auto.setText(QCoreApplication.translate("submission", u"Auto Rename", None))
        self.label_36.setText(QCoreApplication.translate("submission", u"Preview:", None))
#if QT_CONFIG(tooltip)
        self.name_preview.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>Renamer checks all folders one folder above the package folder.<br/>For every folder there, it tries to detect date stamp and version  by the regexes.<br/>Then it produces {package_version} keyword, depending on Version options.<br/>Finally, the package name is constructed by Template that contains {package_version} keyword.<br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.name_preview.setText("")
        self.name_preview.setPlaceholderText(QCoreApplication.translate("submission", u"preview", None))
        self.TopTab.setTabText(self.TopTab.indexOf(self.tab), QCoreApplication.translate("submission", u"Package", None))
#if QT_CONFIG(tooltip)
        self.scrollArea.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>Creating new keys<br/>1. source is the text to be searched. For every file, the {keys} are replaced first</p><p>2. Pattern is used for Python re.sub regex</p><p>3. Repl is used for Python re.sub replace. If itr starts with lambda, the repl is evaluated as Python</p><p>4. Result (found group 1 or replace) is named by the name field</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_18.setText(QCoreApplication.translate("submission", u"Name:", None))
        self.parse_name_01.setText(QCoreApplication.translate("submission", u"shot", None))
        self.label_20.setText(QCoreApplication.translate("submission", u"Pattern:", None))
        self.parse_pattern_01.setText(QCoreApplication.translate("submission", u"([^_*]_[^_*]_)", None))
        self.label_19.setText(QCoreApplication.translate("submission", u"Repl:", None))
        self.label_21.setText(QCoreApplication.translate("submission", u"Source:", None))
        self.parse_source_01.setText(QCoreApplication.translate("submission", u"{name}", None))
        self.label_77.setText(QCoreApplication.translate("submission", u"Filter:", None))
        self.parse_filter_01.setText("")
        self.label_170.setText(QCoreApplication.translate("submission", u"Name:", None))
        self.label_171.setText(QCoreApplication.translate("submission", u"Pattern:", None))
        self.label_172.setText(QCoreApplication.translate("submission", u"Repl:", None))
        self.label_173.setText(QCoreApplication.translate("submission", u"Source:", None))
        self.label_174.setText(QCoreApplication.translate("submission", u"Filter:", None))
        self.label_22.setText(QCoreApplication.translate("submission", u"Name:", None))
        self.label_38.setText(QCoreApplication.translate("submission", u"Pattern:", None))
        self.label_39.setText(QCoreApplication.translate("submission", u"Repl:", None))
        self.label_40.setText(QCoreApplication.translate("submission", u"Source:", None))
        self.label_78.setText(QCoreApplication.translate("submission", u"Filter:", None))
        self.label_175.setText(QCoreApplication.translate("submission", u"Name:", None))
        self.label_176.setText(QCoreApplication.translate("submission", u"Pattern:", None))
        self.label_177.setText(QCoreApplication.translate("submission", u"Repl:", None))
        self.label_178.setText(QCoreApplication.translate("submission", u"Source:", None))
        self.label_179.setText(QCoreApplication.translate("submission", u"Filter:", None))
        self.label_41.setText(QCoreApplication.translate("submission", u"Name:", None))
        self.label_42.setText(QCoreApplication.translate("submission", u"Pattern:", None))
        self.label_43.setText(QCoreApplication.translate("submission", u"Repl:", None))
        self.label_44.setText(QCoreApplication.translate("submission", u"Source:", None))
        self.label_79.setText(QCoreApplication.translate("submission", u"Filter:", None))
        self.label_180.setText(QCoreApplication.translate("submission", u"Name:", None))
        self.label_181.setText(QCoreApplication.translate("submission", u"Pattern:", None))
        self.label_182.setText(QCoreApplication.translate("submission", u"Repl:", None))
        self.label_183.setText(QCoreApplication.translate("submission", u"Source:", None))
        self.label_184.setText(QCoreApplication.translate("submission", u"Filter:", None))
        self.label_47.setText(QCoreApplication.translate("submission", u"Name:", None))
        self.label_48.setText(QCoreApplication.translate("submission", u"Pattern:", None))
        self.label_49.setText(QCoreApplication.translate("submission", u"Repl:", None))
        self.label_50.setText(QCoreApplication.translate("submission", u"Source:", None))
        self.label_80.setText(QCoreApplication.translate("submission", u"Filter:", None))
        self.label_185.setText(QCoreApplication.translate("submission", u"Name:", None))
        self.label_186.setText(QCoreApplication.translate("submission", u"Pattern:", None))
        self.label_187.setText(QCoreApplication.translate("submission", u"Repl:", None))
        self.label_188.setText(QCoreApplication.translate("submission", u"Source:", None))
        self.label_189.setText(QCoreApplication.translate("submission", u"Filter:", None))
        self.label_55.setText(QCoreApplication.translate("submission", u"Name:", None))
        self.label_56.setText(QCoreApplication.translate("submission", u"Pattern:", None))
        self.label_57.setText(QCoreApplication.translate("submission", u"Repl:", None))
        self.label_58.setText(QCoreApplication.translate("submission", u"Source:", None))
        self.label_81.setText(QCoreApplication.translate("submission", u"Filter:", None))
        self.label_190.setText(QCoreApplication.translate("submission", u"Name:", None))
        self.label_191.setText(QCoreApplication.translate("submission", u"Pattern:", None))
        self.label_192.setText(QCoreApplication.translate("submission", u"Repl:", None))
        self.label_193.setText(QCoreApplication.translate("submission", u"Source:", None))
        self.label_194.setText(QCoreApplication.translate("submission", u"Filter:", None))
        self.label_59.setText(QCoreApplication.translate("submission", u"Name:", None))
        self.label_60.setText(QCoreApplication.translate("submission", u"Pattern:", None))
        self.label_61.setText(QCoreApplication.translate("submission", u"Repl:", None))
        self.label_62.setText(QCoreApplication.translate("submission", u"Source:", None))
        self.label_82.setText(QCoreApplication.translate("submission", u"Filter:", None))
        self.label_195.setText(QCoreApplication.translate("submission", u"Name:", None))
        self.label_196.setText(QCoreApplication.translate("submission", u"Pattern:", None))
        self.label_197.setText(QCoreApplication.translate("submission", u"Repl:", None))
        self.label_198.setText(QCoreApplication.translate("submission", u"Source:", None))
        self.label_199.setText(QCoreApplication.translate("submission", u"Filter:", None))
        self.label_63.setText(QCoreApplication.translate("submission", u"Name:", None))
        self.label_64.setText(QCoreApplication.translate("submission", u"Pattern:", None))
        self.label_65.setText(QCoreApplication.translate("submission", u"Repl:", None))
        self.label_66.setText(QCoreApplication.translate("submission", u"Source:", None))
        self.label_83.setText(QCoreApplication.translate("submission", u"Filter:", None))
        self.label_200.setText(QCoreApplication.translate("submission", u"Name:", None))
        self.label_201.setText(QCoreApplication.translate("submission", u"Pattern:", None))
        self.label_202.setText(QCoreApplication.translate("submission", u"Repl:", None))
        self.label_203.setText(QCoreApplication.translate("submission", u"Source:", None))
        self.label_204.setText(QCoreApplication.translate("submission", u"Filter:", None))
        self.label_205.setText(QCoreApplication.translate("submission", u"Name:", None))
        self.label_206.setText(QCoreApplication.translate("submission", u"Pattern:", None))
        self.label_207.setText(QCoreApplication.translate("submission", u"Repl:", None))
        self.label_208.setText(QCoreApplication.translate("submission", u"Source:", None))
        self.label_209.setText(QCoreApplication.translate("submission", u"Filter:", None))
        self.label_67.setText(QCoreApplication.translate("submission", u"Name:", None))
        self.label_68.setText(QCoreApplication.translate("submission", u"Pattern:", None))
        self.label_69.setText(QCoreApplication.translate("submission", u"Repl:", None))
        self.label_70.setText(QCoreApplication.translate("submission", u"Source:", None))
        self.label_84.setText(QCoreApplication.translate("submission", u"Filter:", None))
        self.label_210.setText(QCoreApplication.translate("submission", u"Name:", None))
        self.label_211.setText(QCoreApplication.translate("submission", u"Pattern:", None))
        self.label_212.setText(QCoreApplication.translate("submission", u"Repl:", None))
        self.label_213.setText(QCoreApplication.translate("submission", u"Source:", None))
        self.label_214.setText(QCoreApplication.translate("submission", u"Filter:", None))
        self.label_71.setText(QCoreApplication.translate("submission", u"Name:", None))
        self.label_72.setText(QCoreApplication.translate("submission", u"Pattern:", None))
        self.label_73.setText(QCoreApplication.translate("submission", u"Repl:", None))
        self.label_74.setText(QCoreApplication.translate("submission", u"Source:", None))
        self.label_85.setText(QCoreApplication.translate("submission", u"Filter:", None))
        self.label_215.setText(QCoreApplication.translate("submission", u"Name:", None))
        self.label_216.setText(QCoreApplication.translate("submission", u"Pattern:", None))
        self.label_217.setText(QCoreApplication.translate("submission", u"Repl:", None))
        self.label_218.setText(QCoreApplication.translate("submission", u"Source:", None))
        self.label_219.setText(QCoreApplication.translate("submission", u"Filter:", None))
        self.label_87.setText(QCoreApplication.translate("submission", u"Name:", None))
        self.label_114.setText(QCoreApplication.translate("submission", u"Pattern:", None))
        self.label_115.setText(QCoreApplication.translate("submission", u"Repl:", None))
        self.label_116.setText(QCoreApplication.translate("submission", u"Source:", None))
        self.label_117.setText(QCoreApplication.translate("submission", u"Filter:", None))
        self.label_220.setText(QCoreApplication.translate("submission", u"Name:", None))
        self.label_221.setText(QCoreApplication.translate("submission", u"Pattern:", None))
        self.label_222.setText(QCoreApplication.translate("submission", u"Repl:", None))
        self.label_223.setText(QCoreApplication.translate("submission", u"Source:", None))
        self.label_224.setText(QCoreApplication.translate("submission", u"Filter:", None))
        self.label_118.setText(QCoreApplication.translate("submission", u"Name:", None))
        self.label_119.setText(QCoreApplication.translate("submission", u"Pattern:", None))
        self.label_120.setText(QCoreApplication.translate("submission", u"Repl:", None))
        self.label_121.setText(QCoreApplication.translate("submission", u"Source:", None))
        self.label_122.setText(QCoreApplication.translate("submission", u"Filter:", None))
        self.label_225.setText(QCoreApplication.translate("submission", u"Name:", None))
        self.label_226.setText(QCoreApplication.translate("submission", u"Pattern:", None))
        self.label_227.setText(QCoreApplication.translate("submission", u"Repl:", None))
        self.label_228.setText(QCoreApplication.translate("submission", u"Source:", None))
        self.label_229.setText(QCoreApplication.translate("submission", u"Filter:", None))
        self.label_123.setText(QCoreApplication.translate("submission", u"Name:", None))
        self.label_124.setText(QCoreApplication.translate("submission", u"Pattern:", None))
        self.label_125.setText(QCoreApplication.translate("submission", u"Repl:", None))
        self.label_126.setText(QCoreApplication.translate("submission", u"Source:", None))
        self.label_127.setText(QCoreApplication.translate("submission", u"Filter:", None))
        self.label_230.setText(QCoreApplication.translate("submission", u"Name:", None))
        self.label_231.setText(QCoreApplication.translate("submission", u"Pattern:", None))
        self.label_232.setText(QCoreApplication.translate("submission", u"Repl:", None))
        self.label_233.setText(QCoreApplication.translate("submission", u"Source:", None))
        self.label_234.setText(QCoreApplication.translate("submission", u"Filter:", None))
        self.label_128.setText(QCoreApplication.translate("submission", u"Name:", None))
        self.label_129.setText(QCoreApplication.translate("submission", u"Pattern:", None))
        self.label_130.setText(QCoreApplication.translate("submission", u"Repl:", None))
        self.label_131.setText(QCoreApplication.translate("submission", u"Source:", None))
        self.label_132.setText(QCoreApplication.translate("submission", u"Filter:", None))
        self.label_235.setText(QCoreApplication.translate("submission", u"Name:", None))
        self.label_236.setText(QCoreApplication.translate("submission", u"Pattern:", None))
        self.label_237.setText(QCoreApplication.translate("submission", u"Repl:", None))
        self.label_238.setText(QCoreApplication.translate("submission", u"Source:", None))
        self.label_239.setText(QCoreApplication.translate("submission", u"Filter:", None))
        self.label_133.setText(QCoreApplication.translate("submission", u"Name:", None))
        self.label_144.setText(QCoreApplication.translate("submission", u"Pattern:", None))
        self.label_145.setText(QCoreApplication.translate("submission", u"Repl:", None))
        self.label_146.setText(QCoreApplication.translate("submission", u"Source:", None))
        self.label_147.setText(QCoreApplication.translate("submission", u"Filter:", None))
        self.label_240.setText(QCoreApplication.translate("submission", u"Name:", None))
        self.label_241.setText(QCoreApplication.translate("submission", u"Pattern:", None))
        self.label_242.setText(QCoreApplication.translate("submission", u"Repl:", None))
        self.label_243.setText(QCoreApplication.translate("submission", u"Source:", None))
        self.label_244.setText(QCoreApplication.translate("submission", u"Filter:", None))
        self.label_148.setText(QCoreApplication.translate("submission", u"Name:", None))
        self.label_149.setText(QCoreApplication.translate("submission", u"Pattern:", None))
        self.label_150.setText(QCoreApplication.translate("submission", u"Repl:", None))
        self.label_151.setText(QCoreApplication.translate("submission", u"Source:", None))
        self.label_152.setText(QCoreApplication.translate("submission", u"Filter:", None))
        self.label_153.setText(QCoreApplication.translate("submission", u"Name:", None))
        self.label_154.setText(QCoreApplication.translate("submission", u"Pattern:", None))
        self.label_155.setText(QCoreApplication.translate("submission", u"Repl:", None))
        self.label_156.setText(QCoreApplication.translate("submission", u"Source:", None))
        self.label_157.setText(QCoreApplication.translate("submission", u"Filter:", None))
        self.label_165.setText(QCoreApplication.translate("submission", u"Name:", None))
        self.label_166.setText(QCoreApplication.translate("submission", u"Pattern:", None))
        self.label_167.setText(QCoreApplication.translate("submission", u"Repl:", None))
        self.label_168.setText(QCoreApplication.translate("submission", u"Source:", None))
        self.label_169.setText(QCoreApplication.translate("submission", u"Filter:", None))
        self.TopTab.setTabText(self.TopTab.indexOf(self.tab_10), QCoreApplication.translate("submission", u"Parsing", None))
        self.label_86.setText(QCoreApplication.translate("submission", u"Search Folder:", None))
#if QT_CONFIG(tooltip)
        self.package_explore_2.setToolTip(QCoreApplication.translate("submission", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Opens video directory with system file manager (Explorer, Finder...).</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.package_explore_2.setText("")
#if QT_CONFIG(tooltip)
        self.package_browse_2.setToolTip(QCoreApplication.translate("submission", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:11px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Browse for video file.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.package_browse_2.setText("")
        self.label_92.setText(QCoreApplication.translate("submission", u"Exclude:", None))
        self.label_93.setText(QCoreApplication.translate("submission", u"Include:", None))
        self.side_copy.setText(QCoreApplication.translate("submission", u"Copy Sidecar Files", None))
        self.side_copywithgo.setText(QCoreApplication.translate("submission", u"Copy with Go", None))
        self.side_sub_only.setText(QCoreApplication.translate("submission", u"Submission Only", None))
        self.side_log_only.setText(QCoreApplication.translate("submission", u"Log Only", None))
        self.side_all.setText(QCoreApplication.translate("submission", u"All", None))
        self.label_95.setText(QCoreApplication.translate("submission", u"Pattern:", None))
        self.side_pattern_1.setText("")
        self.label_94.setText(QCoreApplication.translate("submission", u"Repl:", None))
        self.label_96.setText(QCoreApplication.translate("submission", u"If match to:", None))
        self.side_match_1.setText("")
        self.label_97.setText(QCoreApplication.translate("submission", u"Dest:", None))
        self.label_98.setText(QCoreApplication.translate("submission", u"Filter:", None))
        self.label_99.setText(QCoreApplication.translate("submission", u"Pattern:", None))
        self.side_pattern_2.setText("")
        self.label_100.setText(QCoreApplication.translate("submission", u"Repl:", None))
        self.label_101.setText(QCoreApplication.translate("submission", u"If match to:", None))
        self.side_match_2.setText("")
        self.label_102.setText(QCoreApplication.translate("submission", u"Dest:", None))
        self.label_103.setText(QCoreApplication.translate("submission", u"Filter:", None))
        self.label_104.setText(QCoreApplication.translate("submission", u"Pattern:", None))
        self.side_pattern_3.setText("")
        self.label_105.setText(QCoreApplication.translate("submission", u"Repl:", None))
        self.label_106.setText(QCoreApplication.translate("submission", u"If match to:", None))
        self.side_match_3.setText("")
        self.label_107.setText(QCoreApplication.translate("submission", u"Dest:", None))
        self.label_108.setText(QCoreApplication.translate("submission", u"Filter:", None))
        self.label_109.setText(QCoreApplication.translate("submission", u"Pattern:", None))
        self.side_pattern_4.setText("")
        self.label_110.setText(QCoreApplication.translate("submission", u"Repl:", None))
        self.label_111.setText(QCoreApplication.translate("submission", u"If match to:", None))
        self.side_match_4.setText("")
        self.label_112.setText(QCoreApplication.translate("submission", u"Dest:", None))
        self.label_113.setText(QCoreApplication.translate("submission", u"Filter:", None))
        self.label_134.setText(QCoreApplication.translate("submission", u"Pattern:", None))
        self.side_pattern_5.setText("")
        self.label_135.setText(QCoreApplication.translate("submission", u"Repl:", None))
        self.label_136.setText(QCoreApplication.translate("submission", u"If match to:", None))
        self.side_match_5.setText("")
        self.label_137.setText(QCoreApplication.translate("submission", u"Dest:", None))
        self.label_138.setText(QCoreApplication.translate("submission", u"Filter:", None))
        self.label_139.setText(QCoreApplication.translate("submission", u"Pattern:", None))
        self.side_pattern_6.setText("")
        self.label_140.setText(QCoreApplication.translate("submission", u"Repl:", None))
        self.label_141.setText(QCoreApplication.translate("submission", u"If match to:", None))
        self.side_match_6.setText("")
        self.label_142.setText(QCoreApplication.translate("submission", u"Dest:", None))
        self.label_143.setText(QCoreApplication.translate("submission", u"Filter:", None))
        self.TopTab.setTabText(self.TopTab.indexOf(self.tab_13), QCoreApplication.translate("submission", u"Sidecar Files", None))
        self.label_246.setText(QCoreApplication.translate("submission", u"Filter:", None))
        self.rename_filter_01.setText("")
        self.label_35.setText(QCoreApplication.translate("submission", u"Source:", None))
        self.label_245.setText(QCoreApplication.translate("submission", u"Pattern:", None))
        self.rename_pattern_01.setText("")
        self.label_247.setText(QCoreApplication.translate("submission", u"Repl:", None))
        self.label_248.setText(QCoreApplication.translate("submission", u"Filter:", None))
        self.rename_filter_02.setText("")
        self.label_249.setText(QCoreApplication.translate("submission", u"Source:", None))
        self.label_250.setText(QCoreApplication.translate("submission", u"Pattern:", None))
        self.rename_pattern_02.setText("")
        self.label_251.setText(QCoreApplication.translate("submission", u"Repl:", None))
        self.label_252.setText(QCoreApplication.translate("submission", u"Filter:", None))
        self.rename_filter_03.setText("")
        self.label_253.setText(QCoreApplication.translate("submission", u"Source:", None))
        self.label_254.setText(QCoreApplication.translate("submission", u"Pattern:", None))
        self.rename_pattern_03.setText("")
        self.label_255.setText(QCoreApplication.translate("submission", u"Repl:", None))
        self.label_256.setText(QCoreApplication.translate("submission", u"Filter:", None))
        self.rename_filter_04.setText("")
        self.label_257.setText(QCoreApplication.translate("submission", u"Source:", None))
        self.label_258.setText(QCoreApplication.translate("submission", u"Pattern:", None))
        self.rename_pattern_04.setText("")
        self.label_259.setText(QCoreApplication.translate("submission", u"Repl:", None))
        self.label_260.setText(QCoreApplication.translate("submission", u"Filter:", None))
        self.rename_filter_05.setText("")
        self.label_261.setText(QCoreApplication.translate("submission", u"Source:", None))
        self.label_262.setText(QCoreApplication.translate("submission", u"Pattern:", None))
        self.rename_pattern_05.setText("")
        self.label_263.setText(QCoreApplication.translate("submission", u"Repl:", None))
        self.label_264.setText(QCoreApplication.translate("submission", u"Filter:", None))
        self.rename_filter_06.setText("")
        self.label_265.setText(QCoreApplication.translate("submission", u"Source:", None))
        self.label_266.setText(QCoreApplication.translate("submission", u"Pattern:", None))
        self.rename_pattern_06.setText("")
        self.label_267.setText(QCoreApplication.translate("submission", u"Repl:", None))
        self.label_268.setText(QCoreApplication.translate("submission", u"Filter:", None))
        self.rename_filter_07.setText("")
        self.label_269.setText(QCoreApplication.translate("submission", u"Source:", None))
        self.label_270.setText(QCoreApplication.translate("submission", u"Pattern:", None))
        self.rename_pattern_07.setText("")
        self.label_271.setText(QCoreApplication.translate("submission", u"Repl:", None))
        self.label_272.setText(QCoreApplication.translate("submission", u"Filter:", None))
        self.rename_filter_08.setText("")
        self.label_273.setText(QCoreApplication.translate("submission", u"Source:", None))
        self.label_274.setText(QCoreApplication.translate("submission", u"Pattern:", None))
        self.rename_pattern_08.setText("")
        self.label_275.setText(QCoreApplication.translate("submission", u"Repl:", None))
        self.Rename_go.setText(QCoreApplication.translate("submission", u"Rename", None))
        self.rename_reload_after.setText(QCoreApplication.translate("submission", u"Reload after Rename", None))
        self.TopTab.setTabText(self.TopTab.indexOf(self.tab_17), QCoreApplication.translate("submission", u"Rename", None))
#if QT_CONFIG(tooltip)
        self.groupBox_29.setToolTip(QCoreApplication.translate("submission", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_29.setTitle(QCoreApplication.translate("submission", u"Data", None))
        self.data_enable.setText(QCoreApplication.translate("submission", u"Enable Data", None))
        self.label_321.setText(QCoreApplication.translate("submission", u"Column Prefix:", None))
#if QT_CONFIG(tooltip)
        self.name_date_prefix.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>Renamer checks all folders one folder above the package folder<br/>and detects current date stamp in it by using Date Regex</p><p><br/>Keywords:<br/>{yy}: year<br/>{mm}: month<br/>{dd}: day</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.name_date_prefix.setText(QCoreApplication.translate("submission", u"data_", None))
#if QT_CONFIG(tooltip)
        self.groupBox_25.setToolTip(QCoreApplication.translate("submission", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_25.setTitle(QCoreApplication.translate("submission", u"Data CSV:", None))
#if QT_CONFIG(tooltip)
        self.data_csv_path.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>Expects path to folder containing media files.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.data_csv_path.setText("")
#if QT_CONFIG(tooltip)
        self.data_csv_browse.setToolTip(QCoreApplication.translate("submission", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:11px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Browse for video file.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.data_csv_browse.setText("")
        self.data_csv_latest.setText(QCoreApplication.translate("submission", u"Latest in Folder", None))
        self.groupBox_26.setTitle(QCoreApplication.translate("submission", u"Match Package Keys to Data Keys", None))
        self.data_package1_chbx.setText(QCoreApplication.translate("submission", u"Package 1", None))
#if QT_CONFIG(tooltip)
        self.data_package1.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>Renamer checks all folders one folder above the package folder<br/>and detects version in it by using Version Regex</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.data_package1.setText(QCoreApplication.translate("submission", u"{shot}", None))
        self.data_package1.setPlaceholderText(QCoreApplication.translate("submission", u"preview", None))
        self.label_309.setText(QCoreApplication.translate("submission", u"Data 1:", None))
#if QT_CONFIG(tooltip)
        self.data_data1.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>Renamer checks all folders one folder above the package folder<br/>and detects version in it by using Version Regex</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.data_data1.setText(QCoreApplication.translate("submission", u"{data_shot}", None))
        self.data_data1.setPlaceholderText(QCoreApplication.translate("submission", u"preview", None))
        self.data_package2_chbx.setText(QCoreApplication.translate("submission", u"Package 2", None))
#if QT_CONFIG(tooltip)
        self.data_package2.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>Renamer checks all folders one folder above the package folder<br/>and detects version in it by using Version Regex</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.data_package2.setText("")
        self.data_package2.setPlaceholderText(QCoreApplication.translate("submission", u"preview", None))
        self.label_310.setText(QCoreApplication.translate("submission", u"Data 2:", None))
#if QT_CONFIG(tooltip)
        self.data_data2.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>Renamer checks all folders one folder above the package folder<br/>and detects version in it by using Version Regex</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.data_data2.setText("")
        self.data_data2.setPlaceholderText(QCoreApplication.translate("submission", u"preview", None))
        self.data_package3_chbx.setText(QCoreApplication.translate("submission", u"Package 3", None))
#if QT_CONFIG(tooltip)
        self.data_package3.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>Renamer checks all folders one folder above the package folder<br/>and detects version in it by using Version Regex</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.data_package3.setText("")
        self.data_package3.setPlaceholderText(QCoreApplication.translate("submission", u"preview", None))
        self.label_311.setText(QCoreApplication.translate("submission", u"Data 3:", None))
#if QT_CONFIG(tooltip)
        self.data_data3.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>Renamer checks all folders one folder above the package folder<br/>and detects version in it by using Version Regex</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.data_data3.setText("")
        self.data_data3.setPlaceholderText(QCoreApplication.translate("submission", u"preview", None))
        self.TopTab.setTabText(self.TopTab.indexOf(self.tab_23), QCoreApplication.translate("submission", u"Data", None))
        self.groupBox_35.setTitle(QCoreApplication.translate("submission", u"Ftrack", None))
        self.ftrack_use.setText(QCoreApplication.translate("submission", u"Use Ftrack", None))
        self.label_319.setText(QCoreApplication.translate("submission", u"Project:", None))
        self.ftrack_project.setText("")
        self.groupBox_22.setTitle(QCoreApplication.translate("submission", u"Match", None))
        self.label_158.setText(QCoreApplication.translate("submission", u"Shot:", None))
        self.ftrack_shot.setText(QCoreApplication.translate("submission", u"{shot}", None))
        self.label_159.setText(QCoreApplication.translate("submission", u"Task:", None))
        self.ftrack_task.setText(QCoreApplication.translate("submission", u"{task}", None))
        self.label_318.setText(QCoreApplication.translate("submission", u"Extensions:", None))
        self.ftrack_include_2.setText("")
        self.groupBox_23.setTitle(QCoreApplication.translate("submission", u"Match Shot Attributes:", None))
        self.ftrack_do_op.setText(QCoreApplication.translate("submission", u"Query OpenPype Attributes", None))
        self.groupBox_21.setTitle(QCoreApplication.translate("submission", u"Match Notes:", None))
        self.ftrack_do_notes.setText(QCoreApplication.translate("submission", u"Query Notes", None))
        self.ftrack_label_use.setText(QCoreApplication.translate("submission", u"Note Label", None))
        self.ftrack_label.setText("")
        self.ftrack_version_use.setText(QCoreApplication.translate("submission", u"Version", None))
        self.ftrack_version.setText("")
        self.label_91.setText(QCoreApplication.translate("submission", u"Note Pattern:", None))
#if QT_CONFIG(tooltip)
        self.ftrack_note_pattern.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>Search for any note that containds word client:<br/>^(.*?client.*?)$<br/><br/>(WIP|FINAL): (.*) together with repl \\2 will match publish notes staht start with WIP or FINAL and show only second parethes, ie artist's note</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.ftrack_note_pattern.setText(QCoreApplication.translate("submission", u"4client v{version}(.*)", None))
        self.label_160.setText(QCoreApplication.translate("submission", u"Note Repl:", None))
        self.ftrack_note_repl.setText(QCoreApplication.translate("submission", u"\\2", None))
        self.groupBox_37.setTitle(QCoreApplication.translate("submission", u"Shot List", None))
        self.ftrack_export.setText(QCoreApplication.translate("submission", u"Export", None))
        self.ftrack_path.setText("")
        self.TopTab.setTabText(self.TopTab.indexOf(self.tab_11), QCoreApplication.translate("submission", u"Ftrack", None))
#if QT_CONFIG(tooltip)
        self.groupBox_11.setToolTip(QCoreApplication.translate("submission", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_11.setTitle(QCoreApplication.translate("submission", u"Vendor CSV:", None))
        self.vendor_csv_path_detect.setText(QCoreApplication.translate("submission", u"Auto Detect", None))
#if QT_CONFIG(tooltip)
        self.vendor_csv_path.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>Expects path to folder containing media files.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.vendor_csv_path.setText("")
#if QT_CONFIG(tooltip)
        self.vendor_csv_explore.setToolTip(QCoreApplication.translate("submission", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Opens video directory with system file manager (Explorer, Finder...).</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.vendor_csv_explore.setText("")
#if QT_CONFIG(tooltip)
        self.vendor_csv_browse.setToolTip(QCoreApplication.translate("submission", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:11px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Browse for video file.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.vendor_csv_browse.setText("")
        self.groupBox_12.setTitle(QCoreApplication.translate("submission", u"Match Package Key to Vendor Key", None))
        self.label_163.setText(QCoreApplication.translate("submission", u"Package:", None))
#if QT_CONFIG(tooltip)
        self.vendor_csv_package_key.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>Renamer checks all folders one folder above the package folder<br/>and detects version in it by using Version Regex</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.vendor_csv_package_key.setText(QCoreApplication.translate("submission", u"_(\\d{3})$", None))
        self.vendor_csv_package_key.setPlaceholderText(QCoreApplication.translate("submission", u"preview", None))
        self.label_164.setText(QCoreApplication.translate("submission", u"Vendor:", None))
#if QT_CONFIG(tooltip)
        self.vendor_csv_vendor_key.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>Renamer checks all folders one folder above the package folder<br/>and detects version in it by using Version Regex</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.vendor_csv_vendor_key.setText(QCoreApplication.translate("submission", u"_(\\d{3})$", None))
        self.vendor_csv_vendor_key.setPlaceholderText(QCoreApplication.translate("submission", u"preview", None))
        self.groupBox_24.setTitle(QCoreApplication.translate("submission", u"Options", None))
        self.vendor_csv_ignore.setText(QCoreApplication.translate("submission", u"Ignore Items not in CSV", None))
        self.vendor_csv_ftrack.setText(QCoreApplication.translate("submission", u"Cross Check with Ftrack", None))
        self.vendor_csv_skip.setText(QCoreApplication.translate("submission", u"Skip by:", None))
#if QT_CONFIG(tooltip)
        self.vendor_csv_skip_by.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>Renamer checks all folders one folder above the package folder<br/>and detects version in it by using Version Regex</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.vendor_csv_skip_by.setText(QCoreApplication.translate("submission", u"{shot}", None))
        self.vendor_csv_skip_by.setPlaceholderText(QCoreApplication.translate("submission", u"preview", None))
        self.label_308.setText(QCoreApplication.translate("submission", u"To Skip:", None))
#if QT_CONFIG(tooltip)
        self.vendor_csv_skip_what.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>Expects path to folder containing media files.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.vendor_csv_skip_what.setText("")
        self.label_30.setText(QCoreApplication.translate("submission", u"Spreadsheet Preferences:", None))
#if QT_CONFIG(tooltip)
        self.vendor_csv_prefs_spreadsheet.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>The columns are defines as <br/>column name = value,</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.vendor_csv_prefs_spreadsheet.setPlainText("")
        self.label_31.setText(QCoreApplication.translate("submission", u"Representation Preferences:", None))
#if QT_CONFIG(tooltip)
        self.vendor_csv_prefs_repres.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>The columns are defines as <br/>column name = value,</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.vendor_csv_prefs_repres.setPlainText("")
        self.TopTab.setTabText(self.TopTab.indexOf(self.tab_16), QCoreApplication.translate("submission", u"Vendor", None))
#if QT_CONFIG(tooltip)
        self.groupBox_36.setToolTip(QCoreApplication.translate("submission", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_36.setTitle(QCoreApplication.translate("submission", u"Search and Replace CSV", None))
        self.replace_enable.setText(QCoreApplication.translate("submission", u"Enable", None))
#if QT_CONFIG(tooltip)
        self.replace_csv_path.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>Path to CSV file.</p><p>Parent Directory of the file will be used to search for all valid csv files. From list of sorted valid csv files the latest will be picked, regardless of the file name here.</p><p><br/>Required CSV Colums: <span style=\" font-family:'JetBrains Mono','monospace'; font-size:9.8pt; color:#6aab73;\">'Extension'</span><span style=\" font-family:'JetBrains Mono','monospace'; font-size:9.8pt; color:#bcbec4;\">, </span><span style=\" font-family:'JetBrains Mono','monospace'; font-size:9.8pt; color:#6aab73;\">'Pattern'</span><span style=\" font-family:'JetBrains Mono','monospace'; font-size:9.8pt; color:#bcbec4;\">, </span><span style=\" font-family:'JetBrains Mono','monospace'; font-size:9.8pt; color:#6aab73;\">'Search'</span><span style=\" font-family:'JetBrains Mono','monospace'; font-size:9.8pt; color:#bcbec4;\">, </span><span style=\" font-family:'JetBrains Mono','monospace'; font-size:9.8pt; color:#6aab73;\">'Replace'<br/></span>Extension: Which files to process.<br/>"
                        "Pattern: Regex pattern to match the file name</p><p>Search: search for string</p><p>Replace: replace with string.</p><p>Multiple Search and replace string for one file need to be on separfate lines.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.replace_csv_path.setText("")
#if QT_CONFIG(tooltip)
        self.data_csv_browse_2.setToolTip(QCoreApplication.translate("submission", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:11px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Browse for video file.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.data_csv_browse_2.setText("")
        self.replace_withgo.setText(QCoreApplication.translate("submission", u"Replace with Go", None))
        self.replace_button.setText(QCoreApplication.translate("submission", u"Replace", None))
        self.TopTab.setTabText(self.TopTab.indexOf(self.tab_26), QCoreApplication.translate("submission", u"Replace", None))
        self.thumbs_make_on_go.setText(QCoreApplication.translate("submission", u"Convert on Go", None))
        self.thumbs_convert_now.setText(QCoreApplication.translate("submission", u"Convert Now", None))
        self.thumbs_skip_existing.setText(QCoreApplication.translate("submission", u"Skip Existing", None))
        self.label_34.setText(QCoreApplication.translate("submission", u"If:", None))
        self.thumbs_if_01.setText(QCoreApplication.translate("submission", u"'{extension}' == 'mov'", None))
        self.label_276.setText(QCoreApplication.translate("submission", u"Executable:", None))
        self.thumbs_exe_01.setText(QCoreApplication.translate("submission", u"ffmpeg", None))
        self.label_277.setText(QCoreApplication.translate("submission", u"Arguments:", None))
        self.thumbs_args_01.setText(QCoreApplication.translate("submission", u"-i {path} -ss {meta_thumbnail_time} -vframes 1 {package_name_root}/{package_name}/_thumbs/{vendor_Merge_by}.png", None))
        self.label_278.setText(QCoreApplication.translate("submission", u"File Name:", None))
        self.thumbs_name_01.setText("")
        self.label_280.setText(QCoreApplication.translate("submission", u"If:", None))
        self.thumbs_if_02.setText("")
        self.label_281.setText(QCoreApplication.translate("submission", u"Executable:", None))
        self.thumbs_exe_02.setText(QCoreApplication.translate("submission", u"ffmpeg", None))
        self.label_282.setText(QCoreApplication.translate("submission", u"Arguments:", None))
        self.label_283.setText(QCoreApplication.translate("submission", u"File Name:", None))
        self.thumbs_name_02.setText("")
        self.label_284.setText(QCoreApplication.translate("submission", u"If:", None))
        self.thumbs_if_03.setText("")
        self.label_285.setText(QCoreApplication.translate("submission", u"Executable:", None))
        self.thumbs_exe_03.setText(QCoreApplication.translate("submission", u"ffmpeg", None))
        self.label_286.setText(QCoreApplication.translate("submission", u"Arguments:", None))
        self.label_287.setText(QCoreApplication.translate("submission", u"File Name:", None))
        self.thumbs_name_03.setText("")
        self.label_288.setText(QCoreApplication.translate("submission", u"If:", None))
        self.thumbs_if_04.setText("")
        self.label_289.setText(QCoreApplication.translate("submission", u"Executable:", None))
        self.thumbs_exe_04.setText(QCoreApplication.translate("submission", u"ffmpeg", None))
        self.label_290.setText(QCoreApplication.translate("submission", u"Arguments:", None))
        self.label_291.setText(QCoreApplication.translate("submission", u"File Name:", None))
        self.thumbs_name_04.setText("")
        self.label_292.setText(QCoreApplication.translate("submission", u"If:", None))
        self.thumbs_if_05.setText("")
        self.label_293.setText(QCoreApplication.translate("submission", u"Executable:", None))
        self.thumbs_exe_05.setText(QCoreApplication.translate("submission", u"ffmpeg", None))
        self.label_294.setText(QCoreApplication.translate("submission", u"Arguments:", None))
        self.label_295.setText(QCoreApplication.translate("submission", u"File Name:", None))
        self.thumbs_name_05.setText("")
        self.label_296.setText(QCoreApplication.translate("submission", u"If:", None))
        self.thumbs_if_06.setText("")
        self.label_297.setText(QCoreApplication.translate("submission", u"Executable:", None))
        self.thumbs_exe_06.setText(QCoreApplication.translate("submission", u"ffmpeg", None))
        self.label_298.setText(QCoreApplication.translate("submission", u"Arguments:", None))
        self.label_299.setText(QCoreApplication.translate("submission", u"File Name:", None))
        self.thumbs_name_06.setText("")
        self.label_300.setText(QCoreApplication.translate("submission", u"If:", None))
        self.thumbs_if_07.setText("")
        self.label_301.setText(QCoreApplication.translate("submission", u"Executable:", None))
        self.thumbs_exe_07.setText(QCoreApplication.translate("submission", u"ffmpeg", None))
        self.label_302.setText(QCoreApplication.translate("submission", u"Arguments:", None))
        self.label_303.setText(QCoreApplication.translate("submission", u"File Name:", None))
        self.thumbs_name_07.setText("")
        self.label_304.setText(QCoreApplication.translate("submission", u"If:", None))
        self.thumbs_if_08.setText("")
        self.label_305.setText(QCoreApplication.translate("submission", u"Executable:", None))
        self.thumbs_exe_08.setText(QCoreApplication.translate("submission", u"ffmpeg", None))
        self.label_306.setText(QCoreApplication.translate("submission", u"Arguments:", None))
        self.label_307.setText(QCoreApplication.translate("submission", u"File Name:", None))
        self.thumbs_name_08.setText("")
        self.TopTab.setTabText(self.TopTab.indexOf(self.tab_18), QCoreApplication.translate("submission", u"Convert", None))
#if QT_CONFIG(tooltip)
        self.scrollArea_2.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>Defines output columns for submission, drive log and text outputs.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("submission", u"Submission:", None))
#if QT_CONFIG(tooltip)
        self.sub_columns.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>The columns are defines as <br/>column name = value,</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.sub_columns.setPlainText(QCoreApplication.translate("submission", u"Shot = {printf_pattern},\n"
"Vendor = AmazingVFX", None))
        self.label_7.setText(QCoreApplication.translate("submission", u"Exclude:", None))
#if QT_CONFIG(tooltip)
        self.sub_exclude.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>Do not use files that contain this string in path or name.<br/>Can use more than one string, separated by space.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("submission", u"Include:", None))
#if QT_CONFIG(tooltip)
        self.sub_include.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>Only use files that contain this string in path or name.<br/>Can use more than one string, separated by space</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("submission", u"Drive Log", None))
#if QT_CONFIG(tooltip)
        self.log_columns.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>The columns are defines as <br/>column name = value,</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.log_columns.setPlainText(QCoreApplication.translate("submission", u"Shot = {printf_pattern},\n"
"Vendor = AmazingVFX", None))
        self.label_9.setText(QCoreApplication.translate("submission", u"Exclude:", None))
#if QT_CONFIG(tooltip)
        self.log_exclude.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>Do not use files that contain this string in path or name.<br/>Can use more than one string, separated by space.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_11.setText(QCoreApplication.translate("submission", u"Include:", None))
#if QT_CONFIG(tooltip)
        self.log_include.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>Only use files that contain this string in path or name.<br/>Can use more than one string, separated by space</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("submission", u"Text", None))
#if QT_CONFIG(tooltip)
        self.txt_columns.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>The columns are defines as <br/>column name = value,</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.txt_columns.setPlainText(QCoreApplication.translate("submission", u"File = {Shot = {printf_pattern}", None))
        self.label_12.setText(QCoreApplication.translate("submission", u"Exclude:", None))
#if QT_CONFIG(tooltip)
        self.txt_exclude.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>Do not use files that contain this string in path or name.<br/>Can use more than one string, separated by space.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_13.setText(QCoreApplication.translate("submission", u"Include:", None))
#if QT_CONFIG(tooltip)
        self.txt_include.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>Only use files that contain this string in path or name.<br/>Can use more than one string, separated by space</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.TopTab.setTabText(self.TopTab.indexOf(self.tab_2), QCoreApplication.translate("submission", u"Spreadsheet", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("submission", u"Export Submission:", None))
        self.text_txt.setText(QCoreApplication.translate("submission", u"TXT", None))
        self.text_root.setText(QCoreApplication.translate("submission", u"Root", None))
        self.text_above.setText(QCoreApplication.translate("submission", u"One folder above Root", None))
        self.text_custom.setText(QCoreApplication.translate("submission", u"Custom Location", None))
        self.label_17.setText(QCoreApplication.translate("submission", u"Custom Location", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("submission", u"Body:", None))
        self.text_add_titles.setText(QCoreApplication.translate("submission", u"Add Column Titles", None))
        self.text_sep_tab.setText(QCoreApplication.translate("submission", u"Tab Separator", None))
        self.text_sep_fixed.setText(QCoreApplication.translate("submission", u"Space Separator", None))
        self.label_52.setText(QCoreApplication.translate("submission", u"Header:", None))
        self.text_header.setPlainText(QCoreApplication.translate("submission", u"My Header", None))
        self.label_75.setText(QCoreApplication.translate("submission", u"Footer", None))
        self.text_footer.setPlainText(QCoreApplication.translate("submission", u"My Footer", None))
        self.TopTab.setTabText(self.TopTab.indexOf(self.tab_5), QCoreApplication.translate("submission", u"Text", None))
        self.check_sequence_size_consistency.setText(QCoreApplication.translate("submission", u"File Sequence Size consistency", None))
        self.check_sequence_holes.setText(QCoreApplication.translate("submission", u"Check for File Sequence Holes", None))
        self.groupBox_ch01.setTitle("")
        self.label_357.setText(QCoreApplication.translate("submission", u"If", None))
        self.label_358.setText(QCoreApplication.translate("submission", u"Check:", None))
        self.label_359.setText(QCoreApplication.translate("submission", u"#01", None))
        self.check_warning_01.setText(QCoreApplication.translate("submission", u"Warning", None))
        self.check_error_01.setText(QCoreApplication.translate("submission", u"Error", None))
        self.groupBox_ch02.setTitle("")
        self.label_360.setText(QCoreApplication.translate("submission", u"If", None))
        self.label_361.setText(QCoreApplication.translate("submission", u"Check:", None))
        self.label_362.setText(QCoreApplication.translate("submission", u"#02", None))
        self.check_warning_02.setText(QCoreApplication.translate("submission", u"Warning", None))
        self.check_error_02.setText(QCoreApplication.translate("submission", u"Error", None))
        self.groupBox_ch03.setTitle("")
        self.label_363.setText(QCoreApplication.translate("submission", u"If", None))
        self.label_364.setText(QCoreApplication.translate("submission", u"Check:", None))
        self.label_365.setText(QCoreApplication.translate("submission", u"#03", None))
        self.check_warning_03.setText(QCoreApplication.translate("submission", u"Warning", None))
        self.check_error_03.setText(QCoreApplication.translate("submission", u"Error", None))
        self.groupBox_ch04.setTitle("")
        self.label_366.setText(QCoreApplication.translate("submission", u"If", None))
        self.label_367.setText(QCoreApplication.translate("submission", u"Check:", None))
        self.label_368.setText(QCoreApplication.translate("submission", u"#04", None))
        self.check_warning_04.setText(QCoreApplication.translate("submission", u"Warning", None))
        self.check_error_04.setText(QCoreApplication.translate("submission", u"Error", None))
        self.groupBox_ch05.setTitle("")
        self.label_369.setText(QCoreApplication.translate("submission", u"If", None))
        self.label_370.setText(QCoreApplication.translate("submission", u"Check:", None))
        self.label_371.setText(QCoreApplication.translate("submission", u"#05", None))
        self.check_warning_05.setText(QCoreApplication.translate("submission", u"Warning", None))
        self.check_error_05.setText(QCoreApplication.translate("submission", u"Error", None))
        self.groupBox_ch06.setTitle("")
        self.label_372.setText(QCoreApplication.translate("submission", u"If", None))
        self.label_373.setText(QCoreApplication.translate("submission", u"Check:", None))
        self.label_374.setText(QCoreApplication.translate("submission", u"#06", None))
        self.check_warning_06.setText(QCoreApplication.translate("submission", u"Warning", None))
        self.check_error_06.setText(QCoreApplication.translate("submission", u"Error", None))
        self.groupBox_ch07.setTitle("")
        self.label_375.setText(QCoreApplication.translate("submission", u"If", None))
        self.label_376.setText(QCoreApplication.translate("submission", u"Check:", None))
        self.label_377.setText(QCoreApplication.translate("submission", u"#07", None))
        self.check_warning_07.setText(QCoreApplication.translate("submission", u"Warning", None))
        self.check_error_07.setText(QCoreApplication.translate("submission", u"Error", None))
        self.groupBox_ch08.setTitle("")
        self.label_378.setText(QCoreApplication.translate("submission", u"If", None))
        self.label_379.setText(QCoreApplication.translate("submission", u"Check:", None))
        self.label_380.setText(QCoreApplication.translate("submission", u"#08", None))
        self.check_warning_08.setText(QCoreApplication.translate("submission", u"Warning", None))
        self.check_error_08.setText(QCoreApplication.translate("submission", u"Error", None))
        self.groupBox_ch09.setTitle("")
        self.label_381.setText(QCoreApplication.translate("submission", u"If", None))
        self.label_382.setText(QCoreApplication.translate("submission", u"Check:", None))
        self.label_383.setText(QCoreApplication.translate("submission", u"#09", None))
        self.check_warning_09.setText(QCoreApplication.translate("submission", u"Warning", None))
        self.check_error_09.setText(QCoreApplication.translate("submission", u"Error", None))
        self.groupBox_ch10.setTitle("")
        self.label_411.setText(QCoreApplication.translate("submission", u"If", None))
        self.label_412.setText(QCoreApplication.translate("submission", u"Check:", None))
        self.label_413.setText(QCoreApplication.translate("submission", u"#10", None))
        self.check_warning_10.setText(QCoreApplication.translate("submission", u"Warning", None))
        self.check_error_10.setText(QCoreApplication.translate("submission", u"Error", None))
        self.groupBox_ch14.setTitle("")
        self.label_414.setText(QCoreApplication.translate("submission", u"If", None))
        self.label_415.setText(QCoreApplication.translate("submission", u"Check:", None))
        self.label_416.setText(QCoreApplication.translate("submission", u"#11", None))
        self.check_warning_11.setText(QCoreApplication.translate("submission", u"Warning", None))
        self.check_error_11.setText(QCoreApplication.translate("submission", u"Error", None))
        self.groupBox_ch15.setTitle("")
        self.label_417.setText(QCoreApplication.translate("submission", u"If", None))
        self.label_418.setText(QCoreApplication.translate("submission", u"Check:", None))
        self.label_419.setText(QCoreApplication.translate("submission", u"#12", None))
        self.check_warning_12.setText(QCoreApplication.translate("submission", u"Warning", None))
        self.check_error_12.setText(QCoreApplication.translate("submission", u"Error", None))
        self.groupBox_ch16.setTitle("")
        self.label_420.setText(QCoreApplication.translate("submission", u"If", None))
        self.label_421.setText(QCoreApplication.translate("submission", u"Check:", None))
        self.label_422.setText(QCoreApplication.translate("submission", u"#13", None))
        self.check_warning_13.setText(QCoreApplication.translate("submission", u"Warning", None))
        self.check_error_13.setText(QCoreApplication.translate("submission", u"Error", None))
        self.groupBox_ch17.setTitle("")
        self.label_423.setText(QCoreApplication.translate("submission", u"If", None))
        self.label_424.setText(QCoreApplication.translate("submission", u"Check:", None))
        self.label_425.setText(QCoreApplication.translate("submission", u"#14", None))
        self.check_warning_14.setText(QCoreApplication.translate("submission", u"Warning", None))
        self.check_error_14.setText(QCoreApplication.translate("submission", u"Error", None))
        self.groupBox_ch18.setTitle("")
        self.label_426.setText(QCoreApplication.translate("submission", u"If", None))
        self.label_427.setText(QCoreApplication.translate("submission", u"Check:", None))
        self.label_428.setText(QCoreApplication.translate("submission", u"#15", None))
        self.check_warning_15.setText(QCoreApplication.translate("submission", u"Warning", None))
        self.check_error_15.setText(QCoreApplication.translate("submission", u"Error", None))
        self.groupBox_ch19.setTitle("")
        self.label_429.setText(QCoreApplication.translate("submission", u"If", None))
        self.label_430.setText(QCoreApplication.translate("submission", u"Check:", None))
        self.label_431.setText(QCoreApplication.translate("submission", u"#16", None))
        self.check_warning_16.setText(QCoreApplication.translate("submission", u"Warning", None))
        self.check_error_16.setText(QCoreApplication.translate("submission", u"Error", None))
        self.groupBox_ch20.setTitle("")
        self.label_432.setText(QCoreApplication.translate("submission", u"If", None))
        self.label_433.setText(QCoreApplication.translate("submission", u"Check:", None))
        self.label_434.setText(QCoreApplication.translate("submission", u"#17", None))
        self.check_warning_17.setText(QCoreApplication.translate("submission", u"Warning", None))
        self.check_error_17.setText(QCoreApplication.translate("submission", u"Error", None))
        self.groupBox_ch21.setTitle("")
        self.label_435.setText(QCoreApplication.translate("submission", u"If", None))
        self.label_436.setText(QCoreApplication.translate("submission", u"Check:", None))
        self.label_437.setText(QCoreApplication.translate("submission", u"#18", None))
        self.check_warning_18.setText(QCoreApplication.translate("submission", u"Warning", None))
        self.check_error_18.setText(QCoreApplication.translate("submission", u"Error", None))
        self.groupBox_ch11.setTitle("")
        self.label_438.setText(QCoreApplication.translate("submission", u"If", None))
        self.label_439.setText(QCoreApplication.translate("submission", u"Check:", None))
        self.label_440.setText(QCoreApplication.translate("submission", u"#19", None))
        self.check_warning_19.setText(QCoreApplication.translate("submission", u"Warning", None))
        self.check_error_19.setText(QCoreApplication.translate("submission", u"Error", None))
        self.groupBox_ch12.setTitle("")
        self.label_441.setText(QCoreApplication.translate("submission", u"If", None))
        self.label_442.setText(QCoreApplication.translate("submission", u"Check:", None))
        self.label_443.setText(QCoreApplication.translate("submission", u"#20", None))
        self.check_warning_20.setText(QCoreApplication.translate("submission", u"Warning", None))
        self.check_error_20.setText(QCoreApplication.translate("submission", u"Error", None))
        self.groupBox_ch13.setTitle("")
        self.label_444.setText(QCoreApplication.translate("submission", u"If", None))
        self.label_445.setText(QCoreApplication.translate("submission", u"Check:", None))
        self.label_446.setText(QCoreApplication.translate("submission", u"#21", None))
        self.check_warning_21.setText(QCoreApplication.translate("submission", u"Warning", None))
        self.check_error_21.setText(QCoreApplication.translate("submission", u"Error", None))
        self.TopTab.setTabText(self.TopTab.indexOf(self.tab_12), QCoreApplication.translate("submission", u"Checks", None))
        self.groupBox_27.setTitle(QCoreApplication.translate("submission", u"Deadline Submission", None))
        self.label_279.setText(QCoreApplication.translate("submission", u"Primary Pool:", None))
#if QT_CONFIG(tooltip)
        self.dead_primpool.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>Renamer checks all folders one folder above the package folder<br/>and detects version in it by using Version Regex</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.dead_primpool.setText("")
        self.dead_primpool.setPlaceholderText(QCoreApplication.translate("submission", u"preview", None))
        self.label_312.setText(QCoreApplication.translate("submission", u"Secondary Pool:", None))
#if QT_CONFIG(tooltip)
        self.dead_secpool.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>Renamer checks all folders one folder above the package folder<br/>and detects version in it by using Version Regex</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.dead_secpool.setText("")
        self.dead_secpool.setPlaceholderText(QCoreApplication.translate("submission", u"preview", None))
        self.label_313.setText(QCoreApplication.translate("submission", u"Group:", None))
#if QT_CONFIG(tooltip)
        self.dead_group.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>Renamer checks all folders one folder above the package folder<br/>and detects version in it by using Version Regex</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.dead_group.setText("")
        self.dead_group.setPlaceholderText(QCoreApplication.translate("submission", u"preview", None))
        self.label_314.setText(QCoreApplication.translate("submission", u"Priority:", None))
#if QT_CONFIG(tooltip)
        self.dead_priority.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>Renamer checks all folders one folder above the package folder<br/>and detects version in it by using Version Regex</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.dead_priority.setText("")
        self.dead_priority.setPlaceholderText(QCoreApplication.translate("submission", u"preview", None))
        self.label_315.setText(QCoreApplication.translate("submission", u"Limits:", None))
#if QT_CONFIG(tooltip)
        self.dead_limits.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>Renamer checks all folders one folder above the package folder<br/>and detects version in it by using Version Regex</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.dead_limits.setText("")
        self.dead_limits.setPlaceholderText(QCoreApplication.translate("submission", u"preview", None))
        self.label_316.setText(QCoreApplication.translate("submission", u"Comment:", None))
#if QT_CONFIG(tooltip)
        self.dead_limits_2.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>Renamer checks all folders one folder above the package folder<br/>and detects version in it by using Version Regex</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.dead_limits_2.setText("")
        self.dead_limits_2.setPlaceholderText(QCoreApplication.translate("submission", u"preview", None))
        self.label_317.setText(QCoreApplication.translate("submission", u"Department:", None))
#if QT_CONFIG(tooltip)
        self.dead_department.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>Renamer checks all folders one folder above the package folder<br/>and detects version in it by using Version Regex</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.dead_department.setText("")
        self.dead_department.setPlaceholderText(QCoreApplication.translate("submission", u"preview", None))
        self.groupBox_28.setTitle(QCoreApplication.translate("submission", u"Ayon Publish", None))
        self.dead_go_ayon.setText(QCoreApplication.translate("submission", u"Send Submission CSV to Ayon on Go", None))
        self.label_328.setText(QCoreApplication.translate("submission", u"Folder:", None))
#if QT_CONFIG(tooltip)
        self.dead_ayon_folder.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>Expects path to folder containing media files.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.dead_ayon_folder.setText("")
        self.label_329.setText(QCoreApplication.translate("submission", u"Task:", None))
#if QT_CONFIG(tooltip)
        self.dead_ayon_task.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>Expects path to folder containing media files.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.dead_ayon_task.setText("")
        self.TopTab.setTabText(self.TopTab.indexOf(self.tab_24), QCoreApplication.translate("submission", u"Deadline", None))
        self.groupBox_30.setTitle(QCoreApplication.translate("submission", u"Ayon", None))
        self.ayon_do_shotlist.setText(QCoreApplication.translate("submission", u"Enable", None))
        self.label_322.setText(QCoreApplication.translate("submission", u"Project :", None))
#if QT_CONFIG(tooltip)
        self.ayon_project.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>Expects path to folder containing media files.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.ayon_project.setText("")
        self.groupBox_32.setTitle(QCoreApplication.translate("submission", u"List", None))
        self.ayon_export_csv.setText(QCoreApplication.translate("submission", u"Export CSV", None))
        self.ayon_export_excel.setText(QCoreApplication.translate("submission", u"Export Excel", None))
        self.ayon_thumbnails.setText(QCoreApplication.translate("submission", u"Thumbnails", None))
        self.label_323.setText(QCoreApplication.translate("submission", u"Column Prefix:", None))
#if QT_CONFIG(tooltip)
        self.ayon_prefix.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>Renamer checks all folders one folder above the package folder<br/>and detects current date stamp in it by using Date Regex</p><p><br/>Keywords:<br/>{yy}: year<br/>{mm}: month<br/>{dd}: day</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.ayon_prefix.setText(QCoreApplication.translate("submission", u"list_", None))
        self.label_28.setText(QCoreApplication.translate("submission", u"Output:", None))
#if QT_CONFIG(tooltip)
        self.ayon_output_folder.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>Expects path to folder containing media files.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.ayon_output_folder.setText("")
#if QT_CONFIG(tooltip)
        self.ayon_path_browse_2.setToolTip(QCoreApplication.translate("submission", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:11px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Browse for video file.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.ayon_path_browse_2.setText("")
        self.groupBox_33.setTitle(QCoreApplication.translate("submission", u"Match Package Keys to Shot List Keys", None))
        self.ayon_package1_chbx.setText(QCoreApplication.translate("submission", u"Package 1", None))
#if QT_CONFIG(tooltip)
        self.ayon_package1.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>Renamer checks all folders one folder above the package folder<br/>and detects version in it by using Version Regex</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.ayon_package1.setText(QCoreApplication.translate("submission", u"{shot}", None))
        self.ayon_package1.setPlaceholderText(QCoreApplication.translate("submission", u"preview", None))
        self.label_324.setText(QCoreApplication.translate("submission", u"Data 1:", None))
#if QT_CONFIG(tooltip)
        self.ayon_list1.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>Renamer checks all folders one folder above the package folder<br/>and detects version in it by using Version Regex</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.ayon_list1.setText(QCoreApplication.translate("submission", u"{Folder Name}", None))
        self.ayon_list1.setPlaceholderText(QCoreApplication.translate("submission", u"preview", None))
        self.ayon_package2_chbx.setText(QCoreApplication.translate("submission", u"Package 2", None))
#if QT_CONFIG(tooltip)
        self.ayon_package2.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>Renamer checks all folders one folder above the package folder<br/>and detects version in it by using Version Regex</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.ayon_package2.setText("")
        self.ayon_package2.setPlaceholderText(QCoreApplication.translate("submission", u"preview", None))
        self.label_325.setText(QCoreApplication.translate("submission", u"Data 2:", None))
#if QT_CONFIG(tooltip)
        self.ayon_list2.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>Renamer checks all folders one folder above the package folder<br/>and detects version in it by using Version Regex</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.ayon_list2.setText("")
        self.ayon_list2.setPlaceholderText(QCoreApplication.translate("submission", u"preview", None))
        self.ayon_package3_chbx.setText(QCoreApplication.translate("submission", u"Package 3", None))
#if QT_CONFIG(tooltip)
        self.ayon_package3.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>Renamer checks all folders one folder above the package folder<br/>and detects version in it by using Version Regex</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.ayon_package3.setText("")
        self.ayon_package3.setPlaceholderText(QCoreApplication.translate("submission", u"preview", None))
        self.label_326.setText(QCoreApplication.translate("submission", u"Data 3:", None))
#if QT_CONFIG(tooltip)
        self.ayon_list3.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>Renamer checks all folders one folder above the package folder<br/>and detects version in it by using Version Regex</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.ayon_list3.setText("")
        self.ayon_list3.setPlaceholderText(QCoreApplication.translate("submission", u"preview", None))
        self.groupBox_34.setTitle(QCoreApplication.translate("submission", u"List Filters:", None))
        self.ayon_filter_assets.setText(QCoreApplication.translate("submission", u"Assets", None))
        self.ayon_filter_shots.setText(QCoreApplication.translate("submission", u"Shots", None))
        self.ayon_filter_tasks.setText(QCoreApplication.translate("submission", u"Tasks", None))
        self.ayon_filter_other.setText(QCoreApplication.translate("submission", u"Other", None))
        self.ayon_filter_tasktype_chbx.setText(QCoreApplication.translate("submission", u"Task Types:", None))
#if QT_CONFIG(tooltip)
        self.ayon_filter_tasktypes.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>Renamer checks all folders one folder above the package folder<br/>and detects version in it by using Version Regex</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.ayon_filter_tasktypes.setText("")
        self.ayon_filter_tasktypes.setPlaceholderText(QCoreApplication.translate("submission", u"preview", None))
        self.ayon_filter_assignee_chbx.setText(QCoreApplication.translate("submission", u"Assignees:", None))
#if QT_CONFIG(tooltip)
        self.ayon_filter_assignees.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>Renamer checks all folders one folder above the package folder<br/>and detects version in it by using Version Regex</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.ayon_filter_assignees.setText("")
        self.ayon_filter_assignees.setPlaceholderText(QCoreApplication.translate("submission", u"preview", None))
        self.ayon_export_butt.setText(QCoreApplication.translate("submission", u"Export Shot List", None))
        self.ayon_export_go.setText(QCoreApplication.translate("submission", u"Export with Go", None))
        self.TopTab.setTabText(self.TopTab.indexOf(self.tab_25), QCoreApplication.translate("submission", u"Ayon", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("submission", u"Frame Rate:", None))
        self.label_45.setText(QCoreApplication.translate("submission", u"Frame Rate:", None))
        self.prefs_frame_rate_txt.setText(QCoreApplication.translate("submission", u"24", None))
        self.prefs_frame_rate_use_meta.setText(QCoreApplication.translate("submission", u"Use Metadata FPS if Available", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("submission", u"TimeCode:", None))
        self.prefs_tc_from_meta.setText(QCoreApplication.translate("submission", u"From Metadata", None))
        self.prefs_tc_from_counter.setText(QCoreApplication.translate("submission", u"From Frame Counter", None))
        self.label_46.setText(QCoreApplication.translate("submission", u"Default TC:", None))
        self.prefs_tc_default.setText(QCoreApplication.translate("submission", u"01:00:00:00", None))
        self.groupBox_17.setTitle(QCoreApplication.translate("submission", u"File Sequence File Size Check:", None))
        self.prefs_size_scan.setText(QCoreApplication.translate("submission", u"Scan Sizes", None))
        self.label_51.setText(QCoreApplication.translate("submission", u"Ignore first frames:", None))
        self.label_53.setText(QCoreApplication.translate("submission", u"Neighborhood frames:", None))
        self.label_54.setText(QCoreApplication.translate("submission", u"Warning %", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("submission", u"OIIO Tool", None))
        self.prefs_oiio_custom_ocio.setText(QCoreApplication.translate("submission", u"Custom OCIO:", None))
        self.prefs_oiio_custom_ocio_path.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("submission", u"Counter:", None))
        self.label.setText(QCoreApplication.translate("submission", u"From:", None))
        self.label_2.setText(QCoreApplication.translate("submission", u"Step:", None))
        self.label_14.setText(QCoreApplication.translate("submission", u"Leading Zeroes:", None))
        self.groupBox_19.setTitle(QCoreApplication.translate("submission", u"Merge Lines", None))
        self.prefs_merge_chbx.setText(QCoreApplication.translate("submission", u"Merge by:", None))
        self.prefs_merge_by.setText(QCoreApplication.translate("submission", u"{shot}", None))
        self.prefs_merge_collapse.setText(QCoreApplication.translate("submission", u"Collapse Values", None))
        self.label_88.setText(QCoreApplication.translate("submission", u"Separator:", None))
        self.prefs_merge_sep.setText(QCoreApplication.translate("submission", u"/", None))
        self.label_89.setText(QCoreApplication.translate("submission", u"Soft By:", None))
        self.prefs_merge_sort.setText(QCoreApplication.translate("submission", u"{extension}", None))
        self.label_162.setText(QCoreApplication.translate("submission", u"Order:", None))
        self.prefs_merge_order.setText(QCoreApplication.translate("submission", u"exr,mov,mp4,cube", None))
        self.prefs_merge_hide.setText(QCoreApplication.translate("submission", u"Hide Merged", None))
        self.TopTab.setTabText(self.TopTab.indexOf(self.tab_4), QCoreApplication.translate("submission", u"Preferences", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("submission", u"Export Submission:", None))
        self.export_sub_excel.setText(QCoreApplication.translate("submission", u"Excel", None))
        self.export_sub_csv.setText(QCoreApplication.translate("submission", u"CSV", None))
        self.export_sub_root.setText(QCoreApplication.translate("submission", u"Root", None))
        self.export_sub_above.setText(QCoreApplication.translate("submission", u"One folder above Root", None))
        self.export_sub_custom.setText(QCoreApplication.translate("submission", u"Custom Location", None))
        self.label_15.setText(QCoreApplication.translate("submission", u"Custom Location", None))
#if QT_CONFIG(tooltip)
        self.export_sub_custom_path.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>Expects path to folder</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_32.setText(QCoreApplication.translate("submission", u"Suffix: ", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("submission", u"Export Drive Log:", None))
        self.export_log_excel.setText(QCoreApplication.translate("submission", u"Excel", None))
        self.export_log_csv.setText(QCoreApplication.translate("submission", u"CSV", None))
        self.export_log_root.setText(QCoreApplication.translate("submission", u"Root", None))
        self.export_log_above.setText(QCoreApplication.translate("submission", u"One folder above Root", None))
        self.export_log_custom.setText(QCoreApplication.translate("submission", u"Custom Location", None))
        self.label_16.setText(QCoreApplication.translate("submission", u"Custom Location", None))
#if QT_CONFIG(tooltip)
        self.export_log_custom_path.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>Expects path to folder</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_33.setText(QCoreApplication.translate("submission", u"Suffix: ", None))
        self.TopTab.setTabText(self.TopTab.indexOf(self.tab_9), QCoreApplication.translate("submission", u"Exports", None))
        self.groupBox_31.setTitle(QCoreApplication.translate("submission", u"Presets", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("submission", u"Load:", None))
        self.label_5.setText(QCoreApplication.translate("submission", u"Preset:", None))
        self.load_preset_button.setText(QCoreApplication.translate("submission", u"Load Preset", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("submission", u"Save:", None))
        self.label_29.setText(QCoreApplication.translate("submission", u"Preset Name:", None))
        self.save_preset_button.setText(QCoreApplication.translate("submission", u"Save Preset", None))
        self.preset_explore.setText(QCoreApplication.translate("submission", u"Open Preset Folder", None))
        self.groupBox_18.setTitle(QCoreApplication.translate("submission", u"Modules", None))
        self.preset_mod_package.setText(QCoreApplication.translate("submission", u"Package", None))
        self.preset_mod_parsing.setText(QCoreApplication.translate("submission", u"Parsing", None))
        self.preset_mod_sidecar.setText(QCoreApplication.translate("submission", u"Sidecar Files", None))
        self.preset_mod_rename.setText(QCoreApplication.translate("submission", u"Rename", None))
        self.preset_mod_data.setText(QCoreApplication.translate("submission", u"Data", None))
        self.preset_mod_ftrack.setText(QCoreApplication.translate("submission", u"Ftrack", None))
        self.preset_mod_vendor.setText(QCoreApplication.translate("submission", u"Vendor", None))
        self.preset_mod_replace.setText(QCoreApplication.translate("submission", u"Replace", None))
        self.preset_mod_convert.setText(QCoreApplication.translate("submission", u"Convert", None))
        self.preset_mod_spreadsheet.setText(QCoreApplication.translate("submission", u"Spreadsheet", None))
        self.preset_mod_text.setText(QCoreApplication.translate("submission", u"Text", None))
        self.preset_mod_checks.setText(QCoreApplication.translate("submission", u"Checks", None))
        self.preset_mod_deadline.setText(QCoreApplication.translate("submission", u"Deadline", None))
        self.preset_mod_ayon.setText(QCoreApplication.translate("submission", u"Ayon", None))
        self.preset_mod_preferences.setText(QCoreApplication.translate("submission", u"Preferences", None))
        self.preset_mod_exports.setText(QCoreApplication.translate("submission", u"Exports", None))
        self.preset_mod_log.setText(QCoreApplication.translate("submission", u"Log", None))
        self.preset_mod_help.setText(QCoreApplication.translate("submission", u"Help", None))
        self.preset_mod_submission.setText(QCoreApplication.translate("submission", u"Submission", None))
        self.preset_mod_drivelog.setText(QCoreApplication.translate("submission", u"Drive Log", None))
        self.preset_mod_inspector.setText(QCoreApplication.translate("submission", u"Inspector", None))
        self.preset_mod_files.setText(QCoreApplication.translate("submission", u"Files", None))
        self.TopTab.setTabText(self.TopTab.indexOf(self.tab_3), QCoreApplication.translate("submission", u"Presets", None))
        self.TopTab.setTabText(self.TopTab.indexOf(self.tab_21), QCoreApplication.translate("submission", u"Log", None))
        self.textEdit.setHtml(QCoreApplication.translate("submission", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; color:#e8e8e8;\">Submission Helper</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">[2025-06-13]</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">This tool is helping vfx vendors to send media to productions or other studios.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px;"
                        " margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#e8e8e8;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">Each sending usually consists of one or more media files, together with spreadsheet that binds the media files with additional info like notes, status, version, task...</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#e8e8e8;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">This process doesn't seem to have an industry standard, Submission Helper has numerous options to help interface vendor and production with as little friction as possible.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:"
                        "0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#e8e8e8;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://knowledge.autodesk.com/support/shotgrid/getting-started/caas/CloudHelp/cloudhelp/ENU/SG-Tutorials/files/SG-Tutorials-tu-submission-overview-html-html.html\"><span style=\" text-decoration: underline; color:#0000ff;\">Here</span></a><span style=\" color:#e8e8e8;\"> is the overview from ShotGrid:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#e8e8e8;\">Intended use</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-blo"
                        "ck-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">Package starts with one or more files that you want to package and send. Submission Helper checks all the files and helps to produce spreadsheet(s) and email that is easily ingested in receiver's system, often automatically.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#e8e8e8;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#e8e8e8;\">Features</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">* Helps to name the package by the template, including consecutive or per day versions</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-inden"
                        "t:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">* Reads metadata from the files by ffprobe and other methods</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">* Calculates file sizes</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">* Allows to gather and copy sidecar files like CDLs or LUTs to the package.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">* Allows to define spreadsheet columns and values in a flexible way</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">* Generates up to two spreadsheets that are called in gui submission"
                        " and drive log</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">* Generates a text file that is often used for email that follows up the sending.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">* Can read notes from Ftrack</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">* Allows for checking for holes in file sequences, files with zero size and other common problems</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">* Allows saving config to json files</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:"
                        "0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">* Can be used head-less </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#e8e8e8;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#e8e8e8;\">Quick How-to</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">Submission Helper assumes you put the file(s) in one folder - the Package Folder.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#e8e8e8;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-ind"
                        "ent:0px;\"><span style=\" color:#e8e8e8;\">1. Drag the package folder path anywhere to the Submission Helper window</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">2. Set the Package Name options, till the preview matches what you need</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">3. Use Spreadsheet tab to define columns and their values</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">4. Set the export options in Exports and text tabs</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">5. Press Go to export</span></p>\n"
"<p style=\"-qt-para"
                        "graph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#e8e8e8;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#e8e8e8;\">Keywords</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#e8e8e8;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">name: file name, no path, no extension</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">printf_pattern: file name, for file sequence number is replaced with %04d for 0001</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom"
                        ":0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">sequence_nuke: file name, number for file sequence is replaced by [start..end]</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">sequence_slate</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">sequence_slate_nuke</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">clean_name: file name with no extension and no trailing number</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">clean_name_no_sep: file name with no extension and no trailing n"
                        "umber, if there is dot underscore or dash before trailing number, it is removed</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">clean_name_sep_char: the number separation character</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#e8e8e8;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">number: trailing number</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">start_number: first number in file sequence</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span st"
                        "yle=\" color:#e8e8e8;\">end_number: last number in file sequence</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">padding: leading zeroes used for trailing number</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">range: start-end frames for file sequence</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">range_slate: same as range, start+1</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#e8e8e8;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" co"
                        "lor:#e8e8e8;\">extension: file extension, no dot</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#e8e8e8;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">path_prs: path, with no file, no trailing slash</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">full_path: path to the file or first frame in file sequence</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">relative_path: path to the file, minus the path start to the package. Starts with slash</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt"
                        "-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">drive: drive letter (windows)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#e8e8e8;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">size_bytes: file size in bytes, calculated as total for file sequence</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">size_human: same as size_bytes, rounded to one decimal, with units</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#e8e8e8;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-b"
                        "lock-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">category: files are categorized by extension. still, sequence, video, audio, multiframe, other</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#e8e8e8;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">cnt_sub, cnt_log, cnt_txt: counter for each export</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">total_sub, total_log, total_txt: total number of files for each export</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">files_sub, files_log, files_txt: total files for each export</"
                        "span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#e8e8e8;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">d, dd, y, yy, m, mm: today day, month and year</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">package_date: package renaming date </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">package_name: package renaming name</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">package_version: package renaming version</span></p>\n"
"<"
                        "p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">package_name_from_folder: folder name initially provided by user</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">package_name_root: path to the package, without end folder</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#e8e8e8;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_aspect: image aspect, float</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_aspect_x: </span></p>\n"
"<p st"
                        "yle=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_aspect_y:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_audio_present</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_audio_present</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_audio_present</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_bits_per_sample_audio</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block"
                        "-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_channels_audio</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_codec_long_name_audio</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_codec_long_name_video</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_codec_name_audio</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_codec_name_audio</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_"
                        "data_present</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_duration_audio</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_duration_frames</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_duration_frames_slate</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_duration_secs</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_fields</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left"
                        ":0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_fps</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_fps_a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_fps_a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_fps_raw</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_frame_end_from_tc</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_frame_end_from_tc_"
                        "slate</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_frame_start_from_tc</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_frame_start_from_tc_slate</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_height</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_is_log</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_reel</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-rig"
                        "ht:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_sample_rate_audio</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_time_code</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_time_stamp_audio</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_time_stamp_video</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_video_present</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_"
                        "width</span></p></body></html>", None))
        self.TopTab.setTabText(self.TopTab.indexOf(self.tab_14), QCoreApplication.translate("submission", u"Help", None))
        self.BottomTab.setTabText(self.BottomTab.indexOf(self.tab_6), QCoreApplication.translate("submission", u"Submission", None))
        self.BottomTab.setTabText(self.BottomTab.indexOf(self.tab_7), QCoreApplication.translate("submission", u"Drive Log", None))
        self.BottomTab.setTabText(self.BottomTab.indexOf(self.tab_8), QCoreApplication.translate("submission", u"Text", None))
        self.BottomTab.setTabText(self.BottomTab.indexOf(self.tab_15), QCoreApplication.translate("submission", u"Sidecar Files", None))
        self.groupBox_16.setTitle("")
        self.rename_tab_relative.setText(QCoreApplication.translate("submission", u"Relative Paths", None))
        self.rename_tab_absolute.setText(QCoreApplication.translate("submission", u"Absolute Paths", None))
        self.rename_tab_names_only.setText(QCoreApplication.translate("submission", u"File Names Only", None))
        self.BottomTab.setTabText(self.BottomTab.indexOf(self.tab_20), QCoreApplication.translate("submission", u"Rename", None))
        self.label_23.setText(QCoreApplication.translate("submission", u"File:", None))
#if QT_CONFIG(tooltip)
        self.tree_filter_file.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>Template for naming the package. <br/><br/>Keywords:<br/>{package_version} : detects consecutive versions one folder up from package folder<br/>{yy}: year<br/>{mm}: month<br/>{dd}: day</p><p><br/></p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.tree_filter_file.setText("")
        self.label_24.setText(QCoreApplication.translate("submission", u"Key:", None))
#if QT_CONFIG(tooltip)
        self.tree_filter_key.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>Template for naming the package. <br/><br/>Keywords:<br/>{package_version} : detects consecutive versions one folder up from package folder<br/>{yy}: year<br/>{mm}: month<br/>{dd}: day</p><p><br/></p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.tree_filter_key.setText("")
        self.label_25.setText(QCoreApplication.translate("submission", u"Value:", None))
#if QT_CONFIG(tooltip)
        self.tree_filter_value.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>Template for naming the package. <br/><br/>Keywords:<br/>{package_version} : detects consecutive versions one folder up from package folder<br/>{yy}: year<br/>{mm}: month<br/>{dd}: day</p><p><br/></p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.tree_filter_value.setText("")
        self.BottomTab.setTabText(self.BottomTab.indexOf(self.tab_19), QCoreApplication.translate("submission", u"Inspector", None))
        self.BottomTab.setTabText(self.BottomTab.indexOf(self.tab_22), QCoreApplication.translate("submission", u"Files", None))
        self.write_button.setText(QCoreApplication.translate("submission", u"Go", None))
        self.publish_local_button.setText(QCoreApplication.translate("submission", u"Publish Ayon Local", None))
        self.publish_farm_button.setText(QCoreApplication.translate("submission", u"Publish Ayon Deadline", None))
        self.reload.setText(QCoreApplication.translate("submission", u"Reload", None))
    # retranslateUi

