from tkinter import*

from PIL import ImageTk, Image

root = Tk()

ventanaPrincipal =Frame(root, background="#a0a0a0")

ventanaPrincipal.grid()

contra = StringVar()

confcontra= StringVar()


def sesion():
    if contra.get()==confcontra.get():
        print("SESIÓN INICIADA")
        ventanaPrincipal.config(bg="#00ff00")
        titulo1.config(bg="#00ff00")
        titulo2.config(bg="#00ff00")
        titulo3.config(bg="#00ff00")
        titulo4.config(bg="#00ff00")


    else:
        print("CONTRASEÑA INCORRECTA")
        ventanaPrincipal.config(bg="#a0a0a0")



titulo1 = Label(ventanaPrincipal, text="LOG IN ", font=("Roboto", 12),background="#a0a0a0")
titulo1.grid(row=4,column=1, rowspan=2, columnspan=4)

titulo2 = Label(ventanaPrincipal, text="Nombre: ", font=("Roboto", 12),background="#a0a0a0")
titulo2.grid(row=7, column=1)

titulo3 = Label(ventanaPrincipal, text="Contraseña: ", font=("Roboto", 12), background="#a0a0a0")
titulo3.grid(row=8, column=1)

titulo4 = Label(ventanaPrincipal, text="Confirmar contraseña: ", font=("Roboto", 12),background="#a0a0a0")
titulo4.grid(row=9, column=1)

#textoNombre1 = Entry(ventanaPrincipal, font=("Roboto", 12))
#textoNombre1.grid(row=4,column=2,pady=2)

textoNombre2 = Entry(ventanaPrincipal, font=("Roboto", 12))
textoNombre2.grid(row=7,column=2, pady=2)

textoNombre3= Entry(ventanaPrincipal, font=("Roboto", 12), textvariable=contra)
textoNombre3.grid(row=8,column=2, pady=2)

textoNombre4 = Entry(ventanaPrincipal, font=("Roboto", 12), textvariable=confcontra)
textoNombre4.grid(row=9,column=2, pady=2)

checkbox1 = Checkbutton(ventanaPrincipal, text="Hombre", background="#a0a0a0").grid(row=10, column=1,)

checkbox2 = Checkbutton(ventanaPrincipal, text="Mujer", background="#a0a0a0").grid(row=10, column=2)

checkbox3 = Checkbutton(ventanaPrincipal, text="Acepto términos", background="#a0a0a0").grid(row=11, column=1, rowspan=1)


botonLog =Button(ventanaPrincipal, text="INICIAR", width=10, height=1, command=sesion, background="#a0a0a0").grid(row=12, column=1,columnspan=3, rowspan=4)




imgPerfil = Image.open("perfil.jpeg") #Variable que contiene el nombre de la imagen
imagenMusica = imgPerfil.resize((50,50))
imag = ImageTk.PhotoImage(imagenMusica)


miTitulo = Label(ventanaPrincipal,image=imag)
miTitulo.grid(row=1,column=1, rowspan=2, columnspan=4)


root.mainloop()