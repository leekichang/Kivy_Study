from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

# Builder.load_file('./whatever.kv')

Builder.load_string("""
<MyGridLayout>

    name : name
    pizza : pizza
    color : color

    GridLayout:
        cols : 1
        size : root.width, root.height
        GridLayout:
            cols:2

            Label:
                text : "Name"
            TextInput:
                id : name
                multiline : False 

            Label:
                text : "Pizza"
            TextInput:
                id : pizza
                multiline : False

            Label:
                text : "Color"
            TextInput:
                id : color
                multiline : False

        Button:
            text : "Submit"
            font_size : 32
            on_press: root.press()
""")

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

class AwesomeApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    AwesomeApp().run()