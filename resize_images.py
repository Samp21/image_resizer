# https://www.youtube.com/watch?v=uR50xQX27-g
# https://www.youtube.com/watch?v=6Qs3wObeWwc

import os
from PIL import Image

# path_resources = '.'
path_resources = './resources/'
path_output = './output/'

# decalre target width
target_size = 600
min_size = 500

def process_images():
    # loop directory to find filenames
    for file in os.listdir(path_resources):
        # get image
        image = Image.open(path_resources + file)

        # get image width, height
        width, height = image.size

        if width > target_size or height > target_size:
            image = shrink_image(image, width, height)
            width, height = image.size
        elif width < min_size or height < min_size:
            image =  expand_image(image, width, height)
            width, height = image.size

        # calculate offset
        height_offset = (target_size - height) // 2
        width_offset = (target_size - width) // 2

        # first and second params are for top left corner of image
        # third and forth params are for bottom right corner of image
        area = (width_offset, 0 + height_offset, width + width_offset, height + height_offset)

        # combine the two images
        template = Image.open('template.jpg')
        template.paste(image, area)

        # template.show()
        save_image(template, file)

def shrink_image(image, width, height):
    if width > height:
        reduce_by = width/target_size
    else:
        reduce_by = height/target_size

    new_width = int(width//reduce_by)
    new_height = int(height//reduce_by)
    image = image.resize((new_width, new_height))

    return image

def expand_image(image, width, height):
    if width > height:
        expand_by = width/target_size
    else:
        expand_by = height/target_size

    new_width = int(width//expand_by)
    new_height = int(height//expand_by)
    image = image.resize((new_width, new_height))

    return image

def save_image(template, file):
    prefix = 'ipad-'
    template.save('output/{}{}'.format(prefix, file))

if __name__ == "__main__":
     process_images()
