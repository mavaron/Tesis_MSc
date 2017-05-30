from ij import IJ
from ij.gui import PolygonRoi
from ij.gui import Roi
from ij.plugin import ImageCalculator as IC
from ij.process import ImageStatistics as IS  
from ij.io import FileSaver
from ij import WindowManager 
import os  

xpoints = [954,708,3156,2760]
ypoints = [1290,2112,1920,1158]
folderds = "F:\\MSc Misis\\4 Semestre\\Tesis 1\\DS Prueba"  
folderdsf ="F:\\MSc Misis\\4 Semestre\\Tesis 1\\DS Duplicado"
i=0
for filename in os.listdir(folderds):
	#Establecer Path
	Pathfile=("F:\\MSc Misis\\4 Semestre\\Tesis 1\\DS Prueba\\"+filename)
	#Extraer imagen del Path
	dsimage=IJ.openImage(Pathfile)
	#Creación del área de interés
	roi=PolygonRoi(xpoints,ypoints,4,Roi.POLYGON)
	#Creación de la imagen
	dsimage.setRoi(roi)
	#Duplicación de la imagen
	imp2=dsimage.duplicate()
	#conversion a recipiente FileSaver
	fs=FileSaver(imp2)
	#Nombrar archivo
	filename = folderdsf + "\\" + str(i) +".jpg"
	#Guardar archivo como JPEG
	fs.saveAsJpeg(filename)
	#impresion en consola del proceso
	print "Proccessing FinalFile", filename
	i=i+1