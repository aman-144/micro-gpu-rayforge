import numpy
from PIL import Image

height = 600
width = 800

def dot(v1, v2):
    return (v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2])
    
def subtract(v1, v2): # Spelling fix kar di
    return (v1[0]-v2[0], v1[1]-v2[1], v1[2]-v2[2])

sphere = {
  "center" : (0, 0, -5),
  "radius" : 1
}

def hit_sphere(sphere, ray_origin, ray_direction):
    a = dot(ray_direction, ray_direction)
    a1 = subtract(ray_origin, sphere["center"])
    b = 2 * dot(a1, ray_direction)
    c = dot(a1, a1) - sphere["radius"]**2
    discriminant = b**2 - 4*a*c
    
    if discriminant >= 0:
        return True
    else:
        return False
        
image = numpy.zeros((height, width, 3), dtype=numpy.uint8)

for i in range(height):
    for j in range(width):
        ray_origin = (0, 0, 0)
        ray_direction = (j/width - 0.5, i/height - 0.5, -1)
        
      
        # Ab hum function call karke check karenge ki hit hua ya nahi
        if hit_sphere(sphere, ray_origin, ray_direction):
            # Agar hit hua, toh is pixel ko Red color (R=255, G=0, B=0) de denge
            image[i, j] = [255, 0, 0]

to_save = Image.fromarray(image)
to_save.save("sphere_traced_red.png")
print("Image Saved as sphere_traced_red.png!!")