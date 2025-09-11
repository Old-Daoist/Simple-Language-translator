from tkinter import Tk, Text, Button, OptionMenu, StringVar, messagebox

# Define the translation dataset
translation_data = {
    'good morning': {'Lotha': 'enya mongkhum', 'Rongmei': 'lathoung gaidai'},
    'good evening': {'Lotha': 'mmyu mongkhum', 'Rongmei': 'tingjin gaidai'},
    'bad': {'Lotha': 'unmhon', 'Rongmei': 'shi ae'},
    # Add more translations here
}

def translate_text(selected_language_1, selected_language_2, entry_1, entry_2):
    src_lang = selected_language_1.get()
    tgt_lang = selected_language_2.get()
    input_text = entry_1.get("1.0", "end-1c").strip()

    if src_lang == "Select Language" or tgt_lang == "Select Language":
        messagebox.showinfo("Error", "Please select source and target languages.")
        return

    if not input_text:
        messagebox.showinfo("Error", "Please enter text to translate.")
        return

    # Get the translation based on the selected source language and input text
    translation = translation_data.get(input_text.lower(), {}).get(tgt_lang)
    if translation:
        entry_2.delete("1.0", "end")
        entry_2.insert("1.0", translation)
    else:
        messagebox.showinfo("Error", "Translation not available. Please try again.")
        entry_2.delete("1.0", "end")

def clear_text(entry_1, entry_2):
    entry_1.delete("1.0", "end")
    entry_2.delete("1.0", "end")

def create_gui():
    window = Tk()
    window.geometry("500x300")
    window.title("Custom Translator")

    selected_language_1 = StringVar(window)
    selected_language_1.set("Select Language")

    selected_language_2 = StringVar(window)
    selected_language_2.set("Select Language")

    language_options = ["English", "Lotha", "Rongmei"]
    language_dropdown_1 = OptionMenu(window, selected_language_1, *language_options)
    language_dropdown_1.place(x=50, y=50)

    language_dropdown_2 = OptionMenu(window, selected_language_2, *language_options)
    language_dropdown_2.place(x=250, y=50)

    entry_1 = Text(window, width=40, height=5)
    entry_1.place(x=50, y=100)

    entry_2 = Text(window, width=40, height=5)
    entry_2.place(x=50, y=180)

    translate_button = Button(window, text="Translate",
                              command=lambda: translate_text(selected_language_1, selected_language_2, entry_1, entry_2))
    translate_button.place(x=50, y=250)

    clear_button = Button(window, text="Clear", command=lambda: clear_text(entry_1, entry_2))
    clear_button.place(x=150, y=250)

    window.mainloop()

if __name__ == "__main__":
    create_gui()
