from ij import IJ
from ij.plugin import ImageCalculator as IC
from ij.process import ImageStatistics as IS  
from ij.io import FileSaver
import os  

#Asignación del ROI de fondo
background=IJ.openImage("F:\\MSc Misis\\4 Semestre\\Tesis 1\\Fondo\\Fondo.jpg")
#Path a folder del Dataset Incial
folderds = "F:\\MSc Misis\\4 Semestre\\Tesis 1\\Dataset Final"  
#Path a folder del Dataset final  
folderdsf = "F:\\MSc Misis\\4 Semestre\\Tesis 1\\DS Prueba"  
i=0
for filename in os.listdir(folderds):  
	#Establecer Path
	Pathfile=("F:\\MSc Misis\\4 Semestre\\Tesis 1\\Dataset Final\\"+filename)
	#Extraer imagen del Path
	dsimage=IJ.openImage(Pathfile)
	#Substracción del área fuera del ROI
	resultado=IC().run("Subtract create",background,dsimage)
	#conversion a recipiente FileSaver
	fs=FileSaver(resultado)
	#Nombrar archivo
	filename = folderdsf + "\\" + str(i) +".jpg"
	#Guardar archivo como JPEG
	fs.saveAsJpeg(filename)   
	#impresion en consola del proceso
	print "Proccessing FinalFile", filename
	i=i+1 