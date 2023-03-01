def main(a):
    """
    Check the natural number. Natural numbers are numbers used in counting.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    return a == int(abs(a)) != 0

print(main(3))