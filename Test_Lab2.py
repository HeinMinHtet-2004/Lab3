import Lab2.bmi as bmi

def test_bmi_normal_weight():
    result = bmi.calcualate_bmi(57, 1.73)
    assert result == 0

def test_bmi_over_weight():
    result = bmi.calcualate_bmi(85, 1.73)
    assert result == 1

def test_bmi_under_weight():
    result = bmi.calcualate_bmi(53, 1.73)
    assert result == -1

print("All test passed!")

