#!/usr/bin/env python3
from time import sleep
from sys import exit as exit_sys, stdout

from main_process_prod import sub_log as log


def func_from_subproc() -> str:

    log.error('ERROR log from sub_process')
    log.warning('WARNING log from sub_process')
    log.info('INFO log from sub_process')

    log.debug('First log from sub_process')
    sleep(0.1)
    log.debug('Second log from sub_process')
    return 'some answer'


if __name__ == '__main__':
    try:
        log.info(f'{log.getEffectiveLevel()=}')
        result = func_from_subproc()
        stdout.write(result)
    except Exception as err:
        stdout.write(str(err))
        exit_sys(1)
