import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    # Initialize infinite keywords
    def __init__(self, **kwargs):
        # Call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)

        # Set columns
        self.cols = 2

        # Add widgets
        self.add_widget(Label(text="Name: "))

        # Add Input Box
        self.name = TextInput(multiline = False)
        self.add_widget(self.name)

        # Add widgets
        self.add_widget(Label(text="Favorite Pizza: "))

        # Add Input Box
        self.pizza = TextInput(multiline = False)
        self.add_widget(self.pizza)

        # Add widgets
        self.add_widget(Label(text="Favorite Color: "))

        # Add Input Box
        self.color = TextInput(multiline = False)
        self.add_widget(self.color)

        # Create a Submit Button
        self.submit = Button(text="Submit", font_size = 32)
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, instance):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text
        # print(f'Hello {name}, favorite pizza is {pizza} and your favorite color is {color}')
        # print it to the screen
        if name != "" and color != "" and pizza != "":
            self.add_widget(Label(text=f'Hello {name}, favorite pizza is {pizza} and your favorite color is {color}'))
            # clear the input boxes
            self.name.text = ""
            self.color.text = ""
            self.pizza.text = ""

class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    MyApp().run()