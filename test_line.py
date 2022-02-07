import pytest

@pytest.mark.parametrize("tuple1, tuple2, x, expected", 
                        [[(0,0), (1,1), 0.5, 0.5],[(0,0), 
                        (1,2), 0.5, 1],[(0,0), (1,4), 0.5, 2])
def test_line(tuple1, tuple2, x, expected):
    from line import predict
    answer = predict(tuple1, tuple2, x)
    assert answer == expected