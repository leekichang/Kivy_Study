from kivy.app import App
from kivy.uix.button import Button
class MFCCApp(App):
    def build(self):
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

        carhorn_path_dir = "./"
        carhorn_file_list = []

        start = time.time()
        for name in load_file(carhorn_path_dir):
            carhorn_file_list.append(carhorn_path_dir+name)
        end = time.time()

        print(f'file loading done took {end-start:.3f} sec')

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

        start = time.time()
        carhorn = mfcc(carhorn_file_list[0])
        end = time.time()

        print(f'MFCC don took {end-start:.3f} sec')
        return Button(text=str(end-start))

if __name__ == "__main__":
    

    MFCCApp().run()