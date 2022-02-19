from datetime import date
import sys 
Cabecalho = open("Relatórios.txt", "a")
print("\n" + 50*"=" + "\n" + "RELATÓRIO DO DIA: " + str(date.today()) + "\n" + 50*"=" + "\n")
Cabecalho.write("\n" + 50*"=" + "\n" + "RELATÓRIO DO DIA: " + str(date.today()) + "\n" + 50*"=" + "\n")
Cabecalho.close()

def Perguntar():
    Sim = ["Sim","sim","S","s","SIM"]
    if input("Deseja usar o Programa? S/N \n") in Sim:
        Relatorio()
    sys.exit()

def Relatorio():

    def informacoes():
        dadosPessoais = [("Nome").capitalize,"Curso",10,10,10]
        global perguntas
        perguntas = ["Digite seu nome: ","Digite sua turma: ","Digite sua idade: " , "Digite seu peso: ","Digite sua altura: "]
        for i in range (len(perguntas)):
            dadosPessoais[i] = input(perguntas[i])
        return dadosPessoais

    def calcular(peso,altura):
        classificacao = ["Magreza grave","Magreza","Normalidade","Sobrepeso","Obesidade","Obesidade grave"]
        medidaIndice = [17,18,24,29,30,31]
        imc = round(peso/altura**altura,2)
        c = 0
        for i in range (len(classificacao)):
            if(imc > medidaIndice[i]):
                c = i
        calculo = [imc,classificacao[c]] 
        return calculo

    Dados = informacoes()
    imc = calcular(float((Dados[len(perguntas)-2]).replace(",",".")),float((Dados[len(perguntas)-1]).replace(",",".")))
    Resultado = "\n" + " Nome: " + Dados[0]+"\n" + " Turma: " + Dados[1]+"\n" + " Idade: " + Dados[2]+"\n" + " Peso: " + Dados[3]+" kg \n" + " Altura:" + Dados[4]+" metros \n" + " Índice: " + str(imc[0])+"\n" + " Considerado de: " + str(imc[1])+"\n"
    print(Resultado)
    Relatorio = open("Relatórios.txt", "a")
    Relatorio.write(Resultado)
    Relatorio.close()
    Perguntar()

Relatorio()