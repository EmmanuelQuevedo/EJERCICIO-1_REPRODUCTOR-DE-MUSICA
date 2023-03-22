
from tkinter import *

from tkinter import ttk

root=Tk()

root.title("CONVERSOR DE MONEDAS")


def Conversion():
    
    if Valor1.get()!=Valor2.get():

        if Valor2.get()=="MXN":

            if Valor1.get()=="USD":
                resultado = Moneda.get()*18.60
                textoResult.config(text=f'{resultado} MXN')

            if Valor1.get()=="EUR":
                resultado = Moneda.get()*20.04
                textoResult.config(text=f'{resultado} MXN')

        if Valor2.get()=="USD":

            if Valor1.get()=="MXN":
                resultado = Moneda.get()*0.054
                textoResult.config(text=f'{resultado} USD')

            if Valor1.get()=="EUR":
                resultado = Moneda.get()*1.08
                textoResult.config(text=f'{resultado} USD')

        if Valor2.get()=="EUR":

            if Valor1.get()=="MXN":
                resultado = Moneda.get()*0.05
                textoResult.config(text=f'{resultado} EUR')

            if Valor1.get()=="USD":
                resultado = Moneda.get()*0.93
                textoResult.config(text=f'{resultado} EUR')

    else:
        textoResult.config(text=f'VERIFIQUE LA OPCIÓN SELECIONADA')


Moneda = IntVar()
Valor2 = StringVar()
Valor1 = StringVar()

ventanaPrincipal = Frame(root, bg="#a0a0a0")
ventanaPrincipal.grid()

#titulo de la raiz
titulo = Label(ventanaPrincipal, text="Conversor de Monedas", font=("Roboto",18,"bold"), bg="#a0a0a0")
titulo.grid(row=1,column=1, rowspan=2, columnspan=4)

#Etiqueta moneda actual
titulo = Label(ventanaPrincipal, text="Numero A", font=("Roboto",12), bg="#a0a0a0")
titulo.grid(row=3,column=1,pady=20)

textoNumeroA = Entry(ventanaPrincipal, font=("Roboto",12), textvariable=Moneda).grid(row=3,column=2)

#moneda actual
titulo = Label(ventanaPrincipal, text="Moneda Actual", font=("Roboto",12), bg="#a0a0a0")
titulo.grid(row=4,column=1)

Lista = ttk.Combobox(ventanaPrincipal,values=["USD", "MXN", "EUR"], state="readonly", textvariable=Valor1).grid(row=4,column=2,pady=10)

#moneda a convertir
titulo = Label(ventanaPrincipal, text="Moneda", font=("Roboto",12), bg="#a0a0a0")
titulo.grid(row=4,column=3, padx=10)

Lista = ttk.Combobox(ventanaPrincipal,values=["USD", "MXN", "EUR"], state="readonly", textvariable = Valor2).grid(row=4,column=4, pady=10)

#etiqueta resultado
titulo = Label(ventanaPrincipal, text="Resultado", font=("Roboto",12), bg="#a0a0a0")
titulo.grid(row=5,column=1,pady=10)

textoResult = Label(ventanaPrincipal, text="                         ", font=("Roboto",12))
textoResult.grid(row=5,column=2)

#Boton para convertir
botonConvertir = Button(ventanaPrincipal, text="Convertir", font=("Roboto",12), command=Conversion).grid(row=12, column=2,columnspan=10, rowspan=4,pady=10)

root.mainloop()