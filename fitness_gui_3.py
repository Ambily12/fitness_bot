import tkinter as tk
from tkinter import scrolledtext
import openai

openai.api_key = "*******************************"

class ChatbotInterface:
    def __init__(self, master):
        self.master = master
        self.master.title('Fitness Bot')
        self.master.geometry('800x600')

        self.create_widgets()

    def create_widgets(self):
        # Heading
        heading_label = tk.Label(self.master, text="Fitness Bot", font=('Helvetica', 16, 'bold'))
        heading_label.pack(pady=10)

        # Chat history
        self.chat_history = scrolledtext.ScrolledText(self.master, wrap=tk.WORD, height=30, width=150)
        self.chat_history.pack(padx=10, pady=10)

        # User entry
        self.user_entry = tk.Entry(self.master, width=40)
        self.user_entry.pack(pady=10)

        # Send button
        self.send_button = tk.Button(self.master, text='Send', command=self.send_message)
        self.send_button.pack(pady=10)

    def send_message(self):
        user_input = self.user_entry.get()
        if user_input.lower() in ['bye', 'exit', 'quit']:
            self.master.destroy()
        else:
            try:
                bot_response = self.fitness_bot(user_input)
            except Exception as e:
                bot_response = f"Error: {str(e)}"

            self.update_chat_history(f"User: {user_input}\n", 'blue')
            self.update_chat_history(f"Bot: {bot_response}\n\n", 'green')
            self.user_entry.delete(0, tk.END)

    def fitness_bot(self, user_message):
        prompt = f"I want to know more about {user_message}"

        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=150
        )
        bot_message = response['choices'][0]['text'].strip()
        return bot_message

    def update_chat_history(self, message, color):
        self.chat_history.config(state=tk.NORMAL)
        self.chat_history.insert(tk.END, message, color)
        self.chat_history.tag_configure(color, foreground=color)
        self.chat_history.tag_add(color, f"{self.chat_history.index(tk.END)}-2l", tk.END)  # Apply tag to the last inserted line
        self.chat_history.config(state=tk.DISABLED)
        self.chat_history.yview(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotInterface(root)
    root.mainloop()
