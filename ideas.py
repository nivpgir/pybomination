

import json

parse_out = json.loads("text.json")
ds_name = "text.txt"
foo3_contains_none = any(e is None for e in
                         [k, v is None for k, v in parse_out["k2"]["k3"]["k4"]["foo3"].items()
                          if k == "foo3" ])



d = {"k1": 1, "k2": {"k3": {"k4":[{"foo": "bar"}, {"foo2": "bar2"}, {"foo3": [0,1,2,3]}]}}}

d.k2.k3.k4.*.foo3 =["k2": {"k3": {"k4": [None, None, {"foo3": [0,1,2,3]}]}}]

d.k2.k3.k4.foo3 = {"k2": {"k3": {"k4": [{"foo3": [0,1,2,3]}]}}}
d.k2.k3.k4.foo3 = ["k2 - k3 - k4": [{"foo3": [0,1,2,3]}]]

[_a-zA-Z][_0-9A-Za-z]*

d.k2.k3.k4


class MyDict:

    def __init__(self, inner_dict):
        self._inner = inner_dict

    def __or__(self, other):
        pass

    def __matmul__(self, other):
        isinstance(other, dict)
        return MyDict(self._inner[other])

    def __getattribute(self, other)
        return self._inner[other]

    def quux(*args):
        return copy.deepcopy(self._inner)

# Mylist
class Map:
    def __init__(self, func):
        self._func = func

    def __or__(self, other):
        return [self._foo(e) for e in other]

a @ ... @ d

a.STAR.r
class Ellipsis: pass

... == Ellipsis()

md = MyDict(d)
md | k2 | k3 | k4.find(key="foo3") @ foo4

class Star:
    def __init__(self, match):
        self._to_match = match

    def __call__(self, args):
        return MyDict([e for e in args if e == self._to_match])

star = Star()
stars = s(1,2,3)
md | k2 | k3 | Star("foo3")

x1, x2 == (1, 2)
flunc = lambda x1, x2: any(e is None for e in v)
flunc = lambda x1, x2: e = blabla(v) ; any(e is None for e in v)
flunc(*(1, 2))


d.k2.k3.k4 | Select(lambda d: "foo3" in d) | Map(lambda lv: any(e is None for e in lv))

# underscore internally transforms to a `Select` and the next condition is determined by the attribute access of the select
d.k2.k3.k4._.foo3

# get_item returns a select, where the predict is determined by the value given inside the braces
d.k2.k3.k4[...].foo3

# same as previous, but can select by both key and value (hence the argument is a tuple)
# but that applies only filtering, without, access, so the key must also be accessed later
d.k2.k3.k4.["foo3",...].foo3

# doesn't return just the leaf value, but also the path that led to it.
# this requires us to call a method on `d`, so we won't be able to select keys directly from it,
# we would need to have methods that give us a *different* wrapped dict, which does
# give access to nested values using the dot notation
d.with_path().k2.k3.k4.["foo3",...].foo3
