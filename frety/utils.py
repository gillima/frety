class CallableCollection(list):
    def __call__(self, *args, **kwargs):
        for callback in self[:]:
            callback(*args, **kwargs)

    def __iadd__(self, other):
        self.append(other)
        return self

    def __isub__(self, other):
        self.remove(other)
        return self
