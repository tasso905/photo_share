from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import requests
import wikipedia

Builder.load_file('frontend.kv')

headers = {
    'User-Agent': 'My User Agent 1.0'
}

class FirstScreen(Screen):
    def search_image(self):
        #get user query from the text box (TextInput)
        query = self.manager.current_screen.ids.user_query.text
        #get wikipedia page and the first image from list
        page = wikipedia.page(query, auto_suggest=False, redirect=True, preload=False)
        image_link = page.images[0]
        #download the image using requests
        req = requests.get(image_link, headers=headers)
        #write image to file
        imagepath = 'files/image.jpg'
        with open(imagepath, 'wb') as file:
            file.write(req.content)
        #set image in the kivy Image widget
        self.manager.current_screen.ids.img.source = imagepath

class RootWidget(ScreenManager):
    pass

class MainApp(App):

    def build(self):
        return RootWidget()
    
MainApp().run()

