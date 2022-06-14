import imp
from tkinter import Button
from turtle import onclick, onkeypress
from typing import Text
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput


class Rental(App):
    def build(self):
        self.window =GridLayout()
        self.window.cols =1
         
        self.window.add_widget(Image(source="newlogo.png"))

        self.welcome = Label(text="Welcome to SD Bike Rentals.")
        self.window.add_widget(self.welcome)

        self.button = Button(text="Continue")
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)
        return self.window   
    
    def callback(self,instance):
        self.welcome.text = "Lets go !!"


    
        

if __name__=="__main__":
    Rental().run()