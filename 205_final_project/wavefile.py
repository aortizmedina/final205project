import numpy as np
from scipy.io.wavfile import write
#**********************************All team members worked on this*******************************************************


#this is going to take the "average" of the red, green, and blue values. It well then create a 3 frequencies and write a wave file.
# def wavfile(red,green,blue)
#samples per second
#Roberto and Mac worked on this section
def make_wave(reds,greens,blues, id):
    samples_s = 44100

    # red_freq = np.mean(red) + 80
    # green_freq = np.mean(green) + 80
    # blue_freq = np.mean(blue) + 80

    #frequency of sine wave, concert a
    freq_red = np.mean(reds)
    freq_green = np.mean(greens)
    freq_blue = np.mean(blues)

    #if statements for making wave files more unique
    #Everyone worked on this section
    if (freq_red < 105):
        freq_red += 180
    if(freq_green < 105):
        freq_green += 180
    if(freq_blue < 105):
        freq_blue += 180

    if (freq_red < 120):
        freq_red += 360
    if (freq_green < 120):
        freq_green += 360
    if (freq_blue < 155):
        freq_blue += 360

    if (freq_red < 160):
        freq_red += 420
    if (freq_green < 160):
        freq_green += 420
    if (freq_blue < 160):
        freq_blue += 420

    if (freq_red < 255):
        freq_red += 540
    if (freq_green < 255):
        freq_green += 540
    if (freq_blue < 255):
        freq_blue += 540

    #duration in seconds
    duration_s = 3.0
#Roberto and Mac work on this section with the TA
    sample_nums = np.arange(duration_s * samples_s)

    R_waveform = np.sin(2 * np.pi * sample_nums * freq_red / samples_s)
    G_waveform = np.sin(2 * np.pi * sample_nums * freq_green / samples_s)
    B_waveform = np.sin(2 * np.pi * sample_nums * freq_blue / samples_s)

    waveform_quiet = R_waveform * 0.75
    waveform_quiet2 = G_waveform * 0.75
    waveform_quiet3 = B_waveform * 0.75

    R_waveform_integers = np.int16(waveform_quiet * 32767)
    G_waveform_integers = np.int16(waveform_quiet2 * 32767)
    B_waveform_integers = np.int16(waveform_quiet3 * 32767)

    all_color_sounds = R_waveform + G_waveform + B_waveform

    #concat = np.concatenate((R_waveform_integers,G_waveform_integers,B_waveform_integers))

    # write('./static/'+ id + '.wav', samples_s, all_color_sounds)
