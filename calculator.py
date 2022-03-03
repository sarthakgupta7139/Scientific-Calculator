from tkinter import *
import math
import tkinter.font as font
#from PIL import Image,ImageTk

'''import pygame
pygame.mixer.init()
pygame.mixer.music.load('Equips_Graphics\Shape_of_you.mp3')
pygame.mixer.music.play(loops=9)'''

exp = ""

def buttonclick(x):
	global exp
	func = ['Sin', 'Cos', 'Tan', 'Sin^-1', 'Cos^-1', 'Tan^-1', 'log']
	if exp in func:
		exp=''
	elif exp == 0 :
		exp = ''
	exp = exp + str(x)
	entry.set(exp)


def clear():
	global exp
	exp = 0
	entry.set(exp)

def equal():
	try:
		global exp, fnum
		global f
		if exp == '' :
			entry.set(0)
		if f == 'pow':
			snum = float(entry.get())
			res = math.pow(fnum, snum)
			entry.set(res)
			exp = str(res)

		elif f == 'sin':
			snum = float(entry.get())
			a = math.radians(snum)
			ans = round(math.sin(a), 5)
			entry.set(ans)
			exp = str(ans)

		elif f == 'cos':
			snum = float(entry.get())
			a = math.radians(snum)
			ans = round(math.cos(a), 5)
			entry.set(ans)
			exp = str(ans)

		elif f == 'tan':
			snum = float(entry.get())
			a = math.radians(snum)
			ans = round(math.tan(a), 5)
			entry.set(ans)
			exp = str(ans)

		elif f == 'per':
			snum = float(entry.get())
			res = (fnum / snum) * 100
			entry.set(res)
			exp = str(res)

		elif f == 'sininv':
			snum = float(entry.get())
			a = math.radians(snum)
			ans = round(math.asin(a), 5)
			entry.set(ans)
			exp = str(ans)

		elif f == 'cosinv':
			snum = float(entry.get())
			a = math.radians(snum)
			ans = round(math.acos(a), 5)
			entry.set(ans)
			exp = str(ans)

		elif f == 'taninv':
			snum = float(entry.get())
			a = math.radians(snum)
			ans = round(math.atan(a), 5)
			entry.set(ans)
			exp = str(ans)

		elif f == 'log':
			snum = float(entry.get())
			a = math.log(snum)
			entry.set(a)
			exp = str(a)

	except:

		q = entry.get()
		res = eval(q)
		entry.set(res)
		exp = str(res)



def squareroot():
	global exp
	a = float(entry.get())
	res = math.sqrt(a)
	entry.set(res)
	exp = str(res)


def power():
	global fnum, exp, f
	fnum = float(entry.get())
	exp = ''
	entry.set(exp)
	f = 'pow'



def log():
	try:
		global exp, f
		exp = 'log'
		entry.set(exp)
		f = 'log'

	except:
		entry.set('Expression Error')


def Eulersno():
	global fnum, exp
	a = math.e
	entry.set(a)
	exp = str(a)


def Sinfun():
	global exp, f
	exp = 'Sin'
	entry.set(exp)
	f = 'sin'


def Cosfun():
	global exp, f
	exp = 'Cos'
	entry.set(exp)
	f = 'cos'


def Tanfun():
	global exp, f
	exp = 'Tan'
	entry.set(exp)
	f = 'tan'


def Percent():
	global exp, fnum, f
	fnum = float(entry.get())
	exp = ''
	entry.set(exp)
	f = 'per'


def Factorial():
	global exp
	try :
		a = int(entry.get())
		for i in range(1, a):
			a = a * i
		entry.set(a)
		exp = str(a)
	except :
		entry.set('Expression Error')


def Sininv():
	global exp, f
	exp = 'Sin^-1'
	entry.set(exp)
	f = 'sininv'


def Cosinv():
	global exp, f
	exp = 'Cos^-1'
	entry.set(exp)
	f = 'cosinv'


def Taninv():
	global exp, f
	exp = 'Tan^-1'
	entry.set(exp)
	f = 'taninv'


