from tkinter import *

master = Tk()

w = Text(master, height=1)
w.delete(1.0, "end")
w.insert(1.0, "Hello, world!")
w.pack()



# if tkinter is 8.5 or above you'll want the selection background
# to appear like it does when the widget is activated
# comment this out for older versions of Tkinter
w.configure(bg=master.cget('bg'), relief="flat")

w.configure(state="disabled")

mainloop()