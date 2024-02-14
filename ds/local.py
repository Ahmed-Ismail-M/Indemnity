from models.models import JobLeaveOptions, JobLeaveReasons
JobLeaveRules = {
    JobLeaveReasons.AGAINST_ARTICLE_81.value: JobLeaveOptions.COMLETE,
    JobLeaveReasons.MATERNITY.value: JobLeaveOptions.COMLETE,
    JobLeaveReasons.AGREEMAENT.value: JobLeaveOptions.COMLETE,
    JobLeaveReasons.RESIGNATION.value: JobLeaveOptions.WITH_RULES,
    JobLeaveReasons.AGAINST_ARTICLE_81.value: JobLeaveOptions.NA,
    JobLeaveReasons.FORCE_MAJEURE.value: JobLeaveOptions.COMLETE,
    JobLeaveReasons.TERMINATION.value: JobLeaveOptions.COMLETE,
    JobLeaveReasons.WITH_ARTCLE_80.value: JobLeaveOptions.COMLETE
}
