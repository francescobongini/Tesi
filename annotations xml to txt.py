'''
import xml.etree.ElementTree as ET
from PIL import Image
tree = ET.parse('C:/Users/Francesco/Desktop/Materiale tesi/XML/XML/annotations_Scena02_Fabio.xml')
root = tree.getroot()
print(root[0][2].attrib) #restituisce la annotazione del frame 2

a=root[0][2].attrib
float(a['xbr'])
#960-576

#file=open(destination_path + '/FLIR_{:05d}.txt'.format(counter + 1), 'a'))
#with open("../yolov3/coco/images/FLIR_Dataset/training/labels/randaug_{:05d}.txt".format(i + 1), 'w') as file:
i=1
xc=(float(a['xbr'])+float(a['xtl']))/2/960
yc=1-(float(a['ybr'])+float(a['ytl']))/2/576
wx=(float(a['xbr'])-float(a['xtl']))/2/960
wy=(float(a['ybr'])-float(a['ytl']))/2/576

with open("C:/Users/Francesco/Desktop/XML/XML/Fabio/i.txt",'w') as file:
    a=root[0][i].attrib
    file.write("0")
    file.write(" ")
    file.write(str(xc))
    file.write(" ")
    file.write(str(yc))
    file.write(" ")
    file.write(str(wx))
    file.write(" ")
    file.write(str(wy))
    

image = Image.open('C:/Users/Francesco/Desktop/Scena01_Fabio/Scena01_Fabio/Scena01_Fabio_0002.jpg')
image=image.resize((640, 512), Image.ANTIALIAS)
image.save('C:/Users/Francesco/Desktop/XML/2.jpeg', 'JPEG')


'''




#1038,1554, 1880

#########################################################################################
import xml.etree.ElementTree as ET
from PIL import Image
tree = ET.parse('C:/Users/Francesco/Desktop/Materiale tesi/XML/XML/annotations_Scena01_Fabio.xml') #annotations_Scena02_Leopold #annotations_Scena03_Stefania
root = tree.getroot()
for i in range(0,1038,2):
    print(i)
    a=root[0][i].attrib
    a['ybr']=576-float(a['ybr'])
    a['ytl']=576-float(a['ytl'])
    xc=(float(a['xbr'])+float(a['xtl']))/2/960
    yc=(float(a['ytl'])+float(a['ybr']))/2/576
    wx=(float(a['xbr'])-float(a['xtl']))/960
    wy=(float(a['ytl'])-float(a['ybr']))/576
    with open("C:/Users/Francesco/Desktop/scene/labels/Fabio_{:d}.txt".format(i), 'w') as file:
        if xc==0 and wx==0:
            image = Image.open('C:/Users/Francesco/Desktop/Materiale tesi/Scena01_Fabio/Scena01_Fabio_{:04d}.jpg'.format(i))
            image=image.resize((640, 512), Image.ANTIALIAS)
            image.save('C:/Users/Francesco/Desktop/scene/immagini/Fabio01/Fabio_{:d}.jpeg'.format(i), 'JPEG')
            continue
        else:
            file.write("0")
            file.write(" ")
            file.write(str(xc))
            file.write(" ")
            file.write(str(1-yc))
            file.write(" ")
            file.write(str(wx))
            file.write(" ")
            file.write(str(wy))
            image = Image.open('C:/Users/Francesco/Desktop/Materiale tesi/Scena01_Fabio/Scena01_Fabio_{:04d}.jpg'.format(i))
            image=image.resize((640, 512), Image.ANTIALIAS)
            image.save('C:/Users/Francesco/Desktop/scene/immagini/Fabio01/Fabio_{:d}.jpeg'.format(i), 'JPEG')



