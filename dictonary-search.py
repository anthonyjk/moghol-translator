import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog

select_file = tk.Tk()  # Dialog box to prompt user for the file.
select_file.withdraw()

# read

in_path = filedialog.askopenfilename()
inspect_log = open(in_path)  # Open event_log.log for read only access.*
data = inspect_log.read()

# search

pattern = simpledialog.askstring('Search', 'What to search?')

results = []
for line in data.split('\n'):
    if pattern in line:
        results.append(line)
results = "".join(results)

# save results

output_file = open("output.txt", "w")
output_file.write(results)
output_file.close()

# display result

text = tk.Text(select_file)
text.pack()

text.insert('end', results)

button = tk.Button(select_file, text="Close", command=select_file.destroy)
button.pack()

select_file.deiconify()
select_file.mainloop()
