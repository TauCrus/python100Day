'''用Pillow操作图像'''

from PIL import Image

image = Image.open('./res/ball.png')
print(image.format)
print(image.size)
print(image.mode)
image.show()
