from PyQt5 import QtWidgets, uic, QtCore,QtGui
from PyQt5.QtCore import QTime,QTimer
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *



import copy 
import argparse
import itertools

import sys
import cv2

from ultralytics import YOLO



modeloYOLO = YOLO("ModeloNN_TraductorLSM.pt")

var_buffer = ""
contador_buffer=0
buffer_sal = ""
#-----------------------
#Clase para Hilos en el programa 

class Hilos(QThread):
	Imageupd = pyqtSignal(QImage) 	#Variable para actualizar la imagen cuando se le mande señal
	lbl_detect = pyqtSignal(str)
	def run(self):
		self.hilo_corriendo = True 	#Objeto hilo verdadero
		cap = cv2.VideoCapture(0)	#Capturar video con OpenCV
		while self.hilo_corriendo:
			ret, frame = cap.read()	#leemos la camara
			rp = "N/D"
			if ret:

				flip = cv2.flip(frame,1)
				resultados = modeloYOLO(flip,conf=0.3)
				
				cajas = resultados[0].boxes.cls 
				KK = resultados[0].boxes.data
				print(KK)
				cajitas = str(cajas)
				
				kjita1 = cajitas[8]
				kjita2 = cajitas[9]
				kjita = kjita1+kjita2
				print(kjita)
				if kjita == '0.':
					self.lbl_detect.emit("A")
					
				elif kjita == '1.':
					self.lbl_detect.emit("B")
					
				elif kjita == '2.':
					self.lbl_detect.emit("C")
					
				elif kjita == '3.':
					self.lbl_detect.emit("D")
					
				elif kjita == '4.':
					self.lbl_detect.emit("E")
					
				elif kjita == '5.':
					self.lbl_detect.emit("F")
					
				elif kjita == '6.':
					self.lbl_detect.emit("G")
					
				elif kjita == '7.':
					self.lbl_detect.emit("H")
					
				elif kjita == '8.':
					self.lbl_detect.emit("I")
					
				elif kjita == '9.':
					self.lbl_detect.emit("L")
					
				elif kjita == '10':
					self.lbl_detect.emit("M")
					
				elif kjita == '11':
					self.lbl_detect.emit("N")
					
				elif kjita == '12':
					self.lbl_detect.emit("O")
					
				elif kjita == '13':
					self.lbl_detect.emit("P")
					
				elif kjita == '14':
					self.lbl_detect.emit("R")
					
				elif kjita == '15':
					self.lbl_detect.emit("S")
					#print("B")
				elif kjita == '16':
					self.lbl_detect.emit("T")
					
				elif kjita == '17':
					self.lbl_detect.emit("U")
					
				elif kjita == '18':
					self.lbl_detect.emit("V")
					
				elif kjita == '19':
					self.lbl_detect.emit("W")
					
				elif kjita == '20':
					self.lbl_detect.emit("Y")
					
				else:
					self.lbl_detect.emit("N/D")
					

				Image = cv2.cvtColor(flip, cv2.COLOR_BGR2RGB) 

				convertir_img_to_formatoQT = QImage(Image.data, flip.shape[1], flip.shape[0], QImage.Format_RGB888) #Convertimos la imagen a formato de QT
				picture = convertir_img_to_formatoQT.scaled(350,350, Qt.KeepAspectRatio)	#Reescalamos la imagen
				
				self.Imageupd.emit(picture)				#Enviamos la imagen que optivumos 

	def stop(self):										#Funcion para detener el video
		self.hilo_corriendo = False
		self.quit()


#----------------------

