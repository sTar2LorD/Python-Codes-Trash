
"""
Created on Mon Jun 22 22:04:17 2020
Alumno: Walter Tarmeño Noriega
Codigo: 16190148
"""

"Libreria tkinter para podercrear las interfaces graficas GUI y libreria math para las operaciones"
from tkinter import *              
from math import *

"Se crea una raiz llamada Calculadora donde estara toda la GUI"

Calculadora=Tk()
Calculadora.title("Calculadora Simple")
Calculadora.iconbitmap("calculadora.ico")
Calculadora.geometry("320x466")
Calculadora.resizable(0,0)
Calculadora.config(bg="#272825")

"------------------------Configuracion Botones------------------------"

color_boton_operadores="#A0AABB"
color_boton_numeros="#4E5053"

ancho_boton=9
alto_boton=3

"-----------------------------Operaciones-----------------------------"
"Se define un variable global que se usara para las operaciones, se lo deja en blanco para que"
"sea reemplazda por los valores de entrada de los botones"

operador = ""
 
"Otra variable para los valores que se muestren en las pantalla que sera de tipo string"
texto_pantalla = StringVar()

"Luego se define variables para las botones especiales, en este caso para limpiar la pantalla"
"con el boton Del (Delete), donde cada vez que se presione ese boton se pone la variable global"
"en vacio, a la espera del ingreso del sgte valor, y en la pantalla se muestra el numero 0"
def clear():
    global operador
    operador = ""
    texto_pantalla.set("0")
    
"La variable clic sirve para que tome el valor de de la variable operador y lo concatene con los valores"
"que se vayan ingresando, luego en pantalla sse muestra la variable operador (los digitos y operadores presionados"  
def click(b):
    global operador
    operador += str(b)
    texto_pantalla.set(operador)
    
"Por ultimo en la variable resultado (que se muestra cuando se presiona el boton igual) "
"se usa la funcion try-except para el operador igual, puesto que se hara la secuencia de try, mientras"
"no se de un caso de error operativo o de sintaxis que en este caso el programa se deendra"
"y seguira con la secuencia mostrando la variable local r como error"

"La variable r en try evalua primero la variable operador en busca de una secuencia logico matematico"
"que sea operativo por ejemplo 3+5 luego la resuelve y se convierte en un valor de tipo string"
"para mostrarse en la pantalla, pesto que la variable texto_pantalla es una variable de tipo string"
def resultado():
    global operador
    try:
        r = str(eval(operador))
    except:
        r = "Error de Calculo"
    texto_pantalla.set(r)
    
clear()

"-----------------------BOTONES------------------------"

"Se crea una variable para cada boton con la funcion Button en la que dentro se pondra donde esta"
"contenido en este caso la rai calculadora, luego el texto que tendra el boton, el color de fondo bg"
"y dependiendo de su es un boton de tipo diferente a un operador matematico, se usara la funcion"
"command='una de las 3 variables especiales'caso contrario se remplazara por lambda:clic(""variable operador"")"
"Luego se usa la funcion grid para posicionar los botones"

"------------------------FILA 1------------------------"

BotonLimp = Button(Calculadora,text="DEL",bg=color_boton_operadores,width=ancho_boton,
                height=alto_boton,command=clear).grid(row=1,column=0,pady=3)
BotonParIzq = Button(Calculadora,text="(",bg=color_boton_operadores,width=ancho_boton,
                height=alto_boton,command=lambda:click("(")).grid(row=1,column=1,pady=3)
BotonParDer = Button(Calculadora,text=")",bg=color_boton_operadores,width=ancho_boton,
                height=alto_boton,command=lambda:click(")")).grid(row=1,column=2,pady=3)
BotonDiv = Button(Calculadora,text="/",bg=color_boton_operadores,width=ancho_boton,
                  height=alto_boton,command=lambda:click("/")).grid(row=1,column=3,pady=3)

"------------------------FILA 2------------------------"

Boton7 = Button(Calculadora,text="7",bg=color_boton_numeros,width=ancho_boton,
                height=alto_boton,command=lambda:click(7)).grid(row=2,column=0,pady=3)
