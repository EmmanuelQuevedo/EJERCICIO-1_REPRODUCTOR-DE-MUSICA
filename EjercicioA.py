from tkinter import *
from PIL import ImageTk, Image
#from tkinter.ttk import *

root =Tk()
#root.geometry("600x500")
root.title("Ejercicio A")

#def registar():
    #print(f'{deptoo.get()} {apellidoo.get()}')

3#def clicked():
    #print(value.get())


value = BooleanVar()

deptoo=StringVar()
apellidoo=StringVar()
skuu=StringVar()
valor=StringVar

framePrincipal=Frame(root, bg="#CD853F")
framePrincipal.grid()

titulo=Label (framePrincipal, text="Registro Productos", bg="#CD853F", font=("Roboto", 20, "bold") )
titulo.grid(row=1, column=2)

producto= Label(framePrincipal,bg="#CD853F", text="Producto:       ",font=("Roboto", 12))
producto.grid(row=5, column=1,padx=10, pady=10)


SKU= Label(framePrincipal,bg="#CD853F", text="SKU:", font=("Roboto", 12)).grid(row=6, column=1,padx=10, pady=10)

Depto= Label(framePrincipal,bg="#CD853F", text="Depto:",font=("Roboto", 12)).grid(row=7, column=1,padx=10, pady=10)

checkbox1 = Checkbutton(framePrincipal, text="A").grid(row=8, column=1,padx=10, pady=10)
checkbox2= Checkbutton(framePrincipal, text="B").grid(row=8, column=2,padx=10, pady=10)
checkbox3= Checkbutton(framePrincipal, text="C").grid(row=8, column=3,padx=10, pady=10)


proveedor= Label(framePrincipal,bg="#CD853F", text="Proveedor:",font=("Roboto", 12)).grid(row=9, column=1,padx=10, pady=10)
opciones=['COCACOLA','BIMBO','PEPSICO']
opcion=OptionMenu(framePrincipal,valor,*opciones).grid(row=9,column=2,padx=10, pady=10)

idioma= Label(framePrincipal,bg="#CD853F", text="Idioma:",font=("Roboto", 12)).grid(row=10, column=1,padx=10, pady=10)

checkbox4 = Checkbutton(framePrincipal, text="EN").grid(row=12, column=1)
checkbox5= Checkbutton(framePrincipal, text="SP").grid(row=12, column=2)




productoTexto= Entry(framePrincipal,textvariable=deptoo).grid(row=5, column=2)

SKUTexto= Entry(framePrincipal,textvariable=apellidoo).grid(row=6, column=2)

DeptoTexto= Entry(framePrincipal,textvariable=skuu).grid(row=7, column=2)

#proveedorTexto= Entry(framePrincipal,textvariable=deptoo).grid(row=9, column=2)

#BotonregistrarSong 
botonregistrarSong =Button(framePrincipal, text="REGISTRAR", fg="#000000", bg="#F5FFFA", font=("Roboto", 10, "bold"), width=15, height=2)
botonregistrarSong.grid(row=15, column=2,padx=10, pady=10)

imgCorreo = Image.open("correo.jpeg") #Variable que contiene el nombre de la imagen
imagenMusica = imgCorreo.resize((100,70))
imag = ImageTk.PhotoImage(imagenMusica)

miTitulo = Label(framePrincipal,image=imag)
miTitulo.grid(row=2,column=2,padx=10, pady=10)




root.mainloop()
