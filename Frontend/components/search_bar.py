from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

import os
import sys
sys.path.append(r'C:/Users/kanik/OneDrive/Desktop/FindMyFile/backend/core')
from file_indexer import process_text

class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 1

        self.folder_path = "C:/Users/kanik/OneDrive/Desktop/Documents and Headshots"

        self.add_widget(Label(text='Which file would you like to access?'))

        self.query = TextInput(multiline=False)
        self.add_widget(self.query)

        btn = Button(text="Submit")
        btn.bind(on_press=self.on_submit)
        self.add_widget(btn)

    def on_submit(self, instance):
        input_text = self.query.text
        print("You entered:", input_text)

        file_names, _ = process_text(input_text)

        # Remove old buttons (if re-searching)
        self.clear_widgets()
        self.cols = 1

        self.add_widget(Label(text='Top matches (click to open):'))

        for fname in file_names:
            file_btn = Button(text=fname, size_hint_y=None, height=40)
            file_btn.bind(on_press=self.open_file)
            self.add_widget(file_btn)

        # Re-add query field and submit button
        self.add_widget(Label(text='Search again:'))
        self.query = TextInput(multiline=False)
        self.add_widget(self.query)

        submit_btn = Button(text="Submit")
        submit_btn.bind(on_press=self.on_submit)
        self.add_widget(submit_btn)

    def open_file(self, instance):
        file_to_open = instance.text
        full_path = os.path.join(self.folder_path, file_to_open)
        print(f"Opening file: {full_path}")
        os.startfile(full_path)

class MyApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run()
