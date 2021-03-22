import PySimpleGUI as sg
import os
import random
import time
from logic import get_winner

def main():
    sg.LOOK_AND_FEEL_TABLE['MyColorTheme'] = {'BACKGROUND': '#ffffff',
                                          'TEXT': '#000000',
                                          'INPUT': '#ffffff',
                                          'TEXT_INPUT': '#000000',
                                          'SCROLL': '#86A8FF',
                                          'BUTTON': ('#FFFFFF', '#5079D3'),
                                          'PROGRESS': sg.DEFAULT_PROGRESS_BAR_COLOR,
                                          'BORDER': 0, 'SLIDER_DEPTH': 0,
                                          'PROGRESS_DEPTH': 0,
                                          'ACCENT1': '#FF0266',
                                          'ACCENT2': '#FF5C93',
                                          'ACCENT3': '#C5003C'}
    sg.theme('MyColorTheme')

    layout = [
        [sg.Combo(['easy', 'hard'], default_value='easy', key='difficulty')],
        [sg.Text('Player:', font=("Helvetica", 15)), sg.Text('0', font=("Arial", 15), size=(10,1), key='PS')],
        [sg.Text('Computer:', font=("Helvetica", 15)), sg.Text('0', font=("Arial", 15), size=(10,1), key='CS')],
        [sg.Image("blank.png"), sg.Image("computer.png", key="computer"), sg.Image("blank.png")],
        [sg.ReadFormButton('', image_filename="rock.png", key='Rock'),
         sg.ReadFormButton('', image_filename="paper.png", key='Paper'),
         sg.ReadFormButton('', image_filename="scissors.PNG", key='Scissors')]
    ]

    window = sg.Window('Rock, Paper, Scissors!', layout)

    while True:
        button, event = window.read()

        event_list = ['rock', 'paper', 'scissors']

        if event == sg.WIN_CLOSED:
            break

        player_action = 0
        computer_action = 0

        if button is 'Rock':
            player_action = 'rock'
        if button is 'Paper':
            player_action = 'paper'
        if button is 'Scissors':
            player_action = 'scissors'

        if player_action != 0:

            if window['difficulty'].get() == 'easy':
                computer_action = event_list[random.randint(0, 2)]

            elif window['difficulty'].get() == 'hard':
                new_list = event_list.copy()

                if player_action == 'rock':
                    new_list.remove('scissors')
                elif player_action == 'paper':
                    new_list.remove('rock')
                else:
                    new_list.remove('paper')

                computer_action = new_list[random.randint(0, 1)]

            if computer_action == 'rock':
                window['computer'].update("rock.png")
            elif computer_action == 'paper':
                window['computer'].update("paper.png")
            else:
                window['computer'].update("scissors.png")

        if computer_action != 0:

            win = get_winner(player_action, computer_action)

            if win == 'tie':
                window['PS'].update(int(window['PS'].get()) + 1)
                window['CS'].update(int(window['CS'].get()) + 1)
            elif win:
                window['PS'].update(int(window['PS'].get()) + 1)
            else:
                window['CS'].update(int(window['CS'].get()) + 1)


if __name__ == "__main__":
    main()