import unittest

#def soma(numero1, numero2):
#	return numero1 + numero2
#def validador(numero):
#	return type(numero) == int

class TestDojoMethods(unittest.TestCase):

   lista = list(range(100))

  #for indice, valor in enumerate(lista):
  #  print "lista[%d] = %d" % (indice, valor)

    def test_soma(self):
    	self.assertEqual(soma(2,2), 4)



if __name__ == '__main__':
    unittest.main()
