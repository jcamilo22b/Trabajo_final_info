from PyQt5 import QtWidgets, uic

# Cargar el archivo .ui
app = QtWidgets.QApplication([])
ui_file = "mikeesunaputa.ui"
window = uic.loadUi(ui_file)

# Mostrar la ventana
window.show()

# Ejecutar la aplicación
app.exec()