# Importing TextBlob to help the chatbot understand language nuances.
from textblob import TextBlob

# Importing tkinter to create the user interface for chatting.
import tkinter as tk

# Defining the ChatBotGUI class, which sets up the chatting window.
class ChatBotGUI(tk.Tk):
    def __init__(self):
        # Calling the parent's constructor (Tk's constructor).
        super().__init__()

        # Setting the title and dimensions of the chat window.
        self.title("ChatBot")
        self.geometry("400x500")

        # Creating a text area to display chat history.
        self.chat_history = tk.Text(self, state=tk.DISABLED, wrap="word")
        self.chat_history.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Demonstrating GUI creation
app = ChatBotGUI()
app.mainloop()