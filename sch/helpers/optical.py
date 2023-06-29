from time import sleep
from sch.helpers.decoder import decoder, check
from sch.helpers.fail_handler import fail_checker
from sch.helpers.regex_conditions import condition_onu_pwr, condition_onu_temp


def optical_values(comm, command, data):
    TEMP = None
    PWR = None
    command(f'  interface  gpon  {data["frame"]}/{data["slot"]}  ')
    command(
        f'  display  ont  optical-info  {data["port"]}  {data["onu_id"]}  |  no-more'
    )
    sleep(2)
    command("quit")
    value = decoder(comm)
    fail = fail_checker(value)
    re_pwr = check(value, condition_onu_pwr)
    re_temp = check(value, condition_onu_temp)
    if fail is not None and re_pwr is None:
        return (TEMP, PWR)
    (_, eT) = re_temp.span()
    (_, eP) = re_pwr.span()
    PWR = value[eP : eP + 6]
    TEMP = value[eT : eT + 4].replace("\n", "").replace(" ", "").replace("\r", "")
    return (TEMP, PWR)
