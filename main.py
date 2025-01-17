from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

# set window size
Window.size = (300, 450)
# load the string for design
Builder.load_string("""
<CalLayout>
    BoxLayout:
        orientation: "vertical"
        size: root.width, root.height
        TextInput:
            id:input
            text:"0"
            halign:"right"
            font_size:60
            size_hint:(1, .20)
        GridLayout:
            cols:4
            rows:5
            # first row
            Button:
                size_hint:(.2, .2)
                font_size:32
                text:"C"
                on_press:root.clear()
            Button:
                size_hint:(.2, .2)
                font_size:27
                text:"TNGA"
                on_press:root.new()
            
            Button:
                size_hint:(.2, .2)
                font_size:27
                text:"ZR"
                on_press:root.new_zr()                
            Button:
                size_hint:(.2, .2)
                font_size:32
                text:"/"
                on_press:root.pressed('/')
            # second row
            Button:
                size_hint:(.2, .2)
                font_size:32
                text:"7"
                background_color:(157/255,157/255, 157/255, 1)
                on_press:root.pressed(7)
            Button:
                size_hint:(.2, .2)
                font_size:32
                text:"8"
                background_color:(157/255,157/255, 157/255, 1)
                on_press:root.pressed(8)
            Button:
                size_hint:(.2, .2)
                font_size:32
                text:"9"
                background_color:(157/255,157/255, 157/255, 1)
                on_press:root.pressed(9)
            Button:
                size_hint:(.2, .2)
                font_size:32
                text:"-"
                on_press:root.pressed('-')
            # third row
            Button:
                size_hint:(.2, .2)
                font_size:32
                text:"4"
                background_color:(157/255,157/255, 157/255, 1)
                on_press:root.pressed(4)
            Button:
                size_hint:(.2, .2)
                font_size:32
                text:"5"
                background_color:(157/255,157/255, 157/255, 1)
                on_press:root.pressed(5)
            Button:
                size_hint:(.2, .2)
                font_size:32
                text:"6"
                background_color:(157/255,157/255, 157/255, 1)
                on_press:root.pressed(6)
            Button:
                size_hint:(.2, .2)
                font_size:32
                text:"+"
                on_press:root.pressed('+')
            # fourth row
            Button:
                size_hint:(.2, .2)
                font_size:32
                text:"1"
                background_color:(157/255,157/255, 157/255, 1)
                on_press:root.pressed(1)
            Button:
                size_hint:(.2, .2)
                font_size:32
                text:"2"
                background_color:(157/255,157/255, 157/255, 1)
                on_press:root.pressed(2)
            Button:
                size_hint:(.2, .2)
                font_size:32
                text:"3"
                background_color:(157/255,157/255, 157/255, 1)
                on_press:root.pressed(3)
            Button:
                size_hint:(.2, .2)
                font_size:32
                text:"="
                on_press:root.answer()
            # fifth row
            
            Button:
                size_hint:(.2, .2)
                font_size:32
                text:"0"
                background_color:(157/255,157/255, 157/255, 1)
                on_press:root.pressed(0)
            
            
""")


# Create a class for calculator layout
class CalLayout(Widget):

    def new(self):
        expression = self.ids.input.text
        expression = int(expression)
        expression = expression * 14
        while expression % 4 != 0:
            expression += 1
        self.ids.input.text = str(expression)

    def new_zr(self):
        expression = self.ids.input.text
        expression = int(expression)
        expression = expression * 16
        if expression % 4 == "0":
            self.ids.input.text = str(expression)
        else:
            self.ids.input.text = str(expression + 2)
    # function to clear text field
    def clear(self):
        self.ids.input.text = ""

    # function to delete last number
    # from text field
    def back(self):
        expression = self.ids.input.text
        expression = expression[:-1]
        self.ids.input.text = expression

    # function take button inuputs pressed
    # by user
    def pressed(self, button):
        # expression to store all text field values
        expression = self.ids.input.text
        # if text field expression contains
        # error then set it to empty field
        if "Error" in expression:
            expression = ""
        # if text filed expression contains
        # 0 then first set the field to empty and
        # display the button text pressed by user
        if expression == "0":
            self.ids.input.text = ""
            self.ids.input.text = f"{button}"
        else:
            self.ids.input.text = f"{expression}{button}"

    def answer(self):
        expression = self.ids.input.text
        try:
            # evaluate text field expression
            # using eval() function
            self.ids.input.text = str(eval(expression))

        except:
            # set text field to Error if
            # try block throws an error
            self.ids.input.text = "Error"
        # class to create calculator app


class CalculatorApp(App):
    # function to build app layout
    def build(self):
        return CalLayout()


# create an object of class
cal = CalculatorApp()
# run the app using object
cal.run()
