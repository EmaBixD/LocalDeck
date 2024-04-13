from flask import Flask, render_template, request
import pyautogui
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/button_clicked', methods=['POST'])
def button_clicked():
    data = request.get_json()
    button_number = data.get('buttonNumber')

    if not button_number or button_number < 1 or button_number > 10:
        return '', 400  # Bad Request

    if button_number == 1:
        perform_control_a()
    elif button_number == 2:
        perform_control_c()
    elif button_number == 3:
        perform_control_v()
    elif button_number == 4:
        perform_win_tab()
    elif button_number == 5:
        open_edge_browser()
    elif button_number == 6:
        open_fortnite()
    elif button_number == 7:
        perform_win_d()
    elif button_number == 8:
        perform_alt_f4()
    elif button_number == 9 or button_number == 10:
        pass  # No action for buttons 9 and 10

    return '', 204

def perform_control_a():
    try:
        pyautogui.hotkey('ctrl', 'a')
    except Exception as e:
        print(f"Error performing control-a: {e}")

def perform_control_c():
    try:
        pyautogui.hotkey('ctrl', 'c')
    except Exception as e:
        print(f"Error performing control-c: {e}")

def perform_control_v():
    try:
        pyautogui.hotkey('ctrl', 'v')
    except Exception as e:
        print(f"Error performing control-v: {e}")

def perform_win
