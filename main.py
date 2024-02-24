from PyQt5 import QtCore, QtGui, QtWidgets
from classes import manage
import shutil


class Ui_homeWindow(object):
    def goToCustomerWindow(self):
        homeWindow.hide()
        customerLogin.show()

    def goToManageWindow(self):
        homeWindow.hide()
        manageLogin.show()

    def setupUi(self, homeWindow):
        homeWindow.setObjectName("homeWindow")
        homeWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        homeWindow.setEnabled(True)
        homeWindow.resize(720, 540)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(homeWindow.sizePolicy().hasHeightForWidth())
        homeWindow.setSizePolicy(sizePolicy)
        homeWindow.setMinimumSize(QtCore.QSize(720, 540))
        homeWindow.setMaximumSize(QtCore.QSize(720, 540))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        homeWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./media/favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        homeWindow.setWindowIcon(icon)
        homeWindow.setAutoFillBackground(False)
        homeWindow.setStyleSheet("margin:0;\n"
                                 "padding:0;")
        homeWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        homeWindow.setDocumentMode(False)
        homeWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(homeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 270, 720, 270))
        font = QtGui.QFont()
        font.setUnderline(False)
        self.frame_2.setFont(font)
        self.frame_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.frame_2.setMouseTracking(False)
        self.frame_2.setAutoFillBackground(False)
        self.frame_2.setStyleSheet("background-color: #C0686E;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.manageNavBtn = QtWidgets.QPushButton(self.frame_2, clicked=self.goToManageWindow)
        self.manageNavBtn.setGeometry(QtCore.QRect(225, 85, 270, 100))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.manageNavBtn.setFont(font)
        self.manageNavBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.manageNavBtn.setStyleSheet("#manageNavBtn{\n"
                                        "background-color:#F3F3F3;\n"
                                        "border-radius: 25px;\n"
                                        "}\n"
                                        "#manageNavBtn::hover{\n"
                                        "background-color:#FCFCFC;\n"
                                        "}\n"
                                        "")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./media/manager icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.manageNavBtn.setIcon(icon1)
        self.manageNavBtn.setIconSize(QtCore.QSize(60, 60))
        self.manageNavBtn.setObjectName("manageNavBtn")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 720, 270))
        font = QtGui.QFont()
        font.setUnderline(False)
        self.frame.setFont(font)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-color: #81C3E7;")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.customerNavBtn = QtWidgets.QPushButton(self.frame, clicked=self.goToCustomerWindow)
        self.customerNavBtn.setGeometry(QtCore.QRect(225, 80, 270, 100))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.customerNavBtn.setFont(font)
        self.customerNavBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.customerNavBtn.setStyleSheet("#customerNavBtn{\n"
                                          "background-color:#F3F3F3;\n"
                                          "border-radius: 25px;\n"
                                          "}\n"
                                          "#customerNavBtn::hover{\n"
                                          "background-color:#FCFCFC;\n"
                                          "}\n"
                                          "")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./media/cart icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.customerNavBtn.setIcon(icon2)
        self.customerNavBtn.setIconSize(QtCore.QSize(60, 60))
        self.customerNavBtn.setObjectName("customerNavBtn")
        homeWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(homeWindow)
        QtCore.QMetaObject.connectSlotsByName(homeWindow)

    def retranslateUi(self, homeWindow):
        _translate = QtCore.QCoreApplication.translate
        homeWindow.setWindowTitle(_translate("homeWindow", "Supermarket System by <X-Coders/>"))
        self.manageNavBtn.setText(_translate("homeWindow", "   Management"))
        self.customerNavBtn.setText(_translate("homeWindow", "         Customer"))