def Square():
	global exp
	try:
		fnum = float(entry.get())
		res = fnum ** 2
		entry.set(res)
	except:
		entry.set('Enter Valid Expression')


def checkMemory() :
	new = Toplevel(root)
	new.geometry('400x250+100+00')
	new.title('Check')


root = Tk()
root.title('Scientific Calculator')
root.geometry('780x380+190+140')
root.configure(bg='grey24')
root.resizable(width=False, height=False)
entry = StringVar()
entry.set('Enter Expression')

'''Frame Background if not worked: SlateBlue2'''
frame = Frame(root,bg='red',borderwidth=6,relief=GROOVE)
frame.grid(column=6,rowspan=7,padx=20)
'''img = Image.open("Equips_Graphics\cal1.jpg")
img = img.resize((250,250),Image.ANTIALIAS)
photo = ImageTk.PhotoImage(img)
image1 = Label(frame,image=photo)
image1.grid(pady=10)
'''
'''checkbtn = Button(frame,text='Check', fg='black', bg='coral',command=checkMemory)
checkbtn.grid(pady=10)'''

#root = Frame(root, bg='cyan')
#root.grid(column=5, row=1, rowspan=5)

myfont = font.Font(family='Comic Sans MS', weight='bold', size=10)

font2 = font.Font(family='courier',slant='italic')

inputexp = Entry(root, justify=RIGHT, textvariable=entry,font=font2)
inputexp.grid(row=0, columnspan=6, ipadx=100, ipady=5, pady=20)

btn7 = Button(root, text=' 7 ', fg='black', bg='coral', padx=12, pady=5, bd=4, font=font2, command=lambda: buttonclick(7))
btn7.grid(row=1, column=0, padx=5, pady=5)

btn8 = Button(root, text=' 8 ', fg='black', bg='coral', padx=12, pady=5, bd=4, font=font2, command=lambda: buttonclick(8))
btn8.grid(row=1, column=1, padx=5, pady=5)

btn9 = Button(root, text=' 9 ', fg='black', bg='coral', padx=12, pady=5, bd=4, font=font2, command=lambda: buttonclick(9))
btn9.grid(row=1, column=2, padx=5, pady=5)

btn4 = Button(root, text=' 4 ', fg='black', bg='coral', padx=12, pady=5, bd=4, font=font2, command=lambda: buttonclick(4))
btn4.grid(row=2, column=0, padx=5, pady=5)

btn5 = Button(root, text=' 5 ', fg='black', bg='coral', padx=12, pady=5, bd=4, font=font2, command=lambda: buttonclick(5))
btn5.grid(row=2, column=1, padx=5, pady=5)

btn6 = Button(root, text=' 6 ', fg='black', bg='coral', padx=12, pady=5, bd=4, font=font2, command=lambda: buttonclick(6))
btn6.grid(row=2, column=2, padx=5, pady=5)

btn1 = Button(root, text=' 1 ', fg='black', bg='coral', padx=12, pady=5, bd=4, font=font2, command=lambda: buttonclick(1))
btn1.grid(row=3, column=0, padx=5, pady=5)

btn2 = Button(root, text=' 2 ', fg='black', bg='coral', padx=12, pady=5, bd=4, font=font2, command=lambda: buttonclick(2))
btn2.grid(row=3, column=1, padx=5, pady=5)

btn3 = Button(root, text=' 3 ', fg='black', bg='coral', padx=12, pady=5, bd=4, font=font2, command=lambda: buttonclick(3))
btn3.grid(row=3, column=2, padx=5, pady=5)

add = Button(root, text=" + ", fg='black', bg='misty rose', font=myfont, bd=6, padx=12, pady=5,command=lambda: buttonclick('+'))
add.grid(row=1, column=3, padx=5, pady=5)

sub = Button(root, text=" - ", fg='black', bg='misty rose', font=myfont, bd=6, padx=12, pady=5,command=lambda: buttonclick('-'))
sub.grid(row=2, column=3, padx=5, pady=5)

