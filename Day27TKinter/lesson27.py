import tkinter

window = tkinter.Tk()

window.title("FIrst Tkinter title")
window.minsize(width=500, height=300)

# adds padding the edges of the window
window.config(padx=20,pady=20)


#label/place/grid (PLACEMENTS)
my_label = tkinter.Label(text="I love you", font=("arial", 24, 'bold'))
# my_label.pack()
#pack calls something and centers it in the widnow
# my_label.place(x=0,y=0)
#place (0,0) is the top left
my_label.grid(column=1,row=1)
my_label.config(padx=50,pady=50)
    #   NOTE grid and pack CANNOT be used together

# IF NO PLACEMENTS ARE DEFINED THEN THE ELEMENT WILL NOT SHOW


#button (GUIs)

def button_action():
  my_label.config(text=input.get())
  
button = tkinter.Button(text='enter', command=button_action)
button.grid(column=2,row=2)
new_button = tkinter.Button(text='enter', command=button_action)
new_button.grid(column=3,row=1)
# button.pack()


#entry

input = tkinter.Entry(width=10)
input.grid(column=4,row=3)
# input.pack()


#text
text = tkinter.Text(height=5,width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(tkinter.END,"Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", tkinter.END))
  #NOTE still not really sure what the 'end' does in the index in this situation
# text.pack()


#spinbox
def spinbox_action():
  print(spinbox.get())
  
spinbox = tkinter.Spinbox(from_=0, to=100,width=5,command=spinbox_action)
# spinbox.pack()


#scale
def scale_action(value):
  print(value)
  
scale = tkinter.Scale(from_=0, to=100, command=scale_action)
# scale.pack()


#checkbox
def checkbox_action():
  #print 1 if on and 0 if not checked
  print(checked_state.get())
  
checked_state = tkinter.IntVar()
checkbutton = tkinter.Checkbutton(
  text='is it on?',
  variable=checked_state,
  command=checkbox_action
  )
checked_state.get()
# checkbutton.pack()


#radio buttons
def radio_action():
  print(radio_state.get())
  
radio_state = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(
  text='option1',
  value=1,
  variable=radio_state,
  command=radio_action
  )
radiobutton2 = tkinter.Radiobutton(
  text='option2',
  value=2,
  variable=radio_state,
  command=radio_action
  )
# radiobutton1.pack()
# radiobutton2.pack()

#mainloop is always the end 
window.mainloop()
