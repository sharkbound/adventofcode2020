from collections import UserDict

__all__ = [
    'DotDict'
]


class DotDict(UserDict):
    def __getattr__(self, item):
        return self[item]

    def __setattr__(self, key, value):
        if key == 'data':
            self.__dict__[key] = value
        else:
            self[key] = value

    def __repr__(self):
        init_args = ', '.join(f'{key}={value!r}' for key, value in self.items())
        return f'{self.__class__.__name__}({init_args})'

    def is_type(self, key, required_type):
        return isinstance(self.get(key), required_type)
