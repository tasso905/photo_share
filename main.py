from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import requests
import wikipedia

Builder.load_file('frontend.kv')

class FirstScreen(Screen):
    def search_image(self):
        #get user query from the text box (TextInput)
        query = self.manager.current_screen.ids.user_query.text
        #get wikipedia page and the first image from list
        page = wikipedia.page(query)
        image_link = page.images[0]
        #download the image using requests
        req = requests.get(image_link)
        #write image to file
        imagepath = 'files/image.jpg'
        with open(imagepath, 'wb') as file:
            file.write(imagepath)
        #set image in the kivy Image widget
        self.manager.current_screen.ids.img.source = imagepath

class RootWidget(ScreenManager):
    pass

class MainApp(App):

    def build(self):
        return RootWidget()
    
MainApp().run()

