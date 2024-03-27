import flet as ft
import math as tgnm
import local as LOCAL   
import random as r 
import pygame as pg

bg = "#000000"
bgtxt = "#0F0F0F"
brdtxt = ""
c_tmg = ["#1B7F79", "#66E4F2", "#3FB2BF"]
c_ari = ["#ff4d6d", "#ffb3c1", "#800f2f"]
c_num = ["#FF81D0", "#80888F", "#400036"]
equal = ["#02733E", "#023535f", "#038C4C"]
c = ["#BF0F0F", "#BF5315", "#F20519"]
delete = ["#fa5e1f", "#ff7e33", "#fa5e1f"]
radian = ["#2D3E40", "#387373", "#97A6A0"]
btn_w = 80
btn_h = 70
pg.mixer.init()
click = pg.mixer.Sound('assets/click.mp3')

# pg.mixer.music.load('assets/main.mp3')
# pg.mixer.music.play(-1)
def main(page : ft.Page):
    pg.mixer.music.load('assets/main.mp3')
    pg.mixer.music.play(-1)
    page.window_height = 620
    page.window_width = 680
    page.bgcolor = bg
    page.window_resizable = False
    page.window_maximizable = False
    page.title = "Calculadora"

    def tecla(e: ft.KeyboardEvent):
        k = e.key
        print(k)
        if k == "Numpad 0" or k == "0":
            texto.value = texto.value + "0"
        if k == "Numpad 1" or k == "1":
            texto.value = texto.value + "1"
        if k == "Numpad 2" or k == "2":
            texto.value = texto.value + "2"
        if k == "Numpad 3" or k == "3":
            texto.value = texto.value + "3"
        if k == "Numpad 4" or k == "4":
            texto.value = texto.value + "4"
        if k == "Numpad 5" or k == "5":
            texto.value = texto.value + "5"
        if k == "Numpad 6" or k == "6":
            texto.value = texto.value + "6"
        if k == "Numpad 7" or k == "7":
            texto.value = texto.value + "7"
        if k == "Numpad 8" or k == "8":
            texto.value = texto.value + "8"
        if k == "Numpad 9" or k == "9":
            texto.value = texto.value + "9"
        if k == "Backspace":
            texto.value = texto.value[:-1]
        if k == "Numpad Add":
            texto.value += "+"        
        if k == "Numpad Subtract":
            texto.value += "-"        
        if k == "Numpad Multiply":
            texto.value += "*"        
        if k == "Numpad Divide":
            texto.value += "/"
        if k == "Enter":
            try:
                texto.value = str(eval(texto.value))
            except Exception as e:
                texto.value = "Error de Sintaxis"
        page.update()

    def grados_a_radianes(grados):
        return grados * tgnm.pi / 180
    def get_data(e):
        click.play()
        data = e.control.data
        if data == "=":
            try:
                texto.value = str(eval(texto.value))
            except Exception as e:
                texto.value = "Error de Sintaxis"
        elif data == "AC":
            texto.value = ""
        elif data == "C":
            texto.value = texto.value[:-1] if texto.value else texto.value
        elif data == "p":
            try:
                texto.value = str(float(texto.value) / 100)
            except ValueError:
                texto.value = "Error de Sintaxis"
        elif data == ".":
            if not texto.value or texto.value[:-1] not in [".", "+", "*", "/"]:
                texto.value += data
        elif data == "±":
            texto.value = "-" + texto.value if texto.value and texto.value[0] != "-" else texto.value[1:]
        elif data == "sin":
            try:
                if not LOCAL.radianes:
                    print(LOCAL.radianes)
                    angulo_radianes = grados_a_radianes(float(texto.value))
                    num = texto.value
                    sen = tgnm.sin(angulo_radianes)
                    texto.value = f"Sin({num})° = {sen}"
                else:
                    num = float(texto.value)
                    sen = tgnm.sin(num)
                    texto.value = f"Sin({num})° = {sen}"
            except Exception as e:
                print(e)
                texto.value= "Error de Sintaxis"
        elif data == "cos":
            try:
                if not LOCAL.radianes:
                    angulo_radianes = grados_a_radianes(float(texto.value))
                    num = float(texto.value)
                    cos = tgnm.cos(angulo_radianes)
                    texto.value = f"Cos({num})° = {cos}"
                else:
                    num = float(texto.value)
                    cos = tgnm.cos(num)
                    texto.value = f"Cos({num})° = {cos}"
            except Exception as e:    
                texto.value = "Error de Sintaxis"
        elif data == "tan":
            if texto.value == "270" or texto.value == "90":
                texto.value = "Eres tonto?"
            else:
                try:
                    if not LOCAL.radianes:
                        angulo_radianes = grados_a_radianes(float(texto.value))
                        num = float(texto.value)
                        tan = tgnm.tan(angulo_radianes)
                        texto.value = f"Tan({num})° = {tan}"
                    else: 
                        num = texto.value
                        tan = tgnm.tan(num)
                        texto.value = f"Tan({num})° = {tan}"
                except Exception as e:    
                    texto.value = "Error de Sintaxis"   
        elif data == "!":
            try: 
                n = int(texto.value)
                f = 1
                for i in range(1, n+1):
                    f*=i
                texto.value = str(f)
            except Exception as e:
                texto.value = "Error de sintaxis"
        elif data == "r":
            try:
                texto.value = str(float(texto.value) ** 0.5)
            except Exception as e:
                texto.value = "Error de Sintaxis"
        elif data == "abs":
            texto.value = str(abs(int(float(texto.value))))
        elif data == "bin":
            try: 
                bina = bin(int(texto.value))[2:]
                num = texto.value
                texto.value = f"Binario ( {num} ) = {bina}"
            except Exception as e:
                texto.value = "Error de sintaxis"
        elif data == "hex":
            try: 
                hexa = hex(int(texto.value))[2:]
                uphexa = str(hexa).upper()
                num = texto.value
                texto.value = f"Hexadecimal ( {num} ) = {uphexa}"
            except Exception as e:
                texto.value = "Error de sintaxis"
        elif data == "oct":
            try:
                octa = oct(int(texto.value))[2:]
                num = texto.value
                texto.value = f"Octal ( {num} ) = {octa}"
            except Exception as e:
                texto.value= "Error de sinstasis"
        elif data == "med":
            if medida.text == "Deg":
                medida.text = "Rad"
                medida.bgcolor = radian[0]
                medida.style = ft.ButtonStyle(shape=ft.CircleBorder(), padding = 14,
                                                   shadow_color=radian[1],side=ft.BorderSide(width=2, color=radian[2]))
                LOCAL.radianes = True
            else: 
                medida.text = "Deg"
                medida.bgcolor = c_ari[0]
                medida.style = ft.ButtonStyle(shape=ft.CircleBorder(), padding = 14,
                                                   shadow_color=c_ari[1],side=ft.BorderSide(width=2, color=c_ari[2]))
                LOCAL.radianes = False
        elif data == "log":
            try:
                num = texto.value
                x = float(texto.value)
                log = tgnm.log(x)
                texto.value = f"Log( {num} ) = {log}"
            except Exception as e:
                texto.value = "Error de sintaxis"
        elif data == "int":
            texto.value = str(int(float(texto.value)))
        elif data == "redo":
            texto.value = str(round(float(texto.value)))
        elif data == "x2":
            texto.value = str(float(texto.value) * float(texto.value))
        elif data == "fac":
            try:
                factorizado = LOCAL.fac(int(texto.value))
                texto.value = str(factorizado)
            except Exception as e:
                texto.value = "Error de Sintaxis"
        elif data == "rand":
            try:
                n = int(texto.value)
                texto.value = str(r.randint(0,n))
            except Exception as e:
                texto.value = "Error de Sintaxis"
        elif data == "sci":
            try:
                n = float(texto.value)
                sci = '{:.3e}'.format(n)
                texto.value = sci.replace('e', '').replace('+', '^')
            except Exception as e:
                texto.value = "Error de Sintaxis"
        elif data in ["[", "]", "0.5","1.618","2.718281828","1", "2","3","4","5", "6", "7", "8", "9", "0", "+", "-", "*", "/", "%", "(", ")", "3.141592653", "//", "**"]:
            texto.value += data
        page.update()
    
    page.on_keyboard_event = tecla
    texto = ft.TextField(read_only=True, bgcolor=bgtxt,border_color=ft.colors.WHITE,text_align="right",
                        text_style=ft.TextStyle(size=30, color ="white"))
    page.add(texto)
    medida = ft.ElevatedButton(text = "Deg", height=btn_h, width=btn_w,
                              bgcolor = c_ari[0],
                              color = ft.colors.WHITE,
                              style=ft.ButtonStyle(shape=ft.CircleBorder(), padding = 14,
                                                   shadow_color=c_ari[1],side=ft.BorderSide(width=2, color=c_ari[2])),
                                                   elevation=5, data="med",
                                                   on_click=get_data)                                              
    page.add(
        ft.Row([
            ft.ElevatedButton(text = "C",width=btn_w,height=btn_h,
                              bgcolor = c[0],
                              color = ft.colors.WHITE,
                              style=ft.ButtonStyle(shape=ft.CircleBorder(), padding = 14,
                                                   shadow_color=c[1],side=ft.BorderSide(width=2, color=c[2])),
                                                   elevation=5, data="AC",
                                                   on_click=get_data),
            ft.ElevatedButton(text = "⌫",width=btn_w,height=btn_h, 
                              bgcolor = delete[0],
                              color = ft.colors.WHITE,
                              style=ft.ButtonStyle(shape=ft.CircleBorder(), padding = 14,
                                                   shadow_color=delete[1],side=ft.BorderSide(width=2, color=delete[2])),
                                                   elevation=5, data="C",
                                                   on_click=get_data),
            medida,
            ft.ElevatedButton(text = "÷",width=btn_w,height=btn_h, 
                              bgcolor = c_ari[0],
                              color = ft.colors.WHITE,
                              style=ft.ButtonStyle(shape=ft.CircleBorder(), padding = 14,
                                                   shadow_color=c_ari[1],side=ft.BorderSide(width=2, color=c_ari[2])),
                                                   elevation=5, data="/",
                                                   on_click=get_data),
            ft.ElevatedButton(text = "/",width=btn_w,height=btn_h, 
                              bgcolor = c_ari[0],
                              color = ft.colors.WHITE,
                              style=ft.ButtonStyle(shape=ft.CircleBorder(), padding = 14,
                                                   shadow_color=c_ari[1],side=ft.BorderSide(width=2, color=c_ari[2])),
                                                   elevation=5, data="//",
                                                   on_click=get_data),
            ft.ElevatedButton(text = "!",width=btn_w,height=btn_h, 
                              bgcolor = c_ari[0],
                              color = ft.colors.WHITE,
                              style=ft.ButtonStyle(shape=ft.CircleBorder(), padding = 14,
                                                   shadow_color=c_ari[1],side=ft.BorderSide(width=2, color=c_ari[2])),
                                                   elevation=5, data="!",
                                                   on_click=get_data),
            ft.ElevatedButton(text = "Mod",width=btn_w,height=btn_h, 
                              bgcolor = c_tmg[0],
                              color = ft.colors.WHITE,
                              style=ft.ButtonStyle(shape=ft.CircleBorder(), padding = 14,
                                                   shadow_color=c_tmg[1],side=ft.BorderSide(width=2, color=c_tmg[2])),
                                                   elevation=5, data="%",
                                                   on_click=get_data),
            ft.ElevatedButton(text = "Abs",width=btn_w,height=btn_h, 
                              bgcolor = c_tmg[0],
                              color = ft.colors.WHITE,
                              style=ft.ButtonStyle(shape=ft.CircleBorder(), padding = 14,
                                                   shadow_color=c_tmg[1],side=ft.BorderSide(width=2, color=c_tmg[2])),
                                                   elevation=5, data="abs",
                                                   on_click=get_data),
        ], 
        alignment= ft.MainAxisAlignment.SPACE_EVENLY
        ),
        ft.Row([
            ft.ElevatedButton(text = "7",width=btn_w,height=btn_h, 
                              bgcolor = c_num[0],
                              color = ft.colors.WHITE,
                              style=ft.ButtonStyle(shape=ft.CircleBorder(), padding = 14,
                                                   shadow_color = c_num[1],side=ft.BorderSide(width=2, color = c_num[2])),
                                                   elevation=5, data="7",
                                                   on_click=get_data),
            ft.ElevatedButton(text = "8",width=btn_w,height=btn_h, 
                              bgcolor = c_num[0],
                              color = ft.colors.WHITE,
                              style=ft.ButtonStyle(shape=ft.CircleBorder(), padding = 14,
                                                   shadow_color = c_num[1],side=ft.BorderSide(width=2, color = c_num[2])),
                                                   elevation=5, data="8",
                                                   on_click=get_data),
            ft.ElevatedButton(text = "9",width=btn_w,height=btn_h, 
                              bgcolor = c_num[0],
                              color = ft.colors.WHITE,
                              style=ft.ButtonStyle(shape=ft.CircleBorder(), padding = 14,
                                                   shadow_color = c_num[1],side=ft.BorderSide(width=2, color = c_num[2])),
                                                   elevation=5, data="9",
                                                   on_click=get_data),                                           
            ft.ElevatedButton(text = "*",width=btn_w,height=btn_h, 
                              bgcolor = c_ari[0],
                              color = ft.colors.WHITE,
                              style=ft.ButtonStyle(shape=ft.CircleBorder(), padding = 14,
                                                   shadow_color=c_ari[1],side=ft.BorderSide(width=2, color=c_ari[2])),
                                                   elevation=5, data="*",
                                                   on_click=get_data),
            ft.ElevatedButton(text = "(",width=btn_w,height=btn_h, 
                              bgcolor = c_ari[0],
                              color = ft.colors.WHITE,
                              style=ft.ButtonStyle(shape=ft.CircleBorder(), padding = 14,
                                                   shadow_color=c_ari[1],side=ft.BorderSide(width=2, color=c_ari[2])),
                                                   elevation=5, data="(",
                                                   on_click=get_data), 
            ft.ElevatedButton(text = ")",width=btn_w,height=btn_h, 
                              bgcolor = c_ari[0],
                              color = ft.colors.WHITE,
                              style=ft.ButtonStyle(shape=ft.CircleBorder(), padding = 14,
                                                   shadow_color=c_ari[1],side=ft.BorderSide(width=2, color=c_ari[2])),
                                                   elevation=5, data=")",
                                                   on_click=get_data), 
            ft.ElevatedButton(text = "Sin",width=btn_w,height=btn_h, 
                              bgcolor = c_tmg[0],
                              color = ft.colors.WHITE,
                              style=ft.ButtonStyle(shape=ft.CircleBorder(), padding = 14,
                                                   shadow_color=c_tmg[1],side=ft.BorderSide(width=2, color=c_tmg[2])),
                                                   elevation=5, data="sin",
                                                   on_click=get_data),   
            ft.ElevatedButton(text = "Oct",width=btn_w,height=btn_h, 
                              bgcolor = c_tmg[0],
                              color = ft.colors.WHITE,
                              style=ft.ButtonStyle(shape=ft.CircleBorder(), padding = 14,
                                                   shadow_color=c_tmg[1],side=ft.BorderSide(width=2, color=c_tmg[2])),
                                                   elevation=5, data="oct",
                                                   on_click=get_data),   
        
        ], 
        alignment= ft.MainAxisAlignment.SPACE_EVENLY
        ),
        ft.Row([
            ft.ElevatedButton(text = "4",width=btn_w,height=btn_h, 
                              bgcolor = c_num[0],
                              color = ft.colors.WHITE,
                              style=ft.ButtonStyle(shape=ft.CircleBorder(), padding = 14,
                                                   shadow_color = c_num[1],side=ft.BorderSide(width=2, color = c_num[2])),
                                                   elevation=5, data="4",
                                                   on_click=get_data),
            ft.ElevatedButton(text = "5",width=btn_w,height=btn_h, 
                              bgcolor = c_num[0],
                              color = ft.colors.WHITE,
                              style=ft.ButtonStyle(shape=ft.CircleBorder(), padding = 14,
                                                   shadow_color = c_num[1],side=ft.BorderSide(width=2, color = c_num[2])),
                                                   elevation=5, data="5",
                                                   on_click=get_data),
            ft.ElevatedButton(text = "6",width=btn_w,height=btn_h, 
                              bgcolor = c_num[0],
                              color = ft.colors.WHITE,
                              style=ft.ButtonStyle(shape=ft.CircleBorder(), padding = 14,
                                                   shadow_color = c_num[1],side=ft.BorderSide(width=2, color = c_num[2])),
                                                   elevation=5, data="6",
                                                   on_click=get_data),                                           
            ft.ElevatedButton(text = "-",width=btn_w,height=btn_h, 
                              bgcolor = c_ari[0],
                              color = ft.colors.WHITE,
                              style=ft.ButtonStyle(shape=ft.CircleBorder(), padding = 14,
                                                   shadow_color=c_ari[1],side=ft.BorderSide(width=2, color=c_ari[2])),
                                                   elevation=5, data="-",
                                                   on_click=get_data),
            ft.ElevatedButton(text = "^",width=btn_w,height=btn_h, 
                              bgcolor = c_ari[0],
                              color = ft.colors.WHITE,
                              style=ft.ButtonStyle(shape=ft.CircleBorder(), padding = 14,
                                                   shadow_color=c_ari[1],side=ft.BorderSide(width=2, color=c_ari[2])),
                                                   elevation=5, data="**",
                                                   on_click=get_data),  
            ft.ElevatedButton(text = "SCI",width=btn_w,height=btn_h, 
                              bgcolor = c_ari[0],
                              color = ft.colors.WHITE,
                              style=ft.ButtonStyle(shape=ft.CircleBorder(), padding = 14,
                                                   shadow_color=c_ari[1],side=ft.BorderSide(width=2, color=c_ari[2])),
                                                   elevation=5, data="sci",
                                                   on_click=get_data),          
            ft.ElevatedButton(text = "Cos",width=btn_w,height=btn_h, 
                              bgcolor = c_tmg[0],
                              color = ft.colors.WHITE,
                              style=ft.ButtonStyle(shape=ft.CircleBorder(), padding = 14,
                                                   shadow_color=c_tmg[1],side=ft.BorderSide(width=2, color=c_tmg[2])),
                                                   elevation=5, data="cos",
                                                   on_click=get_data),        
            ft.ElevatedButton(text = "Hex",width=btn_w,height=btn_h, 
                              bgcolor = c_tmg[0],
                              color = ft.colors.WHITE,
                              style=ft.ButtonStyle(shape=ft.CircleBorder(), padding = 14,
                                                   shadow_color=c_tmg[1],side=ft.BorderSide(width=2, color=c_tmg[2])),
                                                   elevation=5, data="hex",
                                                   on_click=get_data),   
        
        ], 
        alignment= ft.MainAxisAlignment.SPACE_EVENLY
        ),
        ft.Row([
            ft.ElevatedButton(text = "1",width=btn_w,height=btn_h, 
                              bgcolor = c_num[0],
                              color = ft.colors.WHITE,
                              style=ft.ButtonStyle(shape=ft.CircleBorder(), padding = 14,
                                                   shadow_color = c_num[1],side=ft.BorderSide(width=2, color = c_num[2])),
                                                   elevation=5, data="1",
                                                   on_click=get_data),
            ft.ElevatedButton(text = "2",width=btn_w,height=btn_h, 
                              bgcolor = c_num[0],
                              color = ft.colors.WHITE,
                              style=ft.ButtonStyle(shape=ft.CircleBorder(), padding = 14,
                                                   shadow_color = c_num[1],side=ft.BorderSide(width=2, color = c_num[2])),
                                                   elevation=5, data="2",
                                                   on_click=get_data),
            ft.ElevatedButton(text = "3",width=btn_w,height=btn_h, 
                              bgcolor = c_num[0],
                              color = ft.colors.WHITE,
                              style=ft.ButtonStyle(shape=ft.CircleBorder(), padding = 14,
                                                   shadow_color = c_num[1],side=ft.BorderSide(width=2, color = c_num[2])),
                                                   elevation=5, data="3",
                                                   on_click=get_data),                                           
            ft.ElevatedButton(text = "+",width=btn_w,height=btn_h, 
                              bgcolor = c_ari[0],
                              color = ft.colors.WHITE,
                              style=ft.ButtonStyle(shape=ft.CircleBorder(), padding = 14,
                                                   shadow_color=c_ari[1],side=ft.BorderSide(width=2, color=c_ari[2])),
                                                   elevation=5, data="+",
                                                   on_click=get_data),
            ft.ElevatedButton(text = "²√ ",width=btn_w,height=btn_h, 
                              bgcolor = c_ari[0],
                              color = ft.colors.WHITE,
                              style=ft.ButtonStyle(shape=ft.CircleBorder(), padding = 14,
                                                   shadow_color=c_ari[1],side=ft.BorderSide(width=2, color=c_ari[2])),
                                                   elevation=5, data="r",
                                                   on_click=get_data),
            ft.ElevatedButton(text = "x²",width=btn_w,height=btn_h, 
                              bgcolor = c_ari[0],
                              color = ft.colors.WHITE,
                              style=ft.ButtonStyle(shape=ft.CircleBorder(), padding = 14,
                                                   shadow_color=c_ari[1],side=ft.BorderSide(width=2, color=c_ari[2])),
                                                   elevation=5, data="x2",
                                                   on_click=get_data),
            ft.ElevatedButton(text = "Tan",width=btn_w,height=btn_h, 
                              bgcolor = c_tmg[0],
                              color = ft.colors.WHITE,
                              style=ft.ButtonStyle(shape=ft.CircleBorder(), padding = 14,
                                                   shadow_color=c_tmg[1],side=ft.BorderSide(width=2, color=c_tmg[2])),
                                                   elevation=5, data="",
                                                   on_click=get_data),
            ft.ElevatedButton(text = "Bin",width=btn_w,height=btn_h, 
                              bgcolor = c_tmg[0],
                              color = ft.colors.WHITE,
                              style=ft.ButtonStyle(shape=ft.CircleBorder(), padding = 14,
                                                   shadow_color=c_tmg[1],side=ft.BorderSide(width=2, color=c_tmg[2])),
                                                   elevation=5, data="bin",
                                                   on_click=get_data),   
        
        ], 
        alignment= ft.MainAxisAlignment.SPACE_EVENLY
        ),
        ft.Row([
            ft.ElevatedButton(text = "±",width=btn_w,height=btn_h, 
                              bgcolor = c_ari[0],
                              color = ft.colors.WHITE,
                              style=ft.ButtonStyle(shape=ft.CircleBorder(), padding = 14,
                                                   shadow_color=c_ari[1],side=ft.BorderSide(width=2, color=c_ari[2])),
                                                   elevation=5, data="±",
                                                   on_click=get_data),
            ft.ElevatedButton(text = "0",width=btn_w,height=btn_h, 
                              bgcolor = c_num[0],
                              color = ft.colors.WHITE,
                              style=ft.ButtonStyle(shape=ft.CircleBorder(), padding = 14,
                                                   shadow_color = c_num[1],side=ft.BorderSide(width=2, color = c_num[2])),
                                                   elevation=5, data="0",
                                                   on_click=get_data),
            ft.ElevatedButton(text = ".",width=btn_w,height=btn_h, 
                              bgcolor = c_ari[0],
                              color = ft.colors.WHITE,
                              style=ft.ButtonStyle(shape=ft.CircleBorder(), padding = 14,
                                                   shadow_color=c_ari[1],side=ft.BorderSide(width=2, color=c_ari[2])),
                                                   elevation=5, data=".",
                                                   on_click=get_data),                                          
            ft.ElevatedButton(text = "%",width=btn_w,height=btn_h, 
                              bgcolor = c_ari[0],
                              color = ft.colors.WHITE,
                              style=ft.ButtonStyle(shape=ft.CircleBorder(), padding = 14,
                                                   shadow_color=c_ari[1],side=ft.BorderSide(width=2, color=c_ari[2])),
                                                   elevation=5, data="p",
                                                   on_click=get_data),                                                 
            ft.ElevatedButton(text = "π",width=btn_w,height=btn_h, 
                              bgcolor = c_tmg[0],
                              color = ft.colors.WHITE,
                              style=ft.ButtonStyle(shape=ft.CircleBorder(), padding = 14,
                                                   shadow_color=c_tmg[1],side=ft.BorderSide(width=2, color=c_tmg[2])),
                                                   elevation=5, data="3.141592653",
                                                   on_click=get_data),
            ft.ElevatedButton(text = "e",width=btn_w,height=btn_h, 
                              bgcolor = c_tmg[0],
                              color = ft.colors.WHITE,
                              style=ft.ButtonStyle(shape=ft.CircleBorder(), padding = 14,
                                                   shadow_color=c_tmg[1],side=ft.BorderSide(width=2, color=c_tmg[2])),
                                                   elevation=5, data="2.718281828",
                                                   on_click=get_data),
            ft.ElevatedButton(text = "f",width=btn_w,height=btn_h, 
                              bgcolor = c_tmg[0],
                              color = ft.colors.WHITE,
                              style=ft.ButtonStyle(shape=ft.CircleBorder(), padding = 14,
                                                   shadow_color=c_tmg[1],side=ft.BorderSide(width=2, color=c_tmg[2])),
                                                   elevation=5, data="1.618",
                                                   on_click=get_data),
            ft.ElevatedButton(text = "Log",width=btn_w,height=btn_h, 
                              bgcolor = c_tmg[0],
                              color = ft.colors.WHITE,
                              style=ft.ButtonStyle(shape=ft.CircleBorder(), padding = 14,
                                                   shadow_color=c_tmg[1],side=ft.BorderSide(width=2, color=c_tmg[2])),
                                                   elevation=5, data="log",
                                                   on_click=get_data),
        ], 
        alignment= ft.MainAxisAlignment.SPACE_EVENLY
        ),
        ft.Row([
            ft.ElevatedButton(text = "½",width=btn_w,height=btn_h, 
                              bgcolor = c_ari[0],
                              color = ft.colors.WHITE,
                              style=ft.ButtonStyle(shape=ft.CircleBorder(), padding = 14,
                                                   shadow_color=c_ari[1],side=ft.BorderSide(width=2, color=c_ari[2])),
                                                   elevation=5, data="0.5",
                                                   on_click=get_data),
            ft.ElevatedButton(text = "[",width=btn_w,height=btn_h, 
                              bgcolor = c_ari[0],
                              color = ft.colors.WHITE,
                              style=ft.ButtonStyle(shape=ft.CircleBorder(), padding = 14,
                                                   shadow_color=c_ari[1],side=ft.BorderSide(width=2, color=c_ari[2])),
                                                   elevation=5, data="[",
                                                   on_click=get_data), 
            ft.ElevatedButton(text = "]",width=btn_w,height=btn_h, 
                              bgcolor = c_ari[0],
                              color = ft.colors.WHITE,
                              style=ft.ButtonStyle(shape=ft.CircleBorder(), padding = 14,
                                                   shadow_color=c_ari[1],side=ft.BorderSide(width=2, color=c_ari[2])),
                                                   elevation=5, data="]",
                                                   on_click=get_data),   
            ft.ElevatedButton(text = "R",width=btn_w,height=btn_h, 
                              bgcolor = c_ari[0],
                              color = ft.colors.WHITE,
                              style=ft.ButtonStyle(shape=ft.CircleBorder(), padding = 14,
                                                   shadow_color=c_ari[1],side=ft.BorderSide(width=2, color=c_ari[2])),
                                                   elevation=5, data="rand",
                                                   on_click=get_data),                                        
            ft.ElevatedButton(text = "Fac",width=btn_w,height=btn_h, 
                              bgcolor = c_tmg[0],
                              color = ft.colors.WHITE,
                              style=ft.ButtonStyle(shape=ft.CircleBorder(), padding = 14,
                                                   shadow_color=c_tmg[1],side=ft.BorderSide(width=2, color=c_tmg[2])),
                                                   elevation=5, data="fac",
                                                   on_click=get_data),         
            ft.ElevatedButton(text = "Int",width=btn_w,height=btn_h, 
                              bgcolor = c_tmg[0],
                              color = ft.colors.WHITE,
                              style=ft.ButtonStyle(shape=ft.CircleBorder(), padding = 14,
                                                   shadow_color=c_tmg[1],side=ft.BorderSide(width=2, color=c_tmg[2])),
                                                   elevation=5, data="int",
                                                   on_click=get_data),
            ft.ElevatedButton(text = "Redo",width=btn_w,height=btn_h, 
                              bgcolor = c_tmg[0],
                              color = ft.colors.WHITE,
                              style=ft.ButtonStyle(shape=ft.CircleBorder(), padding = 14,
                                                   shadow_color=c_tmg[1],side=ft.BorderSide(width=2, color=c_tmg[2])),
                                                   elevation=5, data="redo",
                                                   on_click=get_data),
            ft.ElevatedButton(text = "=",width=btn_w,height=btn_h, 
                              bgcolor = equal[0],
                              color = ft.colors.WHITE,
                              style=ft.ButtonStyle(shape=ft.CircleBorder(), padding = 14,
                                                   shadow_color=equal[1],side=ft.BorderSide(width=2, color=equal[2])),
                                                   elevation=5, data="=",
                                                   on_click=get_data),
        ], 
        alignment= ft.MainAxisAlignment.SPACE_EVENLY
        ),
        )

    

ft.app(target=main)
