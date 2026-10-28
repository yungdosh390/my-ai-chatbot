from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

Window.clearcolor = (0.06, 0.08, 0.13, 1)

class ChatApp(App):
    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=15,
            spacing=10
        )

        title = Label(
            text="My AI Chatbot",
            font_size=26,
            size_hint_y=None,
            height=60
        )
        layout.add_widget(title)

        self.messages = Label(
            text="Hello! Welcome to your AI chatbot.",
            halign="left",
            valign="top"
        )
        self.messages.bind(
            size=lambda instance, value:
            setattr(instance, "text_size", value)
        )
        layout.add_widget(self.messages)

        self.input_box = TextInput(
            hint_text="Type your message...",
            multiline=False,
            size_hint_y=None,
            height=50
        )
        layout.add_widget(self.input_box)

        send_button = Button(
            text="Send",
            size_hint_y=None,
            height=50
        )
        send_button.bind(on_press=self.send_message)
        layout.add_widget(send_button)

        return layout

    def send_message(self, instance):
        message = self.input_box.text.strip()
        if message:
            self.messages.text += f"\n\nYou: {message}"
            self.messages.text += "\nAI: Chat connection coming next!"
            self.input_box.text = ""

ChatApp().run() 
