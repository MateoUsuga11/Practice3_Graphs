import sys
import random
from PyQt5 import QtWidgets, QtGui, QtCore
from grafos_ui import Ui_MainWindow
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsEllipseItem, QGraphicsLineItem, QGraphicsTextItem, QGraphicsItem, QTableWidgetItem


class Nodo(QGraphicsEllipseItem):
    def __init__(self, x, y, radius, id, app):
        super().__init__(-radius, -radius, 2 * radius, 2 * radius)
        self.setBrush(QtGui.QBrush(QtGui.QColor("lightblue")))
        self.setPen(QtGui.QPen(QtCore.Qt.black))
        self.id = id
        self.setFlag(QGraphicsEllipseItem.ItemIsMovable)
        self.setFlag(QGraphicsEllipseItem.ItemSendsGeometryChanges)
        self.text_item = QGraphicsTextItem(f"Nodo {self.id}", self)
        self.text_item.setPos(-10, -10)
        self.app = app
        self.aristas = []

    def agregar_arista(self, arista):
        self.aristas.append(arista)

    def itemChange(self, change, value):
        if change == QGraphicsItem.ItemPositionChange:
            for arista in self.aristas:
                arista.actualizar_posiciones()
        return super().itemChange(change, value)


class Arista(QGraphicsLineItem):
    def __init__(self, nodo1, nodo2, peso, scene):
        super().__init__()
        self.nodo1 = nodo1
        self.nodo2 = nodo2
        self.peso = peso
        self.scene = scene

        self.text_item = QGraphicsTextItem(str(self.peso))
        self.scene.addItem(self.text_item)

        self.actualizar_posiciones()
        self.setFlag(QGraphicsLineItem.ItemIsSelectable)
        self.setPen(QtGui.QPen(QtCore.Qt.black))

    def actualizar_posiciones(self):
        x1, y1 = self.nodo1.scenePos().x(), self.nodo1.scenePos().y()
        x2, y2 = self.nodo2.scenePos().x(), self.nodo2.scenePos().y()
        self.setLine(x1, y1, x2, y2)
        self.text_item.setPos((x1 + x2) / 2, (y1 + y2) / 2)

    def mousePressEvent(self, event):
        self.setPen(QtGui.QPen(QtCore.Qt.red, 3))
        self.nodo1.setPen(QtGui.QPen(QtCore.Qt.red, 3))
        self.nodo2.setPen(QtGui.QPen(QtCore.Qt.red, 3))
        super().mousePressEvent(event)


class GrafoApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(GrafoApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Scene / GraphicsView
        self.graphicsView = self.ui.graphicsView
        self.scene = QGraphicsScene()
        self.graphicsView.setScene(self.scene)

        # Conexiones de botones
        self.ui.btnPintarGrafo.clicked.connect(self.dibujar_grafo)
        self.ui.btnGenerarAdyacencia.clicked.connect(self.generar_matriz_adyacencia)
        self.ui.btnGenerarK2.clicked.connect(lambda: self.generar_matriz_k(2))
        self.ui.btnGenerarK3.clicked.connect(lambda: self.generar_matriz_k(3))
        self.ui.tableWidget.horizontalHeader().sectionClicked.connect(self.llenar_matriz_aleatoria)

        # Conexión para resaltar caminos al hacer clic en celdas
        self.ui.tableK2.cellClicked.connect(lambda r, c: self.resaltar_camino(r, c, 2))
        self.ui.tableK3.cellClicked.connect(lambda r, c: self.resaltar_camino(r, c, 3))

        # Listas de nodos y aristas
        self.nodos = []
        self.aristas = []

        # Ajustes visuales de tablas
        self._ajustar_tablas_visuales()

        # Tooltips informativos
        self._agregar_tooltips()

    # ------------------ TOOLTIP HELPERS ------------------
    def _agregar_tooltips(self):
        """Agrega tooltips a botones y tablas."""
        self.ui.btnPintarGrafo.setToolTip("Dibuja el grafo en base a la matriz de pesos.")
        self.ui.btnGenerarAdyacencia.setToolTip("Genera la matriz de adyacencia (1 si hay conexión).")
        self.ui.btnGenerarK2.setToolTip("Calcula la matriz A² — caminos de longitud 2.")
        self.ui.btnGenerarK3.setToolTip("Calcula la matriz A³ — caminos de longitud 3.")
        self.ui.tableWidget.setToolTip("Matriz principal de pesos entre nodos.")
        self.ui.tableAdyacencia.setToolTip("Matriz binaria que muestra conexiones directas entre nodos.")
        self.ui.tableK2.setToolTip("Cantidad de caminos posibles de longitud 2 entre nodos.")
        self.ui.tableK3.setToolTip("Cantidad de caminos posibles de longitud 3 entre nodos.")

    # ------------------ UTILIDADES DE MATRICES ------------------
    def obtener_matriz_pesos(self):
        try:
            filas = self.ui.tableWidget.rowCount()
            columnas = self.ui.tableWidget.columnCount()
            matriz = []
            for i in range(filas):
                fila = []
                for j in range(columnas):
                    item = self.ui.tableWidget.item(i, j)
                    valor = int(item.text()) if item and item.text().strip().lstrip('-').isdigit() else 0
                    fila.append(valor)
                matriz.append(fila)
            return matriz
        except Exception as e:
            print("Error al obtener matriz de pesos:", e)
            return []

    def calcular_adyacencia(self, matriz_pesos):
        n = len(matriz_pesos)
        A = [[1 if matriz_pesos[i][j] != 0 else 0 for j in range(n)] for i in range(n)]
        return A

    def multiplicar_matrices(self, A, B):
        n = len(A)
        C = [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
        return C

    # ------------------ RELLENAR TABLAS ------------------
    def llenar_qtable_con_matriz(self, qtable, matriz):
        if matriz is None:
            return
        n = len(matriz)
        qtable.setRowCount(n)
        qtable.setColumnCount(n)
        qtable.setHorizontalHeaderLabels([str(i + 1) for i in range(n)])
        qtable.setVerticalHeaderLabels([str(i + 1) for i in range(n)])
        qtable.horizontalHeader().setDefaultSectionSize(80)
        qtable.verticalHeader().setDefaultSectionSize(40)
        for i in range(n):
            for j in range(n):
                item = QTableWidgetItem(str(matriz[i][j]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                qtable.setItem(i, j, item)

    # ------------------ FUNCIONES DE BOTONES ------------------
    def generar_matriz_adyacencia(self):
        pesos = self.obtener_matriz_pesos()
        if not pesos:
            return
        A = self.calcular_adyacencia(pesos)
        self.llenar_qtable_con_matriz(self.ui.tableAdyacencia, A)

    def generar_matriz_k(self, k):
        pesos = self.obtener_matriz_pesos()
        if not pesos:
            return
        A = self.calcular_adyacencia(pesos)
        if k == 2:
            Ak = self.multiplicar_matrices(A, A)
            self.llenar_qtable_con_matriz(self.ui.tableK2, Ak)
        elif k == 3:
            A2 = self.multiplicar_matrices(A, A)
            Ak = self.multiplicar_matrices(A2, A)
            self.llenar_qtable_con_matriz(self.ui.tableK3, Ak)

    # ------------------ DIBUJAR GRAFO ------------------
    def dibujar_grafo(self):
        try:
            self.scene.clear()
            self.nodos.clear()
            self.aristas.clear()
            matriz = self.obtener_matriz_pesos()
            if not matriz:
                return
            self.dibujar_nodos_y_aristas(matriz)
        except Exception as e:
            print(f"Error al dibujar el grafo: {e}")

    def dibujar_nodos_y_aristas(self, matriz):
        try:
            num_nodos = len(matriz)
            radius = 20
            width = self.graphicsView.width() - 100
            height = self.graphicsView.height() - 100
            for i in range(num_nodos):
                x = random.randint(50, max(50, width))
                y = random.randint(50, max(50, height))
                nodo = Nodo(x, y, radius, i + 1, self)
                nodo.setPos(x, y)
                self.scene.addItem(nodo)
                self.nodos.append(nodo)
            for i in range(num_nodos):
                for j in range(i + 1, num_nodos):
                    peso = matriz[i][j]
                    if peso > 0:
                        nodo1 = self.nodos[i]
                        nodo2 = self.nodos[j]
                        arista = Arista(nodo1, nodo2, peso, self.scene)
                        self.aristas.append(arista)
                        self.scene.addItem(arista)
                        nodo1.agregar_arista(arista)
                        nodo2.agregar_arista(arista)
        except Exception as e:
            print(f"Error al dibujar nodos y aristas: {e}")

    # ------------------ MATRIZ ALEATORIA ------------------
    def llenar_matriz_aleatoria(self, index):
        try:
            filas = self.ui.tableWidget.rowCount()
            columnas = self.ui.tableWidget.columnCount()
            for i in range(filas):
                for j in range(columnas):
                    if i == j:
                        self.ui.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem('0'))
                    else:
                        crear = random.random() < 0.6
                        valor_aleatorio = random.randint(1, 20) if crear else 0
                        self.ui.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(valor_aleatorio)))
        except Exception as e:
            print(f"Error al llenar la matriz: {e}")

    # ------------------ RESALTAR CAMINO ------------------
    def resaltar_camino(self, fila, columna, k):
        """Resalta visualmente los nodos conectados por caminos de longitud k."""
        try:
            # Limpiar colores previos
            for nodo in self.nodos:
                nodo.setBrush(QtGui.QBrush(QtGui.QColor("lightblue")))
            for arista in self.aristas:
                arista.setPen(QtGui.QPen(QtCore.Qt.black, 1))

            # Obtener valor de la celda
            item = self.ui.tableK2.item(fila, columna) if k == 2 else self.ui.tableK3.item(fila, columna)
            if not item or not item.text().isdigit():
                return
            valor = int(item.text())
            if valor == 0:
                return

            # Resaltar nodos
            origen = self.nodos[fila]
            destino = self.nodos[columna]
            origen.setBrush(QtGui.QBrush(QtGui.QColor("#4CAF50")))
            destino.setBrush(QtGui.QBrush(QtGui.QColor("#FF5722")))

            # Si hay arista directa
            for arista in self.aristas:
                if (arista.nodo1 == origen and arista.nodo2 == destino) or (arista.nodo1 == destino and arista.nodo2 == origen):
                    arista.setPen(QtGui.QPen(QtCore.Qt.red, 3))

            # Tooltip informativo
            QtWidgets.QToolTip.showText(QtGui.QCursor.pos(),
                                        f"Caminos de longitud {k} entre Nodo {fila+1} y Nodo {columna+1}: {valor}")

        except Exception as e:
            print("Error al resaltar camino:", e)

    # ------------------ AJUSTES VISUALES ------------------
    def _ajustar_tablas_visuales(self):
        try:
            for t in (self.ui.tableWidget, self.ui.tableAdyacencia, self.ui.tableK2, self.ui.tableK3):
                t.horizontalHeader().setDefaultSectionSize(80)
                t.verticalHeader().setDefaultSectionSize(40)
        except Exception:
            pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = GrafoApp()
    window.show()
    sys.exit(app.exec_())



