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
    return a == int(abs(a)) != 0

print(main(3))