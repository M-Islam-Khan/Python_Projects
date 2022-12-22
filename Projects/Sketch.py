#Available images in  sketchpy
'''from sketchpy import library as lib
obj = lib.rdj()
obj.draw()'''

from sketchpy import canvas
obj = canvas.sketch_from_image("D:\Sketch Sami\Sami2.jpg")
obj.draw(threshold = 127)