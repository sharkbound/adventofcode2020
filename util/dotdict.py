from collections import UserDict


class DotDict(UserDict):
    def __getattr__(self, item):
        return self[item]

    def __setattr__(self, key, value):
        if key == 'data':
            self.__dict__[key] = value
        else:
            self[key] = value

    def is_type(self, key, required_type):
        return isinstance(self.get(key), required_type)
