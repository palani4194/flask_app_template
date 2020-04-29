import unittest

import {{cookiecutter.application_name}}


class {{cookiecutter.application_name.capitalize()}}TestCase(unittest.TestCase):

    def setUp(self):
        self.app = {{cookiecutter.application_name}}.app.test_client()

    def test_index(self):
        rv = self.app.get('/')
        self.assertIn('Welcome to {{cookiecutter.application_name}}', rv.data.decode())


if __name__ == '__main__':
    unittest.main()
