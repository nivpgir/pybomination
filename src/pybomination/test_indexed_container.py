from unpythonic.syntax import macros, test, test_raises, fail, error, warn, the
from unpythonic.test.fixtures import session, testset, terminate, returns_normally

with session("indexed container"):
    with testset():
        from indexed_container import IndexedContainer as C
        flat_dict = {"one": 1}
        test[C(flat_dict).one == 1]

        depth_one_dict = {"one": {"two": 2}}
        test[C(depth_one_dict).one.two == 2]
