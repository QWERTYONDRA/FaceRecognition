from PIL import Image
import PIL.ImageOps 
 
#read the image
color_image = Image.open('kocka-C.jpg')
 
#convert the image to black and white mode with dither set to None
bw = color_image.convert('1', dither=Image.NONE)
 
#save the image with name "BW_image.jpg"
bw.save('BW.jpg')

image = Image.open('BW.jpg')

inverted_image = PIL.ImageOps.invert(image)

inverted_image.save('inverted.jpg')