from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import Property
from kivy.lang import Builder
import MFCC_utils as mu
import time

Builder.load_file('./MFCC_test.kv')

class MyLayout(Widget):
    def press(self):
        carhorn_path_dir = "./MFCC_Test/"
        carhorn_file_list = []
        for name in mu.load_file(carhorn_path_dir):
            carhorn_file_list.append(carhorn_path_dir+name)
        
        start = time.time()
        carhorn = mu.mfcc(carhorn_file_list[0])
        end = time.time()
                
        result = str(end-start)[:6]
        self.ids.result.text = f'Hello {result}!'
        
        
class AwesomeApp(App):
    def build(self):
        return MyLayout()

if __name__ == "__main__":
    AwesomeApp().run()