import sys
from PyQt5.QtWidgets import QMessageBox,QFileDialog,QAction, QTextEdit, QApplication, QMainWindow

class NotepadV2(QMainWindow):
	def __init__(self):
		super().__init__()
		self.InitializeUI()

	def InitializeUI(self):
		self.setGeometry(100, 100, 300, 400)
		self.setWindowTitle("CYRIL-TextEditor")

		self.notepadWidgets()
		self.notepadmenu()

		self.show()

	def notepadWidgets(self):
		self.text_field = QTextEdit()
		self.setCentralWidget(self.text_field)

	def notepadmenu(self):
		#create actions for file menu
		new_action = QAction('Clear file', self)
		new_action.setShortcut('ctrl+N')
		new_action.triggered.connect(self.clearText)

		open_action = QAction('Open Files', self)
		open_action.setShortcut('ctrl+O')
		open_action.triggered.connect(self.openFile)

		save_action = QAction('Save', self)
		save_action.setShortcut('ctrl+S')
		save_action.triggered.connect(self.saveText)

		exit_action = QAction('Exit', self)
		exit_action.setShortcut('ctrl+Q')
		#exit_action.triggered.connect(self.exit)

		#functions for edit menu
		undo_action = QAction('undo', self)
		undo_action.setShortcut('ctrl+z')
		#undo_action.triggered.connect(self.undo)

		redo_action = QAction('redo', self)
		redo_action.setShortcut('ctrl+Y')
		#redo_action.triggered.connect(self.redo)

		cut_action = QAction('cut', self)
		cut_action.setShortcut('ctrl+X')
		#cut_action.triggered.connect(self.cut)

		copy_action = QAction('copy', self)
		copy_action.setShortcut('ctrl+C')
		#copy_action.triggered.connect(self.copy)
		
		paste_action = QAction('paste', self)
		paste_action.setShortcut('ctrl+V')
		#paste_action.triggered.connect(self.paste)


		find_action = QAction('find', self)
		find_action.setShortcut('ctrl+F')
		#find_action.triggered.connect(self.find)

		#create actions for tools menu
		font_action = QAction('Fonts', self)
		font_action.setShortcut('Ctrl+T')
		#font_action.triggered.connect(self.chooseFont)

		color_action = QAction('Colors', self)
		color_action.setShortcut('Ctrl+shift+C')
		#color_action.triggered.connect(self.chooseFontColor)


		highlight_actiom = QAction('Highlight', self)
		highlight_actiom.setShortcut('Ctrl+shift+H')
		#highlight_actiom.triggered.connect(self.chooseFontBackgroundColor)
		
		about_action = QAction('About', self)
		#about_action.triggered.connect(self.aboutDialog)

		#create menu bar
		menu_bar = self.menuBar()

		#Create menu add actions
		filemenu = menu_bar.addMenu('File')
		filemenu.addAction(new_action)
		filemenu.addSeparator()
		filemenu.addAction(open_action)
		filemenu.addAction(save_action)
		filemenu.addSeparator()
		filemenu.addAction(exit_action)

		editmenu = menu_bar.addMenu('Edit')
		editmenu.addAction(undo_action)
		editmenu.addAction(redo_action)
		editmenu.addSeparator()
		editmenu.addAction(copy_action)
		editmenu.addAction(paste_action)
		editmenu.addAction(cut_action)
		editmenu.addSeparator()
		editmenu.addAction(find_action)

		toolsmenu = menu_bar.addMenu('Tools')
		toolsmenu.addAction(font_action)
		#toolsmenu.addSeparator()
		toolsmenu.addAction(color_action)
		#toolsmenu.addSeparator()
		toolsmenu.addAction(highlight_actiom)


		aboutmenu = menu_bar.addMenu('Help')
		aboutmenu.addAction(about_action)

	def openFile(self):
		filename, _ = QFileDialog.getOpenFileName(self, 'Open file', '', 'HTML files(*.html);;TextFiles (*.txt);;Python File(*.py);;All Files(*)')

		if filename:
			with open(filename,'r') as f:
				notepad_txt = f.read()
				self.text_field.setText(notepad_txt)
		else:
			QMessageBox.information(self, 'error', 'unable to open the file', QMessageBox.Ok)	
	
	def saveText(self):
		filename,_=QFileDialog.getSaveFileName(self, 'save', '','Text file(*.txt);;html files(*.html)')

		if filename.endswith('.txt'):
			notepad_txt = self.text_field.toPlainText()
			with open(filename, 'w') as f:
				f.write(notepad_txt)

		elif filename.endswith('.html'):
			notepad_txt = self.text_field.toHtml()
			with open(filename, 'w') as f:
				f.write(notepad_txt)

		else:
			QMessageBox.information(self, 'error', 'unable to save', QMessageBox.Ok)

	def clearText(self):
		answer = QMessageBox.question(self, "clear","Do you want to clear everything?", QMessageBox.No | QMessageBox.Yes, QMessageBox.Yes)

		if answer == QMessageBox.Yes:
			self.text_field.clear()
		else:
			pass

#	def exit(self):
# Hello this is a a text editor written by  Cyril Maxwel with python and  PyQt5.

# LEAVE A COMMENT  


#run the application
if __name__=='__main__':
	app = QApplication(sys.argv)
	window = NotepadV2()
	sys.exit(app.exec_())