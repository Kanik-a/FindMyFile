from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import sys
sys.path.append(r'C:/Users/kanik/OneDrive/Desktop/FindMyFile/backend/core')

from file_indexer import process_text
class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 1
        
        self.add_widget(Label(text='Which file would you like to access?'))
        
        self.query = TextInput(multiline=False)
        self.add_widget(self.query)
        
        btn = Button(text="Submit")
        btn.bind(on_press=self.print_text)
        self.add_widget(btn)

    def print_text(self, instance):
        input_text = self.query.text
        print("You entered:", input_text)
        processed = process_text(input_text)
        print("Processed text:", processed)



class MyApp(App):

    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()