#########################################################################################
import xml.etree.ElementTree as ET
from PIL import Image
tree = ET.parse('C:/Users/Francesco/Desktop/XML/XML/annotations_Scena02_Leopold.xml') #annotations_Scena02_Leopold #annotations_Scena03_Stefania
root = tree.getroot()
for i in range(0,1555,2):
    print(i)
    a=root[0][i].attrib
    a['ybr']=576-float(a['ybr'])
    a['ytl']=576-float(a['ytl'])
    xc=(float(a['xbr'])+float(a['xtl']))/2/960
    yc=(float(a['ytl'])+float(a['ybr']))/2/576
    wx=(float(a['xbr'])-float(a['xtl']))/960
    wy=(float(a['ytl'])-float(a['ybr']))/576
    with open("C:/Users/Francesco/Desktop/scene/labels/Leopold_{:d}.txt".format(i), 'w') as file:
        if xc==0 and wx==0:
            image = Image.open('C:/Users/Francesco/Desktop/Materiale tesi/Scena02_Leopold/Scena02_Leopold_{:04d}.jpg'.format(i))
            image=image.resize((640, 512), Image.ANTIALIAS)
            image.save('C:/Users/Francesco/Desktop/scene/immagini/Leopold02/Leopold_{:d}.jpeg'.format(i), 'JPEG')
            continue
        else:
            file.write("0")
            file.write(" ")
            file.write(str(xc))
            file.write(" ")
            file.write(str(1-yc))
            file.write(" ")
            file.write(str(wx))
            file.write(" ")
            file.write(str(wy))
            image = Image.open('C:/Users/Francesco/Desktop/Materiale tesi/Scena02_Leopold/Scena02_Leopold_{:04d}.jpg'.format(i))
            image=image.resize((640, 512), Image.ANTIALIAS)
            image.save('C:/Users/Francesco/Desktop/scene/immagini/Leopold02/Leopold_{:d}.jpeg'.format(i), 'JPEG')




#########################################################################################
import xml.etree.ElementTree as ET
from PIL import Image
tree = ET.parse('C:/Users/Francesco/Desktop/Materiale tesi/XML/XML/annotations_Scena03_Stefania.xml') #annotations_Scena02_Leopold #annotations_Scena03_Stefania
root = tree.getroot()
for i in range(0,1800,2):
    print(i)
    a=root[0][i].attrib
    a['ybr']=576-float(a['ybr'])
    a['ytl']=576-float(a['ytl'])
    xc=(float(a['xbr'])+float(a['xtl']))/2/960
    yc=(float(a['ytl'])+float(a['ybr']))/2/576
    wx=(float(a['xbr'])-float(a['xtl']))/960
    wy=(float(a['ytl'])-float(a['ybr']))/576
    with open("C:/Users/Francesco/Desktop/scene/labels/Stefania_{:d}.txt".format(i), 'w') as file:
        if xc==0 and wx==0:
            image = Image.open('C:/Users/Francesco/Desktop/Materiale tesi/Scena03_Stefania/Scena03_Stefania_{:04d}.jpg'.format(i))
            image=image.resize((640, 512), Image.ANTIALIAS)
            image.save('C:/Users/Francesco/Desktop/scene/immagini/Stefania03/Stefania_{:d}.jpeg'.format(i), 'JPEG')
            continue
        else:
            file.write("0")
            file.write(" ")
            file.write(str(xc))
            file.write(" ")
            file.write(str(1-yc))
            file.write(" ")
            file.write(str(wx))
            file.write(" ")
            file.write(str(wy))
            image = Image.open('C:/Users/Francesco/Desktop/Materiale tesi/Scena03_Stefania/Scena03_Stefania_{:04d}.jpg'.format(i))
            image=image.resize((640, 512), Image.ANTIALIAS)
            image.save('C:/Users/Francesco/Desktop/scene/immagini/Stefania03/Stefania_{:d}.jpeg'.format(i), 'JPEG')




#########################################################################################################################




#########################################################################################
import xml.etree.ElementTree as ET
from PIL import Image
tree = ET.parse('C:/Users/Francesco/Desktop/Materiale tesi/XML/XML/annotations_Scena01_Alice.xml') #annotations_Scena02_Leopold #annotations_Scena03_Stefania
root = tree.getroot()
for i in range(0,1038,2):
    print(i)
    a=root[0][i].attrib
    a['ybr']=576-float(a['ybr'])
    a['ytl']=576-float(a['ytl'])
    xc=(float(a['xbr'])+float(a['xtl']))/2/960
    yc=(float(a['ytl'])+float(a['ybr']))/2/576
    wx=(float(a['xbr'])-float(a['xtl']))/960
    wy=(float(a['ytl'])-float(a['ybr']))/576
    with open("C:/Users/Francesco/Desktop/scene/labels/Alice01_{:d}.txt".format(i), 'w') as file:
        if xc==0 and wx==0:
            image = Image.open('C:/Users/Francesco/Desktop/Materiale tesi/Scena01_Alice/Scena01_Alice_{:04d}.jpg'.format(i))
            image=image.resize((640, 512), Image.ANTIALIAS)
            image.save('C:/Users/Francesco/Desktop/scene/immagini/Alice01/Alice01_{:d}.jpeg'.format(i), 'JPEG')
            continue
        else:
            file.write("0")
            file.write(" ")
            file.write(str(xc))
            file.write(" ")
            file.write(str(1-yc))
            file.write(" ")
            file.write(str(wx))
            file.write(" ")
            file.write(str(wy))
            image = Image.open('C:/Users/Francesco/Desktop/Materiale tesi/Scena01_Alice/Scena01_Alice_{:04d}.jpg'.format(i))
            image=image.resize((640, 512), Image.ANTIALIAS)
            image.save('C:/Users/Francesco/Desktop/scene/immagini/Alice01/Alice01_{:d}.jpeg'.format(i), 'JPEG')




