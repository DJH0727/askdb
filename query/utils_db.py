from django.db import connection
import logging

logger = logging.getLogger(__name__)

def run_sql(sql):
    """
    执行任意 SQL 并返回结果（字典列表）
    """
    logger.info(f"Executing SQL: {sql}")
    with connection.cursor() as cursor:
        cursor.execute(sql)
        if sql.strip().lower().startswith("select"):
            columns = [col[0] for col in cursor.description]
            results = [dict(zip(columns, row)) for row in cursor.fetchall()]
            logger.info(f"Returned {len(results)} rows")
            return results
        else:
            affected = cursor.rowcount
            logger.info(f"{affected} rows affected")
            return affected
