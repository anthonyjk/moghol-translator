import tkinter as tk

root = tk.Tk()
root.geometry("145x145")
root.wm_title("Dictonary Search")
search = tk.StringVar()

def dict_search():
    global search
    word = search.get()
    with open("dictonary.txt") as f:
        moheng = f.read().splitlines()
    for mh in moheng:
        line = mh.split(" : ")
        if line[1] == word.lower():
            display(line[0])
            return
    display("No translation found.")

def display(word):
    translation_label.config(text = word)
    
    
srh_entry = tk.Entry(root,textvariable = search, font=('calibre',10))
srh_btn=tk.Button(root, text="Search", command = dict_search)
translation_label = tk.Label(root, text="")

srh_entry.grid(row=0,column=0)
srh_btn.grid(row=1,column=0)
translation_label.grid(row=2,column=0)

root.mainloop()
