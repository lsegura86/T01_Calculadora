#Creado por Luis Segura
import calculadora
import pytest

def test_sumar():
    #Se comprueba el funcionamiento del metodo de SUMAR
    res = calculadora.sumar(1.0, 1.0)
    print(res)
    assert res == 2.0
    res = calculadora.sumar(1, 10)
    print(res)
    assert res == 11
    res =  calculadora.sumar(-1, -20)
    print(res)
    assert res == -21


    #Se comprueba el funcionamiento del metodo RESTAR
def test_restar():
    res = calculadora.restar(10.0, 1.0)
    print(res)
    assert res == 9.0
    res = calculadora.restar(1, 10)
    print(res)
    assert res == -9
    res =  calculadora.restar(-1, -20)
    print(res)
    assert res == 19

    #Se comprueba el funcionamiento del metodo MULTIPLICAR
def test_multiplicar():
    res = calculadora.multiplicar(10.0, 1.0)
    print(res)
    assert res == 10.0
    res = calculadora.multiplicar(2, 10)
    print(res)
    assert res == 20
    res =  calculadora.multiplicar(0, -20)
    print(res)
    assert res == 0
    res =  calculadora.multiplicar(1, -20)
    print(res)
    assert res == -20

    #Se comprueba el funcionamiento del metodo DIVIDIR
def test_dividir():
    res = calculadora.dividir(10.0, 1.0)
    print(res)
    assert res == 10.0
    res = calculadora.dividir(2, 10)
    print(res)
    assert res == 0.2
    res =  calculadora.dividir(0, -20)
    print(res)
    assert res == 0
    res =  calculadora.dividir(1, -20)
    print(res)
    assert res == -0.05
    res =  calculadora.dividir(10, 0)
    print(res)
    assert res == 'ZeroDivisionError'

    #Se comprueba el funcionamiento del metodo VALIDAR_ENTRADA
def test_validar_entrada():
    res = calculadora.valida_entrada(['1', '+', '2'])
    assert res == True
    print(res)
    res = calculadora.valida_entrada(['1', '-', '2'])
    assert res == True
    print(res)
    res = calculadora.valida_entrada(['1', '*', '2'])
    assert res == True
    print(res)
    res = calculadora.valida_entrada(['1', '/', '2'])
    assert res == True
    print(res)
    res = calculadora.valida_entrada(['1', '.', '2'])
    assert res == False
    print(res)
    res = calculadora.valida_entrada(['1', '2', '2'])
    assert res == False
    print(res)
    res = calculadora.valida_entrada(['1', 'e', '2'])
    assert res == False
    print(res)
    res = calculadora.valida_entrada(['1', '+', '2', '2'])
    assert res == False
    print(res)
    res = calculadora.valida_entrada(['1', '2'])
    assert res == False
    print(res)
    res = calculadora.valida_entrada(['1'])
    assert res == False
    print(res)
    res = calculadora.valida_entrada([])
    assert res == False
    print(res)