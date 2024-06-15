from typing import Any, Iterator


class IteratorMeta(type):
    def __iter__(self) -> Iterator[Any]:
        for attr in self.__dict__.keys():
            if not attr.startswith("__"):
                yield getattr(self, attr)
