# -*- coding: utf-8 -*-
"""
Alumno: Tarmeño Noriega, Walter
Codigo: 16190148
"""


#--------------------Librerias Filtros--------------------------

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from scipy.fft import fft, fftshift

#---------------------Librerias GUI-----------------------------
from tkinter import *

#----------------------------------------------------------------

from PIL import ImageTk, Image

def Filtro_IRR():
    
    Raiz=Toplevel()
    Raiz.title("Analisis de Filtros IIR")
    Raiz.geometry("571x644")
    Raiz.resizable(0,0)
    Raiz.config(bg="#F4F4F4")
    
    #----------------------Estancia 0-------------------------------
    
    Imagen=LabelFrame(Raiz,text="Grafica IIR",
                font=("Times New Roma",12,"bold")) #,padx=200,pady=150
    
    Imagen.grid(row=0,column=0,columnspan=3)
    
    my_img=ImageTk.PhotoImage(Image.open("IRR_img_Filter.png"))
    mylabel=Label(Imagen,image=my_img)
    mylabel.grid(row=0,column=0)
    
    #--------------------------Filtros------------------------------
    
    def Butterworth(N,fcI,fcS,F_tipo,fs,ang):
        
    #-------------------------Tipo de Filtro IRR------------------------
        
        if F_tipo==0:
            Wn=fcI
            F_tipo='lowpass'
        elif F_tipo==1:
            Wn=fcS
            F_tipo='highpass'
        elif F_tipo==2:
            Wn=[fcI,fcS]
            F_tipo='bandpass'
    
    #--------------------------Tipo de filtro-----------------------
            
        if ang==0:
    #-----------------------Creacion del Filtro digital-------------
            wnI=fcI/(fs/2)
            wnS=fcS/(fs/2)
            if wnI==0:
                Wn=wnS
            elif wnS==0:
                Wn=wnI
            else:
                Wn=[wnI,wnS]
                
            ang=False
            b,a=signal.butter(N,Wn,btype=F_tipo,analog=ang)
            wz,hz=signal.freqz(b,a)
            plt.figure(figsize=(6,5))
            plt.subplot(2,1,1)
            plt.semilogx(wz*fs/6,20*np.log10(abs(hz)))
            plt.title('Respuesta en Frecuencia de un filtro Butterworth Digital')
            plt.xlabel('Frequencia [Hz]')
            plt.ylabel('Amplitud [dB]')
            plt.margins(0, 0.1)
            axes = plt.gca()
            axes.set_xlim([1,10000])
            axes.set_ylim([-60,3])
            plt.tight_layout(True)
            plt.grid(which='both', axis='both')
            
            plt.subplot(2,1,2)
            plt.semilogx(wz*fs/6,np.angle(hz,deg=True),'r')
            plt.title('Fase de un filtro Butterworth')
            plt.xlabel('Frequencia [Hz]')
            plt.ylabel('Fase [Grados]')
            plt.margins(0, 0.1)
            axes = plt.gca()
            axes.set_xlim([1,10000])
            axes.set_ylim([-360,360])
            plt.grid(which='both', axis='both')
            plt.tight_layout(True)
            
            plt.savefig('img.png')
            
        else: 
            ang=True
    #-----------------------Creacion del Filtro Analogico--------------------- 
            
            b, a = signal.butter(N, Wn, btype=F_tipo, analog=ang)
            w, h = signal.freqs(b, a)
            
        #-------------------------Grafica-------------------------------
            plt.figure(figsize=(6,5))
            plt.subplot(2,1,1)
            plt.semilogx(w,20 * np.log10(abs(h)))
            plt.title('Respuesta en Frecuencia de un filtro Butterworth Analogico')
            plt.xlabel('Frequencia [Hz]')
            plt.ylabel('Amplitud [dB]')
            plt.margins(0, 0.1)
            plt.grid(which='both', axis='both')
            axes = plt.gca()
            axes.set_xlim([1,10000])
            axes.set_ylim([-60,3])
            plt.tight_layout(True)
            
            
            plt.subplot(2,1,2)
            plt.semilogx(w,np.angle(h,deg=True),'r')
            plt.title('Fase de un filtro Butterworth')
            plt.xlabel('Frequencia [Hz]')
            plt.ylabel('Fase [Grados]')
            plt.margins(0, 0.1)
            plt.grid(which='both', axis='both')
            plt.tight_layout(True)
            
            plt.savefig('img.png')
        
    def Cebyshev_1(N,rp,fcI,fcS,F_tipo,fs,ang):
        
        if F_tipo==0:
            Wn=fcI
            F_tipo='lowpass'
        elif F_tipo==1:
            Wn=fcS
            F_tipo='highpass'
        elif F_tipo==2:
            Wn=[fcI,fcS]
            F_tipo='bandpass'
        
    #--------------------------Tipo de filtro-----------------------
            
        if ang==0:
    #-----------------------Creacion del Filtro digital-------------
            wnI=fcI/(fs/2)
            wnS=fcS/(fs/2)
            if wnI==0:
                Wn=wnS
            elif wnS==0:
                Wn=wnI
            else:
                Wn=[wnI,wnS]
                
            ang=False
            b,a=signal.cheby1(N, rp, Wn, btype=F_tipo, analog=ang)
            wz,hz=signal.freqz(b,a)
            plt.figure(figsize=(6,5))
            plt.subplot(2,1,1)
            plt.semilogx(wz*fs/6,20*np.log10(abs(hz)))
            plt.title('Respuesta en Frecuencia de un Filtro Chebyshev Tipo I Digital')
            plt.xlabel('Frequencia [Hz]')
            plt.ylabel('Amplitud [dB]')
            plt.margins(0, 0.1)
            axes = plt.gca()
            axes.set_xlim([1,10000])
            axes.set_ylim([-60,3])
            plt.tight_layout(True)
            plt.grid(which='both', axis='both')
            
            plt.subplot(2,1,2)
            plt.semilogx(wz*fs/6,np.angle(hz,deg=True),'r')
            plt.title('Fase de un filtro Chebyshev Tipo I')
            plt.xlabel('Frequencia [Hz]')
            plt.ylabel('Fase [Grados]')
            plt.margins(0, 0.1)
            axes = plt.gca()
            axes.set_xlim([1,10000])
            axes.set_ylim([-360,360])
            plt.grid(which='both', axis='both')
            plt.tight_layout(True)
            
            plt.savefig('img.png')
            
        else:  
    #-----------------------Creacion del Filtro Analogico---------------------     
            ang=True
            b, a = signal.cheby1(N, rp, Wn, btype=F_tipo, analog=ang)
            w, h = signal.freqs(b, a)
    
    #-------------------------Grafica-------------------------------
            plt.figure(figsize=(6,5))
            plt.subplot(2,1,1)
            plt.semilogx(w,20 * np.log10(abs(h)))
            plt.title('Respuesta en Frecuencia de un Filtro Chebyshev Tipo I')
            plt.xlabel('Frequencia [Hz]')
            plt.ylabel('Amplitud [dB]')
            plt.margins(0, 0.1)
            plt.grid(which='both', axis='both')
            plt.tight_layout(True)
            
            
            plt.subplot(2,1,2)
            plt.semilogx(w,np.angle(h,deg=True),'r')
            plt.title('Fase de un filtro Chebyshev Tipo I')
            plt.xlabel('Frequencia [Hz]')
            plt.ylabel('Fase [Grados]')
            plt.margins(0, 0.1)
            plt.grid(which='both', axis='both')
            plt.tight_layout(True)
            
            plt.savefig('img.png')
        
    def Cebyshev_2(N,rp,fcI,fcS,F_tipo,fs,ang):
        
        if F_tipo==0:
            Wn=fcI
            F_tipo='lowpass'
        elif F_tipo==1:
            Wn=fcS
            F_tipo='highpass'
        elif F_tipo==2:
            Wn=[fcI,fcS]
            F_tipo='bandpass'
    
    #--------------------------Tipo de filtro-----------------------
            
        if ang==0:
    #-----------------------Creacion del Filtro digital-------------
            wnI=fcI/(fs/2)
            wnS=fcS/(fs/2)
            if wnI==0:
                Wn=wnS
            elif wnS==0:
                Wn=wnI
            else:
                Wn=[wnI,wnS]
                
            ang=False
            b,a=signal.cheby2(N, rp, Wn, btype=F_tipo, analog=ang)
            wz,hz=signal.freqz(b,a)
            plt.figure(figsize=(6,5))
            plt.subplot(2,1,1)
            plt.semilogx(wz*fs/6,20*np.log10(abs(hz)))
            plt.title('Respuesta en Frecuencia de un Filtro Chebyshev Tipo II Digital')
            plt.xlabel('Frequencia [Hz]')
            plt.ylabel('Amplitud [dB]')
            plt.margins(0, 0.1)
            axes = plt.gca()
            axes.set_xlim([1,10000])
            axes.set_ylim([-60,3])
            plt.tight_layout(True)
            plt.grid(which='both', axis='both')
            
            plt.subplot(2,1,2)
            plt.semilogx(wz*fs/6,np.angle(hz,deg=True),'r')
            plt.title('Fase de un filtro Chebyshev Tipo II')
            plt.xlabel('Frequencia [Hz]')
            plt.ylabel('Fase [Grados]')
            plt.margins(0, 0.1)
            axes = plt.gca()
            axes.set_xlim([1,10000])
            axes.set_ylim([-360,360])
            plt.grid(which='both', axis='both')
            plt.tight_layout(True)
            
            plt.savefig('img.png')
            
        else: 
            ang=True
    #-----------------------Creacion del Filtro Analogico--------------------- 
            b, a = signal.cheby2(N, rp, Wn, btype=F_tipo, analog=ang)
            w, h = signal.freqs(b, a)
    #-------------------------Grafica-------------------------------
            plt.figure(figsize=(6,5))
            plt.subplot(2,1,1)
            plt.semilogx(w,20 * np.log10(abs(h)))
            plt.title('Respuesta en Frecuencia de un Filtro Chebyshev Tipo II ')
            plt.xlabel('Frequencia [Hz]')
            plt.ylabel('Amplitudd [dB]')
            plt.margins(0, 0.1)
            plt.grid(which='both', axis='both')
            plt.tight_layout(True)
            
            
            plt.subplot(2,1,2)
            plt.semilogx(w,np.angle(h,deg=True),'r')
            plt.title('Fase de un filtro Chebyshev Tipo II')
            plt.xlabel('Frequencia [Hz]')
            plt.ylabel('Fase [Grados]')
            plt.margins(0, 0.1)
            plt.grid(which='both', axis='both')
            plt.tight_layout(True)
            
            plt.savefig('img.png')
    #--------------------------------------------------------------
    
    def Bot_Butt():
        ang=varOpcion_1.get()
        F_tipo=varOpcion.get()
        N=int(Nro.get())
        fs=int(frecs.get())
        fcI=int(freccI.get())
        fcS=int(freccS.get())
        
        Butterworth(N,fcI,fcS,F_tipo,fs,ang)
        my_img=ImageTk.PhotoImage(Image.open("img.png"))
        mylabel=Label(Imagen,image=my_img)
        mylabel.grid(row=0,column=0)
        
    
    def Bot_Cheby1():
        ang=varOpcion_1.get()
        F_tipo=varOpcion.get()
        N=int(Nro.get())
        fs=int(frecs.get())
        fcI=int(freccI.get())
        fcS=int(freccS.get())
        rp=int(ripp.get())
        
        Cebyshev_1(N,rp,fcI,fcS,F_tipo,fs,ang)
        my_img=ImageTk.PhotoImage(Image.open("img.png"))
        mylabel=Label(Imagen,image=my_img)
        mylabel.grid(row=0,column=0)
    
    def Bot_Cheby2():
        ang=varOpcion_1.get()
        F_tipo=varOpcion.get()
        N=int(Nro.get())
        fs=int(frecs.get())
        fcI=int(freccI.get())
        fcS=int(freccS.get())
        rp=int(ripp.get())
        
        Cebyshev_2(N,rp,fcI,fcS,F_tipo,fs,ang)
        my_img=ImageTk.PhotoImage(Image.open("img.png"))
        mylabel=Label(Imagen,image=my_img)
        mylabel.grid(row=0,column=0)
    #--------------------------------------------------------------    
    #--------------------------GUI---------------------------------
    #--------------------------------------------------------------
    
    
      
    
    
    
    
    #-------------------------Estancia 1---------------------------
    
    varOpcion=IntVar()
    
    cuadro_1=LabelFrame(Raiz,text="Tipo de Respuesta",font=("Times New Roma",10,"bold"))
    cuadro_1.grid(row=1,column=0,pady=1,padx=3)
    cuadro_1.config(bg="#F4F4F4",
                    relief="ridge",bd="3")
    
    
    
    Radiobutton(cuadro_1,text="Pasa bajo",variable=varOpcion, value=0).grid(row=1,column=0,sticky="w")
    Radiobutton(cuadro_1,text="Pasa alto",variable=varOpcion, value=1).grid(row=2,column=0,sticky="w")
    Radiobutton(cuadro_1,text="Pasa banda",variable=varOpcion, value=2).grid(row=3,column=0,sticky="w")
    
    #-------------------------Estancia 2---------------------------
    
    varOpcion_1=IntVar()
    
    
    cuadro_1_2=LabelFrame(Raiz,text="Tipo de Filtro",
                      font=("Times New Roma",10,"bold"),padx=23,pady=10)
    cuadro_1_2.grid(row=1,column=1,pady=1)
    cuadro_1_2.config(bg="#F4F4F4",
                    relief="ridge",bd="3")
    
    
    Radiobutton(cuadro_1_2,text="Analogico",variable=varOpcion_1, value=1).grid(row=2,column=0,sticky="w",pady=2)
    Radiobutton(cuadro_1_2,text="Digital",variable=varOpcion_1, value=0).grid(row=1,column=0,sticky="w",pady=1)
    
    #-------------------------Estancia 3---------------------------
    
    Nro=StringVar()
    
    cuadro_2=LabelFrame(Raiz,text="N° de orden del Filtro",
                      font=("Times New Roma",10,"bold"))
    cuadro_2.grid(row=1,column=2,pady=1)
    cuadro_2.config(bg="#F4F4F4",
                    relief="ridge",bd="3")
    
    
    etiqueta21=Label(cuadro_2,text="Orden: ",
                        font=("Times New Roma",10)).grid(row=1,column=0,padx=51,pady=27)
    cuadroTexto21=Entry(cuadro_2,textvariable=Nro).grid(row=1,column=1,padx=5)
    
    
    #-------------------------Estancia 4---------------------------
    
    cuadro_3=LabelFrame(Raiz,text="Tipo de Filtro IRR",
                      font=("Times New Roma",10,"bold"))
    cuadro_3.grid(row=2,column=0,columnspan=2,padx=3,pady=2)
    cuadro_3.config(bg="#F4F4F4",
                    relief="ridge",bd="3")
    
    
    botonButter=Button(cuadro_3,text="Diseñar Filtro Butterworth", command=Bot_Butt)
    botonButter.grid(row=1,column=0,columnspan=2,pady=4,padx=59)
    
    botonCheby1=Button(cuadro_3,text="Diseñar Filtro Chebyshev Tipo I", command=Bot_Cheby1)
    botonCheby1.grid(row=2,column=0,padx=25,pady=5)
    
    botonCheby2=Button(cuadro_3,text="Diseñar Filtro Chebyshev Tipo II",command=Bot_Cheby2)
    botonCheby2.grid(row=3,column=0,padx=25,pady=4)
    
    #-------------------------Estancia 5---------------------------
    
    frecs=StringVar()
    freccI=StringVar()
    freccS=StringVar()
    ripp=StringVar()
    
    cuadro_4=LabelFrame(Raiz,text="Especificaciones del Filtro",
                      font=("Times New Roma",10,"bold"))
    cuadro_4.grid(row=2,column=2,pady=2)
    cuadro_4.config(bg="#F4F4F4",
                    relief="ridge",bd="3")
    
    #----------------------------------------------------------------
    
    #------------------------------------------------------------------------------------
    
    #------------------------------------------------------------------------------------
    etiqueta41=Label(cuadro_4,text="Frec. de Muestreo: ",
                        font=("Times New Roma",10)).grid(row=1,column=0,sticky="w",padx=2,pady=2)
    cuadroTexto41=Entry(cuadro_4,textvariable=frecs).grid(row=1,column=1,padx=5)
    #------------------------------------------------------------------------------------
    etiqueta42=Label(cuadro_4,text="Frec. de Corte Inferior: ",
                        font=("Times New Roma",10)).grid(row=2,column=0,sticky="w",padx=2,pady=2)
    cuadroTexto42=Entry(cuadro_4,textvariable=freccI).grid(row=2,column=1)
    #------------------------------------------------------------------------------------
    etiqueta43=Label(cuadro_4,text="Frec. de Corte Superior: ",
                        font=("Times New Roma",10)).grid(row=3,column=0,sticky="w",padx=2,pady=2)
    cuadroTexto43=Entry(cuadro_4,textvariable=freccS).grid(row=3,column=1)
    #------------------------------------------------------------------------------------
    etiqueta44=Label(cuadro_4,text="Maximum Ripple: ",
                        font=("Times New Roma",10)).grid(row=4,column=0,sticky="w",padx=2,pady=2)
    cuadroTexto44=Entry(cuadro_4,textvariable=ripp).grid(row=4,column=1)
    #------------------------------------------------------------------------------------
    #------------------------------------------------------------------------------------
    
    def back():
        try:
            Raiz.destroy()
        except:
            pass
    
    Back=Frame(Raiz)
    Back.grid(row=3,column=0,columnspan=3)
    B=Button(Back,text="<< Regresar a la ventana de Opciones",command=back)
    B.grid(row=0,column=0)
    
    
    
    Raiz.mainloop()

