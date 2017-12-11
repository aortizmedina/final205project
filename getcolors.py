# Course: CST205
# Title: getcolors.py(205 final project)
# Abstract: We are creating a multimedia program that will allow a user to listen to a unique sound from a picture
# Authors: Angel Ortiz, Roberto Bradley, Edith Gonzalez, Mac Cooper
# Date: December 9, 2017
#********************************Roberto's Work***************************************************
# This function has 4 dictionaries 3 for RGB colors and 1 for all the colors.At the en
#returns all the colors in the last dictionary.
def get_colors(pixel_list):
    red_pixels = []
    blue_pixels = []
    green_pixels = []
    all_colors = []
    for element in pixel_list:
        red_pixels.append(element[0])
        green_pixels.append(element[1])
        blue_pixels.append(element[2])
    all_colors.extend([red_pixels,green_pixels,blue_pixels])
    return all_colors
