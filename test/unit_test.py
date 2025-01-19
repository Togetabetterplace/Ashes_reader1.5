import unittest
from flask import Flask
from flask.testing import FlaskClient
from services.user_service import register, login, get_user_info
from services.conversation_service import create_conversation, get_conversation
from utils.github_search import search_github, download_repo
from utils.arXiv_search import arxiv_search
import os
import json

class TestUserService(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.client = self.app.test_client()

    def test_register(self):
        response = self.client.post('/api/register', json={
            'username': 'testuser',
            'password': 'testpassword',
            'email': 'testuser@example.com'
        })
        self.assertEqual(response.status_code, 201)

    def test_login(self):
        response = self.client.post('/api/login', json={
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('user_id', response.json)

class TestConversationService(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.client = self.app.test_client()

    def test_create_conversation(self):
        response = self.client.post('/api/conversations', json={'user_id': 1})
        self.assertEqual(response.status_code, 201)

    def test_get_conversation(self):
        response = self.client.get('/api/conversations/1')
        self.assertEqual(response.status_code, 200)

class TestGitHubSearch(unittest.TestCase):
    def test_search_github(self):
        results, repo_choices = search_github('tensorflow', 1, max_results=5)
        self.assertTrue(len(json.loads(results)) > 0)

    def test_download_repo(self):
        success = download_repo('tensorflow', 'tensorflow', '/path/to/save')
        self.assertTrue(success)

class TestArxivSearch(unittest.TestCase):
    def test_arxiv_search(self):
        results = arxiv_search('2101.06808', 1, translate=True, dest_language='zh-cn')
        self.assertTrue(len(json.loads(results)) > 0)

if __name__ == '__main__':
    unittest.main()
