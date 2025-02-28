# Result
# /usr/bin/python3.10 /main_process_prod.py
# sub_log.getEffectiveLevel()=10
# Main process start
# stdout_result: b'some answer'
# stderr: b'log.getEffectiveLevel()=10\nERROR log from sub_process\nWARNING log from sub_process\nINFO log from sub_process\nFirst log from sub_process\nSecond log from sub_process\n'
# Main process finish
#
# Process finished with exit code 0

import asyncio
import sys
from logging import getLogger, StreamHandler, DEBUG

SUB_LOGGER_NAME = 'SUB_LOGGER_NAME'

def get_sub_log():
    sub_log = getLogger(SUB_LOGGER_NAME)
    sub_log.setLevel(DEBUG)
    handler = StreamHandler(stream=None)
    handler.setLevel(DEBUG)
    sub_log.addHandler(handler)
    return sub_log

log = getLogger(__name__)
sub_log = get_sub_log()

async def func_main_process() -> None:
    log.debug('Main process start')
    proc = await asyncio.create_subprocess_exec(
        './subproc_prod.py',
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await proc.communicate()
    log.debug('stdout_result: %s', stdout)
    log.debug('stderr: %s', stderr)
    log.debug('Main process finish')


if __name__ == '__main__':

    log.setLevel(DEBUG)
    log.addHandler(StreamHandler(stream=sys.stdout))
    log.info(f'{sub_log.getEffectiveLevel()=}')

    asyncio.run(func_main_process())
