def test_0101hw():
    assert ('home', 'work') == ('home', 'work')


def test_0102hw():
    assert 'QA' != 'QC'


def test_0103hw():
    assert not (1, 1, 2, 3, 5) == (2, 3, 5)
