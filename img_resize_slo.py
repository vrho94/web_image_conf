from PIL import Image
import os

print('****************************************')
file_location=os.popen('pwd').read()
print('Datoteke v '+file_location)
print(os.popen('ls').read())
print('****************************************')
print('Vnesi ime slike, ki jo želiš obdelati:')
image_name=input()

try:
    image = Image.open(image_name)
except:
    print("Ta datoteka ne obstaja!")
    exit()

print('Vnesi faktor pomanšanja:')
try:
    downscale_fac=float(input())
except:
    print('Vnos faktorja mora biti številsko!')
    exit()
old_width=str(image.width)
old_height=str(image.height)
newImage = image.resize((int(image.width/downscale_fac),int(image.height/downscale_fac)))
new_width=str(newImage.width)
new_height=str(newImage.height)
print('****************************************')
print('Vnesi ime slike:')
newImage_name=input()
newImage.save(newImage_name+'.jpg')
print('****************************************')
print('****************************************')
print('Shranjeno!:'+newImage_name)
print('Resolucija spremenjena iz '+old_width+'x'+old_height+' na '+new_width+'x'+new_height+'.')
print('****************************************')
print('****************************************')
