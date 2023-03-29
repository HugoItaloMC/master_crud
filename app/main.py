from abc import ABC

from app.api import API
from config._2handler import Index

renderer = Index


class Home(API):

    def get(self):
        self.service(1)


class Post(API):

    def get(self):
        self.service(2)

    def post(self):
        self._post()


class Put(API):

    def get(self):
        self.service(1)

    def update(self):
        self._put()


class Delete(API):

    def delete(self):
        self._remove()
