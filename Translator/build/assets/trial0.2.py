from tkinter import Tk, Text, Button, OptionMenu, StringVar, messagebox, PhotoImage,Canvas
from pathlib import Path

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Projects\HUANMIKO\Translator\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Define the translation dataset
translation_data = {
    'good morning': {'Lotha': 'enya mongkhum', 'Rongmei': 'lathoung gaidai'},
    'good evening': {'Lotha': 'mmyu mongkhum', 'Rongmei': 'tingjin gaidai'},
    'bad': {'Lotha': 'unmhon', 'Rongmei': 'shi ae'},
    # Add more translations here
}

def translate_text():
    # Get the selected languages
    src_lang = selected_language_1.get()
    tgt_lang = selected_language_2.get()
    
    # Get the input text
    input_text = entry_1.get("1.0", "end-1c")
    
    # Check if source and target languages are selected
    if src_lang == "Select Language" or tgt_lang == "Select Language":
        messagebox.showinfo("Error", "Please select source and target languages.")
        return
    
    # Check if input text is provided
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

def clear_text():
    entry_1.delete("1.0", "end")
    entry_2.delete("1.0", "end")

window = Tk()
window.geometry("700x500")
window.configure(bg="#D9D9D9")

canvas = Canvas(
    window,
    bg="#D9D9D9",
    height=500,
    width=700,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(348.0, 65.0, image=image_image_1)
image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(85,50, image=image_image_2)

canvas.create_text(198.0, 44.0, anchor="nw", text="Language Translator", fill="#000000", font=("Inter Bold", 32 * -1))

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(155.0, 248.5, image=entry_image_1)
entry_1 = Text(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_1.place(x=35.0, y=151.0, width=240.0, height=193.0)

entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(546.0, 248.5, image=entry_image_2)
entry_2 = Text(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_2.place(x=426.0, y=151.0, width=240.0, height=193.0)

selected_language_1 = StringVar()
selected_language_1.set("Select Language")
language_options = ["English", "Lotha", "Rongmei", "Mao"]
language_dropdown_1 = OptionMenu(window, selected_language_1, *language_options)
language_dropdown_1.config(bg="#FFFFFF", fg="#000716", font=("Inter Bold", 14 * -1), anchor="nw")
language_dropdown_1.place(x=85, y=110, width=150, height=30)

selected_language_2 = StringVar()
selected_language_2.set("Select Language")
language_dropdown_2 = OptionMenu(window, selected_language_2, *language_options)
language_dropdown_2.config(bg="#FFFFFF", fg="#000716", font=("Inter Bold", 14 * -1), anchor="nw")
language_dropdown_2.place(x=485, y=110, width=150, height=30)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(image=button_image_1, borderwidth=0, highlightthickness=0, command=translate_text, relief="flat")
button_1.place(x=240.0, y=354.0, width=225.0, height=76.0)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(image=button_image_2, borderwidth=0, highlightthickness=0, command=clear_text, relief="flat")
button_2.place(x=303.0, y=194.0, width=91.0, height=91.0)

canvas.create_text(580.0, 454.0, anchor="nw", text="huan_miko", fill="#000000", font=("Inter Bold", 16 * -1))

image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(676.0, 464.0, image=image_image_3)

window.resizable(False, False)
window.mainloop()

