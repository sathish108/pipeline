import requests as reqs
import unittest
import sys
import re
from requests.exceptions import Timeout


class funcTest(unittest.TestCase):
    def test_health_check(self):
        url = 'http://' + self.ip
        url = url.strip(' \t\n\r')
        url = url + ':' + self.port
        url = url.strip(' \t\n\r')
        url = url + '/health-check'
        try:
            response = reqs.get(url, timeout=5)
            st_code = response.status_code
            result = response.text
        except Timeout as ex:
            print("Exception Raised", ex)
        # print(result)
        res = re.sub(r"[ \n\t\s]*", "", result)
        # print(result)
        self.assertEqual(res, '{"Message":"Serverisalive"}')


if __name__ == '__main__':
    input_file = open(sys.argv[1], 'r')
    c = input_file.readlines()
    x = []
    for i in c:
        ip = i
        x.append(i)
        print(i)

    input_file.close()
    del sys.argv[1:]
    funcTest.ip = x[0]
    funcTest.port = x[1]
    unittest.main()
