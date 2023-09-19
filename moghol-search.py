import tkinter as tk

root = tk.Tk()
root.geometry("145x145")
root.wm_title("Dictonary Search")
search = tk.StringVar()

#expanded_table = tk.Tk()

# Searches Moghol Dictonary for Word
def dict_search():
    global search
    
    #expanded_table.destroy()
    
    word = search.get()
    with open("dictonary.txt") as f:
        moheng = f.read().splitlines()
    for mh in moheng:
        line = mh.split(" : ")
        if line[1] == word.lower():
            display(line[0])
            return
    display("No translation found.")

# Table controller and translation display
def display(word):
    translation_label.config(text = word)
    declination_table(word)

class Table:

    def __init__(self,root,grmr_names,modifiers,word):
        for i in range(2):
            for j in range(len(grmr_names)):
                if i == 0:
                    self.lbl = tk.Label(root)

                    self.lbl.grid(row=j, column=i)
                    self.lbl.config(text=grmr_names[j])

                if i == 1:
                    self.wrd = tk.Label(root)

                    self.wrd.grid(row=j, column=i)
                    self.wrd.configure(text=word+modifiers[j])
                    
# Noun declination table pop-up
def declination_table(word):
    declinations = ["Nomative", "Genitive-Accusative", "Dative-Locative","Ablative","Instrumental","Comitative"]
    endings = ["", "i", "du", "asa", "ar", "lei"] # Not 100% accurate
    expanded_table = tk.Tk()
    expanded_table.geometry("300x300")
    expanded_table.title("Declination Table")
    d_t = Table(expanded_table,declinations,endings,word)
    expanded_table.mainloop()
            
    
    
    
srh_entry = tk.Entry(root,textvariable = search, font=('arial',10))
srh_btn=tk.Button(root, text="Search", command = dict_search)
translation_label = tk.Label(root, text="")

srh_entry.grid(row=0,column=0)
srh_btn.grid(row=1,column=0)
translation_label.grid(row=2,column=0)

root.mainloop()
