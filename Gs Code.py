from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk , Image 
import os

root = Tk()
root.title("Gs Code's")
root.minsize(650,650)
root.maxsize(650,650)
root.configure(bg = "grey75")

open_image = ImageTk.PhotoImage(Image.open("open.png"))

save_image = ImageTk.PhotoImage(Image.open("save.png"))

exit_image = ImageTk.PhotoImage(Image.open("play.png"))



file_name_label = Label(root , text = "File Name" , bg = "grey75")
file_name_label.place(relx = 0.35 , rely = 0.03 , anchor=  CENTER)

enput_name = Entry(root)
enput_name.place(relx = 0.50 , rely = 0.03 , anchor=  CENTER)

myText = Text(root , width = 80 , height = 35)
myText.place(relx = 0.5 , rely = 0.55 , anchor = CENTER)


name  = "" 
def open_file():
    global name
    myText.delete(1.0 , END)
    enput_name.delete(0 , END)
    text_file = filedialog.askopenfilename(title=" Open HTML File",filetypes=(("HTML File","*.html"),))
    print(text_file)    
    
    name = os.path.basename(text_file)
    formate_name = name.split('.')[0]
    
    print(formate_name)
    enput_name.insert(END, formate_name)
    root.title(formate_name)
    
    text_file = open(name , 'r')
    paragraph = text_file.read()
    
    myText.insert(END , paragraph)
    text_file.close()    
  
    
    

open_btn = Button(root, image = open_image , text = "Open File" , command = open_file )
open_btn.place(relx = 0.05 , rely = 0.03 , anchor=  CENTER)

save_btn = Button(root, image = save_image , text = "Save File")
save_btn.place(relx = 0.10, rely = 0.03 , anchor=  CENTER)

exit_btn = Button(root, image = exit_image , text = "Play File")
exit_btn.place(relx = 0.15 , rely = 0.03 , anchor=  CENTER)
root.mainloop()