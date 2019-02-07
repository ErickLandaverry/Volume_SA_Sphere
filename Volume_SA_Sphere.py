import math
pi = math.pi

def sphereVolume(r):
  vol  = (4/3) * pi * r * r * r
  return vol

def sphereArea(r):
  surface = 4 * pi * r * r
  return surface

radius = float(input("What is the radius?:" ))
print( "The volume of the Sphere is :" , sphereVolume(radius))
print( "The surface area of the Sphere is :", sphereArea(radius))
