import PySimpleGUI as sg
from pygame import mixer
from time import sleep
from smelting import get_smelting_cost


def show_alert():
    popup = sg.popup_timed(f'O preço de fundição hoje é de {atual}', auto_close_duration=5)
    if popup == 'OK':
        return False
    return True


    

# Cria a janela com um botão "Activate"
layout = [[sg.Text('Smelting today', font=24)],
          [sg.Button('Activate', key='Act')]]
window = sg.Window('Smelting Calculator', layout)

window.set_icon('smpic.ico')
atual = get_smelting_cost()
memo_price = []
memo_price.append(atual)
is_minimized = False

# Loop principal da aplicação
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        
        break

    if event == 'Act':
        # Minimiza a janela na área de notificação
        window.minimize()
        is_minimized = True

    while is_minimized:
        atual = get_smelting_cost()
        if atual < memo_price[-1]:
        
            mixer.init()
            mixer.music.load("Calling.mp3")
            mixer.music.play()
            should_continue = show_alert()
            sleep(10)
            memo_price.append(atual)
            print(memo_price)
            if len(memo_price) > 3:
                memo_price.pop(0)
            if not should_continue:
                    break
        
            
        
    
window.close()
