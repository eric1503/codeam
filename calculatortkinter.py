from tkinter import *

window = Tk()
window.title("Calculator")
window.configure(bg="gray10")

input_bar = Entry(window, width = 45, borderwidth = 5)
input_bar.grid(row = 0, column = 0, columnspan = 3, padx = 0, pady = 10)

def button_click(number):
	current = input_bar.get()
	input_bar.delete(0, END)
	input_bar.insert(0, str(current) + str(number))

def button_clear():
	input_bar.delete(0, END)

def button_add():
	first_number = input_bar.get()
	global f_num
	global math
	math = "addition"
	f_num = float(first_number)
	input_bar.delete(0, END)

def button_subtract():
	first_number = input_bar.get()
	global f_num
	global math
	math = "subtraction"
	f_num = float(first_number)
	input_bar.delete(0, END)

def button_multiply():
	first_number = input_bar.get()
	global f_num
	global math
	math = "multiplication"
	f_num = float(first_number)
	input_bar.delete(0, END)

def button_divide():
	first_number = input_bar.get()
	global f_num
	global math
	math = "division"
	f_num = float(first_number)
	input_bar.delete(0, END)

def button_equal():
	second_number = input_bar.get()
	input_bar.delete(0,END)

	if math == "addition":
		input_bar.insert(0, f_num + float(second_number))

	if math == "subtraction":
		input_bar.insert(0, f_num - float(second_number))

	if math == "multiplication":
		input_bar.insert(0, f_num * float(second_number))

	if math == "division":
		input_bar.insert(0, f_num / float(second_number))




button1 = Button(window, text = "1", padx=40, pady=20, bg = "gray10", fg = "AntiqueWhite1", relief = "flat", font = "Bold", command = lambda: button_click(1))
button2 = Button(window, text = "2", padx=40, pady=20, bg = "gray10", fg = "AntiqueWhite1", relief = "flat",font = "Bold", command = lambda: button_click(2))
button3 = Button(window, text = "3", padx=40, pady=20, bg = "gray10", fg = "AntiqueWhite1",relief = "flat",font = "Bold", command = lambda: button_click(3))
button4 = Button(window, text = "4", padx=40, pady=20, bg = "gray10", fg = "AntiqueWhite1",relief = "flat",font = "Bold", command = lambda: button_click(4))
button5 = Button(window, text = "5", padx=40, pady=20, bg = "gray10", fg = "AntiqueWhite1",relief = "flat",font = "Bold", command = lambda: button_click(5))
button6 = Button(window, text = "6", padx=40, pady=20, bg = "gray10", fg = "AntiqueWhite1",relief = "flat",font = "Bold", command = lambda: button_click(6))
button7 = Button(window, text = "7", padx=40, pady=20, bg = "gray10", fg = "AntiqueWhite1",relief = "flat",font = "Bold", command = lambda: button_click(7))
button8 = Button(window, text = "8", padx=40, pady=20, bg = "gray10", fg = "AntiqueWhite1",relief = "flat",font = "Bold", command = lambda: button_click(8))
button9 = Button(window, text = "9", padx=40, pady=20, bg = "gray10", fg = "AntiqueWhite1",relief = "flat",font = "Bold", command = lambda: button_click(9))
button0 = Button(window, text = "0", padx=40, pady=20, bg = "gray10", fg = "AntiqueWhite1",relief = "flat",font = "Bold", command = lambda: button_click(0))
buttonpoint = Button(window, text = ".", padx=43, pady=20, bg = "gray10", fg = "AntiqueWhite1",relief = "flat",font = "Bold", command = lambda: button_click("."))
button_clear = Button(window, text = "cls", padx=35, bg = "gray10", fg = "AntiqueWhite1",relief = "flat",font = "Bold", pady=20, command = button_clear)
button_equal = Button(window, text = "=", padx=40, pady=20, bg = "gray10", fg = "AntiqueWhite1",relief = "flat",font = "Bold", command = button_equal)
button_add = Button(window, text = "+", padx=40, pady=20, bg = "spring green", fg = "black",relief = "flat",font = "Bold", command = button_add)
button_subtract = Button(window, text = "-", padx=42,pady=20, bg = "spring green", fg = "black",relief = "flat",font = "Bold", command = button_subtract)
button_multiply = Button(window, text = "x", padx=41, pady=20, bg = "spring green", fg = "black",relief = "flat",font = "Bold", command = button_multiply)
button_divide = Button(window, text = "/", padx=43, pady=20, bg = "spring green", fg = "black",relief = "flat",font = "Bold", command = button_divide)
button_blank = Button(window, text = "", padx=45, pady=23,relief = "flat", bg = "spring green")
#third row
button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)
button_multiply.grid(row=6, column= 0)

#second row
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button_subtract.grid(row=5, column=2)

#first row
button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)
button_add.grid(row=5, column=0)
buttonpoint.grid(row=4, column = 2)

#fourth row
button_clear.grid(row=4, column= 0)
button0.grid(row=4,column=1)
button_equal.grid(row = 5, column=1)
button_divide.grid(row=6, column = 2)
button_blank.grid(row=6,column=1)






window.mainloop()