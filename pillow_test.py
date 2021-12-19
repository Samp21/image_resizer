from PIL import Image
import os

size_300 = (300, 300)

for file in os.listdir('./resources'):
    if file.endswith('.jpg'):
        # print (file)
        i = Image.open('./resources/' + file)
        filename, file_extension = os.path.splitext(file)
        # print (filename)

        # resize images
        i.thumbnail(size_300)
        i.save('output/{}_300.{}'.format(filename, file_extension))

        # save images in pngs dir 
        # i.save('pngs/{}.png'.format(filename))

        

# path = 'resources/tv01.jpg'

# image01 = Image.open(path)
# image01.show()

# save as different format
# image01.save('TV_PNG.png')
