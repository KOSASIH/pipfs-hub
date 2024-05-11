# Web test file
import unittest

from app import app, db
from app.models import File, User


class TestWeb(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        app.config["WTF_CSRF_ENABLED"] = False
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"
        self.client = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_index(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_upload_file(self):
        response = self.client.post(
            "/upload",
            data={"username": "test_user", "file": ("test_file.txt", "test_file.txt")},
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(File.query.count() > 0)

    def test_file_list(self):
        file = File(
            name="test_file.txt", content="test_hash", user=User(username="test_user")
        )
        db.session.add(file)
        db.session.commit()
        response = self.client.get("/files")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"test_file.txt", response.data)


if __name__ == "__main__":
    unittest.main()
