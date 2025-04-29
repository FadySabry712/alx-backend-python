#!/usr/bin/env python3
""" return asyncio task object """
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ return asyncio type object """
    return asyncio.create_task(wait_random(max_delay))
