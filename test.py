from image_dictionary import image_info #import of dicitionary
from wavefile import make_wave #import of function
from getcolors import get_colors #import of function
from gettuples import get_tuples #import of function
import numpy as np
from PIL import Image
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from scipy.io.wavfile import write
import wave
import pyaudio
# import wavefile


app = Flask(__name__)
Bootstrap(app)

#**************************Roberto's Work **********************************************
@app.route('/')
@app.route('/home')
def home():

    #this gets the id of each picture
    id1 = image_info[0]["id"]
    id2 = image_info[1]["id"]
    id3 = image_info[2]["id"]

    #this gets the title of each picture
    title1 = image_info[0]["title"]
    title2 = image_info[1]["title"]
    title3 = image_info[2]["title"]

    #this gets the tuples from each picture using the id
    firstImage = get_tuples(id1)
    secondImage = get_tuples(id2)
    thirdImage = get_tuples(id3)

    #gets the colors from the tuples
    reds_1,greens_1,blues_1 = get_colors(firstImage)
    reds_2,greens_2,blues_2 = get_colors(secondImage)
    reds_3,greens_3,blues_3 = get_colors(thirdImage)

    #makes the unique sound from the colors of each picture
    make_wave(reds_1,greens_1,blues_1, id1)
    make_wave(reds_2,greens_2,blues_2, id2)
    make_wave(reds_3,greens_3,blues_3, id3)

    return render_template('home.html', title1 = title1, title2 = title2, title3 = title3 , id1 =id1, id2 = id2, id3 = id3)
# *************************ANGEL'S WORK ************************************************
@app.route('/play/<id>', methods=['GET','POST'])
def play(id):
    chunk = 1024

    #open a wav format music
    #THIS IS WHERE WE ARE WITH THE SOUND
    f = wave.open(r'./static/'+ id + '.wav',"rb")
    #instantiate PyAudio
    p = pyaudio.PyAudio()
    #open stream
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
                    channels = f.getnchannels(),
                    rate = f.getframerate(),
                    output = True)
    #read data
    data = f.readframes(chunk)

    #play stream to play the sound
    while data:
        stream.write(data)
        data = f.readframes(chunk)

    #stop stream
    stream.stop_stream()
    stream.close()
    # return 'this is the home page'
    #close PyAudio
    p.terminate()

    return render_template('play.html', id = id)
