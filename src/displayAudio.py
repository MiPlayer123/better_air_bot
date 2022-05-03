import sys
import time
from PIL import Image,ImageDraw,ImageFont
sys.path.insert(1, '/home/mikul/git_clones/Environment_sensor_fot_jetson_nano')
import SH1106 #OLED

oled = SH1106.SH1106()
image = Image.new('1', (oled.width, oled.height), "BLACK")
draw = ImageDraw.Draw(image)
x = 0
font = ImageFont.truetype('Font.ttc', 10)

time.sleep(1)
print("Ready")
#Display stuff
draw.rectangle((0, 0, 128, 64), fill = 0)

draw.text((0, 0), "Background", font = font, fill = 1)
oled.display(image)
print("Background")
time.sleep(4)

draw.rectangle((0, 0, 128, 64), fill = 0)
draw.text((0, 0), "GlassBreak", font = font, fill = 1)
oled.display(image)
print("GlassBreak")
time.sleep(4)

image2 = Image.new('1', (oled.width, oled.height), "BLACK")
oled.display(image2)
print("Cleared")
exit()