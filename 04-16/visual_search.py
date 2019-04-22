import tkinter
import random

target = 'F'
distractor = 'E'
max_elements = 6
keys = ['i', 'n']
stimuli = []

width = 10
height = 10
available_position = []

window = None

def instr_press(event):
  global window
  root.unbind('<KeyPress>')
  window = tkinter.Toplevel(root)
  window.configure(background='black')

  for i in range(width):
    window.grid_columnconfigure(i, minsize=50)

  for i in range(height):
    window.grid_rowconfigure(i, minsize=50)

  generate_stimuli()
  next()
  window.bind('<KeyPress>', stimuli_press)
  window.focus_set()

def generate_stimuli():
  global stimuli
  for i in range(1, max_elements + 1):
    stimuli.append((i, True))
    stimuli.append((i, False))
  random.shuffle(stimuli)

def reset_available_positions():
  global available_position
  for i in range(height):
    for j in range(width):
      available_position.append((i, j))

def next():
  global stimuli
  global available_position

  for slave in window.grid_slaves():
    slave.destroy()

  reset_available_positions()
  random.shuffle(available_position)
  stimulus = stimuli.pop()
  for i in range(stimulus[0]):
    if i == 0 and stimulus[1]:
      letter = target
    else:
      letter = distractor
    label = tkinter.Label(window, font=(None, 20), text=letter, fg='white', bg='black')
    position = available_position.pop()
    label.grid(column=position[0], row=position[1])

def stimuli_press(event):
  if event.keysym in keys:
    if stimuli:
      next()
    else:
      window.destroy()

root = tkinter.Tk()
root.title('Visual search')

instr_file = open('instruction.txt', 'r')
instr_text = instr_file.read()

instr_label = tkinter.Label(root, font=(None, 20), text=instr_text)
instr_label.pack()

root.bind('<KeyPress>', instr_press)

root.mainloop()

