import unittest
from server import app

class TestChatbot(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_traducao_ingles_para_frances(self):
        texto_ingles = "Hello"
        resultado_esperado = "Bonjour"

        response = self.app.post('/traduzir', json={'texto': texto_ingles, 'target': 'fr'})
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['texto'], resultado_esperado)

    def test_traducao_frances_para_ingles(self):
        texto_frances = "Bonjour"
        resultado_esperado = "Hello"

        response = self.app.post('/traduzir', json={'texto': texto_frances, 'target': 'en'})
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['texto'], resultado_esperado)

if __name__ == '__main__':
    unittest.main()