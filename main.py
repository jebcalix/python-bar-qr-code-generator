from functools import partial
from tkinter.filedialog import *
import tkinter as tk
from tkinter import ttk
import qrcode
from barcode import EAN13
from barcode.writer import ImageWriter


def QRG(code):
	qr = qrcode.QRCode(
		version = 1,
		box_size = 15,
		border = 10
	)
	print('code:', code.get())
	qr.add_data(code.get())
	qr.make(fit=True)

	img = qr.make_image(fill = 'black', back_color = 'white')

	save_path = asksaveasfilename(filetypes=[('Images', '.png')])

	img.save(save_path + 'qr_code.png', optimize=True, quality=70)
def BARG(code):
	print('code:', code.get())
	code = code.get()
	my_code = EAN13(code, writer=ImageWriter())

	save_path = asksaveasfilename(filetypes=[('Images', '.png')])

	my_code.save(save_path + 'bar_code.png')
	

root = tk.Tk()
root.title("Generador de Codigos")
root.geometry("400x400+400+400")
root.config(bg='gray')
root.resizable(False, False)
code = ttk.Entry(width=20, font=('Arial Bold',28))
code.place(x=0,y=0)
tk.Button(width=3, height=1,font=('Arial Bold', 18), text='QR', relief='groove', bg='white',command=partial(QRG, code)).place(x=100, y=125)
tk.Button(width=3, height=1,font=('Arial Bold', 18), text='BAR', relief='groove', bg='white',command=partial(BARG, code)).place(x=225, y=125)

root.mainloop()