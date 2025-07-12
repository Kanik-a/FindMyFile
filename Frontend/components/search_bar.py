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
        super().__init__(**kwargs)
        self.cols = 1

        self.search_path = "C:/Users/kanik/OneDrive/Desktop"
        self.build_ui()

    def build_ui(self):
        self.clear_widgets()

        # Folder buttons
        btn_desktop = Button(text="Desktop")
        btn_desktop.bind(on_press=lambda x: self.set_path("C:/Users/kanik/OneDrive/Desktop"))
        self.add_widget(btn_desktop)

        btn_documents = Button(text="Documents")
        btn_documents.bind(on_press=lambda x: self.set_path("C:/Users/kanik/OneDrive/Documents"))
        self.add_widget(btn_documents)

        btn_downloads = Button(text="Downloads")
        btn_downloads.bind(on_press=lambda x: self.set_path("C:/Users/kanik/Downloads"))
        self.add_widget(btn_downloads)

        self.add_widget(Label(text=f"Current Folder: {self.search_path}"))

        self.add_widget(Label(text="Enter filename to search:"))
        self.query = TextInput(multiline=False)
        self.add_widget(self.query)

        submit_btn = Button(text="Search")
        submit_btn.bind(on_press=self.on_submit)
        self.add_widget(submit_btn)

    def set_path(self, path):
        self.search_path = path
        print(f"Search folder set to: {path}")
        self.build_ui()  # rebuild UI with new folder

    def on_submit(self, instance):
        query = self.query.text.strip()
        if not query:
            return

        results = process_text(query, self.search_path)  # returns list of dicts

        self.clear_widgets()

    # Re-add folder buttons and current folder label
        btn_desktop = Button(text="Desktop")
        btn_desktop.bind(on_press=lambda x: self.set_path("C:/Users/kanik/OneDrive/Desktop"))
        self.add_widget(btn_desktop)

        btn_documents = Button(text="Documents")
        btn_documents.bind(on_press=lambda x: self.set_path("C:/Users/kanik/OneDrive/Documents"))
        self.add_widget(btn_documents)

        btn_downloads = Button(text="Downloads")
        btn_downloads.bind(on_press=lambda x: self.set_path("C:/Users/kanik/Downloads"))
        self.add_widget(btn_downloads)

        self.add_widget(Label(text=f"Current Folder: {self.search_path}"))
        self.add_widget(Label(text=f"Top results for '{query}':"))

        for file_record in results:
            file_name = file_record["file_name"]
            parent_folder = file_record["parent_folder"]
            display_text = f"{file_name} ({parent_folder})"

            btn = Button(text=display_text, size_hint_y=None, height=40)
            btn.full_path = file_record["full_path"]  # full file path
            btn.bind(on_press=self.open_file)
            self.add_widget(btn)

    def open_file(self, instance):
        print(f"Opening: {instance.full_path}")
        os.startfile(instance.full_path)


class MyApp(App):
    def build(self):
        return LoginScreen()

if __name__ == "__main__":
    MyApp().run()