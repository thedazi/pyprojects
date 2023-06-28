from tkinter import *


window = Tk()

window.title('Converter tool')
window.minsize(width=300,height=150)
window.config(padx=20,pady=20)

# labels 
mile_label = Label(text="Miles",font=('arial',10))
equal_to_label = Label(text="is equal to",font=('arial',10))
km_label = Label(text="Kilometers",font=('arial',10))
result_label = Label(text="0",font=('arial',10))

# entry
input = Entry(width=10)

# button
def convert_km():
  mile_input = int(input.get())
  km_output = str(round(mile_input * 1.61,2))
  result_label.config(text=km_output)
  
convert_button = Button(text='Calculate', command=convert_km)

#Placement
input.grid(column=5,row=3)
mile_label.grid(column=6,row=3)
equal_to_label.grid(column=4,row=4)
result_label.grid(column=5,row=4)
km_label.grid(column=6,row=4)
convert_button.grid(column=5,row=5)




window.mainloop()