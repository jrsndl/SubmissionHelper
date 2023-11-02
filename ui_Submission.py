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
        submission.resize(863, 600)
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
        self.verticalLayout_51 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_50 = QVBoxLayout()
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.TopTab = QTabWidget(self.centralwidget)
        self.TopTab.setObjectName(u"TopTab")
        sizePolicy.setHeightForWidth(self.TopTab.sizePolicy().hasHeightForWidth())
        self.TopTab.setSizePolicy(sizePolicy)
        self.TopTab.setMinimumSize(QSize(780, 320))
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 814, 542))
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
        self.hl_parse1 = QHBoxLayout()
        self.hl_parse1.setObjectName(u"hl_parse1")
        self.label_18 = QLabel(self.scrollAreaWidgetContents)
        self.label_18.setObjectName(u"label_18")
        sizePolicy2.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy2)
        self.label_18.setMinimumSize(QSize(50, 25))

        self.hl_parse1.addWidget(self.label_18)

        self.parse_name_01 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_name_01.setObjectName(u"parse_name_01")
        sizePolicy1.setHeightForWidth(self.parse_name_01.sizePolicy().hasHeightForWidth())
        self.parse_name_01.setSizePolicy(sizePolicy1)
        self.parse_name_01.setMinimumSize(QSize(30, 25))
        self.parse_name_01.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse1.addWidget(self.parse_name_01)

        self.label_20 = QLabel(self.scrollAreaWidgetContents)
        self.label_20.setObjectName(u"label_20")
        sizePolicy2.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy2)
        self.label_20.setMinimumSize(QSize(50, 25))

        self.hl_parse1.addWidget(self.label_20)

        self.parse_pattern_01 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_pattern_01.setObjectName(u"parse_pattern_01")
        sizePolicy1.setHeightForWidth(self.parse_pattern_01.sizePolicy().hasHeightForWidth())
        self.parse_pattern_01.setSizePolicy(sizePolicy1)
        self.parse_pattern_01.setMinimumSize(QSize(100, 25))

        self.hl_parse1.addWidget(self.parse_pattern_01)

        self.label_19 = QLabel(self.scrollAreaWidgetContents)
        self.label_19.setObjectName(u"label_19")
        sizePolicy2.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy2)
        self.label_19.setMinimumSize(QSize(50, 25))

        self.hl_parse1.addWidget(self.label_19)

        self.parse_repl_01 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_repl_01.setObjectName(u"parse_repl_01")
        sizePolicy1.setHeightForWidth(self.parse_repl_01.sizePolicy().hasHeightForWidth())
        self.parse_repl_01.setSizePolicy(sizePolicy1)
        self.parse_repl_01.setMinimumSize(QSize(80, 25))
        self.parse_repl_01.setMaximumSize(QSize(1600, 16777215))

        self.hl_parse1.addWidget(self.parse_repl_01)

        self.label_21 = QLabel(self.scrollAreaWidgetContents)
        self.label_21.setObjectName(u"label_21")
        sizePolicy2.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy2)
        self.label_21.setMinimumSize(QSize(50, 25))

        self.hl_parse1.addWidget(self.label_21)

        self.parse_source_01 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_source_01.setObjectName(u"parse_source_01")
        sizePolicy1.setHeightForWidth(self.parse_source_01.sizePolicy().hasHeightForWidth())
        self.parse_source_01.setSizePolicy(sizePolicy1)
        self.parse_source_01.setMinimumSize(QSize(30, 25))
        self.parse_source_01.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse1.addWidget(self.parse_source_01)

        self.label_77 = QLabel(self.scrollAreaWidgetContents)
        self.label_77.setObjectName(u"label_77")
        sizePolicy2.setHeightForWidth(self.label_77.sizePolicy().hasHeightForWidth())
        self.label_77.setSizePolicy(sizePolicy2)
        self.label_77.setMinimumSize(QSize(40, 25))

        self.hl_parse1.addWidget(self.label_77)

        self.parse_filter_01 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_filter_01.setObjectName(u"parse_filter_01")
        sizePolicy1.setHeightForWidth(self.parse_filter_01.sizePolicy().hasHeightForWidth())
        self.parse_filter_01.setSizePolicy(sizePolicy1)
        self.parse_filter_01.setMinimumSize(QSize(30, 25))
        self.parse_filter_01.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse1.addWidget(self.parse_filter_01)


        self.verticalLayout_30.addLayout(self.hl_parse1)

        self.hl_parse2 = QHBoxLayout()
        self.hl_parse2.setObjectName(u"hl_parse2")
        self.label_22 = QLabel(self.scrollAreaWidgetContents)
        self.label_22.setObjectName(u"label_22")
        sizePolicy2.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy2)
        self.label_22.setMinimumSize(QSize(50, 25))

        self.hl_parse2.addWidget(self.label_22)

        self.parse_name_02 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_name_02.setObjectName(u"parse_name_02")
        sizePolicy1.setHeightForWidth(self.parse_name_02.sizePolicy().hasHeightForWidth())
        self.parse_name_02.setSizePolicy(sizePolicy1)
        self.parse_name_02.setMinimumSize(QSize(30, 25))
        self.parse_name_02.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse2.addWidget(self.parse_name_02)

        self.label_38 = QLabel(self.scrollAreaWidgetContents)
        self.label_38.setObjectName(u"label_38")
        sizePolicy2.setHeightForWidth(self.label_38.sizePolicy().hasHeightForWidth())
        self.label_38.setSizePolicy(sizePolicy2)
        self.label_38.setMinimumSize(QSize(50, 25))

        self.hl_parse2.addWidget(self.label_38)

        self.parse_pattern_02 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_pattern_02.setObjectName(u"parse_pattern_02")
        sizePolicy1.setHeightForWidth(self.parse_pattern_02.sizePolicy().hasHeightForWidth())
        self.parse_pattern_02.setSizePolicy(sizePolicy1)
        self.parse_pattern_02.setMinimumSize(QSize(100, 25))

        self.hl_parse2.addWidget(self.parse_pattern_02)

        self.label_39 = QLabel(self.scrollAreaWidgetContents)
        self.label_39.setObjectName(u"label_39")
        sizePolicy2.setHeightForWidth(self.label_39.sizePolicy().hasHeightForWidth())
        self.label_39.setSizePolicy(sizePolicy2)
        self.label_39.setMinimumSize(QSize(50, 25))

        self.hl_parse2.addWidget(self.label_39)

        self.parse_repl_02 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_repl_02.setObjectName(u"parse_repl_02")
        sizePolicy1.setHeightForWidth(self.parse_repl_02.sizePolicy().hasHeightForWidth())
        self.parse_repl_02.setSizePolicy(sizePolicy1)
        self.parse_repl_02.setMinimumSize(QSize(80, 25))
        self.parse_repl_02.setMaximumSize(QSize(1600, 16777215))

        self.hl_parse2.addWidget(self.parse_repl_02)

        self.label_40 = QLabel(self.scrollAreaWidgetContents)
        self.label_40.setObjectName(u"label_40")
        sizePolicy2.setHeightForWidth(self.label_40.sizePolicy().hasHeightForWidth())
        self.label_40.setSizePolicy(sizePolicy2)
        self.label_40.setMinimumSize(QSize(50, 25))

        self.hl_parse2.addWidget(self.label_40)

        self.parse_source_02 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_source_02.setObjectName(u"parse_source_02")
        sizePolicy1.setHeightForWidth(self.parse_source_02.sizePolicy().hasHeightForWidth())
        self.parse_source_02.setSizePolicy(sizePolicy1)
        self.parse_source_02.setMinimumSize(QSize(30, 25))
        self.parse_source_02.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse2.addWidget(self.parse_source_02)

        self.label_78 = QLabel(self.scrollAreaWidgetContents)
        self.label_78.setObjectName(u"label_78")
        sizePolicy2.setHeightForWidth(self.label_78.sizePolicy().hasHeightForWidth())
        self.label_78.setSizePolicy(sizePolicy2)
        self.label_78.setMinimumSize(QSize(40, 25))

        self.hl_parse2.addWidget(self.label_78)

        self.parse_filter_02 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_filter_02.setObjectName(u"parse_filter_02")
        sizePolicy1.setHeightForWidth(self.parse_filter_02.sizePolicy().hasHeightForWidth())
        self.parse_filter_02.setSizePolicy(sizePolicy1)
        self.parse_filter_02.setMinimumSize(QSize(30, 25))
        self.parse_filter_02.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse2.addWidget(self.parse_filter_02)


        self.verticalLayout_30.addLayout(self.hl_parse2)

        self.hl_parse3 = QHBoxLayout()
        self.hl_parse3.setObjectName(u"hl_parse3")
        self.label_41 = QLabel(self.scrollAreaWidgetContents)
        self.label_41.setObjectName(u"label_41")
        sizePolicy2.setHeightForWidth(self.label_41.sizePolicy().hasHeightForWidth())
        self.label_41.setSizePolicy(sizePolicy2)
        self.label_41.setMinimumSize(QSize(50, 25))

        self.hl_parse3.addWidget(self.label_41)

        self.parse_name_03 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_name_03.setObjectName(u"parse_name_03")
        sizePolicy1.setHeightForWidth(self.parse_name_03.sizePolicy().hasHeightForWidth())
        self.parse_name_03.setSizePolicy(sizePolicy1)
        self.parse_name_03.setMinimumSize(QSize(30, 25))
        self.parse_name_03.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse3.addWidget(self.parse_name_03)

        self.label_42 = QLabel(self.scrollAreaWidgetContents)
        self.label_42.setObjectName(u"label_42")
        sizePolicy2.setHeightForWidth(self.label_42.sizePolicy().hasHeightForWidth())
        self.label_42.setSizePolicy(sizePolicy2)
        self.label_42.setMinimumSize(QSize(50, 25))

        self.hl_parse3.addWidget(self.label_42)

        self.parse_pattern_03 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_pattern_03.setObjectName(u"parse_pattern_03")
        sizePolicy1.setHeightForWidth(self.parse_pattern_03.sizePolicy().hasHeightForWidth())
        self.parse_pattern_03.setSizePolicy(sizePolicy1)
        self.parse_pattern_03.setMinimumSize(QSize(100, 25))

        self.hl_parse3.addWidget(self.parse_pattern_03)

        self.label_43 = QLabel(self.scrollAreaWidgetContents)
        self.label_43.setObjectName(u"label_43")
        sizePolicy2.setHeightForWidth(self.label_43.sizePolicy().hasHeightForWidth())
        self.label_43.setSizePolicy(sizePolicy2)
        self.label_43.setMinimumSize(QSize(50, 25))

        self.hl_parse3.addWidget(self.label_43)

        self.parse_repl_03 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_repl_03.setObjectName(u"parse_repl_03")
        sizePolicy1.setHeightForWidth(self.parse_repl_03.sizePolicy().hasHeightForWidth())
        self.parse_repl_03.setSizePolicy(sizePolicy1)
        self.parse_repl_03.setMinimumSize(QSize(80, 25))
        self.parse_repl_03.setMaximumSize(QSize(1600, 16777215))

        self.hl_parse3.addWidget(self.parse_repl_03)

        self.label_44 = QLabel(self.scrollAreaWidgetContents)
        self.label_44.setObjectName(u"label_44")
        sizePolicy2.setHeightForWidth(self.label_44.sizePolicy().hasHeightForWidth())
        self.label_44.setSizePolicy(sizePolicy2)
        self.label_44.setMinimumSize(QSize(50, 25))

        self.hl_parse3.addWidget(self.label_44)

        self.parse_source_03 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_source_03.setObjectName(u"parse_source_03")
        sizePolicy1.setHeightForWidth(self.parse_source_03.sizePolicy().hasHeightForWidth())
        self.parse_source_03.setSizePolicy(sizePolicy1)
        self.parse_source_03.setMinimumSize(QSize(30, 25))
        self.parse_source_03.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse3.addWidget(self.parse_source_03)

        self.label_79 = QLabel(self.scrollAreaWidgetContents)
        self.label_79.setObjectName(u"label_79")
        sizePolicy2.setHeightForWidth(self.label_79.sizePolicy().hasHeightForWidth())
        self.label_79.setSizePolicy(sizePolicy2)
        self.label_79.setMinimumSize(QSize(40, 25))

        self.hl_parse3.addWidget(self.label_79)

        self.parse_filter_03 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_filter_03.setObjectName(u"parse_filter_03")
        sizePolicy1.setHeightForWidth(self.parse_filter_03.sizePolicy().hasHeightForWidth())
        self.parse_filter_03.setSizePolicy(sizePolicy1)
        self.parse_filter_03.setMinimumSize(QSize(30, 25))
        self.parse_filter_03.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse3.addWidget(self.parse_filter_03)


        self.verticalLayout_30.addLayout(self.hl_parse3)

        self.hl_parse4 = QHBoxLayout()
        self.hl_parse4.setObjectName(u"hl_parse4")
        self.label_47 = QLabel(self.scrollAreaWidgetContents)
        self.label_47.setObjectName(u"label_47")
        sizePolicy2.setHeightForWidth(self.label_47.sizePolicy().hasHeightForWidth())
        self.label_47.setSizePolicy(sizePolicy2)
        self.label_47.setMinimumSize(QSize(50, 25))

        self.hl_parse4.addWidget(self.label_47)

        self.parse_name_04 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_name_04.setObjectName(u"parse_name_04")
        sizePolicy1.setHeightForWidth(self.parse_name_04.sizePolicy().hasHeightForWidth())
        self.parse_name_04.setSizePolicy(sizePolicy1)
        self.parse_name_04.setMinimumSize(QSize(30, 25))
        self.parse_name_04.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse4.addWidget(self.parse_name_04)

        self.label_48 = QLabel(self.scrollAreaWidgetContents)
        self.label_48.setObjectName(u"label_48")
        sizePolicy2.setHeightForWidth(self.label_48.sizePolicy().hasHeightForWidth())
        self.label_48.setSizePolicy(sizePolicy2)
        self.label_48.setMinimumSize(QSize(50, 25))

        self.hl_parse4.addWidget(self.label_48)

        self.parse_pattern_04 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_pattern_04.setObjectName(u"parse_pattern_04")
        sizePolicy1.setHeightForWidth(self.parse_pattern_04.sizePolicy().hasHeightForWidth())
        self.parse_pattern_04.setSizePolicy(sizePolicy1)
        self.parse_pattern_04.setMinimumSize(QSize(100, 25))

        self.hl_parse4.addWidget(self.parse_pattern_04)

        self.label_49 = QLabel(self.scrollAreaWidgetContents)
        self.label_49.setObjectName(u"label_49")
        sizePolicy2.setHeightForWidth(self.label_49.sizePolicy().hasHeightForWidth())
        self.label_49.setSizePolicy(sizePolicy2)
        self.label_49.setMinimumSize(QSize(50, 25))

        self.hl_parse4.addWidget(self.label_49)

        self.parse_repl_04 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_repl_04.setObjectName(u"parse_repl_04")
        sizePolicy1.setHeightForWidth(self.parse_repl_04.sizePolicy().hasHeightForWidth())
        self.parse_repl_04.setSizePolicy(sizePolicy1)
        self.parse_repl_04.setMinimumSize(QSize(80, 25))
        self.parse_repl_04.setMaximumSize(QSize(1600, 16777215))

        self.hl_parse4.addWidget(self.parse_repl_04)

        self.label_50 = QLabel(self.scrollAreaWidgetContents)
        self.label_50.setObjectName(u"label_50")
        sizePolicy2.setHeightForWidth(self.label_50.sizePolicy().hasHeightForWidth())
        self.label_50.setSizePolicy(sizePolicy2)
        self.label_50.setMinimumSize(QSize(50, 25))

        self.hl_parse4.addWidget(self.label_50)

        self.parse_source_04 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_source_04.setObjectName(u"parse_source_04")
        sizePolicy1.setHeightForWidth(self.parse_source_04.sizePolicy().hasHeightForWidth())
        self.parse_source_04.setSizePolicy(sizePolicy1)
        self.parse_source_04.setMinimumSize(QSize(30, 25))
        self.parse_source_04.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse4.addWidget(self.parse_source_04)

        self.label_80 = QLabel(self.scrollAreaWidgetContents)
        self.label_80.setObjectName(u"label_80")
        sizePolicy2.setHeightForWidth(self.label_80.sizePolicy().hasHeightForWidth())
        self.label_80.setSizePolicy(sizePolicy2)
        self.label_80.setMinimumSize(QSize(40, 25))

        self.hl_parse4.addWidget(self.label_80)

        self.parse_filter_04 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_filter_04.setObjectName(u"parse_filter_04")
        sizePolicy1.setHeightForWidth(self.parse_filter_04.sizePolicy().hasHeightForWidth())
        self.parse_filter_04.setSizePolicy(sizePolicy1)
        self.parse_filter_04.setMinimumSize(QSize(30, 25))
        self.parse_filter_04.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse4.addWidget(self.parse_filter_04)


        self.verticalLayout_30.addLayout(self.hl_parse4)

        self.hl_parse5 = QHBoxLayout()
        self.hl_parse5.setObjectName(u"hl_parse5")
        self.label_55 = QLabel(self.scrollAreaWidgetContents)
        self.label_55.setObjectName(u"label_55")
        sizePolicy2.setHeightForWidth(self.label_55.sizePolicy().hasHeightForWidth())
        self.label_55.setSizePolicy(sizePolicy2)
        self.label_55.setMinimumSize(QSize(50, 25))

        self.hl_parse5.addWidget(self.label_55)

        self.parse_name_05 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_name_05.setObjectName(u"parse_name_05")
        sizePolicy1.setHeightForWidth(self.parse_name_05.sizePolicy().hasHeightForWidth())
        self.parse_name_05.setSizePolicy(sizePolicy1)
        self.parse_name_05.setMinimumSize(QSize(30, 25))
        self.parse_name_05.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse5.addWidget(self.parse_name_05)

        self.label_56 = QLabel(self.scrollAreaWidgetContents)
        self.label_56.setObjectName(u"label_56")
        sizePolicy2.setHeightForWidth(self.label_56.sizePolicy().hasHeightForWidth())
        self.label_56.setSizePolicy(sizePolicy2)
        self.label_56.setMinimumSize(QSize(50, 25))

        self.hl_parse5.addWidget(self.label_56)

        self.parse_pattern_05 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_pattern_05.setObjectName(u"parse_pattern_05")
        sizePolicy1.setHeightForWidth(self.parse_pattern_05.sizePolicy().hasHeightForWidth())
        self.parse_pattern_05.setSizePolicy(sizePolicy1)
        self.parse_pattern_05.setMinimumSize(QSize(100, 25))

        self.hl_parse5.addWidget(self.parse_pattern_05)

        self.label_57 = QLabel(self.scrollAreaWidgetContents)
        self.label_57.setObjectName(u"label_57")
        sizePolicy2.setHeightForWidth(self.label_57.sizePolicy().hasHeightForWidth())
        self.label_57.setSizePolicy(sizePolicy2)
        self.label_57.setMinimumSize(QSize(50, 25))

        self.hl_parse5.addWidget(self.label_57)

        self.parse_repl_05 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_repl_05.setObjectName(u"parse_repl_05")
        sizePolicy1.setHeightForWidth(self.parse_repl_05.sizePolicy().hasHeightForWidth())
        self.parse_repl_05.setSizePolicy(sizePolicy1)
        self.parse_repl_05.setMinimumSize(QSize(80, 25))
        self.parse_repl_05.setMaximumSize(QSize(1600, 16777215))

        self.hl_parse5.addWidget(self.parse_repl_05)

        self.label_58 = QLabel(self.scrollAreaWidgetContents)
        self.label_58.setObjectName(u"label_58")
        sizePolicy2.setHeightForWidth(self.label_58.sizePolicy().hasHeightForWidth())
        self.label_58.setSizePolicy(sizePolicy2)
        self.label_58.setMinimumSize(QSize(50, 25))

        self.hl_parse5.addWidget(self.label_58)

        self.parse_source_05 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_source_05.setObjectName(u"parse_source_05")
        sizePolicy1.setHeightForWidth(self.parse_source_05.sizePolicy().hasHeightForWidth())
        self.parse_source_05.setSizePolicy(sizePolicy1)
        self.parse_source_05.setMinimumSize(QSize(30, 25))
        self.parse_source_05.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse5.addWidget(self.parse_source_05)

        self.label_81 = QLabel(self.scrollAreaWidgetContents)
        self.label_81.setObjectName(u"label_81")
        sizePolicy2.setHeightForWidth(self.label_81.sizePolicy().hasHeightForWidth())
        self.label_81.setSizePolicy(sizePolicy2)
        self.label_81.setMinimumSize(QSize(40, 25))

        self.hl_parse5.addWidget(self.label_81)

        self.parse_filter_05 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_filter_05.setObjectName(u"parse_filter_05")
        sizePolicy1.setHeightForWidth(self.parse_filter_05.sizePolicy().hasHeightForWidth())
        self.parse_filter_05.setSizePolicy(sizePolicy1)
        self.parse_filter_05.setMinimumSize(QSize(30, 25))
        self.parse_filter_05.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse5.addWidget(self.parse_filter_05)


        self.verticalLayout_30.addLayout(self.hl_parse5)

        self.hl_parse6 = QHBoxLayout()
        self.hl_parse6.setObjectName(u"hl_parse6")
        self.label_59 = QLabel(self.scrollAreaWidgetContents)
        self.label_59.setObjectName(u"label_59")
        sizePolicy2.setHeightForWidth(self.label_59.sizePolicy().hasHeightForWidth())
        self.label_59.setSizePolicy(sizePolicy2)
        self.label_59.setMinimumSize(QSize(50, 25))

        self.hl_parse6.addWidget(self.label_59)

        self.parse_name_06 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_name_06.setObjectName(u"parse_name_06")
        sizePolicy1.setHeightForWidth(self.parse_name_06.sizePolicy().hasHeightForWidth())
        self.parse_name_06.setSizePolicy(sizePolicy1)
        self.parse_name_06.setMinimumSize(QSize(30, 25))
        self.parse_name_06.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse6.addWidget(self.parse_name_06)

        self.label_60 = QLabel(self.scrollAreaWidgetContents)
        self.label_60.setObjectName(u"label_60")
        sizePolicy2.setHeightForWidth(self.label_60.sizePolicy().hasHeightForWidth())
        self.label_60.setSizePolicy(sizePolicy2)
        self.label_60.setMinimumSize(QSize(50, 25))

        self.hl_parse6.addWidget(self.label_60)

        self.parse_pattern_06 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_pattern_06.setObjectName(u"parse_pattern_06")
        sizePolicy1.setHeightForWidth(self.parse_pattern_06.sizePolicy().hasHeightForWidth())
        self.parse_pattern_06.setSizePolicy(sizePolicy1)
        self.parse_pattern_06.setMinimumSize(QSize(100, 25))

        self.hl_parse6.addWidget(self.parse_pattern_06)

        self.label_61 = QLabel(self.scrollAreaWidgetContents)
        self.label_61.setObjectName(u"label_61")
        sizePolicy2.setHeightForWidth(self.label_61.sizePolicy().hasHeightForWidth())
        self.label_61.setSizePolicy(sizePolicy2)
        self.label_61.setMinimumSize(QSize(50, 25))

        self.hl_parse6.addWidget(self.label_61)

        self.parse_repl_06 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_repl_06.setObjectName(u"parse_repl_06")
        sizePolicy1.setHeightForWidth(self.parse_repl_06.sizePolicy().hasHeightForWidth())
        self.parse_repl_06.setSizePolicy(sizePolicy1)
        self.parse_repl_06.setMinimumSize(QSize(80, 25))
        self.parse_repl_06.setMaximumSize(QSize(1600, 16777215))

        self.hl_parse6.addWidget(self.parse_repl_06)

        self.label_62 = QLabel(self.scrollAreaWidgetContents)
        self.label_62.setObjectName(u"label_62")
        sizePolicy2.setHeightForWidth(self.label_62.sizePolicy().hasHeightForWidth())
        self.label_62.setSizePolicy(sizePolicy2)
        self.label_62.setMinimumSize(QSize(50, 25))

        self.hl_parse6.addWidget(self.label_62)

        self.parse_source_06 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_source_06.setObjectName(u"parse_source_06")
        sizePolicy1.setHeightForWidth(self.parse_source_06.sizePolicy().hasHeightForWidth())
        self.parse_source_06.setSizePolicy(sizePolicy1)
        self.parse_source_06.setMinimumSize(QSize(30, 25))
        self.parse_source_06.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse6.addWidget(self.parse_source_06)

        self.label_82 = QLabel(self.scrollAreaWidgetContents)
        self.label_82.setObjectName(u"label_82")
        sizePolicy2.setHeightForWidth(self.label_82.sizePolicy().hasHeightForWidth())
        self.label_82.setSizePolicy(sizePolicy2)
        self.label_82.setMinimumSize(QSize(40, 25))

        self.hl_parse6.addWidget(self.label_82)

        self.parse_filter_06 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_filter_06.setObjectName(u"parse_filter_06")
        sizePolicy1.setHeightForWidth(self.parse_filter_06.sizePolicy().hasHeightForWidth())
        self.parse_filter_06.setSizePolicy(sizePolicy1)
        self.parse_filter_06.setMinimumSize(QSize(30, 25))
        self.parse_filter_06.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse6.addWidget(self.parse_filter_06)


        self.verticalLayout_30.addLayout(self.hl_parse6)

        self.hl_parse7 = QHBoxLayout()
        self.hl_parse7.setObjectName(u"hl_parse7")
        self.label_63 = QLabel(self.scrollAreaWidgetContents)
        self.label_63.setObjectName(u"label_63")
        sizePolicy2.setHeightForWidth(self.label_63.sizePolicy().hasHeightForWidth())
        self.label_63.setSizePolicy(sizePolicy2)
        self.label_63.setMinimumSize(QSize(50, 25))

        self.hl_parse7.addWidget(self.label_63)

        self.parse_name_07 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_name_07.setObjectName(u"parse_name_07")
        sizePolicy1.setHeightForWidth(self.parse_name_07.sizePolicy().hasHeightForWidth())
        self.parse_name_07.setSizePolicy(sizePolicy1)
        self.parse_name_07.setMinimumSize(QSize(30, 25))
        self.parse_name_07.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse7.addWidget(self.parse_name_07)

        self.label_64 = QLabel(self.scrollAreaWidgetContents)
        self.label_64.setObjectName(u"label_64")
        sizePolicy2.setHeightForWidth(self.label_64.sizePolicy().hasHeightForWidth())
        self.label_64.setSizePolicy(sizePolicy2)
        self.label_64.setMinimumSize(QSize(50, 25))

        self.hl_parse7.addWidget(self.label_64)

        self.parse_pattern_07 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_pattern_07.setObjectName(u"parse_pattern_07")
        sizePolicy1.setHeightForWidth(self.parse_pattern_07.sizePolicy().hasHeightForWidth())
        self.parse_pattern_07.setSizePolicy(sizePolicy1)
        self.parse_pattern_07.setMinimumSize(QSize(100, 25))

        self.hl_parse7.addWidget(self.parse_pattern_07)

        self.label_65 = QLabel(self.scrollAreaWidgetContents)
        self.label_65.setObjectName(u"label_65")
        sizePolicy2.setHeightForWidth(self.label_65.sizePolicy().hasHeightForWidth())
        self.label_65.setSizePolicy(sizePolicy2)
        self.label_65.setMinimumSize(QSize(50, 25))

        self.hl_parse7.addWidget(self.label_65)

        self.parse_repl_07 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_repl_07.setObjectName(u"parse_repl_07")
        sizePolicy1.setHeightForWidth(self.parse_repl_07.sizePolicy().hasHeightForWidth())
        self.parse_repl_07.setSizePolicy(sizePolicy1)
        self.parse_repl_07.setMinimumSize(QSize(80, 25))
        self.parse_repl_07.setMaximumSize(QSize(1600, 16777215))

        self.hl_parse7.addWidget(self.parse_repl_07)

        self.label_66 = QLabel(self.scrollAreaWidgetContents)
        self.label_66.setObjectName(u"label_66")
        sizePolicy2.setHeightForWidth(self.label_66.sizePolicy().hasHeightForWidth())
        self.label_66.setSizePolicy(sizePolicy2)
        self.label_66.setMinimumSize(QSize(50, 25))

        self.hl_parse7.addWidget(self.label_66)

        self.parse_source_07 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_source_07.setObjectName(u"parse_source_07")
        sizePolicy1.setHeightForWidth(self.parse_source_07.sizePolicy().hasHeightForWidth())
        self.parse_source_07.setSizePolicy(sizePolicy1)
        self.parse_source_07.setMinimumSize(QSize(30, 25))
        self.parse_source_07.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse7.addWidget(self.parse_source_07)

        self.label_83 = QLabel(self.scrollAreaWidgetContents)
        self.label_83.setObjectName(u"label_83")
        sizePolicy2.setHeightForWidth(self.label_83.sizePolicy().hasHeightForWidth())
        self.label_83.setSizePolicy(sizePolicy2)
        self.label_83.setMinimumSize(QSize(40, 25))

        self.hl_parse7.addWidget(self.label_83)

        self.parse_filter_07 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_filter_07.setObjectName(u"parse_filter_07")
        sizePolicy1.setHeightForWidth(self.parse_filter_07.sizePolicy().hasHeightForWidth())
        self.parse_filter_07.setSizePolicy(sizePolicy1)
        self.parse_filter_07.setMinimumSize(QSize(30, 25))
        self.parse_filter_07.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse7.addWidget(self.parse_filter_07)


        self.verticalLayout_30.addLayout(self.hl_parse7)

        self.hl_parse8 = QHBoxLayout()
        self.hl_parse8.setObjectName(u"hl_parse8")
        self.label_67 = QLabel(self.scrollAreaWidgetContents)
        self.label_67.setObjectName(u"label_67")
        sizePolicy2.setHeightForWidth(self.label_67.sizePolicy().hasHeightForWidth())
        self.label_67.setSizePolicy(sizePolicy2)
        self.label_67.setMinimumSize(QSize(50, 25))

        self.hl_parse8.addWidget(self.label_67)

        self.parse_name_08 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_name_08.setObjectName(u"parse_name_08")
        sizePolicy1.setHeightForWidth(self.parse_name_08.sizePolicy().hasHeightForWidth())
        self.parse_name_08.setSizePolicy(sizePolicy1)
        self.parse_name_08.setMinimumSize(QSize(30, 25))
        self.parse_name_08.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse8.addWidget(self.parse_name_08)

        self.label_68 = QLabel(self.scrollAreaWidgetContents)
        self.label_68.setObjectName(u"label_68")
        sizePolicy2.setHeightForWidth(self.label_68.sizePolicy().hasHeightForWidth())
        self.label_68.setSizePolicy(sizePolicy2)
        self.label_68.setMinimumSize(QSize(50, 25))

        self.hl_parse8.addWidget(self.label_68)

        self.parse_pattern_08 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_pattern_08.setObjectName(u"parse_pattern_08")
        sizePolicy1.setHeightForWidth(self.parse_pattern_08.sizePolicy().hasHeightForWidth())
        self.parse_pattern_08.setSizePolicy(sizePolicy1)
        self.parse_pattern_08.setMinimumSize(QSize(100, 25))

        self.hl_parse8.addWidget(self.parse_pattern_08)

        self.label_69 = QLabel(self.scrollAreaWidgetContents)
        self.label_69.setObjectName(u"label_69")
        sizePolicy2.setHeightForWidth(self.label_69.sizePolicy().hasHeightForWidth())
        self.label_69.setSizePolicy(sizePolicy2)
        self.label_69.setMinimumSize(QSize(50, 25))

        self.hl_parse8.addWidget(self.label_69)

        self.parse_repl_08 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_repl_08.setObjectName(u"parse_repl_08")
        sizePolicy1.setHeightForWidth(self.parse_repl_08.sizePolicy().hasHeightForWidth())
        self.parse_repl_08.setSizePolicy(sizePolicy1)
        self.parse_repl_08.setMinimumSize(QSize(80, 25))
        self.parse_repl_08.setMaximumSize(QSize(1600, 16777215))

        self.hl_parse8.addWidget(self.parse_repl_08)

        self.label_70 = QLabel(self.scrollAreaWidgetContents)
        self.label_70.setObjectName(u"label_70")
        sizePolicy2.setHeightForWidth(self.label_70.sizePolicy().hasHeightForWidth())
        self.label_70.setSizePolicy(sizePolicy2)
        self.label_70.setMinimumSize(QSize(50, 25))

        self.hl_parse8.addWidget(self.label_70)

        self.parse_source_08 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_source_08.setObjectName(u"parse_source_08")
        sizePolicy1.setHeightForWidth(self.parse_source_08.sizePolicy().hasHeightForWidth())
        self.parse_source_08.setSizePolicy(sizePolicy1)
        self.parse_source_08.setMinimumSize(QSize(30, 25))
        self.parse_source_08.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse8.addWidget(self.parse_source_08)

        self.label_84 = QLabel(self.scrollAreaWidgetContents)
        self.label_84.setObjectName(u"label_84")
        sizePolicy2.setHeightForWidth(self.label_84.sizePolicy().hasHeightForWidth())
        self.label_84.setSizePolicy(sizePolicy2)
        self.label_84.setMinimumSize(QSize(40, 25))

        self.hl_parse8.addWidget(self.label_84)

        self.parse_filter_08 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_filter_08.setObjectName(u"parse_filter_08")
        sizePolicy1.setHeightForWidth(self.parse_filter_08.sizePolicy().hasHeightForWidth())
        self.parse_filter_08.setSizePolicy(sizePolicy1)
        self.parse_filter_08.setMinimumSize(QSize(30, 25))
        self.parse_filter_08.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse8.addWidget(self.parse_filter_08)


        self.verticalLayout_30.addLayout(self.hl_parse8)

        self.hl_parse9 = QHBoxLayout()
        self.hl_parse9.setObjectName(u"hl_parse9")
        self.label_71 = QLabel(self.scrollAreaWidgetContents)
        self.label_71.setObjectName(u"label_71")
        sizePolicy2.setHeightForWidth(self.label_71.sizePolicy().hasHeightForWidth())
        self.label_71.setSizePolicy(sizePolicy2)
        self.label_71.setMinimumSize(QSize(50, 25))

        self.hl_parse9.addWidget(self.label_71)

        self.parse_name_09 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_name_09.setObjectName(u"parse_name_09")
        sizePolicy1.setHeightForWidth(self.parse_name_09.sizePolicy().hasHeightForWidth())
        self.parse_name_09.setSizePolicy(sizePolicy1)
        self.parse_name_09.setMinimumSize(QSize(30, 25))
        self.parse_name_09.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse9.addWidget(self.parse_name_09)

        self.label_72 = QLabel(self.scrollAreaWidgetContents)
        self.label_72.setObjectName(u"label_72")
        sizePolicy2.setHeightForWidth(self.label_72.sizePolicy().hasHeightForWidth())
        self.label_72.setSizePolicy(sizePolicy2)
        self.label_72.setMinimumSize(QSize(50, 25))

        self.hl_parse9.addWidget(self.label_72)

        self.parse_pattern_09 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_pattern_09.setObjectName(u"parse_pattern_09")
        sizePolicy1.setHeightForWidth(self.parse_pattern_09.sizePolicy().hasHeightForWidth())
        self.parse_pattern_09.setSizePolicy(sizePolicy1)
        self.parse_pattern_09.setMinimumSize(QSize(100, 25))

        self.hl_parse9.addWidget(self.parse_pattern_09)

        self.label_73 = QLabel(self.scrollAreaWidgetContents)
        self.label_73.setObjectName(u"label_73")
        sizePolicy2.setHeightForWidth(self.label_73.sizePolicy().hasHeightForWidth())
        self.label_73.setSizePolicy(sizePolicy2)
        self.label_73.setMinimumSize(QSize(50, 25))

        self.hl_parse9.addWidget(self.label_73)

        self.parse_repl_09 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_repl_09.setObjectName(u"parse_repl_09")
        sizePolicy1.setHeightForWidth(self.parse_repl_09.sizePolicy().hasHeightForWidth())
        self.parse_repl_09.setSizePolicy(sizePolicy1)
        self.parse_repl_09.setMinimumSize(QSize(80, 25))
        self.parse_repl_09.setMaximumSize(QSize(1600, 16777215))

        self.hl_parse9.addWidget(self.parse_repl_09)

        self.label_74 = QLabel(self.scrollAreaWidgetContents)
        self.label_74.setObjectName(u"label_74")
        sizePolicy2.setHeightForWidth(self.label_74.sizePolicy().hasHeightForWidth())
        self.label_74.setSizePolicy(sizePolicy2)
        self.label_74.setMinimumSize(QSize(50, 25))

        self.hl_parse9.addWidget(self.label_74)

        self.parse_source_09 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_source_09.setObjectName(u"parse_source_09")
        sizePolicy1.setHeightForWidth(self.parse_source_09.sizePolicy().hasHeightForWidth())
        self.parse_source_09.setSizePolicy(sizePolicy1)
        self.parse_source_09.setMinimumSize(QSize(30, 25))
        self.parse_source_09.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse9.addWidget(self.parse_source_09)

        self.label_85 = QLabel(self.scrollAreaWidgetContents)
        self.label_85.setObjectName(u"label_85")
        sizePolicy2.setHeightForWidth(self.label_85.sizePolicy().hasHeightForWidth())
        self.label_85.setSizePolicy(sizePolicy2)
        self.label_85.setMinimumSize(QSize(40, 25))

        self.hl_parse9.addWidget(self.label_85)

        self.parse_filter_09 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_filter_09.setObjectName(u"parse_filter_09")
        sizePolicy1.setHeightForWidth(self.parse_filter_09.sizePolicy().hasHeightForWidth())
        self.parse_filter_09.setSizePolicy(sizePolicy1)
        self.parse_filter_09.setMinimumSize(QSize(30, 25))
        self.parse_filter_09.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse9.addWidget(self.parse_filter_09)


        self.verticalLayout_30.addLayout(self.hl_parse9)

        self.hl_parse10 = QHBoxLayout()
        self.hl_parse10.setObjectName(u"hl_parse10")
        self.label_87 = QLabel(self.scrollAreaWidgetContents)
        self.label_87.setObjectName(u"label_87")
        sizePolicy2.setHeightForWidth(self.label_87.sizePolicy().hasHeightForWidth())
        self.label_87.setSizePolicy(sizePolicy2)
        self.label_87.setMinimumSize(QSize(50, 25))

        self.hl_parse10.addWidget(self.label_87)

        self.parse_name_10 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_name_10.setObjectName(u"parse_name_10")
        sizePolicy1.setHeightForWidth(self.parse_name_10.sizePolicy().hasHeightForWidth())
        self.parse_name_10.setSizePolicy(sizePolicy1)
        self.parse_name_10.setMinimumSize(QSize(30, 25))
        self.parse_name_10.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse10.addWidget(self.parse_name_10)

        self.label_114 = QLabel(self.scrollAreaWidgetContents)
        self.label_114.setObjectName(u"label_114")
        sizePolicy2.setHeightForWidth(self.label_114.sizePolicy().hasHeightForWidth())
        self.label_114.setSizePolicy(sizePolicy2)
        self.label_114.setMinimumSize(QSize(50, 25))

        self.hl_parse10.addWidget(self.label_114)

        self.parse_pattern_10 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_pattern_10.setObjectName(u"parse_pattern_10")
        sizePolicy1.setHeightForWidth(self.parse_pattern_10.sizePolicy().hasHeightForWidth())
        self.parse_pattern_10.setSizePolicy(sizePolicy1)
        self.parse_pattern_10.setMinimumSize(QSize(100, 25))

        self.hl_parse10.addWidget(self.parse_pattern_10)

        self.label_115 = QLabel(self.scrollAreaWidgetContents)
        self.label_115.setObjectName(u"label_115")
        sizePolicy2.setHeightForWidth(self.label_115.sizePolicy().hasHeightForWidth())
        self.label_115.setSizePolicy(sizePolicy2)
        self.label_115.setMinimumSize(QSize(50, 25))

        self.hl_parse10.addWidget(self.label_115)

        self.parse_repl_10 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_repl_10.setObjectName(u"parse_repl_10")
        sizePolicy1.setHeightForWidth(self.parse_repl_10.sizePolicy().hasHeightForWidth())
        self.parse_repl_10.setSizePolicy(sizePolicy1)
        self.parse_repl_10.setMinimumSize(QSize(80, 25))
        self.parse_repl_10.setMaximumSize(QSize(1600, 16777215))

        self.hl_parse10.addWidget(self.parse_repl_10)

        self.label_116 = QLabel(self.scrollAreaWidgetContents)
        self.label_116.setObjectName(u"label_116")
        sizePolicy2.setHeightForWidth(self.label_116.sizePolicy().hasHeightForWidth())
        self.label_116.setSizePolicy(sizePolicy2)
        self.label_116.setMinimumSize(QSize(50, 25))

        self.hl_parse10.addWidget(self.label_116)

        self.parse_source_10 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_source_10.setObjectName(u"parse_source_10")
        sizePolicy1.setHeightForWidth(self.parse_source_10.sizePolicy().hasHeightForWidth())
        self.parse_source_10.setSizePolicy(sizePolicy1)
        self.parse_source_10.setMinimumSize(QSize(30, 25))
        self.parse_source_10.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse10.addWidget(self.parse_source_10)

        self.label_117 = QLabel(self.scrollAreaWidgetContents)
        self.label_117.setObjectName(u"label_117")
        sizePolicy2.setHeightForWidth(self.label_117.sizePolicy().hasHeightForWidth())
        self.label_117.setSizePolicy(sizePolicy2)
        self.label_117.setMinimumSize(QSize(40, 25))

        self.hl_parse10.addWidget(self.label_117)

        self.parse_filter_10 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_filter_10.setObjectName(u"parse_filter_10")
        sizePolicy1.setHeightForWidth(self.parse_filter_10.sizePolicy().hasHeightForWidth())
        self.parse_filter_10.setSizePolicy(sizePolicy1)
        self.parse_filter_10.setMinimumSize(QSize(30, 25))
        self.parse_filter_10.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse10.addWidget(self.parse_filter_10)


        self.verticalLayout_30.addLayout(self.hl_parse10)

        self.hl_parse11 = QHBoxLayout()
        self.hl_parse11.setObjectName(u"hl_parse11")
        self.label_118 = QLabel(self.scrollAreaWidgetContents)
        self.label_118.setObjectName(u"label_118")
        sizePolicy2.setHeightForWidth(self.label_118.sizePolicy().hasHeightForWidth())
        self.label_118.setSizePolicy(sizePolicy2)
        self.label_118.setMinimumSize(QSize(50, 25))

        self.hl_parse11.addWidget(self.label_118)

        self.parse_name_11 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_name_11.setObjectName(u"parse_name_11")
        sizePolicy1.setHeightForWidth(self.parse_name_11.sizePolicy().hasHeightForWidth())
        self.parse_name_11.setSizePolicy(sizePolicy1)
        self.parse_name_11.setMinimumSize(QSize(30, 25))
        self.parse_name_11.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse11.addWidget(self.parse_name_11)

        self.label_119 = QLabel(self.scrollAreaWidgetContents)
        self.label_119.setObjectName(u"label_119")
        sizePolicy2.setHeightForWidth(self.label_119.sizePolicy().hasHeightForWidth())
        self.label_119.setSizePolicy(sizePolicy2)
        self.label_119.setMinimumSize(QSize(50, 25))

        self.hl_parse11.addWidget(self.label_119)

        self.parse_pattern_11 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_pattern_11.setObjectName(u"parse_pattern_11")
        sizePolicy1.setHeightForWidth(self.parse_pattern_11.sizePolicy().hasHeightForWidth())
        self.parse_pattern_11.setSizePolicy(sizePolicy1)
        self.parse_pattern_11.setMinimumSize(QSize(100, 25))

        self.hl_parse11.addWidget(self.parse_pattern_11)

        self.label_120 = QLabel(self.scrollAreaWidgetContents)
        self.label_120.setObjectName(u"label_120")
        sizePolicy2.setHeightForWidth(self.label_120.sizePolicy().hasHeightForWidth())
        self.label_120.setSizePolicy(sizePolicy2)
        self.label_120.setMinimumSize(QSize(50, 25))

        self.hl_parse11.addWidget(self.label_120)

        self.parse_repl_11 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_repl_11.setObjectName(u"parse_repl_11")
        sizePolicy1.setHeightForWidth(self.parse_repl_11.sizePolicy().hasHeightForWidth())
        self.parse_repl_11.setSizePolicy(sizePolicy1)
        self.parse_repl_11.setMinimumSize(QSize(80, 25))
        self.parse_repl_11.setMaximumSize(QSize(1600, 16777215))

        self.hl_parse11.addWidget(self.parse_repl_11)

        self.label_121 = QLabel(self.scrollAreaWidgetContents)
        self.label_121.setObjectName(u"label_121")
        sizePolicy2.setHeightForWidth(self.label_121.sizePolicy().hasHeightForWidth())
        self.label_121.setSizePolicy(sizePolicy2)
        self.label_121.setMinimumSize(QSize(50, 25))

        self.hl_parse11.addWidget(self.label_121)

        self.parse_source_11 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_source_11.setObjectName(u"parse_source_11")
        sizePolicy1.setHeightForWidth(self.parse_source_11.sizePolicy().hasHeightForWidth())
        self.parse_source_11.setSizePolicy(sizePolicy1)
        self.parse_source_11.setMinimumSize(QSize(30, 25))
        self.parse_source_11.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse11.addWidget(self.parse_source_11)

        self.label_122 = QLabel(self.scrollAreaWidgetContents)
        self.label_122.setObjectName(u"label_122")
        sizePolicy2.setHeightForWidth(self.label_122.sizePolicy().hasHeightForWidth())
        self.label_122.setSizePolicy(sizePolicy2)
        self.label_122.setMinimumSize(QSize(40, 25))

        self.hl_parse11.addWidget(self.label_122)

        self.parse_filter_11 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_filter_11.setObjectName(u"parse_filter_11")
        sizePolicy1.setHeightForWidth(self.parse_filter_11.sizePolicy().hasHeightForWidth())
        self.parse_filter_11.setSizePolicy(sizePolicy1)
        self.parse_filter_11.setMinimumSize(QSize(30, 25))
        self.parse_filter_11.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse11.addWidget(self.parse_filter_11)


        self.verticalLayout_30.addLayout(self.hl_parse11)

        self.hl_parse12 = QHBoxLayout()
        self.hl_parse12.setObjectName(u"hl_parse12")
        self.label_123 = QLabel(self.scrollAreaWidgetContents)
        self.label_123.setObjectName(u"label_123")
        sizePolicy2.setHeightForWidth(self.label_123.sizePolicy().hasHeightForWidth())
        self.label_123.setSizePolicy(sizePolicy2)
        self.label_123.setMinimumSize(QSize(50, 25))

        self.hl_parse12.addWidget(self.label_123)

        self.parse_name_12 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_name_12.setObjectName(u"parse_name_12")
        sizePolicy1.setHeightForWidth(self.parse_name_12.sizePolicy().hasHeightForWidth())
        self.parse_name_12.setSizePolicy(sizePolicy1)
        self.parse_name_12.setMinimumSize(QSize(30, 25))
        self.parse_name_12.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse12.addWidget(self.parse_name_12)

        self.label_124 = QLabel(self.scrollAreaWidgetContents)
        self.label_124.setObjectName(u"label_124")
        sizePolicy2.setHeightForWidth(self.label_124.sizePolicy().hasHeightForWidth())
        self.label_124.setSizePolicy(sizePolicy2)
        self.label_124.setMinimumSize(QSize(50, 25))

        self.hl_parse12.addWidget(self.label_124)

        self.parse_pattern_12 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_pattern_12.setObjectName(u"parse_pattern_12")
        sizePolicy1.setHeightForWidth(self.parse_pattern_12.sizePolicy().hasHeightForWidth())
        self.parse_pattern_12.setSizePolicy(sizePolicy1)
        self.parse_pattern_12.setMinimumSize(QSize(100, 25))

        self.hl_parse12.addWidget(self.parse_pattern_12)

        self.label_125 = QLabel(self.scrollAreaWidgetContents)
        self.label_125.setObjectName(u"label_125")
        sizePolicy2.setHeightForWidth(self.label_125.sizePolicy().hasHeightForWidth())
        self.label_125.setSizePolicy(sizePolicy2)
        self.label_125.setMinimumSize(QSize(50, 25))

        self.hl_parse12.addWidget(self.label_125)

        self.parse_repl_12 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_repl_12.setObjectName(u"parse_repl_12")
        sizePolicy1.setHeightForWidth(self.parse_repl_12.sizePolicy().hasHeightForWidth())
        self.parse_repl_12.setSizePolicy(sizePolicy1)
        self.parse_repl_12.setMinimumSize(QSize(80, 25))
        self.parse_repl_12.setMaximumSize(QSize(1600, 16777215))

        self.hl_parse12.addWidget(self.parse_repl_12)

        self.label_126 = QLabel(self.scrollAreaWidgetContents)
        self.label_126.setObjectName(u"label_126")
        sizePolicy2.setHeightForWidth(self.label_126.sizePolicy().hasHeightForWidth())
        self.label_126.setSizePolicy(sizePolicy2)
        self.label_126.setMinimumSize(QSize(50, 25))

        self.hl_parse12.addWidget(self.label_126)

        self.parse_source_12 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_source_12.setObjectName(u"parse_source_12")
        sizePolicy1.setHeightForWidth(self.parse_source_12.sizePolicy().hasHeightForWidth())
        self.parse_source_12.setSizePolicy(sizePolicy1)
        self.parse_source_12.setMinimumSize(QSize(30, 25))
        self.parse_source_12.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse12.addWidget(self.parse_source_12)

        self.label_127 = QLabel(self.scrollAreaWidgetContents)
        self.label_127.setObjectName(u"label_127")
        sizePolicy2.setHeightForWidth(self.label_127.sizePolicy().hasHeightForWidth())
        self.label_127.setSizePolicy(sizePolicy2)
        self.label_127.setMinimumSize(QSize(40, 25))

        self.hl_parse12.addWidget(self.label_127)

        self.parse_filter_12 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_filter_12.setObjectName(u"parse_filter_12")
        sizePolicy1.setHeightForWidth(self.parse_filter_12.sizePolicy().hasHeightForWidth())
        self.parse_filter_12.setSizePolicy(sizePolicy1)
        self.parse_filter_12.setMinimumSize(QSize(30, 25))
        self.parse_filter_12.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse12.addWidget(self.parse_filter_12)


        self.verticalLayout_30.addLayout(self.hl_parse12)

        self.hl_parse13 = QHBoxLayout()
        self.hl_parse13.setObjectName(u"hl_parse13")
        self.label_128 = QLabel(self.scrollAreaWidgetContents)
        self.label_128.setObjectName(u"label_128")
        sizePolicy2.setHeightForWidth(self.label_128.sizePolicy().hasHeightForWidth())
        self.label_128.setSizePolicy(sizePolicy2)
        self.label_128.setMinimumSize(QSize(50, 25))

        self.hl_parse13.addWidget(self.label_128)

        self.parse_name_13 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_name_13.setObjectName(u"parse_name_13")
        sizePolicy1.setHeightForWidth(self.parse_name_13.sizePolicy().hasHeightForWidth())
        self.parse_name_13.setSizePolicy(sizePolicy1)
        self.parse_name_13.setMinimumSize(QSize(30, 25))
        self.parse_name_13.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse13.addWidget(self.parse_name_13)

        self.label_129 = QLabel(self.scrollAreaWidgetContents)
        self.label_129.setObjectName(u"label_129")
        sizePolicy2.setHeightForWidth(self.label_129.sizePolicy().hasHeightForWidth())
        self.label_129.setSizePolicy(sizePolicy2)
        self.label_129.setMinimumSize(QSize(50, 25))

        self.hl_parse13.addWidget(self.label_129)

        self.parse_pattern_13 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_pattern_13.setObjectName(u"parse_pattern_13")
        sizePolicy1.setHeightForWidth(self.parse_pattern_13.sizePolicy().hasHeightForWidth())
        self.parse_pattern_13.setSizePolicy(sizePolicy1)
        self.parse_pattern_13.setMinimumSize(QSize(100, 25))

        self.hl_parse13.addWidget(self.parse_pattern_13)

        self.label_130 = QLabel(self.scrollAreaWidgetContents)
        self.label_130.setObjectName(u"label_130")
        sizePolicy2.setHeightForWidth(self.label_130.sizePolicy().hasHeightForWidth())
        self.label_130.setSizePolicy(sizePolicy2)
        self.label_130.setMinimumSize(QSize(50, 25))

        self.hl_parse13.addWidget(self.label_130)

        self.parse_repl_13 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_repl_13.setObjectName(u"parse_repl_13")
        sizePolicy1.setHeightForWidth(self.parse_repl_13.sizePolicy().hasHeightForWidth())
        self.parse_repl_13.setSizePolicy(sizePolicy1)
        self.parse_repl_13.setMinimumSize(QSize(80, 25))
        self.parse_repl_13.setMaximumSize(QSize(1600, 16777215))

        self.hl_parse13.addWidget(self.parse_repl_13)

        self.label_131 = QLabel(self.scrollAreaWidgetContents)
        self.label_131.setObjectName(u"label_131")
        sizePolicy2.setHeightForWidth(self.label_131.sizePolicy().hasHeightForWidth())
        self.label_131.setSizePolicy(sizePolicy2)
        self.label_131.setMinimumSize(QSize(50, 25))

        self.hl_parse13.addWidget(self.label_131)

        self.parse_source_13 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_source_13.setObjectName(u"parse_source_13")
        sizePolicy1.setHeightForWidth(self.parse_source_13.sizePolicy().hasHeightForWidth())
        self.parse_source_13.setSizePolicy(sizePolicy1)
        self.parse_source_13.setMinimumSize(QSize(30, 25))
        self.parse_source_13.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse13.addWidget(self.parse_source_13)

        self.label_132 = QLabel(self.scrollAreaWidgetContents)
        self.label_132.setObjectName(u"label_132")
        sizePolicy2.setHeightForWidth(self.label_132.sizePolicy().hasHeightForWidth())
        self.label_132.setSizePolicy(sizePolicy2)
        self.label_132.setMinimumSize(QSize(40, 25))

        self.hl_parse13.addWidget(self.label_132)

        self.parse_filter_13 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_filter_13.setObjectName(u"parse_filter_13")
        sizePolicy1.setHeightForWidth(self.parse_filter_13.sizePolicy().hasHeightForWidth())
        self.parse_filter_13.setSizePolicy(sizePolicy1)
        self.parse_filter_13.setMinimumSize(QSize(30, 25))
        self.parse_filter_13.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse13.addWidget(self.parse_filter_13)


        self.verticalLayout_30.addLayout(self.hl_parse13)

        self.hl_parse14 = QHBoxLayout()
        self.hl_parse14.setObjectName(u"hl_parse14")
        self.label_133 = QLabel(self.scrollAreaWidgetContents)
        self.label_133.setObjectName(u"label_133")
        sizePolicy2.setHeightForWidth(self.label_133.sizePolicy().hasHeightForWidth())
        self.label_133.setSizePolicy(sizePolicy2)
        self.label_133.setMinimumSize(QSize(50, 25))

        self.hl_parse14.addWidget(self.label_133)

        self.parse_name_14 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_name_14.setObjectName(u"parse_name_14")
        sizePolicy1.setHeightForWidth(self.parse_name_14.sizePolicy().hasHeightForWidth())
        self.parse_name_14.setSizePolicy(sizePolicy1)
        self.parse_name_14.setMinimumSize(QSize(30, 25))
        self.parse_name_14.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse14.addWidget(self.parse_name_14)

        self.label_144 = QLabel(self.scrollAreaWidgetContents)
        self.label_144.setObjectName(u"label_144")
        sizePolicy2.setHeightForWidth(self.label_144.sizePolicy().hasHeightForWidth())
        self.label_144.setSizePolicy(sizePolicy2)
        self.label_144.setMinimumSize(QSize(50, 25))

        self.hl_parse14.addWidget(self.label_144)

        self.parse_pattern_14 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_pattern_14.setObjectName(u"parse_pattern_14")
        sizePolicy1.setHeightForWidth(self.parse_pattern_14.sizePolicy().hasHeightForWidth())
        self.parse_pattern_14.setSizePolicy(sizePolicy1)
        self.parse_pattern_14.setMinimumSize(QSize(100, 25))

        self.hl_parse14.addWidget(self.parse_pattern_14)

        self.label_145 = QLabel(self.scrollAreaWidgetContents)
        self.label_145.setObjectName(u"label_145")
        sizePolicy2.setHeightForWidth(self.label_145.sizePolicy().hasHeightForWidth())
        self.label_145.setSizePolicy(sizePolicy2)
        self.label_145.setMinimumSize(QSize(50, 25))

        self.hl_parse14.addWidget(self.label_145)

        self.parse_repl_14 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_repl_14.setObjectName(u"parse_repl_14")
        sizePolicy1.setHeightForWidth(self.parse_repl_14.sizePolicy().hasHeightForWidth())
        self.parse_repl_14.setSizePolicy(sizePolicy1)
        self.parse_repl_14.setMinimumSize(QSize(80, 25))
        self.parse_repl_14.setMaximumSize(QSize(1600, 16777215))

        self.hl_parse14.addWidget(self.parse_repl_14)

        self.label_146 = QLabel(self.scrollAreaWidgetContents)
        self.label_146.setObjectName(u"label_146")
        sizePolicy2.setHeightForWidth(self.label_146.sizePolicy().hasHeightForWidth())
        self.label_146.setSizePolicy(sizePolicy2)
        self.label_146.setMinimumSize(QSize(50, 25))

        self.hl_parse14.addWidget(self.label_146)

        self.parse_source_14 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_source_14.setObjectName(u"parse_source_14")
        sizePolicy1.setHeightForWidth(self.parse_source_14.sizePolicy().hasHeightForWidth())
        self.parse_source_14.setSizePolicy(sizePolicy1)
        self.parse_source_14.setMinimumSize(QSize(30, 25))
        self.parse_source_14.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse14.addWidget(self.parse_source_14)

        self.label_147 = QLabel(self.scrollAreaWidgetContents)
        self.label_147.setObjectName(u"label_147")
        sizePolicy2.setHeightForWidth(self.label_147.sizePolicy().hasHeightForWidth())
        self.label_147.setSizePolicy(sizePolicy2)
        self.label_147.setMinimumSize(QSize(40, 25))

        self.hl_parse14.addWidget(self.label_147)

        self.parse_filter_14 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_filter_14.setObjectName(u"parse_filter_14")
        sizePolicy1.setHeightForWidth(self.parse_filter_14.sizePolicy().hasHeightForWidth())
        self.parse_filter_14.setSizePolicy(sizePolicy1)
        self.parse_filter_14.setMinimumSize(QSize(30, 25))
        self.parse_filter_14.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse14.addWidget(self.parse_filter_14)


        self.verticalLayout_30.addLayout(self.hl_parse14)

        self.hl_parse15 = QHBoxLayout()
        self.hl_parse15.setObjectName(u"hl_parse15")
        self.label_148 = QLabel(self.scrollAreaWidgetContents)
        self.label_148.setObjectName(u"label_148")
        sizePolicy2.setHeightForWidth(self.label_148.sizePolicy().hasHeightForWidth())
        self.label_148.setSizePolicy(sizePolicy2)
        self.label_148.setMinimumSize(QSize(50, 25))

        self.hl_parse15.addWidget(self.label_148)

        self.parse_name_15 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_name_15.setObjectName(u"parse_name_15")
        sizePolicy1.setHeightForWidth(self.parse_name_15.sizePolicy().hasHeightForWidth())
        self.parse_name_15.setSizePolicy(sizePolicy1)
        self.parse_name_15.setMinimumSize(QSize(30, 25))
        self.parse_name_15.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse15.addWidget(self.parse_name_15)

        self.label_149 = QLabel(self.scrollAreaWidgetContents)
        self.label_149.setObjectName(u"label_149")
        sizePolicy2.setHeightForWidth(self.label_149.sizePolicy().hasHeightForWidth())
        self.label_149.setSizePolicy(sizePolicy2)
        self.label_149.setMinimumSize(QSize(50, 25))

        self.hl_parse15.addWidget(self.label_149)

        self.parse_pattern_15 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_pattern_15.setObjectName(u"parse_pattern_15")
        sizePolicy1.setHeightForWidth(self.parse_pattern_15.sizePolicy().hasHeightForWidth())
        self.parse_pattern_15.setSizePolicy(sizePolicy1)
        self.parse_pattern_15.setMinimumSize(QSize(100, 25))

        self.hl_parse15.addWidget(self.parse_pattern_15)

        self.label_150 = QLabel(self.scrollAreaWidgetContents)
        self.label_150.setObjectName(u"label_150")
        sizePolicy2.setHeightForWidth(self.label_150.sizePolicy().hasHeightForWidth())
        self.label_150.setSizePolicy(sizePolicy2)
        self.label_150.setMinimumSize(QSize(50, 25))

        self.hl_parse15.addWidget(self.label_150)

        self.parse_repl_15 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_repl_15.setObjectName(u"parse_repl_15")
        sizePolicy1.setHeightForWidth(self.parse_repl_15.sizePolicy().hasHeightForWidth())
        self.parse_repl_15.setSizePolicy(sizePolicy1)
        self.parse_repl_15.setMinimumSize(QSize(80, 25))
        self.parse_repl_15.setMaximumSize(QSize(1600, 16777215))

        self.hl_parse15.addWidget(self.parse_repl_15)

        self.label_151 = QLabel(self.scrollAreaWidgetContents)
        self.label_151.setObjectName(u"label_151")
        sizePolicy2.setHeightForWidth(self.label_151.sizePolicy().hasHeightForWidth())
        self.label_151.setSizePolicy(sizePolicy2)
        self.label_151.setMinimumSize(QSize(50, 25))

        self.hl_parse15.addWidget(self.label_151)

        self.parse_source_15 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_source_15.setObjectName(u"parse_source_15")
        sizePolicy1.setHeightForWidth(self.parse_source_15.sizePolicy().hasHeightForWidth())
        self.parse_source_15.setSizePolicy(sizePolicy1)
        self.parse_source_15.setMinimumSize(QSize(30, 25))
        self.parse_source_15.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse15.addWidget(self.parse_source_15)

        self.label_152 = QLabel(self.scrollAreaWidgetContents)
        self.label_152.setObjectName(u"label_152")
        sizePolicy2.setHeightForWidth(self.label_152.sizePolicy().hasHeightForWidth())
        self.label_152.setSizePolicy(sizePolicy2)
        self.label_152.setMinimumSize(QSize(40, 25))

        self.hl_parse15.addWidget(self.label_152)

        self.parse_filter_15 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_filter_15.setObjectName(u"parse_filter_15")
        sizePolicy1.setHeightForWidth(self.parse_filter_15.sizePolicy().hasHeightForWidth())
        self.parse_filter_15.setSizePolicy(sizePolicy1)
        self.parse_filter_15.setMinimumSize(QSize(30, 25))
        self.parse_filter_15.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse15.addWidget(self.parse_filter_15)


        self.verticalLayout_30.addLayout(self.hl_parse15)

        self.hl_parse16 = QHBoxLayout()
        self.hl_parse16.setObjectName(u"hl_parse16")
        self.label_153 = QLabel(self.scrollAreaWidgetContents)
        self.label_153.setObjectName(u"label_153")
        sizePolicy2.setHeightForWidth(self.label_153.sizePolicy().hasHeightForWidth())
        self.label_153.setSizePolicy(sizePolicy2)
        self.label_153.setMinimumSize(QSize(50, 25))

        self.hl_parse16.addWidget(self.label_153)

        self.parse_name_16 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_name_16.setObjectName(u"parse_name_16")
        sizePolicy1.setHeightForWidth(self.parse_name_16.sizePolicy().hasHeightForWidth())
        self.parse_name_16.setSizePolicy(sizePolicy1)
        self.parse_name_16.setMinimumSize(QSize(30, 25))
        self.parse_name_16.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse16.addWidget(self.parse_name_16)

        self.label_154 = QLabel(self.scrollAreaWidgetContents)
        self.label_154.setObjectName(u"label_154")
        sizePolicy2.setHeightForWidth(self.label_154.sizePolicy().hasHeightForWidth())
        self.label_154.setSizePolicy(sizePolicy2)
        self.label_154.setMinimumSize(QSize(50, 25))

        self.hl_parse16.addWidget(self.label_154)

        self.parse_pattern_16 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_pattern_16.setObjectName(u"parse_pattern_16")
        sizePolicy1.setHeightForWidth(self.parse_pattern_16.sizePolicy().hasHeightForWidth())
        self.parse_pattern_16.setSizePolicy(sizePolicy1)
        self.parse_pattern_16.setMinimumSize(QSize(100, 25))

        self.hl_parse16.addWidget(self.parse_pattern_16)

        self.label_155 = QLabel(self.scrollAreaWidgetContents)
        self.label_155.setObjectName(u"label_155")
        sizePolicy2.setHeightForWidth(self.label_155.sizePolicy().hasHeightForWidth())
        self.label_155.setSizePolicy(sizePolicy2)
        self.label_155.setMinimumSize(QSize(50, 25))

        self.hl_parse16.addWidget(self.label_155)

        self.parse_repl_16 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_repl_16.setObjectName(u"parse_repl_16")
        sizePolicy1.setHeightForWidth(self.parse_repl_16.sizePolicy().hasHeightForWidth())
        self.parse_repl_16.setSizePolicy(sizePolicy1)
        self.parse_repl_16.setMinimumSize(QSize(80, 25))
        self.parse_repl_16.setMaximumSize(QSize(1600, 16777215))

        self.hl_parse16.addWidget(self.parse_repl_16)

        self.label_156 = QLabel(self.scrollAreaWidgetContents)
        self.label_156.setObjectName(u"label_156")
        sizePolicy2.setHeightForWidth(self.label_156.sizePolicy().hasHeightForWidth())
        self.label_156.setSizePolicy(sizePolicy2)
        self.label_156.setMinimumSize(QSize(50, 25))

        self.hl_parse16.addWidget(self.label_156)

        self.parse_source_16 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_source_16.setObjectName(u"parse_source_16")
        sizePolicy1.setHeightForWidth(self.parse_source_16.sizePolicy().hasHeightForWidth())
        self.parse_source_16.setSizePolicy(sizePolicy1)
        self.parse_source_16.setMinimumSize(QSize(30, 25))
        self.parse_source_16.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse16.addWidget(self.parse_source_16)

        self.label_157 = QLabel(self.scrollAreaWidgetContents)
        self.label_157.setObjectName(u"label_157")
        sizePolicy2.setHeightForWidth(self.label_157.sizePolicy().hasHeightForWidth())
        self.label_157.setSizePolicy(sizePolicy2)
        self.label_157.setMinimumSize(QSize(40, 25))

        self.hl_parse16.addWidget(self.label_157)

        self.parse_filter_16 = QLineEdit(self.scrollAreaWidgetContents)
        self.parse_filter_16.setObjectName(u"parse_filter_16")
        sizePolicy1.setHeightForWidth(self.parse_filter_16.sizePolicy().hasHeightForWidth())
        self.parse_filter_16.setSizePolicy(sizePolicy1)
        self.parse_filter_16.setMinimumSize(QSize(30, 25))
        self.parse_filter_16.setMaximumSize(QSize(16000, 16777215))

        self.hl_parse16.addWidget(self.parse_filter_16)


        self.verticalLayout_30.addLayout(self.hl_parse16)


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
        self.tab_11 = QWidget()
        self.tab_11.setObjectName(u"tab_11")
        self.horizontalLayout_81 = QHBoxLayout(self.tab_11)
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.verticalLayout_38 = QVBoxLayout()
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.ftrack_use = QCheckBox(self.tab_11)
        self.ftrack_use.setObjectName(u"ftrack_use")
        self.ftrack_use.setMinimumSize(QSize(120, 25))
        self.ftrack_use.setChecked(True)

        self.verticalLayout_38.addWidget(self.ftrack_use)

        self.horizontalLayout_80 = QHBoxLayout()
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.label_161 = QLabel(self.tab_11)
        self.label_161.setObjectName(u"label_161")
        sizePolicy2.setHeightForWidth(self.label_161.sizePolicy().hasHeightForWidth())
        self.label_161.setSizePolicy(sizePolicy2)
        self.label_161.setMinimumSize(QSize(80, 25))

        self.horizontalLayout_80.addWidget(self.label_161)

        self.ftrack_include = QLineEdit(self.tab_11)
        self.ftrack_include.setObjectName(u"ftrack_include")
        sizePolicy2.setHeightForWidth(self.ftrack_include.sizePolicy().hasHeightForWidth())
        self.ftrack_include.setSizePolicy(sizePolicy2)
        self.ftrack_include.setMinimumSize(QSize(200, 25))

        self.horizontalLayout_80.addWidget(self.ftrack_include)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_80.addItem(self.horizontalSpacer_25)


        self.verticalLayout_38.addLayout(self.horizontalLayout_80)

        self.horizontalLayout_76 = QHBoxLayout()
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.label_90 = QLabel(self.tab_11)
        self.label_90.setObjectName(u"label_90")
        sizePolicy2.setHeightForWidth(self.label_90.sizePolicy().hasHeightForWidth())
        self.label_90.setSizePolicy(sizePolicy2)
        self.label_90.setMinimumSize(QSize(80, 25))

        self.horizontalLayout_76.addWidget(self.label_90)

        self.ftrack_project = QLineEdit(self.tab_11)
        self.ftrack_project.setObjectName(u"ftrack_project")
        sizePolicy2.setHeightForWidth(self.ftrack_project.sizePolicy().hasHeightForWidth())
        self.ftrack_project.setSizePolicy(sizePolicy2)
        self.ftrack_project.setMinimumSize(QSize(200, 25))

        self.horizontalLayout_76.addWidget(self.ftrack_project)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_76.addItem(self.horizontalSpacer_10)


        self.verticalLayout_38.addLayout(self.horizontalLayout_76)

        self.horizontalLayout_75 = QHBoxLayout()
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.label_158 = QLabel(self.tab_11)
        self.label_158.setObjectName(u"label_158")
        sizePolicy2.setHeightForWidth(self.label_158.sizePolicy().hasHeightForWidth())
        self.label_158.setSizePolicy(sizePolicy2)
        self.label_158.setMinimumSize(QSize(80, 25))

        self.horizontalLayout_75.addWidget(self.label_158)

        self.ftrack_shot = QLineEdit(self.tab_11)
        self.ftrack_shot.setObjectName(u"ftrack_shot")
        sizePolicy2.setHeightForWidth(self.ftrack_shot.sizePolicy().hasHeightForWidth())
        self.ftrack_shot.setSizePolicy(sizePolicy2)
        self.ftrack_shot.setMinimumSize(QSize(200, 25))

        self.horizontalLayout_75.addWidget(self.ftrack_shot)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_75.addItem(self.horizontalSpacer_16)


        self.verticalLayout_38.addLayout(self.horizontalLayout_75)

        self.horizontalLayout_73 = QHBoxLayout()
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.label_159 = QLabel(self.tab_11)
        self.label_159.setObjectName(u"label_159")
        sizePolicy2.setHeightForWidth(self.label_159.sizePolicy().hasHeightForWidth())
        self.label_159.setSizePolicy(sizePolicy2)
        self.label_159.setMinimumSize(QSize(80, 25))

        self.horizontalLayout_73.addWidget(self.label_159)

        self.ftrack_task = QLineEdit(self.tab_11)
        self.ftrack_task.setObjectName(u"ftrack_task")
        sizePolicy2.setHeightForWidth(self.ftrack_task.sizePolicy().hasHeightForWidth())
        self.ftrack_task.setSizePolicy(sizePolicy2)
        self.ftrack_task.setMinimumSize(QSize(200, 25))

        self.horizontalLayout_73.addWidget(self.ftrack_task)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_73.addItem(self.horizontalSpacer_18)


        self.verticalLayout_38.addLayout(self.horizontalLayout_73)

        self.horizontalLayout_77 = QHBoxLayout()
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.ftrack_label_use = QCheckBox(self.tab_11)
        self.ftrack_label_use.setObjectName(u"ftrack_label_use")
        self.ftrack_label_use.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.ftrack_label_use.sizePolicy().hasHeightForWidth())
        self.ftrack_label_use.setSizePolicy(sizePolicy2)
        self.ftrack_label_use.setMinimumSize(QSize(80, 25))
        self.ftrack_label_use.setCheckable(True)

        self.horizontalLayout_77.addWidget(self.ftrack_label_use)

        self.ftrack_label = QLineEdit(self.tab_11)
        self.ftrack_label.setObjectName(u"ftrack_label")
        self.ftrack_label.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.ftrack_label.sizePolicy().hasHeightForWidth())
        self.ftrack_label.setSizePolicy(sizePolicy2)
        self.ftrack_label.setMinimumSize(QSize(200, 25))

        self.horizontalLayout_77.addWidget(self.ftrack_label)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_77.addItem(self.horizontalSpacer_20)


        self.verticalLayout_38.addLayout(self.horizontalLayout_77)

        self.horizontalLayout_79 = QHBoxLayout()
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.ftrack_version_use = QCheckBox(self.tab_11)
        self.ftrack_version_use.setObjectName(u"ftrack_version_use")
        sizePolicy2.setHeightForWidth(self.ftrack_version_use.sizePolicy().hasHeightForWidth())
        self.ftrack_version_use.setSizePolicy(sizePolicy2)
        self.ftrack_version_use.setMinimumSize(QSize(80, 25))

        self.horizontalLayout_79.addWidget(self.ftrack_version_use)

        self.ftrack_version = QLineEdit(self.tab_11)
        self.ftrack_version.setObjectName(u"ftrack_version")
        sizePolicy2.setHeightForWidth(self.ftrack_version.sizePolicy().hasHeightForWidth())
        self.ftrack_version.setSizePolicy(sizePolicy2)
        self.ftrack_version.setMinimumSize(QSize(200, 25))

        self.horizontalLayout_79.addWidget(self.ftrack_version)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_79.addItem(self.horizontalSpacer_24)


        self.verticalLayout_38.addLayout(self.horizontalLayout_79)

        self.horizontalLayout_72 = QHBoxLayout()
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.label_91 = QLabel(self.tab_11)
        self.label_91.setObjectName(u"label_91")
        sizePolicy2.setHeightForWidth(self.label_91.sizePolicy().hasHeightForWidth())
        self.label_91.setSizePolicy(sizePolicy2)
        self.label_91.setMinimumSize(QSize(80, 25))

        self.horizontalLayout_72.addWidget(self.label_91)

        self.ftrack_note_pattern = QLineEdit(self.tab_11)
        self.ftrack_note_pattern.setObjectName(u"ftrack_note_pattern")
        sizePolicy2.setHeightForWidth(self.ftrack_note_pattern.sizePolicy().hasHeightForWidth())
        self.ftrack_note_pattern.setSizePolicy(sizePolicy2)
        self.ftrack_note_pattern.setMinimumSize(QSize(200, 25))

        self.horizontalLayout_72.addWidget(self.ftrack_note_pattern)

        self.label_160 = QLabel(self.tab_11)
        self.label_160.setObjectName(u"label_160")
        sizePolicy2.setHeightForWidth(self.label_160.sizePolicy().hasHeightForWidth())
        self.label_160.setSizePolicy(sizePolicy2)
        self.label_160.setMinimumSize(QSize(70, 25))

        self.horizontalLayout_72.addWidget(self.label_160)

        self.ftrack_note_repl = QLineEdit(self.tab_11)
        self.ftrack_note_repl.setObjectName(u"ftrack_note_repl")
        sizePolicy2.setHeightForWidth(self.ftrack_note_repl.sizePolicy().hasHeightForWidth())
        self.ftrack_note_repl.setSizePolicy(sizePolicy2)
        self.ftrack_note_repl.setMinimumSize(QSize(200, 25))

        self.horizontalLayout_72.addWidget(self.ftrack_note_repl)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_72.addItem(self.horizontalSpacer_21)


        self.verticalLayout_38.addLayout(self.horizontalLayout_72)

        self.verticalSpacer_6 = QSpacerItem(20, 17, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_38.addItem(self.verticalSpacer_6)


        self.horizontalLayout_81.addLayout(self.verticalLayout_38)

        self.TopTab.addTab(self.tab_11, "")
        self.tab_16 = QWidget()
        self.tab_16.setObjectName(u"tab_16")
        self.horizontalLayout_129 = QHBoxLayout(self.tab_16)
        self.horizontalLayout_129.setObjectName(u"horizontalLayout_129")
        self.verticalLayout_55 = QVBoxLayout()
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.groupBox_11 = QGroupBox(self.tab_16)
        self.groupBox_11.setObjectName(u"groupBox_11")
        sizePolicy1.setHeightForWidth(self.groupBox_11.sizePolicy().hasHeightForWidth())
        self.groupBox_11.setSizePolicy(sizePolicy1)
        self.groupBox_11.setMinimumSize(QSize(600, 60))
        self.groupBox_11.setMaximumSize(QSize(16777215, 60))
        self.groupBox_11.setBaseSize(QSize(631, 70))
        self.groupBox_11.setFlat(False)
        self.verticalLayout_54 = QVBoxLayout(self.groupBox_11)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.horizontalLayout_122 = QHBoxLayout()
        self.horizontalLayout_122.setObjectName(u"horizontalLayout_122")
        self.vendor_csv_path_detect = QCheckBox(self.groupBox_11)
        self.vendor_csv_path_detect.setObjectName(u"vendor_csv_path_detect")
        self.vendor_csv_path_detect.setMinimumSize(QSize(100, 25))
        self.vendor_csv_path_detect.setMaximumSize(QSize(100, 25))
        self.vendor_csv_path_detect.setChecked(False)

        self.horizontalLayout_122.addWidget(self.vendor_csv_path_detect)

        self.vendor_csv_path = QLineEdit(self.groupBox_11)
        self.vendor_csv_path.setObjectName(u"vendor_csv_path")
        sizePolicy1.setHeightForWidth(self.vendor_csv_path.sizePolicy().hasHeightForWidth())
        self.vendor_csv_path.setSizePolicy(sizePolicy1)
        self.vendor_csv_path.setMinimumSize(QSize(250, 25))
        self.vendor_csv_path.setMaximumSize(QSize(16000, 16777215))
        self.vendor_csv_path.setDragEnabled(True)

        self.horizontalLayout_122.addWidget(self.vendor_csv_path)

        self.horizontalLayout_123 = QHBoxLayout()
        self.horizontalLayout_123.setObjectName(u"horizontalLayout_123")
        self.vendor_csv_explore = QPushButton(self.groupBox_11)
        self.vendor_csv_explore.setObjectName(u"vendor_csv_explore")
        sizePolicy2.setHeightForWidth(self.vendor_csv_explore.sizePolicy().hasHeightForWidth())
        self.vendor_csv_explore.setSizePolicy(sizePolicy2)
        self.vendor_csv_explore.setMinimumSize(QSize(20, 25))
        self.vendor_csv_explore.setAutoFillBackground(False)
        self.vendor_csv_explore.setIcon(icon1)
        self.vendor_csv_explore.setFlat(True)

        self.horizontalLayout_123.addWidget(self.vendor_csv_explore)

        self.vendor_csv_browse = QPushButton(self.groupBox_11)
        self.vendor_csv_browse.setObjectName(u"vendor_csv_browse")
        sizePolicy2.setHeightForWidth(self.vendor_csv_browse.sizePolicy().hasHeightForWidth())
        self.vendor_csv_browse.setSizePolicy(sizePolicy2)
        self.vendor_csv_browse.setMinimumSize(QSize(60, 25))
        self.vendor_csv_browse.setMaximumSize(QSize(60, 24))
        self.vendor_csv_browse.setAutoFillBackground(False)
        self.vendor_csv_browse.setIcon(icon)
        self.vendor_csv_browse.setFlat(True)

        self.horizontalLayout_123.addWidget(self.vendor_csv_browse)


        self.horizontalLayout_122.addLayout(self.horizontalLayout_123)


        self.verticalLayout_54.addLayout(self.horizontalLayout_122)


        self.verticalLayout_55.addWidget(self.groupBox_11)

        self.groupBox_12 = QGroupBox(self.tab_16)
        self.groupBox_12.setObjectName(u"groupBox_12")
        sizePolicy5 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.groupBox_12.sizePolicy().hasHeightForWidth())
        self.groupBox_12.setSizePolicy(sizePolicy5)
        self.horizontalLayout_127 = QHBoxLayout(self.groupBox_12)
        self.horizontalLayout_127.setObjectName(u"horizontalLayout_127")
        self.horizontalLayout_126 = QHBoxLayout()
        self.horizontalLayout_126.setObjectName(u"horizontalLayout_126")
        self.horizontalLayout_124 = QHBoxLayout()
        self.horizontalLayout_124.setObjectName(u"horizontalLayout_124")
        self.label_163 = QLabel(self.groupBox_12)
        self.label_163.setObjectName(u"label_163")
        sizePolicy2.setHeightForWidth(self.label_163.sizePolicy().hasHeightForWidth())
        self.label_163.setSizePolicy(sizePolicy2)
        self.label_163.setMinimumSize(QSize(90, 25))
        self.label_163.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_124.addWidget(self.label_163)

        self.vendor_csv_package_key = QLineEdit(self.groupBox_12)
        self.vendor_csv_package_key.setObjectName(u"vendor_csv_package_key")
        sizePolicy1.setHeightForWidth(self.vendor_csv_package_key.sizePolicy().hasHeightForWidth())
        self.vendor_csv_package_key.setSizePolicy(sizePolicy1)
        self.vendor_csv_package_key.setMinimumSize(QSize(300, 25))
        self.vendor_csv_package_key.setMaximumSize(QSize(150, 16777215))
        self.vendor_csv_package_key.setReadOnly(False)

        self.horizontalLayout_124.addWidget(self.vendor_csv_package_key)


        self.horizontalLayout_126.addLayout(self.horizontalLayout_124)

        self.horizontalLayout_125 = QHBoxLayout()
        self.horizontalLayout_125.setObjectName(u"horizontalLayout_125")
        self.label_164 = QLabel(self.groupBox_12)
        self.label_164.setObjectName(u"label_164")
        sizePolicy2.setHeightForWidth(self.label_164.sizePolicy().hasHeightForWidth())
        self.label_164.setSizePolicy(sizePolicy2)
        self.label_164.setMinimumSize(QSize(90, 25))
        self.label_164.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_125.addWidget(self.label_164)

        self.vendor_csv_vendor_key = QLineEdit(self.groupBox_12)
        self.vendor_csv_vendor_key.setObjectName(u"vendor_csv_vendor_key")
        sizePolicy1.setHeightForWidth(self.vendor_csv_vendor_key.sizePolicy().hasHeightForWidth())
        self.vendor_csv_vendor_key.setSizePolicy(sizePolicy1)
        self.vendor_csv_vendor_key.setMinimumSize(QSize(300, 25))
        self.vendor_csv_vendor_key.setMaximumSize(QSize(150, 16777215))
        self.vendor_csv_vendor_key.setReadOnly(False)

        self.horizontalLayout_125.addWidget(self.vendor_csv_vendor_key)


        self.horizontalLayout_126.addLayout(self.horizontalLayout_125)


        self.horizontalLayout_127.addLayout(self.horizontalLayout_126)


        self.verticalLayout_55.addWidget(self.groupBox_12)

        self.horizontalLayout_128 = QHBoxLayout()
        self.horizontalLayout_128.setObjectName(u"horizontalLayout_128")
        self.verticalLayout_56 = QVBoxLayout()
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.label_30 = QLabel(self.tab_16)
        self.label_30.setObjectName(u"label_30")
        sizePolicy2.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy2)
        self.label_30.setMinimumSize(QSize(150, 20))
        self.label_30.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_56.addWidget(self.label_30)

        self.vendor_csv_prefs_spreadsheet = QPlainTextEdit(self.tab_16)
        self.vendor_csv_prefs_spreadsheet.setObjectName(u"vendor_csv_prefs_spreadsheet")
        sizePolicy6 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.vendor_csv_prefs_spreadsheet.sizePolicy().hasHeightForWidth())
        self.vendor_csv_prefs_spreadsheet.setSizePolicy(sizePolicy6)
        self.vendor_csv_prefs_spreadsheet.setMinimumSize(QSize(150, 100))
        self.vendor_csv_prefs_spreadsheet.setMaximumSize(QSize(16777215, 400))

        self.verticalLayout_56.addWidget(self.vendor_csv_prefs_spreadsheet)


        self.horizontalLayout_128.addLayout(self.verticalLayout_56)

        self.verticalLayout_57 = QVBoxLayout()
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.label_31 = QLabel(self.tab_16)
        self.label_31.setObjectName(u"label_31")
        sizePolicy2.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy2)
        self.label_31.setMinimumSize(QSize(150, 20))
        self.label_31.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_57.addWidget(self.label_31)

        self.vendor_csv_prefs_repres = QPlainTextEdit(self.tab_16)
        self.vendor_csv_prefs_repres.setObjectName(u"vendor_csv_prefs_repres")
        sizePolicy6.setHeightForWidth(self.vendor_csv_prefs_repres.sizePolicy().hasHeightForWidth())
        self.vendor_csv_prefs_repres.setSizePolicy(sizePolicy6)
        self.vendor_csv_prefs_repres.setMinimumSize(QSize(150, 100))
        self.vendor_csv_prefs_repres.setMaximumSize(QSize(16777215, 400))

        self.verticalLayout_57.addWidget(self.vendor_csv_prefs_repres)


        self.horizontalLayout_128.addLayout(self.verticalLayout_57)


        self.verticalLayout_55.addLayout(self.horizontalLayout_128)


        self.horizontalLayout_129.addLayout(self.verticalLayout_55)

        self.TopTab.addTab(self.tab_16, "")
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
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 819, 269))
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.scrollAreaWidgetContents_3.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_3.setSizePolicy(sizePolicy7)
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
        sizePolicy6.setHeightForWidth(self.sub_columns.sizePolicy().hasHeightForWidth())
        self.sub_columns.setSizePolicy(sizePolicy6)
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
        sizePolicy6.setHeightForWidth(self.log_columns.sizePolicy().hasHeightForWidth())
        self.log_columns.setSizePolicy(sizePolicy6)
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
        sizePolicy6.setHeightForWidth(self.txt_columns.sizePolicy().hasHeightForWidth())
        self.txt_columns.setSizePolicy(sizePolicy6)
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
        self.tab_12 = QWidget()
        self.tab_12.setObjectName(u"tab_12")
        self.horizontalLayout_68 = QHBoxLayout(self.tab_12)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.verticalLayout_48 = QVBoxLayout()
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.horizontalLayout_64 = QHBoxLayout()
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.check_sequence_size_consistency = QCheckBox(self.tab_12)
        self.check_sequence_size_consistency.setObjectName(u"check_sequence_size_consistency")
        self.check_sequence_size_consistency.setMinimumSize(QSize(220, 25))

        self.horizontalLayout_64.addWidget(self.check_sequence_size_consistency)

        self.check_sequence_holes = QCheckBox(self.tab_12)
        self.check_sequence_holes.setObjectName(u"check_sequence_holes")
        self.check_sequence_holes.setMinimumSize(QSize(220, 25))

        self.horizontalLayout_64.addWidget(self.check_sequence_holes)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_64.addItem(self.horizontalSpacer)


        self.verticalLayout_48.addLayout(self.horizontalLayout_64)

        self.scrollArea_3 = QScrollArea(self.tab_12)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setMinimumSize(QSize(0, 200))
        self.scrollArea_3.setMaximumSize(QSize(16777215, 500))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 812, 302))
        self.verticalLayout_39 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_36 = QVBoxLayout()
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.groupBox_13 = QGroupBox(self.scrollAreaWidgetContents_4)
        self.groupBox_13.setObjectName(u"groupBox_13")
        sizePolicy1.setHeightForWidth(self.groupBox_13.sizePolicy().hasHeightForWidth())
        self.groupBox_13.setSizePolicy(sizePolicy1)
        self.groupBox_13.setMinimumSize(QSize(600, 90))
        self.groupBox_13.setMaximumSize(QSize(16777215, 90))
        self.horizontalLayout_115 = QHBoxLayout(self.groupBox_13)
        self.horizontalLayout_115.setObjectName(u"horizontalLayout_115")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_56 = QHBoxLayout()
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_24 = QLabel(self.groupBox_13)
        self.label_24.setObjectName(u"label_24")
        sizePolicy2.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy2)
        self.label_24.setMinimumSize(QSize(15, 25))

        self.horizontalLayout_2.addWidget(self.label_24)

        self.check_if_1 = QLineEdit(self.groupBox_13)
        self.check_if_1.setObjectName(u"check_if_1")
        sizePolicy1.setHeightForWidth(self.check_if_1.sizePolicy().hasHeightForWidth())
        self.check_if_1.setSizePolicy(sizePolicy1)
        self.check_if_1.setMinimumSize(QSize(160, 25))

        self.horizontalLayout_2.addWidget(self.check_if_1)


        self.horizontalLayout_56.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_53 = QHBoxLayout()
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.label_23 = QLabel(self.groupBox_13)
        self.label_23.setObjectName(u"label_23")
        sizePolicy2.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy2)
        self.label_23.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_53.addWidget(self.label_23)

        self.check_check_1 = QLineEdit(self.groupBox_13)
        self.check_check_1.setObjectName(u"check_check_1")
        sizePolicy1.setHeightForWidth(self.check_check_1.sizePolicy().hasHeightForWidth())
        self.check_check_1.setSizePolicy(sizePolicy1)
        self.check_check_1.setMinimumSize(QSize(160, 25))

        self.horizontalLayout_53.addWidget(self.check_check_1)


        self.horizontalLayout_56.addLayout(self.horizontalLayout_53)


        self.verticalLayout_3.addLayout(self.horizontalLayout_56)

        self.horizontalLayout_55 = QHBoxLayout()
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_54 = QHBoxLayout()
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.check_warning_1 = QRadioButton(self.groupBox_13)
        self.check_warning_1.setObjectName(u"check_warning_1")
        self.check_warning_1.setMinimumSize(QSize(100, 25))

        self.horizontalLayout_54.addWidget(self.check_warning_1)

        self.check_error_1 = QRadioButton(self.groupBox_13)
        self.check_error_1.setObjectName(u"check_error_1")
        self.check_error_1.setMinimumSize(QSize(100, 25))
        self.check_error_1.setChecked(True)

        self.horizontalLayout_54.addWidget(self.check_error_1)


        self.horizontalLayout_55.addLayout(self.horizontalLayout_54)

        self.check_message_1 = QLineEdit(self.groupBox_13)
        self.check_message_1.setObjectName(u"check_message_1")
        sizePolicy1.setHeightForWidth(self.check_message_1.sizePolicy().hasHeightForWidth())
        self.check_message_1.setSizePolicy(sizePolicy1)
        self.check_message_1.setMinimumSize(QSize(170, 25))

        self.horizontalLayout_55.addWidget(self.check_message_1)


        self.verticalLayout_3.addLayout(self.horizontalLayout_55)


        self.horizontalLayout_115.addLayout(self.verticalLayout_3)


        self.verticalLayout_36.addWidget(self.groupBox_13)

        self.groupBox_16 = QGroupBox(self.scrollAreaWidgetContents_4)
        self.groupBox_16.setObjectName(u"groupBox_16")
        sizePolicy1.setHeightForWidth(self.groupBox_16.sizePolicy().hasHeightForWidth())
        self.groupBox_16.setSizePolicy(sizePolicy1)
        self.groupBox_16.setMinimumSize(QSize(600, 90))
        self.groupBox_16.setMaximumSize(QSize(16777215, 90))
        self.horizontalLayout_116 = QHBoxLayout(self.groupBox_16)
        self.horizontalLayout_116.setObjectName(u"horizontalLayout_116")
        self.verticalLayout_34 = QVBoxLayout()
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.horizontalLayout_57 = QHBoxLayout()
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_58 = QHBoxLayout()
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.label_25 = QLabel(self.groupBox_16)
        self.label_25.setObjectName(u"label_25")
        sizePolicy2.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy2)
        self.label_25.setMinimumSize(QSize(15, 25))

        self.horizontalLayout_58.addWidget(self.label_25)

        self.check_if_2 = QLineEdit(self.groupBox_16)
        self.check_if_2.setObjectName(u"check_if_2")
        sizePolicy1.setHeightForWidth(self.check_if_2.sizePolicy().hasHeightForWidth())
        self.check_if_2.setSizePolicy(sizePolicy1)
        self.check_if_2.setMinimumSize(QSize(160, 25))

        self.horizontalLayout_58.addWidget(self.check_if_2)


        self.horizontalLayout_57.addLayout(self.horizontalLayout_58)

        self.horizontalLayout_59 = QHBoxLayout()
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.label_26 = QLabel(self.groupBox_16)
        self.label_26.setObjectName(u"label_26")
        sizePolicy2.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy2)
        self.label_26.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_59.addWidget(self.label_26)

        self.check_check_2 = QLineEdit(self.groupBox_16)
        self.check_check_2.setObjectName(u"check_check_2")
        sizePolicy1.setHeightForWidth(self.check_check_2.sizePolicy().hasHeightForWidth())
        self.check_check_2.setSizePolicy(sizePolicy1)
        self.check_check_2.setMinimumSize(QSize(160, 25))

        self.horizontalLayout_59.addWidget(self.check_check_2)


        self.horizontalLayout_57.addLayout(self.horizontalLayout_59)


        self.verticalLayout_34.addLayout(self.horizontalLayout_57)

        self.horizontalLayout_60 = QHBoxLayout()
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_65 = QHBoxLayout()
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.check_warning_2 = QRadioButton(self.groupBox_16)
        self.check_warning_2.setObjectName(u"check_warning_2")
        self.check_warning_2.setMinimumSize(QSize(100, 25))

        self.horizontalLayout_65.addWidget(self.check_warning_2)

        self.check_error_2 = QRadioButton(self.groupBox_16)
        self.check_error_2.setObjectName(u"check_error_2")
        self.check_error_2.setMinimumSize(QSize(100, 25))

        self.horizontalLayout_65.addWidget(self.check_error_2)


        self.horizontalLayout_60.addLayout(self.horizontalLayout_65)

        self.check_message_2 = QLineEdit(self.groupBox_16)
        self.check_message_2.setObjectName(u"check_message_2")
        sizePolicy1.setHeightForWidth(self.check_message_2.sizePolicy().hasHeightForWidth())
        self.check_message_2.setSizePolicy(sizePolicy1)
        self.check_message_2.setMinimumSize(QSize(170, 25))

        self.horizontalLayout_60.addWidget(self.check_message_2)


        self.verticalLayout_34.addLayout(self.horizontalLayout_60)


        self.horizontalLayout_116.addLayout(self.verticalLayout_34)


        self.verticalLayout_36.addWidget(self.groupBox_16)

        self.groupBox_18 = QGroupBox(self.scrollAreaWidgetContents_4)
        self.groupBox_18.setObjectName(u"groupBox_18")
        sizePolicy1.setHeightForWidth(self.groupBox_18.sizePolicy().hasHeightForWidth())
        self.groupBox_18.setSizePolicy(sizePolicy1)
        self.groupBox_18.setMinimumSize(QSize(600, 90))
        self.groupBox_18.setMaximumSize(QSize(16777215, 90))
        self.horizontalLayout_117 = QHBoxLayout(self.groupBox_18)
        self.horizontalLayout_117.setObjectName(u"horizontalLayout_117")
        self.verticalLayout_35 = QVBoxLayout()
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.horizontalLayout_66 = QHBoxLayout()
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_67 = QHBoxLayout()
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.label_27 = QLabel(self.groupBox_18)
        self.label_27.setObjectName(u"label_27")
        sizePolicy2.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy2)
        self.label_27.setMinimumSize(QSize(15, 25))

        self.horizontalLayout_67.addWidget(self.label_27)

        self.check_if_3 = QLineEdit(self.groupBox_18)
        self.check_if_3.setObjectName(u"check_if_3")
        sizePolicy1.setHeightForWidth(self.check_if_3.sizePolicy().hasHeightForWidth())
        self.check_if_3.setSizePolicy(sizePolicy1)
        self.check_if_3.setMinimumSize(QSize(160, 25))

        self.horizontalLayout_67.addWidget(self.check_if_3)


        self.horizontalLayout_66.addLayout(self.horizontalLayout_67)

        self.horizontalLayout_112 = QHBoxLayout()
        self.horizontalLayout_112.setObjectName(u"horizontalLayout_112")
        self.label_28 = QLabel(self.groupBox_18)
        self.label_28.setObjectName(u"label_28")
        sizePolicy2.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy2)
        self.label_28.setMinimumSize(QSize(50, 25))

        self.horizontalLayout_112.addWidget(self.label_28)

        self.check_check_3 = QLineEdit(self.groupBox_18)
        self.check_check_3.setObjectName(u"check_check_3")
        sizePolicy1.setHeightForWidth(self.check_check_3.sizePolicy().hasHeightForWidth())
        self.check_check_3.setSizePolicy(sizePolicy1)
        self.check_check_3.setMinimumSize(QSize(160, 25))

        self.horizontalLayout_112.addWidget(self.check_check_3)


        self.horizontalLayout_66.addLayout(self.horizontalLayout_112)


        self.verticalLayout_35.addLayout(self.horizontalLayout_66)

        self.horizontalLayout_113 = QHBoxLayout()
        self.horizontalLayout_113.setObjectName(u"horizontalLayout_113")
        self.horizontalLayout_114 = QHBoxLayout()
        self.horizontalLayout_114.setObjectName(u"horizontalLayout_114")
        self.check_warning_3 = QRadioButton(self.groupBox_18)
        self.check_warning_3.setObjectName(u"check_warning_3")
        self.check_warning_3.setMinimumSize(QSize(100, 25))

        self.horizontalLayout_114.addWidget(self.check_warning_3)

        self.check_error_3 = QRadioButton(self.groupBox_18)
        self.check_error_3.setObjectName(u"check_error_3")
        self.check_error_3.setMinimumSize(QSize(100, 25))
        self.check_error_3.setChecked(True)

        self.horizontalLayout_114.addWidget(self.check_error_3)


        self.horizontalLayout_113.addLayout(self.horizontalLayout_114)

        self.check_message_3 = QLineEdit(self.groupBox_18)
        self.check_message_3.setObjectName(u"check_message_3")
        sizePolicy1.setHeightForWidth(self.check_message_3.sizePolicy().hasHeightForWidth())
        self.check_message_3.setSizePolicy(sizePolicy1)
        self.check_message_3.setMinimumSize(QSize(170, 25))

        self.horizontalLayout_113.addWidget(self.check_message_3)


        self.verticalLayout_35.addLayout(self.horizontalLayout_113)


        self.horizontalLayout_117.addLayout(self.verticalLayout_35)


        self.verticalLayout_36.addWidget(self.groupBox_18)


        self.verticalLayout_39.addLayout(self.verticalLayout_36)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_48.addWidget(self.scrollArea_3)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_48.addItem(self.verticalSpacer_7)


        self.horizontalLayout_68.addLayout(self.verticalLayout_48)

        self.TopTab.addTab(self.tab_12, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_47 = QVBoxLayout(self.tab_4)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_40 = QVBoxLayout()
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.groupBox_14 = QGroupBox(self.tab_4)
        self.groupBox_14.setObjectName(u"groupBox_14")
        sizePolicy8 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.groupBox_14.sizePolicy().hasHeightForWidth())
        self.groupBox_14.setSizePolicy(sizePolicy8)
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

        self.horizontalSpacer_23 = QSpacerItem(20, 25, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_23)


        self.verticalLayout_5.addLayout(self.horizontalLayout_36)


        self.verticalLayout_40.addWidget(self.groupBox_14)

        self.groupBox_15 = QGroupBox(self.tab_4)
        self.groupBox_15.setObjectName(u"groupBox_15")
        sizePolicy8.setHeightForWidth(self.groupBox_15.sizePolicy().hasHeightForWidth())
        self.groupBox_15.setSizePolicy(sizePolicy8)
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

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_12)


        self.horizontalLayout_38.addLayout(self.horizontalLayout_9)


        self.verticalLayout_11.addLayout(self.horizontalLayout_38)


        self.verticalLayout_40.addWidget(self.groupBox_15)

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
        self.label.setMinimumSize(QSize(70, 25))
        self.label.setMaximumSize(QSize(70, 25))

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
        self.label_2.setMinimumSize(QSize(50, 25))
        self.label_2.setMaximumSize(QSize(50, 25))

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

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_5)


        self.horizontalLayout_28.addLayout(self.horizontalLayout_27)


        self.horizontalLayout_70.addLayout(self.horizontalLayout_28)


        self.verticalLayout_40.addWidget(self.groupBox_2)

        self.groupBox_17 = QGroupBox(self.tab_4)
        self.groupBox_17.setObjectName(u"groupBox_17")
        sizePolicy8.setHeightForWidth(self.groupBox_17.sizePolicy().hasHeightForWidth())
        self.groupBox_17.setSizePolicy(sizePolicy8)
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
        self.label_54.setMinimumSize(QSize(125, 25))
        self.label_54.setMaximumSize(QSize(125, 25))

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

        self.horizontalSpacer_19 = QSpacerItem(18, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_19)


        self.horizontalLayout_30.addLayout(self.horizontalLayout_22)


        self.verticalLayout_40.addWidget(self.groupBox_17)

        self.groupBox_19 = QGroupBox(self.tab_4)
        self.groupBox_19.setObjectName(u"groupBox_19")
        sizePolicy8.setHeightForWidth(self.groupBox_19.sizePolicy().hasHeightForWidth())
        self.groupBox_19.setSizePolicy(sizePolicy8)
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
        self.prefs_merge_by.setMinimumSize(QSize(60, 25))
        self.prefs_merge_by.setMaximumSize(QSize(60, 25))

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
        self.prefs_merge_sort.setMinimumSize(QSize(80, 25))
        self.prefs_merge_sort.setMaximumSize(QSize(80, 25))

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

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_121.addItem(self.horizontalSpacer_2)


        self.verticalLayout_28.addLayout(self.horizontalLayout_121)


        self.verticalLayout_40.addWidget(self.groupBox_19)

        self.verticalSpacer_5 = QSpacerItem(1381, 13, QSizePolicy.Minimum, QSizePolicy.Expanding)

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
        sizePolicy9 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.export_sub_custom_path.sizePolicy().hasHeightForWidth())
        self.export_sub_custom_path.setSizePolicy(sizePolicy9)
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
        sizePolicy9.setHeightForWidth(self.export_log_custom_path.sizePolicy().hasHeightForWidth())
        self.export_log_custom_path.setSizePolicy(sizePolicy9)
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
        sizePolicy6.setHeightForWidth(self.text_header.sizePolicy().hasHeightForWidth())
        self.text_header.setSizePolicy(sizePolicy6)
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
        sizePolicy6.setHeightForWidth(self.text_footer.sizePolicy().hasHeightForWidth())
        self.text_footer.setSizePolicy(sizePolicy6)
        self.text_footer.setMinimumSize(QSize(200, 50))

        self.verticalLayout_45.addWidget(self.text_footer)


        self.horizontalLayout_8.addLayout(self.verticalLayout_45)


        self.verticalLayout_49.addLayout(self.horizontalLayout_8)


        self.horizontalLayout_32.addLayout(self.verticalLayout_49)

        self.TopTab.addTab(self.tab_5, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_37 = QVBoxLayout(self.tab_3)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.groupBox_3 = QGroupBox(self.tab_3)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy5.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy5)
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
        self.load_preset_combobox.setMinimumSize(QSize(250, 25))
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


        self.verticalLayout_12.addWidget(self.groupBox_3)

        self.groupBox_7 = QGroupBox(self.tab_3)
        self.groupBox_7.setObjectName(u"groupBox_7")
        sizePolicy5.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy5)
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
        self.save_preset_name.setMinimumSize(QSize(250, 25))

        self.horizontalLayout_33.addWidget(self.save_preset_name)

        self.save_preset_button = QPushButton(self.groupBox_7)
        self.save_preset_button.setObjectName(u"save_preset_button")
        self.save_preset_button.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.save_preset_button.sizePolicy().hasHeightForWidth())
        self.save_preset_button.setSizePolicy(sizePolicy2)
        self.save_preset_button.setMinimumSize(QSize(120, 25))

        self.horizontalLayout_33.addWidget(self.save_preset_button)


        self.verticalLayout_8.addLayout(self.horizontalLayout_33)


        self.verticalLayout_12.addWidget(self.groupBox_7)

        self.preset_explore = QPushButton(self.tab_3)
        self.preset_explore.setObjectName(u"preset_explore")
        sizePolicy1.setHeightForWidth(self.preset_explore.sizePolicy().hasHeightForWidth())
        self.preset_explore.setSizePolicy(sizePolicy1)
        self.preset_explore.setMinimumSize(QSize(250, 25))
        self.preset_explore.setIcon(icon1)

        self.verticalLayout_12.addWidget(self.preset_explore)

        self.version_231024 = QLineEdit(self.tab_3)
        self.version_231024.setObjectName(u"version_231024")
        self.version_231024.setReadOnly(True)

        self.verticalLayout_12.addWidget(self.version_231024)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_2)


        self.verticalLayout_37.addLayout(self.verticalLayout_12)

        self.TopTab.addTab(self.tab_3, "")
        self.tab_14 = QWidget()
        self.tab_14.setObjectName(u"tab_14")
        self.horizontalLayout_91 = QHBoxLayout(self.tab_14)
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.textEdit = QTextEdit(self.tab_14)
        self.textEdit.setObjectName(u"textEdit")

        self.horizontalLayout_91.addWidget(self.textEdit)

        self.TopTab.addTab(self.tab_14, "")

        self.verticalLayout_50.addWidget(self.TopTab)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.BottomTab = QTabWidget(self.centralwidget)
        self.BottomTab.setObjectName(u"BottomTab")
        sizePolicy3.setHeightForWidth(self.BottomTab.sizePolicy().hasHeightForWidth())
        self.BottomTab.setSizePolicy(sizePolicy3)
        self.BottomTab.setMinimumSize(QSize(670, 150))
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.verticalLayout_15 = QVBoxLayout(self.tab_6)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.sub_table = QTableWidget(self.tab_6)
        self.sub_table.setObjectName(u"sub_table")
        sizePolicy.setHeightForWidth(self.sub_table.sizePolicy().hasHeightForWidth())
        self.sub_table.setSizePolicy(sizePolicy)
        self.sub_table.setMinimumSize(QSize(600, 100))
        self.sub_table.setMaximumSize(QSize(16000, 16000))

        self.verticalLayout_15.addWidget(self.sub_table)

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

        self.verticalLayout_10.addWidget(self.BottomTab)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.write_button = QPushButton(self.centralwidget)
        self.write_button.setObjectName(u"write_button")
        sizePolicy1.setHeightForWidth(self.write_button.sizePolicy().hasHeightForWidth())
        self.write_button.setSizePolicy(sizePolicy1)
        self.write_button.setMinimumSize(QSize(350, 40))
        self.write_button.setBaseSize(QSize(520, 51))
        self.write_button.setAutoFillBackground(False)
        self.write_button.setStyleSheet(u"")
        self.write_button.setFlat(True)

        self.horizontalLayout_3.addWidget(self.write_button)

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


        self.verticalLayout_50.addLayout(self.verticalLayout_10)


        self.verticalLayout_51.addLayout(self.verticalLayout_50)

        submission.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(submission)
        self.statusBar.setObjectName(u"statusBar")
        sizePolicy10 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.statusBar.sizePolicy().hasHeightForWidth())
        self.statusBar.setSizePolicy(sizePolicy10)
        submission.setStatusBar(self.statusBar)

        self.retranslateUi(submission)

        self.TopTab.setCurrentIndex(10)
        self.package_explore.setDefault(True)
        self.package_browse.setDefault(True)
        self.package_explore_2.setDefault(True)
        self.package_browse_2.setDefault(True)
        self.vendor_csv_explore.setDefault(True)
        self.vendor_csv_browse.setDefault(True)
        self.BottomTab.setCurrentIndex(0)
        self.write_button.setDefault(True)
        self.reload.setDefault(True)


        QMetaObject.connectSlotsByName(submission)
    # setupUi

    def retranslateUi(self, submission):
        submission.setWindowTitle(QCoreApplication.translate("submission", u"Submission Helper", None))
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
        self.label_22.setText(QCoreApplication.translate("submission", u"Name:", None))
        self.label_38.setText(QCoreApplication.translate("submission", u"Pattern:", None))
        self.label_39.setText(QCoreApplication.translate("submission", u"Repl:", None))
        self.label_40.setText(QCoreApplication.translate("submission", u"Source:", None))
        self.label_78.setText(QCoreApplication.translate("submission", u"Filter:", None))
        self.label_41.setText(QCoreApplication.translate("submission", u"Name:", None))
        self.label_42.setText(QCoreApplication.translate("submission", u"Pattern:", None))
        self.label_43.setText(QCoreApplication.translate("submission", u"Repl:", None))
        self.label_44.setText(QCoreApplication.translate("submission", u"Source:", None))
        self.label_79.setText(QCoreApplication.translate("submission", u"Filter:", None))
        self.label_47.setText(QCoreApplication.translate("submission", u"Name:", None))
        self.label_48.setText(QCoreApplication.translate("submission", u"Pattern:", None))
        self.label_49.setText(QCoreApplication.translate("submission", u"Repl:", None))
        self.label_50.setText(QCoreApplication.translate("submission", u"Source:", None))
        self.label_80.setText(QCoreApplication.translate("submission", u"Filter:", None))
        self.label_55.setText(QCoreApplication.translate("submission", u"Name:", None))
        self.label_56.setText(QCoreApplication.translate("submission", u"Pattern:", None))
        self.label_57.setText(QCoreApplication.translate("submission", u"Repl:", None))
        self.label_58.setText(QCoreApplication.translate("submission", u"Source:", None))
        self.label_81.setText(QCoreApplication.translate("submission", u"Filter:", None))
        self.label_59.setText(QCoreApplication.translate("submission", u"Name:", None))
        self.label_60.setText(QCoreApplication.translate("submission", u"Pattern:", None))
        self.label_61.setText(QCoreApplication.translate("submission", u"Repl:", None))
        self.label_62.setText(QCoreApplication.translate("submission", u"Source:", None))
        self.label_82.setText(QCoreApplication.translate("submission", u"Filter:", None))
        self.label_63.setText(QCoreApplication.translate("submission", u"Name:", None))
        self.label_64.setText(QCoreApplication.translate("submission", u"Pattern:", None))
        self.label_65.setText(QCoreApplication.translate("submission", u"Repl:", None))
        self.label_66.setText(QCoreApplication.translate("submission", u"Source:", None))
        self.label_83.setText(QCoreApplication.translate("submission", u"Filter:", None))
        self.label_67.setText(QCoreApplication.translate("submission", u"Name:", None))
        self.label_68.setText(QCoreApplication.translate("submission", u"Pattern:", None))
        self.label_69.setText(QCoreApplication.translate("submission", u"Repl:", None))
        self.label_70.setText(QCoreApplication.translate("submission", u"Source:", None))
        self.label_84.setText(QCoreApplication.translate("submission", u"Filter:", None))
        self.label_71.setText(QCoreApplication.translate("submission", u"Name:", None))
        self.label_72.setText(QCoreApplication.translate("submission", u"Pattern:", None))
        self.label_73.setText(QCoreApplication.translate("submission", u"Repl:", None))
        self.label_74.setText(QCoreApplication.translate("submission", u"Source:", None))
        self.label_85.setText(QCoreApplication.translate("submission", u"Filter:", None))
        self.label_87.setText(QCoreApplication.translate("submission", u"Name:", None))
        self.label_114.setText(QCoreApplication.translate("submission", u"Pattern:", None))
        self.label_115.setText(QCoreApplication.translate("submission", u"Repl:", None))
        self.label_116.setText(QCoreApplication.translate("submission", u"Source:", None))
        self.label_117.setText(QCoreApplication.translate("submission", u"Filter:", None))
        self.label_118.setText(QCoreApplication.translate("submission", u"Name:", None))
        self.label_119.setText(QCoreApplication.translate("submission", u"Pattern:", None))
        self.label_120.setText(QCoreApplication.translate("submission", u"Repl:", None))
        self.label_121.setText(QCoreApplication.translate("submission", u"Source:", None))
        self.label_122.setText(QCoreApplication.translate("submission", u"Filter:", None))
        self.label_123.setText(QCoreApplication.translate("submission", u"Name:", None))
        self.label_124.setText(QCoreApplication.translate("submission", u"Pattern:", None))
        self.label_125.setText(QCoreApplication.translate("submission", u"Repl:", None))
        self.label_126.setText(QCoreApplication.translate("submission", u"Source:", None))
        self.label_127.setText(QCoreApplication.translate("submission", u"Filter:", None))
        self.label_128.setText(QCoreApplication.translate("submission", u"Name:", None))
        self.label_129.setText(QCoreApplication.translate("submission", u"Pattern:", None))
        self.label_130.setText(QCoreApplication.translate("submission", u"Repl:", None))
        self.label_131.setText(QCoreApplication.translate("submission", u"Source:", None))
        self.label_132.setText(QCoreApplication.translate("submission", u"Filter:", None))
        self.label_133.setText(QCoreApplication.translate("submission", u"Name:", None))
        self.label_144.setText(QCoreApplication.translate("submission", u"Pattern:", None))
        self.label_145.setText(QCoreApplication.translate("submission", u"Repl:", None))
        self.label_146.setText(QCoreApplication.translate("submission", u"Source:", None))
        self.label_147.setText(QCoreApplication.translate("submission", u"Filter:", None))
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
        self.ftrack_use.setText(QCoreApplication.translate("submission", u"Use Ftrack", None))
        self.label_161.setText(QCoreApplication.translate("submission", u"Include:", None))
        self.ftrack_include.setText("")
        self.label_90.setText(QCoreApplication.translate("submission", u"Project:", None))
        self.ftrack_project.setText("")
        self.label_158.setText(QCoreApplication.translate("submission", u"Shot", None))
        self.ftrack_shot.setText(QCoreApplication.translate("submission", u"{shot}", None))
        self.label_159.setText(QCoreApplication.translate("submission", u"Task", None))
        self.ftrack_task.setText(QCoreApplication.translate("submission", u"{task}", None))
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
        self.TopTab.setTabText(self.TopTab.indexOf(self.tab_11), QCoreApplication.translate("submission", u"Ftrack Note", None))
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
        self.groupBox_12.setTitle(QCoreApplication.translate("submission", u"Match Package to Vendor", None))
        self.label_163.setText(QCoreApplication.translate("submission", u"Package Key:", None))
