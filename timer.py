from os import system
from tkinter import Button, Label, Frame, Entry, Tk, PhotoImage
from re import findall


class Timer():
    def __init__(self, janela) -> None:
        self.base = janela
        self.frame = Frame(janela, bg="#191919")
        self.frame.pack(fill = "both", expand=True)
        self.frame2 = Frame(self.frame, bg="#191919")
        self.frame2.pack(side="bottom", pady=10)
    def inicio(self):
        text = Label(self.frame,text="tempo para o desligamento em minutos:".capitalize(), width=50, pady=20, bg="#191919", fg="#ffffff", font=("Calibri", 15))
        text.pack(pady=10)

        self.tempo = Entry(self.frame, width=50)
        self.tempo.pack(pady=10)
        self.tempo.bind('<Return>', timer.event)

        button = Button(self.frame, text="desligar".capitalize(), command=timer.shutdow)
        button.pack(pady=10)
    def event(self, e):
        timer.shutdow()
    def shutdow(self):
        tempo = self.tempo.get()
        limpo = findall("\d", tempo)
        tempo = timer.concate(limpo)
        if tempo:
            system(f"shutdown -s -t {tempo*60}")
            timer.frames()
            alerta = Label(self.frame2, text=f"O computador desligara em {tempo} minutos.".capitalize(), bg="#191919", fg="#ffffff", font=("Calibri", 13))
            alerta.pack(side="top", pady=10)
            self.base.after(3000, self.base.destroy)
        else:
            timer.frames()
            alerta = Label(self.frame2, text=f"Ensira um tempo para o deligamento".capitalize(), bg="#191919", fg="#ffffff", font=("Calibri", 13))
            alerta.pack(side="top",pady=10)
    def concate(self, x):
            string = ""
            for i in x:string+=i
            return string
    def frames(self):
        self.frame2.destroy()
        self.frame2 = Frame(self.frame, bg="#191919")
        self.frame2.pack(side="bottom", pady=10)
janela = Tk()
janela.title("Timer")
janela.geometry("500x250")
janela.iconphoto(False, PhotoImage(file = "icon.png"))
timer = Timer(janela)
timer.inicio()
janela.mainloop()