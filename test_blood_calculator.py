# def test_check_HDL1():
#     from blood_calculator import check_HDL
#     answer = check_HDL(70)
#     assert answer == "Normal"

# def test_check_HDL2():
#     from blood_calculator import check_HDL
#     answer = check_HDL(50)
#     assert answer == "Borderline Low"

# def test_check_HDL3():
#     from blood_calculator import check_HDL
#     answer = check_HDL(20)
#     assert answer == "Low"

import pytest

@pytest.mark.parametrize("input_HDL, expected", [[70, "Normal"],[45, "Borderline Low"],[20, "Low"]])
def test_check_HDL(input_HDL, expected):
    from blood_calculator import check_HDL
    answer = check_HDL(input_HDL)
    assert answer == expected