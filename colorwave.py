# Example showing how functions, that accept tuples of rgb values,
# simplify working with gradients

import time
from neopixel import Neopixel

numpix = 48
strip = Neopixel(numpix, 0, 28, "GRB")
#strip = Neopixel(numpsix, 0, 0, "GRBW")

red = (255, 0, 0)
orange = (255, 50, 0)
yellow = (255, 100, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
indigo = (100, 0, 90)
violet = (200, 0, 100)
black = (0,0,0)
white = (255,255,255)
colors_rgb = [red, orange, yellow, green, blue, indigo, violet]
#colors_rgb = [red, black,black,black,black,black,black]
# same colors as normaln rgb, just 0 added at the end
#colors_rgbw = [color+tuple([0]) for color in colors_rgb]
#colors_rgbw.append((0, 0, 0, 255))

# uncomment colors_rgbw if you have RGBW strip
colors = colors_rgb
#colors = colors_rgbw


#step = round(numpix / len(colors))
#current_pixel = 0
strip.brightness(50)

#for color1, color2 in zip(colors, colors[1:]):
#    strip.set_pixel_line_gradient(current_pixel, current_pixel + step, color1, color2)
#    current_pixel += step

#strip.set_pixel_line_gradient(current_pixel, numpix - 1, violet, red)

strip.fill(black)
strip.show()
strip.set_pixel(1,red)
#strip.set_pixel_line(0,8,red)
strip.show()
strip.rotate_left(1)
strip.show()
strip.rotate_left(1)
strip.show()
strip.rotate_left(1)
strip.show()

for i in range(12):
    strip.rotate_right(1)
    time.sleep(1)
    strip.show()
