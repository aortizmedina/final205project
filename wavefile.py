
#**********************************All team members worked on this*******************************************************


#this is going to take the "average" of the red, green, and blue values. It well then create a 3 frequencies and write a wave file.
# def wavfile(red,green,blue)
#samples per second
samples_s = 44100

# red_freq = np.mean(red) + 80
# green_freq = np.mean(green) + 80
# blue_freq = np.mean(blue) + 80

#frequency of sine wave, concert a
freq_hz1 =121.683038822 # numbers are for testing
freq_hz2 = 118.241009371
freq_hz3 = 110.635499331
#duration in seconds
duration_s = 3.0

sample_nums = np.arange(duration_s * samples_s)

#print(sample_nums[0:40])

waveform = np.sin(2 * np.pi * sample_nums * freq_hz / samples_s)

waveform2 = np.sin(2 * np.pi * sample_nums * freq_hz2 / samples_s)

waveform_quiet = waveform * 0.3
waveform_quiet2 = waveform2 * 0.3

waveform_integers = np.int16(waveform_quiet * 32767)

write('sound.wave', samples_s, waveform_integers)
