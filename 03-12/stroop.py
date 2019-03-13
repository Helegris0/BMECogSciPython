import tkinter
import random

keys = ['Left', 'Down', 'Right', 'Up']
colors = ['RED', 'GREEN', 'BLUE', 'YELLOW']
color = ''

corr = []

def close_selected():
  print(corr)
  root.destroy()

def stimulus():
  global color
  color = random.choice(colors)
  word = random.choice(colors)
  return (color, word)

def next():
  color, word = stimulus()
  label.config(fg=color, text=word)
  label.update()

def start_selected():
  start_button.pack_forget()
  next()

def press(event):
  if (event.keysym in keys):
    if (keys.index(event.keysym) == colors.index(color)):
      corr.append(True)
    else:
      corr.append(False)
    next()

root = tkinter.Tk()

label = tkinter.Label(root, font=(None, 30), text='ajeékgbealrberli', width=25, height=10)
label.pack()

start_button = tkinter.Button(root, text='start', command=start_selected)
start_button.pack()

close_button = tkinter.Button(root, text='close', command=close_selected)
close_button.pack()

root.bind('<KeyPress>', press)

root.mainloop()

