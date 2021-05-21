from time import strftime
 
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.utils import get_color_from_hex
 
# 윈도우 설정
Window.size = (400, 300)
Window.clearcolor = get_color_from_hex('#3385ff')
 
class ClockApp(App):
    def update_clock(self, nap):
        self.root.ids.time.text = strftime('   Clock\n[b]%H[/b]:%M:%S')
 
    def on_start(self):
        Clock.schedule_interval(self.update_clock, 1)
 
if __name__ == '__main__':
    ClockApp().run()
 
LabelBase.register(name='Roboto',
                   fn_regular='./font/Roboto-Thin.ttf',
                   fn_bold='./font/Roboto-Medium.ttf')
