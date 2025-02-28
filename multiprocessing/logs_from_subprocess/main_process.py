import asyncio
import sys
from logging import getLogger, StreamHandler, DEBUG
log = getLogger(__name__)

async def func_main_process() -> None:
    log.debug('Main process start')
    proc = await asyncio.create_subprocess_exec(
        './subproc.py',
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

    asyncio.run(func_main_process())
