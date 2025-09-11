from tkinter import Tk, Text, Button, OptionMenu, StringVar, messagebox
from dataset import dataset

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

    translated_text = ""
    for data in dataset:
        if input_text.lower() == data[0].lower() and src_lang.lower() == data[1].lower() and tgt_lang.lower() == data[2].lower():
            translated_text = data[3]
            break

    if translated_text:
        entry_2.delete("1.0", "end")
        entry_2.insert("1.0", translated_text)
    else:
        messagebox.showinfo("Error", "Translation not available. Database not yet updated.")
        entry_2.delete("1.0", "end")

def clear_text(entry_1, entry_2):
    entry_1.delete("1.0", "end")
    entry_2.delete("1.0", "end")

def create_gui():
    window = Tk()
    window.geometry("700x500")
    window.configure(bg="#D9D9D9")

    selected_language_1 = StringVar()
    selected_language_1.set("Select Language")
    selected_language_2 = StringVar()
    selected_language_2.set("Select Language")

    language_options = ["English", "Lotha", "Rongmei", "Mao"]
    language_dropdown_1 = OptionMenu(window, selected_language_1, *language_options)
    language_dropdown_1.config(bg="#FFFFFF", fg="#000716", font=("Inter Bold", 14 * -1), anchor="nw")
    language_dropdown_1.place(x=85, y=110, width=150, height=30)

    language_dropdown_2 = OptionMenu(window, selected_language_2, *language_options)
    language_dropdown_2.config(bg="#FFFFFF", fg="#000716", font=("Inter Bold", 14 * -1), anchor="nw")
    language_dropdown_2.place(x=485, y=110, width=150, height=30)

    entry_1 = Text(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
    entry_1.place(x=35.0, y=151.0, width=240.0, height=193.0)

    entry_2 = Text(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
    entry_2.place(x=426.0, y=151.0, width=240.0, height=193.0)

    button_1 = Button(window, text="Translate", command=lambda: translate_text(selected_language_1, selected_language_2, entry_1, entry_2))
    button_1.place(x=240.0, y=354.0, width=225.0, height=76.0)

    button_2 = Button(window, text="Clear", command=lambda: clear_text(entry_1, entry_2))
    button_2.place(x=303.0, y=194.0, width=91.0, height=91.0)

    window.mainloop()




