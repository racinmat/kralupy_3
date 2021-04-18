from typing import Iterator, Dict, List, Union


def pow(x, y, z=None, /):
    r = x ** y
    if z is not None:
        r %= z
    return r


def baz():
    rest = (4, 5, 6)
    yield 1, 2, 3, *rest


class A:
    def __init__(self, b, c, d) -> None:
        super().__init__()
        self.b = b
        self.c = c
        self.d = d


def fib(n: int) -> Iterator[int]:
    a, b = 0, 1
    while a < n:
        print(f"going to yield {a}")
        yield a
        a, b = b, a + b


def sum_nums(a: int, b: int) -> int:
    return a + b


def merge_lists(a: List[int], b: List[int]) -> List[int]:
    return a + b


def merge_lists2(a: List[int], b: List[int], /) -> List[int]:
    return a + b


def return_and_print(a):
    print(a)
    return a


def fun(a=return_and_print(5)):
    return a * 2


def merge_lists3(a=None, b=None, /, c=None) -> List[int]:
    if c is None:
        c = [1]
    if b is None:
        b = [1]
    if a is None:
        a = [1]
    return a + b + c


def int_or_str(a: int) -> Union[str, int]:
    return "a is odd" if a % 2 else 0


if __name__ == '__main__':
    europe = {"Norway": "Oslo", "Spain": "Madrid"}
    africa = {"Egypt": "Cairo", "Zimbabwe": "Harare"}

    joined = europe | africa

    joined2 = europe.copy()
    joined2.update(africa)

    (joined2 := europe.copy()).update(africa)
    together = {}  # type: Dict[str, str]
    together |= europe
    together |= africa

    pow(2, 10)  # valid
    pow(2, 10, 17)  # valid
    pow(x=2, y=10)  # invalid, will raise a TypeError
    pow(2, 10, z=17)  # invalid, will raise a TypeError

    foo = 1
    bar = 2


    print("foo="+str(foo)+" bar="+str(bar))
    print(f"foo={foo} bar={bar}")
    print(f"{foo=} {bar=}")

    my_dict = dict(a=1, b=2)
    list(reversed(my_dict))
    list(reversed(my_dict.items()))

    sum_nums(1, 2)
    merge_lists([1, 2, 3], [4, 5])
    # merge_lists([1, 2, 3], [4, "5"])
    print(int_or_str(4))
    print(int_or_str(5))

    merge_lists([1, 2, 3], [4, 5])
    merge_lists(a=[1, 2, 3], b=[4, 5])
    merge_lists([1, 2, 3], b=[4, 5])

    merge_lists2([1, 2, 3], [4, 5])
    merge_lists2(a=[1, 2, 3], b=[4, 5])
    merge_lists2([1, 2, 3], b=[4, 5])

    merge_lists3([1, 2, 3], c=[4, 5])

    my_fib = fib(10)
    for i in my_fib:
        print(f"I got {i}")

    a, b = (1, 2)
    a, b, c = (1, 2, 3)
    a, *b, c, d = (1, 2, 3, 4, 5, 6)

    e = a, *b

    sum_nums(1, 2)
    b = (4, 2)
    sum_nums(*b)

