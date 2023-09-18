import tkinter as tk
from tkinter import Tk, Label, Entry, Button, END, Text
from tkinter.ttk import Combobox
from googletrans import Translator
import speech_recognition as sr
import threading


def translate():
    current = combobox.get()
    if current == 'Ru':
        text = entry1.get(0, END)
        translator = Translator(service_urls=['translate.googleapis.com'])
        translated_label.config(text=str(translator.translate(text, dest='en').text))
    else:
        text = entry1.get(0)
        translator = Translator(service_urls=['translate.googleapis.com'])
        translated_label.config(text=str(translator.translate(text, dest='ru').text))


def voice_input():
    current = combobox.get()
    if current == "Ru":
        def recognize_russian():
            r = sr.Recognizer()
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)

            try:
                voice = r.recognize_google(audio, language="ru")
                entry1.delete(0, END)
                entry1.insert(0, voice)
            except sr.UnknownValueError:
                return "Try again"

        thread = threading.Thread(target=recognize_russian)
        thread.start()
    else:
        def recognize_english():
            r = sr.Recognizer()
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)

            try:
                voice = r.recognize_google(audio, language="en")
                entry1.delete(0, END)
                entry1.insert(0, voice)
            except sr.UnknownValueError:
                return "Try again"

        thread = threading.Thread(target=recognize_english)
        thread.start()


def combobox_select(event):
    selected_item = event.widget.get()
    print(f"Выберите язык: {selected_item}")


def combobox_select2(event):
    selected_item = event.widget.get()
    print(f"Выберите язык: {selected_item}")


def swap_buttons():
    btn1_row, btn1_col = combobox.grid_info()['row'], combobox.grid_info()['column']
    btn2_row, btn2_col = combobox2.grid_info()['row'], combobox2.grid_info()['column']

    combobox.grid(row=btn2_row, column=btn2_col)
    combobox2.grid(row=btn1_row, column=btn1_col)


window = Tk()
window.title("Audio Translator")

window.geometry("650x300")
window['bg'] = '#7d33ff'
window.resizable(width=True, height=True)

combobox = Combobox(window, values=["Ru", "En"])
combobox.grid(row=0, column=0, pady=10)
combobox.bind("<<ComboboxSelected>>", combobox_select)

switch_btn = Button(window, text="<----->", background='blue', command=swap_buttons)
switch_btn.grid(row=0, column=1, pady=10)

combobox2 = Combobox(window, values=["En", "Ru"])
combobox2.grid(row=0, column=2, pady=10)
combobox2.bind("<<ComboboxSelected>>", combobox_select2)

entry1 = Text(window, width=40, height=5)
entry1.grid(row=1, column=0, columnspan=3, pady=20, padx=30)

button1 = Button(window, text="Перевести", width=30, height=2, command=translate)
button1.grid(row=2, column=2, padx=45)

button2 = Button(window, text="Голос    )))", width=30, height=2, command=voice_input)
button2.grid(row=2, column=0, padx=45)

translated_label = tk.Label(window, text="", wraplength=400, font='Arial 14 bold', background='#7d33ff')
translated_label.grid(row=3, column=0, columnspan=3, pady=20)

window.mainloop()
