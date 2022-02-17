print("Digite seu peso: ")
peso = input()
print("Digite sua altura: ") 
altura = input()
valores, alerta = [17,18,26,30,29],["O indíce é de magreza severa","O índice é de magreza","O índice está normal","O índice é de obesidade","O índice é de obesidade mórbida"]

def calcular (p, a):
    resultado = p / a*a
    return resultado
    
calcular (peso, altura)
if(calcular.resultado < valores[0]):
   print(alerta[0])
elif(calcular.resultado < valores[1]):
   print(alerta[1])   
elif(calcular.resultado < valores[2]):
   print(alerta[2])
elif(calcular.resultado < valores[3]):
   print(alerta[3])
else:
   print(alerta[4])