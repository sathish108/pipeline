import requests as reqs
import unittest
import re
import sys



class funcTest(unittest.TestCase):
    
    def test_A_health_check(self):
        
        url = 'http://' + self.ip
        url = url.strip(' \t\n\r')
        url = url + ':' + self.port
        url = url.strip(' \t\n\r')
        url = url + '/health-check'
        response = reqs.get(url)
        st_code = response.status_code
        result = response.text
        res = re.sub(r"[ \n\t\s]*", "", result)
        # print(result)
        self.assertEqual(res, '{"Message":"Serverisalive"}')

    def test_B_get(self):
            
        url = 'http://' + self.ip
        url = url.strip(' \t\n\r')
        url = url + ':' + self.port
        url = url.strip(' \t\n\r')
        url = url + '/lang'
        response = reqs.get(url)
        st_code = response.status_code
        result = response.text
        print(result)
        print(type(result))
        res = re.sub(r"[\n\t\s]*", "", result)
        # print(res)
        self.assertEqual(res, '{"languages":[{"name":"python"},{"name":"java"},{"name":"javascript"},{"name":"C#"}]}')

    def test_C_post(self):
        
        json = {'name': 'C'}
        url = 'http://' + self.ip
        url = url.strip(' \t\n\r')
        url = url + ':' + self.port
        url = url.strip(' \t\n\r')
        url = url + '/lang'
        response = reqs.post(url, json=json)
        print(response.json())
        print(response.status_code)
        result = response.text
        # print(result)
        res = re.sub(r"[\n\t\s]*", "", result)
        print(res)
        self.assertEqual(res,'{"languages":[{"name":"python"},{"name":"java"},{"name":"javascript"},{"name":"C"}]}')

    def test_E_put(self):
        
        json = {"name": "pyt"}
        url = 'http://' + self.ip
        url = url.strip(' \t\n\r')
        url = url + ':' + self.port
        url = url.strip(' \t\n\r')
        url = url + '/lang/python'
        response = reqs.put(url, json=json)
        print(response.status_code)
        print(response.text)
        result = response.text
        res = re.sub(r"[\n\t\s]*", "", result)
        print(res)
        self.assertEqual(res, '{"languages":[{"name":"pyt"},{"name":"java"},{"name":"javascript"}]}')

    def test_F_delete(self):
        
        url = 'http://' + self.ip
        url = url.strip(' \t\n\r')
        url = url + ':' + self.port
        url = url.strip(' \t\n\r')
        url = url + '/lang/java'
        response = reqs.delete(url, data=None, json=None)
        print(response.status_code)
        print(response.text)
        result = response.text
        res = re.sub(r"[\n\t\s]*", "", result)
        print(res)
        self.assertEqual(res, '{"languages":[{"name":"python"},{"name":"javascript"}]}')


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

# unittest trying to read the command line arguments you use. You can solve it by reading the arguments and then deleting them before calling unittest.main()
