# Course: CST205
# Title: gettuples.py(205 final project)
# Abstract: We are creating a multimedia program that will allow a user to listen to a unique sound from a picture
# Authors: Angel Ortiz, Roberto Bradley, Edith Gonzalez, Mac Cooper
# Date: December 9, 2017
from PIL import Image


#************************************** Roberto's Work **************************************************************
def get_tuples(file_name):
    im = Image.open("./static/" + file_name + ".jpg")
    width, height = im.size

    pixel_list = []

    for x in range(width):
        for y in range(height):
            pixel_list.append(im.getpixel((x,y)))
    return pixel_list

#This takes a list of lists and assigns it to red green and blue.
# firstImage = get_tuples("randbear")
# reds,greens,blues = get_colors(firstImage)
# average_blue = np.mean(blues)
# print(average_blue)
