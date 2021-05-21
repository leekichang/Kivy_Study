from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

import os, glob
import librosa
import librosa.display
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
import sklearn.preprocessing
import time

def load_file(path_dir):
    files = os.listdir(path_dir)
    return [file for file in files if file.endswith(".wav")]

def mfcc(file):
    mfcc_list=[]
    audio, sr = librosa.load(file, sr=None)
    hop_length = 256
    n_fft = 1024
    n_mfcc = 20
    mfcc = librosa.feature.mfcc(audio, sr=44100, n_mfcc=n_mfcc, n_fft=n_fft, hop_length=hop_length)
    mfcc = sklearn.preprocessing.scale(mfcc, axis=1)
    pad2d = lambda a, i: a[:, 0:i] if a.shape[1] > i else np.hstack((a, np.zeros((a.shape[0], i-a.shape[1]))))
    mfcc_list.append(pad2d(mfcc, 100))
    return mfcc_list

carhorn_path_dir = "./MFCC_Test/"
carhorn_file_list = []

for name in load_file(carhorn_path_dir):
    carhorn_file_list.append(carhorn_path_dir+name)

test_text = 'Press Button to run MFCC'
elapsed_time = 'MFCC Result'
class MFCCApp(App):

    def button_click_callback(self, instance):
        start = time.time()
        carhorn = mfcc(carhorn_file_list[0])
        end = time.time()
        elapsed_time = str(end-start)[:6]

    def build(self):
        layout = BoxLayout(padding=10)
        button = Button(text=elapsed_time, size_hint=(.5, .5), font_size=12)
        button2 = Button(text=test_text, size_hint=(.5, .5), font_size=12)
        button2.bind(on_press=self.button_click_callback)
        layout.add_widget(button)
        layout.add_widget(button2)
        return layout

if __name__ == "__main__":
    MFCCApp().run()