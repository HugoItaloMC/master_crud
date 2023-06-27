
class Method:

    def __set__(self, instance):
        return lambda content_type: instance.api.sender_header(content_type=content_type)

    def __get__(self, instance, owner):
        return self.__set__(instance)

    def __call__(self, *args):
        return self.__set__(args)
