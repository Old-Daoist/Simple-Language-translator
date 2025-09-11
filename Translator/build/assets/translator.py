import tkinter as tk

class MyApp:
    def __init__(self, master):
        self.master = master
        self.master.title("My App")
        
        # Creating frames for different sections
        self.frame1 = tk.Frame(master)
        self.frame1.pack(fill="both", expand=True)
        
        self.frame2 = tk.Frame(master)
        self.frame2.pack(fill="both", expand=True)
        
        # Adding widgets to frame1
        self.label1 = tk.Label(self.frame1, text="Welcome to My App")
        self.label1.pack(pady=10)
        
        self.button1 = tk.Button(self.frame1, text="Click Me", command=self.button_click)
        self.button1.pack(pady=5)
        
        # Adding widgets to frame2
        self.label2 = tk.Label(self.frame2, text="This is another section")
        self.label2.pack(pady=10)
        
        self.entry1 = tk.Entry(self.frame2)
        self.entry1.pack(pady=5)
    
    def button_click(self):
        print("Button clicked!")

root = tk.Tk()
app = MyApp(root)
root.mainloop()
