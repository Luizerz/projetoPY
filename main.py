from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class MyBoxLayout(BoxLayout):
	...

class MainApp(App):
	def build(self):
		return MyBoxLayout()

MainApp().run()
