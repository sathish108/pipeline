"""
This module is used for  creating flask  api
"""
from functools import wraps
from flask import Flask, request, jsonify, Response
flask_jenkins_app = Flask(__name__)
#languages=[{"name":"python"},{"name":"java"},{"name":"javascript"}]

def infra(*args, **dec_kwargs):
    global d1, d2, d3, d4, d5, d6, d7, d8
    d1 = dec_kwargs.get('cpuLimit', "210m")
    d2 = dec_kwargs.get('cpuRequest', "100m")
    d3 = dec_kwargs.get('image', "gcr.io/disney-218910/flask-app:latest")
    d4 = dec_kwargs.get('memoryLimit', "100M")
    d5 = dec_kwargs.get('memoryRequest', "75M")
    d6 = dec_kwargs.get('replicaCount', 1)
    d7 = dec_kwargs.get('serviceport',8086)
    d8 = dec_kwargs.get('servicetype', "LoadBalancer")

    def inner(original_func):
        @wraps(original_func)
        def wrapper(*args, **kwargs):
            # print(dec_kwargs['image'])
            # print('Wrapped function name:',func.__name__)
            # print('Arguments for kwargs: {}'.format(kwargs))
            print('original func return values', original_func(*args, **kwargs))
            res = original_func(*args, **kwargs)

        return wrapper

    return inner
    
    
# @infra(cpuLimit='75m', cpuRequest='100m', image='gcr.io/disney-218910/flask-app:latest', memoryLimit='100M',
#       memoryRequest='75M', replicaCount=3, serviceport=8086,
#       servicetype='LoadBalancer')
@infra(cpuLimit='300m', cpuRequest='100m', replicaCount=1)
def testing():
    pass

@flask_jenkins_app.route("/health-check")
def health_check():
    """
  This method is used  to check flask API is working or not
"""
    response = jsonify({'Message': 'Server is alive'})
    response.status_code = 200
    return response
@flask_jenkins_app.route("/lang", methods=["GET"])
def returnall():
    """
This method is used for to perform GET operation
"""
    languages = [{"name": "python"}, {"name": "java"}, {"name": "javascript"},{"name":"C#"}]
    return jsonify({"languages":languages})
@flask_jenkins_app.route("/lang", methods=["POST"])
def addone():
    """
This method is used for performing POST operation
"""
    languages = [{"name": "python"}, {"name": "java"}, {"name": "javascript"}]
    data = request.get_json()
    language = {"name":data['name']}
    languages.append(language)
    response = jsonify({"languages":languages})
    response.status_code = 200
    return response
@flask_jenkins_app.route("/lang/<string:name>", methods=["PUT"])
def editone(name):
    """
This method is used  to perform the PUT operation
    """
    languages = [{"name": "python"}, {"name": "java"}, {"name": "javascript"}]
    for language in languages:
        if language['name'] == name:
            data = request.get_json()
            language['name'] = data['name']
            return jsonify({"languages":languages})
@flask_jenkins_app.route("/lang/<string:name>", methods=["DELETE"])
def removeone(name):
    """
This method is used  to perform DELETE  operation
"""
    languages = [{"name": "python"}, {"name": "java"}, {"name": "javascript"}]
    for language in languages:
        if language['name'] == name:
            languages.remove(language)
            return jsonify({"languages":languages})

if __name__ == '__main__':
    flask_jenkins_app.run(host="0.0.0.0", debug=True, port=8086)