multi = Button(root, text=" X ", fg='black', bg='misty rose', font=myfont, bd=6, padx=12, pady=5, command=lambda: buttonclick('*'))
multi.grid(row=3, column=3, padx=5, pady=5)

div = Button(root, text=" / ", fg='black', bg='misty rose', font=myfont, bd=6, padx=12, pady=5, command=lambda: buttonclick('/'))
div.grid(row=4, column=3, padx=5, pady=5)

btn0 = Button(root, text=' 0 ', fg='black', bg='coral', padx=12, pady=5, bd=4, font=font2, command=lambda: buttonclick(0))
btn0.grid(row=4, column=1, padx=5, pady=5)

btndec = Button(root, text=' . ', fg='black', bg='coral', font=myfont, bd=6, padx=12, pady=5, command=lambda: buttonclick('.'))
btndec.grid(row=4, column=0, padx=5, pady=5)

btnclr = Button(root, text=' C ', fg='black', bg='wheat3', font=myfont, bd=6, padx=12, pady=5, command=clear)
btnclr.grid(row=4, column=2, padx=5, pady=5)

btneq = Button(root, text=' = ', fg='black', bg='cyan', font=myfont, bd=6, padx=12, pady=5, command=equal)
btneq.grid(row=5, column=3, padx=5, pady=5)

btnsqrt = Button(root, text=' √ ', fg='black', bg='misty rose', font=myfont, bd=6, padx=12, pady=5, command=squareroot)
btnsqrt.grid(row=5, column=0, padx=5, pady=5)

btnpow = Button(root, text=' ^ ', fg='black', bg='misty rose', font=myfont, bd=6, padx=12, pady=5, command=power)
btnpow.grid(row=5, column=1, padx=5, pady=5)

btper = Button(root, text=' % ', fg='black', bg='misty rose', font=myfont, bd=6, padx=12, pady=5, command=Percent)
btper.grid(row=5, column=2, padx=5, pady=5)

btne = Button(root, text=' e ', fg='black', bg='misty rose', font=myfont, bd=6, padx=12, pady=5, command=Eulersno)
btne.grid(row=1, column=4, padx=5, pady=5)

btnlog = Button(root, text=' ln ', fg='black', bg='misty rose', font=myfont, bd=6, padx=10, pady=5, command=log)
btnlog.grid(row=2, column=4, padx=5, pady=5)

btsin = Button(root, text='sin', fg='black', bg='misty rose', font=myfont, bd=6, padx=12, pady=5, command=Sinfun)
btsin.grid(row=3, column=4, padx=5, pady=5)

btcos = Button(root, text='cos', fg='black', bg='misty rose', font=myfont, bd=6, padx=12, pady=5, command=Cosfun)
btcos.grid(row=4, column=4, padx=5, pady=5)

bttan = Button(root, text='tan', fg='black', bg='misty rose', font=myfont, bd=6, padx=12, pady=5, command=Tanfun)
bttan.grid(row=5, column=4, padx=5, pady=5)

btfac = Button(root, text=' ! ', fg='black', bg='misty rose', font=myfont, bd=6, padx=26, pady=5, command=Factorial)
btfac.grid(row=1, column=5, padx=5, pady=5)

btisin = Button(root, text='sin^-1', fg='black', bg='misty rose', font=myfont, bd=6, padx=12, pady=5, command=Sininv)
btisin.grid(row=2, column=5, padx=5, pady=5)

bticos = Button(root, text='cos^-1', fg='black', bg='misty rose', font=myfont, bd=6, padx=12, pady=5, command=Cosinv)
bticos.grid(row=3, column=5, padx=5, pady=5)

btitan = Button(root, text='tan^-1', fg='black', bg='misty rose', font=myfont, bd=6, padx=12, pady=5, command=Taninv)
btitan.grid(row=4, column=5, padx=5, pady=5)

btnsq = Button(root, text='x^2', fg='black', bg='misty rose', font=myfont, bd=6, padx=22, pady=5, command=Square)
btnsq.grid(row=5, column=5, padx=5, pady=5)

root.mainloop()
