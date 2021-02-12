import kivy
kivy.require("2.0.0")
# print(kivy.__version__)

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class NeuerLabelText(BoxLayout):
    def __init__(self, **kwargs):
        super(NeuerLabelText, self).__init__(**kwargs)
        self.orientation="vertical"

        self.button = Button(text="Klick hier", on_press=self.klickbutton)
        self.label = Label(text="Alter Text")

        self.add_widget(self.button)
        self.add_widget(self.label)

    def klickbutton(self, event):
        self.label.text = "Neuer Text"

class App(App):
    def build(self):
        return NeuerLabelText()


App().run()