from tkinter import*
from tkinter import messagebox
from tkinter import filedialog
from tkinter import scrolledtext
root=Tk()
root.title('NotePad')
root.geometry("500x400+400+200")
textpad=scrolledtext.ScrolledText(root,width=800,height=580)
def work():
    print("Still I am working on it , just hang on")
def open_command():
    file=filedialog.askopenfile(parent=root,mode='rb',title='select a file')
    if file!=None:
        contents=file.read()
        textpad.insert('1.0',contents)
        file.close()
def save_command():
    file=filedialog.asksaveasfile(mode='w')
    if file!=None:
        data=textpad.get('1.0',END+'-1c')
        file.write(data)
        file.close()
def saveas_command():
    file=filedialog.asksaveasfile(mode='w')
    if file!=None:
        contents=file.writelines()
        textpad.insert('1.0',contents)
        file.close()


def exit_command():
    if messagebox.askokcancel("Quit","do you really want to quit?"):
        root.destroy()
def about_command():
    label=messagebox.showinfo("about","this text Editor is created for my gui")
    menu=Menu(root)
    root.config(menu=menu)
menu1=Menu(root)
root.config(menu=menu1)
Submenu=Menu(menu1)
Editmenu=Menu(menu1)
Formatmenu=Menu(menu1)
Viewmenu=Menu(menu1)
Helpmenu=Menu(menu1)
menu1.add_cascade(label="File", menu=Submenu)
menu1.add_cascade(label="Edit",menu=Editmenu)
menu1.add_cascade(label="Format",menu=Formatmenu)
menu1.add_cascade(label="View",menu=Viewmenu)
menu1.add_cascade(label="Help",menu=Helpmenu)
Submenu.add_command(label="new",command="work")
Submenu.add_command(label="open...",command=open_command)
Submenu.add_command(label="save",command=save_command)
Submenu.add_command(label="save as",command=saveas_command)
Submenu.add_command(label="page setup....",command=work)
Submenu.add_separator()
Submenu.add_command(label="print...",command=work)
Submenu.add_command(label="Exit",command=exit_command)
Editmenu.add_command(label="Undo")
Editmenu.add_command(label="Cut",command="work")
Editmenu.add_command(label="Copy",command="work")
Editmenu.add_command(label="paste",command="work")
Editmenu.add_command(label="Delete",command=quit)
Editmenu.add_command(label="Find",command="work")
Editmenu.add_command(label="Replace",command="work")
Formatmenu.add_command(label="Word Wrap",command="work")
Formatmenu.add_command(label="Font...",command="work")
Viewmenu.add_command(label="Status Bar",command="work")
Helpmenu.add_command(label="View Help",command="work")
Helpmenu.add_command(label="About Notepad",command=about_command)
textpad.pack()
root.mainloop()
