import os
import sys
import time

import serial


from threading import *

#from PyQt5.QtWidgets import *        #remember add this line instead of the following line if there will be any error


#from PyQt5 import QtGui                   #also those###########################################################!!!!!!!!!!1
#from PyQt5 import QtWidgets
#from PyQt5 import QtCore



from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication,QLCDNumber,QPushButton,QLabel
from PyQt5.QtGui import QFont, QFontDatabase

import RPi.GPIO as GPIO

################################################################################################
# Convert UI to PyQt5 py file
################################################################################################
#os.system("pyuic5 -o interface_ui.py interface.ui")


################################################################################################
# Import the generated UI
################################################################################################
#from interface_ui import *                #this line is from the video but i can write it as the following as i has understood
from interface_ui import Ui_MainWindow as interface_ui

ser = serial.Serial('/dev/ttyAMA0', 9600)


################################################################################################
# MAIN WINDOW CLASS
################################################################################################
class MainWindow(QMainWindow, interface_ui):
	mode=0
	def __init__(self, parent=None):
		QMainWindow.__init__(self)
		################################################################################################
		# Setup the UI main window
		################################################################################################
		#self.ui =  Ui_MainWindow()
		#self.ui.setupUi(self)
		self.setupUi(self)

		################################################################################################
		# buttons
		###############################################################################################
		self.accel.setAutoRepeat(True)
		self.accel.setAutoRepeatDelay(1000)
		self.decl.setAutoRepeat(True)
		self.decl.setAutoRepeatDelay(1000)
		self.accel.clicked.connect(self.accell)
		self.decl.clicked.connect(self.decll)
		self.ACC.clicked.connect(self.acc)
		self.NCC.clicked.connect(self.ncc)
		self.CC.clicked.connect(self.cc)
		self.Range1.clicked.connect(self.thread1)
		self.Range2.clicked.connect(self.thread2)
		self.Range3.clicked.connect(self.thread3)
		self.stop.clicked.connect(self.stopFun)


		################################################################################################
		# Show window
		################################################################################################
		self.show()
		# i have tried to make the code as i have understood from the playlist...






		##############################################################################################
		#customize Analogue Gauge Wadget
		##############################################################################################
		#self.ui.widget.enableBarGraph =True
		self.widget.enableBarGraph =True

		self.widget.setEnableBarGraph(False)




		#set Gauge units
		#self.ui.widget.units = "Km/h"
		self.widget.units = "Meter/minute"

		#set minimum gaugae value
		#self.ui.widget.minValue =0
		self.widget.minValue =0


		#set max gaugae value
		self.widget.maxValue =50


		#set scale value
		self.widget.scalacount =5


		#start from the minimum value
		#self.widget.updateValue(self.widget.minValue)
		#OR
		#start from half or middle value
		#self.widget.updateValue(int(self.widget.maxValue - self.widget.minValue)/2)
		#Or
		#if i want a specific value to be started from
		def change(value):
			self.lcd.display(value)

		self.widget.valueChanged.connect(change)



		#self.widget.updateValue(40)


		#select gauage theme
		self.widget.setGaugeTheme(20)  #choose number from zero to 24       ####20 IS fgood 24,16, 22, 18, 17,14


		'''
		#set custom gauge theme
		self.widget.setCustomGaugeTheme(
			color1 = "#FF00A6" ,  #bright
			color2 = "#870058" , #middle brightness
			color3 = "#360023"     #darkest

		)
		'''


		'''
		self.widget.setCustomGaugeTheme(
			color1 = "#002523" ,  #bright
			color2 = "#990008" , #middle brightness
			color3 = "#00F6E9"     #darkest

		)      #good one
		'''

		'''
		self.widget.setCustomGaugeTheme(
			color1 = "#fff" ,  #white
			color2 = "#555" , #grey
			color3 = "#000"     #black

		)  
		'''


		self.widget.setScalePolygonColor(
			color1 = "Red",
			color2 = "green", 

			color3 = "white"  
			#color2 = "#C1007D" , 
			#color3 = "#880808"
			
			#color3 = "#green"    

		)   #good one



		self.widget.setNeedleCenterColor(
			color1 = "white" ,  
			color2 = "#2D16B3" , 
			color3 = "#green"    

		)


		'''
		self.widget.setOuterCircleColor(
			color1 = "#22FF00" ,  
			color2 = "#15A100" , 
			color3 = "#021200"    

		)
		'''



		self.widget.setBigScaleColor("white")           #good
		self.widget.setFineScaleColor("blue")         #good

		#self.widget.setScaleValueColor(34,255,0,255) 
		#self.widget.setScaleValueColor(34,255,0,255)

		#self.widget.setScaleValueColor(11,202,194,202)
		#self.widget.setDisplayValueColor(11,202,194,202)

		self.widget.setScaleValueColor(255,255,255,255)              #veryyyyyyyyyyyy gooood
		self.widget.setDisplayValueColor(255,255,255,255)

		self.widget.setNeedleColor(255,255,255,255)



		#he explained some beautiful notes about the gauge theme  here at 13:00 to 19:30 (i neglect this points...if i need it i will return back to it)
		#he also explained some other notes about the fonts at 19:30 20:30to (and i also neglect them now...)
		#he continued explaining the color beautiful notes at 21: 00 to    (and i also neglect them now...)
		#he reexplained all what he had done from 26:00 to the end of the video but kin another way(that's even more professional in code (he worked there, on Joson file))but i 
		#neglect this way(from26:30 to the end of the video)



		#self.widget.setEnableValueText(True)
		self.widget.setEnableCenterPoint(True)       #it's not important 

		#self.widget.setEnableNeedlePolygon(True)

		#self.widget.setEnableScaleText(True)
		#self.widget.setEnableScalePolygon(True)
		#self.widget.setEnableBigScaleGrid(True)
		#self.widget.setEnableFineScaleGrid(True)
		self.widget.setMouseTracking(False)           #if false, this makes me only moves the needle when i clicke on the mouse not just point!


		##############################################################################
		#this comming part of the code I have made by my self and wasn't in the video#
		##############################################################################


			




		'''
		#this function is not true
		duty = 0
		def acceler():
			global duty
			duty +=1
			#pi_pwm.ChangeDutyCycle(duty)
			#txt.setText(str(duty))     #instead of this i want to move the needle
			self.widget.setValue(duty)
			#self.widget.valueChanged.connect(duty)
			'''

		#for i in range (0,101,1):
			#self.widget.setValue(i)
			#self.widget.valueChanged.connect(i)

		#self.Accel.clicked.connect(acceler)



		#def acceler():
			#print ('5')
		#self.Accel.clicked.connect(acceler)

		'''
		Button {
			id: Accel
			#x: 20
			#y:520
			#width: 100
			#height: 100
			text: "+"
			onClicked: needleAngle +=10
		}

		Button {
			id: Decel
			#x: 236
			#y:520
			#width: 100
			#height: 100
			text: "-"
			onClicked: needleAngle -=10
		}

		'''



	def thread1(self):
		t1=Thread(target=self.range1)
		t1.start()
        
        
	def thread2(self):
		t1=Thread(target=self.range2)
		t1.start()
        
        
	def thread3(self):
		t1=Thread(target=self.range3)
		t1.start()
        
        
	def thread4(self):
		t1=Thread(target=self.stop)
		t1.start()
        
        
	def threadRead(self):
		t12=Thread(target=self.SerUpdate)
		t12.start()        
        
	def accell(self):
		ser.write(b"A")
		print('sent A')
    
    
	def decll(self):
		#global duty
		#duty -=10
		#pi_pwm.ChangeDutyCycle(duty)
		#self.lcd.display(duty)
		if self.mode==2:
			self.mode=1
			self.lineEdit_2.clear()
			self.lineEdit_2.setText('NCC')
		ser.write(b"D")
		print('sent D')
        
    
	def acc(self):
		self.lineEdit_2.setText('ACC')
		self.lineEdit_3.setText('CC ON')
		self.mode = 2
		ser.write(b"P")
		print('sent P')

		#self.sec = second(option)
		#self.sec.show()
        
        
	def ncc(self):
		self.lineEdit_2.setText('NCC')
		self.lineEdit_3.setText('CC ON')
		self.mode = 1
		ser.write(b"N")
		print('sent N')
        
    
    
	def cc(self):
		self.lineEdit_2.clear()
		self.lineEdit_3.setText('CC OFF')
		self.mode =0
		ser.write(b"O")
		print('sent O')

            
            
	def range1(self):
		ser.write(b"C")
		print('sent C')
        
        
	def range2(self):
		ser.write(b"M")
		print('sent M')
		
	def range3(self):
		ser.write(b"F")
		print('sent F')
		
		
		
	def stopFun(self):
		self.lineEdit_2.clear()
		self.lineEdit_3.setText('CC OFF')
		ser.write(b"S")
		print('sent S')





	def SerUpdate(self):
		#for i in range (10):
			#time.sleep(0.5)
			#self.widget.updateValue(i)

		while(1):
			c=ser.read(1)

			if c == b'\r':
				char=ser.read(22)
				msg=char.split(b' ')
				#print(msg)
				speed = msg[0].strip(b'\x00\r')
				distance = msg[1].strip(b'\x00\r')

				print("speed = {}".format(speed))
				print("distance = {}".format(distance))
				
				#dist = int.from_bytes(distance, "big")
				#print (dist)
				dd=str(distance)
				ddd=dd.strip("b\'")
				self.lineEdit.setText(ddd)
				Distance = int(ddd)

				ss=str(speed)
				sss=ss.strip("b\'")
				#self.lcd_3.display(ddd)
				sssss= int(sss)
				self.widget.updateValue(sssss)
				if Distance <= 10:

					self.mode =0
					self.lineEdit_2.clear()
					self.lineEdit_3.setText('CC OFF')

                #for i in range (ddddd):
                    #self.widget.updateValue(i)




########################################################################
## EXECUTE APP
########################################################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ########################################################################
    ## 
    ########################################################################

    window =MainWindow()    #the name of the class
    window.show()
    window.threadRead()

    #lcd = QLCDNumber(window)
    #lcd.move(100,100)
    #try to connect the needle value to the lcd value.....


    

    sys.exit(app.exec_())

########################################################################
## END===>
########################################################################
