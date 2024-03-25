import unittest

class TestCalculator(unittest.TestCase):  #classe que terá os casos de testes
    #setup
    def setUpClass():  
        print("Start")

    #tests
    def test_sun(self):
        self.assertEqual(1+1, 2)

    #tests
    def test_sub(self):
        self.assertEqual(2-1, 1)

    #tear down
    def tearDownClass():
        print("End")

if __name__ == '__main__':#diz que essa classe é a classe principal e ajuda o unittest a dizer que aqui tem tests para executar
    unittest.main()




