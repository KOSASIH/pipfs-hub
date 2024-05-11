# API test file
import os
import tempfile
import shutil
import unittest
from app import app, db
from app.models import User, File
from app.services.encryption import encrypt_file

class TestAPI(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        self.client = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_upload_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = os.path.join(temp_dir, 'test_file.txt')
            with open(file_path, 'w') as f:
                f.write('Test file content')
            with open(file_path, 'rb') as f:
                file = f.read()
            encrypted_file = encrypt_file(file)
            response = self.client.post('/files', data={
                'username': 'test_user',
                'file': (file_path, 'test_file.txt')
            })
            self.assertEqual(response.status_code, 200)
            self.assertTrue(File.query.count() > 0)

    def test_download_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = os.path.join(temp_dir, 'test_file.txt')
            with open(file_path, 'w') as f:
                f.write('Test file content')
            with open(file_path, 'rb') as f:
                file = f.read()
            encrypted_file = encrypt_file(file)
            ipfs_hash = IPFS.add(encrypted_file)
            file = File(name='test_file.txt', content=ipfs_hash, user=User(username='test_user'))
            db.session.add(file)
            db.session.commit()
            response = self.client.get(f'/files/{ipfs_hash}')
            self.assertEqual(response.status_code, 200)
            self.assertTrue(response.content)

if __name__ == '__main__':
    unittest.main()
