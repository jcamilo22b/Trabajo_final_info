# #login

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QFrame, QHBoxLayout, QPushButton, QLabel, QLineEdit, QWidget, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("login.ui", self)  

        
        self.ingresar.clicked.connect(self.mostrar_datos)

    def mostrar_datos(self):
        
        usuario = self.line_user.text()
        contrasena = self.line_password.text()
        
     #Verificar 
        if usuario == "medicoAnalista" and contrasena == "bio1234":
            # abrir la ventana principal #############################################
            print(" ESTEBAN SAPA") 
            # meter aqui lo que sigueeeeeeeeeeeeeee
        else:
            # Credenciales incorrectas, mostrar un mensaje de error
            print("Credenciales incorrectas")
            self.mostrar_mensaje_error()

    def mostrar_mensaje_error(self):
        mensaje = QMessageBox()
        mensaje.setIcon(QMessageBox.Warning)
        mensaje.setWindowTitle("Error de autenticación")
        mensaje.setText("Usuario o contraseña incorrectos. Por favor, inténtalo de nuevo.")
        mensaje.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())




