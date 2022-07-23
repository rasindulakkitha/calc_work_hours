import pytest

from calc_work_hours.utils import format_time, format_time_range, format_output


@pytest.mark.parametrize("input,expected_output", [(36000, "10 AM"), (64800, "6 PM"), (3600, "1 AM"), (43200, "12 PM")])
def test_format_time(input, expected_output):
    assert expected_output == format_time(input)


@pytest.mark.parametrize("input,expected_output",
                         [(['10 AM', '6 PM'], "10 AM - 6 PM"), (['10 AM', '1 AM'], "10 AM - 1 AM")])
def test_format_time_range(input, expected_output):
    assert expected_output == format_time_range(str(input[0]), str(input[1]))


test_input1 = {'monday': [], 'tuesday': ['10 AM - 6 PM'], 'wednesday': [], 'thursday': ['10 AM - 6 PM'], 'friday': ['10 AM - 1 AM'], 'saturday': ['10 AM - 1 AM'], 'sunday': ['12 PM - 9 PM', '9:00:01 PM - 9:00:10 PM']}

test_output1 = """Monday: Closed
Tuesday: 10 AM - 6 PM
Wednesday: Closed
Thursday: 10 AM - 6 PM
Friday: 10 AM - 1 AM
Saturday: 10 AM - 1 AM
Sunday: 12 PM - 9 PM, 9:00:01 PM - 9:00:10 PM"""


@pytest.mark.parametrize("input,expected_output", [(test_input1, test_output1)])
def test_format_time(input, expected_output):
    assert expected_output == format_output(input)
