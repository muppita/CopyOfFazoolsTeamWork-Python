import tkinter as tk
from tkinter import *
from PIL import ImageTk


root = tk.Tk()

#width, height = Image.open(image.png).size


canvas = tk.Canvas(root, width=1800, height=2659,background="#DCDCDC")
canvas.pack()
image = ImageTk.PhotoImage(file="board2.png")
canvas.create_image(0,790, image=image,anchor = SW)
root.title('Loco Motive')

#option menu buttons hosting area
pickcarriagecard_button = tk.Button(root, text = "   Saved Game",font=("courier", 15),  command = root.quit, anchor = 'w',width = 16,height = 2,
                       activebackground = "#33B5E5")
pickcarriagecard_button_window = canvas.create_window(1070, 180, anchor='nw', window=pickcarriagecard_button)    
pickroute_button = tk.Button(root, text = "     New Game",font=("courier", 15),  command = root.quit, anchor = 'w',
                    width = 18,height = 2, activebackground = "#33B5E5")
pickroute_button_window = canvas.create_window(1290, 180, anchor='nw', window=pickroute_button)
claimroute_button = tk.Button(root, text = "  Claim a route",font=("courier", 15),  command = root.quit, anchor = 'w',
                    width = 16,height = 2, activebackground = "#33B5E5")
claimroute_button_window = canvas.create_window(1070, 300, anchor='nw', window=claimroute_button)
endturn_button = tk.Button(root, text = "    End Turn",font=("courier", 15),  command = root.quit, anchor = 'w',
                    width = 18,height = 2, activebackground = "#33B5E5")
endturn_button_window = canvas.create_window(1290, 300, anchor='nw', window=endturn_button)
howtoplay_button = tk.Button(root, text = "   How to Play",font=("courier", 15),  command = root.quit, anchor = 'w',
                    width = 18,height = 1, activebackground = "#33B5E5")
howtoplay_button_window = canvas.create_window(1210, 400, anchor='nw', window=howtoplay_button)
scoreboard_button = tk.Button(root, text = "",font=("courier", 15), command = root.quit, anchor = 'w',
                    width =37,height = 10, activebackground = "#33B5E5")
scoareboard_button_window = canvas.create_window(1065, 450, anchor='nw', window=scoreboard_button)

# carriage cards
carriagecard1_button = tk.Button(root, text = "      Carriage Card", command = root.quit, anchor = 'w',
                    width =16,height = 2, activebackground = "#33B5E5")
carriagecard1_button_window = canvas.create_window(20, 795, anchor='nw', window=carriagecard1_button)

carriagecard2_button = tk.Button(root, text = "      Carriage Card", command = root.quit, anchor = 'w',
                    width =16,height = 2, activebackground = "#33B5E5")
carriagecard2_button_window = canvas.create_window(160, 795, anchor='nw', window=carriagecard2_button)
carriagecard3_button = tk.Button(root, text = "      Carriage Card", command = root.quit, anchor = 'w',
                    width =16,height = 2, activebackground = "#33B5E5")
carriagecard3_button_window = canvas.create_window(300, 795, anchor='nw', window=carriagecard3_button)

carriagecard4_button = tk.Button(root, text = "      Carriage Card", command = root.quit, anchor = 'w',
                    width =16,height = 2, activebackground = "#33B5E5")
carriagecard4_button_window = canvas.create_window(438, 795, anchor='nw', window=carriagecard4_button)

carriagecard5_button = tk.Button(root, text = "      Carriage Card", command = root.quit, anchor = 'w',
                    width =16,height = 2, activebackground = "#33B5E5")
carriagecard5_button_window = canvas.create_window(576, 795, anchor='nw', window=carriagecard5_button)

carriagecard6_button = tk.Button(root, text = "      Carriage Card", command = root.quit, anchor = 'w',
                    width =16,height = 2, activebackground = "#33B5E5")
carriagecard6_button_window = canvas.create_window(717, 795, anchor='nw', window=carriagecard6_button)

carriagecard7_button = tk.Button(root, text = "      Carriage Card", command = root.quit, anchor = 'w',
                    width =16,height = 2, activebackground = "#33B5E5")
carriagecard7_button_window = canvas.create_window(855, 795, anchor='nw', window=carriagecard7_button)

carriagecard8_button = tk.Button(root, text = "      Carriage Card", command = root.quit, anchor = 'w',
                    width =16,height = 2, activebackground = "#33B5E5")
carriagecard8_button_window = canvas.create_window(995, 795, anchor='nw', window=carriagecard8_button)

carriagecard9_button = tk.Button(root, text = "      Carriage Card", command = root.quit, anchor = 'w',
                    width =16,height = 2, activebackground = "#33B5E5")
carriagecard9_button_window = canvas.create_window(1147, 795, anchor='nw', window=carriagecard9_button)

carriagecard10_button = tk.Button(root, text = "      Carriage Card", command = root.quit, anchor = 'w',
                    width =16,height = 2, activebackground = "#33B5E5")
carriagecard10_button_window = canvas.create_window(20, 843, anchor='nw', window=carriagecard10_button)

carriagecard11_button = tk.Button(root, text =" Carriage Card", command = root.quit, anchor = 'w',
                    width =16,height = 2, activebackground = "#33B5E5")
carriagecard11_button_window = canvas.create_window(170, 843, anchor='nw', window=carriagecard11_button)

carriagecard12_button = tk.Button(root, text = " Carriage Card",command = root.quit, anchor = 'w',
                    width =16,height = 2, activebackground = "#33B5E5")
carriagecard12_button_window = canvas.create_window(320, 843, anchor='nw', window=carriagecard12_button)

carriagecard13_button = tk.Button(root, text = " Carriage Card", command = root.quit, anchor = 'w',
                    width =16,height = 2, activebackground = "#33B5E5")
carriagecard13_button_window = canvas.create_window(460, 843, anchor='nw', window=carriagecard13_button)

carriagecard14_button = tk.Button(root, text = " Carriage Card", command = root.quit, anchor = 'w',
                    width =16,height = 2, activebackground = "#33B5E5")
carriagecard14_button_window = canvas.create_window(590, 843, anchor='nw', window=carriagecard14_button)

carriagecard15_button = tk.Button(root, text = " Carriage Card", command = root.quit, anchor = 'w',
                    width =16,height = 2, activebackground = "#33B5E5")
carriagecard15_button_window = canvas.create_window(720, 843, anchor='nw', window=carriagecard15_button)














canvas_id = canvas.create_text(1225, 70, anchor="nw")
canvas.itemconfig(canvas_id, text="Loco Motive "*1, width=1200)
canvas.itemconfig(canvas_id, font=("courier", 25))


root.mainloop()

