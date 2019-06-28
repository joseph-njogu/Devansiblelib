import calculator


def test_add():
    assert calculator.add(2, 2) == 4


def test_subtract():
    assert calculator.subtract(4, 2) == 2

# def test_multiplication():
# 	assert calculator.multiplication(10, 10) == 100
