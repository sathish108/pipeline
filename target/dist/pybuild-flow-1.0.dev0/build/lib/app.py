"""
This module is used for  creating flask  api
"""
from flask import Flask, request, jsonify, Response
flask_jenkins_app = Flask(__name__)
#languages=[{"name":"python"},{"name":"java"},{"name":"javascript"}]

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
    languages = [{"name": "python"}, {"name": "java"}, {"name": "javascript"}]
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
