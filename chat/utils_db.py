import re
import logging
from django.db import connection

logger = logging.getLogger(__name__)

def run_sql(sql: str):
    """
    执行只读 SQL（仅允许 SELECT）
    返回结果：字典列表
    """
    output = {
        "code": 0,
        "msg": "success",
        "data": []
    }
    sql_clean = sql.strip().lower()

    # 限制只能执行 SELECT
    if not sql_clean.startswith("select"):
        logger.warning(f"Blocked non-SELECT SQL: {sql}")
        return "查询出错"

    try:
        logger.info(f"Executing SQL: {sql}")
        with connection.cursor() as cursor:
            cursor.execute(sql)
            columns = [col[0] for col in cursor.description]
            results = [dict(zip(columns, row)) for row in cursor.fetchall()]
            logger.info(f"Returned {len(results)} rows")

            print(results)
            return {
                "code": 0,
                "msg": "success",
                "data": results
            }
    except Exception as e:
        logger.error(f"SQL execution error: {e}")
        return {
            "code": 1,
            "msg": e.__str__(),
            "data": []
        }

