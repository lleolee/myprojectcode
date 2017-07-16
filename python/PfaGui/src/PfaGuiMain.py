#!/usr/bin/env python

from functools import partial
from tkinter import Tk, Button, X
from tkinter.messagebox import showinfo, showwarning, showerror

WARN = 'warn'
CRIT = 'crit'
REGU = 'regu'

SIGNS = {'do not enter ':CRIT,
         'railroad crossing':WARN,
         'speed limit':REGU,
         'wrong way':CRIT,
         'merging traffic':WARN,
         'one way':REGU, }

critCB = lambda:showerror('Error', 'Error Button Pressed!')
warnCB = lambda:showwarning('Warning', 'Warning Button Pressed!')
infoCB = lambda:showinfo('Info', 'Info Button Pressed!')

top = Tk()
top.title('Rosd Signs')
Button(top, text='QUIT', command=top.quit, bg='red', fg='white').pack()

MyBttton = partial(Button, top)
CritButton = partial(MyBttton, command=critCB, bg='white', fg='red')
WarnButton = partial(MyBttton, command=warnCB, bg='goldenrod1')
ReguButton = partial(MyBttton, command=infoCB, bg='white')

for eachSign in SIGNS:
    signType = SIGNS[eachSign]
    cmd = '%sButton(text=%r%s).pack(fill=X,expand=True)' % (
        signType.title(), eachSign,
        '.upper()' if signType == CRIT else '.title()')
    print(cmd)
    print(eachSign)
    print(signType)
    eval(cmd)
    
top.mainloop()
