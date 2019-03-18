# 将图片转换成黑白效果
from PIL import Image
import numpy as np

for i in range(10):
    img = Image.open('{}.jpg'.format(i+1))
    img_cv = img.convert('L')
    img_cv.save('Gray{}.jpg'.format(i+1))
    
# 制作gif图片
import imageio  

def create_gif(image_list, gif_name):  
    ls = []  
    for image_name in image_list:  
        ls.append(imageio.imread(image_name))  
    imageio.mimsave(gif_name, ls, 'GIF', duration = 0.5)

  
def main():  
    image_list = ['1.jpg', 'Gray1.jpg', '2.jpg','Gray2.jpg', '3.jpg',
                  'Gray3.jpg','4.jpg', 'Gray4.jpg', '5.jpg','Gray5.jpg',
                  '6.jpg', 'Gray6.jpg', '7.jpg','Gray7.jpg', '8.jpg',
                  'Gray8.jpg','9.jpg', 'Gray9.jpg', '10.jpg','Gray10.jpg']  
    gif_name = 'New.gif'
    #调用创建的gif函数
    create_gif(image_list, gif_name)

main()
    
