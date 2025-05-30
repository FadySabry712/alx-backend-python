#!/usr/bin/env python3
""" testing async coroutines """

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ return value after random number of seconds """

    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
