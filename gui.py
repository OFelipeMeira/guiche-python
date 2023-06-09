
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter

import pynput
from pynput.keyboard import Key, Controller, KeyCode
import pymysql

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/home/aa/Downloads/guiche-python-main/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

keyboard = Controller()

def conecta():
    conexao = pymysql.connect(
        user="butterfly@peixe",
        password="Manteigavoadora1",
        host="peixe.mariadb.database.azure.com",
        port=3306,
        database='secretariasenai'
    )
    cursor = conexao.cursor()
    return cursor, conexao

def executaefecha(cursor, conexao):
    cursor.fetchone()
    conexao.commit()
    cursor.close()
    conexao.close()

class Fullscreen_Window:

    def __init__(self):
        self.tk = Tk()
        self.frame = tkinter.Frame(self.tk)
        self.frame.pack()
        self.state = False
        self.tk.bind("<F11>", self.toggle_fullscreen)
        self.tk.bind("<Escape>", self.end_fullscreen)

    def toggle_fullscreen(self, event=None):
        self.state = not self.state  # Just toggling the boolean
        self.tk.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.tk.attributes("-fullscreen", False)
        return "break"

window = Fullscreen_Window()

window.tk.attributes('-fullscreen',True)
window.tk.geometry("1920x1080+0+0")
window.tk.configure(bg = "#FFFFFF")


def presschapeu():
    with keyboard.pressed(Key.shift):
        keyboard.press(pynput.keyboard.KeyCode().from_dead('~'))

def shift(x):
    with keyboard.pressed(Key.shift):
        keyboard.press(x)

def format_nome(event=None):
    text = entry_1.get()[:19]
    new_text = ""


    for index in range(len(text)):
            new_text += text[index]

    entry_1.delete(0, "end")
    entry_1.insert(0, new_text)

def tela2():


    global botoes
    for i in botoes:
        i.place_forget()

    global button_a, button_b, button_c

    button_c = Button(
        text="PREFERENCIAL",
        font=("Gotham Medium", 64 * -1),
        borderwidth=0,
        highlightthickness=0,
        command=lambda: [infos.append(1), infos.append("Preferencial"),button_c.place_forget(), button_a.place_forget(), button_b.place_forget(), tela3(), window.tk.after(2000, lambda: place_tela1())],
        relief="flat"
    )
    button_c.place(
        x=398.0,
        y=243.0,
        width=1123.0,
        height=178.0
    )
    button_a = Button(
        text="GERAL",
        font=("Gotham Medium", 64 * -1),
        borderwidth=0,
        highlightthickness=0,
        command=lambda: [infos.append(0), infos.append("Geral"), button_c.place_forget(), button_a.place_forget(), button_b.place_forget(), tela3(), window.tk.after(2000, lambda: place_tela1())],
        relief="flat"
    )
    button_a.place(
        x=398.0,
        y=451.0,
        width=1123.0,
        height=178.0

    )

    button_b = Button(
        text="MATRICULA",
        font=("Gotham Medium", 64 * -1),
        borderwidth=0,
        highlightthickness=0,
        command=lambda: [infos.append(0), infos.append("Matricula"), button_c.place_forget(), button_a.place_forget(), button_b.place_forget(), tela3(), window.tk.after(2000, lambda: place_tela1())],
        relief="flat"
    )
    button_b.place(
        x=398.0,
        y=659.0,
        width=1123.0,
        height=178.0
    )


canvas = Canvas(
    window.tk,
    bg = "#FFFFFF",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    1920.0,
    124.0,
    fill="#F20505",
    outline="")

canvas.create_rectangle(
    0.0,
    1021.0,
    1920.0,
    1080.0,
    fill="#F20505",
    outline="")

