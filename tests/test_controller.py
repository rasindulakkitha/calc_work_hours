import pytest

from calc_work_hours.controller import CalculateWorkHours

"""" input is validated json """

test_input1 = {"monday": [],
               "tuesday": [{"type": "open", "value": 36000}, {"type": "close", "value": 64800}],
               "wednesday": [],
               "thursday": [],
               "friday": [{"type": "open", "value": 36000}],
               "saturday": [{"type": "close", "value": 3600}],
               "sunday": [{"type": "open", "value": 3600}, {"type": "close", "value": 43200}]}

test_output1 = {"monday": [],
                "tuesday": [{"type": "open", "value": 36000}, {"type": "close", "value": 64800}],
                "wednesday": [],
                "thursday": [],
                "friday": [{"type": "open", "value": 36000}, {"type": "close", "value": 3600}],
                "saturday": [],
                "sunday": [{"type": "open", "value": 3600}, {"type": "close", "value": 43200}]}


@pytest.mark.parametrize("input,expected_output", [(test_input1, test_output1)])
def test_refactor_input_json_with_correct_data(input, expected_output):
    test_obj = CalculateWorkHours(input)
    assert expected_output == test_obj.refactor_input_json_with_correct_data()


test_output2 = """Monday: Closed
Tuesday: 10 AM - 6 PM
Wednesday: Closed
Thursday: Closed
Friday: 10 AM - 1 AM
Saturday: Closed
Sunday: 1 AM - 12 PM"""


@pytest.mark.parametrize("input,expected_output", [(test_output1, test_output2)])
def test_working_hours_in_human_readable_format(input, expected_output):
    test_obj = CalculateWorkHours(input)
    test_obj.refactored_schema = test_output1
    assert expected_output == test_obj.working_hours_in_human_readable_format()
