def rasterize(func: callable, xDomain: (float, float), yDomain: (float, float)) -> set[(float, float)]:
    """
    :param func: function
    :param xDomain: domain of x, (x left, x right)
    :param yDomain: domain of y, (y left, y right)
    :return: gridCoordinates set[(x1, y1), (x2, y2), ... ]
    """
    ...


def function(x: float, y: float) -> float:
    """implicitFunctionEquation"""
    return (x ** 2 + y ** 2 - 1) ** 3 - x ** 2 * y ** 3