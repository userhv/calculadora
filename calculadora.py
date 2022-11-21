class Calculadora:
  def soma(self, op1, op2):
    return op1 + op2

  def subtracao(self, op1, op2):
    return op1 - op2

  def divisao(self, op1, op2):
    if op2 == 0:
      raise ZeroDivisionError
    else:
      return op1 / op2

  def multiplicacao(self,op1, op2):
    return op1 * op2

  def potencia(self, op1, op2):
    return op1 ** op2

  def raiz(self, radicando, indice):
    if radicando < 0:
      raise Exception('Não há raiz de número negativo')
    else:
      return radicando ** (1/indice)