from enum import Enum
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
    COMPLETE = 'complete'
    NA = 'NA'
    BASED_ON_EXPERIENCE = 'with_rules'