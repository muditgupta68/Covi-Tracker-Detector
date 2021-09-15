from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, QTime
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from trackWindow import Ui_trackWidget
from plyer import notification
from detectWindow import Ui_Form

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        # main window is group box
        # properties handling using PyQt5 designer
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(809, 687)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(41, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 222, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 222, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 222, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 222, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 222, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 222, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 222, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        MainWindow.setStyleSheet("background-color:#292929;color:#FFDE59;")

        # setting up the widgets and its properties
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainbox = QtWidgets.QGroupBox(self.centralwidget)
        self.mainbox.setGeometry(QtCore.QRect(10, 10, 791, 651))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setBold(True)
        font.setWeight(75)
        self.mainbox.setFont(font)
        self.mainbox.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.mainbox.setStyleSheet("")
        self.mainbox.setAlignment(QtCore.Qt.AlignCenter)
        self.mainbox.setObjectName("mainbox")

        # setting up the buttons : Tracking and Detecting properties into the widget
        # Tracking button properties
        self.Tracking = QtWidgets.QPushButton(self.mainbox)
        self.Tracking.setGeometry(QtCore.QRect(270, 360, 271, 61))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.Tracking.setFont(font)
        self.Tracking.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.Tracking.setStyleSheet(
            "*{color: white; border: 1px solid '#FFDE59'; border-radius: 15%;}" +
            "*:hover{background-color:'#FFDE59';color:'#22041C';border: 2px solid '#EE3EC9'}")
        self.Tracking.setObjectName("Tracking")
        self.Time = QtWidgets.QLabel(self.mainbox)

        # Date and Time named Labels properties setting up in the widget
        # These will Label will show the current date and opening Time of executable file
        self.Time.setGeometry(QtCore.QRect(670, 620, 111, 21))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setBold(True)
        font.setWeight(75)
        self.Time.setFont(font)
        self.Time.setObjectName("Time")
        self.Date = QtWidgets.QLabel(self.mainbox)
        self.Date.setGeometry(QtCore.QRect(10, 620, 91, 21))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setBold(True)
        font.setWeight(75)
        self.Date.setFont(font)
        self.Date.setObjectName("Date")

        # Detector button properties
        self.Detector = QtWidgets.QPushButton(self.mainbox)
        self.Detector.setGeometry(QtCore.QRect(270, 440, 271, 61))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.Detector.setFont(font)
        self.Detector.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Detector.setMouseTracking(False)
        self.Detector.setStyleSheet(
            "*{color: white; border: 1px solid '#FFDE59'; border-radius: 15%;}" +
            "*:hover{background-color:'#FFDE59';color:'#22041C';border: 2px solid '#EE3EC9'}")
        self.Detector.move(270, 480)
        self.Tracking.move(270, 400)
        self.Detector.setObjectName("Detector")

        # Widget properties
        self.line = QtWidgets.QFrame(self.mainbox)
        self.line.setGeometry(QtCore.QRect(10, 600, 771, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.Exit = QtWidgets.QAction(MainWindow)
        self.Exit.setObjectName("Exit")
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        QtWidgets.QToolTip.setFont(QtGui.QFont("MV Boli", 10))

        # Extra propretires for buttons
        self.Tracking.setToolTip('<em>Track the case</em>')
        self.Tracking.setToolTipDuration(1000)
        self.Detector.setToolTip('<em>Detect Symptom</em>')
        self.Detector.setToolTipDuration(1000)

        # time and date function for updating respective labels
        self.time()
        self.date()

        # Setting up the .gif Logo file and its positioning
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 50, 500, 500))
        self.label.setMinimumSize(QtCore.QSize(310, 310))
        self.label.setMaximumSize(QtCore.QSize(320, 320))
        self.label.setObjectName("gifClip")
        MainWindow.setCentralWidget(self.centralwidget)

        self.movie = QMovie("img\\logo.gif")
        self.label.setMovie(self.movie)
        self.movie.start()

        # setting-up the button's actions
        self.Tracking.clicked.connect(self.newWin1)
        self.Detector.clicked.connect(self.newWin2)
        
        self.notify("Covi-Tracker",
                    "Welcome to Covi-Tracker\nStay Home Stay Safe\n😄")

    # setting tracking window
    def newWin1(self):
        self.notify("Covi-Tracker",
                    "Action in progress...\nPlease wait for a while")
        self.window = QtWidgets.QWidget()
        self.ui = Ui_trackWidget()
        self.ui.setupUi(self.window)
        self.window.show()

    def newWin2(self):
        self.notify("Covi-Tracker",
                    "Action in progress...\nPlease wait for a while")
        self.window2 = QtWidgets.QWidget()
        self.ui2 = Ui_Form()
        self.ui2.setupUi(self.window2)
        self.window2.show()
    
    # setting notification message for the action
    def notify(self, t, m):
        notification.notify(
            title=t,
            message=m,
            app_icon="img\\covid.ico",
            timeout=5)

    # date function
    def date(self):
        date = QDate.currentDate()
        date = date.toString()
        self.Date.setText(f"Date : {date}")
        self.Date.adjustSize()

    # time function
    def time(self):
        time = QTime.currentTime()
        time = time.toString()
        self.Time.setText(f"Time : {time}")
        self.Time.adjustSize()

    # setting up the texts on buttons,labels and group widgets
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Covi-Tracker"))
        self.mainbox.setTitle(_translate(
            "MainWindow", "Made with ❤ by Mudit Gupta"))
        self.Tracking.setText(_translate(
            "MainWindow", "Track the Corona Case"))
        self.Time.setText(_translate("MainWindow", "Time:"))
        self.Date.setText(_translate("MainWindow", "Date:"))
        self.Detector.setText(_translate(
            "MainWindow", "Coronavirus Detector"))
        self.Exit.setText(_translate("MainWindow", "exit"))
        MainWindow.setWindowIcon(QtGui.QIcon('img\\covid.ico'))
        MainWindow.setFixedSize(809, 687)


# main function
# def main():
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