Boton8 = Button(Calculadora,text="8",bg=color_boton_numeros,width=ancho_boton,
                height=alto_boton,command=lambda:click(8)).grid(row=2,column=1,pady=3)
Boton9 = Button(Calculadora,text="9",bg=color_boton_numeros,width=ancho_boton,
                height=alto_boton,command=lambda:click(9)).grid(row=2,column=2,pady=3)
BotonMult = Button(Calculadora,text="x",bg=color_boton_operadores,width=ancho_boton,
                  height=alto_boton,command=lambda:click("*")).grid(row=2,column=3,pady=3)

"------------------------FILA 3------------------------"

Boton4 = Button(Calculadora,text="4",bg=color_boton_numeros,width=ancho_boton,
                height=alto_boton,command=lambda:click(4)).grid(row=3,column=0,pady=3)
Boton5 = Button(Calculadora,text="5",bg=color_boton_numeros,width=ancho_boton,
                height=alto_boton,command=lambda:click(5)).grid(row=3,column=1,pady=3)
Boton6 = Button(Calculadora,text="6",bg=color_boton_numeros,width=ancho_boton,
                height=alto_boton,command=lambda:click(6)).grid(row=3,column=2,pady=3)
BotonResta = Button(Calculadora,text="-",bg=color_boton_operadores,width=ancho_boton,
                   height=alto_boton,command=lambda:click("-")).grid(row=3,column=3,pady=3)

"------------------------FILA 4------------------------"

Boton1 = Button(Calculadora,text="1",bg=color_boton_numeros,width=ancho_boton,
                height=alto_boton,command=lambda:click(1)).grid(row=4,column=0,pady=3)
Boton2 = Button(Calculadora,text="2",bg=color_boton_numeros,width=ancho_boton,
                height=alto_boton,command=lambda:click(2)).grid(row=4,column=1,pady=3)
Boton3 = Button(Calculadora,text="3",bg=color_boton_numeros,width=ancho_boton,
                height=alto_boton,command=lambda:click(3)).grid(row=4,column=2,pady=3)
BotonSuma = Button(Calculadora,text="+",bg=color_boton_operadores,width=ancho_boton,
                   height=alto_boton,command=lambda:click("+")).grid(row=4,column=3,pady=3)

"------------------------FILA 5------------------------"

BotonNada = Button(Calculadora,text="",bg=color_boton_operadores,width=ancho_boton,
                height=alto_boton).grid(row=5,column=0,pady=3)
Boton0 = Button(Calculadora,text="0",bg=color_boton_numeros,width=ancho_boton,
                height=alto_boton,command=lambda:click(0)).grid(row=5,column=1,pady=3)
BotonPunto = Button(Calculadora,text=".",bg=color_boton_operadores,width=ancho_boton,
                    height=alto_boton,command=lambda:click(".")).grid(row=5,column=2,pady=3)
BotonIgual = Button(Calculadora,text="=",bg="#3564B2",width=ancho_boton,
                   height=alto_boton,command=resultado).grid(row=5,column=3,pady=3)

"------------------------Configuracion Pantalla-----------------------"

"Se llama a una variable pantalla en la que se usara una funcion llamada entry para que los datos se vayan mostrando"
"luego se pone donde estara ubicado en este caso en la raiz llamada calculadora, se le asigna la alineacion de texto,"
"fuente, tamaño, ancho ancho del borde color de fondo y color de la parte frontal, para finalizar colocanto la variable,"
"mediante la funcion textvariable, que se mostrará, en este caso la variable asignada texto_pantalla"
pantalla=Entry(Calculadora, justify="left",font=("Times New Roma",20,"bold"),width=19,
                 borderwidth=8,bg="#98CD3B",fg="#151614", textvariable=texto_pantalla)
"luego se le asigna su posicion en la raiz"
pantalla.grid(row=0,column=0, padx=9, pady=45, columnspan=4)

"para finalizar se usa la funcion mainloop para mantener siempre abierto el GUI"
Calculadora.mainloop()