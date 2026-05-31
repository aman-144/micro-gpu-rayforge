import numpy
from PIL import Image
height= 600
width =800

sphere={
  "center" : (0,0,-5),
  "radius" : 1
}
image  = numpy.zeros((height,width,3),dtype=numpy.uint8)
to_save = Image.fromarray(image)
to_save.save("output.png")
print("Image Saved!!")



