import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class MyGridLayout(Widget):
    name = ObjectProperty(None)
    pizza = ObjectProperty(None)
    color = ObjectProperty(None)

    def press(self):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text
        # print(f'Hello {name}, favorite pizza is {pizza} and your favorite color is {color}')
        # print it to the screen
        if name != "" and color != "" and pizza != "":
            print(f'Hello {name}, favorite pizza is {pizza} and your favorite color is {color}')
            # self.add_widget(Label(text=f'Hello {name}, favorite pizza is {pizza} and your favorite color is {color}'))
            # clear the input boxes
            self.name.text = ""
            self.color.text = ""
            self.pizza.text = ""

class KivyDesignApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    KivyDesignApp().run()