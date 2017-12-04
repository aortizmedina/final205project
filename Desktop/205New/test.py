from dict import image_info #import of dicitionary
from wavefile import wavfile #import of function
from getcolors import get_colors #import of function
from gettuples import get_tuples #import of function
import numpy as np
from PIL import Image
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from scipy.io.wavfile import write
import pyaudio
import wave


app = Flask(__name__)
Bootstrap(app)

#**************************Roberto's Work **********************************************
@app.route('/')
@app.route('/home')
def home():

    id1 = image_info[0]["id"]
    id2 = image_info[1]["id"]
    id3 = image_info[2]["id"]

    title1 = image_info[0]["title"]
    title2 = image_info[1]["title"]
    title3 = image_info[2]["title"]

    return render_template('home.html', title1 = title1, title2 = title2, title3 = title3 , id1 =id1, id2 = id2, id3 = id3)
# *************************ANGEL'S WORK ************************************************
@app.route('/play/<id>')
def play(id):
    chunk = 1024

    #open a wav format music
    #THIS IS WHERE WE ARE WITH THE SOUND
    f = wave.open(r'/static/'+ {id} + '.wav',"rb")
    #instantiate PyAudio
    p = pyaudio.PyAudio()
    #open stream
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
                    channels = f.getnchannels(),
                    rate = f.getframerate(),
                    output = True)
    #read data
    data = f.readframes(chunk)

    #play stream
    while data:
        stream.write(data)
        data = f.readframes(chunk)

    #stop stream
    stream.stop_stream()
    stream.close()
    # return 'this is the home page'
    return render_template('play.html')
    #close PyAudio
    p.terminate()
