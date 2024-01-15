# Importing TextBlob to help the chatbot understand language nuances.
from textblob import TextBlob

# Importing tkinter to create the user interface for chatting.
import tkinter as tk


# Defining the ChatBotGUI class, which sets up the chatting window.
class ChatBotGUI(tk.Tk):
    # The constructor gets called when the ChatBotGUI is created.
    def __init__(self):
        # Calling the parent's constructor (Tk's constructor).
        super().__init__()

        # Setting the title and dimensions of the chat window.
        self.title("ChatBot")
        self.geometry("400x500")

        # Creating a text area to display chat history.
        self.chat_history = tk.Text(self, state=tk.DISABLED, wrap="word")
        self.chat_history.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Creating a text area for user messages.
        self.chat_input = tk.Entry(self)  # Changed from Text to Entry
        self.chat_input.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        # Adding a "Send" button to trigger the handle_chat_input method.
        self.send_button = tk.Button(self, text="Send", command=self.handle_chat_input)
        self.send_button.pack(side=tk.BOTTOM)

        # Initializing the sentiment analysis tool.
        self.sentiment_analyzer = TextBlob("")

        # Starting the conversation with a greeting.
        self.display_chat_message("ChatBot: Hi, how can I help you?")

    # Handling user's message input when they press "Return" (Enter).
    def handle_chat_input(self):
        # Retrieving the user's message from the input area.
        user_message = self.chat_input.get().strip()
        self.chat_input.delete(0, tk.END)

        # Adding the user's message to the chat history.
        self.display_chat_message("You: " + user_message)

        # Analyzing the sentiment of the user's message.
        self.sentiment_analyzer = TextBlob(user_message)
        sentiment_score = self.sentiment_analyzer.sentiment.polarity

        # Generating the chatbot's response based on sentiment.
        if sentiment_score > 0:
            chatbot_message = f"ChatBot: That's great to hear! Is there anything I could help with? \n Sentiment score: {sentiment_score}\n"
        elif sentiment_score < 0:
            chatbot_message = f"ChatBot: I'm sorry to hear that. May I transfer you to a live agent? \n Sentiment score: {sentiment_score}\n"
        else:
            chatbot_message = f"ChatBot: Hmm, I see. Can you please provide additional details? \n Sentiment score: {sentiment_score}\n"

        # Adding the chatbot's response to the chat history.
        self.display_chat_message(chatbot_message)

    # Displaying messages in the chat history area.
    def display_chat_message(self, message):
        # Enabling the text area for writing.
        self.chat_history.configure(state=tk.NORMAL)
        # Adding the message to the text area.
        self.chat_history.insert(tk.END, message + "\n")
        # Locking the text area to prevent accidental edits.
        self.chat_history.configure(state=tk.DISABLED)
        # Scrolling to show the latest message.
        self.chat_history.see(tk.END)


# Checking if the program is being run directly.
if __name__ == "__main__":
    # Creating the chatbot window and starting the chat loop.
    app = ChatBotGUI()
    app.mainloop()
