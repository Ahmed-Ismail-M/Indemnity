from models.reasons import JobLeaveReasons
from models.employee import EMPLOYEE

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
    example_employee = EMPLOYEE(base_salary=5000, joining_date="21-2-2022")
    reason = get_leave_reason_from_user()
    final_amount = example_employee.calculate_indemnity(reason=reason)
    print(f'The calculated indemnity is : {final_amount}')

main()