def place_tela1():
    global button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9, button_10, button_11, button_12, button_13, button_14, button_15, button_16, button_17, button_18, button_19, button_20, button_21, button_22, button_23, button_24, button_25, button_26, button_27, button_28, button_29, button_30, button_31, button_32, entry_1, texto1


    texto1.place(
        x=330.0,
        y=188.0
    )
    entry_1.place(
        x=269.0,
        y=286.0,
        width=1408.0,
        height=119.0
    )
    button_1.place(
        x=278.0,
        y=465.0,
        width=104.69134521484375,
        height=93.99015045166016
    )
    button_2.place(
        x=402.4444274902344,
        y=465.0,
        width=104.69136047363281,
        height=93.99015045166016
    )
    button_3.place(
        x=526.888916015625,
        y=465.0,
        width=104.69136047363281,
        height=93.99015045166016
    )

    button_4.place(
        x=651.3333740234375,
        y=465.0,
        width=104.69136047363281,
        height=93.99015045166016
    )

    button_5.place(
        x=775.77783203125,
        y=465.0,
        width=104.69136047363281,
        height=93.99015045166016
    )

    button_6.place(
        x=900.22216796875,
        y=465.0,
        width=104.69134521484375,
        height=93.99015045166016
    )

    button_7.place(
        x=1024.6666259765625,
        y=465.0,
        width=104.69134521484375,
        height=93.99015045166016
    )

    button_8.place(
        x=1149.111083984375,
        y=465.0,
        width=104.69134521484375,
        height=93.99015045166016
    )

    button_9.place(
        x=1273.5555419921875,
        y=465.0,
        width=104.69134521484375,
        height=93.99015045166016
    )

    button_10.place(
        x=1398.0,
        y=465.0,
        width=104.69134521484375,
        height=93.99015045166016
    )

    button_11.place(
        x=1520.4691162109375,
        y=465.0,
        width=122.4691162109375,
        height=93.99015045166016
    )

    button_12.place(
        x=362.9382629394531,
        y=580.2708740234375,
        width=104.69136047363281,
        height=93.99015045166016
    )

    button_13.place(
        x=402.4444274902344,
        y=695.5418701171875,
        width=104.69136047363281,
        height=93.99014282226562
    )

    button_14.place(
        x=526.888916015625,
        y=695.5418701171875,
        width=104.69136047363281,
        height=93.99014282226562
    )

    button_15.place(
        x=651.3333740234375,
        y=695.5418701171875,
        width=104.69136047363281,
        height=93.99014282226562
    )

    button_16.place(
        x=775.77783203125,
        y=695.5418701171875,
        width=104.69136047363281,
        height=93.99014282226562
    )

    button_17.place(
        x=900.22216796875,
        y=695.5418701171875,
        width=104.69134521484375,
        height=93.99014282226562
    )

    button_18.place(
        x=1024.6666259765625,
        y=695.5418701171875,
        width=104.69134521484375,
        height=93.99014282226562
    )

    button_19.place(
        x=1149.111083984375,
        y=695.5418701171875,
        width=104.69134521484375,
        height=93.99014282226562
    )

    button_20.place(
        x=1273.5555419921875,
        y=695.5418701171875,
        width=104.69134521484375,
        height=93.99014282226562
    )

    button_21.place(
        x=1398.0,
        y=695.5418701171875,
        width=104.69134521484375,
        height=93.99014282226562
    )

    button_22.place(
        x=1522.4444580078125,
        y=695.5418701171875,
        width=104.69134521484375,
        height=93.99014282226562
    )

    button_23.place(
        x=487.3827209472656,
        y=580.2708740234375,
        width=104.69136047363281,
        height=93.99015045166016
    )

    button_24.place(
        x=611.8271484375,
        y=580.2708740234375,
        width=104.69136047363281,
        height=93.99015045166016
    )

    button_25.place(
        x=736.2716064453125,
        y=580.2708740234375,
        width=104.69136047363281,
        height=93.99015045166016
    )

    button_26.place(
        x=860.716064453125,
        y=580.2708740234375,
        width=104.69134521484375,
        height=93.99015045166016
    )

    button_27.place(
        x=985.1605224609375,
        y=580.2708740234375,
        width=104.69134521484375,
        height=93.99015045166016
    )

    button_28.place(
        x=1109.6048583984375,
        y=580.2708740234375,
        width=104.69134521484375,
        height=93.99015045166016
    )

    button_29.place(
        x=1234.04931640625,
        y=580.2708740234375,
        width=104.69134521484375,
        height=93.99015045166016
    )

    button_30.place(
        x=1358.4937744140625,
        y=580.2708740234375,
        width=104.69134521484375,
        height=93.99015045166016
    )

    button_31.place(
        x=1484.91357421875,
        y=580.2708740234375,
        width=158.024658203125,
        height=93.99015045166016
    )

    button_32.place(
        x=712.56787109375,
        y=810.812744140625,
        width=582.716064453125,
        height=93.99014282226562
    )


