import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

RESET_PIN = digitalio.DigitalInOut(board.D4)

i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(128,64,i2c,addr=0x3c, reset=RESET_PIN)

image = Image.new("1",(oled.width, oled.height))
draw = ImageDraw.Draw(image)

oled.fill(0)
oled.show()

font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",20)
font2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",10)

draw.text((0,0),"1506", font=font, fill=255)
draw.text((0,25),"Kim Myung Woo", font=font2, fill=255)
draw.text((0,45),"Fun Iot Class", font=font2, fill=255)

oled.image(image)
oled.show()