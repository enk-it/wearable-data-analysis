import clickhouse_connect

from settings import settings

client = clickhouse_connect.get_client(
    host=settings.CLICKHOUSE_HOST,
    username=settings.CLICKHOUSE_USER,
    password=settings.CLICKHOUSE_PASSWORD
)

