#!/usr/bin/env python3
""" practice async compernhansion """
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """make a list using async comperhantion """
    return [num async for num in async_generator()]
