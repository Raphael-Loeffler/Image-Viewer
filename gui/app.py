import tkinter as tk
from tkinter import Frame, Label, PhotoImage, Label, Button
from PIL import Image, ImageTk
from constants import *
import os

class Gui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title(APP_TITLE)
        self.root.geometry(f"{APP_WIDTH}x{APP_HEIGHT}")
        
        self.count = 0
        
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.update_idletasks()
        
        
        self.bar_height = self.root.winfo_height()//BAR_HEIGHT_CONTROL
        self.top_bar = Frame(self.root, bg=BAR_COLOR, height=self.bar_height)
        self.top_bar.grid(row=0, column=0, sticky="ew", columnspan=3)
        self.top_bar.grid_propagate(False)
        self.clean_up_button = Button(self.top_bar, text="Clean Up", command=self.clean_up, fg=BUTTON_FG, bg=BUTTON_BG, relief="raised", activebackground=BUTTON_ACTIVEBACKGROUND, cursor="hand2")
        self.clean_up_button.place(relx=0.009, rely=0.08)
        
        
        self.image_frame = Frame(self.root, bg=IMAGE_FRAME_COLOR)
        self.image_frame.grid(row=1, column=0, sticky="nsew")
        self.image_label = Label(self.image_frame, borderwidth=0, relief="flat")
        
        self.info_frame = Frame(self.root, bg=INFO_FRAME_COLOR, width=self.root.winfo_width()//INFO_WIDTH_CONTROL)
        self.info_frame.grid(row=1, column=2, sticky="nsew")
        self.info_label = Label(self.info_frame)
        
        self.bottom_bar = Frame(self.root, bg=BAR_COLOR, height=self.bar_height)
        self.bottom_bar.grid(row=2, column=0, sticky="ew", columnspan=3)
        
        self.root.after(1000, self.check_stack)
        self.root.bind("<Configure>", self.update)
    
    def clean_up(self) -> None:
        for file in os.listdir("image_stack"):
            os.rename(f"image_stack/{file}", f"old_image_stack/{file}")
        self.count = 0
    
    def check_stack(self) -> None:
        if os.listdir("image_stack").__contains__(f"{self.count}.png"):
            try:
                print(f"{self.count}")
                img = Image.open(f"image_stack/{self.count}.png")
                img = ImageTk.PhotoImage(img)
                self.image_label.config(image=img)
                self.image_label.image = img
                self.image_label.grid(row=1, column=0, sticky="nsw")
                self.root.update()
            except Exception as e:
                print(e)
            self.count += 1
        self.root.after(250, self.check_stack)
    
    def update(self, event) -> None:
        if event.widget == self.root:
            self.info_frame.config(width=self.root.winfo_width()//INFO_WIDTH_CONTROL)
            self.bar_height = self.root.winfo_height()//BAR_HEIGHT_CONTROL
            self.top_bar.config(height=self.bar_height)
            self.bottom_bar.config(height=self.bar_height)
    
    def run(self) -> None:
        self.root.mainloop()


if __name__ == "__main__":
    gui = Gui()
    gui.run()