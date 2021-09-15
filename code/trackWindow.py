
from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from bs4 import BeautifulSoup
import re


class Ui_trackWidget():

    # ? properties handling using PyQt5 designer
    #! Added extra label elements on my own so .ui file might not be same

    def setupUi(self, trackWidget):
        trackWidget.setObjectName("trackWidget")
        trackWidget.resize(747, 663)
        trackWidget.setStyleSheet("background-color:#292929;color:#FFDE59;")
        self.place_box = QtWidgets.QComboBox(trackWidget)
        self.place_box.setGeometry(QtCore.QRect(230, 120, 281, 51))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.place_box.setFont(font)
        self.place_box.setStyleSheet(
            "border: 1px solid #FFDE59; color: white;")
        self.place_box.setEditable(False)
        self.place_box.setCurrentText("")
        self.place_box.setDuplicatesEnabled(False)
        self.place_box.setFrame(True)
        self.place_box.setObjectName("place_box")
        self.noActionLabel = QtWidgets.QLabel(trackWidget)
        self.noActionLabel.setGeometry(QtCore.QRect(230, 40, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.noActionLabel.setFont(font)
        self.noActionLabel.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.noActionLabel.setFocusPolicy(QtCore.Qt.NoFocus)
        self.noActionLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.noActionLabel.setStyleSheet(
            "color:white;border: 1px outset #FFDE59;border-style: none none outset none;")
        self.noActionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.noActionLabel.setObjectName("noActionLabel")
        self.countries_checkbox = QtWidgets.QRadioButton(trackWidget)
        self.countries_checkbox.setGeometry(QtCore.QRect(230, 210, 101, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.countries_checkbox.setFont(font)
        self.countries_checkbox.setObjectName("countries_checkbox")
        self.states_of_india__checkbox = QtWidgets.QRadioButton(trackWidget)
        self.states_of_india__checkbox.setGeometry(
            QtCore.QRect(360, 210, 151, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.states_of_india__checkbox.setFont(font)
        self.states_of_india__checkbox.setObjectName(
            "states_of_india__checkbox")
        self.result_data = QtWidgets.QGroupBox(trackWidget)
        self.result_data.setGeometry(QtCore.QRect(180, 350, 391, 281))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.result_data.setFont(font)
        self.result_data.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.result_data.setAlignment(QtCore.Qt.AlignCenter)
        self.result_data.setObjectName("result_data")
        self.l1 = QtWidgets.QLabel(self.result_data)
        self.l1.setGeometry(QtCore.QRect(40, 30, 311, 71))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.l1.setFont(font)
        self.l1.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.l1.setStyleSheet("border: 1px dotted #EE3EC9; color: white;")
        self.l1.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.l1.setObjectName("l1")
        self.corona_data = QtWidgets.QLabel(self.result_data)
        self.corona_data.setGeometry(QtCore.QRect(170, 50, 161, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.corona_data.setFont(font)
        self.corona_data.setStyleSheet(
            "border: 1px solid #FFDE59; color: white;")
        self.corona_data.setText("")
        self.corona_data.setAlignment(QtCore.Qt.AlignCenter)
        self.corona_data.setObjectName("corona_data")
        self.l2 = QtWidgets.QLabel(self.result_data)
        self.l2.setGeometry(QtCore.QRect(40, 110, 311, 71))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.l2.setFont(font)
        self.l2.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.l2.setStyleSheet("border: 1px dotted #EE3EC9; color: white;")
        self.l2.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.l2.setObjectName("l2")
        self.death_data = QtWidgets.QLabel(self.result_data)
        self.death_data.setGeometry(QtCore.QRect(170, 130, 161, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.death_data.setFont(font)
        self.death_data.setStyleSheet(
            "border: 1px solid #FFDE59; color: white;")
        self.death_data.setText("")
        self.death_data.setAlignment(QtCore.Qt.AlignCenter)
        self.death_data.setObjectName("death_data")
        self.l3 = QtWidgets.QLabel(self.result_data)
        self.l3.setGeometry(QtCore.QRect(40, 190, 311, 71))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.l3.setFont(font)
        self.l3.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.l3.setStyleSheet("border: 1px dotted #EE3EC9; color: white;")
        self.l3.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.l3.setObjectName("l3")
        self.recover_data = QtWidgets.QLabel(self.result_data)
        self.recover_data.setGeometry(QtCore.QRect(170, 210, 161, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.recover_data.setFont(font)
        self.recover_data.setStyleSheet(
            "border: 1px solid #FFDE59; color: white;")
        self.recover_data.setText("")
        self.recover_data.setAlignment(QtCore.Qt.AlignCenter)
        self.recover_data.setObjectName("recover_data")
        self.TrackingC_button = QtWidgets.QPushButton(trackWidget)
        self.TrackingS_button = QtWidgets.QPushButton(trackWidget)
        self.TrackingC_button.setGeometry(QtCore.QRect(180, 280, 201, 51))
        self.TrackingS_button.setGeometry(QtCore.QRect(400, 280, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.TrackingC_button.setFont(font)
        self.TrackingS_button.setFont(font)
        self.TrackingC_button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.TrackingS_button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.TrackingC_button.setMouseTracking(False)
        self.TrackingS_button.setMouseTracking(False)
        self.TrackingC_button.setStyleSheet(
            "*{color: white; border: 1px solid '#FFDE59'; border-radius: 15%;}" +
            "*:hover{background-color:'#FFDE59';color:'#22041C';border: 2px solid '#EE3EC9'}")
        self.TrackingS_button.setStyleSheet(
            "*{color: white; border: 1px solid '#FFDE59'; border-radius: 15%;}" +
            "*:hover{background-color:'#FFDE59';color:'#22041C';border: 2px solid '#EE3EC9'}")
        self.TrackingC_button.setObjectName("TrackingC_button")
        self.TrackingS_button.setObjectName("TrackingS_button")
        self.retranslateUi(trackWidget)
        QtCore.QMetaObject.connectSlotsByName(trackWidget)
        self.scrapping()

    # ? when country checkbox clicks, function fills names in form of data in comboBox
    def countryComboBox(self, soup):
        emptyData = ["", "", ""]
        self.valueBox(emptyData)
        self.name = []
        for block in soup.find_all("a", class_="mt_a"):
            self.name.append(block.text)
        self.place_box.clear()
        self.place_box.addItems(self.name)

        #! disables the state tracking button if country checkbox enabled
        if self.countries_checkbox.isChecked() == True:
            self.TrackingC_button.setEnabled(True)
            self.TrackingS_button.setEnabled(False)
            self.TrackingC_button.clicked.connect(self.trackCountry)

    # ? extracting html data sets from the websites for respective countries

    def trackCountry(self):
        ctryName = self.place_box.currentText()
        ctryName = ctryName.lower()
        ctryName = ctryName.replace(" ", "-")
        ctryName = ctryName.replace("s.-korea", "south-korea")

        if ctryName == 'usa':
            ctryName = 'us'
        elif ctryName == 'north-macedonia':
            ctryName = 'macedonia'
        elif ctryName == 'drc':
            ctryName = 'democratic-republic-of-the-congo'

        url = "https://www.worldometers.info/coronavirus/country/" + ctryName + "/"
        # print(url)
        r = self.dataCollect(url)
        soup = BeautifulSoup(r, "html.parser")

        outerDiv = soup.find(
            "div", class_="content-inner").find_all("div", id="maincounter-wrap")
        # print(outerDiv)
        caseData = []

        for block in outerDiv:
            case = block.find("span")
            caseData.append(case)

        caseData = str(caseData)
        caseData = caseData.replace(", ", " ")
        exp = r"([0-9,]+)"
        cases = re.findall(exp, caseData)

        self.valueBox(cases)

    # ? data filling in the respective O/P label
    def valueBox(self, caseData):

        self.corona_data.setText(caseData[0])
        self.death_data.setText(caseData[1])
        self.recover_data.setText(caseData[2])

    # ? when state checkbox clicks, function fills names in form of data in comboBox
    def stateComboBox(self, soup):

        # clearing O/P fields
        emptyData = ["", "", ""]
        self.valueBox(emptyData)

        # data extraction
        stateName = soup.find_all(
            "div", class_='field field-name-field-select-state field-type-list-text field-label-above')

        totCase = soup.find_all(
            "div", class_='field field-name-field-total-confirmed-indians field-type-number-integer field-label-above')

        recover = soup.find_all(
            "div", class_='field field-name-field-cured field-type-number-integer field-label-above')

        death = soup.find_all(
            "div", class_='field field-name-field-deaths field-type-number-integer field-label-above')

        #!Name of state entry
        nameData = self.dataEntry(stateName)
        exp = r"[a-zA-Z ]+"
        nameFinal = re.findall(exp, nameData)

        self.place_box.clear()
        self.place_box.addItems(nameFinal)

        #!Data list of death, recover and overall cases
        self.totData = self.dataEntry(totCase)
        self.deathData = self.dataEntry(death)
        self.recoverData = self.dataEntry(recover)

        #! disables the country tracking button if state checkbox enabled
        if self.states_of_india__checkbox.isChecked() == True:
            self.TrackingS_button.setEnabled(True)
            self.TrackingC_button.setEnabled(False)
            self.TrackingS_button.clicked.connect(self.trackstate)

    # functionality inputs the data in the O/P fields
    def trackstate(self):
        exp = r"[0-9,]+"
        totFinal = re.findall(exp, self.totData)
        recoverFinal = re.findall(exp, self.deathData)
        deathFinal = re.findall(exp, self.recoverData)

        dataName = self.place_box.currentText()
        index = self.place_box.findText(dataName, QtCore.Qt.MatchFixedString)

        finalDataSet = [totFinal[index],
                        deathFinal[index], recoverFinal[index]]
        # print(finalDataSet)
        self.valueBox(finalDataSet)

    # function returns values of tags in string
    def dataEntry(self, data):
        nameData = ""
        for block in data:
            nameData = nameData + block.text + "\n"
        nameData = nameData.replace('State Name:', "")
        return nameData

    # url functionality
    def urlData(self):
        self.url = ["https://www.mygov.in/corona-data/covid19-statewise-status/",
                    "https://www.worldometers.info/coronavirus/#countries",
                    "https://www.worldometers.info/coronavirus/country/"]
        return self.url

    # returns html tags of the website <page source>
    def dataCollect(self, url):
        self.r = requests.get(url)
        return self.r.text

    # web scrapping MAIN functionality
    def scrapping(self):
        self.url = self.urlData()
        self.r1 = self.dataCollect(self.url[0])  # ? states data
        self.r2 = self.dataCollect(self.url[1])  # ? countries list
        self.r3 = self.dataCollect(self.url[2])  # ? countries Covid data

        self.soup1 = BeautifulSoup(self.r1, "html.parser")
        self.soup2 = BeautifulSoup(self.r2, "html.parser")
        self.soup3 = BeautifulSoup(self.r3, "html.parser")

        self.countries_checkbox.toggled.connect(
            lambda: self.countryComboBox(self.soup2))

        self.states_of_india__checkbox.toggled.connect(
            lambda: self.stateComboBox(self.soup1))

    # setting up the texts on buttons,labels and group widgets
    def retranslateUi(self, trackWidget):
        _translate = QtCore.QCoreApplication.translate
        trackWidget.setWindowTitle(_translate("trackWidget", "Form"))
        self.noActionLabel.setText(_translate("trackWidget", "Covi-Tracker"))
        self.countries_checkbox.setText(_translate("trackWidget", "Countries"))
        self.states_of_india__checkbox.setText(
            _translate("trackWidget", "States of India"))
        self.l1.setText(_translate("trackWidget", "  CORONA CASES :"))
        self.l2.setText(_translate("trackWidget", "   DEATH DATA :"))
        self.l3.setText(_translate("trackWidget", "   RECOVERED :"))
        self.TrackingC_button.setText(
            _translate("trackWidget", "Track Countries"))
        self.TrackingS_button.setText(
            _translate("trackWidget", "Track States"))
        trackWidget.setWindowIcon(QtGui.QIcon('img\\covid.ico'))
        trackWidget.setFixedSize(809, 687)


# def main():
# MAIN function
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    trackWidget = QtWidgets.QWidget()
    ui = Ui_trackWidget()
    ui.setupUi(trackWidget)
    trackWidget.show()
    sys.exit(app.exec_())
