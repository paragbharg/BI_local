from Tkinter import *

def sayHello(val):
    print "hello = ",  val

root = Tk("300x300+200+200")

root.title("Hello Worlk")

topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side = BOTTOM)

button1 = Button(topFrame, text = "Button1", command = lambda: sayHello(1))
button2 = Button(topFrame, text = "Button2", command = lambda: sayHello(2))
button3 = Button(topFrame, text = "Button3", command = lambda: sayHello(3))
button4 = Button(bottomFrame, text = "Button4", command = lambda: sayHello(4))
button5 = Button(bottomFrame, text = "Button4", command = lambda: sayHello(5))

button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()

root.mainloop()








