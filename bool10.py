from math import sqrt
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
    return (a == int(sqrt(a)) ** 2) > 0

print(main(625))