import kivy
kivy.require('1.0.6')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MyApp(App):

    def button_click_callback(self, instance):
        print('The button <%s> is being pressed' % instance.text)
        
    def build(self):
        layout = BoxLayout(padding=10)
        button = Button(text='Train', size_hint=(.5, .0), font_size=12)
        button.bind(on_press=self.button_click_callback)
        button2 = Button(text='Test', size_hint=(.5, .0), font_size=12)
        button2.bind(on_press=self.button_click_callback)
        layout.add_widget(button)
        layout.add_widget(button2)
        
        return layout


if __name__ == '__main__':
    MyApp().run()