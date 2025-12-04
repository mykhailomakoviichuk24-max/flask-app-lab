import unittest
from app import app, db, bcrypt
from app.auth.models import User

class AuthTestCase(unittest.TestCase):
    def setUp(self):
        """Налаштування перед кожним тестом"""
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
        
        db.create_all()

    def tearDown(self):
        """Очищення після кожного тесту"""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_register_page_loads(self):
        """Перевірка: сторінка реєстрації завантажується"""
        response = self.app.get('/register')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Register', response.data)

    def test_login_page_loads(self):
        """Перевірка: сторінка входу завантажується"""
        response = self.app.get('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login', response.data)

    def test_user_registration(self):
        """Перевірка: реєстрація нового користувача"""
        response = self.app.post('/register', data={
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'password123',
            'confirm_password': 'password123'
        }, follow_redirects=True)
        
        self.assertEqual(response.status_code, 200)
        
        user = User.query.filter_by(username='testuser').first()
        self.assertIsNotNone(user)
        self.assertEqual(user.email, 'test@example.com')

    def test_login_logout(self):
        """Перевірка: вхід та вихід користувача"""
        
        hashed_pw = bcrypt.generate_password_hash('password123').decode('utf-8')
        user = User(username='loginuser', email='login@test.com', password=hashed_pw)
        db.session.add(user)
        db.session.commit()

        
        response = self.app.post('/login', data={
            'email': 'login@test.com',
            'password': 'password123'
        }, follow_redirects=True)
        
        self.assertIn(b'success', response.data) 

        
        response = self.app.get('/logout', follow_redirects=True)
        self.assertIn(b'info', response.data) 

if __name__ == "__main__":
    unittest.main()