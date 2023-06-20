from time import sleep
from sch.helpers.decoder import decoder, check
from sch.helpers.fail_handler import fail_checker
from sch.helpers.regex_conditions import (
    condition_onu_last_down_cause,
    condition_onu_last_down_time,
)


def down_values(comm, command, data):
    command(f'  interface  gpon  {data["frame"]}/{data["slot"]}  ')
    command(f'  display  ont  info  {data["port"]}  {data["onu_id"]}  |  no-more')
    sleep(1)
    command("quit")
    value = decoder(comm)
    fail = fail_checker(value)
    re_cause_start = check(value, condition_onu_last_down_cause[0])
    re_cause_end = check(value, condition_onu_last_down_cause[1])
    re_time_start = check(value, condition_onu_last_down_time[0])
    re_time_end = check(value, condition_onu_last_down_time[1])

    CAUSE = None
    TIME = None
    DATE = None

    if fail is not None and re_cause_start is None:
        return (CAUSE, TIME, DATE)

    (_, s_c) = re_cause_start.span()
    (e_c, _) = re_cause_end.span()
    (_, s_t) = re_time_start.span()
    (e_t, _) = re_time_end.span()

    CAUSE = value[s_c : e_c - 2].replace("\n", "").replace("\r", "")
    DATE = value[s_t : e_t - 2].replace("\n", "").replace("\r", "").split(" ")[0]
    TIME = value[s_t : e_t - 2].replace("\n", "").replace("\r", "").split(" ")[1]

    return (CAUSE, TIME, DATE)
