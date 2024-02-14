from models.models import JobLeaveReasons, JobLeaveOptions, EMPLOYEE
from ds.local import JobLeaveRules

def get_rule(reason: str) -> JobLeaveOptions:
    return JobLeaveRules[reason]


def calculate_indemnity( reason: str)-> float:
    
    example_employee = EMPLOYEE(base_salary=5000, start_date="2020-2-21")
    rules = {
         JobLeaveOptions.COMLETE : example_employee.base_salary,
         JobLeaveOptions.NA: 0,
         JobLeaveOptions.WITH_RULES: example_employee.calculate_indemnity()
    }
    try:
        rule = get_rule(reason)
        return rules[rule]
    except Exception :
        raise Exception(f'Cannot find rule for : {reason}')

def get_leave_reason_from_user()-> str:
    available_reasons = JobLeaveReasons.get_tuple_values()
    print("Choose a leave reason:")
    for i, reason in enumerate(available_reasons, 1):
        print(f"{i}. {reason}")
    while True:
        try:
            choice = int(input("Enter the number corresponding to the leave reason: "))
            if 1 <= choice <= len(available_reasons):
                selected_reason = available_reasons[choice - 1]
                print(f"Selected leave reason: {selected_reason}")
                break
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return selected_reason

def main():
    reason = get_leave_reason_from_user()
    final_amount = calculate_indemnity(reason=reason)
    print(f'The calculated indemnity is : {final_amount}')

main()
