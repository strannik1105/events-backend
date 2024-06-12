class Iterator(type):
    def __iter__(self) -> None:
        for attr in dir(self):
            if not attr.startswith("__"):
                yield attr
