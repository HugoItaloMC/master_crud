# The interfaces to rest
class Post:
    # Read Http Body
    # Post new data in database

    def __set__(self, instance):
        return lambda request_body: instance.api.post(request_body)

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.__set__(instance)


class Put:
    # Read content request body
    # Update tuple where id
    def __set__(self, instance):
        def read_id(id):
            # Parser url to get `id`
            url_parser = instance.request.path.split('/')
            id_index = url_parser.index('produto') + 2
            return url_parser[id_index]  # Find id from index in end-point

        return lambda id: instance.api.put(instance.request.body, read_id(int(id)))

    def __get__(self, instance, owner):
        return self.__set__(instance)

    def __call__(self, *args):
        return self.__set__(args)


class GetAll:
    # Request data in database
    # Response data in output HTTP Body

    def __set__(self, instance):
        instance.set_header('Content-type', 'application/json')  # Http Body to JSON
        return lambda response: instance.write(response)  # OUTPUT Response HTTP Body

    def __get__(self, instance, owner):
        if instance is None: return self
        return self.__set__(instance)


class GetAn:
    # Request data in database where id
    # Response data in output Http Body
    def __set__(self, instance):
        def read_id(id):
            # Parser url to get `id`
            url_parser = instance.request.path.split('/')
            id_index = url_parser.index('home') + 1
            id = int(url_parser[id_index])

            # Read database where id
            response = instance.api.getter(id)
            return response  # output data
        instance.set_header('Content-type', 'application/json')  # Body HTTP to JSON
        return lambda id: instance.write(read_id(id))  # Output Response HTTP Body

    def __get__(self, instance, owner):
        if instance is None: return self
        return self.__set__(instance)

    def __call__(self, *args):
        return self.__set__(args)

