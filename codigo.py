from tkinter import *

def simulador():
    casa = float(entry_casa.get())
    salario = float(entry_salario.get())
    duracao = int(entry_duracao.get())

    prestacao = casa / (duracao * 12)
    porcent = salario * (30 / 100)

    if prestacao <= porcent:
        simular['text'] = f'Para pagar um imóvel de R$ {casa} em {duracao} anos\nA prestação será de R$ {prestacao:.2f}.\nEmpréstimo pode ser CONCEDIDO!'
    else:
        simular['text'] = f'Para pagar um imóvel de R$ {casa} em {duracao} anos\nA prestação será de R$ {prestacao:.2f}.\nEmpréstimo NEGADO'

#interface
janela = Tk()
janela.geometry("400x400")
janela.title('SIMULADOR DE IMOVEIS')

title = Label(janela, text='SIMULADOR DE FINANCIAMENTO DE IMÓVEIS', font=('calibre', 12, 'bold'))
title.pack()
title.place(x=20, y=15)

Label_casa = Label(janela,  text='Qual o valor do Imovel?', font=('calibre',10, 'bold'))
Label_casa.pack()
Label_casa.place(x=100, y=51)

Real1 = Label(janela, text='R$', font=('calibre', 10, 'bold'))
Real1.place(x=100, y=71)

entry_casa = Entry(janela)
entry_casa.pack()
entry_casa.place(x=130,y=73)

Label_salario = Label(janela,  text='Quanto você recebe?', font=('calibre',10, 'bold'))
Label_salario.pack()
Label_salario.place(x=100, y=98)

Real2 = Label(janela, text='R$', font=('calibre', 10, 'bold'))
Real2.place(x=100, y=118)

entry_salario = Entry(janela)
entry_salario.pack()
entry_salario.place(x=130, y=120)

Label_duracao = Label(janela,  text='Financiar por quantos anos?', font=('calibre',10, 'bold'))
Label_duracao.pack()
Label_duracao.place(x=100, y=145)

Real3 = Label(janela, text='R$', font=('calibre', 10, 'bold'))
Real3.place(x=100, y=165)

entry_duracao = Entry(janela)
entry_duracao.pack()
entry_duracao.place(x=130, y=167)

btn_calcular = Button(janela, text='Simular', command=simulador)
btn_calcular.pack()
btn_calcular.place(x=170, y=205)

simular = Label(janela, text='')
simular.pack()
simular.place(x=75, y=250)

janela.mainloop()