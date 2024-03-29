
from tkinter import *

expression = ""

print("Warning! Close this window will cause the calculator to close")
print("this version (0.1.2-Indev release) is still in development, use for testing purpose only. Thanks for using")

def sqrtpress():
    gui = Tk()
    gui.title("Calculate Your Square Root!")

    canvas = Canvas(gui, width=400, height=300, relief='raised')
    canvas.pack()

    lab1 = Label(gui, text='Calculate The Square Root')
    lab1.config(font=('helvetica', 14))
    canvas.create_window(200, 25, window=lab1)

    lab2 = Label(gui, text='Enter the  Number:')
    lab2.config(font=('helvetica', 10))
    canvas.create_window(200, 100, window=lab2)

    entry1 = Entry(gui)
    canvas.create_window(200, 140, window=entry1)

    def get_SquareRoot():
        a1 = entry1.get()

        lab3 = Label(gui, text='The Square Root of ' + a1 + ' is:', font=('helvetica', 10))
        canvas.create_window(200, 210, window=lab3)

        lab4 = Label(gui, text=float(a1) ** 0.5, font=('helvetica', 10, 'bold'))
        canvas.create_window(200, 230, window=lab4)

    button = Button(gui, text=' Get the number ', fg='white', bg='gray',
                    command=get_SquareRoot, height=1, width=16)
    canvas.create_window(200, 180, window=button)

    gui.mainloop()

def clear():
  global expression
  expression = ""
  equation.set("")

def press(num):
  global expression

  expression = expression + str(num)

  equation.set(expression)

def roundbracketlpress():
    global expression

    expression = expression + '('

    equation.set(expression)

def roundbracketrpress():
    global expression

    expression = expression + ')'

    equation.set(expression)

def equalpress():

 try:

    global expression

    total = str(eval(expression))

    equation.set(total)


 except:
    equation.set(" Error, cannot calculate ")
    expression = ""

if __name__ == "__main__":
  gui = Tk()

  gui.configure(background="black")

  gui.title("CreeperVN's Simple Calculator v.0.1.2 (Indev release)")

  gui.geometry("934x380")

  equation = StringVar()

  expression_field = Entry(gui, textvariable=equation)

  expression_field.grid(columnspan=4, ipadx=360)

  button1 = Button(gui, text=' 1 ', fg='white', bg='gray',
                   command=lambda: press(1), height=4, width=32)
  button1.grid(row=2, column=0)

  button2 = Button(gui, text=' 2 ', fg='white', bg='gray',
                   command=lambda: press(2), height=4, width=32)
  button2.grid(row=2, column=1)

  button3 = Button(gui, text=' 3 ', fg='white', bg='gray',
                   command=lambda: press(3), height=4, width=32)
  button3.grid(row=2, column=2)

  button4 = Button(gui, text=' 4 ', fg='white', bg='gray',
                   command=lambda: press(4), height=4, width=32)
  button4.grid(row=3, column=0)

  button5 = Button(gui, text=' 5 ', fg='white', bg='gray',
                   command=lambda: press(5), height=4, width=32)
  button5.grid(row=3, column=1)

  button6 = Button(gui, text=' 6 ', fg='white', bg='gray',
                   command=lambda: press(6), height=4, width=32)
  button6.grid(row=3, column=2)

  button7 = Button(gui, text=' 7 ', fg='white', bg='gray',
                   command=lambda: press(7), height=4, width=32)
  button7.grid(row=4, column=0)

  button8 = Button(gui, text=' 8 ', fg='white', bg='gray',
                   command=lambda: press(8), height=4, width=32)
  button8.grid(row=4, column=1)

  button9 = Button(gui, text=' 9 ', fg='white', bg='gray',
                   command=lambda: press(9), height=4, width=32)
  button9.grid(row=4, column=2)

  button0 = Button(gui, text=' 0 ', fg='white', bg='gray',
                   command=lambda: press(0), height=4, width=32)
  button0.grid(row=5, column=0)

  plus = Button(gui, text=' + ', fg='white', bg='gray',
                command=lambda: press("+"), height=4, width=32)
  plus.grid(row=2, column=3)

  minus = Button(gui, text=' - ', fg='white', bg='gray',
                 command=lambda: press("-"), height=4, width=32)
  minus.grid(row=3, column=3)

  multiply = Button(gui, text=' * ', fg='white', bg='gray',
                    command=lambda: press("*"), height=4, width=32)
  multiply.grid(row=4, column=3)

  divide = Button(gui, text=' / ', fg='white', bg='gray',
                  command=lambda: press("/"), height=4, width=32)
  divide.grid(row=5, column=3)

  equal = Button(gui, text=' = ', fg='white', bg='gray',
                 command=equalpress, height=4, width=32)
  equal.grid(row=5, column=2)

  clear = Button(gui, text='Clear', fg='white', bg='gray',
                 command=clear, height=4, width=32)
  clear.grid(row=5, column='1')

  Decimal = Button(gui, text='.', fg='white', bg='gray',
                   command=lambda: press('.'), height=4, width=32)
  Decimal.grid(row=6, column=0)

  roundbracketl = Button(gui, text='(', fg='white', bg='gray',
                          command=roundbracketlpress, height=4, width=32)
  roundbracketl.grid(row=6, column=1)

  roundbracketr = Button(gui, text=')', fg='white', bg='gray',
                          command=roundbracketrpress, height=4, width=32)
  roundbracketr.grid(row=6, column=2)

  sqrt = Button(gui, text='√', fg='white', bg='gray',
                          command=sqrtpress, height=4, width=32)
  sqrt.grid(row=6, column=3)

  gui.mainloop()

