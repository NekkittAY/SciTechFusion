import redis.asyncio as redis


redis_client = redis.Redis(host='localhost', port=6379, db=0)


async def get_data(key: int) -> str:
    """
    Get data from Redis cache async function

    :param key: id of data, int
    :return: data, str
    """

    data = await redis_client.get(str(key))
    return data


async def set_data(key: int, value: str) -> None:
    """
    Set data to Redis cache async function

    :param key: id of data, int
    :param value: values of data for cache, str (json in str)
    """
    await redis_client.set(str(key), value)
