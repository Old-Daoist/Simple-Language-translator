import tkinter as tk
from tkinter import Text, Button, OptionMenu, StringVar, messagebox, PhotoImage
from pathlib import Path
import mysql.connector

# Constants
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Projects\HUANMIKO\Translator\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Connect to MySQL database
def connect_to_mysql():
    try:
        connection = mysql.connector.connect(
            host="your_host",
            user="your_username",
            password="your_password",
            database="your_database"
        )
        return connection
    except mysql.connector.Error as error:
        print("Error connecting to MySQL database:", error)
        return None

# Insert translation data into MySQL table
def insert_translations(connection, translations):
    try:
        cursor = connection.cursor()
        insert_query = "INSERT INTO translations (source_text, source_language, target_language, translated_text) VALUES (%s, %s, %s, %s)"
        cursor.executemany(insert_query, translations)
        connection.commit()
        cursor.close()
        print("Translations inserted successfully.")
    except mysql.connector.Error as error:
        print("Error inserting translations into MySQL:", error)

# Translation functions
def translate_text():
    src_lang = selected_language_1.get()
    tgt_lang = selected_language_2.get()
    input_text = entry_1.get("1.0", "end-1c")
    
    if src_lang == "Select Language" or tgt_lang == "Select Language":
        messagebox.showinfo("Error", "Please select source and target languages.")
        return
    
    if not input_text:
        messagebox.showinfo("Error", "Please enter text to translate.")
        return
    
    # Query translations from MySQL database
    translations = query_translations(connection, input_text.lower(), tgt_lang)
    if translations:
        entry_2.delete("1.0", "end")
        entry_2.insert("1.0", translations)
    else:
        messagebox.showinfo("Error", "Translation not available. Please try again.")
        entry_2.delete("1.0", "end")

# Query translations from MySQL table
def query_translations(connection, source_text, target_language):
    try:
        cursor = connection.cursor()
        query = "SELECT translated_text FROM translations WHERE source_text = %s AND target_language = %s"
        cursor.execute(query, (source_text, target_language))
        translations = cursor.fetchone()
        cursor.close()
        return translations[0] if translations else None
    except mysql.connector.Error as error:
        print("Error querying translations from MySQL:", error)
        return None

def clear_text():
    entry_1.delete("1.0", "end")
    entry_2.delete("1.0", "end")

# GUI Setup
window = tk.Tk()
window.geometry("700x500")
window.configure(bg="#D9D9D9")
window.resizable(False, False)

canvas = tk.Canvas(
    window,
    bg="#D9D9D9",
    height=500,
    width=700,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

# Load images
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))

# Create GUI elements
canvas.create_image(348.0, 65.0, image=image_image_1)
canvas.create_image(85, 50, image=image_image_2)
canvas.create_text(198.0, 44.0, anchor="nw", text="Language Translator", fill="#000000", font=("Inter Bold", 32))
entry_bg_1 = canvas.create_image(155.0, 248.5, image=entry_image_1)
entry_1 = Text(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_1.place(x=35.0, y=151.0, width=240.0, height=193.0)
entry_bg_2 = canvas.create_image(546.0, 248.5, image=entry_image_2)
entry_2 = Text(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_2.place(x=426.0, y=151.0, width=240.0, height=193.0)
selected_language_1 = StringVar()
selected_language_1.set("Select Language")
language_options = ["English", "Lotha", "Rongmei", "Mao"]
language_dropdown_1 = OptionMenu(window, selected_language_1, *language_options)
language_dropdown_1.config(bg="#FFFFFF", fg="#000716", font=("Inter Bold", 14), anchor="nw")
language_dropdown_1.place(x=85, y=110, width=150, height=30)
selected_language_2 = StringVar()
selected_language_2.set("Select Language")
language_dropdown_2 = OptionMenu(window, selected_language_2, *language_options)
language_dropdown_2.config(bg="#FFFFFF", fg="#000716", font=("Inter Bold", 14), anchor="nw")
language_dropdown_2.place(x=485, y=110, width=150, height=30)
button_1 = Button(image=button_image_1, borderwidth=0, highlightthickness=0, command=translate_text, relief="flat")
button_1.place(x=240.0, y=354.0, width=225.0, height=76.0)
button_2 = Button(image=button_image_2, borderwidth=0, highlightthickness=0, command=clear_text, relief="flat")
button_2.place(x=303.0, y=194.0, width=91.0, height=91.0)
canvas.create_text(580.0, 454.0, anchor="nw", text="huan_miko", fill="#000000", font=("Inter Bold", 16))
canvas.create_image(676.0, 464.0, image=image_image_3)

# Connect to MySQL database
connection = connect_to_mysql()

window.mainloop()