texto1 = tkinter.Label(
    anchor="nw",
    background= "#FFFFFF",
    text="COMO GOSTARIA DE SER CHAMADO?",
    font=("Gotham Bold", 64 * -1)
)



entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font = ("Gotham Medium", 64 * -1)
)


button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0, 
    command=lambda: [shift("q"), format_nome()],
    relief="flat"
)


button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [shift("W"), format_nome()],
    relief="flat"
)


button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [shift("e") , format_nome()],
    relief="flat"
)


button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [shift("r"), format_nome()],
    relief="flat"
)


button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [shift("t"), format_nome()],
    relief="flat"
)


button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [shift("y"), format_nome()],
    relief="flat"
)


button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [shift("u"), format_nome()],
    relief="flat"
)


button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [shift("i"), format_nome()],
    relief="flat"
)


button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [shift("o"), format_nome()],
    relief="flat"
)


button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [shift("p"), format_nome()],
    relief="flat"
)


button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: entry_1.delete(len(entry_1.get())-1),
    relief="flat"
)


button_image_12 = PhotoImage(
    file=relative_to_assets("button_12.png"))
button_12 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [shift("a"), format_nome()],
    relief="flat"
)


button_image_13 = PhotoImage(
    file=relative_to_assets("button_13.png"))
button_13 = Button(
    image=button_image_13,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [shift("z"), format_nome()],
    relief="flat"
)


button_image_14 = PhotoImage(
    file=relative_to_assets("button_14.png"))
button_14 = Button(
    image=button_image_14,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [shift("x"), format_nome()],
    relief="flat"
)


button_image_15 = PhotoImage(
    file=relative_to_assets("button_15.png"))
button_15 = Button(
    image=button_image_15,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [shift("c"), format_nome()],
    relief="flat"
)


button_image_16 = PhotoImage(
    file=relative_to_assets("button_16.png"))
button_16 = Button(
    image=button_image_16,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [shift("v"), format_nome()],
    relief="flat"
)


button_image_17 = PhotoImage(
    file=relative_to_assets("button_17.png"))
button_17 = Button(
    image=button_image_17,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [shift("b"), format_nome()],
    relief="flat"
)


button_image_18 = PhotoImage(
    file=relative_to_assets("button_18.png"))
button_18 = Button(
    image=button_image_18,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [shift("n"), format_nome()],
    relief="flat"
)


button_image_19 = PhotoImage(
    file=relative_to_assets("button_19.png"))
button_19 = Button(
    image=button_image_19,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [shift("m"), format_nome()],
    relief="flat"
)



button_image_20 = PhotoImage(
    file=relative_to_assets("button_20.png"))
button_20 = Button(
    image=button_image_20,
    borderwidth=0,
    highlightthickness=0,
    command= lambda: [presschapeu(), format_nome()],
    relief="flat"
)


button_image_21 = PhotoImage(
    file=relative_to_assets("button_21.png"))
button_21 = Button(
    image=button_image_21,
    borderwidth=0,
    highlightthickness=0,
    command= lambda: [keyboard.press(pynput.keyboard.KeyCode().from_dead('~')), format_nome()],
    relief="flat"
)


button_image_22 = PhotoImage(
    file=relative_to_assets("button_22.png"))
