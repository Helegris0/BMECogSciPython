import tkinter
import random
import time

keys = ['Left', 'Down', 'Right', 'Up']
colors = ['RED', 'GREEN', 'BLUE', 'YELLOW']
color = ''

n = 10

input_enabled = False
start_time = 0

corr = []
rt = []

def close():
  file = open('result.csv', 'w')
  file.write('corr,rt\n')
  for i in range(len(corr)):
    file.write(str(corr[i]) + ',' + str(rt[i]) + '\n')
  file.close()
  root.destroy()

def stimulus():
  global color
  color = random.choice(colors)
  word = random.choice(colors)
  return (color, word)

def next():
  global input_enabled
  global start_time

  input_enabled = False
  label.config(text='')
  label.update()

  time.sleep(.5)

  color, word = stimulus()
  label.config(fg=color, text=word)
  label.update()
  input_enabled = True
  start_time = time.time()

def start_selected():
  start_button.pack_forget()
  next()

def press(event):
  global n
  if (input_enabled and event.keysym in keys):
    n = n - 1
    if (keys.index(event.keysym) == colors.index(color)):
      corr.append(True)
    else:
      corr.append(False)
    rt.append(time.time() - start_time)
    if (n > 0):
      next()
    else:
      close()

root = tkinter.Tk()
root.title('Stroop')

label = tkinter.Label(root, font=(None, 30), text='', width=25, height=10)
label.pack()

start_button = tkinter.Button(root, text='start', command=start_selected)
start_button.pack()

root.bind('<KeyPress>', press)

root.mainloop()

