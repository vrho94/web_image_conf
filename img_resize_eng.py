from PIL import Image
import os

print('****************************************')
file_location=os.popen('pwd').read()
print('Files in '+file_location)
print(os.popen('ls').read())
print('****************************************')
print('Chose the image:')
image_name=input()

try:
    image = Image.open(image_name)
except:
    print("Thise image doesen't exist!")
    exit()

print('Enter the decrease factor:')
try:
    downscale_fac=float(input())
except:
    print('The factor input must be numeric!')
    exit()
newImage = image.resize((int(image.width/downscale_fac),int(image.height/downscale_fac)))
print('****************************************')
print('Enter a name for the image:')
newImage_name=input()
newImage.save(newImage_name+'.jpg')
print('****************************************')
print('Saved!:'+newImage_name)
print('****************************************')
