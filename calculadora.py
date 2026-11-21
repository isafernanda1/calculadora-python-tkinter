import tkinter as Tk
#Função clicar nos botoes
def clicar(botao):
    atual = entrada.get()

    if botao == "=":
        try:
            expressao = atual.replace("÷", "/")
            expressao = expressao.replace("×", "*")
            expressao = expressao.replace("−", "-")
            expressao = expressao.replace("xʸ", "**")
            resultado = str(eval(expressao))

            entrada.delete(0, Tk.END)
            entrada.insert(0, resultado)

            historico_text.insert(
                Tk.END, f"{atual} = {resultado}\n"
            )
        except:
            entrada.delete(0, Tk.END)
            entrada.insert(0, "erro")

    elif botao == "C":
        entrada.delete(0, Tk.END)

    else:
        entrada.insert(Tk.END, botao)
# Janela principal
janela = Tk.Tk()
janela.title("Calculadora")
#Entrada de texto
entrada=Tk.Entry(janela,width=16,font=("Arial",24), borderwidth=2,relief="solid",justify="right")
entrada.grid(row=0,column=0,columnspan=4)
#Botoes
botoes=[
    "1","2","3","+",
    "4","5","6","-",
    "7","8","9","×",
    " ","0"," ","÷",
    "C","xʸ","%","="
]
linha=1
coluna=0
for botao in botoes:
    Tk.Button(janela,text=botao,width=5,height=2,font=("Arial",18),command=lambda b=botao: clicar(b)).grid(row=linha,column=coluna)
    coluna += 1
    if coluna >3:
        coluna=0
        linha+=1
#Caixa de historico ao lado direito
historico_label= Tk.Label(janela,text="Histórico", font=("Arial",14,"bold"))
historico_label.grid(row=0,column=4,padx=10)
historico_text=Tk.Text(janela,width=25,height=10,font=("Arial",14))
historico_text.grid(row=1, column=4,rowspan=5,padx=10,pady=5)
janela.mainloop()