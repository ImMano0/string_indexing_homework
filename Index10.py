def main(s):
    """
    A string of five numbers is given. Find the sum of its numbers.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
 d = int(s)

    d1  = d % 10
    d //= 10

    d2  = d % 10
    d //= 10

    d3  = d % 10
    d //= 10

    d4  = d % 10
    d //= 10

    d5  = d % 10
    d //= 10 

    return d1 + d2 + d3 + d4 + d5
print(main('12305'))