#########################################################################################
import xml.etree.ElementTree as ET
from PIL import Image
tree = ET.parse('C:/Users/Francesco/Desktop/Materiale tesi/XML/XML/annotations_Scena02_Alice.xml') #annotations_Scena02_Leopold #annotations_Scena03_Stefania
root = tree.getroot()
for i in range(0,1554,2):
    print(i)
    a=root[0][i].attrib
    a['ybr']=576-float(a['ybr'])
    a['ytl']=576-float(a['ytl'])
    xc=(float(a['xbr'])+float(a['xtl']))/2/960
    yc=(float(a['ytl'])+float(a['ybr']))/2/576
    wx=(float(a['xbr'])-float(a['xtl']))/960
    wy=(float(a['ytl'])-float(a['ybr']))/576
    with open("C:/Users/Francesco/Desktop/scene/labels/Alice02_{:d}.txt".format(i), 'w') as file:
        if xc==0 and wx==0:
            image = Image.open('C:/Users/Francesco/Desktop/Materiale tesi/Scena02_Alice/Scena02_Alice_{:04d}.jpg'.format(i))
            image=image.resize((640, 512), Image.ANTIALIAS)
            image.save('C:/Users/Francesco/Desktop/scene/immagini/Alice02/Alice02_{:d}.jpeg'.format(i), 'JPEG')
            continue
        else:
            file.write("0")
            file.write(" ")
            file.write(str(xc))
            file.write(" ")
            file.write(str(1-yc))
            file.write(" ")
            file.write(str(wx))
            file.write(" ")
            file.write(str(wy))
            image = Image.open('C:/Users/Francesco/Desktop/Materiale tesi/Scena02_Alice/Scena02_Alice_{:04d}.jpg'.format(i))
            image=image.resize((640, 512), Image.ANTIALIAS)
            image.save('C:/Users/Francesco/Desktop/scene/immagini/Alice02/Alice02_{:d}.jpeg'.format(i), 'JPEG')





#########################################################################################
import xml.etree.ElementTree as ET
from PIL import Image
tree = ET.parse('C:/Users/Francesco/Desktop/Materiale tesi/XML/XML/annotations_Scena03_Alice.xml') #annotations_Scena02_Leopold #annotations_Scena03_Stefania
root = tree.getroot()
for i in range(0,1800,2):
    print(i)
    a=root[0][i].attrib
    a['ybr']=576-float(a['ybr'])
    a['ytl']=576-float(a['ytl'])
    xc=(float(a['xbr'])+float(a['xtl']))/2/960
    yc=(float(a['ytl'])+float(a['ybr']))/2/576
    wx=(float(a['xbr'])-float(a['xtl']))/960
    wy=(float(a['ytl'])-float(a['ybr']))/576
    with open("C:/Users/Francesco/Desktop/scene/labels/Alice03_{:d}.txt".format(i), 'w') as file:
        if xc==0 and wx==0:
            image = Image.open('C:/Users/Francesco/Desktop/Materiale tesi/Scena03_Alice/Scena03_Alice_{:04d}.jpg'.format(i))
            image=image.resize((640, 512), Image.ANTIALIAS)
            image.save('C:/Users/Francesco/Desktop/scene/immagini/Alice03/Alice03_{:d}.jpeg'.format(i), 'JPEG')
            continue
        else:
            file.write("0")
            file.write(" ")
            file.write(str(xc))
            file.write(" ")
            file.write(str(1-yc))
            file.write(" ")
            file.write(str(wx))
            file.write(" ")
            file.write(str(wy))
            image = Image.open('C:/Users/Francesco/Desktop/Materiale tesi/Scena03_Alice/Scena03_Alice_{:04d}.jpg'.format(i))
            image=image.resize((640, 512), Image.ANTIALIAS)
            image.save('C:/Users/Francesco/Desktop/scene/immagini/Alice03/Alice03_{:d}.jpeg'.format(i), 'JPEG')



























