def inputArgs(first, second, third=3, *args, **kwargs):
    print("first: " + str(first))
    print("second: " + str(second))
    print("third: " + str(third))
    for arg in args:
        print("ARG: " + str(arg))
    for (k, v) in kwargs.items():
        print("KEY: " + str(k) + ", VALUE: " + str(v))


inputArgs(5, "second", "third", 2, 5, foo="bar", baz="bippy")
