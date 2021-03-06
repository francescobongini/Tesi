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


######################################################################################################
#scena con auto e persone
#annotazioni dell'immagine di background
import shutil
import os

for i in range(0,185):
    src = r'C:/Users/Francesco/Desktop/FLIR_00010.txt'
    dst =  "C:/Users/Francesco/Desktop/scene/labels/TwoCarsTwoPeople_{:d}.txt".format(i)
    shutil.copyfile(src, dst)

import xml.etree.ElementTree as ET
from PIL import Image
tree = ET.parse('C:/Users/Francesco/Desktop/Materiale tesi/XML/XML/annotations_TwoCarsTwoPeople.xml') #annotations_Scena02_Leopold #annotations_Scena03_Stefania
root = tree.getroot()
for i in range(0,185):
    print(i)
    #person
    a=root[0][i].attrib
    a['ybr']=512-float(a['ybr'])
    a['ytl']=512-float(a['ytl'])
    xc=(float(a['xbr'])+float(a['xtl']))/2/640
    yc=(float(a['ytl'])+float(a['ybr']))/2/512
    wx=(float(a['xbr'])-float(a['xtl']))/640
    wy=(float(a['ytl'])-float(a['ybr']))/512
    with open("C:/Users/Francesco/Desktop/scene/labels/TwoCarsTwoPeople_{:d}.txt".format(i), 'a') as file:
        if xc==0 and wx==0:
            image = Image.open('C:/Users/Francesco/Desktop/Materiale tesi/TwoCarsTwoPeople/TwoCarsTwoPeople_{:03d}.jpg'.format(i))
            image=image.resize((640, 512), Image.ANTIALIAS)
            image.save('C:/Users/Francesco/Desktop/scene/immagini/TwoCarsTwoPeople/TwoCarsTwoPeople_{:d}.jpeg'.format(i), 'JPEG')
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
            file.write("\n")
            image = Image.open('C:/Users/Francesco/Desktop/Materiale tesi/TwoCarsTwoPeople/TwoCarsTwoPeople_{:03d}.jpg'.format(i))
            image=image.resize((640, 512), Image.ANTIALIAS)
            image.save('C:/Users/Francesco/Desktop/scene/immagini/TwoCarsTwoPeople/TwoCarsTwoPeople_{:d}.jpeg'.format(i), 'JPEG')
    #car -> nel xml sono state suddivise in car01 e car02, quindi farò due cicli
for i in range(0,185):
    print(i)
    a=root[1][i].attrib
    a['ybr']=512-float(a['ybr'])
    a['ytl']=512-float(a['ytl'])
    xc=(float(a['xbr'])+float(a['xtl']))/2/640
    yc=(float(a['ytl'])+float(a['ybr']))/2/512
    wx=(float(a['xbr'])-float(a['xtl']))/640
    wy=(float(a['ytl'])-float(a['ybr']))/512
    with open("C:/Users/Francesco/Desktop/scene/labels/TwoCarsTwoPeople_{:d}.txt".format(i), 'a') as file:
        if xc!=0 and wx!=0:
            file.write("0")
            file.write(" ")
            file.write(str(xc))
            file.write(" ")
            file.write(str(1-yc))
            file.write(" ")
            file.write(str(wx))
            file.write(" ")
            file.write(str(wy))
            file.write("\n")
            image = Image.open('C:/Users/Francesco/Desktop/Materiale tesi/TwoCarsTwoPeople/TwoCarsTwoPeople_{:03d}.jpg'.format(i))
            image=image.resize((640, 512), Image.ANTIALIAS)
            image.save('C:/Users/Francesco/Desktop/scene/immagini/TwoCarsTwoPeople/TwoCarsTwoPeople_{:d}.jpeg'.format(i), 'JPEG')
        else:
            image = Image.open('C:/Users/Francesco/Desktop/Materiale tesi/TwoCarsTwoPeople/TwoCarsTwoPeople_{:03d}.jpg'.format(i))
            image=image.resize((640, 512), Image.ANTIALIAS)
            image.save('C:/Users/Francesco/Desktop/scene/immagini/TwoCarsTwoPeople/TwoCarsTwoPeople_{:d}.jpeg'.format(i), 'JPEG')

