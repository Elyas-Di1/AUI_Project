import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from gtts import gTTS
import os

# Function to convert and play text
def play_text():
    text = text_entry.get("1.0", tk.END).strip()
    language = language_var.get()

    if text:
        try:
            tts = gTTS(text, lang=language)
            tts.save("output.mp3")
            os.system("start output.mp3" if os.name == "nt" else "open output.mp3")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        messagebox.showwarning("Warning", "Please enter some text to play.")

def clear_text():
    text_entry.delete("1.0", tk.END)

def save_audio():
    text = text_entry.get("1.0", tk.END).strip()
    language = language_var.get()

    if text:
        file_path = filedialog.asksaveasfilename(defaultextension=".mp3", 
                                                filetypes=[("MP3 files", "*.mp3"), ("All files", "*.*")])
        if file_path:
            try:
                tts = gTTS(text, lang=language)
                tts.save(file_path)
                messagebox.showinfo("Success", f"Audio saved successfully at {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        messagebox.showwarning("Warning", "Please enter some text to save.")

def exit_app():
    root.destroy()

root = tk.Tk()
root.title("Text-to-Speech App")
root.geometry("600x400")
root.resizable(False, False)

style = ttk.Style(root)
style.theme_use("clam")  # Modern theme
style.configure("TButton", font=("Arial", 12), padding=5)
style.configure("TLabel", font=("Arial", 14))

# Title Label
title_label = ttk.Label(root, text="Text-to-Speech Application", anchor="center", background="lightblue", foreground="darkblue")
title_label.pack(pady=10, fill=tk.X)

text_entry = tk.Text(root, wrap=tk.WORD, height=10, width=50, font=("Arial", 12), background="lightyellow", foreground="darkgreen")
text_entry.pack(pady=10)

language_label = ttk.Label(root, text="Select Language:", background="lightblue")
language_label.pack(pady=5)

language_var = tk.StringVar(value="en")
language_selector = ttk.Combobox(root, textvariable=language_var, state="readonly", font=("Arial", 12))
language_selector['values'] = ["en", "fr", "es", "de", "it", "ar"]
language_selector.pack()

buttons_frame = ttk.Frame(root)
buttons_frame.pack(pady=20)

play_button = ttk.Button(buttons_frame, text="Play", command=play_text)
play_button.grid(row=0, column=0, padx=10)

save_button = ttk.Button(buttons_frame, text="Save", command=save_audio)
save_button.grid(row=0, column=1, padx=10)

clear_button = ttk.Button(buttons_frame, text="Clear", command=clear_text)
clear_button.grid(row=0, column=2, padx=10)

exit_button = ttk.Button(buttons_frame, text="Exit", command=exit_app)
exit_button.grid(row=0, column=3, padx=10)

root.mainloop()

"""
Willkommen bei der Text-to-Speech-App! Mit dieser Anwendung können Sie Text in Sprache umwandeln, speichern und abspielen. Wählen Sie einfach eine Sprache aus, geben Sie Text ein, und genießen Sie die Audioausgabe!

"""