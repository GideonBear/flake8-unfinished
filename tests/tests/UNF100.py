def test():  # 1: Only useless statements in the function body: `...`
    ...


def test():  # 1: Only useless statements in the function body: `pass`
    pass


def test():  # 1: Only useless statements in the function body: docstring
    """Docstring"""


def test():  # 1: Only useless statements in the function body: docstring, `pass`, `...`, docstring
    """Docstring"""
    pass
    ...
    'string'