for i in range(0,185): 
    print(i)           
    a=root[2][i].attrib
    a['ybr']=512-float(a['ybr'])
    a['ytl']=512-float(a['ytl'])
    xc=(float(a['xbr'])+float(a['xtl']))/2/640
    yc=(float(a['ytl'])+float(a['ybr']))/2/512
    wx=(float(a['xbr'])-float(a['xtl']))/640
    wy=(float(a['ytl'])-float(a['ybr']))/512
    with open("C:/Users/Francesco/Desktop/scene/labels/TwoCarsTwoPeople_{:d}.txt".format(i), 'a') as file:
        if xc!=0 and wx!=0:
            file.write("2")
            file.write(" ")
            file.write(str(xc))
            file.write(" ")
            file.write(str(1-yc))
            file.write(" ")
            file.write(str(wx))
            file.write(" ")
            file.write(str(wy))
            file.write("\n")
            image = Image.open('C:/Users/Francesco/Desktop/Materiale tesi/TwoCarsTwoPeople/TwoCarsTwoPeople_{:03d}.jpg'.format(i))
            image=image.resize((640, 512), Image.ANTIALIAS)
            image.save('C:/Users/Francesco/Desktop/scene/immagini/TwoCarsTwoPeople/TwoCarsTwoPeople_{:d}.jpeg'.format(i), 'JPEG')
        else:
            image = Image.open('C:/Users/Francesco/Desktop/Materiale tesi/TwoCarsTwoPeople/TwoCarsTwoPeople_{:03d}.jpg'.format(i))
            image=image.resize((640, 512), Image.ANTIALIAS)
            image.save('C:/Users/Francesco/Desktop/scene/immagini/TwoCarsTwoPeople/TwoCarsTwoPeople_{:d}.jpeg'.format(i), 'JPEG')
for i in range(0,185): 
    print(i) 
    a=root[3][i].attrib
    a['ybr']=512-float(a['ybr'])
    a['ytl']=512-float(a['ytl'])
    xc=(float(a['xbr'])+float(a['xtl']))/2/640
    yc=(float(a['ytl'])+float(a['ybr']))/2/512
    wx=(float(a['xbr'])-float(a['xtl']))/640
    wy=(float(a['ytl'])-float(a['ybr']))/512
    with open("C:/Users/Francesco/Desktop/scene/labels/TwoCarsTwoPeople_{:d}.txt".format(i), 'a') as file:
        if xc!=0 and wx!=0:
            file.write("2")
            file.write(" ")
            file.write(str(xc))
            file.write(" ")
            file.write(str(1-yc))
            file.write(" ")
            file.write(str(wx))
            file.write(" ")
            file.write(str(wy))
            file.write("\n")            
            image = Image.open('C:/Users/Francesco/Desktop/Materiale tesi/TwoCarsTwoPeople/TwoCarsTwoPeople_{:03d}.jpg'.format(i))
            image=image.resize((640, 512), Image.ANTIALIAS)
            image.save('C:/Users/Francesco/Desktop/scene/immagini/TwoCarsTwoPeople/TwoCarsTwoPeople_{:d}.jpeg'.format(i), 'JPEG')
        else:
            image = Image.open('C:/Users/Francesco/Desktop/Materiale tesi/TwoCarsTwoPeople/TwoCarsTwoPeople_{:03d}.jpg'.format(i))
            image=image.resize((640, 512), Image.ANTIALIAS)
            image.save('C:/Users/Francesco/Desktop/scene/immagini/TwoCarsTwoPeople/TwoCarsTwoPeople_{:d}.jpeg'.format(i), 'JPEG')           









'''
#############################################################
import numpy
lista=[]
for i in range(82,83):
    with open("C:/Users/Francesco/Desktop/scene/labels/TwoCarsTwoPeople_{:d}.txt".format(i)) as file:
        liste=file.readlines()
        for j in liste:
            l1 = list(j.split(",")) 
            #print(li1)
            l1 = list(map(float, l1)) 
            for k in liste:
                l2 = list(k.split(","))
                l2 = list(map(float, l2)) 
                if (l1[3]+l2[3])>abs(l1[1]-l2[1]) and l1!=l2:
                    if l1[5]>l2[5]:
                        l1[3]=l2[1]-l1[1]-l2[3]
                    else:
                        l2[3]=l1[1]- (abs(l1[1]-l2[1])-l1[3]-l2[3])
            print(l1)





#l2[3]+intersezione due boxes





l1=['0', '0.656734375', '0.726455078125', '0.22984375000000004', '0.54708984375', '4.33']
l2=['2', '0.8027265625', '0.6795410156249999', '0.39454687499999996', '0.34974609375', '5.93']

l1 = list(map(float, l1))
l2 = list(map(float, l2))

(l1[3]+l2[3])>abs(l1[1]-l2[1])
l1[3]+l2[3]


'''

