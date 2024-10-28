import employee_info as info

def test_average_salary():
    result = 0
    expected_average = (50000 + 60000 + 56000 + 70000 + 65000 + 60000) / 6
    result = info.calculate_average_salary()
    assert result == expected_average