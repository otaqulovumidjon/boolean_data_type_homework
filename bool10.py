def main(a):
    """
    Check that the number "a" is a perfect square.
    “a” soni mukammal kvadrat ekanligini tekshiring.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    return a == (a ** (1/2)) ** 2

print(main(121))