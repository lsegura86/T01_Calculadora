# Definicion del Metodo para efectuar la Suma
def sumar(num_a, num_b):
    return num_a + num_b

# Definicion del Metodo para efectuar la Resta
def restar(num_a, num_b):
    return num_a - num_b

# Definicion del Metodo para efectuar la Multiplicacion
def multiplicar(num_a, num_b):
    return num_a * num_b

# Definicion del Metodo para efectuar la Division
def dividir(num_a, num_b):
    try:
        return num_a / num_b
    except ZeroDivisionError:
        return 'ZeroDivisionError'

#Diccionario para las operaciones a realizar
operadores = {'+':sumar,
             '-':restar,
             '*':multiplicar,
             '/':dividir}

#Valida el formato de la entrada digitada por el usuario
def valida_entrada(entrada):
    if(len(entrada) == 3 and entrada[1] in operadores.keys()):
        try:
            float(entrada[2])
            float(entrada[0])
            return True
        except:
            return False
    else:
        return False


print('#############################################\n'
      '########## Bienvenidos a la PyCalc ##########\n'
      '#############################################')
print('#### Con esta calculadora podrá realizar ####\n'
      '### las 4 operaciones básicas(+, -, *, /) ###\n'
      '#############################################')


#Variable para recursividad del ciclo
ejecucion = True
while ejecucion:
    entrada_operacion = input('\nDigite la operacion a realizar, ejemplo: 1 + 2:   ')
    entrada_operacion = entrada_operacion.split() #Crea la lista de lo digitado

    #Valida lo digitado por el usuario
    if(valida_entrada(entrada_operacion)):
        numero_a = float(entrada_operacion[0])
        operacion = entrada_operacion[1]
        numero_b = float(entrada_operacion[2])

        resultado = operadores[operacion](numero_a,numero_b)
        if resultado == 'ZeroDivisionError':
            print('\nMatemáticamente no es posible la división entre 0')
        else:
            print(f'\nEl resultado de la operacion {numero_a} {operacion} {numero_b} es: {resultado} \n')
    else:
        print('La operación no es válida, favor verifique el formato')

    #Desea el usuario ejecutar otra operacion
    ejecucion = input('Desea realizar otra operacion? Si/No:  ')
    if ejecucion == 'No':
        ejecucion = False

