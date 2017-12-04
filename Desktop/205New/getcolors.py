#********************************Roberto's Work***************************************************
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
