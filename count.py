from PIL import Image
import colorsys

im = Image.open("smokestack_cropped_sm.jpg")   
out = Image.new('I', im.size, 0xffffff)

green = 0
blue = 0
neither = 0

width, height = im.size
for x in range(width):
    for y in range(height):
        r,g,b = im.getpixel((x,y))
        h,s,v = colorsys.rgb_to_hsv(float(r)/255,float(g)/255,float(b)/255)
        if h * 360 >= 81 and h * 360 <= 160:
            green += 1
        elif h * 360 >= 161 and h * 360 <= 240:
            blue += 1
        else:
            neither += 1
        print green, blue, neither
print green, blue, neither
        