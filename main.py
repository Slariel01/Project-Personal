from tkinter import *

from tkinter import ttk

from tkinter import messagebox




#------------GUI----------------

root = Tk()

root.title("Signos zodiacales")

root.iconbitmap("assets/aries.ico")


root.state("zoomed")




bg = PhotoImage(file="assets/fondo.png")
labelFondo = Label(root, image=bg).place(x=0, y=0)



root.config(bd=0)

root.config(relief="groove")













imgTitle = PhotoImage(file="assets/front.png")
labelTitle = Label(root, image=imgTitle, border=0).pack()

textFrame = Frame(width=300, height=400, background="#F2C4F7")
textFrame.pack()





diaLabel = Label(textFrame, text="Introduzca su dia de nacimiento: ", padx=10, pady=10, background="#F2C4F7")
diaLabel.grid(row=0, column=0,  padx=5, pady=5)






mesLabel = Label(textFrame, text="Introduzca su mes de nacimiento: ", padx=10, pady=10, background="#F2C4F7")
mesLabel.grid(row=1, column=0,  padx=5, pady=5)







#------------lista desplegable de meses--------------

opciones = [
    "Enero", 
    "Febrero", 
    "Marzo", 
    "Abril", 
    "Mayo", 
    "Junio", 
    "Julio", 
    "Agosto", 
    "Septiembre", 
    "Octubre", 
    "Noviembre", 
    "Diciembre"] 



#-------------------------------------------------------

diaFront = IntVar()

diaText = Entry(textFrame, textvariable=diaFront)
diaText.grid(row=0, column=1, padx=5, pady=5)
diaText.config(fg="blue", justify="center", font=("Helvetica",20, "bold"))   



mesFront = StringVar()

mesDesplegable = ttk.Combobox(textFrame, values=opciones, state="readonly", justify="center", font=("Helvetica",19, "bold"),textvariable=mesFront)
mesDesplegable.grid(row=1, column=1, padx=5, pady=5)   




def muestra():
    frameVisual = Frame(root)
    frameVisual.pack()
    frameVisual.place(x=370, y=275)
    


    

    result = StringVar()

    visual = Entry(frameVisual, textvariable=result)
    visual.grid(row=1, column=3, padx=10, pady=10, ipady=78, ipadx=86)
    visual.config(disabledbackground="#BA3DF7", disabledforeground="white", justify="center", font=("Helvetica", 30, "bold") , state="disabled")
    result.set("Sos {}".format(signo))
    




#-------------condicionales---------------

def signoMessage():
    
    global dia
    global mes
    global signo
    signo = ""
    dia = diaFront.get()
    mes = mesFront.get()
    if mes in ariesMar and dia in ariesMar.get("Marzo"):
        signo = "Aries"
        muestra()

    elif mes in ariesAbr and dia in ariesAbr.get("Abril"):
        signo = "Aries"
        muestra()

    elif mes in tauroAbr and dia in tauroAbr.get("Abril"):
        signo = "Tauro"
        muestra()


    elif mes in tauroMay and dia in tauroMay.get("Mayo"):
        signo = "Tauro"
        muestra()

    elif mes in GeminisMay and dia in GeminisMay.get("Mayo"):
        signo = "Geminis"
        muestra()


    elif mes in GeminisJun and dia in GeminisJun.get("Junio"):
        signo = "Geminis"
        muestra()   


    elif mes in cancerJun and dia in cancerJun.get("Junio"):
        signo = "Cancer"
        muestra()  


    elif mes in cancerJul and dia in cancerJul.get("Julio"):
        signo = "Cancer"
        muestra()      


    elif mes in leoJul and dia in leoJul.get("Julio"):
        signo = "Leo"
        muestra()



    elif mes in leoAgo and dia in leoAgo.get("Agosto"):
        signo = "Leo"
        muestra()



    elif mes in virgoAgo and dia in virgoAgo.get("Agosto"):
        signo = "Virgo"
        muestra()



    elif mes in virgoSep and dia in virgoSep.get("Septiembre"):
        signo = "Virgo"
        muestra()



    elif mes in libraSep and dia in libraSep.get("Septiembre"):
        signo = "Libra"
        muestra()



    elif mes in libraOct and dia in libraOct.get("Octubre"):
        signo = "Libra"
        muestra()



    elif mes in escorpioOct and dia in escorpioOct.get("Octubre"):
        signo = "Escorpio"
        muestra()



    elif mes in escorpioNov and dia in escorpioNov.get("Noviembre"):
        signo = "Escorpio"
        muestra()



    elif mes in sagitarioNov and dia in sagitarioNov.get("Noviembre"):
        signo = "Sagitario"
        muestra()      



    elif mes in sagitarioDic and dia in sagitarioDic.get("Diciembre"):
        signo = "Sagitario"
        muestra()



    elif mes in capricornioDic and dia in capricornioDic.get("Diciembre"):
        signo = "Capricornio"
        muestra()



    elif mes in capricornioEne and dia in capricornioEne.get("Enero"):
        signo = "Capricornio"
        muestra()




    elif mes in acuarioEne and dia in acuarioEne.get("Enero"):
        signo = "Acuario"
        muestra()




    elif mes in acuarioFeb and dia in acuarioFeb.get("Febrero"):
        signo = "Acuario"
        muestra()      



    elif mes in piscisFeb and dia in piscisFeb.get("Febrero"):
        signo = "Piscis"
        muestra()



    elif mes in piscisMar and dia in piscisMar.get("Marzo"):
        signo = "Piscis"
        muestra()





    else:
        messagebox.showerror(message="Por favor seleccione una fecha correcta", title="Error")    




