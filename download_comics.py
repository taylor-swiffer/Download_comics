# kivy libraries
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.popup import Popup
#from noconflict import classmaker

# link uix author : 
# <a href="https://www.freepik.com/free-vector/gradient-style-ui-ux-background_16923194.htm#query=ui%20ux&position=3&from_view=search&track=ais&uuid=50399363-0a06-460f-8334-af9e0698fdda">Image by pikisuperstar</a> on Freepik

"""
background_normal: "img/dark button rounded.png"
background_down: "img/dark button rounded clicked.png"
"""

"""
To Do List :
    disabilitare pulsanti quando sei nella sezione del programma attiva
    creare sezione dove selezioni capitoli da aggiungere al pdf
    integrare codice esistente nel programma (Crea un modulo separato)
"""

custom_font = "font/Montserrat-Regular.ttf"
LabelBase.register(name="Montserrat1", fn_regular=custom_font)

class DarkButton(ButtonBehavior, Image):
    #__metaclass__=classmaker()
    def convert(self):
        print("Oddioooo")

class MyMenu(Widget):
    def close_app(self):
        App.get_running_app().stop()
        Window.close()
    
    def show_popup(self):
        layout = GridLayout(cols = 1, padding = 10) 
  
        popupLabel = Label(text = "App Created By Carmine Avilio",
                           font_name="Montserrat1") 
        closeButton = Button(text = "Close",
                             background_normal="img/dark button.png",
                             background_down="img/dark button clicked.png",
                             font_name="Montserrat1") 
  
        layout.add_widget(Image(source="img\\Book Icon.png"))
        layout.add_widget(popupLabel) 
        layout.add_widget(closeButton)        
  
        # Instantiate the modal popup and display 
        popup = Popup(title ='Info about Download Comics', 
                      content = layout,
                      size_hint=(None, None),
                      size=(500, 500),
                      background = "img\\Widget 001- grey.png")
        popup.open()    
  
        # Attach close button press with popup.dismiss action 
        closeButton.bind(on_press = popup.dismiss)
    
        # Attach close button press with popup.dismiss action 
        # content.bind(on_press = popup.dismiss) 

#class InfoPopup(Widget):
#    pass
    
class DownloadComicsLayout(Widget):
    background_path = StringProperty("")
    isClosed = True
    
    def animate(self, instance):
        direction = 0
        if self.isClosed:
            direction = 300
        animation = Animation(pos=(direction, instance.pos[1]), t='out_bounce')
        animation2 = Animation(pos=(direction-300, self.ids['menu'].pos[1]), t='out_bounce')
        self.isClosed = not self.isClosed
        animation.start(instance)
        animation2.start(self.ids['menu'])

class DownloadComicsApp(App):
    def build(self):
        self.icon = "img\\Book Icon.png"
        return DownloadComicsLayout()

if __name__ == '__main__':
    DownloadComicsApp().run()