class Ui_manageLogin(object):
    def checkCredentials(self, username, password):
        admin_password = open("./databases/adminPass.txt", mode="r").readline().strip()
        if not (username == "admin" and password == admin_password):
            self.errorBox.show()
        else:
            self.errorBox.hide()
            self.goToDashboard()

    def goToDashboard(self):
        managementDashboard.show()
        manageLogin.hide()

    def goToHome(self):
        manageLogin.hide()
        homeWindow.show()

    def setupUi(self, manageLogin):
        manageLogin.setObjectName("manageLogin")
        manageLogin.setWindowModality(QtCore.Qt.ApplicationModal)
        manageLogin.setEnabled(True)
        manageLogin.resize(720, 540)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(manageLogin.sizePolicy().hasHeightForWidth())
        manageLogin.setSizePolicy(sizePolicy)
        manageLogin.setMinimumSize(QtCore.QSize(720, 540))
        manageLogin.setMaximumSize(QtCore.QSize(720, 540))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        manageLogin.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\media/favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        manageLogin.setWindowIcon(icon)
        manageLogin.setAutoFillBackground(False)
        manageLogin.setStyleSheet("margin:0;\n"
                                  "padding:0;\n"
                                  "background-color: #C0686E;")
        manageLogin.setProperty("documentMode", False)
        self.goToHome = QtWidgets.QPushButton(manageLogin, clicked=self.goToHome)
        self.goToHome.setGeometry(QtCore.QRect(40, 40, 50, 50))
        self.goToHome.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.goToHome.setStyleSheet("\n"
                                    "#goToHome{\n"
                                    "background:none;\n"
                                    "border:0;\n"
                                    "}")
        self.goToHome.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\media/back arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.goToHome.setIcon(icon1)
        self.goToHome.setIconSize(QtCore.QSize(50, 50))
        self.goToHome.setObjectName("goToHome")
        self.frame = QtWidgets.QFrame(manageLogin)
        self.frame.setGeometry(QtCore.QRect(130, 40, 460, 460))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(170, 60, 120, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.user = QtWidgets.QLineEdit(self.frame)
        self.user.setGeometry(QtCore.QRect(105, 165, 250, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.user.setFont(font)
        self.user.setStyleSheet("#user{\n"
                                "background-color:white;\n"
                                "}")
        self.user.setText("")
        self.user.setFrame(True)
        self.user.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.user.setObjectName("user")
        self.password = QtWidgets.QLineEdit(self.frame)
        self.password.setGeometry(QtCore.QRect(105, 215, 250, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.password.setFont(font)
        self.password.setStyleSheet("#password{\n"
                                    "background-color:white;\n"
                                    "}")
        self.password.setText("")
        self.password.setFrame(True)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.password.setObjectName("password")
        self.loginButton = QtWidgets.QPushButton(self.frame, clicked=lambda: self.checkCredentials(self.user.text(),
                                                                                                   self.password.text()))
        self.loginButton.setGeometry(QtCore.QRect(105, 285, 250, 50))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.loginButton.setFont(font)
        self.loginButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.loginButton.setStyleSheet("#loginButton{\n"
                                       "background-color:rgb(143, 212, 151);\n"
                                       "color:white;\n"
                                       "border:0;\n"
                                       "font-size:18px;\n"
                                       "}\n"
                                       "#loginButton::hover{\n"
                                       "background-color:rgb(75, 143, 75);\n"
                                       "}")
        self.loginButton.setObjectName("loginButton")
        self.errorBox = QtWidgets.QLabel(self.frame)
        self.errorBox.setGeometry(QtCore.QRect(80, 365, 300, 40))
        self.errorBox.setStyleSheet("color:#aa0000;\nfont-size:10px;")
        self.errorBox.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.errorBox.setAlignment(QtCore.Qt.AlignCenter)
        self.errorBox.setOpenExternalLinks(False)
        self.errorBox.setObjectName("errorBox")
        self.errorBox.hide()

        self.retranslateUi(manageLogin)
        QtCore.QMetaObject.connectSlotsByName(manageLogin)

    def retranslateUi(self, manageLogin):
        _translate = QtCore.QCoreApplication.translate
        manageLogin.setWindowTitle(_translate("manageLogin", "Supermarket System by <X-Coders/>"))
        self.label.setText(_translate("manageLogin", "Login"))
        self.user.setPlaceholderText(_translate("manageLogin", "Username"))
        self.password.setPlaceholderText(_translate("manageLogin", "Password"))
        self.loginButton.setText(_translate("manageLogin", "Login"))
        self.errorBox.setText(_translate("manageLogin", "Error: The username or password isn\'t correct"))


class Ui_customerLogin(object):
    def goToHome(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_homeWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        manageLogin.hide()

    def setupUi(self, customerLogin):
        customerLogin.setObjectName("customerLogin")
        customerLogin.setWindowModality(QtCore.Qt.ApplicationModal)
        customerLogin.setEnabled(True)
        customerLogin.resize(720, 540)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(customerLogin.sizePolicy().hasHeightForWidth())
        customerLogin.setSizePolicy(sizePolicy)
        customerLogin.setMinimumSize(QtCore.QSize(720, 540))
        customerLogin.setMaximumSize(QtCore.QSize(720, 540))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        customerLogin.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("media/favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        customerLogin.setWindowIcon(icon)
        customerLogin.setAutoFillBackground(False)
        customerLogin.setStyleSheet("margin:0;\n"
                                    "padding:0;\n"
                                    "background-color: #81C3E7;")
        customerLogin.setProperty("documentMode", False)
        self.centralwidget = QtWidgets.QWidget(customerLogin)
        self.centralwidget.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.centralwidget.setObjectName("centralwidget")
        self.goToHome = QtWidgets.QPushButton(customerLogin, clicked=self.goToHome)
        self.goToHome.setGeometry(QtCore.QRect(40, 40, 50, 50))
        self.goToHome.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.goToHome.setStyleSheet("\n"
                                    "#goToHome{\n"
                                    "background:none;\n"
                                    "border:0;\n"
                                    "}")
        self.goToHome.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\media/back arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.goToHome.setIcon(icon1)
        self.goToHome.setIconSize(QtCore.QSize(50, 50))
        self.goToHome.setObjectName("goToHome")
        self.retranslateUi(customerLogin)
        QtCore.QMetaObject.connectSlotsByName(customerLogin)

    def retranslateUi(self, customerLogin):
        _translate = QtCore.QCoreApplication.translate
        customerLogin.setWindowTitle(_translate("customerLogin", "Supermarket System by <X-Coders/>"))


class Ui_managementDashboard(object):

    def addPW(self):
        managementDashboard.hide()
        addProduct.show()

    def addProductCard(self, rowNumber, colNumber, name, qt, p, pic_path):
        self.frame_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setMinimumSize(QtCore.QSize(200, 280))
        self.frame_2.setMaximumSize(QtCore.QSize(200, 280))
        self.frame_2.setStyleSheet("border-radius:15px;\n"
                                   "background-color:white;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pPic = QtWidgets.QLabel(self.frame_2)
        self.pPic.setGeometry(QtCore.QRect(40, 30, 121, 111))
        self.pPic.setText("")
        self.pPic.setPixmap(QtGui.QPixmap(pic_path))
        self.pPic.setScaledContents(True)
        self.pPic.setObjectName("pPic")
        self.pName = QtWidgets.QLabel(self.frame_2)
        self.pName.setGeometry(QtCore.QRect(40, 160, 120, 33))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pName.setFont(font)
        self.pName.setAlignment(QtCore.Qt.AlignCenter)
        self.pName.setObjectName("pName")
        self.pPrice = QtWidgets.QLabel(self.frame_2)
        self.pPrice.setGeometry(QtCore.QRect(110, 190, 101, 33))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pPrice.setFont(font)
        self.pPrice.setStyleSheet("color:#333")
        self.pPrice.setAlignment(QtCore.Qt.AlignCenter)
        self.pPrice.setObjectName("pPrice")
        self.editBtn = QtWidgets.QPushButton(self.frame_2)
        self.editBtn.setGeometry(QtCore.QRect(60, 220, 40, 40))
        self.editBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.editBtn.setStyleSheet("background:none;")
        self.editBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\media/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.editBtn.setIcon(icon1)
        self.editBtn.setObjectName("editBtn")
        self.delBtn = QtWidgets.QPushButton(self.frame_2)
        self.delBtn.setGeometry(QtCore.QRect(100, 220, 40, 40))
        self.delBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delBtn.setStyleSheet("background:none;")
        self.delBtn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(".\\media/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delBtn.setIcon(icon2)
        self.delBtn.setObjectName("delBtn")
        self.pQuantity = QtWidgets.QLabel(self.frame_2)
        self.pQuantity.setGeometry(QtCore.QRect(10, 190, 81, 33))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pQuantity.setFont(font)
        self.pQuantity.setStyleSheet("color:#333")
        self.pQuantity.setAlignment(QtCore.Qt.AlignCenter)
        self.pQuantity.setObjectName("pQuantity")
        self.gridLayout.addWidget(self.frame_2, rowNumber, colNumber, 1, 1)
        self.pName.setText(name)
        self.pQuantity.setText("EGP " + str(p))
        self.pPrice.setText("QT: " + str(qt))

    def setupUi(self, managementDashboard):
        managementDashboard.setObjectName("managementDashboard")
        managementDashboard.resize(720, 540)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(managementDashboard.sizePolicy().hasHeightForWidth())
        managementDashboard.setSizePolicy(sizePolicy)
        managementDashboard.setMinimumSize(QtCore.QSize(720, 540))
        managementDashboard.setMaximumSize(QtCore.QSize(720, 540))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\media/favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        managementDashboard.setWindowIcon(icon)
        managementDashboard.setAutoFillBackground(False)
        managementDashboard.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(managementDashboard)
        self.centralwidget.setStyleSheet("margin:0;\n"
                                         "padding:0;\n"
                                         "")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 700, 100))
        self.frame.setStyleSheet("background-color:#eaeaea;\n"
                                 "border:2px solid grey;\n"
                                 "border-radius:25px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(40, 25, 321, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:#444;\n"
                                 "border:none;\n"
                                 "")
        self.label.setObjectName("label")
        self.changePassBtn = QtWidgets.QPushButton(self.frame)
        self.changePassBtn.setGeometry(QtCore.QRect(410, 30, 145, 40))
        self.changePassBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.changePassBtn.setStyleSheet("font-size:14px;\n"
                                         "background-color:rgb(60,60,60);\n"
                                         "color:white;\n"
                                         "border-radius:10px;\n"
                                         "")
        self.changePassBtn.setObjectName("changePassBtn")
        self.analysisBtn = QtWidgets.QPushButton(self.frame)
        self.analysisBtn.setGeometry(QtCore.QRect(560, 30, 101, 40))
        self.analysisBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.analysisBtn.setStyleSheet("font-size:14px;\n"
                                       "background-color:rgb(60,60,60);\n"
                                       "color:white;\n"
                                       "border-radius:10px;\n"
                                       "")
        self.analysisBtn.setObjectName("analysisBtn")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 130, 114, 33))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 180, 701, 351))
        self.scrollArea.setStyleSheet("background-color:#e5e5e5;")
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 678, 349))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        col = 0
        row = 0
        for i in management.products:
            self.addProductCard(row, col, i["name"], i["quantity"], i["price"], i["pic_path"])
            if col < 2:
                col += 1
            else:
                col = 0
                row += 1
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.addBtn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.addPW())
        self.addBtn.setGeometry(QtCore.QRect(660, 130, 40, 40))
        self.addBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addBtn.setStyleSheet("background:none;")
        self.addBtn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(".\\media/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addBtn.setIcon(icon3)
        self.addBtn.setObjectName("addBtn")
        managementDashboard.setCentralWidget(self.centralwidget)

        self.retranslateUi(managementDashboard)
        QtCore.QMetaObject.connectSlotsByName(managementDashboard)

    def retranslateUi(self, managementDashboard):
        _translate = QtCore.QCoreApplication.translate
        managementDashboard.setWindowTitle(_translate("managementDashboard", "Supermarket System by <X-Coders/>"))
        self.label.setText(_translate("managementDashboard", "Management Dashboard"))
        self.changePassBtn.setText(_translate("managementDashboard", "Change password"))
        self.analysisBtn.setText(_translate("managementDashboard", "Analysis"))
        self.label_2.setText(_translate("managementDashboard", "Products"))


class Ui_addProduct(object):
    def goToDashboard(self):
        addProduct.hide()
        managementDashboard.show()

    def addProduct(self):
        pname = self.pname.text()
        pquantity = self.pquantity.text()
        pprice = self.pprice.text()
        shutil.copy(self.filename, "./media")
        dirs = self.filename.split("/")
        ppath = "./media/" + dirs[-1]
        if management.addProduct(pname, pquantity, pprice, ppath): #and pname != "" and int(pquantity) != 0 and int(
        #         pprice) != 0 and ppath != "":
            management.products = management.viewAllProducts()
            managementDashboard.close()
            ui = Ui_managementDashboard()
            ui.setupUi(managementDashboard)
            addProduct.hide()
            managementDashboard.show()
            self.pname.clear()
            self.pprice.clear()
            self.pquantity.clear()
        else:
            self.label_6.show()

    def getPic(self):
        self.filename = QtWidgets.QFileDialog.getOpenFileName(filter="Images (*.png *.jpeg *.jpg *jfif)")[0]

    def setupUi(self, addProduct):
        addProduct.setObjectName("addProduct")
        addProduct.resize(720, 540)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(addProduct.sizePolicy().hasHeightForWidth())
        addProduct.setSizePolicy(sizePolicy)
        addProduct.setMinimumSize(QtCore.QSize(720, 540))
        addProduct.setMaximumSize(QtCore.QSize(720, 540))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\media/favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        addProduct.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(addProduct)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(180, 50, 340, 100))
        self.frame.setStyleSheet("background:#e5e5e5;\n"
                                 "border-radius:25px;\n"
                                 "border: 1px solid black;\n"
                                 "")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(70, 33, 200, 34))
        self.label.setStyleSheet("border:none;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(180, 170, 340, 291))
        self.frame_2.setStyleSheet("#frame_2{\n"
                                   "background: #e5e5e5;\n"
                                   "border-radius:25px;\n"
                                   "border:1px solid black\n"
                                   "}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pname = QtWidgets.QLineEdit(self.frame_2)
        self.pname.setGeometry(QtCore.QRect(150, 50, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pname.setFont(font)
        self.pname.setObjectName("pname")
        self.pquantity = QtWidgets.QSpinBox(self.frame_2)
        self.pquantity.setGeometry(QtCore.QRect(150, 90, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.pquantity.setFont(font)
        self.pquantity.setObjectName("pquantity")
        self.pprice = QtWidgets.QDoubleSpinBox(self.frame_2)
        self.pprice.setGeometry(QtCore.QRect(150, 130, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pprice.setFont(font)
        self.pprice.setObjectName("pprice")
        self.uploadBtn = QtWidgets.QPushButton(self.frame_2, clicked=self.getPic)
        self.uploadBtn.setGeometry(QtCore.QRect(150, 170, 140, 30))
        self.uploadBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.uploadBtn.setFont(font)
        self.uploadBtn.setObjectName("uploadBtn")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(50, 50, 91, 33))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(50, 90, 91, 33))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(50, 130, 91, 33))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(50, 165, 91, 33))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.addBtn = QtWidgets.QPushButton(self.frame_2, clicked=lambda: self.addProduct())
        self.addBtn.setGeometry(QtCore.QRect(100, 220, 145, 42))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.addBtn.setFont(font)
        self.addBtn.setStyleSheet("#addBtn{\n"
                                  "background-color:rgb(60,60,60);\n"
                                  "border-radius:10px;\n"
                                  "border:none;\n"
                                  "color:white;\n"
                                  "}\n"
                                  "#addBtn::hover{\n"
                                  "background-color:rgb(0,0,0);\n"
                                  "}")
        self.addBtn.setObjectName("addBtn")
        self.addBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backBtn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.goToDashboard())
        self.backBtn.setGeometry(QtCore.QRect(10, 20, 81, 71))
        self.backBtn.setStyleSheet("background-color:none;\n"
                                   "border:none")
        self.backBtn.setText("")
        self.backBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\media/back arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backBtn.setIcon(icon1)
        self.backBtn.setIconSize(QtCore.QSize(60, 60))
        self.backBtn.setObjectName("backBtn")
        addProduct.setCentralWidget(self.centralwidget)
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(30, 10, 261, 33))
        self.label_6.setStyleSheet("font-size:12px;\n"
                                   "color:red;")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_6.hide()
        self.retranslateUi(addProduct)
        QtCore.QMetaObject.connectSlotsByName(addProduct)

    def retranslateUi(self, addProduct):
        _translate = QtCore.QCoreApplication.translate
        addProduct.setWindowTitle(_translate("addProduct", "Supermarket System by <X-Coders/>"))
        self.label.setText(_translate("addProduct", "Product Adding"))
        self.uploadBtn.setText(_translate("addProduct", "Upload"))
        self.label_2.setText(_translate("addProduct", "Name:"))
        self.label_3.setText(_translate("addProduct", "Quantity:"))
        self.label_4.setText(_translate("addProduct", "Price:"))
        self.label_5.setText(_translate("addProduct", "Picture:"))
        self.addBtn.setText(_translate("addProduct", "Add"))
        self.label_6.setText(_translate("addProduct", "Product exist or info missing"))


if __name__ == "__main__":
    import sys

    management = manage.Manage()
    app = QtWidgets.QApplication(sys.argv)

    addProduct = QtWidgets.QMainWindow()
    ui = Ui_addProduct()
    ui.setupUi(addProduct)

    manageLogin = QtWidgets.QMainWindow()
    ui = Ui_manageLogin()
    ui.setupUi(manageLogin)

    managementDashboard = QtWidgets.QMainWindow()
    ui = Ui_managementDashboard()
    ui.setupUi(managementDashboard)

    customerLogin = QtWidgets.QMainWindow()
    ui = Ui_customerLogin()
    ui.setupUi(customerLogin)

    homeWindow = QtWidgets.QMainWindow()
    ui = Ui_homeWindow()
    ui.setupUi(homeWindow)
    homeWindow.show()
    sys.exit(app.exec_())