######################################################################################################
#3 cars 3 pedestrian
import shutil
import os
for i in range(0,240):
    src = r'C:/Users/Francesco/Desktop/FLIR_00343.txt'
    dst =  "C:/Users/Francesco/Desktop/scene/labels/3Cars3People_{:d}.txt".format(i)
    shutil.copyfile(src, dst)

import xml.etree.ElementTree as ET
from PIL import Image
tree = ET.parse('C:/Users/Francesco/Desktop/Materiale tesi/3Cars3People/annotations_xml.xml') #annotations_Scena02_Leopold #annotations_Scena03_Stefania
root = tree.getroot()
for i in range(240):
    for j in [0,2,5]:
        print(i)
        #person
        a=root[j][i].attrib
        a['ybr']=512-float(a['ybr'])
        a['ytl']=512-float(a['ytl'])
        xc=(float(a['xbr'])+float(a['xtl']))/2/640
        yc=(float(a['ytl'])+float(a['ybr']))/2/512
        wx=(float(a['xbr'])-float(a['xtl']))/640
        wy=(float(a['ytl'])-float(a['ybr']))/512
        with open("C:/Users/Francesco/Desktop/scene/labels/3Cars3People_{:d}.txt".format(i), 'a') as file:
            if xc==0 and wx==0:
                image = Image.open('C:/Users/Francesco/Desktop/Materiale Tesi/3Cars3People/3Cars3People/ThreeCars_ThreePeople_Inserimento_{:03d}.jpg'.format(i))
                image=image.resize((640, 512), Image.ANTIALIAS)
                image.save('C:/Users/Francesco/Desktop/scene/immagini/TwoCarsTwoPeople/3Cars3People_{:d}.jpeg'.format(i), 'JPEG')
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
                file.write("\n")
                image = Image.open('C:/Users/Francesco/Desktop/Materiale Tesi/3Cars3People/3Cars3People/ThreeCars_ThreePeople_Inserimento_{:03d}.jpg'.format(i))
                image=image.resize((640, 512), Image.ANTIALIAS)
                image.save('C:/Users/Francesco/Desktop/scene/immagini/3Cars3People/3Cars3People_{:d}.jpeg'.format(i), 'JPEG')
        #car -> nel xml sono state suddivise in car01 e car02, quindi farò due cicli


#cars
for i in range(0,240):
    for j in [1,3,4]:
        print(i)
        #person
        a=root[j][i].attrib
        a['ybr']=512-float(a['ybr'])
        a['ytl']=512-float(a['ytl'])
        xc=(float(a['xbr'])+float(a['xtl']))/2/640
        yc=(float(a['ytl'])+float(a['ybr']))/2/512
        wx=(float(a['xbr'])-float(a['xtl']))/640
        wy=(float(a['ytl'])-float(a['ybr']))/512
        with open("C:/Users/Francesco/Desktop/scene/labels/3Cars3People_{:d}.txt".format(i), 'a') as file:
            if xc==0 and wx==0:
                image = Image.open('C:/Users/Francesco/Desktop/Materiale Tesi/3Cars3People/3Cars3People/ThreeCars_ThreePeople_Inserimento_{:03d}.jpg'.format(i))
                image=image.resize((640, 512), Image.ANTIALIAS)
                image.save('C:/Users/Francesco/Desktop/scene/immagini/TwoCarsTwoPeople/3Cars3People_{:d}.jpeg'.format(i), 'JPEG')
                continue
            else:
                file.write("2")
                file.write(" ")
                file.write(str(xc))
                file.write(" ")
                file.write(str(1-yc))
                file.write(" ")
                file.write(str(wx))
                file.write(" ")
                file.write(str(wy))
                file.write("\n")
                image = Image.open('C:/Users/Francesco/Desktop/Materiale Tesi/3Cars3People/3Cars3People/ThreeCars_ThreePeople_Inserimento_{:03d}.jpg'.format(i))
                image=image.resize((640, 512), Image.ANTIALIAS)
                image.save('C:/Users/Francesco/Desktop/scene/immagini/3Cars3People/3Cars3People_{:d}.jpeg'.format(i), 'JPEG')
        #car -> nel xml sono state suddivise in car01 e car02, quindi farò due cicli









