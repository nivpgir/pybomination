from unpythonic.test.fixtures import session, testset, terminate, returns_normally
from unpythonic.syntax import macros, test, test_raises, fail, error, warn, the

with session("indexed container"):
    # from indexed_container import IndexedContainer as C
    from indexed_container import IndexedContainer
    # TODO: make tests for `__eq__`, `__repr__` and `__str__` implementations
    with testset("getting a key by an attr"):
        my_dict = {"one": {"two": 2}}
        wrapped = IndexedContainer(my_dict)

        # getting a value from first level
        test[wrapped.one == {"two": 2}]

        # getting a nested value
        test[wrapped.one.two == 2]

    with testset("setting a key from an attr"):
        my_dict = {"one": 1}
        wrapped = IndexedContainer(my_dict)

        # setting a level one existing key
        wrapped.one = 2
        test[wrapped.one == 2]

        # setting a new level one key
        wrapped.mymy = "my"
        test[wrapped.mymy == "my"]

        # adding a nested collection still and then retrieving still returns a wrapped collection
        wrapped.nested = {"two": 2}
        test[wrapped.one.two == 2]

        # setting a nested existing key
        wrapped.one.two = 3
        test[wrapped.one.two == 3]

        # setting a new nested existing key
        wrapped.one.twothree = 23
        test[wrapped.one.twothree == 23]

        # setting a new nested key that didn't exist in a collection previously
        wrapped.one.three = 23
        test[wrapped.one.three == 23]

    with testset("the container is only a view for the inner collection"):
        my_dict = {"one": 1}
        wrapped = IndexedContainer(my_dict)

        # mutating the inner collection mutates the container
        my_dict["one"] = {"two": 2}
        test[wrapped.one.two == 3]

        # mutating the container mutates the inner collection
        my_dict.one.two = 3
        test[my_dict["one"]["two"] == 3]

