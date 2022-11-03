from ezflake.testing import assert_violates, assert_not_violates

from flake8_unfinished import UnfinishedPlugin, UNF001


def test_violates():
    assert_violates(UnfinishedPlugin, UNF001(2, 0), '''
        raise NotImplementedError
    ''')
    assert_violates(UnfinishedPlugin, UNF001(2, 0), '''
        raise NotImplementedError()
    ''')


def test_not_violates():
    assert_not_violates(UnfinishedPlugin, '''
        raise Exception
        NotImplementedError
        NotImplementedError()
        raise NotImplemented
        Exception
        raise
    ''')
