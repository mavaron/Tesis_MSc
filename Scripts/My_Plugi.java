import ij.*;
import ij.process.*;
import ij.gui.*;
import java.awt.*;
import ij.plugin.*;

public class My_Plugin implements PlugIn {
	@Override
	public void run(String arg) {
		ImagePlus imp = IJ.openImage("F:\\MSc Misis\\4 Semestre\\Tesis 1\\Fondo\\Fondo.jpg");
		imp = IJ.openImage("F:\\MSc Misis\\4 Semestre\\Tesis 1\\Dataset Final\\GOPR0423.JPG");
		ImageCalculator ic = new ImageCalculator();
		ImagePlus imp1 = WindowManager.getImage("Fondo.jpg");
		ImagePlus imp2 = WindowManager.getImage("GOPR0423.JPG");
		ImagePlus imp3 = ic.run("Subtract create", imp1, imp2);
		imp3.show();
		IJ.saveAs(imp, "Jpeg", "F:\\MSc Misis\\4 Semestre\\Tesis 1\\DS Prueba\\1.jpg");
		imp.close();
	}

}
