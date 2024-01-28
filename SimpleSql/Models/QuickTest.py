class Test():
    _testing = None

    def change(self, x):
        setattr(type(self), '_testing', x)


if __name__ == "__main__":
    test1 = Test()
    test2 = Test()
    print(f"{test1._testing} : {test2._testing}")
    test2.change("2")
    print(f"{test1._testing} : {test2._testing}")
    test1.change("1")
    print(f"{test1._testing} : {test2._testing}")
