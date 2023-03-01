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
    return a == abs(a) and a != 0 and a == int(a)

print(main(3))