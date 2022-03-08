import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMessageBox, QPushButton

class CreateWindows(QWidget):
	def __init__(self):
		super().__init__()
		self.initializeUI() #setup our function to open up a window

	def initializeUI(self):	
		self.resize(400, 300)
		self.setWindowTitle("cy-fi")
		self.dialogwidgets()
		self.show()

	def dialogwidgets(self):
		pglabel = QLabel(self)
		pglabel.setText("hello there?")
		pglabel.move(110, 20)

		pgbutton = QPushButton(self)
		pgbutton.setText('ok')
		pgbutton.move(110, 50)
		pgbutton.clicked.connect(self.dialog)

	def dialog(self):
		mbox = QMessageBox(self)
		mbox.setWindowTitle('Cyril-Software')
		mbox.setText('Your allegiance has been noted')
		mbox.setDetailedText('you are making great progress,this is coming from the all knowing G')
		mbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
		mbox.exec_()


#run the program
if __name__=='__main__':
	app = QApplication(sys.argv)
	window = CreateWindows()
	sys.exit(app.exec_())