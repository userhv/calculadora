from calculadora import Calculadora
import pytest

def test_soma_numeros_iguais():
  calculadora = Calculadora()
  resultado = calculadora.soma(1,1)
  assert resultado == 2

def test_soma_numeros_negativos():
  calculadora = Calculadora()
  resultado = calculadora.soma(-1,-1)
  assert resultado == -2

def test_soma_numeros_diferentes():
  calculadora = Calculadora()
  resultado = calculadora.soma(3,10)
  assert resultado == 13

def test_subtracao_numeros_negativos():
  calculadora = Calculadora()
  resultado = calculadora.subtracao(-11,-7)
  assert resultado == -4

def test_subtracao_numeros_positivos():
  calculadora = Calculadora()
  resultado = calculadora.subtracao(101,1)
  assert resultado == 100

def test_subtracao_com_zero():
  calculadora = Calculadora()
  resultado = calculadora.subtracao(0,-10)
  assert resultado == 10

def test_multiplicacao_numeros_positivos():
  calculadora = Calculadora()
  resultado = calculadora.multiplicacao(2,10)
  assert resultado == 20

def test_multiplicacao_numeros_negativos():
  calculadora = Calculadora()
  resultado = calculadora.multiplicacao(-2,-3)
  assert resultado == 6

def test_multiplicacao_por_zero():
  calculadora = Calculadora()
  resultado = calculadora.multiplicacao(0,2)
  assert resultado == 0

def test_divisao_numeros_positivos():
  calculadora = Calculadora()
  resultado = calculadora.divisao(4,2)
  assert resultado == 2

def test_divisao_numeros_grandes():
  calculadora = Calculadora()
  resultado = calculadora.divisao(256,2)
  assert resultado == 128

def test_divisao_por_zero():
  calculadora = Calculadora()
  with pytest.raises(ZeroDivisionError):
    calculadora.divisao(2,0)

def test_potencia_por_um():
  calculadora = Calculadora()
  resultado = calculadora.potencia(20000,1)
  assert resultado == 20000

def test_potencia_por_zero():
  calculadora = Calculadora()
  resultado = calculadora.potencia(20000,0)
  assert resultado == 1

def test_potencia_numero_positivo():
  calculadora = Calculadora()
  resultado = calculadora.potencia(3,2)
  assert resultado == 9

def test_potencia_numero_negativo_e_par():
  calculadora = Calculadora()
  resultado = calculadora.potencia(-2,4)
  assert resultado == 16

def test_potencia_numero_negativo_e_impar():
  calculadora = Calculadora()
  resultado = calculadora.potencia(-2,3)
  assert resultado == -8

def test_raiz_positiva():
  calculadora = Calculadora()
  resultado = calculadora.raiz(4,2)
  assert resultado == 2

def test_raiz_negativa():
  calculadora = Calculadora()
  with pytest.raises(Exception):
    calculadora.raiz(-4,2)

def test_raiz_indice_zero():
  calculadora = Calculadora()
  with pytest.raises(ZeroDivisionError):
    calculadora.raiz(4,0)

def test_raiz_de_um():
  calculadora = Calculadora()
  resultado = calculadora.raiz(4,1)
  assert resultado == 4

def test_raiz_expoente_indice_iguais():
  calculadora = Calculadora()
  resultado = calculadora.raiz(2**2,2)
  assert resultado == 2