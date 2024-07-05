"""
        iterable:-

            __iter__() or __getitems__()

        iterator :-

            __next__()

        iteration :-

            all process by iterable and iteration


"""

# iterator


# str = "gmc"
# ire = iter(str)
# print(ire.__next__())
# print(ire.__next__())
# print(ire.__next__())


#generator  # we use loop  but loop gives number on time or run time

def generator(n):
    for i in range(n):
        yield i

if __name__ == '__main__':
    g = generator(10)
    print(g.__next__())
    print(g.__next__())
    print(g.__next__())
    print(g.__next__())
    print(g.__next__())
    print(g.__next__())
    print(g.__next__())
    print(g.__next__())