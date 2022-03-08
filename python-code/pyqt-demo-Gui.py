from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMessageBox, QPushButton
import sys

def dialog():
	mbox = QMessageBox()
	mbox.setWindowTitle('Cyril-Software')
	mbox.setText('Your allegiance has been noted')
	mbox.setDetailedText('you are making great progress,this is coming from the all knowing G')
	mbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
	mbox.exec_()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	w = QWidget()
	w.resize(300,300)
	w.setWindowTitle('Cyril-Software')

	label = QLabel(w)
	label.setText('Press the button below')
	label.move(100,130)
	label.show()

	btn = QPushButton(w)
	btn.setText('info')
	btn.move(110,150)
	btn.show()

	btn.clicked.connect(dialog)

	w.show()
	sys.exit(app.exec_())
