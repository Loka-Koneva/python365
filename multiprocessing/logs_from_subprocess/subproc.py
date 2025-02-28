#!/usr/bin/env python3
from logging import getLogger, StreamHandler
from time import sleep
from sys import exit as exit_sys, stdout


SUB_LOGGER_NAME = 'SUB_LOGGER_NAME'
log = getLogger(SUB_LOGGER_NAME)

def func_from_subproc() -> str:
    log.setLevel('DEBUG')
    handler = StreamHandler(stream=None)
    handler.setLevel('DEBUG')
    log.addHandler(handler)

    log.error('ERROR log from sub_process')
    log.warning('WARNING log from sub_process')
    log.info('INFO log from sub_process')

    log.debug('First log from sub_process')
    sleep(0.1)
    log.debug('Second log from sub_process')
    return 'some answer'


if __name__ == '__main__':
    try:
        result = func_from_subproc()
        stdout.write(result)
    except Exception as err:
        stdout.write(str(err))
        exit_sys(1)
