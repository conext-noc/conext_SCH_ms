from sch.helpers.decoder import check, checkIter

FAIL_1 = "Failure: "
FAIL_1_CHAR = "% "
END_FAIL = "MARLLM0"
FAIL_2 = "The required ONT does not exist"
FAIL_3 = "WAN port does not exist"


def fail_checker(value):
    reason = None
    fail1 = check(value, FAIL_1)
    fail2 = check(value, FAIL_1_CHAR)
    fail3 = check(value, FAIL_2)
    fail4 = check(value, FAIL_3)
    if fail1 is not None and fail2 is None and fail3 is None and fail4 is None:
        (_, s) = fail1.span()
        end = checkIter(value, END_FAIL)
        maxLen = len(end) - 1
        (e, _) = end[maxLen]
        reason = value[s:e].replace("\n", "")

    elif fail1 is None and fail2 is not None and fail3 is None and fail4 is None:
        (_, s) = fail2.span()
        end = checkIter(value, END_FAIL)
        maxLen = len(end) - 1
        (e, _) = end[maxLen]
        reason = value[s:e].replace("\n", "")

    elif fail1 is None and fail2 is None and fail3 is not None and fail4 is None:
        reason = FAIL_2

    elif fail1 is None and fail2 is None and fail3 is None and fail4 is not None:
        reason = FAIL_3

    return reason
