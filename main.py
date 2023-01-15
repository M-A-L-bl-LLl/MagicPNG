# This is a sample Python scrip
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from tkinter import *
from tkinter import filedialog as fd


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def callback():
    name = fd.askopenfilename()
    print(name)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    window = Tk()
    window.geometry('600x400')
    window.title("MagicPNG")
    openBtn = Button(window, text='Click to Open File', command=callback).pack(pady=10)
    #openBtn.grid()
    window.resizable(False, False)
    window.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