#if QT_CONFIG(tooltip)
        self.vendor_csv_package_key.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>Renamer checks all folders one folder above the package folder<br/>and detects version in it by using Version Regex</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.vendor_csv_package_key.setText(QCoreApplication.translate("submission", u"_(\\d{3})$", None))
        self.vendor_csv_package_key.setPlaceholderText(QCoreApplication.translate("submission", u"preview", None))
        self.label_164.setText(QCoreApplication.translate("submission", u"Vendor Key:", None))
#if QT_CONFIG(tooltip)
        self.vendor_csv_vendor_key.setToolTip(QCoreApplication.translate("submission", u"<html><head/><body><p>Renamer checks all folders one folder above the package folder<br/>and detects version in it by using Version Regex</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.vendor_csv_vendor_key.setText(QCoreApplication.translate("submission", u"_(\\d{3})$", None))
        self.vendor_csv_vendor_key.setPlaceholderText(QCoreApplication.translate("submission", u"preview", None))
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
        self.check_sequence_size_consistency.setText(QCoreApplication.translate("submission", u"File Sequence Size consistency", None))
        self.check_sequence_holes.setText(QCoreApplication.translate("submission", u"Check for File Sequence Holes", None))
        self.groupBox_13.setTitle("")
        self.label_24.setText(QCoreApplication.translate("submission", u"If", None))
        self.label_23.setText(QCoreApplication.translate("submission", u"Check:", None))
        self.check_warning_1.setText(QCoreApplication.translate("submission", u"Warning", None))
        self.check_error_1.setText(QCoreApplication.translate("submission", u"Error", None))
        self.groupBox_16.setTitle("")
        self.label_25.setText(QCoreApplication.translate("submission", u"If", None))
        self.label_26.setText(QCoreApplication.translate("submission", u"Check:", None))
        self.check_warning_2.setText(QCoreApplication.translate("submission", u"Warning", None))
        self.check_error_2.setText(QCoreApplication.translate("submission", u"Error", None))
        self.groupBox_18.setTitle("")
        self.label_27.setText(QCoreApplication.translate("submission", u"If", None))
        self.label_28.setText(QCoreApplication.translate("submission", u"Check:", None))
        self.check_warning_3.setText(QCoreApplication.translate("submission", u"Warning", None))
        self.check_error_3.setText(QCoreApplication.translate("submission", u"Error", None))
        self.TopTab.setTabText(self.TopTab.indexOf(self.tab_12), QCoreApplication.translate("submission", u"Checks", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("submission", u"Frame Rate:", None))
        self.label_45.setText(QCoreApplication.translate("submission", u"Frame Rate:", None))
        self.prefs_frame_rate_txt.setText(QCoreApplication.translate("submission", u"24", None))
        self.prefs_frame_rate_use_meta.setText(QCoreApplication.translate("submission", u"Use Metadata FPS if Available", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("submission", u"TimeCode:", None))
        self.prefs_tc_from_meta.setText(QCoreApplication.translate("submission", u"From Metadata", None))
        self.prefs_tc_from_counter.setText(QCoreApplication.translate("submission", u"From Frame Counter", None))
        self.label_46.setText(QCoreApplication.translate("submission", u"Default TC:", None))
        self.prefs_tc_default.setText(QCoreApplication.translate("submission", u"01:00:00:00", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("submission", u"Counter:", None))
        self.label.setText(QCoreApplication.translate("submission", u"Start from:", None))
        self.label_2.setText(QCoreApplication.translate("submission", u"Step:", None))
        self.label_14.setText(QCoreApplication.translate("submission", u"Leading Zeroes:", None))
        self.groupBox_17.setTitle(QCoreApplication.translate("submission", u"File Sequence File Size Check:", None))
        self.prefs_size_scan.setText(QCoreApplication.translate("submission", u"Scan Sizes", None))
        self.label_51.setText(QCoreApplication.translate("submission", u"Ignore first frames:", None))
        self.label_53.setText(QCoreApplication.translate("submission", u"Neighborhood frames:", None))
        self.label_54.setText(QCoreApplication.translate("submission", u"Warning Treshhold %", None))
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
        self.groupBox_3.setTitle(QCoreApplication.translate("submission", u"Load Preset:", None))
        self.label_5.setText(QCoreApplication.translate("submission", u"Preset:", None))
        self.load_preset_button.setText(QCoreApplication.translate("submission", u"Load Preset", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("submission", u"Save Preset:", None))
        self.label_29.setText(QCoreApplication.translate("submission", u"Preset Name:", None))
        self.save_preset_button.setText(QCoreApplication.translate("submission", u"Save Preset", None))
        self.preset_explore.setText(QCoreApplication.translate("submission", u"Open Preset Folder", None))
        self.version_231024.setText(QCoreApplication.translate("submission", u"Release 2023-10-24", None))
        self.TopTab.setTabText(self.TopTab.indexOf(self.tab_3), QCoreApplication.translate("submission", u"Presets", None))
        self.textEdit.setHtml(QCoreApplication.translate("submission", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; color:#e8e8e8;\">Submission Helper</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">This tool is helping vfx vendors to send media to productions or other studios.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#e8e8e8;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-lef"
                        "t:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">Each sending usually consists of one or more media files, together with spreadsheet that binds the media files with additional info like notes, status, version, task...</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#e8e8e8;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">This process doesn't seem to have an industry standard, Submission Helper has numerous options to help interface vendor and production with as little friction as possible.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#e8e8e8;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin"
                        "-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://knowledge.autodesk.com/support/shotgrid/getting-started/caas/CloudHelp/cloudhelp/ENU/SG-Tutorials/files/SG-Tutorials-tu-submission-overview-html-html.html\"><span style=\" text-decoration: underline; color:#0000ff;\">Here</span></a><span style=\" color:#e8e8e8;\"> is the overview from ShotGrid:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#e8e8e8;\">Intended use</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">Package starts with one or more files that you want to package and send. Submission Helper checks all the files and h"
                        "elps to produce spreadsheet(s) and email that is easily ingested in receiver's system, often automatically.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#e8e8e8;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#e8e8e8;\">Features</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">* Helps to name the package by the template, including consecutive or per day versions</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">* Reads metadata from the files by ffprobe and other methods</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; ma"
                        "rgin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">* Calculates file sizes</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">* Allows to gather and copy sidecar files like CDLs or LUTs to the package.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">* Allows to define spreadsheet columns and values in a flexible way</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">* Generates up to two spreadsheets that are called in gui submission and drive log</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\""
                        ">* Generates a text file that is often used for email that follows up the sending.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">* Can read notes from Ftrack</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">* Allows for checking for holes in file sequences, files with zero size and other common problems</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">* Allows saving config to json files</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">* Can be used head-less </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom"
                        ":0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#e8e8e8;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#e8e8e8;\">Quick How-to</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">Submission Helper assumes you put the file(s) in one folder - the Package Folder.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#e8e8e8;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">1. Drag the package folder path anywhere to the Submission Helper window</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; marg"
                        "in-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">2. Set the Package Name options, till the preview matches what you need</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">3. Use Spreadsheet tab to define columns and their values</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">4. Set the export options in Exports and text tabs</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">5. Press Go to export</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#e8e8e8;\"><br /></p>\n"
"<p style=\" margin-top:0p"
                        "x; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#e8e8e8;\">Keywords</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#e8e8e8;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">name: file name, no path, no extension</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">printf_pattern: file name, for file sequence number is replaced with %04d for 0001</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">sequence_nuke: file name, number for file sequence is replaced by [sta"
                        "rt..end]</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">sequence_slate</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">sequence_slate_nuke</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">clean_name: file name with no extension and no trailing number</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">clean_name_no_sep: file name with no extension and no trailing number, if there is dot underscore or dash before trailing number, it is removed</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-b"
                        "lock-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">clean_name_sep_char: the number separation character</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#e8e8e8;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">number: trailing number</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">start_number: first number in file sequence</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">end_number: last number in file sequence</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                        "text-indent:0px;\"><span style=\" color:#e8e8e8;\">padding: leading zeroes used for trailing number</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">range: start-end frames for file sequence</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">range_slate: same as range, start+1</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#e8e8e8;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">extension: file extension, no dot</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-i"
                        "ndent:0; text-indent:0px; color:#e8e8e8;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">path_prs: path, with no file, no trailing slash</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">full_path: path to the file or first frame in file sequence</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">relative_path: path to the file, minus the path start to the package. Starts with slash</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">drive: drive letter (windows)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0p"
                        "x; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#e8e8e8;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">size_bytes: file size in bytes, calculated as total for file sequence</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">size_human: same as size_bytes, rounded to one decimal, with units</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#e8e8e8;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">category: files are categorized by extension. still, sequence, video, audio, multiframe, other</span></p>\n"
"<p sty"
                        "le=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#e8e8e8;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">cnt_sub, cnt_log, cnt_txt: counter for each export</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">total_sub, total_log, total_txt: total number of files for each export</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">files_sub, files_log, files_txt: total files for each export</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#e8e8e8;\"><br /><"
                        "/p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">d, dd, y, yy, m, mm: today day, month and year</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">package_date: package renaming date </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">package_name: package renaming name</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">package_version: package renaming version</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">package_name_from_folder: fold"
                        "er name initially provided by user</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">package_name_root: path to the package, without end folder</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#e8e8e8;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_aspect: image aspect, float</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_aspect_x: </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_aspect_y:</span></p>\n"
"<p s"
                        "tyle=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_audio_present</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_audio_present</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_audio_present</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_bits_per_sample_audio</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_channels_audio</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt"
                        "-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_codec_long_name_audio</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_codec_long_name_video</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_codec_name_audio</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_codec_name_audio</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_data_present</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">m"
                        "eta_duration_audio</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_duration_frames</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_duration_frames_slate</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_duration_secs</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_fields</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_fps</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px;"
                        " margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_fps_a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_fps_a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_fps_raw</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_frame_end_from_tc</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_frame_end_from_tc_slate</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_fra"
                        "me_start_from_tc</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_frame_start_from_tc_slate</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_height</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_is_log</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_reel</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_sample_rate_audio</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; m"
                        "argin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_time_code</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_time_stamp_audio</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_time_stamp_video</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_video_present</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e8e8e8;\">meta_width</span></p></body></html>", None))
        self.TopTab.setTabText(self.TopTab.indexOf(self.tab_14), QCoreApplication.translate("submission", u"Help", None))
        self.BottomTab.setTabText(self.BottomTab.indexOf(self.tab_6), QCoreApplication.translate("submission", u"Submission", None))
        self.BottomTab.setTabText(self.BottomTab.indexOf(self.tab_7), QCoreApplication.translate("submission", u"Drive Log", None))
        self.BottomTab.setTabText(self.BottomTab.indexOf(self.tab_8), QCoreApplication.translate("submission", u"Text", None))
        self.BottomTab.setTabText(self.BottomTab.indexOf(self.tab_15), QCoreApplication.translate("submission", u"Sidecar Files", None))
        self.write_button.setText(QCoreApplication.translate("submission", u"Go", None))
        self.reload.setText(QCoreApplication.translate("submission", u"Reload", None))
    # retranslateUi

