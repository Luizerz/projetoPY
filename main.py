from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
#teste Mateus
class MyBoxLayout(BoxLayout):
	...

class MainApp(App):
	def build(self):
		return MyBoxLayout()

MainApp().run()
