class Singleton(type):
    # Controle de instâncias de objetos

    def __new__(meta, name, bases, class_dict):
        return type.__new__(meta, name, bases, class_dict)

    def __call__(cls, *args, **kwargs):
        # To behaviours from singletons patterns in objects Python
        # Know here is writening from magic method `__call__`
        if not hasattr(cls, '__instance'):
            cls.__instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.__instance


if __name__ == '__main__':
    inst1 = Singleton()
    inst2 = Singleton()
    print(id(inst1),
          id(inst2))