#3 cars 3 pedestrian second video
import shutil
import os
for i in range(0,210):
    src = r'C:/Users/Francesco/Desktop/FLIR_00063.txt'
    dst =  "C:/Users/Francesco/Desktop/scene/labels/3Cars3People_2_{:d}.txt".format(i)
    shutil.copyfile(src, dst)

import xml.etree.ElementTree as ET
from PIL import Image
tree = ET.parse('C:/Users/Francesco/Desktop/Materiale tesi/3Cars3People_2/annotations_xml.xml') #annotations_Scena02_Leopold #annotations_Scena03_Stefania
root = tree.getroot()
for i in range(210):
    for j in [0,3,5]:
        print(i)
        #person
        a=root[j][i].attrib
        a['ybr']=512-float(a['ybr'])
        a['ytl']=512-float(a['ytl'])
        xc=(float(a['xbr'])+float(a['xtl']))/2/640
        yc=(float(a['ytl'])+float(a['ybr']))/2/512
        wx=(float(a['xbr'])-float(a['xtl']))/640
        wy=(float(a['ytl'])-float(a['ybr']))/512
        with open("C:/Users/Francesco/Desktop/scene/labels/3Cars3People_2_{:d}.txt".format(i), 'a') as file:
            if xc==0 and wx==0:
                image = Image.open('C:/Users/Francesco/Desktop/Materiale Tesi/3Cars3People_2/3Cars3People_2/ThreeCars_ThreePeople_Inserimento_{:03d}.jpg'.format(i))
                image=image.resize((640, 512), Image.ANTIALIAS)
                image.save('C:/Users/Francesco/Desktop/scene/immagini/3Cars3People_2/3Cars3People_2_{:d}.jpeg'.format(i), 'JPEG')
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
                file.write("\n")
                image = Image.open('C:/Users/Francesco/Desktop/Materiale Tesi/3Cars3People_2/3Cars3People_2/ThreeCars_ThreePeople_Inserimento_{:03d}.jpg'.format(i))
                image=image.resize((640, 512), Image.ANTIALIAS)
                image.save('C:/Users/Francesco/Desktop/scene/immagini/3Cars3People_2/3Cars3People_2_{:d}.jpeg'.format(i), 'JPEG')
        #car -> nel xml sono state suddivise in car01 e car02, quindi farò due cicli


#cars
for i in range(210):
    for j in [1,2,4]:
        print(i)
        #person
        a=root[j][i].attrib
        a['ybr']=512-float(a['ybr'])
        a['ytl']=512-float(a['ytl'])
        xc=(float(a['xbr'])+float(a['xtl']))/2/640
        yc=(float(a['ytl'])+float(a['ybr']))/2/512
        wx=(float(a['xbr'])-float(a['xtl']))/640
        wy=(float(a['ytl'])-float(a['ybr']))/512
        with open("C:/Users/Francesco/Desktop/scene/labels/3Cars3People_2_{:d}.txt".format(i), 'a') as file:
            if xc==0 and wx==0:
                image = Image.open('C:/Users/Francesco/Desktop/Materiale Tesi/3Cars3People_2/3Cars3People_2/ThreeCars_ThreePeople_Inserimento_{:03d}.jpg'.format(i))
                image=image.resize((640, 512), Image.ANTIALIAS)
                image.save('C:/Users/Francesco/Desktop/scene/immagini/3Cars3People_2/3Cars3People_2_{:d}.jpeg'.format(i), 'JPEG')
                continue
            else:
                file.write("2")
                file.write(" ")
                file.write(str(xc))
                file.write(" ")
                file.write(str(1-yc))
                file.write(" ")
                file.write(str(wx))
                file.write(" ")
                file.write(str(wy))
                file.write("\n")
                image = Image.open('C:/Users/Francesco/Desktop/Materiale Tesi/3Cars3People_2/3Cars3People_2/ThreeCars_ThreePeople_Inserimento_{:03d}.jpg'.format(i))
                image=image.resize((640, 512), Image.ANTIALIAS)
                image.save('C:/Users/Francesco/Desktop/scene/immagini/3Cars3People_2/3Cars3People_2_{:d}.jpeg'.format(i), 'JPEG')
        #car -> nel xml sono state suddivise in car01 e car02, quindi farò due cicli


