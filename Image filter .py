import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image


class GUI:
    def __init__(insta, root):#__init__ gets called automatically when you create an instance of a class. Its purpose is to initialize the object and set up its initial state.
        insta.root = root
        insta.root.title("Image Filter GUI")

        # Menu bar
        menu_bar = tk.Menu(insta.root)
        file_menu = tk.Menu(menu_bar)
        file_menu.add_command(label="Open Image", command=insta.open_image)
        file_menu.add_command(label="Exit", command=insta.root.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)
        insta.root.config(menu=menu_bar)

        # Image display area
        insta.image_label = tk.Label(insta.root)
        insta.image_label.pack()

        # Filter selection options
        filter_frame = tk.Frame(insta.root)
        filter_frame.pack(pady=10)

        insta.filter_var = tk.StringVar()
        insta.filter_var.set("Original")

        filter_options = ["Original", "Brightness", "Contrast", "Blur", "Edges"]
        filter_menu = tk.OptionMenu(filter_frame, insta.filter_var, *filter_options)
        filter_menu.pack(side=tk.LEFT)

        apply_button = tk.Button(filter_frame, text="Apply", command=insta.apply_filter)
        apply_button.pack(side=tk.LEFT, padx=10) 
    
    #Opening the image    
    def open_image(insta):
        file_path = filedialog.askopenfilename(initialdir="/path/to/directory/containing/images")
        print(file_path)
        if file_path:
            insta.image = cv2.imread(file_path)
            insta.display_image()

    def display_image(insta):
        img = cv2.cvtColor(insta.image, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img = img.resize((500, 500))
        insta.photo = ImageTk.PhotoImage(img)
        insta.image_label.configure(image=insta.photo)

    def img_temp(insta):
        file_path="/home/kmv/demoprjct/image.jpeg"
        if file_path:
            insta.image=cv2.imread(file_path)
            insta.display_image()

    def apply_filter(insta):
        filter_type = insta.filter_var.get()
        
        if filter_type == "Original":
            GUI.img_temp(insta)
            insta.display_image()
        
        elif filter_type == "Brightness":
            brightness = 5000
            img = cv2.cvtColor(insta.image, cv2.COLOR_BGR2HSV)
            print(img[:,:,:])
            img[:, :, 2] = np.clip(img[:, :, 2] + brightness,0, 1000)
            img = cv2.cvtColor(img, cv2.COLOR_HSV2RGB)
            insta.image = img
            insta.display_image()
            
        elif filter_type == "Contrast":
            contrast = 1.5
            img = cv2.cvtColor(insta.image, cv2.COLOR_BGR2RGB)
            img = cv2.convertScaleAbs(img, alpha=contrast, beta=0)
            insta.image = img
            insta.display_image()
        
        elif filter_type == "Blur":
            blur_amount = (15, 15)
            img = cv2.GaussianBlur(insta.image, blur_amount,0)
            insta.image = img
            insta.display_image()
        
        elif filter_type == "Edges":
            img = cv2.cvtColor(insta.image, cv2.COLOR_BGR2GRAY)
            img = cv2.Canny(img, 100, 200)
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
            insta.image = img
            insta.display_image()

if __name__ == '__main__':
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()