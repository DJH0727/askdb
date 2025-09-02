import logging

from django.http import JsonResponse
from .utils_db import run_sql

logger = logging.getLogger(__name__)
def execute_query(request):
    user_input = request.GET.get("q", "")
    logger.info(f"User input: {user_input}")


    # 临时：直接写 SQL 测试
    sql = "SELECT * FROM testuser LIMIT 5"

    try:
        result = run_sql(sql)
        return JsonResponse({"success": True, "data": result})
    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)})