##########################################################################################




#3 cars 6 pedestrians video
import shutil
import os
for i in range(600):
    src = r'C:/Users/Francesco/Desktop/FLIR_00063.txt'
    dst =  "C:/Users/Francesco/Desktop/scene/labels/3Cars6People_{:d}.txt".format(i)
    shutil.copyfile(src, dst)

import xml.etree.ElementTree as ET
from PIL import Image
tree = ET.parse('C:/Users/Francesco/Desktop/Materiale tesi/3Cars6People/annotations_xml.xml') #annotations_Scena02_Leopold #annotations_Scena03_Stefania
root = tree.getroot()
for i in range(0,600):
    for j in [1,2,4,6,7,8]:
        print(i)
        #person
        a=root[j][i].attrib
        a['ybr']=512-float(a['ybr'])
        a['ytl']=512-float(a['ytl'])
        xc=(float(a['xbr'])+float(a['xtl']))/2/640
        yc=(float(a['ytl'])+float(a['ybr']))/2/512
        wx=(float(a['xbr'])-float(a['xtl']))/640
        wy=(float(a['ytl'])-float(a['ybr']))/512
        with open("C:/Users/Francesco/Desktop/scene/labels/3Cars6People_{:d}.txt".format(i), 'a') as file:
            if xc==0 and wx==0:
                image = Image.open('C:/Users/Francesco/Desktop/Materiale Tesi/3Cars6People/3Cars6People/ThreeCars_SixPeople_Inserimento_{:03d}.jpg'.format(i))
                image=image.resize((640, 512), Image.ANTIALIAS)
                image.save('C:/Users/Francesco/Desktop/scene/immagini/3Cars6People/3Cars6People_{:d}.jpeg'.format(i), 'JPEG')
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
                file.write("\n")
                image = Image.open('C:/Users/Francesco/Desktop/Materiale Tesi/3Cars6People/3Cars6People/ThreeCars_SixPeople_Inserimento_{:03d}.jpg'.format(i))
                image=image.resize((640, 512), Image.ANTIALIAS)
                image.save('C:/Users/Francesco/Desktop/scene/immagini/3Cars6People/3Cars6People_{:d}.jpeg'.format(i), 'JPEG')
        #car -> nel xml sono state suddivise in car01 e car02, quindi farò due cicli


#cars
for i in range(0,600):
    for j in [0,3,5]:
        print(i)
        #person
        a=root[j][i].attrib
        a['ybr']=512-float(a['ybr'])
        a['ytl']=512-float(a['ytl'])
        xc=(float(a['xbr'])+float(a['xtl']))/2/640
        yc=(float(a['ytl'])+float(a['ybr']))/2/512
        wx=(float(a['xbr'])-float(a['xtl']))/640
        wy=(float(a['ytl'])-float(a['ybr']))/512
        with open("C:/Users/Francesco/Desktop/scene/labels/3Cars6People_{:d}.txt".format(i), 'a') as file:
            if xc==0 and wx==0:
                image = Image.open('C:/Users/Francesco/Desktop/Materiale Tesi/3Cars6People/3Cars6People/ThreeCars_SixPeople_Inserimento_{:03d}.jpg'.format(i))
                image=image.resize((640, 512), Image.ANTIALIAS)
                image.save('C:/Users/Francesco/Desktop/scene/immagini/3Cars6People/3Cars6People_{:d}.jpeg'.format(i), 'JPEG')
                continue
            else:
                file.write("2")
                file.write(" ")
                file.write(str(xc))
                file.write(" ")
                file.write(str(1-yc))
                file.write(" ")
                file.write(str(wx))
                file.write(" ")
                file.write(str(wy))
                file.write("\n")
                image = Image.open('C:/Users/Francesco/Desktop/Materiale Tesi/3Cars6People/3Cars6People/ThreeCars_SixPeople_Inserimento_{:03d}.jpg'.format(i))
                image=image.resize((640, 512), Image.ANTIALIAS)
                image.save('C:/Users/Francesco/Desktop/scene/immagini/3Cars6People/3Cars6People_{:d}.jpeg'.format(i), 'JPEG')



