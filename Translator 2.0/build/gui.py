from pathlib import Path
from tkinter import Tk, Text, Button, PhotoImage, Frame, Label
from tkinter.ttk import Combobox

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Projects\HUANMIKO\Translator 2.0\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.geometry("1440x1024")
window.configure(bg="#FFFFFF")

# Configure grid layout for the main window
window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(0, weight=1)

# Create a frame for the content to use grid layout within it
frame = Frame(window, bg="#FFFFFF")
frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

# Configure grid layout for the frame
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)
frame.grid_columnconfigure(2, weight=1)
frame.grid_rowconfigure(1, weight=1)

# Title
title_label = Label(
    frame,
    text="Translator 2.0",
    bg="#FFFFFF",
    fg="#000000",
    font=("Inter bold", 60)
)
title_label.grid(row=0, column=0, columnspan=3, pady=(10, 10), sticky="nw")

# Text widget for multiline input with larger font size
text_1 = Text(
    frame,
    bd=0,
    bg="#9A8686",
    fg="#000716",
    highlightthickness=0,
    font=("Arial", 20)  # Set the desired font and size here
)
text_1.grid(row=1, column=0, columnspan=2, padx=10, pady=(10, 10), sticky="nsew")

# Combobox for language selection

languages = ["Mao", "Rongmei", "Lotha"]
combo = Combobox(frame, values=languages, font=("Arial", 20))
combo.grid(row=1, column=2, padx=10, pady=(10, 10), sticky="n")

# Buttons
button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    frame,
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.grid(row=3, column=1, pady=(20, 10), sticky="e")

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(
    frame,
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.grid(row=3, column=0, pady=(20, 5), sticky="e")

# Additional texts
max_words_label = Label(
    frame,
    text="Maximum of 200 words",
    bg="#FFFFFF",
    fg="#000000",
    font=("Gelasio Medium", 26)
)
max_words_label.grid(row=2, column=0, columnspan=3, pady=(0, 0), padx=(10, 0), sticky="w")

contact_us_label = Label(
    frame,
    text="Contact Us",
    bg="#FFFFFF",
    fg="#000000",
    font=("Roboto", 20)
)
contact_us_label.grid(row=4, column=1, pady=(20, 0), padx=(20, 0))

# Additional buttons
button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_3 = Button(
    frame,
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.grid(row=0, column=3, padx=(0, 20), pady=(10, 0), sticky="ne")

button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
button_4 = Button(
    frame,
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.grid(row=0, column=4, padx=(0, 20), pady=(10, 0), sticky="ne")

button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
button_5 = Button(
    frame,
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.grid(row=0, column=5, padx=(0, 20), pady=(10, 0), sticky="ne")

window.resizable(True, True)
window.mainloop()
