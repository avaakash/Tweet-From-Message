"""
    Connect to redis server
"""
import redis

from utils.settings import get_env

def connect():
    """Connect to redis server"""
    environ_secrets = get_env()
    host = environ_secrets["redis_host"]
    port = environ_secrets["redis_port"]
    password = environ_secrets["redis_password"]
    if password:
        return redis.Redis(host=host, port=port, password=password)
    return redis.Redis(host=host, port=port)
