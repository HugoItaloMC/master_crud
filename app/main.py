from config.handler import Handler


class Post(Handler):

    def post(self):
        # REad content request
        content_body = self.request.body

        # Insert data by API method from JSON body
        self.api.post(content_body)


class Put(Handler):

    def put(self, id):
        # Read content request
        content_body = self.request.body
        url_parser = self.request.path.split('/')
        id_index = url_parser.index('produto') + 2
        id = int(url_parser[id_index])

        # Update date where id in database
        self.api.put(content_body, id=id)


class Getter(Handler):

    def get(self):
        # Request data
        response = self.api.getall()

        # Response data
        self.set_header('Content-type', 'application/json')
        self.write(response)


class Getan(Handler):

    def get(self, id):
        # Parser url
        url_parser = self.request.path.split('/')
        id_index = url_parser.index('home') + 1
        id = int(url_parser[id_index])
        # Request data
        response = self.api.getter(id=id)
        self.set_header('Content-type', 'application/json')
        self.write(response)


class Delete(Handler):

    def delete(self, id):
        url_parser = self.request.path.split('/')
        id_index = url_parser.index('produto') + 2
        id = int(url_parser[id_index])

        # Drop Data
        self.api.remove(id)