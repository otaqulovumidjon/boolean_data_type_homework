def main(a):
    """
    Check the natural number. Natural numbers are numbers used in counting.
    Natural sonni tekshiring. Natural sonlar sanashda ishlatiladigan sonlardir.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    a = (a == abs(a) and a != 0)
    return a

print(main(1))
print(main(0))
print(main(-1))