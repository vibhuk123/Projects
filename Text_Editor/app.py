FONT = 'Georgia'

import tkinter as tk 
from tkinter import filedialog

def showfile():
	fPath = filedialog.askopenfilename()
	if fPath:
		with open(fPath, 'r') as f:
			data = f.read()
		text_box.delete('1.0', tk.END)
		text_box.insert(tk.END, data)
		text_box.fPath = fPath

def save():
	if hasattr(text_box, 'fPath'):
		fPath = text_box.fPath
		with open(fPath, 'w') as f:
			f.write(text_box.get('1.0', tk.END))

def center_popup(win, width, height):
	screenW = win.winfo_screenwidth()
	screenH = win.winfo_screenheight()
	x = int(screenW/2 - width/2)
	y = int(screenH/2 - height/2)
	win.geometry(f"{width}x{height}+{x}+{y}")

def confirm():
	popup = tk.Toplevel(root)
	popup.title('Confirm Save')
	center_popup(popup, 350,200)
	popup.grab_set()

	label = tk.Label(popup, text='Do you want to save the file?', font=(FONT, 20))
	label.place(relx=0.5, rely=0.3, anchor='center')

	def yes():
		save()
		popup.destroy()
		root.destroy()

	def no():
		no_popup = tk.Toplevel(root)
		no_popup.title('No Changes')
		center_popup(no_popup, 250,150)
		tk.Label(no_popup, text="No Changes Made\nEnding Program...", font=(FONT, 10)).place(relx=0.5, rely=0.5, anchor='center')
		no_popup.grab_set()
		no_popup.after(2000, root.destroy)

	yesbtn = tk.Button(popup, text='YES', width=7, font=(FONT, 20), command=yes)
	yesbtn.place(relx=0.325, rely=0.6, anchor='center')

	nobtn = tk.Button(popup, text='NO', width=7, font=(FONT, 20), command=no)
	nobtn.place(relx=0.675, rely=0.6, anchor='center')

root = tk.Tk()
root.title('Text Editor')

win_width = 500
win_height = 500

screenW = root.winfo_screenwidth()
screenH = root.winfo_screenheight()

centerX = int(screenW/2 - win_width/2)
centerY = int(screenH/2 - win_height/2)

root.geometry(f"{win_width}x{win_height}+{centerX}+{centerY}")

label = tk.Label(root, text='Text Editor', font=(FONT, 50))
label.place(relx=0.5, rely=0.1, anchor='center')

text_box = tk.Text(root, wrap='word', width=60, height=20)
text_box.place(relx=0.5, rely=0.5, anchor='center')

open_btn = tk.Button(root, text='Open File', command=showfile, font=(FONT, 25))
open_btn.place(relx=0.325, rely=0.85, anchor='center')

submit_btn = tk.Button(root, text='Done', command=confirm, font=(FONT, 25), width=7)
submit_btn.place(relx=0.675, rely=0.85, anchor='center')

root.mainloop()
