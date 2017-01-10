from Tkinter import *

def sayHello():
    print "hello"

def sayHello2():
    print "sayHello2"

def sayHello3():
    print "sayHello3"

def sayHello4():
    print "sayHello4"

root = Tk("300x300+200+200")

root.title("Hello Worlk")

topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side = BOTTOM)

button1 = Button(topFrame, text = "Button1", command = sayHello)
button2 = Button(topFrame, text = "Button2", command = sayHello2)
button3 = Button(topFrame, text = "Button3", command = sayHello3)
button4 = Button(bottomFrame, text = "Button4", command = sayHello4)
button5 = Button(bottomFrame, text = "Button4", command = sayHello5)


button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()

root.mainloop()








