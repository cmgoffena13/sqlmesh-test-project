import logging
import time
from functools import wraps

logger = logging.getLogger(__name__)


def retry(attempts: int = 3, delay: float = 0.25, backoff: float = 2.0):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            wait = delay
            for index in range(attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if index == attempts - 1:
                        raise e
                    logger.warning(
                        f"Retrying {func.__name__} (attempt {index + 2}/{attempts}) after {type(e).__name__}: {e}"
                    )
                    time.sleep(wait)
                    wait *= backoff

            raise ValueError("Attempts must be greater than 0")

        return wrapper

    return decorator