button_22 = Button(
    image=button_image_22,
    borderwidth=0,
    highlightthickness=0,
    command= lambda: [keyboard.press(pynput.keyboard.KeyCode().from_dead('´')), format_nome()],
    relief="flat"
)


button_image_23 = PhotoImage(
    file=relative_to_assets("button_23.png"))
button_23 = Button(
    image=button_image_23,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [shift("s"), format_nome()],
    relief="flat"
)


button_image_24 = PhotoImage(
    file=relative_to_assets("button_24.png"))
button_24 = Button(
    image=button_image_24,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [shift("d"), format_nome()],
    relief="flat"
)


button_image_25 = PhotoImage(
    file=relative_to_assets("button_25.png"))
button_25 = Button(
    image=button_image_25,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [shift("f"), format_nome()],
    relief="flat"
)


button_image_26 = PhotoImage(
    file=relative_to_assets("button_26.png"))
button_26 = Button(
    image=button_image_26,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [shift("g"), format_nome()],
    relief="flat"
)


button_image_27 = PhotoImage(
    file=relative_to_assets("button_27.png"))
button_27 = Button(
    image=button_image_27,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [shift("h"), format_nome()],
    relief="flat"
)


button_image_28 = PhotoImage(
    file=relative_to_assets("button_28.png"))
button_28 = Button(
    image=button_image_28,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [shift("j"), format_nome()],
    relief="flat"
)


button_image_29 = PhotoImage(
    file=relative_to_assets("button_29.png"))
button_29 = Button(
    image=button_image_29,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [shift("k"), format_nome()],
    relief="flat"
)


button_image_30 = PhotoImage(
    file=relative_to_assets("button_30.png"))
button_30 = Button(
    image=button_image_30,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [shift("l"), format_nome()],
    relief="flat"
)

infos = []

button_image_31 = PhotoImage(
    file=relative_to_assets("button_31.png"))
button_31 = Button(
    image=button_image_31,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [infos.clear(), infos.append(entry_1.get()), entry_1.delete(0, 'end'), tela2()],
    relief="flat"
)



button_image_32 = PhotoImage(
    file=relative_to_assets("button_32.png"))
button_32 = Button(
    image=button_image_32,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [keyboard.press(" "), format_nome()],
    relief="flat"
)


image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    1658.0,
    64.0,
    image=image_image_1
)

def tela3():
    texto = tkinter.Label(
        anchor="nw",
        background="#FFFFFF",
        text="SEU NOME/GUICHE SERÁ CHAMADO NA TELA, AGUARDE. \n OBRIGADO!",
        font=("Gotham Medium", 60 * -1)
    )
    texto.place(
        x=50,
        y=450,
    )
    
    window.tk.after(2000, lambda: [texto.place_forget(), inserebanco(infos)])



def inserebanco(infos: list):
    try:
        cursor, conexao = conecta()
        cursor.execute("INSERT INTO secretariasenai.espera(name, preferencial, motivo , ja_atendido) VALUES (%s, %s, %s, %s);", (infos[0], infos[1], infos[2], False))
        executaefecha(cursor, conexao)
    except:
        try: #tentemais
            cursor, conexao = conecta()
            cursor.execute("INSERT INTO secretariasenai.espera(name, preferencial, motivo, ja_atendido) VALUES (%s, %s, %s, %s);", (infos[0], infos[1], infos[2], False))
            executaefecha(cursor, conexao)
        except:
            cursor, conexao = conecta()
            cursor.execute("INSERT INTO secretariasenai.espera(name, preferencial, motivo, ja_atendido) VALUES (%s, %s, %s, %s);", (infos[0], infos[1], infos[2], False))
            executaefecha(cursor, conexao)
            

entry_1.focus_set()

botoes = [button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9, button_10, button_11, button_12, button_13, button_14, button_15, button_16, button_17, button_18, button_19, button_20, button_21, button_22, button_23, button_24, button_25, button_26, button_27, button_28, button_29, button_30, button_31, button_32, entry_1, texto1]

place_tela1()





window.tk.resizable(False, False)
window.tk.mainloop()

