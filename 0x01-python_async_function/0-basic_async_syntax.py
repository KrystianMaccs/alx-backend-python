#!/usr/bin/env python3

import asyncio
import random

async def wait_random(max_delay=10):
    """
    An asynchronous coroutine that waits for a random delay between 0 and max_delay seconds (inclusive) and returns it.

    Parameters:
    - max_delay (float): The maximum delay in seconds (inclusive). Default value is 10.

    Returns:
    - delay (float): The delay in seconds as a float value.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
