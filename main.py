# This is a sample Python scrip
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import pathlib
import tkinter
from tkinter.messagebox import showinfo

from rembg import remove
from tkinter import filedialog as fd
import customtkinter
from PIL import Image, ImageTk


def erase_bg():
    if len(textbox_file.get("0.0", "end-1c")) == 0 or len(textbox_path.get("0.0", "end-1c")) == 0:
        showinfo(title="Fail", message="Choose Image and Folder!")
        print('Empty')
    else:
        input_file = pathlib.Path(textbox_file.get("1.0", 'end-1c'))
        input_folder = pathlib.Path(textbox_path.get("1.0", 'end-1c'))
        file_name = input_file.stem
        output_file = f'{input_folder}/{file_name}_MagicPNG.png'
        print(output_file)
        input_img = Image.open(input_file)
        output_img = remove(input_img)
        output_img.save(output_file)
        showinfo(title="", message="Done")

def select_file():
    filetypes = (
        ('JPG', '*.jpg'),
        ('PNG', '*.png')
    )
    name = fd.askopenfilename(filetypes=filetypes)
    textbox_file.configure(state='normal')
    textbox_file.insert("0.0", name)
    textbox_file.configure(state='disable')


def select_path():
    selected_user_path = fd.askdirectory()
    textbox_path.configure(state='normal')
    textbox_path.insert("0.0", selected_user_path)
    textbox_path.configure(state='disable')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")
    window = customtkinter.CTk()
    window.geometry('800x600')
    window.title("MagicPNG")
    dir_path = pathlib.Path.cwd()
    pathBg = pathlib.Path(dir_path, 'Icons', 'bg.png')
    bg = ImageTk.PhotoImage(Image.open(pathBg))
    l1 = customtkinter.CTkLabel(master=window, image=bg)
    l1.pack()

    frame = customtkinter.CTkFrame(master=l1, width=600, height=400, corner_radius=0)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    l2 = customtkinter.CTkLabel(master=frame, text="Direction to your Image", font=('Century Gothic', 25))
    l2.place(x=200, y=45)

    pathImg = pathlib.Path(dir_path, 'Icons', 'folder.png')
    # print(pathImg)
    # img = PhotoImage(file=pathImg)
    img = customtkinter.CTkImage(Image.open(pathImg))
    openBtn_file = customtkinter.CTkButton(master=frame, text='', image=img, width=20, height=20, command=select_file)
    openBtn_file.place(x=540, y=100)

    # openBtn.grid(row=1, column=1)
    textbox_file = customtkinter.CTkTextbox(master=frame, width=500, height=20, state='disable')
    textbox_file.place(x=30, y=100)
    # textbox.grid(row=1, column=0, padx=5, pady=60)
    # openBtn.grid(row=1, column=1, pady=0)

    l3 = customtkinter.CTkLabel(master=frame, text="Direction to export Folder", font=('Century Gothic', 25))
    l3.place(x=200, y=200)

    textbox_path = customtkinter.CTkTextbox(master=frame, width=500, height=20, state='disable')
    textbox_path.place(x=30, y=250)

    openBtn_path = customtkinter.CTkButton(master=frame, text='', image=img, width=20, height=20, command=select_path)
    openBtn_path.place(x=540, y=250)

    # textbox.grid(row=1, column=0)

    eraseBtn = customtkinter.CTkButton(master=frame, text='Erase', width=150, height=50, font=('Century Gothic', 25), command=erase_bg)
    eraseBtn.place(x=250, y=320)
    # openBtn.grid()
    window.resizable(False, False)
    window.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
