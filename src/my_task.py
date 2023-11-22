from celery import Task
from proj.custom_request import MyRequest


class MyTask(Task):
    Request = MyRequest  # you can use a FQN 'my.package:MyRequest'