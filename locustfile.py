from locust import HttpLocust, TaskSet, task
from flask import json


class UserBehaviour(TaskSet):

    @task(10)
    def returnall(self):
        self.client.get("/lang")

    @task(20)
    def health_check(self):
        self.client.get("/health-check")
        
    @task(30)
    def add_one(self):
        headers = {'content-type': 'application/json', 'Accept-Encoding': 'gzip'}
        self.client.post(url="/lang", data=json.dumps({
            "name": "ruby"
        }), headers=headers)

    @task(30)
    def edit_one(self):
        print(" in method edit")
        headers = {'content-type': 'application/json', 'Accept-Encoding': 'gzip'}
        # self.client.put(url="/lang/<string:name>", data=json.dumps({
        #     "name": "ruby"}), headers=headers)
        self.client.put(url="/lang/python", data=json.dumps({
            "name": "ruby"}), headers=headers)

    @task(10)
    def remove_one(self):
        headers = {'content-type': 'application/json', 'Accept-Encoding': 'gzip'}
        # self.client.delete(url="/lang/<string:name>", data=json.dumps({
        #     "name": "ruby"}), headers=headers)
        self.client.delete(url="/lang/python",headers=headers)

class WebsiteUser(HttpLocust):
    
    task_set = UserBehaviour
    min_wait = 5000
    max_wait = 15000
