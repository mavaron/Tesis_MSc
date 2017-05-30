from ij import IJ
from ij.plugin import ImageCalculator as IC
from ij.process import ImageStatistics as IS  
from ij.io import FileSaver
import os  

#Path a folder del Dataset Incial
folderds = "F:\\MSc Misis\\4 Semestre\\Tesis 1\\DS Duplicado" 
#Path a folder del Dataset final  
folderdsf = "F:\\MSc Misis\\4 Semestre\\Tesis 1\\DS Binary"
i=0
for filename in os.listdir(folderds):
	#Establecer Path
	Pathfile=("F:\\MSc Misis\\4 Semestre\\Tesis 1\\DS Duplicado\\" + filename)
	#Extraer imagen del Path
	image=IJ.openImage(Pathfile)
	#Convertir a 8 bits
	IJ.run(image, "8-bit", "")
	#Aumentar Contraste
	IJ.run("Brightness/Contrast...")
	IJ.setMinAndMax(image,39, 215)
	#Umbralización con Momentos
	IJ.setAutoThreshold(image, "Moments dark stack");
	#Convertir en Máscara
	IJ.run(image, "Convert to Mask", "");
	#Análisis de Partículas
	IJ.run(image, "Analyze Particles...", "size=1000-Infinity circularity=0.01-1.00 show=Outlines clear in_situ");
	#ruta archivo
	filename = folderdsf + "\\" + str(i) +".jpg"
	#guardar archivo	
	IJ.saveAs(image, "Jpeg", filename)
	#impresion en consola del proceso
	print "Proccessing FinalFile", filename
	i=i+1 


