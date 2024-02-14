from enum import Enum
from dataclasses import dataclass
from datetime import date, datetime


@dataclass
class EMPLOYEE():
    base_salary: float
    start_date: str

    def calculate_years_of_experience(self) -> float:
        start_date_as_date = datetime.strptime(self.start_date, "%Y-%m-%d").date()
        # datetime.strptime(start_date_str, "%Y-%m-%d").date()
        current_date = date.today()
        years_of_experience = (current_date - start_date_as_date).days / 365.25
        return round(years_of_experience, 2)

    def calculate_indemnity(self):
        years_of_experience = self.calculate_years_of_experience()
        if years_of_experience < 2:
            return 0
        elif 2 <= years_of_experience < 5:
            return 1/3 * self.base_salary
        elif 5 <= years_of_experience < 10:
            return 2/3 * self.base_salary
        else:
            return self.base_salary


class SuperEnum(Enum):

    @classmethod
    def get_tuple_values(cls) -> tuple:
        return tuple(member.value for member in cls)


# USE THIS IF YOU WOULD LIKE TO GET REASONS IN ARABIC 
#(in this case we will have to install arabic reshaper to print the statments properly)
    
# class JobLeaveReasons(SuperEnum):
#     MATERNITY = 'إنهاء العاملة لعقد العمل خلال 6 أشهر من الزواج أو 3 أشهر من الوضع'
#     AGREEMAENT = 'اتفاق العامل وصاحب العمل'
#     RESIGNATION = 'استقالة العامل'
#     AGAINST_ARTICLE_81 = 'ترك العمل لأحد الحالات الواردة في المادة (81)'
#     WITH_ARTICLE_81 = 'ترك العمل لأحد الحالات الواردة في المادة (81)'
#     FORCE_MAJEURE = 'ترك العمل لأسباب قاهرة '
#     TERMINATION = 'فسخ العقد من قبل صاحب العمل'
#     WITH_ARTCLE_80 = 'فسخ العقد من قبل صاحب العمل لأحد الحالات الواردة في المادة (80)'
    

class JobLeaveReasons(SuperEnum):
    MATERNITY = 'Termination of Employment Contract within 6 months of marriage or 3 months of childbirth'
    AGREEMAENT = 'Agreement between the employee and the employer'
    RESIGNATION = 'Resignation by the employee'
    AGAINST_ARTICLE_81 = 'Leaving the job without submitting resignation for reasons other than those stated in Article (81)'
    WITH_ARTICLE_81 = 'Leaving the job for one of the cases mentioned in Article (81)'
    FORCE_MAJEURE = 'Leaving the job for compelling reasons'
    TERMINATION = 'Termination of the contract by the employer'
    WITH_ARTCLE_80 = 'Termination of the contract by the employer for one of the cases mentioned in Article (80)'


class JobLeaveOptions(SuperEnum):
    COMLETE = 'complete'
    NA = 'NA'
    WITH_RULES = 'with_rules'