class GUI(QMainWindow): 
	filename = None
	final_image= None
	
	def __init__(self):
		super(GUI, self).__init__()
		uic.loadUi("IG-PT.ui",self)
		
		self.setWindowTitle("Traductor LSM")

		self.pushButtonCargar.clicked.connect(self.StartVideo) #Conectamos la funcion para iniciar el video en lugar de cargar imagen 
		self.pushButtonDetener.clicked.connect(self.DetenerVideo)
		self.pushButtonCargar.setText("Abrir cámara")
		self.buffer.setText("")
		self.Hilo_de_trabajo = Hilos() 									#Inicializamos un objeto de la otra clase
		self.Hilo_de_trabajo.Imageupd.connect(self.Imageupd_slot)	
		self.Hilo_de_trabajo.lbl_detect.connect(self.actualizar_lbl)	#Conecata la señal con la funcion de actualizar lbl

	def StartVideo(self):
		self.Hilo_de_trabajo.start()			#Corremos el hilo
		

	def DetenerVideo(self):
		global var_buffer
		global buffer_sal

		buffer_sal=""
		var_buffer=""

		self.Hilo_de_trabajo.stop()
		self.ImagenEntrada.clear()


	def actualizar_lbl(self, texto):		#Funcion para actualizar lbl
		global var_buffer
		global buffer_sal

		self.DeteccionSalida.setText(texto)	#Manda la señal emitida a el Qlabel deteccionSalida
		
		if texto=="A":
			var_buffer = var_buffer+"A"
		if texto=="B":
			var_buffer = var_buffer+"B"
		if texto=="C":
			var_buffer = var_buffer+"C"
		if texto=="D":
			var_buffer = var_buffer+"D"
		if texto=="E":
			var_buffer = var_buffer+"E"
		if texto=="F":
			var_buffer = var_buffer+"F"
		if texto=="G":
			var_buffer = var_buffer+"G"
		if texto=="H":
			var_buffer = var_buffer+"H"
		if texto=="I":
			var_buffer = var_buffer+"I"
		if texto=="L":
			var_buffer = var_buffer+"L"
		if texto=="M":
			var_buffer = var_buffer+"M"
		if texto=="N":
			var_buffer = var_buffer+"N"
		if texto=="O":
			var_buffer = var_buffer+"O"
		if texto=="P":
			var_buffer = var_buffer+"P"
		if texto=="R":
			var_buffer = var_buffer+"R"
		if texto=="S":
			var_buffer = var_buffer+"S"
		if texto=="T":
			var_buffer = var_buffer+"T"
		if texto=="U":
			var_buffer = var_buffer+"U"
		if texto=="V":
			var_buffer = var_buffer+"V"
		if texto=="W":
			var_buffer = var_buffer+"W"
		if texto=="Y":
			var_buffer = var_buffer+"Y"
					
		if len(var_buffer)>=10:
			if var_buffer=="AAAAAAAAAAA":
				var_buffer = ""
				buffer_sal = buffer_sal+"A"
				self.buffer.setText(buffer_sal)
			if var_buffer=="BBBBBBBBBBB":
				var_buffer = ""
				buffer_sal = buffer_sal+"B"
				self.buffer.setText(buffer_sal)
			if var_buffer=="CCCCCCCCCCC":
				var_buffer = ""
				buffer_sal = buffer_sal+"C"
				self.buffer.setText(buffer_sal)
			if var_buffer=="DDDDDDDDDDD":
				var_buffer = ""
				buffer_sal = buffer_sal+"D"
				self.buffer.setText(buffer_sal)
			if var_buffer=="EEEEEEEEEEE":
				var_buffer = ""
				buffer_sal = buffer_sal+"E"
				self.buffer.setText(buffer_sal)
			if var_buffer=="FFFFFFFFFFF":
				var_buffer = ""
				buffer_sal = buffer_sal+"F"
				self.buffer.setText(buffer_sal)
			if var_buffer=="GGGGGGGGGGG":
				var_buffer = ""
				buffer_sal = buffer_sal+"G"
				self.buffer.setText(buffer_sal)
			if var_buffer=="HHHHHHHHHHH":
				var_buffer = ""
				buffer_sal = buffer_sal+"H"
				self.buffer.setText(buffer_sal)
			if var_buffer=="IIIIIIIIII":
				var_buffer = ""
				buffer_sal = buffer_sal+"I"
				self.buffer.setText(buffer_sal)
			if var_buffer=="LLLLLLLLLLL":
				var_buffer = ""
				buffer_sal = buffer_sal+"L"
				self.buffer.setText(buffer_sal)
			if var_buffer=="MMMMMMMMMMM":
				var_buffer = ""
				buffer_sal = buffer_sal+"M"
				self.buffer.setText(buffer_sal)
			if var_buffer=="NNNNNNNNNNN":
				var_buffer = ""
				buffer_sal = buffer_sal+"N"
				self.buffer.setText(buffer_sal)
			if var_buffer=="OOOOOOOOOOO":
				var_buffer = ""
				buffer_sal = buffer_sal+"O"
				self.buffer.setText(buffer_sal)
			if var_buffer=="PPPPPPPPPPP":
				var_buffer = ""
				buffer_sal = buffer_sal+"P"
				self.buffer.setText(buffer_sal)
			if var_buffer=="RRRRRRRRRRR":
				var_buffer = ""
				buffer_sal = buffer_sal+"R"
				self.buffer.setText(buffer_sal)
			if var_buffer=="SSSSSSSSSSS":
				var_buffer = ""
				buffer_sal = buffer_sal+"S"
				self.buffer.setText(buffer_sal)
			if var_buffer=="TTTTTTTTTTT":
				var_buffer = ""
				buffer_sal = buffer_sal+"T"
				self.buffer.setText(buffer_sal)
			if var_buffer=="UUUUUUUUUUU":
				var_buffer = ""
				buffer_sal = buffer_sal+"U"
				self.buffer.setText(buffer_sal)
			if var_buffer=="VVVVVVVVVVV":
				var_buffer = ""
				buffer_sal = buffer_sal+"V"
				self.buffer.setText(buffer_sal)
			if var_buffer=="WWWWWWWWWWW":
				var_buffer = ""
				buffer_sal = buffer_sal+"W"
				self.buffer.setText(buffer_sal)
			if var_buffer=="YYYYYYYYYYY":
				var_buffer = ""
				buffer_sal = buffer_sal+"Y"
				self.buffer.setText(buffer_sal)
			if len(buffer_sal)>22:
				buffer_sal = ""
				var_buffer = ""
		
			if len(var_buffer)>20:
				var_buffer=""
				

	def Imageupd_slot(self,imagen):			#funcion para actualizar imagen, tiene casi la misma funcion que EnviarImagen(self, imagen)
		self.ImagenEntrada.setPixmap(QtGui.QPixmap.fromImage(imagen))
		

if __name__ == '__main__':
	app = QApplication(sys.argv)
	INTERFAZ = GUI()
	INTERFAZ.setFixedSize(INTERFAZ.size())
	INTERFAZ.show()
	sys.exit(app.exec_())
