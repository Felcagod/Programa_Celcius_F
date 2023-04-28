from email.policy import default
from http.client import TOO_MANY_REQUESTS
from textwrap import wrap
from tkinter import HORIZONTAL, Scrollbar, scrolledtext
from turtle import update
import PySimpleGUI as sg 

def tela_inicial():

    sg.theme('Black')

    layout =  [
        [sg.Canvas(background_color='White',pad=None, size=(400,2))],
        [sg.Text('   Selecione uma temperatura', font=('Arial',20),justification='center',text_color='Yellow')],
        [sg.Text('')],
        [sg.Text('           '),sg.Checkbox('Celcius',key='cel',font=('Arial',16)),sg.Text(''),sg.Checkbox('Fahrenheit',key='fahrenheit',font=('Arial',16))],
        [sg.Text('')],
        [sg.Text('                     '),sg.Button('Continuar',font=('Arial',14)),sg.Button('Exit',button_color=('White','Red'),font=('Arial',14))]
    ]
    return sg.Window('main window', layout=layout, finalize=True,size=(400,200),no_titlebar = True)

def tela_celcius_fahrenheit():
    
    sg.theme('Black')

    layout = [ 
        
        [sg.Canvas(background_color='White',pad=None, size=(400,2))],
        [sg.Text(' Informe a temperatura',font=('Arial',27),justification='center',text_color='Yellow')],
        [sg.Text('           '),sg.Input(key='C',size=(4,2),font=('Arial',30)),sg.Text('=',font=('Arial',40)),sg.Output(size=(5,2),font=('Arial',30),sbar_background_color = 'Black',expand_y = False,expand_x=False)],
        [sg.Text('        C°',font=('Arial',30)),sg.Text('                  '),sg.Text(' F°',font=('Arial',30))],
        [sg.Text('')],
        [sg.Text('              '),sg.Button('Voltar',font=('Arial',14)),sg.Button('Exit',button_color=('White','Red'),font=('Arial',14)),sg.Button('Resultado',key='resu',font=('Arial',14))]
    ]
    return sg.Window('Main second window',layout=layout, size=(400,290),finalize=True,no_titlebar = True)

def tela_fahrenheit_celcius():

    sg.theme('Black')

    layout = [
        [sg.Canvas(background_color='White',pad=None, size=(400,2))],
        [sg.Text(' Informe a temperatura',font=('Arial',27),justification='center',text_color='Yellow')],
        [sg.Text('           '),sg.Input(key='F',size=(4,2),font=('Arial',30)),sg.Text('=',font=('Arial',40)),sg.Output(size=(5,2),font=('Arial',30),sbar_background_color = 'Black',expand_y = False,expand_x=False)],
        [sg.Text('        F°',font=('Arial',30)),sg.Text('                  '),sg.Text(' C°',font=('Arial',30))],
        [sg.Text('')],
        [sg.Text('              '),sg.Button('Voltar',font=('Arial',14)),sg.Button('Exit',button_color=('White','Red'),font=('Arial',14)),sg.Button('Resultado',key='resu',font=('Arial',14))]
    ]
    return sg.Window('Main',layout=layout, size=(400,290),finalize=True,no_titlebar = True)


janela1, janela2, janela3 = tela_inicial(), None, None 

#criando looping de eventos 

while True:

    window, events, values = sg.read_all_windows() 

    #fechando windows


    if window == janela1 and events == sg.WIN_CLOSED:
        break 
    if window == janela2 and events == sg.WIN_CLOSED:
        break 
    if window == janela3 and events == sg.WIN_CLOSED:
        break 
    if window == janela1 and events == 'Exit':
        break  
    if window == janela2 and events == 'Exit':
        break 
    if window == janela3 and events == 'Exit':
        break 


    #abrindo janelas 
    
    #error window
    if window == janela1 and events == 'Continuar':
        if values['cel'] == True and values['fahrenheit'] == True:
            sg.popup_no_border('As duas temperaturas estão marcadas\n                  Tente novamente!',button_color=('White','Red'),font=('Arial',17),auto_close = True, auto_close_duration=5)
        if values['cel'] == False and values['fahrenheit'] == False:
            sg.popup_no_border('Nenhuma das temperaturas estão marcadas\n                     Tente novamente!',button_color=('White','Red'),font=('Arial',17),auto_close = True, auto_close_duration=5)
        
    #verificando valores 

        if values['cel'] == True and values['fahrenheit'] == False:
            janela2 = tela_celcius_fahrenheit() 
            janela1.hide() 
    
        if values['cel'] == False and values['fahrenheit'] == True:
            janela3 = tela_fahrenheit_celcius() 
            janela1.hide() 

    #voltando janelas 
    if window == janela2 and events == 'Voltar':
        janela1.un_hide()
        janela2.hide()
        

    if window == janela3 and events == 'Voltar':
        janela1.un_hide() 
        janela3.hide()
        

    #processamento dos valores de Fahrenheit -> Celcius or Celcius -> Fahrenheit

     #celcius -> fahrenheit
    if window == janela2 and events == 'resu':
        cel = values['C']
        C = float(cel)
        F = C*1.8+32

        print("%.2f"%F)

    if window == janela3 and events == 'resu':
        fah = values['F']
        F = float(fah)

        C=(F-32)/1.8

        print('%.2f'%C)


     

 
    

















