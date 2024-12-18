from loguru import logger


def log_me(func):
    def wrapper(*args, **kwargs):
        logger.info(f"вызов функции {func.__name__}")
        try:
            result = func(*args, **kwargs)
            logger.info(f"результат функции {func.__name__}: ВЫПОЛНЕНО")
            if result:
                return result

        except Exception as e:
            logger.error(f"ошибка в функции {func.__name__}: {e}")
            raise
    return wrapper
