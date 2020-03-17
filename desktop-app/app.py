from tkinter import *
from db import Db

db = Db()
window = Tk("My Window")
window.geometry("500x500")

title_text = StringVar()
author_text = StringVar()
year_text = StringVar()
isbn_text = StringVar()
lb_text = StringVar()


def view_all():
    db.connect()
    listBox.delete(0, END)
    for row in db.get_books():
        listBox.insert(END, row)


def search_book():
    db.connect()
    listBox.delete(0, END)
    search_term = db.search(
        title_text.get(), author_text.get(), year_text.get(), isbn_text.get()
    )
    if type(search_term) is list:
        for row in search_term:
            listBox.insert(END, row)
    else:
        listBox.insert(END, search_term)


def add_book():
    db.connect()
    result = db.insert(
        title_text.get(), author_text.get(), year_text.get(), isbn_text.get()
    )
    listBox.insert(END, result)
    clear_entries()


def get_selected(event):
    global selected_item
    selected_item = listBox.get(listBox.curselection()[0])
    populate_entries(selected_item)


def delete_book():
    db.connect()
    db.delete(selected_item[0])
    clear_entries()
    view_all()


def update_book():
    db.connect()
    db.update(
        title_text.get(),
        author_text.get(),
        year_text.get(),
        isbn_text.get(),
        selected_item[0],
    )
    view_all()


def populate_entries(item):
    title_text.set(item[1])
    author_text.set(item[2])
    year_text.set(item[3])
    isbn_text.set(item[4])


def clear_entries():
    title_text.set("")
    author_text.set("")
    year_text.set("")
    isbn_text.set("")


title_label = Label(window, text="Title")
title_entry = Entry(window, textvariable=title_text)
author_label = Label(window, text="Author")
author_entry = Entry(window, textvariable=author_text)
year_label = Label(window, text="Year")
year_entry = Entry(window, textvariable=year_text)
isbn_label = Label(window, text="ISBN")
isbn_entry = Entry(window, textvariable=isbn_text)
listBox = Listbox(window, height=6, width=40)
sb = Scrollbar(window)
viewBtn = Button(window, text="View All", width=12, comman=view_all)
searchBtn = Button(window, text="Search", width=12, command=search_book)
addBtn = Button(window, text="Add", width=12, command=add_book)
updateBtn = Button(window, text="Update", width=12, command=update_book)
deleteBtn = Button(window, text="Delete", width=12, command=delete_book)
closeBtn = Button(window, text="Close", width=12, command=window.destroy)
title_label.grid(row=0, column=0)
title_entry.grid(row=0, column=1)
author_label.grid(row=0, column=2)
author_entry.grid(row=0, column=3)
year_label.grid(row=1, column=0)
year_entry.grid(row=1, column=1)
isbn_label.grid(row=1, column=2)
isbn_entry.grid(row=1, column=3)
listBox.grid(row=2, column=0, rowspan=6, columnspan=3)
sb.grid(row=2, column=3, rowspan=6)
listBox.configure(yscrollcommand=sb.set)
listBox.bind("<<ListboxSelect>>", get_selected)
sb.configure(command=listBox.yview)
viewBtn.grid(row=2, column=5)
searchBtn.grid(row=3, column=5)
addBtn.grid(row=4, column=5)
updateBtn.grid(row=5, column=5)
deleteBtn.grid(row=6, column=5)
closeBtn.grid(row=7, column=5)


window.mainloop()
