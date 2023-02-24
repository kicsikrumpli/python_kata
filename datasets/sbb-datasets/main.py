from pprint import pprint

from data import ist_daten_sbb
import json

def foo(a: int, b: str, c: bool) -> str:
    """
    This functions foos.
    :param a: is a
    :param b: is b
    :param c: is c
    :return: a coelho quote on programming
    """
    return "{} foo {foo}".format("!!!", foo=42)


if __name__ == '__main__':
    print(f"number of records in 'ist_daten_sbb': {len(ist_daten_sbb)}")
    pprint(ist_daten_sbb)

