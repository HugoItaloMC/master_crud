from typing import Any
from tornado import httputil

from app.model import Calcados
from abstract.pagine import APIMeta


class API(APIMeta):
    @staticmethod
    def _post(self):

        produto: Calcados = Calcados

        nome = self.get_argument('...', None)
        marca = self.get_argument('...', None)
        modelo = self.get_argument('...', None)
        preco = self.get_argument('...', None)
        tamanho = self.get_argument('...', None)

        produto.first_name = nome
        produto.mind_name = marca
        produto.last_name = modelo
        produto.price = preco
        produto.size = tamanho
        produto.manager(opp='POST')
        self.redirect('index.html')

    def _put(self, id):

        produto: Calcados = Calcados
        nome = self.get_argument('...', None)
        marca = self.get_argument('...', None)
        modelo = self.get_argument('...', None)
        preco = self.get_argument('...', None)
        tamanho = self.get_argument('...', None)

        produto.first_name = nome
        produto.mind_name = marca
        produto.last_name = modelo
        produto.price = preco
        produto.size = tamanho

        produto.manager('PUT')
        self.redirect('index.html')

    def _remove(self, id):
        produto: Calcados = Calcados
        produto.get_an(id)
        produto.manager('DELETE')
        self.redirect('index.html')
