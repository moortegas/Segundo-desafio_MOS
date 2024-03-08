print("Bienvenido a la calculadora de IMC ")
print("")

peso = float(input("Ingresa tu peso en KG: "))
altura = float(input("Ingresa tu altura en CM: "))

# Determinar el IMC
imc = peso / ((altura/100)**2)

print("Su IMC es: {:.2f}".format(imc))
# print(f"Su IMC es : {imc:.2f}")

# def clasificar_imc(imc):
if imc < 18.5:
    print ("La clasificación OMS es: Bajo Peso") 
elif 18.5 <= imc < 25:
    print ("La clasificación OMS es: Adecuado")
elif 25 <= imc < 30:
    print ("La clasificación OMS es: Sobrepeso")
elif 30 <= imc < 35:
    print ("La clasificación OMS es: Obesidad Grado I")
elif 35 <= imc < 40:
    print ("La clasificación OMS es: Obesidad Grado II")
else:
    print ("La clasificación OMS es: Obesidad Grado III")


    

