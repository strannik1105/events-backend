class Iterator(type):
    def __iter__(self) -> None:
        for attr in self.__dict__.keys():
            if not attr.startswith("__"):
                yield getattr(self, attr)
