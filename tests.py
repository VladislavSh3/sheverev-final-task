from flask_testing import TestCase
from app import app


class FlaskAppTestCase(TestCase):
    def create_app(self):
        # Возвращаем экземпляр приложения Flask для тестирования
        return app

    def test(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
