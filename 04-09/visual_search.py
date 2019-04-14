import tkinter
import random

target = 'F'
distractor = 'E'
max_elements = 6
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

  generate_stimuli()
  next()

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
  reset_available_positions()
  random.shuffle(available_position)
  stimulus = stimuli.pop()
  for i in range(stimulus[0]):
    label = tkinter.Label(window, font=(None, 20), text=distractor, fg='white', bg='black')
    position = available_position.pop()
    label.grid(column=position[0], row=position[1])

root = tkinter.Tk()
root.title('Visual search')

instr_file = open('instruction.txt', 'r')
instr_text = instr_file.read()

instr_label = tkinter.Label(root, font=(None, 20), text=instr_text)
instr_label.pack()

root.bind('<KeyPress>', instr_press)

root.mainloop()

