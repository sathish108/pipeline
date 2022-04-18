"""
This  module  is used for checking the functionality
"""
import unittest
from werkzeug.test import create_environ, run_wsgi_app
from src.main.python.app import flask_jenkins_app
class TestCompInitTimePeriods(unittest.TestCase):
    """
    This class is used for writing the testcases
    """
    def test_a_health_check(self):
        """
        This method is used for checking the health-check API
        """
        environ_1 = create_environ('/health-check')
        result = run_wsgi_app(flask_jenkins_app, environ_1, True)
        self.assertEqual(result[0], [b'{"Message":"Server is alive"}\n'])

    def test_b_get(self):
        """
         This method is used for checking the GET request
        """
        environ_2 = create_environ("/lang")
        result = run_wsgi_app(flask_jenkins_app, environ_2, True)
        self.assertEqual(result[0], [b'{"languages":[{"name":"python"},\
{"name":"java"},{"name":"javascript"},{"name":"C#"}]}\n'])

    def test_c_post(self):
        """
         This method is used for checking the  POST request
        """

        data = {"method": "POST", "json": {"name": "c"}}
        environ = create_environ("/lang", **data)
        result = run_wsgi_app(flask_jenkins_app, environ, True)
        self.assertEqual(result[0],
                         [b'{"languages":[{"name":"python"},{"name":"java"},\
{"name":"javascript"},{"name":"c"}]}\n'])
    def test_d_put(self):
        """
       This method is used for checking the PUT request
        """
        data = {"method": "PUT", "json": {"name": "Go"}}
        environ_4 = create_environ("/lang/python", **data)
        result = run_wsgi_app(flask_jenkins_app, environ_4, True)
        self.assertEqual(result[0], [b'{"languages":[{"name":"Go"},{"name":"java"},\
{"name":"javascript"}]}\n'])
    def test_e_delete(self):
        """
        This method is used for checking  the DELETE request
        """
        data = {"method": "DELETE"}
        environ_5 = create_environ("/lang/java", **data)
        result = run_wsgi_app(flask_jenkins_app, environ_5, True)
        self.assertEqual(result[0], [b'{"languages":[{"name":"python"},{"name":"javascript"}]}\n'])

#if __name__ == '__main__':
    # unittest.main()
