from PySide2 import QtCore, QtGui, QtWidgets
import sys
from index import Ui_Form
from choose import Choose

form
class Main(object):
	def __init__(self):
		Form = Ui_Form()
		form = Form

	def to_index():
		form.hide()

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv) # 创建一个QApplication，也就是你要开发的软件app
	MainWindow = QtWidgets.QMainWindow()
	window = Ui_Form()
	window.setupUi(form)
	MainWindow.show()
	sys.exit(app.exec_())