#----------------------------------------------------



img = PhotoImage(file="assets/confirm.png")



textButton = Button(root, text="Confirmar", bg="white", command=signoMessage, image=img, border=0).pack() #boton confirmar




#---------------result-------------------






    


  
        





#-------------diccionarios de dias y meses------------------

ariesFirst = list(range(21, 32))

ariesSecond = list(range(1, 20))

ariesMar = {
    "Marzo": ariesFirst,


}

ariesAbr = {
    "Abril": ariesSecond,
}

tauroFirst = list(range(21, 31))

tauroSecond = list(range(1, 21))

tauroAbr = {
    "Abril": tauroFirst
}

tauroMay = {
    "Mayo": tauroSecond
}


GeminisFirst = list(range(21, 32))

GeminisSecond = list(range(1, 21))

GeminisMay = {
    "Mayo": GeminisFirst
}

GeminisJun = {
    "Junio": GeminisSecond
}

cancerFirst = list(range(22, 31))

cancerSecond = list(range(1, 21))

cancerJun = {
    "Junio": cancerFirst
}

cancerJul = {
    "Julio": cancerSecond
}


leoFirst = list(range(22, 32))

leoSecond = list(range(1, 22))

leoJul = {
    "Julio": leoFirst
}

leoAgo = {
    "Agosto": leoSecond
}


virgoFirst = list(range(23, 32))

virgoSecond = list(range(1, 22))

virgoAgo = {
    "Agosto": virgoFirst
}

virgoSep = {
    "Septiembre": virgoSecond
}



libraFirst = list(range(23, 31))

libraSecond = list(range(1, 22))

libraSep = {
    "Septiembre": libraFirst
}

libraOct = {
    "Octubre": libraSecond
}



escorpioFirst = list(range(23, 32))

escorpioSecond = list(range(1, 22))

escorpioOct = {
    "Octubre": escorpioFirst
}

escorpioNov = {
    "Noviembre": escorpioSecond
}




sagitarioFirst = list(range(23, 31))

sagitarioSecond = list(range(1, 21))

sagitarioNov = {
    "Noviembre": sagitarioFirst
}

sagitarioDic = {
    "Diciembre": sagitarioSecond
}



capricornioFirst = list(range(22, 32))

capricornioSecond = list(range(1, 20))

capricornioDic = {
    "Diciembre": capricornioFirst
}

capricornioEne = {
    "Enero": capricornioSecond
}

acuarioFirst = list(range(21, 31))

acuarioSecond = list(range(1, 19))

acuarioEne = {
    "Enero": acuarioFirst
}

acuarioFeb = {
    "Febrero": acuarioSecond
}


piscisFirst = list(range(20, 30))

piscisSecond = list(range(1, 20))

piscisFeb = {
    "Febrero": piscisFirst
}

piscisMar = {
    "Marzo": piscisSecond
}




   









    
    





     







root.mainloop()




