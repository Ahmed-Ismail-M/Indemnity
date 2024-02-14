from models.reasons import JobLeaveOptions, JobLeaveReasons
KSAJobLeaveRules = {
    JobLeaveReasons.AGAINST_ARTICLE_81.value: JobLeaveOptions.COMPLETE,
    JobLeaveReasons.MATERNITY.value: JobLeaveOptions.COMPLETE,
    JobLeaveReasons.AGREEMAENT.value: JobLeaveOptions.COMPLETE,
    JobLeaveReasons.RESIGNATION.value: JobLeaveOptions.BASED_ON_EXPERIENCE,
    JobLeaveReasons.AGAINST_ARTICLE_81.value: JobLeaveOptions.NA,
    JobLeaveReasons.FORCE_MAJEURE.value: JobLeaveOptions.COMPLETE,
    JobLeaveReasons.TERMINATION.value: JobLeaveOptions.COMPLETE,
    JobLeaveReasons.WITH_ARTCLE_80.value: JobLeaveOptions.COMPLETE,
    JobLeaveReasons.WITH_ARTICLE_81.value: JobLeaveOptions.COMPLETE
}

