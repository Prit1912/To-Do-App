from tkinter import *
import backend

def get_selected_row(event):
    global selected_row
    index = list.curselection()[0]
    selected_row = list.get(index)
    e1.delete(0,END)
    e1.insert(END, selected_row[1])
    e2.delete(0,END)
    e2.insert(END, selected_row[2])
    e3.delete(0, END)
    e3.insert(END, selected_row[3])
    e4.delete(0, END)
    e4.insert(END, selected_row[4])

def delete_command():
    global selected_row
    backend.delete(selected_row[0])

def view_command():
    list.delete(0,END)
    for row in backend.view():
        list.insert(END, row)

def search_command():
    list.delete(0, END)
    for row in backend.search(date_text.get(),work1_text.get(), work2_text.get(),work3_text.get()):
        list.insert(END, row)

def add_command():
    backend.insert(date_text.get(),work1_text.get(), work2_text.get(),work3_text.get())
    list.delete(0,END)
    list.insert(END, (date_text.get(),work1_text.get(), work2_text.get(),work3_text.get()))

root = Tk()
root.geometry('500x500')
root.wm_title('To Do App')
root.config(bg = 'black')
l1 = Label(root, text = 'Due Date: ', font = ('Arial', 15, 'bold'), bg = 'black', fg = 'white')
l1.grid(row = 0, column = 0)

l2 = Label(root, text = 'Work 1 : ', font = ('Arial', 15, 'bold'),  bg = 'black', fg = 'white')
l2.grid(row = 1, column = 0)

l3 = Label(root, text = 'Work 2 : ', font = ('Arial', 15, 'bold'), bg = 'black', fg = 'white')
l3.grid(row = 2, column = 0)

l4 = Label(root, text = 'Work 3 : ', font = ('Arial', 15, 'bold'), bg = 'black', fg = 'white')
l4.grid(row = 3, column = 0)

date_text = StringVar()
e1 = Entry(root, bd = 5, bg = 'white', font = ('arial', 15, 'bold'), textvariable = date_text)
e1.grid(row = 0, column = 1, pady = 5)

work1_text = StringVar()
e2 = Entry(root, bd = 5, bg = 'white', font = ('arial', 10, 'bold'), textvariable = work1_text, width = 50)
e2.grid(row = 1, column = 1, pady = 5)

work2_text = StringVar()
e3 = Entry(root, bd = 5, bg = 'white', font = ('arial', 10, 'bold'), textvariable = work2_text, width = 50)
e3.grid(row = 2, column = 1, pady = 5)

work3_text = StringVar()
e4 = Entry(root, bd = 5, bg = 'white', font = ('arial', 10, 'bold'), textvariable = work3_text, width = 50)
e4.grid(row = 3, column = 1, pady = 5)

list = Listbox(root, height = 9, width = 59, font = ('arial', 10, 'bold'))
list.grid(row = 4, column = 0, columnspan = 2, rowspan = 9, pady = 30, padx = 40)

list.bind('<<ListboxSelect>>', get_selected_row)

add_btn = Button(root, text = 'Add', width = 8, font = ('arial', 10, 'bold'), command = add_command)
add_btn.place(x = 130, y = 400)

refresh_btn = Button(root, text = 'Refresh', width = 8 ,font = ('arial', 10, 'bold'), command = view_command)
refresh_btn.place(x = 210, y = 400)

delete_btn = Button(root, text = 'Delete', width = 8 ,font = ('arial', 10, 'bold'), command = delete_command)
delete_btn.place(x = 290, y = 400)

search_btn = Button(root, text = 'Search', width = 8 ,font = ('arial', 10, 'bold'), command = search_command)
search_btn.place(x = 130, y = 450)

view_btn = Button(root, text = 'View All', width = 8, font = ('arial', 10, 'bold'), command = view_command)
view_btn.place(x = 210, y = 450)

close_btn = Button(root, text = 'Close', width = 8, font = ('arial', 10, 'bold'), command = root.destroy)
close_btn.place(x = 290, y = 450)

root.mainloop()