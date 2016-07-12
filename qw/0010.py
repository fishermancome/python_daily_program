import random
import string
from PIL import Image,ImageFilter,ImageFont,ImageDraw

letters = string.ascii_letters + string.digits


def rnd_letter():
    return random.choice(letters)


def rnd_color():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

def rnd_color2():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))


def generate_verification_chart(i):
    width = 60*4
    height = 60

    image = Image.new('RGB',(width,height),(255,255,255))

    font = ImageFont.truetype('arial.ttf',36)

    draw = ImageDraw.Draw(image)

    for x in range(width):
        for y in range(height):
            draw.point((x,y),fill=rnd_color())

    for t in range(4):
        draw.text((60*t+10,10),rnd_letter(),font=font,fill=rnd_color2())

    image = image.filter(ImageFilter.BLUR)
    image.save('code.jpg'+str(i),'jpeg')

if __name__ =="__main__":
    for i in range(4):
        print(i)
        generate_verification_chart(i)
    
