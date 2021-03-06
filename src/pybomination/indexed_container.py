from collections.abc import Mapping, Sequence
class MappingWrapper:
    def __init__(self, mapping):
        self._inner = mapping

    def __iter__(self):
        return ((k, v) for k, v in self._inner.items())

    def __getitem__(self, loc):
        return self._inner[loc]

    def values(self):
        return (v for v in self._inner.values())

    def locs(self):
        return (k for k in self._inner.keys())

class SequenceWrapper:
    def __init__(self, sequence):
        self._inner = sequence

    def __iter__(self):
        return ((i, e) for i, e in enumerate(self._inner))

    def __getitem__(self, loc):
        return self._inner[loc]

    def values(self):
        return (e for e in self._inner)

    def locs(self):
        return (i for i in range(len(self._inner)))

class IndexedContainer(object):

    def __init__(self, container):
        self._inner = _wrap(container)

    def __getattribute__(self, attr_name):
        inner = object.__getattribute__(self, "_inner")
        if attr_name in inner.locs():
            item = inner[attr_name]
            try:
                return object.__class__(self)(item)
            except ValueError as _ve:
                return item

        raise AttributeError


    def __getitem__(self, loc):
        return self._get_inner_val(loc)


def _wrap(container):
    if isinstance(container, Mapping):
        return MappingWrapper(container)
    elif isinstance(container, Sequence):
        return SequenceWrapper(container)

    raise ValueError


def _get_wrapped_inner_val(loc):
    return IndexedContainer(self._get_inner_val(loc))


def _get_inner_val(loc):
    return self._inner[loc]
