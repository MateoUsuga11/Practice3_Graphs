from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 1150)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # === LOGO UNIVERSIDAD ===
        self.lblLogo = QtWidgets.QLabel(self.centralwidget)
        self.lblLogo.setGeometry(QtCore.QRect(50, -10, 150, 100))
        self.lblLogo.setPixmap(QtGui.QPixmap("logo_eafit_blanco.png"))
        self.lblLogo.setScaledContents(True)
        self.lblLogo.setObjectName("lblLogo")

        # === TÍTULO PRINCIPAL ===
        self.lblTtitulo = QtWidgets.QLabel(self.centralwidget)
        self.lblTtitulo.setGeometry(QtCore.QRect(250, 10, 800, 60))
        self.lblTtitulo.setStyleSheet("font: 75 20pt 'MS Shell Dlg 2'; color:rgb(0, 85, 255);")
        self.lblTtitulo.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTtitulo.setObjectName("lblTtitulo")

        # === GROUPBOX: MATRIZ DE PESOS ===
        self.groupPesos = QtWidgets.QGroupBox(self.centralwidget)
        self.groupPesos.setGeometry(QtCore.QRect(30, 90, 750, 260))
        self.groupPesos.setStyleSheet("QGroupBox { font: 14pt 'MS Shell Dlg 2'; color: #1a73e8; }")
        self.groupPesos.setObjectName("groupPesos")

        self.tableWidget = QtWidgets.QTableWidget(self.groupPesos)
        self.tableWidget.setGeometry(QtCore.QRect(30, 50, 500, 180))
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")

        self.btnPintarGrafo = QtWidgets.QPushButton(self.groupPesos)
        self.btnPintarGrafo.setGeometry(QtCore.QRect(570, 110, 140, 40))
        self.btnPintarGrafo.setObjectName("btnPintarGrafo")

        # === GROUPBOX: MATRIZ DE ADYACENCIA ===
        self.groupAdyacencia = QtWidgets.QGroupBox(self.centralwidget)
        self.groupAdyacencia.setGeometry(QtCore.QRect(30, 370, 750, 260))
        self.groupAdyacencia.setStyleSheet("QGroupBox { font: 14pt 'MS Shell Dlg 2'; color: #1a73e8; }")
        self.groupAdyacencia.setObjectName("groupAdyacencia")

        self.tableAdyacencia = QtWidgets.QTableWidget(self.groupAdyacencia)
        self.tableAdyacencia.setGeometry(QtCore.QRect(30, 50, 500, 180))
        self.tableAdyacencia.setRowCount(4)
        self.tableAdyacencia.setColumnCount(4)
        self.tableAdyacencia.setObjectName("tableAdyacencia")

        self.btnGenerarAdyacencia = QtWidgets.QPushButton(self.groupAdyacencia)
        self.btnGenerarAdyacencia.setGeometry(QtCore.QRect(570, 110, 140, 40))
        self.btnGenerarAdyacencia.setObjectName("btnGenerarAdyacencia")

        # === GROUPBOX: MATRIZ K=2 ===
        self.groupK2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupK2.setGeometry(QtCore.QRect(30, 650, 750, 260))
        self.groupK2.setStyleSheet("QGroupBox { font: 14pt 'MS Shell Dlg 2'; color: #1a73e8; }")
        self.groupK2.setObjectName("groupK2")

        self.tableK2 = QtWidgets.QTableWidget(self.groupK2)
        self.tableK2.setGeometry(QtCore.QRect(30, 50, 500, 180))
        self.tableK2.setRowCount(4)
        self.tableK2.setColumnCount(4)
        self.tableK2.setObjectName("tableK2")

        self.btnGenerarK2 = QtWidgets.QPushButton(self.groupK2)
        self.btnGenerarK2.setGeometry(QtCore.QRect(570, 110, 140, 40))
        self.btnGenerarK2.setObjectName("btnGenerarK2")

        # === GROUPBOX: MATRIZ K=3 ===
        self.groupK3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupK3.setGeometry(QtCore.QRect(30, 930, 750, 260))
        self.groupK3.setStyleSheet("QGroupBox { font: 14pt 'MS Shell Dlg 2'; color: #1a73e8; }")
        self.groupK3.setObjectName("groupK3")

        self.tableK3 = QtWidgets.QTableWidget(self.groupK3)
        self.tableK3.setGeometry(QtCore.QRect(30, 50, 500, 180))
        self.tableK3.setRowCount(4)
        self.tableK3.setColumnCount(4)
        self.tableK3.setObjectName("tableK3")

        self.btnGenerarK3 = QtWidgets.QPushButton(self.groupK3)
        self.btnGenerarK3.setGeometry(QtCore.QRect(570, 110, 140, 40))
        self.btnGenerarK3.setObjectName("btnGenerarK3")

        # === VIEW GRAFO ===
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(800, 90, 700, 800))
        self.graphicsView.setObjectName("graphicsView")

        # === MENUBAR Y STATUSBAR ===
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # === ESTILO GLOBAL ===
        MainWindow.setStyleSheet("""
            QWidget {
                background-color: #f3f6fb;
                font-family: 'Segoe UI';
                font-size: 13pt;
            }
            QLabel {
                font-size: 15pt;
            }
            QPushButton {
                background-color: #1a73e8;
                color: white;
                font-size: 10pt;
                border-radius: 6px;
                padding: 6px 10px;
            }
            QPushButton:hover {
                background-color: #1669c1;
            }
            QGroupBox {
                font-size: 14pt;
                font-weight: bold;
                color: #1a73e8;
                border: 2px solid #1a73e8;
                border-radius: 8px;
                margin-top: 10px;
                padding-top: 10px;
            }
            QTableWidget {
                font-size: 13pt;
                border: 1px solid #b0b0b0;
            }
        """)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Visualizador de Grafos"))
        self.lblTtitulo.setText(_translate("MainWindow", "Grafos - Por Mateo Usuga y Diego Peña"))
        self.groupPesos.setTitle(_translate("MainWindow", "Matriz de Pesos"))
        self.groupAdyacencia.setTitle(_translate("MainWindow", "Matriz de Adyacencia"))
        self.groupK2.setTitle(_translate("MainWindow", "Matriz K = 2"))
        self.groupK3.setTitle(_translate("MainWindow", "Matriz K = 3"))
        self.btnPintarGrafo.setText(_translate("MainWindow", "Dibujar Grafo"))
        self.btnGenerarAdyacencia.setText(_translate("MainWindow", "Generar Adyacencia"))
        self.btnGenerarK2.setText(_translate("MainWindow", "Generar K=2"))
        self.btnGenerarK3.setText(_translate("MainWindow", "Generar K=3"))






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
