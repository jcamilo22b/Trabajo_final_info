# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QFrame, QHBoxLayout, QPushButton, QLabel, QLineEdit, QWidget
# from PyQt5.QtGui import QPixmap
# from PyQt5.QtCore import Qt

# class MainWindow(QMainWindow, Ui_MainWindow):
#     def __init__(self):
#         super(MainWindow, self).__init__()
#         self.setupUi(self)

#         # Conectar el botón a una función (puedes personalizar esto)
#         self.pushButton.clicked.connect(self.mostrar_datos)

#     def mostrar_datos(self):
#         # Obtener los datos de los QLineEdit y mostrarlos en la consola
#         usuario = self.lineEdit.text()
#         contrasena = self.lineEdit_2.text()
#         print("Usuario:", usuario)
#         print("Contraseña:", contrasena)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QUiLoader
from PyQt5.QtCore import QFile

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Cargar la interfaz de usuario desde el archivo .ui
        ui_file = QFile("login.ui")  # Reemplaza "tu_archivo.ui" con el nombre real de tu archivo
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.ui = loader.load(ui_file, self)
        ui_file.close()

        # Configurar la interfaz de usuario y conectar señales y ranuras aquí

        # Por ejemplo, conectar el botón a una función
    #     

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

