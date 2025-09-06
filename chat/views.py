import logging

from django.http import JsonResponse
from django.shortcuts import render

from chat.constants import TABLE_SCHEMA, LLM_RESPONSE_TYPE
from chat.utils_db import run_sql
from chat.utils_llm import generate_sql_from_nl, generate_chart_and_summary, check_sql_exception

logger = logging.getLogger(__name__)
# Create your views here.
def chat_page(request):
    return render(request, "chat.html")


def getReply(request):
    response = {
        "status": 200,
        "replyType": "text",
        "reply": "Hello, world!",
        "summary":""
    }
    user_input = request.GET.get("text","")
    logger.info(f"user input: {user_input}")
    llm_response = generate_sql_from_nl(user_input, TABLE_SCHEMA)
    if llm_response.get("intent") == LLM_RESPONSE_TYPE["QUERY"]:
        sql = llm_response.get("sql")
        result = run_sql(sql)
        if result["code"] == 0:
            llm_summary = generate_chart_and_summary(result['data'],user_input)
            response["replyType"] = llm_summary.get("chart_type")
            response["reply"] = result["data"]
            response["summary"] = llm_summary.get("summary")
        else:
            exception_msg = result["msg"]
            check_result = check_sql_exception(sql,exception_msg,TABLE_SCHEMA)
            response["replyType"] = "table"
            response["reply"] = check_result.get("msg")



    elif llm_response.get("intent") == LLM_RESPONSE_TYPE["CHAT"]:
        response["reply"] = llm_response.get("answer")
    elif llm_response.get("intent") == LLM_RESPONSE_TYPE["REJECT"]:
        response["reply"] = llm_response.get("answer")






    return JsonResponse(response)