# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/aarav/Documents/QtWorkspace/TTD_main.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import xlsxwriter
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QVariant
from PyQt5.QtWidgets import QMessageBox, QCheckBox
from datetime import *
from database_connector import Database
from warrant import Cognito
import datetime
import pathlib
import os
import sys

class Ui_FleetConsole(object):
    database = Database()
    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)
    def setupUi(self, FleetConsole):
        FleetConsole.setObjectName("FleetConsole")
        FleetConsole.resize(800, 600)
        FleetConsole.setStyleSheet("background-color: #124E78;")
        self.centralwidget = QtWidgets.QWidget(FleetConsole)
        self.centralwidget.setObjectName("centralwidget")
        self.labelLogo = QtWidgets.QLabel(self.centralwidget)
        self.labelLogo.setGeometry(QtCore.QRect(290, 50, 251, 201))
        self.labelLogo.setText("")

        print(os.path.realpath(os.path.dirname(sys.argv[0])))

        pixmap = QtGui.QPixmap(self.resource_path("truck_blue.png"))
        pixmap = pixmap.scaled(971/4,780/4)
        self.labelLogo.setPixmap(pixmap)
        self.labelLogo.setObjectName("labelLogo")
        self.pushButtonHome = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonHome.setGeometry(QtCore.QRect(720, 20, 50, 50))
        self.pushButtonHome.setIcon(
            QtGui.QIcon(self.resource_path("144x144.png")))
        self.pushButtonHome.setStyleSheet("border-radius: 3px;")
        self.pushButtonHome.setIconSize(QtCore.QSize(45, 45))
        self.pushButtonHome.setText("")
        self.pushButtonHome.setObjectName("pushButtonHome")
        self.pushButtonHome.clicked.connect(self.show_expire_notification)

        self.pushButtonShipper = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonShipper.setGeometry(QtCore.QRect(160, 300, 151, 81))
        self.pushButtonShipper.setStyleSheet("background-color: rgb(255, 255, 255);\n"
            "border-color: rgb(3, 38, 75);\n"
            "selection-background-color: rgb(3, 38, 75);")
        self.pushButtonShipper.setObjectName("pushButtonShipper")
        self.pushButtonShipper.clicked.connect(self.show_shipper_manager)

        self.pushButtonJobs = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonJobs.setGeometry(QtCore.QRect(350, 300, 151, 81))
        self.pushButtonJobs.setStyleSheet("background-color: rgb(255, 255, 255);\n"
            "selection-background-color: rgb(3, 38, 75);\n"
            "selection-color: rgb(255, 255, 255);\n"
            "border-color: rgb(3, 38, 75);")
        self.pushButtonJobs.setObjectName("pushButtonJobs")
        self.pushButtonJobs.clicked.connect(self.show_add_job)

        self.pushButtonCreateBroker = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonCreateBroker.setGeometry(QtCore.QRect(540, 300, 151, 81))
        self.pushButtonCreateBroker.setStyleSheet("background-color: rgb(255, 255, 255);\n"
            "selection-background-color: rgb(3, 38, 75);\n"
            "selection-color: rgb(255, 255, 255);\n"
            "border-color: rgb(3, 38, 75);")
        self.pushButtonCreateBroker.setObjectName("pushButtonCreateBroker")
        self.pushButtonCreateBroker.clicked.connect(self.show_create_broker)

        self.pushButtonGenerateInvoice = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonGenerateInvoice.setGeometry(QtCore.QRect(540, 420, 151, 81))
        self.pushButtonGenerateInvoice.setStyleSheet("background-color: rgb(255, 255, 255);\n"
            "selection-background-color: rgb(3, 38, 75);\n"
            "selection-color: rgb(255, 255, 255);\n"
            "border-color: rgb(3, 38, 75);")
        self.pushButtonGenerateInvoice.setObjectName("pushButtonGenerateInvoice")
        self.pushButtonGenerateInvoice.clicked.connect(self.show_generate)

        self.pushButtonBol = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonBol.setGeometry(QtCore.QRect(160, 420, 151, 81))
        self.pushButtonBol.setStyleSheet("background-color: rgb(255, 255, 255);\n"
            "selection-background-color: rgb(3, 38, 75);\n"
            "selection-color: rgb(255, 255, 255);\n"
            "border-color: rgb(3, 38, 75);")
        self.pushButtonBol.setObjectName("pushButtonBol")
        self.pushButtonBol.clicked.connect(self.show_BOL)

        self.pushButtonDriverLogs = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonDriverLogs.setGeometry(QtCore.QRect(350, 420, 151, 81))
        self.pushButtonDriverLogs.setStyleSheet("background-color: rgb(255, 255, 255);\n"
            "selection-background-color: rgb(3, 38, 75);\n"
            "selection-color: rgb(255, 255, 255);\n"
            "border-color: rgb(3, 38, 75);")
        self.pushButtonDriverLogs.setObjectName("pushButtonDriverLogs")
        self.pushButtonDriverLogs.clicked.connect(self.show_driver_log)

        FleetConsole.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FleetConsole)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuFLEET_MANAGER_CONSOLE = QtWidgets.QMenu(self.menubar)
        self.menuFLEET_MANAGER_CONSOLE.setObjectName("menuFLEET_MANAGER_CONSOLE")
        FleetConsole.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FleetConsole)
        self.statusbar.setObjectName("statusbar")
        FleetConsole.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFLEET_MANAGER_CONSOLE.menuAction())

        self.retranslateUi(FleetConsole)
        QtCore.QMetaObject.connectSlotsByName(FleetConsole)

    def show_expire_notification(self):
        self.pushNotificationMessage = QtWidgets.QMessageBox()
        self.pushNotificationMessage.setIcon(QMessageBox.Warning)
        self.pushNotificationMessage.setText("Notification of any Expired date")
        self.pushNotificationMessage.setInformativeText("This is additional information")
        self.pushNotificationMessage.setWindowTitle("MessageBox demo")
        if len(self.print_exp_notification()) <= 0 and len(self.print_job_notification()) <=0:
            self.pushNotificationMessage.setDetailedText("No events")
        else:
            self.pushNotificationMessage.setDetailedText(self.print_exp_notification() + self.print_job_notification())
        self.pushNotificationMessage.exec_();

    def retranslateUi(self, FleetConsole):
        _translate = QtCore.QCoreApplication.translate
        FleetConsole.setWindowTitle(_translate("FleetConsole", "MainWindow"))
        self.pushButtonShipper.setText(_translate("FleetConsole", "Shipper Manager"))
        self.pushButtonJobs.setText(_translate("FleetConsole", "Jobs Manager"))
        self.pushButtonCreateBroker.setText(_translate("FleetConsole", "Create Broker"))
        self.pushButtonGenerateInvoice.setText(_translate("FleetConsole", "Generate Logs"))
        self.pushButtonBol.setText(_translate("FleetConsole", "View Bill of Ladings"))
        self.pushButtonDriverLogs.setText(_translate("FleetConsole", "Driver Info"))
        self.menuFLEET_MANAGER_CONSOLE.setTitle(_translate("FleetConsole", "FLEET MANAGER CONSOLE"))

    def show_create_broker(self):
        self.database.refresh()
        self.ui.setupUiAddBroker(self.FleetConsole)

    def show_shipper_manager(self):
        self.database.refresh()
        self.ui.setupUiAddShipper(self.FleetConsole)

    def show_generate(self):
        self.database.refresh()
        self.ui.setupUiGenerate(self.FleetConsole)

    def show_add_job(self):
        self.database.refresh()
        self.ui.setupUiAddJob(self.FleetConsole)

    def show_home(self):
        self.database.refresh()
        self.ui.setupUi(self.FleetConsole)

    def show_BOL(self):
        self.database.refresh()
        self.ui.setupUiBOL(self.FleetConsole)

    def show_driver_log(self):
        self.database.refresh()
        self.ui.setupUiDriverLog(self.FleetConsole)

    def setupUiAddJob(self, AddJob):
        AddJob.setObjectName("AddJob")
        AddJob.resize(809, 633)
        AddJob.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(AddJob)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 10, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setStyleSheet('QLabel {color: #124E78;}')

        # self.listWidgetJobs = QtWidgets.QListWidget(self.centralwidget)
        # self.listWidgetJobs.setGeometry(QtCore.QRect(40, 80, 261, 451))
        # self.listWidgetJobs.setEditTriggers(
        #     QtWidgets.QAbstractItemView.DoubleClicked | QtWidgets.QAbstractItemView.EditKeyPressed | QtWidgets.QAbstractItemView.SelectedClicked)
        # self.listWidgetJobs.setObjectName("listWidgetJobs")
        # self.listWidgetJobs.itemSelectionChanged.connect(self.change_data)
        #
        # self.update_jobs_list()
        # self.selected_job = None

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 330, 761, 251))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")

        # label for shipper name

        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(60, 10, 81, 21))
        self.label_2.setObjectName("label_2")

        # spinbox shipper name
        self.spinBoxShipper = QtWidgets.QComboBox(self.groupBox)
        self.spinBoxShipper.setGeometry(QtCore.QRect(150, 10, 201, 22))
        self.spinBoxShipper.setObjectName("spinBoxShipper")
        self.shipername_list = self.database.get_shippernames()
        self.spinBoxShipper.setStyleSheet("background-color: rgb(255, 255, 255); selection-background-color: #4199D8; text-align: left; color: rgb(0, 0, 0);")
        self.spinBoxShipper.addItems(self.shipername_list)

        # label for broker name

        self.label_broker = QtWidgets.QLabel(self.groupBox)
        self.label_broker.setGeometry(QtCore.QRect(60, 40, 101, 21))
        self.label_broker.setObjectName("label_broker")

        # spinbox broker name
        self.spinBoxBroker = QtWidgets.QComboBox(self.groupBox)
        self.spinBoxBroker.setGeometry(QtCore.QRect(150, 40, 201, 22))
        self.spinBoxBroker.setObjectName("spinBoxBroker")
        self.brokername_list = self.database.get_brokernames()
        self.spinBoxBroker.setStyleSheet("background-color: rgb(255, 255, 255); selection-background-color: #4199D8; text-align: left; color: rgb(0, 0, 0);")
        self.spinBoxBroker.addItems(self.brokername_list)


        # label for name
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(60, 70, 81, 21))
        self.label_3.setObjectName("label_3")

        # spinbox for Username
        self.spinBoxUsername = QtWidgets.QComboBox(self.groupBox)
        self.spinBoxUsername.setGeometry(QtCore.QRect(150, 70, 201, 22))
        self.spinBoxUsername.setObjectName("spinBoxUsername")
        self.username_list = self.database.get_usernames()
        self.spinBoxUsername.addItems(self.username_list)
        self.spinBoxUsername.setStyleSheet("background-color: rgb(255, 255, 255); selection-background-color: #4199D8; text-align: left; color: rgb(0, 0, 0);")

        self.dateEdit = QtWidgets.QDateEdit(self.groupBox)
        self.dateEdit.setGeometry(QtCore.QRect(150, 100, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())

        # label7 : date
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(60, 100, 71, 21))
        self.label_7.setObjectName("label_7")


        # label 8 : start time
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(60, 130, 71, 21))
        self.label_8.setObjectName("label_8")
        self.timeEditStartTime = QtWidgets.QTimeEdit(self.groupBox)
        self.timeEditStartTime.setGeometry(QtCore.QRect(150, 130, 111, 22))
        self.timeEditStartTime.setObjectName("timeEditStartTime")
        # Rate $  per type
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(60, 160, 71, 21))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(150, 160, 16, 21))
        self.label_11.setObjectName("label_11")
        self.lineEditRate = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditRate.setGeometry(QtCore.QRect(160, 160, 91, 21))
        self.lineEditRate.setObjectName("lineEdit")
        # spinbox for type
        self.spinBoxRate = QtWidgets.QComboBox(self.groupBox)
        self.spinBoxRate.setGeometry(QtCore.QRect(260, 160, 101, 22))
        self.spinBoxRate.setObjectName("spinBoxRate")
        self.spinBoxRate.setStyleSheet("background-color: rgb(255, 255, 255); selection-background-color: #4199D8; text-align: left; color: rgb(0, 0, 0);")
        self.spinBoxRate.addItem("Per Hour")
        self.spinBoxRate.addItem("Per Load")
        #label4:  Origin address
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(410, 10, 111, 16))
        self.label_4.setObjectName("label_4")
        self.textEditOriginAddress = QtWidgets.QTextEdit(self.groupBox)
        self.textEditOriginAddress.setGeometry(QtCore.QRect(410, 30, 311, 31))
        self.textEditOriginAddress.setObjectName("textEditOriginAddress")
        #label5: Destination address
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(410, 70, 141, 16))
        self.label_5.setObjectName("label_5")
        self.textEditDestinationAddress = QtWidgets.QTextEdit(self.groupBox)
        self.textEditDestinationAddress.setGeometry(QtCore.QRect(410, 90, 311, 31))
        self.textEditDestinationAddress.setObjectName("textEditDestinationAddress")
        #label6: Comments
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(410, 130, 141, 16))
        self.label_6.setObjectName("label_6")

        self.textEditComments = QtWidgets.QTextEdit(self.groupBox)
        self.textEditComments.setGeometry(QtCore.QRect(410, 160, 311, 41))
        self.textEditComments.setObjectName("textEditComments")

        self.pushButtonClearAddJob = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonClearAddJob.setGeometry(QtCore.QRect(520, 210, 114, 32))
        self.pushButtonClearAddJob.setStyleSheet("background-color: rgb(192, 192, 192);")
        self.pushButtonClearAddJob.setObjectName("pushButtonClearAddJob")
        self.pushButtonClearAddJob.clicked.connect(self.clear_form_add_job)

        self.pushButtonAddJob = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonAddJob.setGeometry(QtCore.QRect(400, 210, 114, 32))
        self.pushButtonAddJob.setStyleSheet("background-color: rgb(40, 195, 50);")
        self.pushButtonAddJob.setObjectName("pushButtonAddJob")
        self.pushButtonAddJob.clicked.connect(self.add_job)

        self.pushButtonEditJob = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonEditJob.setGeometry(QtCore.QRect(280, 210, 114, 32))
        self.pushButtonEditJob.setStyleSheet("background-color: rgb(255, 193, 44);")
        self.pushButtonEditJob.setObjectName("pushButtonEditJob")
        self.pushButtonEditJob.clicked.connect(self.edit_job)

        self.pushButtonDeleteJob = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonDeleteJob.setGeometry(QtCore.QRect(160, 210, 114, 32))
        self.pushButtonDeleteJob.setStyleSheet("background-color: rgb(253, 70, 70);")
        self.pushButtonDeleteJob.clicked.connect(self.delete_job)
        self.pushButtonDeleteJob.setObjectName("pushButtonDeleteJob")

        self.labelError = QtWidgets.QLabel(self.centralwidget)
        self.labelError.setGeometry(QtCore.QRect(280, 580, 421, 21))
        self.labelError.setText("")
        self.labelError.setObjectName("labelError")
        self.labelError.setStyleSheet('QLabel {color: #990000;}')



        self.pushButtonHome = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonHome.setGeometry(QtCore.QRect(720, 20, 50, 50))
        self.pushButtonHome.setIcon(
            QtGui.QIcon(self.resource_path("144x144.png")))
        self.pushButtonHome.setStyleSheet("border-radius: 3px;")
        self.pushButtonHome.setIconSize(QtCore.QSize(45, 45))
        self.pushButtonHome.setText("")
        self.pushButtonHome.setObjectName("pushButtonHome")
        self.pushButtonHome.clicked.connect(self.show_home)

        self.tableWidgetJobs = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidgetJobs.setGeometry(QtCore.QRect(20, 70, 771, 261))
        self.tableWidgetJobs.setObjectName("tableWidgetJobs")
        self.tableWidgetJobs.setColumnCount(8)
        self.tableWidgetJobs.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.tableWidgetJobs.itemSelectionChanged.connect(self.change_data)
        column_titles = ['id', 'username','shipper_name','broker_name', 'start_date','Origin','Destination', 'status']
        counter = 0
        for title in column_titles:
            item = QtWidgets.QTableWidgetItem(title)
            item.setBackground(QtGui.QColor(211,211,211))
            self.tableWidgetJobs.setHorizontalHeaderItem(counter,item)
            counter += 1
        self.update_jobs_list()
        self.tableWidgetJobs.setColumnWidth(5,120)
        self.tableWidgetJobs.setColumnWidth(6,120)
        self.tableWidgetJobs.setSortingEnabled(True)
        # self.tableWidgetJobs.resizeRowsToContents()
        # self.tableWidgetJobs.horizontalHeader().sortIndicatorChanged.connect(self.tableWidgetJobs.resizeRowsToContents)
        self.tableWidgetJobs.verticalHeader().setVisible(False)
        header = self.tableWidgetJobs.resizeColumnToContents(0)

        # AddJob.setCentralWidget(self.centralwidget)
        # self.menubar = QtWidgets.QMenuBar(AddJob)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 809, 22))
        # self.menubar.setObjectName("menubar")
        # DriverLog.setMenuBar(self.menubar)
        # self.statusbar = QtWidgets.QStatusBar(DriverLog)
        # self.statusbar.setObjectName("statusbar")
        # DriverLog.setStatusBar(self.statusbar)
        #
        # self.retranslateUiDriverLog(AddJob)
        # QtCore.QMetaObject.connectSlotsByName(AddJob)


        AddJob.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AddJob)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 809, 22))
        self.menubar.setObjectName("menubar")
        AddJob.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AddJob)
        self.statusbar.setObjectName("statusbar")
        AddJob.setStatusBar(self.statusbar)

        self.retranslateUiAddJob(AddJob)
        QtCore.QMetaObject.connectSlotsByName(AddJob)

    def retranslateUiAddJob(self, AddJob):
        _translate = QtCore.QCoreApplication.translate
        AddJob.setWindowTitle(_translate("AddJob", "MainWindow"))
        self.label.setText(_translate("AddJob", "ADD JOB"))
        self.label_2.setText(_translate("AddJob", "Shipper Name:"))
        self.label_broker.setText(_translate("AddJob", "Broker Name:"))
        self.label_3.setText(_translate("AddJob", "Username:"))
        self.label_4.setText(_translate("AddJob", "Origin Address:"))
        self.label_5.setText(_translate("AddJob", "Destination Address:"))
        self.label_6.setText(_translate("AddJob", "Comments:"))
        self.pushButtonAddJob.setText(_translate("AddJob", "Add Job"))
        self.pushButtonEditJob.setText(_translate("AddJob", "Edit Job"))
        self.pushButtonDeleteJob.setText(_translate("AddJob", "Delete Job"))
        self.pushButtonClearAddJob.setText(_translate("AddJob", "Clear Job"))
        self.label_7.setText(_translate("AddJob", "Date:"))
        self.label_8.setText(_translate("AddJob", "Start Time:"))
        self.label_10.setText(_translate("AddJob", "Rate:"))
        self.label_11.setText(_translate("AddJob", "$"))


    def update_jobs_list(self):
        # self.listWidgetJobs.clear()
        # jobs_list = self.database.get_current_jobs()
        # for job in jobs_list:
        #     job_description = "{} - {} on {} at {} : {}".format(job.job_id, job.username, job.start_date, job.shipper_name, job.status.upper())
        #     self.listWidgetJobs.addItem(job_description)

        for i in reversed(range(self.tableWidgetJobs.rowCount())):
            self.tableWidgetJobs.removeRow(i)

        jobs_list = self.database.get_current_jobs()

        for row_number in range(len(jobs_list)):
            self.tableWidgetJobs.insertRow(row_number)
            job = jobs_list[row_number]
            b = QtWidgets.QTableWidgetItem()
            b.setData(Qt.EditRole, QVariant(job.job_id))
            # item.setData(Qt.EditRole, QVariant(data))
            # self.tableWidgetJobs.setItem(row_number, 0, QtWidgets.QTableWidgetItem(str(job.job_id)))
            dt = datetime.datetime.strptime(str(job.start_date), '%Y-%m-%d').strftime('%m/%d/%y')
            # datetime.date.strftime(job.start_date, "%m/%d/%y")
            self.tableWidgetJobs.setItem(row_number, 0, b)
            self.tableWidgetJobs.setItem(row_number, 1, QtWidgets.QTableWidgetItem(str(job.username)))
            self.tableWidgetJobs.setItem(row_number, 2, QtWidgets.QTableWidgetItem(str(job.shipper_name)))
            self.tableWidgetJobs.setItem(row_number, 3, QtWidgets.QTableWidgetItem(str(job.broker_name)))
            # self.tableWidgetJobs.setItem(row_number, 4, QtWidgets.QTableWidgetItem(str(datetime.date.strftime(job.start_date, "%m/%d/%y"))))
            self.tableWidgetJobs.setItem(row_number, 4, QtWidgets.QTableWidgetItem(str(dt)))
            self.tableWidgetJobs.setItem(row_number, 5, QtWidgets.QTableWidgetItem(str(job.origin)))
            self.tableWidgetJobs.setItem(row_number, 6, QtWidgets.QTableWidgetItem(str(job.destination)))
            self.tableWidgetJobs.setItem(row_number, 7, QtWidgets.QTableWidgetItem(str(job.status.upper())))
        return


    def change_data(self):
        item = self.tableWidgetJobs.selectedItems()

        if len(item) == 0:
            return
        else:
            job_id = int(item[0].text())
            index = self.spinBoxShipper.findText(item[2].text(), QtCore.Qt.MatchFixedString)
            if index >= 0:
                self.spinBoxShipper.setCurrentIndex(index)
            index = self.spinBoxUsername.findText(item[1].text(), QtCore.Qt.MatchFixedString)
            if index >= 0:
                self.spinBoxUsername.setCurrentIndex(index)

            self.selected_job = self.database.get_current_job_by_id(job_id)
            # print(self.selected_job.status)
            if self.selected_job.status.lower() in ['pending', 'accepted']:
                self.spinBoxUsername.setEnabled(False)
                self.spinBoxUsername.setStyleSheet("background-color: #dddddd; selection-background-color: #dddddd; text-align: left; color: rgb(0, 0, 0);")
            else:
                self.spinBoxUsername.setEnabled(True)
                self.spinBoxUsername.setStyleSheet("background-color: #ffffff; selection-background-color: #4199D8; text-align: left; color: rgb(0, 0, 0);")
            self.lineEditRate.setText(str(self.selected_job.rate))
            self.textEditOriginAddress.setText(self.selected_job.origin)
            self.textEditDestinationAddress.setText(self.selected_job.destination)
            self.textEditComments.setText(self.selected_job.comments)
            self.dateEdit.setDate(QtCore.QDate(self.selected_job.start_date))
            time = str(self.selected_job.start_time).split(':')
            self.timeEditStartTime.setTime(QtCore.QTime(float(time[0]), float(time[1])))

            index = self.spinBoxRate.findText(self.selected_job.pay_type, QtCore.Qt.MatchFixedString)
            if index >= 0:
                self.spinBoxRate.setCurrentIndex(index)
            index = self.spinBoxBroker.findText(self.selected_job.broker_name, QtCore.Qt.MatchFixedString)
            if index >=0:
                self.spinBoxBroker.setCurrentIndex(index)
    def clear_form_add_job(self):
        self.tableWidgetJobs.setSortingEnabled(False)
        self.database.refresh()
        self.update_jobs_list()
        self.tableWidgetJobs.setSortingEnabled(True)
        self.lineEditRate.setText("")
        self.textEditOriginAddress.setText("")
        self.textEditDestinationAddress.setText("")
        self.textEditComments.setText("")
        self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.tableWidgetJobs.clearSelection()
        self.labelError.setText("")
        self.spinBoxRate.setCurrentIndex(0)
        self.spinBoxBroker.setCurrentIndex(0)
        self.spinBoxShipper.setCurrentIndex(0)
        self.spinBoxUsername.setCurrentIndex(0)
        self.spinBoxUsername.setEnabled(True)
        self.spinBoxUsername.setStyleSheet("background-color: #ffffff; selection-background-color: #4199D8; text-align: left; color: rgb(0, 0, 0);")

    def add_job(self):
        temp = self.dateEdit.date()
        date = temp.toPyDate()
        temp_2 = self.timeEditStartTime.time()
        time = temp_2.toPyTime()
        shipper_name = self.spinBoxShipper.currentText()
        broker_name = self.spinBoxBroker.currentText()
        username = self.spinBoxUsername.currentText()
        rate = self.lineEditRate.text()
        rate_type = self.spinBoxRate.currentText()
        origin = self.textEditOriginAddress.toPlainText()
        destination = self.textEditDestinationAddress.toPlainText()
        comments = self.textEditComments.toPlainText()

        self.database.add_job(shipper_name, broker_name, username, date, time, rate_type, rate, origin, destination, comments)
        self.update_jobs_list()
        self.clear_form_add_job()

    def delete_job(self):
        item = self.tableWidgetJobs.selectedItems()
        if len(item) == 0:
            self.labelError.setText("ERROR PLEASE SELECT JOB TO DELETE!")
        else:
            confirm = self.showdialog()
            if confirm:
                self.database.delete_job(self.selected_job.job_id)
                self.clear_form_add_job()
                self.update_jobs_list()
                return
            else:
                return

    def edit_job(self):
        item = self.tableWidgetJobs.selectedItems()
        if len(item) == 0:
            self.labelError.setText("ERROR PLEASE SELECT JOB TO EDIT!")
        else:
            confirm = self.showdialog()
            if confirm:
                temp = self.dateEdit.date()
                date = temp.toPyDate()
                temp_2 = self.timeEditStartTime.time()
                time = temp_2.toPyTime()
                shipper_name = self.spinBoxShipper.currentText()
                broker_name = self.spinBoxBroker.currentText()
                username = self.spinBoxUsername.currentText()
                rate = self.lineEditRate.text()
                rate_type = self.spinBoxRate.currentText()
                origin = self.textEditOriginAddress.toPlainText()
                destination = self.textEditDestinationAddress.toPlainText()
                comments = self.textEditComments.toPlainText()

                self.database.edit_job(shipper_name, broker_name ,username, date, time, rate_type, rate, origin, destination,
                                      comments, self.selected_job.job_id)
                self.update_jobs_list()
                self.clear_form_add_job()
                return
            else:
                return

    def showdialog(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)

        msg.setText("Make Changes?")
        msg.setInformativeText("The action CANNOT be undone!")
        msg.setWindowTitle("Confirmation")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        retval = msg.exec_()

        if retval == QMessageBox.Yes:
            return True
        else:
            return False

    def setupUiGenerate(self, AddShipper):
        AddShipper.setObjectName("AddShipper")
        AddShipper.resize(809, 633)
        AddShipper.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(AddShipper)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 20, 331, 51))
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setStyleSheet('QLabel {color: #124E78;}')

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(170, 80, 461, 491))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 101, 21))
        self.label_2.setObjectName("label_2")
        # submitted by

        # self.label_6 = QtWidgets.QLabel(self.groupBox)
        # self.label_6.setGeometry(QtCore.QRect(10, 130, 141, 21))
        # self.label_6.setObjectName("label_6")
        #
        # self.textEditSubmitName = QtWidgets.QLineEdit(self.groupBox)
        # self.textEditSubmitName.setGeometry(QtCore.QRect(110, 130, 341, 21))
        # self.textEditSubmitName.setObjectName("textEditSubmitName")

        self.pushButtonGenerateInvoice = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonGenerateInvoice.setGeometry(QtCore.QRect(160, 230, 131, 32))
        self.pushButtonGenerateInvoice.setStyleSheet("background-color: rgb(40, 195, 50);")
        self.pushButtonGenerateInvoice.setObjectName("pushButtonGenerateInvoice")
        self.pushButtonGenerateInvoice.clicked.connect(self.generate_invoice)

        self.spinBoxBroker = QtWidgets.QComboBox(self.groupBox)
        self.spinBoxBroker.setGeometry(QtCore.QRect(110, 10, 341, 22))
        self.spinBoxBroker.setObjectName("spinBoxBroker")
        self.brokername_list = self.database.get_brokernames()
        self.spinBoxBroker.setStyleSheet(
            "background-color: rgb(255, 255, 255); selection-background-color: #4199D8; text-align: left; color: rgb(0, 0, 0);")
        self.spinBoxBroker.addItems(self.brokername_list)

        self.dateEditTo = QtWidgets.QDateEdit(self.groupBox)
        self.dateEditTo.setGeometry(QtCore.QRect(110, 70, 110, 22))
        self.dateEditTo.setObjectName("dateEditTo")
        self.dateEditTo.setDateTime(QtCore.QDateTime.currentDateTime())

        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(10, 70, 71, 21))
        self.label_7.setObjectName("label_7")
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(10, 40, 71, 21))
        self.label_13.setObjectName("label_13")
        self.dateEditFrom = QtWidgets.QDateEdit(self.groupBox)
        self.dateEditFrom.setGeometry(QtCore.QRect(110, 40, 110, 22))
        self.dateEditFrom.setObjectName("dateEditFrom")
        self.dateEditFrom.setDateTime(QtCore.QDateTime.currentDateTime())

        self.label_23 = QtWidgets.QLabel(self.groupBox)
        self.label_23.setGeometry(QtCore.QRect(10, 130, 141, 21))
        self.label_23.setObjectName("label_23")

        self.textEditFileName = QtWidgets.QLineEdit(self.groupBox)
        self.textEditFileName.setGeometry(QtCore.QRect(110, 130, 341, 21))
        self.textEditFileName.setObjectName("textEditFileName")

        self.labelError = QtWidgets.QLabel(self.groupBox)
        self.labelError.setGeometry(QtCore.QRect(20, 200, 421, 21))
        self.labelError.setText("")
        self.labelError.setObjectName("labelError")
        self.labelError.setStyleSheet('QLabel {color: #990000;}')
        self.labelError.setAlignment(QtCore.Qt.AlignCenter)

        self.dateEditTo_2 = QtWidgets.QDateEdit(self.groupBox)
        self.dateEditTo_2.setGeometry(QtCore.QRect(110, 350, 110, 22))
        self.dateEditTo_2.setObjectName("dateEditTo_2")
        self.dateEditTo_2.setDateTime(QtCore.QDateTime.currentDateTime())

        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setGeometry(QtCore.QRect(10, 320, 71, 21))
        self.label_14.setObjectName("label_14")

        self.spinBoxDriverName = QtWidgets.QComboBox(self.groupBox)
        self.spinBoxDriverName.setGeometry(QtCore.QRect(110, 290, 341, 22))
        self.spinBoxDriverName.setObjectName("spinBoxDriverName")
        self.drivername_list = self.database.get_usernames()
        self.spinBoxDriverName.setStyleSheet(
            "background-color: rgb(255, 255, 255); selection-background-color: #4199D8; text-align: left; color: rgb(0, 0, 0);")
        self.spinBoxDriverName.addItems(self.drivername_list)

        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 290, 91, 21))
        self.label_3.setObjectName("label_3")

        self.textEditFileName_2 = QtWidgets.QLineEdit(self.groupBox)
        self.textEditFileName_2.setGeometry(QtCore.QRect(110, 380, 341, 21))
        self.textEditFileName_2.setObjectName("textEditFileName_2")

        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(10, 350, 71, 21))
        self.label_8.setObjectName("label_8")

        self.label_24 = QtWidgets.QLabel(self.groupBox)
        self.label_24.setGeometry(QtCore.QRect(10, 380, 91, 21))
        self.label_24.setObjectName("label_24")

        self.dateEditFrom_2 = QtWidgets.QDateEdit(self.groupBox)
        self.dateEditFrom_2.setGeometry(QtCore.QRect(110, 320, 110, 22))
        self.dateEditFrom_2.setObjectName("dateEditFrom_2")
        self.dateEditFrom_2.setDateTime(QtCore.QDateTime.currentDateTime())

        self.labelError_2 = QtWidgets.QLabel(self.groupBox)
        self.labelError_2.setGeometry(QtCore.QRect(20, 420, 421, 21))
        self.labelError_2.setText("")
        self.labelError_2.setObjectName("labelError_2")
        self.labelError_2.setStyleSheet('QLabel {color: #990000;}')
        self.labelError_2.setAlignment(QtCore.Qt.AlignCenter)

        self.pushButtonGenerateDriver = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonGenerateDriver.setGeometry(QtCore.QRect(160, 450, 131, 32))
        self.pushButtonGenerateDriver.setStyleSheet("background-color: rgb(40, 195, 50);")
        self.pushButtonGenerateDriver.setObjectName("pushButtonGenerateDriver")
        self.pushButtonGenerateDriver.clicked.connect(self.generate_driver_log)

        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 91, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(110, 100, 16, 21))
        self.label_5.setObjectName("label_5")
        self.lineEditRate = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditRate.setGeometry(QtCore.QRect(130, 100, 71, 21))
        self.lineEditRate.setObjectName("lineEditRate")

        self.pushButtonHome = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonHome.setGeometry(QtCore.QRect(720, 20, 50, 50))
        self.pushButtonHome.setIcon(
            QtGui.QIcon(self.resource_path("144x144.png")))
        self.pushButtonHome.setStyleSheet("border-radius: 3px;")
        self.pushButtonHome.setIconSize(QtCore.QSize(45, 45))
        self.pushButtonHome.setText("")
        self.pushButtonHome.setObjectName("pushButtonHome")
        self.pushButtonHome.clicked.connect(self.show_home)


        AddShipper.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AddShipper)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 809, 22))
        self.menubar.setObjectName("menubar")
        AddShipper.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AddShipper)
        self.statusbar.setObjectName("statusbar")
        AddShipper.setStatusBar(self.statusbar)

        self.retranslateUiGenerate(AddShipper)
        QtCore.QMetaObject.connectSlotsByName(AddShipper)

    def clear_form(self):
        self.database.refresh()
        self.textEditFileName.setText("")
        # self.textEditSubmitName.setText("")
        self.labelError.setText("")
        self.textEditFileName_2.setText("")
        self.labelError_2.setText("")
        self.lineEditRate.setText("")

    def generate_driver_log(self):
        filename = self.textEditFileName_2.text()
        if filename == "":
            self.labelError_2.setText("Error: Please enter file name")
        else:
            temp = self.dateEditFrom_2.date()
            date_from = temp.toPyDate()
            temp2 = self.dateEditTo_2.date()
            date_to = temp2.toPyDate()
            driver_name = self.spinBoxDriverName.currentText()
            data = self.database.get_driver_logs(driver_name, date_from, date_to)

            filename += ".xlsx"
            xls_dest = os.path.realpath(os.path.dirname(sys.argv[0]))
            xls_dest += "/excel_files/"
            if not os.path.exists(xls_dest):
                os.makedirs(xls_dest)
            xls_dest += filename
            # workbook = xlsxwriter.Workbook("/Users/marcyp/Desktop/Website_Info/Dashboard/" + filename)

            # workbook = xlsxwriter.Workbook(self.resource_path(filename))
            workbook = xlsxwriter.Workbook(xls_dest)
            worksheet = workbook.add_worksheet()

            header_format = workbook.add_format()
            header_format.set_bold()
            header_format.set_align('left')
            header_format.set_font_size(21)
            header_format.set_bg_color('#a1a7af')

            money = workbook.add_format({'num_format': '$0.00'})

            worksheet.merge_range('A1:E1', 'Pullin\' Freight, LLC', header_format)

            title_format = workbook.add_format()
            title_format.set_bold()
            title_format.set_align('left')
            title_format.set_font_size(15)

            worksheet.write('A2:C2', 'Driver Log For:  {}'.format(driver_name.capitalize()), title_format)
            worksheet.write('A3:C3', 'Rate:', title_format)
            worksheet.write('B3', 20, money)

            title_format_2 = workbook.add_format()
            title_format_2.set_bold()
            title_format_2.set_align('right')
            title_format_2.set_font_size(13)
            title_format_2.set_bg_color('#a1a7af')

            worksheet.merge_range('F1:J1', 'Log from: {} to: {}'.format(str(date_from), str(date_to)),
                                  title_format_2)

            row = 3
            col = 0

            table_title_format = workbook.add_format()
            table_title_format.set_bold()
            table_title_format.set_color('#6d6d6d')
            table_title_format.set_align('center')
            table_title_format.set_font_size(13)

            worksheet.write(row, col, 'Date', table_title_format)
            worksheet.write(row, col + 1, 'Invoice #', table_title_format)
            worksheet.write(row, col + 2, 'Shipper', table_title_format)
            worksheet.write(row, col + 3, 'Origin', table_title_format)
            worksheet.write(row, col + 4, 'Destination', table_title_format)
            worksheet.write(row, col + 5, 'Hours', table_title_format)
            worksheet.write(row, col + 6, 'Sub-Total', table_title_format)

            table_content_even = workbook.add_format()
            table_content_even.set_bg_color('#dbdbdb')
            table_content_even.set_font_size(11)

            table_content_odd = workbook.add_format()
            table_content_odd.set_bg_color('#ffffff')
            table_content_odd.set_font_size(11)

            table_content_even_money = workbook.add_format()
            table_content_even_money.set_bg_color('#dbdbdb')
            table_content_even_money.set_font_size(11)
            table_content_even_money.set_num_format('$0.00')

            table_content_odd_money = workbook.add_format()
            table_content_odd_money.set_bg_color('#ffffff')
            table_content_odd_money.set_font_size(11)
            table_content_odd_money.set_num_format('$0.00')

            row = 4
            theme = table_content_even
            money = table_content_even_money

            for bol in data:
                if row %2 == 0:
                    theme = table_content_even
                    money = table_content_even_money
                else:
                    theme = table_content_odd
                    money = table_content_odd_money
                # if bol.rate_type == "Per Hour":
                #     selected_payment = bol.hours_worked
                # if bol.rate_type == "Per Load":
                #     selected_payment = bol.hours_worked

                row_excel = row+1

                worksheet.write(row, col, str(bol.date), theme)
                print(str(bol.date))
                worksheet.write(row, col + 1, bol.bill_number, theme)
                worksheet.write(row, col + 2, bol.shipper_name, theme)
                worksheet.write(row, col + 3, bol.origin, theme)
                worksheet.write(row, col + 4, bol.destination, theme)
                worksheet.write(row, col + 5, bol.hours_loads, theme)
                worksheet.write(row, col + 6, '=B3*F{}'.format(row_excel), money)
                row += 1

            total = workbook.add_format()
            total.set_bold()
            total.set_num_format('$0.00')
            total.set_font_size(12)
            row_excel = row + 1
            worksheet.write(row, 6, '=SUM(G5:G{})'.format(row),total)
            worksheet.write(row, 5, '=SUM(F5:F{})'.format(row))
            worksheet.write(row,3, 'Grand Total:',total)

            end = workbook.add_format()
            end.set_bg_color('#319e3b')
            row += 1
            row_excel = row + 1
            worksheet.merge_range('A{}:G{}'.format(row_excel, row_excel), '', end)

            workbook.close()
            self.clear_form()

    def generate_invoice(self):
        filename = self.textEditFileName.text()
        # submitter = self.textEditSubmitName.text()
        rate = self.lineEditRate.text()

        print(filename)

        if filename == "" or rate == "":
            self.labelError.setText("Error: Please fill out all fields")
        else:
            temp = self.dateEditFrom.date()
            date_from = temp.toPyDate()
            temp2 = self.dateEditTo.date()
            date_to = temp2.toPyDate()
            broker_name = self.spinBoxBroker.currentText()
            broker_data = self.database.get_broker_by_name(broker_name)
            data = self.database.get_bol_invoiced(broker_name, date_from, date_to)
            rate = float(rate)/100
            print(broker_data)

            filename += ".xlsx"
            # workbook = xlsxwriter.Workbook("/Users/marcyp/Desktop/Website_Info/Dashboard/" + filename)
            xls_dest = os.path.realpath(os.path.dirname(sys.argv[0]))
            xls_dest += "/excel_files/"
            if not os.path.exists(xls_dest):
                os.makedirs(xls_dest)
            xls_dest += filename
            workbook = xlsxwriter.Workbook(xls_dest)
            worksheet = workbook.add_worksheet()

            money = workbook.add_format({'num_format': '$#,###.#0'})

            header_format = workbook.add_format()
            header_format.set_bold()
            header_format.set_align('left')
            header_format.set_font_size(21)
            header_format.set_bg_color('#a1a7af')

            worksheet.merge_range('A1:E1', 'Pullin\' Freight, LLC', header_format)


            title_format = workbook.add_format()
            title_format.set_bold()
            title_format.set_align('left')
            title_format.set_font_size(15)

            worksheet.merge_range('A2:B2','Billed to:', title_format)
            worksheet.merge_range('C2:K2',broker_data.name,title_format)
            worksheet.merge_range('A3:B3', 'Address:', title_format)
            worksheet.merge_range('C3:K3',broker_data.address,title_format)

            title_format_2 = workbook.add_format()
            title_format_2.set_bold()
            title_format_2.set_align('right')
            title_format_2.set_font_size(13)
            title_format_2.set_bg_color('#a1a7af')

            worksheet.merge_range('F1:J1', 'Invoice from: {} to: {}'.format(str(date_from), str(date_to)), title_format_2)

            row = 3
            col = 0

            table_title_format = workbook.add_format()
            table_title_format.set_bold()
            table_title_format.set_color('#6d6d6d')
            table_title_format.set_align('center')
            table_title_format.set_font_size(13)

            worksheet.write(row, col, 'Date',table_title_format)
            worksheet.write(row, col + 1, 'Invoice #',table_title_format)
            worksheet.write(row, col + 2, 'Shipper',table_title_format)
            worksheet.write(row, col + 3, 'Origin',table_title_format)
            worksheet.write(row, col + 4, 'Destination',table_title_format)
            worksheet.write(row, col + 5, 'work type',table_title_format)
            worksheet.write(row, col + 6, 'Loads/Hours',table_title_format)
            worksheet.write(row, col + 7, 'Rate',table_title_format)
            worksheet.write(row, col + 8, 'Sub-Total',table_title_format)
            worksheet.write(row, col + 9, '-{}% Broker Fee'.format(rate*100),table_title_format)
            worksheet.write(row, col + 10, 'Total',table_title_format)

            table_content_even = workbook.add_format()
            table_content_even.set_bg_color('#dbdbdb')
            table_content_even.set_font_size(11)

            table_content_odd = workbook.add_format()
            table_content_odd.set_bg_color('#ffffff')
            table_content_odd.set_font_size(11)

            table_content_even_money = workbook.add_format()
            table_content_even_money.set_bg_color('#dbdbdb')
            table_content_even_money.set_font_size(11)
            table_content_even_money.set_num_format('$0.00')

            table_content_odd_money = workbook.add_format()
            table_content_odd_money.set_bg_color('#ffffff')
            table_content_odd_money.set_font_size(11)
            table_content_odd_money.set_num_format('$0.00')

            row = 4
            theme = table_content_even
            money = table_content_even_money
            # Iterate over the data and write it out row by row.
            for bol in data:
                if row %2 == 0:
                    theme = table_content_even
                    money = table_content_even_money
                else:
                    theme = table_content_odd
                    money = table_content_odd_money
                # if bol.rate_type == "Per Hour":
                #     selected_payment = bol.hours_loads
                # if bol.rate_type == "Per Load":
                #     selected_payment = bol.loads

                row_excel = row+1

                worksheet.write(row, col, str(bol.date), theme)
                print(str(bol.date))
                worksheet.write(row, col + 1, bol.bill_number, theme)
                worksheet.write(row, col + 2, bol.shipper_name, theme)
                worksheet.write(row, col + 3, bol.origin, theme)
                worksheet.write(row, col + 4, bol.destination, theme)
                worksheet.write(row, col + 5, bol.rate_type, theme)
                worksheet.write(row, col + 6, bol.hours_loads, theme)
                worksheet.write(row, col + 7, bol.rate, money)
                worksheet.write(row, col + 8, '=G{}*H{}'.format(row_excel, row_excel),money)
                worksheet.write(row, col+9, '=I{}*{}'.format(row_excel, rate),money)
                worksheet.write(row, col + 10, '=I{}-J{}'.format(row_excel, row_excel),money)
                row += 1

            total = workbook.add_format()
            total.set_bold()
            total.set_num_format('$0.00')
            total.set_font_size(12)
            total.set_align('right')

            row_excel = row + 1
            worksheet.write(row, 10, '=SUM(I5:I{})'.format(row),total)
            worksheet.merge_range('I{}:J{}'.format(row_excel, row_excel), 'Sub Total:',total)
            row += 1
            row_excel = row + 1
            worksheet.write(row, 10, '=SUM(J5:J{})'.format(row-1),total)
            worksheet.merge_range('I{}:J{}'.format(row_excel, row_excel), '-{}% Broker Fee'.format(rate*100),total)
            row += 1
            row_excel = row + 1
            worksheet.write(row, 10, '=SUM(K5:K{})'.format(row-2) ,total)
            worksheet.merge_range('I{}:J{}'.format(row_excel, row_excel), 'Grand Total:',total)
            row += 2
            row_excel = row + 1
            worksheet.merge_range('A{}:K{}'.format(row_excel, row_excel), 'Submitted: {} by '.format(str(datetime.date.today())))

            end = workbook.add_format()
            end.set_bg_color('#319e3b')
            row += 1
            row_excel = row + 1
            worksheet.merge_range('A{}:K{}'.format(row_excel, row_excel), '', end)

            workbook.close()
            self.clear_form()

    def retranslateUiGenerate(self, AddShipper):
        _translate = QtCore.QCoreApplication.translate
        AddShipper.setWindowTitle(_translate("AddShipper", "MainWindow"))
        self.label.setText(_translate("AddShipper", "GENERATE LOGS"))
        self.label_2.setText(_translate("AddShipper", "Broker Name:"))
        # self.label_6.setText(_translate("AddShipper", "Submitted By:"))
        self.pushButtonGenerateInvoice.setText(_translate("AddShipper", "Generate Invoice"))
        self.label_7.setText(_translate("AddShipper", "To Date:"))
        self.label_13.setText(_translate("AddShipper", "From Date:"))
        self.label_23.setText(_translate("AddShipper", "File Name:"))
        self.label_14.setText(_translate("AddShipper", "From Date:"))
        self.label_3.setText(_translate("AddShipper", "Driver Name:"))
        self.label_8.setText(_translate("AddShipper", "To Date:"))
        self.label_24.setText(_translate("AddShipper", "File Name:"))
        self.pushButtonGenerateDriver.setText(_translate("AddShipper", "Generate Driver Log"))
        self.label_4.setText(_translate("AddShipper", "Brokerage"))
        self.label_5.setText(_translate("AddShipper", "%"))

    def setupUiAddShipper(self, AddShipper):
        AddShipper.setObjectName("AddShipper")
        AddShipper.resize(800, 600)
        AddShipper.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(AddShipper)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 10, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(False)
        font.setWeight(50)

        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setStyleSheet('QLabel {color: #124E78;}')

        self.listWidgetShippers = QtWidgets.QListWidget(self.centralwidget)
        self.listWidgetShippers.setGeometry(QtCore.QRect(40, 80, 261, 451))
        self.listWidgetShippers.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.listWidgetShippers.setObjectName("listWidgetShippers")
        self.listWidgetShippers.itemSelectionChanged.connect(self.change_data_add_shipper)

        self.update_shipper_list()

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(320, 80, 471, 441))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.lineEditShipperName = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditShipperName.setGeometry(QtCore.QRect(10, 30, 441, 51))
        self.lineEditShipperName.setObjectName("lineEditShipperName")

        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 101, 16))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 111, 16))
        self.label_3.setObjectName("label_3")

        self.textEditShipperAddress = QtWidgets.QTextEdit(self.groupBox)
        self.textEditShipperAddress.setGeometry(QtCore.QRect(10, 110, 441, 51))
        self.textEditShipperAddress.setObjectName("textEditShipperAddress")

        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 170, 101, 16))
        self.label_4.setObjectName("label_4")

        self.textEditComments = QtWidgets.QTextEdit(self.groupBox)
        self.textEditComments.setGeometry(QtCore.QRect(10, 190, 441, 151))
        self.textEditComments.setObjectName("textEditComments")

        self.pushButtonAddShipper = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonAddShipper.setGeometry(QtCore.QRect(340, 405, 101, 32))
        self.pushButtonAddShipper.setStyleSheet("background-color: rgb(40, 195, 50);")
        self.pushButtonAddShipper.setObjectName("pushButtonAddShipper")
        self.pushButtonAddShipper.clicked.connect(self.add_shipper)

        self.pushButtonEditShipper = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonEditShipper.setGeometry(QtCore.QRect(230, 405, 101, 32))
        self.pushButtonEditShipper.setStyleSheet("background-color: rgb(255, 193, 44);")
        self.pushButtonEditShipper.setObjectName("pushButtonEditShipper")
        self.pushButtonEditShipper.clicked.connect(self.edit_shipper)

        self.pushButtonDeleteShipper = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonDeleteShipper.setGeometry(QtCore.QRect(120, 405, 101, 32))
        self.pushButtonDeleteShipper.setStyleSheet("background-color: rgb(253, 70, 70);")
        self.pushButtonDeleteShipper.setObjectName("pushButtonDeleteShipper")
        self.pushButtonDeleteShipper.clicked.connect(self.delete_shipper)

        self.pushButtonClearForm = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonClearForm.setGeometry(QtCore.QRect(10, 405, 101, 32))
        self.pushButtonClearForm.setStyleSheet("background-color: rgb(122, 122, 122);")
        self.pushButtonClearForm.setObjectName("pushButtonClearForm")
        self.pushButtonClearForm.clicked.connect(self.clear_data_add_shipper)

        # self.lineEditBrokerName = QtWidgets.QLineEdit(self.groupBox)
        # self.lineEditBrokerName.setGeometry(QtCore.QRect(10, 80, 441, 21))
        # self.lineEditBrokerName.setObjectName("lineEditBrokerName")
        # self.label_7 = QtWidgets.QLabel(self.groupBox)
        # self.label_7.setGeometry(QtCore.QRect(10, 55, 101, 21))
        # self.label_7.setObjectName("label_7")
        self.labelError = QtWidgets.QLabel(self.centralwidget)
        self.labelError.setGeometry(QtCore.QRect(340, 520, 421, 21))
        self.labelError.setText("")

        self.labelError.setObjectName("labelError")
        self.labelError.setStyleSheet('QLabel {color: #990000;}')

        self.pushButtonHome = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonHome.setGeometry(QtCore.QRect(720, 20, 50, 50))
        self.pushButtonHome.setIcon(QtGui.QIcon(self.resource_path("144x144.png")))
        self.pushButtonHome.setStyleSheet("border-radius: 3px;")
        self.pushButtonHome.setIconSize(QtCore.QSize(45,45))
        self.pushButtonHome.setText("")
        self.pushButtonHome.setObjectName("pushButtonHome")
        self.pushButtonHome.clicked.connect(self.show_home)

        AddShipper.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AddShipper)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        AddShipper.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AddShipper)
        self.statusbar.setObjectName("statusbar")
        AddShipper.setStatusBar(self.statusbar)

        self.retranslateUiAddShipper(AddShipper)
        QtCore.QMetaObject.connectSlotsByName(AddShipper)

    def retranslateUiAddShipper(self, AddShipper):
        _translate = QtCore.QCoreApplication.translate
        AddShipper.setWindowTitle(_translate("AddShipper", "MainWindow"))
        self.label.setText(_translate("AddShipper", "ADD SHIPPER"))
        self.label_2.setText(_translate("AddShipper", "Shipper Name:"))
        self.label_3.setText(_translate("AddShipper", "Shipper Address:"))
        self.label_4.setText(_translate("AddShipper", "Comments:"))
        self.pushButtonAddShipper.setText(_translate("AddShipper", "Add Shipper"))
        self.pushButtonEditShipper.setText(_translate("AddShipper", "Edit Shipper"))
        self.pushButtonDeleteShipper.setText(_translate("AddShipper", "Delete Shipper"))
        self.pushButtonClearForm.setText(_translate("AddShipper","Clear Form"))
        # self.label_7.setText(_translate("AddShipper", "Broker Name:"))

    def update_shipper_list(self):
        self.listWidgetShippers.clear()
        shipper_list = self.database.get_shippers()
        for shipper in shipper_list:
            shipper_description = "{} - {} - {}".format(shipper.shipper_id, shipper.name, shipper.address)
            self.listWidgetShippers.addItem(shipper_description)

    def change_data_add_shipper(self):
        item = self.listWidgetShippers.selectedItems()
        if len(item) == 0:
            return
        else:
            list = item[0].text().split()
            shipper = self.database.get_shipper(list[0])
            self.lineEditShipperName.setText(shipper.name)
            #self.lineEditBrokerName.setText(shipper.broker_name)
            self.textEditShipperAddress.setText(shipper.address)
            self.textEditComments.setText(shipper.comments)

    def clear_data_add_shipper(self):
        self.database.refresh()
        self.update_shipper_list()
        self.listWidgetShippers.clearSelection()
        self.lineEditShipperName.setText("")
        #self.lineEditBrokerName.setText("")
        self.textEditShipperAddress.setText("")
        self.textEditComments.setText("")
        self.labelError.setText("")

    def edit_shipper(self):
        item = self.listWidgetShippers.selectedItems()
        if len(item) == 0:
            self.labelError.setText("ERROR PLEASE SELECT SHIPPER TO EDIT!")
        else:
            confirm = self.showdialog()
            if confirm:
                list = item[0].text().split()
                shipper_id = list[0]

                name = self.lineEditShipperName.text()
                #broker_name = self.lineEditBrokerName.text()
                address = str(self.textEditShipperAddress.toPlainText())
                origin = ""
                destination = ""
                comments = str(self.textEditComments.toPlainText())
                self.database.update_shipper(shipper_id,name, address,origin,destination,comments)
                self.update_shipper_list()
                self.clear_data_add_shipper()
                return
            else:
                return

    def delete_shipper(self):
        item = self.listWidgetShippers.selectedItems()
        if len(item) == 0:
            self.labelError.setText("ERROR PLEASE SELECT SHIPPER TO DELETE!")
        else:
            confirm = self.showdialog()
            if confirm:
                list = item[0].text().split()
                shipper_id = list[0]

                self.database.delete_shipper(shipper_id)
                self.update_shipper_list()
                self.clear_data_add_shipper()
                return
            else:
                return

    def add_shipper(self):
        name = self.lineEditShipperName.text()
        # broker_name = self.lineEditBrokerName.text()
        address = str(self.textEditShipperAddress.toPlainText())
        origin = ""
        destination = ""
        comments = str(self.textEditComments.toPlainText())

        if (name == ""):
            self.labelError.setText("Error: Name Cannot be blank!")
            return
        if (address == ""):
            self.labelError.setText("Error: Address Cannot be blank")
            return

        self.database.add_shipper(name, address,origin,destination,comments)
        self.update_shipper_list()
        self.clear_data_add_shipper()
        return


    def setupUiBOL(self, Bill_of_Lading):
        Bill_of_Lading.setObjectName("Bill_of_Lading")
        Bill_of_Lading.resize(809, 633)
        Bill_of_Lading.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(Bill_of_Lading)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 10, 281, 51))

        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setStyleSheet('QLabel {color: #124E78;}')
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 320, 741, 261))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 101, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 40, 81, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(310, 130, 101, 16))
        self.label_4.setObjectName("label_4")
        self.textEditOriginAddress = QtWidgets.QTextEdit(self.groupBox)
        self.textEditOriginAddress.setGeometry(QtCore.QRect(420, 130, 301, 21))
        self.textEditOriginAddress.setObjectName("textEditOriginAddress")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(310, 160, 101, 16))
        self.label_5.setObjectName("label_5")
        self.textEditDestinationAddress = QtWidgets.QTextEdit(self.groupBox)
        self.textEditDestinationAddress.setGeometry(QtCore.QRect(420, 160, 301, 21))
        self.textEditDestinationAddress.setObjectName("textEditDestinationAddress")




        self.pushButtonAddJob = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonAddJob.setGeometry(QtCore.QRect(500, 220, 114, 32))
        self.pushButtonAddJob.setStyleSheet("background-color: rgb(40, 195, 50);")
        self.pushButtonAddJob.setObjectName("pushButtonAddJob")
        self.pushButtonAddJob.clicked.connect(self.add_bol)

        self.pushButtonEditJob = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonEditJob.setGeometry(QtCore.QRect(380, 220, 114, 32))
        self.pushButtonEditJob.setStyleSheet("background-color: rgb(255, 193, 44);")
        self.pushButtonEditJob.setObjectName("pushButtonEditJob")
        self.pushButtonEditJob.clicked.connect(self.edit_bol)

        self.pushButtonDeleteJob = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonDeleteJob.setGeometry(QtCore.QRect(260, 220, 114, 32))
        self.pushButtonDeleteJob.setStyleSheet("background-color: rgb(253, 70, 70);")
        self.pushButtonDeleteJob.setObjectName("pushButtonDeleteJob")
        self.pushButtonDeleteJob.clicked.connect(self.delete_bol)


        #Broker_name label
        self.spinBoxBroker = QtWidgets.QComboBox(self.groupBox)
        self.spinBoxBroker.setGeometry(QtCore.QRect(120, 160, 181, 22))
        self.spinBoxBroker.setObjectName("spinBoxBroker")
        self.brokername_list = self.database.get_brokernames()
        self.spinBoxBroker.setStyleSheet(
            "background-color: rgb(255, 255, 255); selection-background-color: #4199D8; text-align: left; color: rgb(0, 0, 0);")
        self.spinBoxBroker.addItems(self.brokername_list)

        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(20, 160, 101, 21))
        self.label_13.setObjectName("label_13")

        #shipper label
        self.spinBoxShipper = QtWidgets.QComboBox(self.groupBox)
        self.spinBoxShipper.setGeometry(QtCore.QRect(120, 10, 181, 22))
        self.spinBoxShipper.setObjectName("spinBoxShipper")
        self.shipername_list = self.database.get_shippernames()

        self.spinBoxShipper.setStyleSheet(
            "background-color: rgb(255, 255, 255); selection-background-color: #4199D8; text-align: left; color: rgb(0, 0, 0);")

        self.spinBoxShipper.addItems(self.shipername_list)

        self.dateEdit = QtWidgets.QDateEdit(self.groupBox)
        self.dateEdit.setGeometry(QtCore.QRect(120, 70, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())

        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(20, 70, 71, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(20, 100, 71, 21))
        self.label_8.setObjectName("label_8")

        self.timeEditStartTime = QtWidgets.QTimeEdit(self.groupBox)
        self.timeEditStartTime.setGeometry(QtCore.QRect(120, 100, 111, 22))
        self.timeEditStartTime.setObjectName("timeEditStartTime")

        self.timeEditEndTime = QtWidgets.QTimeEdit(self.groupBox)
        self.timeEditEndTime.setGeometry(QtCore.QRect(120, 130, 111, 22))
        self.timeEditEndTime.setObjectName("timeEditEndTime")


        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(20, 130, 71, 21))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(310, 40, 71, 21))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(420, 40, 16, 21))
        self.label_11.setObjectName("label_11")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(430, 40, 111, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(310, 100, 101, 21))
        self.label_12.setObjectName("label_12")
        self.lineEditBillNumber = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditBillNumber.setGeometry(QtCore.QRect(120, 40, 171, 21))
        self.lineEditBillNumber.setObjectName("lineEditBillNumber")
        self.lineEditLoads = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditLoads.setGeometry(QtCore.QRect(420, 100, 113, 21))
        self.lineEditLoads.setObjectName("lineEditLoads")

        self.labelError = QtWidgets.QLabel(self.groupBox)
        self.labelError.setGeometry(QtCore.QRect(180, 190, 421, 21))
        self.labelError.setText("")
        self.labelError.setObjectName("labelError")
        self.labelError.setStyleSheet('QLabel {color: #990000;}')

        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(310, 10, 81, 21))
        self.label_6.setObjectName("label_6")

        self.spinBoxUsername = QtWidgets.QComboBox(self.groupBox)
        self.spinBoxUsername.setGeometry(QtCore.QRect(420, 10, 301, 22))
        self.spinBoxUsername.setObjectName("spinBoxUsername")

        self.username_list = self.database.get_usernames()

        self.spinBoxUsername.addItems(self.username_list)

        self.spinBoxUsername.setStyleSheet(
            "background-color: rgb(255, 255, 255); selection-background-color: #4199D8; text-align: left; color: rgb(0, 0, 0);")
        #
        # self.label_13 = QtWidgets.QLabel(self.groupBox)
        # self.label_13.setGeometry(QtCore.QRect(20, 160, 91, 21))
        # self.label_13.setObjectName("label_13")
        # self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        # self.lineEdit_2.setGeometry(QtCore.QRect(120, 160, 101, 21))
        # self.lineEdit_2.setObjectName("lineEdit_2")

        self.pushButtonClearJob = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonClearJob.setGeometry(QtCore.QRect(140, 220, 114, 32))
        self.pushButtonClearJob.setStyleSheet("background-color: rgb(122, 122, 122);")
        self.pushButtonClearJob.setObjectName("pushButtonClearJob")
        self.pushButtonClearJob.clicked.connect(self.clear_form_BOL)

        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setGeometry(QtCore.QRect(310, 70, 71, 21))
        self.label_14.setObjectName("label_14")

        self.spinBoxRate = QtWidgets.QComboBox(self.groupBox)
        self.spinBoxRate.setGeometry(QtCore.QRect(420, 70, 111, 22))
        self.spinBoxRate.setObjectName("spinBoxRate")
        self.spinBoxRate.setObjectName("spinBoxRate")
        self.spinBoxRate.setStyleSheet(
            "background-color: rgb(255, 255, 255); selection-background-color: #4199D8; text-align: left; color: rgb(0, 0, 0);")
        self.spinBoxRate.addItem("Per Hour")
        self.spinBoxRate.addItem("Per Load")

        self.pushButtonHome = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonHome.setGeometry(QtCore.QRect(720, 20, 50, 50))
        self.pushButtonHome.setIcon(
            QtGui.QIcon(self.resource_path("144x144.png")))
        self.pushButtonHome.setStyleSheet("border-radius: 3px;")
        self.pushButtonHome.setIconSize(QtCore.QSize(45, 45))
        self.pushButtonHome.setText("")
        self.pushButtonHome.setObjectName("pushButtonHome")
        self.pushButtonHome.clicked.connect(self.show_home)

        self.tableWidgetBills = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidgetBills.setGeometry(QtCore.QRect(20, 70, 771, 251))
        self.tableWidgetBills.setObjectName("tableWidgetBills")
        self.tableWidgetBills.setColumnCount(13)
        self.tableWidgetBills.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.tableWidgetBills.itemSelectionChanged.connect(self.change_data_BOL)
        column_titles = ['id','broker_name', 'date', 'bill_number', 'shipper_name', 'username', 'rate_type',
                         'hours_loads','rate','origin', 'destination', 'start_time', 'end_time']
        counter = 0
        for title in column_titles:
            item = QtWidgets.QTableWidgetItem(title)
            item.setBackground(QtGui.QColor(211, 211, 211))
            self.tableWidgetBills.setHorizontalHeaderItem(counter, item)
            counter += 1
        self.update_bol_table()
        self.tableWidgetBills.setSortingEnabled(True)
        # self.tableWidgetBills.resizeRowsToContents()
        # self.tableWidgetBills.horizontalHeader().sortIndicatorChanged.connect(self.tableWidgetBills.resizeRowsToContents)
        self.tableWidgetBills.verticalHeader().setVisible(False)
        header = self.tableWidgetBills.resizeColumnToContents(0)

        Bill_of_Lading.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Bill_of_Lading)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 809, 22))
        self.menubar.setObjectName("menubar")
        Bill_of_Lading.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Bill_of_Lading)
        self.statusbar.setObjectName("statusbar")
        Bill_of_Lading.setStatusBar(self.statusbar)

        self.retranslateUiBOL(Bill_of_Lading)
        QtCore.QMetaObject.connectSlotsByName(Bill_of_Lading)

    def update_bol_table(self):
        for i in reversed(range(self.tableWidgetBills.rowCount())):
            self.tableWidgetBills.removeRow(i)

        bills_list = self.database.get_bols()

        for row_number in range(len(bills_list)):
            self.tableWidgetBills.insertRow(row_number)
            bill = bills_list[row_number]
            b = QtWidgets.QTableWidgetItem()
            b.setData(Qt.EditRole, QVariant(bill.bill_id))
            dt = datetime.datetime.strptime(str(bill.date), '%Y-%m-%d').strftime('%m/%d/%y')
            # self.tableWidgetBills.setItem(row_number, 0, QtWidgets.QTableWidgetItem(str(bill.bill_id)))
            self.tableWidgetBills.setItem(row_number, 0, b)
            self.tableWidgetBills.setItem(row_number, 1, QtWidgets.QTableWidgetItem(str(bill.broker_name)))
            self.tableWidgetBills.setItem(row_number, 2, QtWidgets.QTableWidgetItem(str(dt)))
            self.tableWidgetBills.setItem(row_number, 3, QtWidgets.QTableWidgetItem(str(bill.bill_number)))
            self.tableWidgetBills.setItem(row_number, 4, QtWidgets.QTableWidgetItem(str(bill.shipper_name)))
            self.tableWidgetBills.setItem(row_number, 5, QtWidgets.QTableWidgetItem(str(bill.user_name)))
            self.tableWidgetBills.setItem(row_number, 6, QtWidgets.QTableWidgetItem(str(bill.rate_type)))
            self.tableWidgetBills.setItem(row_number, 7, QtWidgets.QTableWidgetItem(str(bill.hours_loads)))
            self.tableWidgetBills.setItem(row_number, 8, QtWidgets.QTableWidgetItem(str(bill.rate)))
            self.tableWidgetBills.setItem(row_number, 9, QtWidgets.QTableWidgetItem(str(bill.origin)))
            self.tableWidgetBills.setItem(row_number, 10, QtWidgets.QTableWidgetItem(str(bill.destination)))
            self.tableWidgetBills.setItem(row_number, 11, QtWidgets.QTableWidgetItem(str(bill.start_time)))
            self.tableWidgetBills.setItem(row_number, 12, QtWidgets.QTableWidgetItem(str(bill.end_time)))
        return

    def change_data_BOL(self):
        item = self.tableWidgetBills.selectedItems()
        if len(item) == 0:
            return
        else:
            # Broker name
            index = self.spinBoxBroker.findText(str(item[1].text()), QtCore.Qt.MatchFixedString)
            if index >= 0:
                self.spinBoxBroker.setCurrentIndex(index)
            #date
            temp = (str(item[2].text())).split('/')
            self.dateEdit.setDate(QtCore.QDate(int(temp[0]), int(temp[1]), int(temp[2])))
            #bill nnumber
            self.lineEditBillNumber.setText(str(item[3].text()))
            # shipper name
            index = self.spinBoxShipper.findText(str(item[4].text()), QtCore.Qt.MatchFixedString)
            if index >= 0:
                self.spinBoxShipper.setCurrentIndex(index)
            # user name
            index = self.spinBoxUsername.findText(str(item[5].text()), QtCore.Qt.MatchFixedString)
            if index >= 0:
                self.spinBoxUsername.setCurrentIndex(index)
            # rate type
            index = self.spinBoxRate.findText(str(item[6].text()), QtCore.Qt.MatchFixedString)
            if index >= 0:
                self.spinBoxRate.setCurrentIndex(index)
            # hours/Loads
            self.lineEditLoads.setText(str(item[7].text()))
            # rate
            self.lineEdit.setText(str(item[8].text()))
            # self.lineEdit_2.setText(str(item[12].text()))
            # Origin Address
            self.textEditOriginAddress.setText(str(item[9].text()))
            # destination
            self.textEditDestinationAddress.setText(str(item[10].text()))
            # start time
            time = str(item[11].text()).split(':')
            self.timeEditStartTime.setTime(QtCore.QTime(float(time[0]), float(time[1])))
            #  end time
            time = str(item[12].text()).split(':')
            self.timeEditEndTime.setTime(QtCore.QTime(float(time[0]), float(time[1])))

            return

    def edit_bol(self):
        item = self.tableWidgetBills.selectedItems()
        if len(item) == 0:
            self.labelError.setText("ERROR PLEASE SELECT JOB TO EDIT!")
        else:
            confirm = self.showdialog()
            if confirm:
                temp = self.dateEdit.date()
                date = temp.toPyDate()
                temp_2 = self.timeEditStartTime.time()
                start_time = temp_2.toPyTime()
                temp_3 = self.timeEditEndTime.time()
                end_time = temp_3.toPyTime()
                broker_name = self.spinBoxBroker.currentText()
                shipper_name = self.spinBoxShipper.currentText()
                username = self.spinBoxUsername.currentText()
                rate_type = self.spinBoxRate.currentText()
                rate = self.lineEdit.text()
                # hours_worked = self.lineEdit_2.text()
                hours_loads = self.lineEditLoads.text()
                origin = self.textEditOriginAddress.toPlainText()
                destination = self.textEditDestinationAddress.toPlainText()
                bill_number = self.lineEditBillNumber.text()
                bill_id = item[0].text()

                self.database.edit_bol(bill_id, date, bill_number, broker_name, shipper_name, username, rate_type, origin, destination, start_time, end_time, hours_loads, rate)
                self.update_bol_table()
                self.clear_form_BOL()

    def clear_form_BOL(self):
        self.tableWidgetBills.setSortingEnabled(False)
        self.database.refresh()
        self.update_bol_table()
        self.tableWidgetBills.setSortingEnabled(True)
        self.tableWidgetBills.clearSelection()
        self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.lineEditBillNumber.setText("")
        self.lineEdit.setText("")
        self.textEditOriginAddress.setText("")
        self.textEditDestinationAddress.setText("")
        self.lineEditLoads.setText("")
        self.timeEditStartTime.setTime(QtCore.QTime.currentTime())
        self.timeEditEndTime.setTime(QtCore.QTime.currentTime())
        # self.lineEdit_2.setText("")
        self.labelError.setText("")
        # self.update_bol_table()

    def add_bol(self):
        temp = self.dateEdit.date()
        date = temp.toPyDate()
        temp_2 = self.timeEditStartTime.time()
        start_time = temp_2.toPyTime()
        temp_3 = self.timeEditEndTime.time()
        end_time = temp_3.toPyTime()
        shipper_name = self.spinBoxShipper.currentText()
        # **
        broker_name = self.spinBoxBroker.currentText()
        username = self.spinBoxUsername.currentText()
        rate_type = self.spinBoxRate.currentText()
        rate = self.lineEdit.text()
        # hours_loads = self.lineEdit_2.text()
        hours_loads = self.lineEditLoads.text()
        origin = self.textEditOriginAddress.toPlainText()
        destination = self.textEditDestinationAddress.toPlainText()
        bill_number = self.lineEditBillNumber.text()
        self.database.add_bol(date, bill_number, broker_name ,shipper_name, username, rate_type, origin, destination, start_time, end_time, hours_loads, rate)
        self.update_bol_table()
        self.clear_form_BOL()

    def delete_bol(self):
        item = self.tableWidgetBills.selectedItems()
        if len(item) == 0:
            self.labelError.setText("ERROR PLEASE SELECT JOB TO EDIT!")
        else:
            confirm = self.showdialog()
            if confirm:
                bill_id = item[0].text()
                self.database.delete_bol(bill_id)
                self.update_bol_table()
                self.clear_form_BOL()
                return


    def retranslateUiBOL(self, Bill_of_Lading):
        _translate = QtCore.QCoreApplication.translate
        Bill_of_Lading.setWindowTitle(_translate("Bill_of_Lading", "MainWindow"))
        self.label.setText(_translate("Bill_of_Lading", "BILL OF LADINGS"))
        self.label_2.setText(_translate("Bill_of_Lading", "Shipper Name:"))
        self.label_3.setText(_translate("Bill_of_Lading", "Bill Number:"))
        self.label_4.setText(_translate("Bill_of_Lading", "Origin:"))
        self.label_5.setText(_translate("Bill_of_Lading", "Destination:"))
        self.pushButtonAddJob.setText(_translate("Bill_of_Lading", "Add BOL"))
        self.pushButtonEditJob.setText(_translate("Bill_of_Lading", "Edit BOL"))
        self.pushButtonDeleteJob.setText(_translate("Bill_of_Lading", "Delete BOL"))
        self.label_7.setText(_translate("Bill_of_Lading", "Date:"))
        self.label_8.setText(_translate("Bill_of_Lading", "Start Time:"))
        self.label_9.setText(_translate("Bill_of_Lading", "End Time:"))
        self.label_10.setText(_translate("Bill_of_Lading", "Rate:"))
        self.label_11.setText(_translate("Bill_of_Lading", "$"))
        self.label_12.setText(_translate("Bill_of_Lading", "Hours/Loads:"))
        self.label_6.setText(_translate("Bill_of_Lading", " Username:"))
        self.label_13.setText(_translate("Bill_of_Lading", "Broker Name:"))
        self.pushButtonClearJob.setText(_translate("Bill_of_Lading", "Clear BOL"))
        self.label_14.setText(_translate("Bill_of_Lading", "Rate Type:"))

    def setupUiDriverLog(self, DriverLog):
        DriverLog.setObjectName("DriverLog")
        DriverLog.resize(809, 633)
        DriverLog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(DriverLog)
        self.centralwidget.setObjectName("centralwidget")
        self.labelTitle = QtWidgets.QLabel(self.centralwidget)
        self.labelTitle.setGeometry(QtCore.QRect(280, 10, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(False)
        font.setWeight(50)
        self.labelTitle.setFont(font)
        self.labelTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitle.setObjectName("labelTitle")
        self.labelTitle.setStyleSheet('QLabel {color: #124E78;}')

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 230, 761, 351))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")

        self.pushButtonClearLog = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonClearLog.setGeometry(QtCore.QRect(520, 310, 114, 32))
        self.pushButtonClearLog.setStyleSheet("background-color: rgb(192, 192, 192);")
        self.pushButtonClearLog.setObjectName("pushButtonClearLog")
        self.pushButtonClearLog.clicked.connect(self.clear_data_driver_log)

        self.pushButtonAddUser = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonAddUser.setGeometry(QtCore.QRect(400, 310, 114, 32))
        self.pushButtonAddUser.setStyleSheet("background-color: rgb(40, 195, 50);")
        self.pushButtonAddUser.setObjectName("pushButtonAddUser")
        self.pushButtonAddUser.clicked.connect(self.add_driver)

        self.pushButtonEditDriver = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonEditDriver.setGeometry(QtCore.QRect(280, 310, 114, 32))
        self.pushButtonEditDriver.setStyleSheet("background-color: rgb(255, 193, 44);")
        self.pushButtonEditDriver.setObjectName("pushButtonEditDriver")
        self.pushButtonEditDriver.clicked.connect(self.edit_driver)

        self.pushButtonDeleteUser = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonDeleteUser.setGeometry(QtCore.QRect(160, 310, 114, 32))
        self.pushButtonDeleteUser.setStyleSheet("background-color: rgb(253, 70, 70);")
        self.pushButtonDeleteUser.setObjectName("pushButtonDeleteUser")
        self.pushButtonDeleteUser.clicked.connect(self.delete_driver)


        self.labelError = QtWidgets.QLabel(self.centralwidget)
        self.labelError.setGeometry(QtCore.QRect(240, 580, 421, 21))
        self.labelError.setText("")
        self.labelError.setObjectName("labelError")
        self.labelError.setStyleSheet('QLabel {color: #990000;}')

        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(60, 10, 81, 21))
        self.label_2.setObjectName("label_2")
        self.lineEditFirstName = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditFirstName.setGeometry(QtCore.QRect(150, 10, 171, 21))
        self.lineEditFirstName.setObjectName("lineEditFirstName")
        self.lineEditLastName = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditLastName.setGeometry(QtCore.QRect(510, 10, 211, 21))
        self.lineEditLastName.setText("")
        self.lineEditLastName.setObjectName("lineEditLastName")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(410, 10, 91, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(60, 40, 81, 21))
        self.label_4.setObjectName("label_4")

        self.labelUsername = QtWidgets.QLineEdit(self.groupBox)
        self.labelUsername.setGeometry(QtCore.QRect(150, 40, 171, 21))
        self.labelUsername.setText("")
        self.labelUsername.setObjectName("labelUsername")

        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(410, 40, 101, 21))
        self.label_5.setObjectName("label_5")
        self.lineEditPhoneNumber = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditPhoneNumber.setGeometry(QtCore.QRect(510, 40, 211, 21))
        self.lineEditPhoneNumber.setObjectName("lineEditPhoneNumber")
        self.lineEditEmail = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditEmail.setGeometry(QtCore.QRect(150, 70, 171, 21))
        self.lineEditEmail.setText("")
        self.lineEditEmail.setObjectName("lineEditEmail")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(60, 70, 71, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(410, 70, 91, 21))
        self.label_7.setObjectName("label_7")
        self.textEditAddress = QtWidgets.QTextEdit(self.groupBox)
        self.textEditAddress.setGeometry(QtCore.QRect(510, 70, 211, 74))
        self.textEditAddress.setObjectName("textEditAddress")

        self.labelLicenseNumber = QtWidgets.QLineEdit(self.groupBox)
        self.labelLicenseNumber.setGeometry(QtCore.QRect(150, 100, 171, 21))
        self.labelLicenseNumber.setText("")
        self.labelLicenseNumber.setObjectName("labelLicenseNumber")

        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(60, 100, 81, 21))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(60, 130, 81, 21))
        self.label_9.setObjectName("label_9")

        self.labelLicenseExpiration = QtWidgets.QDateEdit(self.groupBox)
        self.labelLicenseExpiration.setGeometry(QtCore.QRect(155, 130, 171, 21))
        self.labelLicenseExpiration.setObjectName("labelLicenseExpiration")
        self.labelLicenseExpiration.setDateTime(QtCore.QDateTime.currentDateTime())
        self.labelLicenseExpiration.setCalendarPopup(True)
        # self.labelSpecialExpiration.setEnabled(False)
        # self.labelLicenseExpiration.setEnabled(False)
        # self.labelLicenseExpiration =

        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(60, 160, 95, 21))
        self.label_10.setObjectName("label_10")

        self.labelInsuranceExpiration = QtWidgets.QDateEdit(self.groupBox)
        self.labelInsuranceExpiration.setGeometry(QtCore.QRect(155, 160, 171, 21))
        self.labelInsuranceExpiration.setObjectName("labelInsuranceExpiration")
        self.labelInsuranceExpiration.setDateTime(QtCore.QDateTime.currentDateTime())
        self.labelInsuranceExpiration.setCalendarPopup(True)
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(60, 190, 95, 21))
        self.label_11.setObjectName("label_11")

        self.labelDrugTestExpiration = QtWidgets.QDateEdit(self.groupBox)
        self.labelDrugTestExpiration.setGeometry(QtCore.QRect(155, 190, 171, 21))
        self.labelDrugTestExpiration.setObjectName("labelDrugTestExpiration")
        self.labelDrugTestExpiration.setDateTime(QtCore.QDateTime.currentDateTime())
        self.labelDrugTestExpiration.setCalendarPopup(True)
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(60, 220, 95, 21))
        self.label_12.setObjectName("label_12")

        self.labelCARBExpiration = QtWidgets.QDateEdit(self.groupBox)
        self.labelCARBExpiration.setGeometry(QtCore.QRect(155, 220, 171, 21))
        self.labelCARBExpiration.setObjectName("labelCARBExpiration")
        self.labelCARBExpiration.setDateTime(QtCore.QDateTime.currentDateTime())
        self.labelCARBExpiration.setCalendarPopup(True)
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(60, 250, 95, 21))
        self.label_13.setObjectName("label_13")

        self.labelMPCExpiration = QtWidgets.QDateEdit(self.groupBox)
        self.labelMPCExpiration.setGeometry(QtCore.QRect(155, 250, 171, 21))
        self.labelMPCExpiration.setObjectName("labelMPCExpiration")
        self.labelMPCExpiration.setDateTime(QtCore.QDateTime.currentDateTime())
        self.labelMPCExpiration.setCalendarPopup(True)
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setGeometry(QtCore.QRect(60, 280, 95, 21))
        self.label_14.setObjectName("label_14")

        self.labelDIRExpiration = QtWidgets.QDateEdit(self.groupBox)
        self.labelDIRExpiration.setGeometry(QtCore.QRect(155, 280, 171, 21))
        self.labelDIRExpiration.setObjectName("labelDIRExpiration")
        self.labelDIRExpiration.setDateTime(QtCore.QDateTime.currentDateTime())
        self.labelDIRExpiration.setCalendarPopup(True)

        self.spcialCheckbox = QtWidgets.QCheckBox(self.groupBox)
        self.spcialCheckbox.setGeometry(QtCore.QRect(410, 160, 20, 20))
        self.spcialCheckbox.stateChanged.connect(self.checkBoxChangeAction)

        self.label_15 = QtWidgets.QLabel(self.groupBox)
        self.label_15.setGeometry(QtCore.QRect(435, 160, 100, 21))
        self.label_15.setObjectName("label_15")
        self.labelSpecialExpiration = QtWidgets.QDateEdit(self.groupBox)
        self.labelSpecialExpiration.setGeometry(QtCore.QRect(540, 160, 171, 21))
        self.labelSpecialExpiration.setObjectName("labelSpecialExpiration")
        self.labelSpecialExpiration.setDateTime(self.labelSpecialExpiration.maximumDateTime())
        self.labelSpecialExpiration.setEnabled(False)
        self.labelSpecialExpiration.setStyleSheet("selection-background-color: #ffffff;")
        self.labelSpecialExpiration.setCalendarPopup(True)

        self.label_16 = QtWidgets.QLabel(self.groupBox)
        self.label_16.setGeometry(QtCore.QRect(410, 190, 91, 21))
        self.label_16.setObjectName("label_16")
        self.textEditComments= QtWidgets.QTextEdit(self.groupBox)
        self.textEditComments.setGeometry(QtCore.QRect(510, 190, 211, 74))
        self.textEditComments.setObjectName("textEditComments")
        # self.show()
        # if self.spcialCheckbox.
        self.pushButtonHome = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonHome.setGeometry(QtCore.QRect(720, 20, 50, 50))
        self.pushButtonHome.setIcon(
            QtGui.QIcon(self.resource_path("144x144.png")))
        self.pushButtonHome.setStyleSheet("border-radius: 3px;")
        self.pushButtonHome.setIconSize(QtCore.QSize(45, 45))
        self.pushButtonHome.setText("")
        self.pushButtonHome.setObjectName("pushButtonHome")
        self.pushButtonHome.clicked.connect(self.show_home)

        self.tableWidgetUsers = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidgetUsers.setGeometry(QtCore.QRect(20, 70, 771, 161))
        self.tableWidgetUsers.setObjectName("tableWidgetUsers")
        self.tableWidgetUsers.setColumnCount(9)
        self.tableWidgetUsers.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.tableWidgetUsers.itemSelectionChanged.connect(self.change_data_driver_log)
        column_titles = ['id', 'first name', 'last name','username','phone number', 'email', 'address', 'license no.', 'license exp.']
        counter = 0
        for title in column_titles:
            item = QtWidgets.QTableWidgetItem(title)
            item.setBackground(QtGui.QColor(211,211,211))
            self.tableWidgetUsers.setHorizontalHeaderItem(counter,item)
            counter += 1
        self.update_user_list()

        self.tableWidgetUsers.setSortingEnabled(True)
        # self.tableWidgetUsers.resizeRowsToContents()
        # self.tableWidgetUsers.horizontalHeader().sortIndicatorChanged.connect(self.tableWidgetUsers.resizeRowsToContents)
        self.tableWidgetUsers.verticalHeader().setVisible(False)
        header = self.tableWidgetUsers.resizeColumnToContents(0)

        DriverLog.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DriverLog)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 809, 22))
        self.menubar.setObjectName("menubar")
        DriverLog.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DriverLog)
        self.statusbar.setObjectName("statusbar")
        DriverLog.setStatusBar(self.statusbar)

        self.retranslateUiDriverLog(DriverLog)
        QtCore.QMetaObject.connectSlotsByName(DriverLog)

    def checkBoxChangeAction(self, state):
        if (QtCore.Qt.Checked == state):
            self.labelSpecialExpiration.setDateTime(QtCore.QDateTime.currentDateTime())
            self.labelSpecialExpiration.setEnabled(True)
            self.labelSpecialExpiration.setStyleSheet("selection-background-color: #dddddd;")
        else:
            self.labelSpecialExpiration.setDateTime(self.labelSpecialExpiration.maximumDateTime())
            self.labelSpecialExpiration.setEnabled(False)
            self.labelSpecialExpiration.setStyleSheet("selection-background-color: #ffffff;")

    def retranslateUiDriverLog(self, DriverLog):
        _translate = QtCore.QCoreApplication.translate
        DriverLog.setWindowTitle(_translate("DriverLog", "MainWindow"))
        self.labelTitle.setText(_translate("DriverLog", "DRIVER LOG"))
        self.pushButtonClearLog.setText(_translate("DriverLog", "Clear Form"))
        self.pushButtonAddUser.setText(_translate("DriverLog", "Add User"))
        self.pushButtonEditDriver.setText(_translate("DriverLog", "Edit User"))
        self.pushButtonDeleteUser.setText(_translate("DriverLog", "Delete User"))
        self.label_2.setText(_translate("DriverLog", "First Name:"))
        self.label_3.setText(_translate("DriverLog", "Last Name:"))
        self.label_4.setText(_translate("DriverLog", "Username:"))
        self.label_5.setText(_translate("DriverLog", "Phone Number:"))
        self.label_6.setText(_translate("DriverLog", "Email:"))
        self.label_7.setText(_translate("DriverLog", "Address:"))
        self.label_8.setText(_translate("DriverLog", "License No.:"))
        self.label_9.setText(_translate("DriverLog", "License Exp.:"))
        self.label_10.setText(_translate("DriverLog", "Insurance Exp.:"))
        self.label_11.setText(_translate("DriverLog", "Drug Test Exp.:"))
        self.label_12.setText(_translate("DriverLog", "CARB Exp.:"))
        self.label_13.setText(_translate("DriverLog", "MCP Exp.:"))
        self.label_14.setText(_translate("DriverLog", "DIR Exp.:"))
        self.label_15.setText(_translate("DriverLog", "Registration Exp.:"))
        self.label_16.setText(_translate("DriverLog", "Comments:"))

    def change_data_driver_log(self):
        item = self.tableWidgetUsers.selectedItems()
        if len(item) == 0:
            return
        else:
            user_id = int(item[0].text())
            user = self.database.get_user(user_id)
            #time = str(self.selected_job.start_time).split(':')
            #self.timeEditStartTime.setTime(QtCore.QTime(int(time[0]), int(time[1])))
            self.lineEditFirstName.setText(user.first_name)
            self.lineEditLastName.setText(user.last_name)
            self.labelUsername.setText(user.username)
            self.labelUsername.setEnabled(False)
            self.labelUsername.setStyleSheet("selection-background-color: #ffffff;")
            self.lineEditPhoneNumber.setText(user.phone_number)
            self.lineEditEmail.setText(user.email)
            self.textEditAddress.setText(user.address)
            self.labelLicenseNumber.setText(user.license_number)

            # self.labelLicenseExpiration.setText(str(item[8].text()))
            # print(user.license_expire)

            self.labelLicenseExpiration.setDate(user.license_expire)
            self.labelDrugTestExpiration.setDate(user.drug_test)
            self.labelCARBExpiration.setDate(user.carb)
            self.labelMPCExpiration.setDate(user.mpc)
            self.labelDIRExpiration.setDate(user.dir)
            self.labelSpecialExpiration.setDate(user.special_expire)
            self.textEditComments.setText(user.comment)
            return

    def update_user_list(self):
        for i in reversed(range(self.tableWidgetUsers.rowCount())):
            self.tableWidgetUsers.removeRow(i)

        users_list = self.database.get_users()

        for row_number in range(len(users_list)):
            self.tableWidgetUsers.insertRow(row_number)
            user = users_list[row_number]
            b = QtWidgets.QTableWidgetItem()
            b.setData(Qt.EditRole, QVariant(user.user_id))
            dt = datetime.datetime.strptime(str(user.license_expire), '%Y-%m-%d').strftime('%m/%d/%y')
            self.tableWidgetUsers.setItem(row_number, 0, QtWidgets.QTableWidgetItem(str(user.user_id)))
            self.tableWidgetUsers.setItem(row_number, 1, QtWidgets.QTableWidgetItem(str(user.first_name)))
            self.tableWidgetUsers.setItem(row_number, 2, QtWidgets.QTableWidgetItem(str(user.last_name)))
            self.tableWidgetUsers.setItem(row_number, 3, QtWidgets.QTableWidgetItem(str(user.username)))
            self.tableWidgetUsers.setItem(row_number, 4, QtWidgets.QTableWidgetItem(str(user.phone_number)))
            self.tableWidgetUsers.setItem(row_number, 5, QtWidgets.QTableWidgetItem(str(user.email)))
            self.tableWidgetUsers.setItem(row_number, 6, QtWidgets.QTableWidgetItem(str(user.address)))
            self.tableWidgetUsers.setItem(row_number, 7, QtWidgets.QTableWidgetItem(str(user.license_number)))
            self.tableWidgetUsers.setItem(row_number, 8, QtWidgets.QTableWidgetItem(str(dt)))
        return

    def add_job(self):
        temp = self.dateEdit.date()
        date = temp.toPyDate()
        temp_2 = self.timeEditStartTime.time()
        time = temp_2.toPyTime()
        shipper_name = self.spinBoxShipper.currentText()
        broker_name = self.spinBoxBroker.currentText()
        username = self.spinBoxUsername.currentText()
        rate = self.lineEditRate.text()
        rate_type = self.spinBoxRate.currentText()
        origin = self.textEditOriginAddress.toPlainText()
        destination = self.textEditDestinationAddress.toPlainText()
        comments = self.textEditComments.toPlainText()

        self.database.add_job(shipper_name, broker_name, username, date, time, rate_type, rate, origin, destination, comments)
        self.update_jobs_list()
        self.clear_form_add_job()

    def add_driver(self):
        first_name = self.lineEditFirstName.text()
        last_name = self.lineEditLastName.text()
        user_name = self.labelUsername.text()
        phone_number = self.lineEditPhoneNumber.text()
        email = self.lineEditEmail.text()
        address = str(self.textEditAddress.toPlainText())
        license_number = self.labelLicenseNumber.text()
        isDateValid =False
        if self.labelLicenseExpiration.date().isValid():
            license_expire = self.labelLicenseExpiration.date().toPyDate()
            isDateValid = True
        else:
            isDateValid = False
        if self.labelInsuranceExpiration.date().isValid() and isDateValid is True:
            insurance_expire = self.labelInsuranceExpiration.date().toPyDate()
            isDateValid = True
        else:
            isDateValid = False
        if self.labelDrugTestExpiration.date().isValid() and isDateValid is True:
            drug_test_expire = self.labelDrugTestExpiration.date().toPyDate()
            isDateValid = True
        else:
            isDateValid = False
        if self.labelCARBExpiration.date().isValid() and isDateValid is True:
            carb_expire = self.labelCARBExpiration.date().toPyDate()
            isDateValid = True
        else:
            isDateValid = False
        if self.labelMPCExpiration.date().isValid() and isDateValid is True:
            mpc_expire = self.labelMPCExpiration.date().toPyDate()
            isDateValid = True
        else:
            isDateValid = False
        if self.labelDIRExpiration.date().isValid() and isDateValid is True:
            dir_expire = self.labelDIRExpiration.date().toPyDate()
            isDateValid = True
        else:
            isDateValid = False
        if self.labelSpecialExpiration.date().isValid() and isDateValid is True:
            special_expire = self.labelSpecialExpiration.date().toPyDate()
            isDateValid = True
        else:
            isDateValid = False
        comment = str(self.textEditComments.toPlainText())
        # if isDateValid is True:
        #     self.labelError.setText("")
        #     self.database.add_user(first_name, last_name, user_name, phone_number, email, address, license_number, license_expire,
        #         insurance_expire, drug_test_expire, carb_expire, mpc_expire, dir_expire, special_expire, comment)
        #     self.update_user_list()
        # # self.sign_up(user_name, email)
        #     self.clear_data_driver_log()
        if isDateValid is False:
            self.labelError.setText("Error: Invalid Date!")
        elif not user_name and not user_name.strip():
            self.labelError.setText("Please enter username!")
        elif not first_name and not first_name.strip():
            self.labelError.setText("Please enter firstname!")
        elif not last_name and not last_name.strip():
            self.labelError.setText("Please enter lastname!")
        elif not email and not email.strip():
            self.labelError.setText("Please enter email!")
        else:
            self.labelError.setText("")
            self.database.add_user(first_name, last_name, user_name, phone_number, email, address, license_number, license_expire,
                insurance_expire, drug_test_expire, carb_expire, mpc_expire, dir_expire, special_expire, comment)
            self.update_user_list()
        self.sign_up(user_name, email)
        self.clear_data_driver_log()
        return

    def edit_driver(self):
        item = self.tableWidgetUsers.selectedItems()
        if len(item) == 0:
            self.labelError.setText("ERROR PLEASE SELECT DRIVER TO EDIT OR ADD NEW DRIVER!")
        else:
            confirm = self.showdialog()
            if confirm:
                user_id = int(item[0].text())
                username = self.labelUsername.text()
                first_name = self.lineEditFirstName.text()
                last_name = self.lineEditLastName.text()
                phone_number = self.lineEditPhoneNumber.text()
                email = self.lineEditEmail.text()
                address = str(self.textEditAddress.toPlainText())
                license_number = self.labelLicenseNumber.text()
                isDateValid =False
                if self.labelLicenseExpiration.date().isValid():
                    license_expire = self.labelLicenseExpiration.date().toPyDate()
                    isDateValid = True
                else:
                    isDateValid = False
                if self.labelInsuranceExpiration.date().isValid() and isDateValid is True:
                    insurance_expire = self.labelInsuranceExpiration.date().toPyDate()
                    isDateValid = True
                else:
                    isDateValid = False
                if self.labelDrugTestExpiration.date().isValid() and isDateValid is True:
                    drug_test_expire = self.labelDrugTestExpiration.date().toPyDate()
                    isDateValid = True
                else:
                    isDateValid = False
                if self.labelCARBExpiration.date().isValid() and isDateValid is True:
                    carb_expire = self.labelCARBExpiration.date().toPyDate()
                    isDateValid = True
                else:
                    isDateValid = False
                if self.labelMPCExpiration.date().isValid() and isDateValid is True:
                    mpc_expire = self.labelMPCExpiration.date().toPyDate()
                    isDateValid = True
                else:
                    isDateValid = False
                if self.labelDIRExpiration.date().isValid() and isDateValid is True:
                    dir_expire = self.labelDIRExpiration.date().toPyDate()
                    isDateValid = True
                else:
                    isDateValid = False
                if self.labelSpecialExpiration.date().isValid() and isDateValid is True:
                    special_expire = self.labelSpecialExpiration.date().toPyDate()
                    isDateValid = True
                else:
                    isDateValid = False
                comment = str(self.textEditComments.toPlainText())

                if isDateValid is False:
                    self.labelError.setText("Error: Invalid Date!")
                elif not first_name and not first_name.strip():
                    self.labelError.setText("Please enter firstname!")
                elif not last_name and not last_name.strip():
                    self.labelError.setText("Please enter lastname!")
                elif not email and not email.strip():
                    self.labelError.setText("Please enter email!")
                else:
                    self.labelError.setText("")
                    self.database.update_user(user_id, username, first_name, last_name, phone_number, email, address,
                        insurance_expire, drug_test_expire, carb_expire, mpc_expire, dir_expire, special_expire, comment,
                        license_number, license_expire)
                    self.update_user_list()
                    self.clear_data_driver_log()
                return
            else:
                return

    def delete_driver(self):
        item = self.tableWidgetUsers.selectedItems()
        if len(item) == 0:
            self.labelError.setText("ERROR PLEASE SELECT DRIVER TO DELETE OR ADD NEW DRIVER!")
        else:
            confirm = self.showdialog()
            if confirm:
                user_id = int(item[0].text())
                username = self.labelUsername.text()
                self.database.delete_user(user_id, username)
                self.cognito_delete_user(username)
                self.update_user_list()
                self.clear_data_driver_log()
                return
            else:
                return

    def clear_data_driver_log(self):
        self.tableWidgetUsers.setSortingEnabled(False)
        self.database.refresh()
        self.update_user_list()
        self.tableWidgetUsers.setSortingEnabled(True)
        self.lineEditFirstName.setText("")
        self.lineEditLastName.setText("")
        self.labelUsername.setText("")
        self.lineEditPhoneNumber.setText("")
        self.lineEditEmail.setText("")
        self.textEditAddress.setText("")
        self.labelLicenseNumber.setText("")
        self.textEditComments.setText("")
        self.labelError.setText("")
        self.labelUsername.setEnabled(True)
        self.spcialCheckbox.setChecked(False)
        self.labelLicenseExpiration.setDateTime(QtCore.QDateTime.currentDateTime())

    def setupUiAddBroker(self, AddBroker):
        AddBroker.setObjectName("AddBroker")
        AddBroker.resize(800, 600)
        AddBroker.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(AddBroker)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 10, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(False)
        font.setWeight(50)

        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setStyleSheet('QLabel {color: #124E78;}')

        self.listWidgetBrokers = QtWidgets.QListWidget(self.centralwidget)
        self.listWidgetBrokers.setGeometry(QtCore.QRect(40, 80, 261, 451))
        self.listWidgetBrokers.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.listWidgetBrokers.setObjectName("listWidgetBrokers")
        self.listWidgetBrokers.itemSelectionChanged.connect(self.change_data_add_broker)

        self.update_broker_list()

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(320, 80, 461, 441))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.lineEditBrokerName = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditBrokerName.setGeometry(QtCore.QRect(10, 30, 441, 21))
        self.lineEditBrokerName.setObjectName("lineEditBrokerName")

        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 101, 16))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 111, 16))
        self.label_3.setObjectName("label_3")

        self.textEditBrokerAddress = QtWidgets.QTextEdit(self.groupBox)
        self.textEditBrokerAddress.setGeometry(QtCore.QRect(10, 130, 441, 51))
        self.textEditBrokerAddress.setObjectName("textEditBrokerAddress")

        self.pushButtonAddBroker = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonAddBroker.setGeometry(QtCore.QRect(353, 400, 101, 32))
        self.pushButtonAddBroker.setStyleSheet("background-color: rgb(40, 195, 50);")
        self.pushButtonAddBroker.setObjectName("pushButtonAddBroker")
        self.pushButtonAddBroker.clicked.connect(self.add_broker)

        self.pushButtonEditBroker = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonEditBroker.setGeometry(QtCore.QRect(243, 400, 101, 32))
        self.pushButtonEditBroker.setStyleSheet("background-color: rgb(255, 193, 44);")
        self.pushButtonEditBroker.setObjectName("pushButtonEditBroker")
        self.pushButtonEditBroker.clicked.connect(self.edit_broker)

        self.pushButtonDeleteBroker = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonDeleteBroker.setGeometry(QtCore.QRect(130, 400, 101, 32))
        self.pushButtonDeleteBroker.setStyleSheet("background-color: rgb(253, 70, 70);")
        self.pushButtonDeleteBroker.setObjectName("pushButtonDeleteBroker")
        self.pushButtonDeleteBroker.clicked.connect(self.delete_broker)

        self.pushButtonClearForm = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonClearForm.setGeometry(QtCore.QRect(10, 400, 101, 32))
        self.pushButtonClearForm.setStyleSheet("background-color: rgb(122, 122, 122);")
        self.pushButtonClearForm.setObjectName("pushButtonClearForm")
        self.pushButtonClearForm.clicked.connect(self.clear_data_add_broker)

        self.labelError = QtWidgets.QLabel(self.centralwidget)
        self.labelError.setGeometry(QtCore.QRect(340, 520, 421, 21))
        self.labelError.setText("")
        self.labelError.setObjectName("labelError")
        self.labelError.setStyleSheet('QLabel {color: #990000;}')

        self.pushButtonHome = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonHome.setGeometry(QtCore.QRect(720, 20, 50, 50))
        self.pushButtonHome.setIcon(QtGui.QIcon(self.resource_path("144x144.png")))
        self.pushButtonHome.setStyleSheet("border-radius: 3px;")
        self.pushButtonHome.setIconSize(QtCore.QSize(45,45))
        self.pushButtonHome.setText("")
        self.pushButtonHome.setObjectName("pushButtonHome")
        self.pushButtonHome.clicked.connect(self.show_home)

        AddBroker.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AddBroker)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        AddBroker.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AddBroker)
        self.statusbar.setObjectName("statusbar")
        AddBroker.setStatusBar(self.statusbar)

        self.retranslateUiAddBroker(AddBroker)
        QtCore.QMetaObject.connectSlotsByName(AddBroker)

    def retranslateUiAddBroker(self, AddBroker):
        _translate = QtCore.QCoreApplication.translate
        AddBroker.setWindowTitle(_translate("AddBroker", "MainWindow"))
        self.label.setText(_translate("AddBroker", "ADD BROKER"))
        self.label_2.setText(_translate("AddBroker", "Broker Name:"))
        self.label_3.setText(_translate("AddBroker", "Broker Address:"))
        self.pushButtonAddBroker.setText(_translate("AddBroker", "Add Broker"))
        self.pushButtonEditBroker.setText(_translate("AddBroker", "Edit Broker"))
        self.pushButtonDeleteBroker.setText(_translate("AddBroker", "Delete Broker"))
        self.pushButtonClearForm.setText(_translate("AddBroker","Clear Form"))

    def update_broker_list(self):
        self.listWidgetBrokers.clear()
        broker_list = self.database.get_brokers()
        for broker in broker_list:
            broker_description = "{} - {} - {}".format(broker.broker_id, broker.name, broker.address)
            self.listWidgetBrokers.addItem(broker_description)

    def change_data_add_broker(self):
        item = self.listWidgetBrokers.selectedItems()
        if len(item) == 0:
            return
        else:
            list = item[0].text().split()
            broker = self.database.get_broker(list[0])
            self.lineEditBrokerName.setText(broker.name)
            self.textEditBrokerAddress.setText(broker.address)

    def clear_data_add_broker(self):
        self.listWidgetBrokers.clearSelection()
        self.lineEditBrokerName.setText("")
        self.textEditBrokerAddress.setText("")
        self.labelError.setText("")

    def edit_broker(self):
        item = self.listWidgetBrokers.selectedItems()
        if len(item) == 0:
            self.labelError.setText("ERROR PLEASE SELECT SHIPPER TO EDIT!")
        else:
            confirm = self.showdialog()
            if confirm:
                list = item[0].text().split()
                broker_id = list[0]

                name = self.lineEditBrokerName.text()
                address = str(self.textEditBrokerAddress.toPlainText())
                self.database.update_broker(broker_id, name, address)
                self.update_broker_list()
                self.clear_data_add_broker()
                return
            else:
                return

    def delete_broker(self):
        item = self.listWidgetBrokers.selectedItems()
        if len(item) == 0:
            self.labelError.setText("ERROR PLEASE SELECT SHIPPER TO DELETE!")
        else:
            confirm = self.showdialog()
            if confirm:
                list = item[0].text().split()
                broker_id = list[0]

                self.database.delete_broker(broker_id)
                self.update_broker_list()
                self.clear_data_add_broker()
                return
            else:
                return

    def add_broker(self):
        name = self.lineEditBrokerName.text()
        address = str(self.textEditBrokerAddress.toPlainText())

        if (name == ""):
            self.labelError.setText("Error: Name Cannot be blank!")
            return
        if (address == ""):
            self.labelError.setText("Error: Address Cannot be blank")
            return

        self.database.add_broker(name, address)
        self.update_broker_list()
        self.clear_data_add_broker()
        return

    def set_layout(self, ui, FleetConsole):
        self.ui = ui
        self.FleetConsole = FleetConsole

    def sign_up(self, username, email):
        self.aws_cog = Cognito('*******', '********', username= username, access_key='******',
        secret_key='********', user_pool_region = '*******')
        self.aws_cog.add_base_attributes(email=email)
        self.aws_cog.register(username, '123456')
        self.aws_cog.admin_confirm_sign_up(username=username)
    def cognito_delete_user(self, username):
        self.aws_cog = Cognito('********', '*********', username= username, access_key='************',
        secret_key='***********', user_pool_region = '***********')
        self.aws_cog.admin_delete_user();

    def print_exp_notification(self):
        users = self.database.get_users()
        expirations = ""
        for user in users:
            license_expire = user.license_expire - timedelta(45) - date.today()
            drug_test_expire = user.drug_test - timedelta(45) - date.today()
            carb_expire = user.carb - timedelta(45) - date.today()
            mpc_expire = user.mpc - timedelta(45) - date.today()
            dir_expire = user.dir - timedelta(45) - date.today()
            if date(9999,12,31) != user.special_expire:
                special_expire = user.special_expire - timedelta(45) -date.today()
                if special_expire.days < 45 and special_expire.days > 0 :
                    expirations += " - " + user.username + "\'s " + user.comment + " will expire within " + str(special_expire.days) +" days. \n"
                elif special_expire.days < 0 :
                    expirations += " - " + user.username + "\'s " + user.comment + " expired " + str(abs(special_expire.days)) +" days ago. \n"
            # License_test_expiratation
            if license_expire.days < 45 and license_expire.days > 0 :
                expirations += " - " + user.username + "\'s driver license will expire within " + str(license_expire.days) +" days. \n"
            elif license_expire.days < 0 :
                expirations += " - " + user.username + "\'s driver license expired " + str(abs(license_expire.days)) +" days ago. \n"
            # Drug_test_expiration
            if drug_test_expire.days < 45 and drug_test_expire.days > 0 :
                expirations += " - " + user.username + "\'s DRUG TEST will expire within " + str(drug_test_expire.days) +" days. \n"
            elif drug_test_expire.days < 0 :
                expirations += " - " + user.username + "\'s DRUG TEST expired " + str(abs(drug_test_expire.days)) +" days ago. \n"
            # carb_expiration
            if carb_expire.days < 45 and carb_expire.days > 0 :
                expirations += " - " + user.username + "\'s CARB will expire within " + str(carb_expire.days) +" days. \n"
            elif carb_expire.days < 0 :
                expirations += " - " + user.username + "\'s CARB expired " + str(abs(carb_expire.days)) +" days ago. \n"
            # mpc_expiration
            if mpc_expire.days < 45 and mpc_expire.days > 0 :
                expirations += " - " + user.username + "\'s MCP will expire within " + str(mpc_expire.days) +" days. \n"
            elif mpc_expire.days < 0 :
                expirations += " - " + user.username + "\'s MCP expired " + str(abs(mpc_expire.days)) +" days ago. \n"
            # Dir_expiration
            if dir_expire.days < 45 and dir_expire.days > 0 :
                expirations += " - " + user.username + "\'s MCP will expire within " + str(dir_expire.days) +" days. \n"
            elif dir_expire.days < 0 :
                expirations += " - " + user.username + "\'s MCP expired " + str(abs(dir_expire.days)) +" days ago. \n"
        return expirations

    def print_job_notification(self):
        jobs = self.database.get_current_jobs()
        declined = ""
        isNotified = False
        for job in jobs:
            if job.status.lower() in ['declined']:
                declined += " - " + job.username + " declined the job offered on " + str(job.start_date) + ".\n"
        return declined
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FleetConsole = QtWidgets.QMainWindow()
    ui = Ui_FleetConsole()
    ui.setupUi(FleetConsole)
    ui.set_layout(ui, FleetConsole)
    FleetConsole.show()
    sys.exit(app.exec_())
