def info():
    dadosPessoais = ["Nome",10,10]
    perguntas = ["Digite seu nome: ", "Digite seu peso: ","Digite sua altura: "]
    for i in range (len(perguntas)):
        print(perguntas[i])
        dadosPessoais[i] = input()
    return dadosPessoais

def calculo(peso,altura):
    classificacao = ["Magreza grave","Magreza","Normalidade","Sobrepeso","Obesidade","Obesidade grave"]
    medidaIndice = [17,18,26,29,30,31]
    imc = round(peso/altura**altura,2)
    c = 0
    for i in range (len(classificacao)):
        if(imc > medidaIndice[i]):
            c = i
    resultado = [imc,classificacao[c]] 
    return resultado

Dados = info()
imc = calculo(float(Dados[1]),float(Dados[2]))
print(Dados[0] + ", com " + Dados[1] + "KG e " + Dados[2] + " metros de altura possuí índice igual a " + str(imc[0]) + ", considerado de: " + str(imc[1]))