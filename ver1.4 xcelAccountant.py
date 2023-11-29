import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import openai

openai.api_key = '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'

messages = [
    {"role": "system", "content": "You are a helpful AI assistant working at Mangal Analytics and Research Consulting."},
]

def send_message():
    message = user_input.get()
    if message:
        messages.append({"role": "user", "content": message})
        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        chat_history.config(state=tk.NORMAL)
        chat_history.insert(tk.END, f"You: {message}\n")
        chat_history.insert(tk.END, f"Marc.GPT: {reply}\n")
        chat_history.config(state=tk.DISABLED)
        user_input.delete(0, tk.END)

# Read the Excel file
file_path = r'C:\Users\HP\OneDrive\Desktop\TBBB.xlsx'
sheet_name = 'Sheet3'
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Iterate through the rows and classify subheaders
for index, row in df.iterrows():
    main_header = row['Main Header']
    sub_header = row['Sub Header']
    classification = classify_subheaders([main_header], [sub_header])
    print(f"Main Header: {main_header} | Sub Header: {sub_header} | Classification: {classification}")

# Create the GUI window
window = tk.Tk()
window.title("marc.ai")
window.geometry("500x400")  # Adjust the window size

# Define the color palette
primary_color = "#2D2D2D"
secondary_color = "#FFFFFF"
accent_color = "#00A67E"

# Set the background color
window.configure(bg=primary_color)

# Load the ChatGPT logo image
logo_image = ImageTk.PhotoImage(Image.open("marc.png"))

# Create a label for the logo
logo_label = tk.Label(window, image=logo_image, bg=primary_color)
logo_label.pack(pady=10)

# Create a styled frame for the chat history
chat_frame = ttk.Frame(window, style="Chat.TFrame")
chat_frame.pack(pady=10)

# Create a text widget to display the chat history
chat_history = tk.Text(chat_frame, width=95, height=15, bg=secondary_color, fg=primary_color, relief=tk.FLAT,
                       font=("Arial", 12))
chat_history.config(state=tk.DISABLED)
chat_history.pack(side=tk.LEFT, fill=tk.BOTH, padx=5, pady=5)

# Create a scrollbar for the chat history
scrollbar = tk.Scrollbar(chat_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
scrollbar.config(command=chat_history.yview)
chat_history.config(yscrollcommand=scrollbar.set)

# Create a styled frame for the user input
input_frame = ttk.Frame(window, style="Input.TFrame")
input_frame.pack(pady=10)

# Create an entry widget for user input
user_input = tk.Entry(input_frame, width=40, bg=secondary_color, relief=tk.FLAT, font=("Arial", 12))
user_input.pack(side=tk.LEFT, padx=5)

# Create a button to send the user's message
send_button = tk.Button(input_frame, text="Send", command=send_message, relief=tk.FLAT, bg=accent_color,
                        fg=secondary_color, font=("Arial", 12))
send_button.pack(side=tk.RIGHT, padx=5)

# Configure styles for the frames
window.style = ttk.Style()
window.style.configure("Chat.TFrame", background=primary_color)
window.style.configure("Input.TFrame", background=primary_color)

# Add a separator for visual separation
separator = ttk.Separator(window, orient="horizontal")
separator.pack(fill="x", padx=10, pady=10)

# Start the GUI event loop
window.mainloop()
