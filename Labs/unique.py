class Unique(object):
    def __init__(self, items, **kwargs):
        self._ignore_case = kwargs.get('ignore_case', False)
        self._iterator = iter(items)
        self._seen = set()

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            item = next(self._iterator)  # поднимет StopIteration, когда всё кончится
            key = item
            if self._ignore_case and isinstance(item, str):
                key = item.lower()

            if key not in self._seen:
                self._seen.add(key)
                return item