#ad ogni modo la mia idea è che avendo cosi tanti oggetti per immagine, il numero necessario sia inferiore a quello di fabio, leopold e stefania.


#3 cars 7 pedestrians video
import shutil
import os
for i in range(1000):
    src = r'C:/Users/Francesco/Desktop/FLIR_00432.txt'
    dst =  "C:/Users/Francesco/Desktop/scene/labels/3Cars7People_{:d}.txt".format(i)
    shutil.copyfile(src, dst)

import xml.etree.ElementTree as ET
from PIL import Image
tree = ET.parse('C:/Users/Francesco/Desktop/Materiale tesi/3Cars7People/annotations_xml.xml') #annotations_Scena02_Leopold #annotations_Scena03_Stefania
root = tree.getroot()
for i in range(0,1000):
    for j in [0,1,3,5,6,7,8]:
        print(i)
        #person
        a=root[j][i].attrib
        a['ybr']=512-float(a['ybr'])
        a['ytl']=512-float(a['ytl'])
        xc=(float(a['xbr'])+float(a['xtl']))/2/640
        yc=(float(a['ytl'])+float(a['ybr']))/2/512
        wx=(float(a['xbr'])-float(a['xtl']))/640
        wy=(float(a['ytl'])-float(a['ybr']))/512
        with open("C:/Users/Francesco/Desktop/scene/labels/3Cars7People_{:d}.txt".format(i), 'a') as file:
            if xc==0 and wx==0:
                image = Image.open('C:/Users/Francesco/Desktop/Materiale Tesi/3Cars7People/3Cars7People/ThreeCars_SevenPeople_Inserimento_{:04d}.jpg'.format(i))
                image=image.resize((640, 512), Image.ANTIALIAS)
                image.save('C:/Users/Francesco/Desktop/scene/immagini/3Cars7People/3Cars7People_{:d}.jpeg'.format(i), 'JPEG')
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
                file.write("\n")
                image = Image.open('C:/Users/Francesco/Desktop/Materiale Tesi/3Cars7People/3Cars7People/ThreeCars_SevenPeople_Inserimento_{:04d}.jpg'.format(i))
                image=image.resize((640, 512), Image.ANTIALIAS)
                image.save('C:/Users/Francesco/Desktop/scene/immagini/3Cars7People/3Cars7People_{:d}.jpeg'.format(i), 'JPEG')
        #car -> nel xml sono state suddivise in car01 e car02, quindi farò due cicli


#cars
for i in range(0,1000):
    for j in [2,4,9]:
        print(i)
        #person
        a=root[j][i].attrib
        a['ybr']=512-float(a['ybr'])
        a['ytl']=512-float(a['ytl'])
        xc=(float(a['xbr'])+float(a['xtl']))/2/640
        yc=(float(a['ytl'])+float(a['ybr']))/2/512
        wx=(float(a['xbr'])-float(a['xtl']))/640
        wy=(float(a['ytl'])-float(a['ybr']))/512
        with open("C:/Users/Francesco/Desktop/scene/labels/3Cars7People_{:d}.txt".format(i), 'a') as file:
            if xc==0 and wx==0:
                image = Image.open('C:/Users/Francesco/Desktop/Materiale Tesi/3Cars7People/3Cars7People/ThreeCars_SevenPeople_Inserimento_{:04d}.jpg'.format(i))
                image=image.resize((640, 512), Image.ANTIALIAS)
                image.save('C:/Users/Francesco/Desktop/scene/immagini/3Cars7People/3Cars7People_{:d}.jpeg'.format(i), 'JPEG')
                continue
            else:
                file.write("2")
                file.write(" ")
                file.write(str(xc))
                file.write(" ")
                file.write(str(1-yc))
                file.write(" ")
                file.write(str(wx))
                file.write(" ")
                file.write(str(wy))
                file.write("\n")
                image = Image.open('C:/Users/Francesco/Desktop/Materiale Tesi/3Cars7People/3Cars7People/ThreeCars_SevenPeople_Inserimento_{:04d}.jpg'.format(i))
                image=image.resize((640, 512), Image.ANTIALIAS)
                image.save('C:/Users/Francesco/Desktop/scene/immagini/3Cars7People/3Cars7People_{:d}.jpeg'.format(i), 'JPEG')