#----------------------------------------------------------------

def Filtro_FIR():
    Raiz=Toplevel()
    Raiz.title("Analisis de Filtros FIR")
    Raiz.geometry("643x644")
    Raiz.resizable(0,0)
    Raiz.config(bg="#F4F4F4")
    
    #----------------------Estancia 0-------------------------------
    
    Imagen=LabelFrame(Raiz,text="Grafica FIR",
                font=("Times New Roma",12,"bold")) #,padx=200,pady=150
    
    Imagen.grid(row=0,column=0,columnspan=3)
    
    my_img=ImageTk.PhotoImage(Image.open("FIR_img_Filter.png"))
    mylabel=Label(Imagen,image=my_img)
    mylabel.grid(row=0,column=0)
    
    #----------------------------------------------------
    
    def Rectangular(riz,fcI,fcS,fs,N,F_tipo):
        
        if F_tipo==0:
            wcI=(fcI/fs)*2*np.pi
            wcS=0
        elif F_tipo==1:
            wcS=(fcS/fs)*2*np.pi
            wcI=0
        elif F_tipo==2:
            wcI=(fcI/fs)*2*np.pi
            wcS=(fcS/fs)*2*np.pi
            
            
        
        riz_dB=20*np.log10(riz)

        M=N-1
        wc=(wcI+wcS)/2
        n=np.arange(0,N)
        
        hid=np.sin(wc*(n-M/2))/(np.pi*(n-M/2))
        
        window=np.ones(N)
        h=window*hid
        w=np.linspace(0,2*np.pi,2048)
        H=np.abs(np.fft.fft(h,2048))
        plt.figure(figsize=(6,5))
        plt.semilogx(w[0:1024],20*np.log10(H[0:1024]))
        plt.title("Rectangular")
        plt.ylabel("Amplitude")
        plt.xlabel("Frecuencia")
        
        plt.savefig("img2.png")
        
    def Barlett(riz,fcI,fcS,fs,N,F_tipo):
        if F_tipo==0:
            wcI=(fcI/fs)*2*np.pi
            wcS=0
        elif F_tipo==1:
            wcS=(fcS/fs)*2*np.pi
            wcI=0
        elif F_tipo==2:
            wcI=(fcI/fs)*2*np.pi
            wcS=(fcS/fs)*2*np.pi
        riz_dB=20*np.log10(riz)

        M=N-1
        wc=(wcI+wcS)/2
        n=np.arange(0,N)
        
        hid=np.sin(wc*(n-M/2))/(np.pi*(n-M/2))
        window=np.zeros(N)
        window[0:int(M/2)+1]=2*n[0:int(M/2)+1]/M
        window[int(M/2)+1:-1]=2-2*n[int(M/2)+1:-1]/M
        
        h=window*hid
        w=np.linspace(0,2*np.pi,2048)
        H=np.abs(np.fft.fft(h,2048))
        plt.figure(figsize=(6,5))
        plt.semilogx(w[0:1024],20*np.log10(H[0:1024]))
        plt.title("Barlet")
        plt.ylabel("Amplitude")
        plt.xlabel("Frecuencia")
        
    def Hann(riz,fcI,fcS,fs,N,F_tipo):
        if F_tipo==0:
            wcI=(fcI/fs)*2*np.pi
            wcS=0
        elif F_tipo==1:
            wcS=(fcS/fs)*2*np.pi
            wcI=0
        elif F_tipo==2:
            wcI=(fcI/fs)*2*np.pi
            wcS=(fcS/fs)*2*np.pi
        riz_dB=20*np.log10(riz)

        M=N-1
        wc=(wcI+wcS)/2
        n=np.arange(0,N)
        
        hid=np.sin(wc*(n-M/2))/(np.pi*(n-M/2))
        window=0.5-0.5*np.cos(2*np.pi*n/M)
        h=window*hid
        w=np.linspace(0,2*np.pi,2048)
        H=np.abs(np.fft.fft(h,2048))
        plt.figure(figsize=(6,5))
        plt.semilogx(w[0:1024],20*np.log10(H[0:1024]))
        plt.title("Hann")
        plt.ylabel("Amplitude")
        plt.xlabel("Frecuencia")
        
    def Hamming(riz,fcI,fcS,fs,N,F_tipo):
        if F_tipo==0:
            wcI=(fcI/fs)*2*np.pi
            wcS=0
        elif F_tipo==1:
            wcS=(fcS/fs)*2*np.pi
            wcI=0
        elif F_tipo==2:
            wcI=(fcI/fs)*2*np.pi
            wcS=(fcS/fs)*2*np.pi
        riz_dB=20*np.log10(riz)

        M=N-1
        wc=(wcI+wcS)/2
        n=np.arange(0,N)
        
        hid=np.sin(wc*(n-M/2))/(np.pi*(n-M/2))
        window=0.54-0.46*np.cos(2*np.pi*n/M)
        h=window*hid
        w=np.linspace(0,2*np.pi,2048)
        H=np.abs(np.fft.fft(h,2048))
        plt.figure(figsize=(6,5))
        plt.semilogx(w[0:1024],20*np.log10(H[0:1024]))
        plt.title("hamming")
        plt.ylabel("Amplitude")
        plt.xlabel("Frecuencia")
        
    def Blackman(riz,fcI,fcS,fs,N,F_tipo):
        if F_tipo==0:
            wcI=(fcI/fs)*2*np.pi
            wcS=0
        elif F_tipo==1:
            wcS=(fcS/fs)*2*np.pi
            wcI=0
        elif F_tipo==2:
            wcI=(fcI/fs)*2*np.pi
            wcS=(fcS/fs)*2*np.pi
        riz_dB=20*np.log10(riz)

        M=N-1
        wc=(wcI+wcS)/2
        n=np.arange(0,N)
        
        hid=np.sin(wc*(n-M/2))/(np.pi*(n-M/2))
        window=0.42-0.5*np.cos(2*np.pi*n/M)+0.08*np.cos(4*np.pi*n/M)
        h=window*hid
        w=np.linspace(0,2*np.pi,2048)
        H=np.abs(np.fft.fft(h,2048))
        plt.figure(figsize=(6,5))
        plt.semilogx(w[0:1024],20*np.log10(H[0:1024]))
        plt.title("Blackman")
        plt.ylabel("Amplitude")
        plt.xlabel("Frecuencia")
        
    def Kaise():
        m
    
    #------------------------------------------------------
    def Bot_Rec():
        #ang=varOpcion_1.get()
        F_tipo=varOpcion.get()
        N=int(Nro.get())
        riz=float(ripp.get())
        fs=int(frecs.get())
        fcI=int(freccI.get())
        fcS=int(freccS.get())
        
        #Butterworth(N,fcI,fcS,F_tipo,fs,ang)
        
        Rectangular(riz,fcI,fcS,fs,N,F_tipo)
        
        my_img=ImageTk.PhotoImage(Image.open("img2.png"))
        mylabel=Label(Imagen,image=my_img)
        mylabel.grid(row=0,column=0)
        
    
    def Bot_Ban():
        #ang=varOpcion_1.get()
        F_tipo=varOpcion.get()
        N=int(Nro.get())
        riz=float(ripp.get())
        fs=int(frecs.get())
        fcI=int(freccI.get())
        fcS=int(freccS.get())
        
        Barlett(riz,fcI,fcS,fs,N,F_tipo)
        
        my_img=ImageTk.PhotoImage(Image.open("img2.png"))
        mylabel=Label(Imagen,image=my_img)
        mylabel.grid(row=0,column=0)
    
    def Bot_Han():
        ang=varOpcion_1.get()
        F_tipo=varOpcion.get()
        N=int(Nro.get())
        riz=float(ripp.get())
        fs=int(frecs.get())
        fcI=int(freccI.get())
        fcS=int(freccS.get())
        
        
        Hann(riz,fcI,fcS,fs,N,F_tipo)
        my_img=ImageTk.PhotoImage(Image.open("img2.png"))
        mylabel=Label(Imagen,image=my_img)
        mylabel.grid(row=0,column=0)
        
    def Bot_Ham():
        ang=varOpcion_1.get()
        F_tipo=varOpcion.get()
        N=int(Nro.get())
        riz=float(ripp.get())
        fs=int(frecs.get())
        fcI=int(freccI.get())
        fcS=int(freccS.get())
        
        
        Hamming(riz,fcI,fcS,fs,N,F_tipo)
        
        my_img=ImageTk.PhotoImage(Image.open("img2.png"))
        mylabel=Label(Imagen,image=my_img)
        mylabel.grid(row=0,column=0)
        
    def Bot_Bla():
        ang=varOpcion_1.get()
        F_tipo=varOpcion.get()
        N=int(Nro.get())
        riz=float(ripp.get())
        fs=int(frecs.get())
        fcI=int(freccI.get())
        fcS=int(freccS.get())
        
        
        Blackman(riz,fcI,fcS,fs,N,F_tipo)
        
        my_img=ImageTk.PhotoImage(Image.open("img2.png"))
        mylabel=Label(Imagen,image=my_img)
        mylabel.grid(row=0,column=0)
        
    def Bot_Kai():
        m
    #--------------------------------------------------------------    
    #--------------------------GUI---------------------------------
    #--------------------------------------------------------------
    
    
      
    
    
    
    
    #-------------------------Estancia 1---------------------------
    
    varOpcion=IntVar()
    
    cuadro_1=LabelFrame(Raiz,text="Tipo de Respuesta",font=("Times New Roma",10,"bold"),padx=38)
    cuadro_1.grid(row=1,column=0,pady=1,padx=3)
    cuadro_1.config(bg="#F4F4F4",
                    relief="ridge",bd="3")
    
    
    
    Radiobutton(cuadro_1,text="Pasa bajo",variable=varOpcion, value=0).grid(row=1,column=0,sticky="w")
    Radiobutton(cuadro_1,text="Pasa alto",variable=varOpcion, value=1).grid(row=2,column=0,sticky="w")
    Radiobutton(cuadro_1,text="Pasa banda",variable=varOpcion, value=2).grid(row=3,column=0,sticky="w")
    
    #-------------------------Estancia 2---------------------------
    
    varOpcion_1=IntVar()
    
    
    cuadro_1_2=LabelFrame(Raiz,text="Tipo de Filtro",
                      font=("Times New Roma",10,"bold"),padx=40,pady=10)
    cuadro_1_2.grid(row=1,column=1,pady=1)
    cuadro_1_2.config(bg="#F4F4F4",
                    relief="ridge",bd="3")
    
    
    Radiobutton(cuadro_1_2,text="Analogico",variable=varOpcion_1, value=1).grid(row=2,column=0,sticky="w",pady=2)
    Radiobutton(cuadro_1_2,text="Digital",variable=varOpcion_1, value=0).grid(row=1,column=0,sticky="w",pady=1)
    
    #-------------------------Estancia 3---------------------------
    
    Nro=StringVar()
    
    cuadro_2=LabelFrame(Raiz,text="N° de orden del Filtro",
                      font=("Times New Roma",10,"bold"))
    cuadro_2.grid(row=1,column=2,pady=1)
    cuadro_2.config(bg="#F4F4F4",
                    relief="ridge",bd="3")
    
    
    etiqueta21=Label(cuadro_2,text="Orden: ",
                        font=("Times New Roma",10)).grid(row=1,column=0,padx=51,pady=27)
    cuadroTexto21=Entry(cuadro_2,textvariable=Nro).grid(row=1,column=1,padx=5)
    
    
    #-------------------------Estancia 4---------------------------
    
    cuadro_3=LabelFrame(Raiz,text="Tipo de Filtro FIR",
                      font=("Times New Roma",10,"bold"))
    cuadro_3.grid(row=2,column=0,columnspan=2,padx=3,pady=2)
    cuadro_3.config(bg="#F4F4F4",
                    relief="ridge",bd="3")
    
    
    botonButter=Button(cuadro_3,text="Filtro Ventana Rectangular", command=Bot_Rec,width=22)
    botonButter.grid(row=0,column=0,pady=4,padx=2)
    
    botonCheby1=Button(cuadro_3,text="Filtro Ventana Banlett", command=Bot_Ban,width=22)
    botonCheby1.grid(row=1,column=0,padx=2,pady=4)
    
    botonCheby2=Button(cuadro_3,text="Filtro Ventana Hann",command=Bot_Han,width=22)
    botonCheby2.grid(row=2,column=0,padx=2,pady=4)
    
    botonButter=Button(cuadro_3,text="Filtro Ventana Hamming", command=Bot_Ham,width=22)
    botonButter.grid(row=0,column=1,pady=4,padx=2)
    
    botonCheby1=Button(cuadro_3,text="Filtro Ventana Blackman", command=Bot_Bla,width=22)
    botonCheby1.grid(row=1,column=1,padx=2,pady=4)
    
    botonCheby2=Button(cuadro_3,text="Filtro Ventana Kaise",command=Bot_Kai,width=22)
    botonCheby2.grid(row=2,column=1,padx=2,pady=4)
    
    #-------------------------Estancia 5---------------------------
    
    frecs=StringVar()
    freccI=StringVar()
    freccS=StringVar()
    ripp=StringVar()
    
    cuadro_4=LabelFrame(Raiz,text="Especificaciones del Filtro",
                      font=("Times New Roma",10,"bold"))
    cuadro_4.grid(row=2,column=2,pady=2)
    cuadro_4.config(bg="#F4F4F4",
                    relief="ridge",bd="3")
    
    #----------------------------------------------------------------
    
    #------------------------------------------------------------------------------------
    
    #------------------------------------------------------------------------------------
    etiqueta41=Label(cuadro_4,text="Frec. de Muestreo: ",
                        font=("Times New Roma",10)).grid(row=1,column=0,sticky="w",padx=2,pady=2)
    cuadroTexto41=Entry(cuadro_4,textvariable=frecs).grid(row=1,column=1,padx=5)
    #------------------------------------------------------------------------------------
    etiqueta42=Label(cuadro_4,text="Frec. de Corte Inferior: ",
                        font=("Times New Roma",10)).grid(row=2,column=0,sticky="w",padx=2,pady=2)
    cuadroTexto42=Entry(cuadro_4,textvariable=freccI).grid(row=2,column=1)
    #------------------------------------------------------------------------------------
    etiqueta43=Label(cuadro_4,text="Frec. de Corte Superior: ",
                        font=("Times New Roma",10)).grid(row=3,column=0,sticky="w",padx=2,pady=2)
    cuadroTexto43=Entry(cuadro_4,textvariable=freccS).grid(row=3,column=1)
    #------------------------------------------------------------------------------------
    etiqueta44=Label(cuadro_4,text="Maximum Ripple: ",
                        font=("Times New Roma",10)).grid(row=4,column=0,sticky="w",padx=2,pady=2)
    cuadroTexto44=Entry(cuadro_4,textvariable=ripp).grid(row=4,column=1)
    #------------------------------------------------------------------------------------
    #------------------------------------------------------------------------------------
    
    def back():
        try:
            Raiz.destroy()
        except:
            pass

    
    Back=Frame(Raiz)
    Back.grid(row=3,column=0,columnspan=3)
    B=Button(Back,text="<< Regresar a la ventana de Opciones",command=back)
    B.grid(row=0,column=0)
    
    
    Raiz.mainloop()
#-----------------------------------------------------------

def bot1():
    Filtro_IRR()

def bot2():
    Filtro_FIR()
    
ventana=Tk()
ventana.title("Opciones")
ventana.geometry("265x134")
    
C=LabelFrame(ventana,text="Elegir Tipo de analisis",padx=25,pady=25,font=("Times New Roma",12,"bold"))
C.grid(row=0,column=0,padx=15,pady=8)
    
boton1=Button(C,text="Filtros IIR", command=bot1,width=10,height=2)
boton1.grid(row=0,column=0,padx=6)
    
boton2=Button(C,text="Filtros FIR", command=bot2,width=10,height=2)
boton2.grid(row=0,column=1,padx=6)
ventana.mainloop()
#--------------------Referencias------------------------
    
"https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.butter.html"
"https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.cheby1.html"    
"https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.cheby2.html" 
"https://docs.python.org/3.3/library/tkinter.html#the-packer"
"https://www.youtube.com/watch?v=YfYUOUGMaXU&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=50"