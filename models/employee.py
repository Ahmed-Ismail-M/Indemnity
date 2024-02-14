
from dataclasses import dataclass
from datetime import date, datetime
from ds.local import KSAJobLeaveRules
from models.reasons import JobLeaveOptions


@dataclass
class EMPLOYEE():
    base_salary: float
    joining_date: str

    def calculate_total_experience(self) -> float:
        start_date_as_date = datetime.strptime(self.joining_date, "%d-%m-%Y").date()
        current_date = date.today()
        total_of_experience = (current_date - start_date_as_date).days / 365.25
        return round(total_of_experience, 1)

    def check_rule(self, total_experience: float) -> float:
        years_of_experience = int(total_experience) # get number of years from the total experience
        months = total_experience - int(total_experience) # get number of months from the total experience
        five_years_experience = 5 # to apply first 5 years rules
        if years_of_experience < 2:
            return 0
        elif 2 <= years_of_experience < 5:
            if months > 0.59:# If the employee stayed more than 5 months will add another year
                years_of_experience += 1
            return round(1/3 * self.get_half_indemnity(years_of_experience), 2)
        elif 5 <= years_of_experience < 10:
            years_above_five_exp = round(years_of_experience - 5, 1)
            if months > 0.59: # If the employee stayed more than 5 months will add another year
                five_years_experience = 6

            return round(2/3 * (self.get_half_indemnity(five_years_experience) + (years_above_five_exp * self.base_salary)), 2)
        else:
            years_above_five_exp = years_of_experience - 5
            if months > 1:
                five_years_experience = 6
            return round(self.get_half_indemnity(five_years_experience) + (years_above_five_exp * self.base_salary), 2)
        
    def get_complete_indemnity(self):
        total_experience = self.calculate_total_experience()
        years_of_experience = int(total_experience)
        months = total_experience - int(total_experience)
        if months > 0.59:# If the employee stayed more than 5 months will add another year
            years_of_experience +=1
        return self.base_salary * years_of_experience
    
    def get_half_indemnity(self, years_of_experience) -> float:
        return (self.base_salary / 2) * years_of_experience

    def calculate_rule(self):
        years_of_experience = self.calculate_total_experience()
        return self.check_rule(years_of_experience)


    def calculate_indemnity(self, reason: str) -> float:
        rules = {
            JobLeaveOptions.COMPLETE: self.get_complete_indemnity(),
            JobLeaveOptions.NA: 0,
            JobLeaveOptions.BASED_ON_EXPERIENCE: self.calculate_rule()
        }
        try:
            rule = KSAJobLeaveRules[reason]
            return rules[rule]
        except Exception:
            raise Exception(f'Cannot find rule for : {reason}')
