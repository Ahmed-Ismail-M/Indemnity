import unittest
from models.employee import EMPLOYEE
from models.reasons import JobLeaveReasons


class TestIndemnity(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            #JOING DATE      # LEAVING REASON                #Expected Indemnity
            #(DD-MM-YYYY)     Choices                        FLOAT
            ("01-2-2023", JobLeaveReasons.RESIGNATION.value, 0),
            ("01-2-2022", JobLeaveReasons.RESIGNATION.value, 1666.67),
            ("01-2-2018", JobLeaveReasons.RESIGNATION.value, 11666.67),
            ("01-7-2017", JobLeaveReasons.RESIGNATION.value, 13333.33),
            ("01-2-2014", JobLeaveReasons.RESIGNATION.value, 37500),
        ]

    def test_calculate_indemnity(self):
        for joining_date, reason, expected_indemnity in self.test_cases:
            self.example_employee = EMPLOYEE(base_salary=5000, joining_date=joining_date, leave_date="15-2-2024")
            actual_indemnity = self.example_employee.calculate_indemnity(reason=reason)
            self.assertEqual(actual_indemnity, expected_indemnity)


if __name__ == "__main__":
    unittest.main()
