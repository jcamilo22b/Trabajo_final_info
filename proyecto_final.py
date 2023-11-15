#login
# from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit 
# from PyQt5.QtGui import QGuiApplication, QIcon
# from PyQt5 import QtCore, QtWidgets
# from PyQt5.uic import loadUi
# from PyQt5.QtCore import Qt
# import sys

# class Login(QMainWindow):
#     def __init__(self):
#         super(Login, self)._init_()
#         loadUi('login.ui',self)

######################################################
# from PyQt5.QtWidgets import QMainWindow
# from PyQt5.uic import loadUi

# class Login(QMainWindow):
#     def __init__(self):
#         super(Login, self)._init_()
#         loadUi('login.ui', self)

# if __name__ == "__main__":
#     import sys
#     from PyQt5.QtWidgets import QApplication, QWidget

#     app = QApplication(sys.argv)
#     window = QWidget()
#     window.show()
#     sys.exit(app.exec_())
#me aparece error con el qlineEdit , Qtcore

###################################################

from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi

class Login(QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        loadUi('login.ui', self)

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    login_window = Login()
    login_window.show()
    sys.exit(app.exec_())





#q

