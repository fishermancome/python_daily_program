'''将你的 QQ 头像（或者微博头像）右上角加上红色的数字，
类似于微信未读信息数量那种提示效果。'''
from PIL import Image,ImageDraw,ImageFont
import random


mes = "f**k WFG[::-1]"


im = Image.open('test.png')
w,h = im.size
wDraw = 0.1 * w
hDraw = 0.3 * h


font = ImageFont.truetype('arial.ttf',60)
draw = ImageDraw.Draw(im)
draw.text((wDraw,hDraw), mes,font=font, fill='blue')


im.save('we.png', 'png')
