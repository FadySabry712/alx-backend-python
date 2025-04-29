#!/usr/bin/env python3
""" async functions practice """
import random
import asyncio
from typing import Generator



async def async_generator() -> Generator[float, None, None]:
    """ yields a number every one second """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
