# import tkinter as tk
# window = tk.Tk()
# label = tk.Label(text = "Hello world!")
# label.pack()
# input()
############################
# import tkinter as tk

# window = tk.Tk()
# label = tk.Label(text="Hello world!", foreground="green", background="red", width = 20, height = 20)
# label.pack()
# input()
###########################
# import tkinter as tk

# window = tk.Tk()
# entry = tk.Entry(width = 40, background="red")
# entry.pack()
# input()
############################
# import tkinter as tk

# window = tk.Tk()
# text = tk.Text(width = 40, background="red")
# text.pack()
# input()
##########################
# import tkinter as tk

# window = tk.Tk()
# frame_1 = tk.Frame()
# label_1 = tk.Label(master=frame_1, text="Hello 1")
# frame_2 = tk.Frame()
# label_2 = tk.Label(master=frame_2, text="Hello 2")

# label_1.pack()
# label_2.pack()
# frame_2.pack()
# frame_1.pack()

# input()
###############################
# import tkinter as tk

# window = tk.Tk()


# for i in range(3):
#     for j in range(3):
#         frame = tk.Frame(master=window)
#         frame.grid(row = i, column = j)
#         label = tk.Label(master=frame, text = f"{i} {j}")
#         label.pack()
# input()
#############################################
# import tkinter as tk

# window = tk.Tk()

# button = tk.Button(text = "Button", width=30, height=10, bg = "red")
# button.pack()
# input()
#############################################
# import tkinter as tk

# window = tk.Tk()

# def handle_click(e):
#     print("3")

# def handle_key(e):
#     print("3")
# # window.mainloop()
# events = []
# while  True:
#     if len(events)==0:
#         continue
#     event = events[0]
    
#     if event.type == "click":
#         handle_click(event)
#     elif event.type == "key":
#          handle_key(event)
#########################################
# import tkinter as tk

# window = tk.Tk()

# def handle_key(e):
#     print(e.char)
    
# window.bind ("<Key>", handle_key) 
# window.mainloop()
#########################################
# import tkinter as tk

# def handle_click(e):
#     print("Click!")

# window = tk.Tk()

# button = tk.Button(text="Click")
# button.pack()
# button.bind("<Button-1>", handle_click)

# window.mainloop()
# print("finish")
#######################################
# import tkinter as tk

# def decrease():
#     value = int(lbl["text"])
#     lbl["text"] = f"{value-1}"
# def increase():
#     value = int(lbl["text"])
#     lbl["text"] = f"{value+1}"

# window = tk.Tk()

# btn_increase = tk.Button(text = "+", command=increase)
# btn_decrease = tk.Button(text = "-", command=decrease)
# lbl = tk.Label(text = "0")
# btn_increase.grid(row = 0, column=0)
# lbl.grid(row = 0, column=1)
# btn_decrease.grid(row = 0, column=2)
# window.mainloop()
################################################
# import tkinter as tk


# def usd_to_rub():
#     usd = ent_usd.get()
#     res = float(usd)*73
#     lbl_result["text"] = f"{round(res,2)}"
    
# window = tk.Tk()

# window.resizable(width=False, height=False)

# frm_input = tk.Frame(master=window)
# ent_usd = tk.Entry(master = frm_input, width = 20)
# lbl_usd = tk.Label(master=frm_input, text="USD")

# ent_usd.grid(row = 0, column = 0)
# lbl_usd.grid(row = 0, column = 1)

# lbl_result = tk.Label(master=frm_input, text = "RUB")
# btn_convert = tk.Button(master=window, text = "CONVERT", command=usd_to_rub)

# frm_input.grid(row = 0, column=0)
# btn_convert.grid(row = 0, column = 1)
# lbl_result.grid(row = 0, column = 2)

# window.mainloop()

###########################################




