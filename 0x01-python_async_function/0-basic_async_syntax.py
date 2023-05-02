#!/usr/bin/env python3
'''Task 0's module.
'''
import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    An asynchronous coroutine that waits for a random delay between 0 and max_delay seconds (inclusive) and returns it.

    Parameters:
    - max_delay (float): The maximum delay in seconds (inclusive). Default value is 10.

    Returns:
    - delay (float): The delay in seconds as a float value.
    """
    
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
