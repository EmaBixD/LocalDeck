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
    button_number = data['buttonNumber']
    if button_number == 1:
        print("1")
        pyautogui.hotkey('ctrl', 'a')
    elif button_number == 2:
        print("2")
        pyautogui.hotkey('ctrl', 'c')
    elif button_number == 3:
        print("3")
        pyautogui.hotkey('ctrl', 'v')
    elif button_number == 4:
        print("4")
        pyautogui.hotkey('win', 'tab')
    elif button_number == 5:
        print("5")
        subprocess.Popen([r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"])
    elif button_number == 6:
        print("6")
        subprocess.Popen([r"D:\Epic Games\Fortnite\FortniteGame\Binaries\Win64\FortniteClient-Win64-Shipping_EAC_EOS.exe"])
    elif button_number == 7:
        print("7")
        pyautogui.hotkey('win', 'd')
    elif button_number == 8:
        print("8")
        pyautogui.hotkey('alt', 'F4')
    elif button_number == 9:
        print("9")
    elif button_number == 10:
        print("10")
    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
