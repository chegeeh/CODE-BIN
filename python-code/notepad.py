import sys
from PyQt5.QtWidgets import QFileDialog, QApplication, QWidget, QTextEdit, QLabel, QPushButton, QMessageBox

class Notepad(QWidget):
	def __init__(self):
		super().__init__()
		self.InitializeUI() #SETUP OUR FUNCTION TO BUILD  A WINDOW

	def InitializeUI(self):
		self.setGeometry(100, 100, 300, 400)
		self.setWindowTitle('notepad v1')
		#setup up yor notepad widgets	
		self.notepadWidgets()
		
		self.show()

	def notepadWidgets(self):
		newButton = QPushButton("new", self)
		newButton.move(10, 20)
		newButton.clicked.connect(self.clearText)

		saveButton = QPushButton("save", self)
		saveButton.move(100,20)
		saveButton.clicked.connect(self.saveText)
		
		self.text_Field = QTextEdit(self)
		self.text_Field.resize(280, 330)
		self.text_Field.move(10, 60)

	def clearText(self):
		answer = QMessageBox.question(self, "clear text","Do you want to clear text?", QMessageBox.No | QMessageBox.Yes, QMessageBox.Yes)
		if answer == QMessageBox.Yes:
			self.text_Field.clear()
		else:
			pass

	def saveText(self):
		options =QFileDialog.Options()
		notepad_Text =self.text_Field.toPlainText()

		filename, _=QFileDialog.getSaveFileName(self, "save file", "", "All files(*);;textfiles(*.txt)", options=options) 	  

		if filename:
			with open(filename,"w") as f:
				f.write(notepad_Text)
#run the program
if __name__=="__main__":
	app=QApplication(sys.argv)
	window = Notepad()
	sys.exit(app.exec_())
