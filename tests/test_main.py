from calc_work_hours.main import calculate_working_hours

expected_output = """Monday: Closed
Tuesday: 10 AM - 6 PM
Wednesday: Closed
Thursday: 10 AM - 6 PM
Friday: 10 AM - 1 AM
Saturday: 10 AM - 1 AM
Sunday: 12 PM - 9 PM, 9:00:01 PM - 9:00:10 PM"""


def test_calculate_working_hours():
    formatted_output = calculate_working_hours("../input.json")
    assert expected_output == formatted_output
