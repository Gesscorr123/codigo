def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

n = int(input("Ingrese un número: "))
contador = 0
numero_actual = 2

while contador < n:
    if es_primo(numero_actual):
        print(numero_actual)
        contador += 1
    numero_actual += 1

print("hola mundo")