
import json
import logging

from openai import OpenAI

from chat.prompt import generate_sql_from_nl_prompt, generate_chart_and_summary_prompt

logger = logging.getLogger(__name__)
client = OpenAI(api_key="sk-1dd6e304227b483a9911286af31c6827", base_url="https://api.deepseek.com")
#client = OpenAI(api_key="sk-qUUM06aGftDv1gKf2TBY4AjfwfIlCxkm3yYPqh5HHYSUGls9", base_url="https://api.deepseek.com")

def call_llm_json(prompt: str, role: str,temperature: float = 1):
    response = client.chat.completions.create(
        model="deepseek-chat",
        response_format={
            'type': 'json_object'
        },
        messages=[
            {"role": "system", "content": role},
            {"role": "user", "content": prompt},
        ],
        stream=False,
        temperature=temperature
    )
    content = response.choices[0].message.content.strip()
    print(content)
    try:
        result = json.loads(content)
        return {
            "code": 0,
            "msg": result
        }
    except json.JSONDecodeError:
        return {
            "code": 1,
            "msg": "返回格式错误"
        }


def generate_sql_from_nl(nl_question: str, table_schema: str):
    """
    使用 LLM 将自然语言问题转换成 SQL 语句
    参数:
      nl_question: 用户的自然语言输入
      table_schema: 提供数据库表结构，帮助 LLM 生成正确 SQL
    返回:
       {
            "intent": "query|chat|reject",
            "sql": None,
            "answer": ""
        }
    """
    prompt = generate_sql_from_nl_prompt(nl_question, table_schema)
    role = "你是一个SQL生成器和数据库助手"
    result = call_llm_json(prompt, role)
    logger.info("generate_sql_from_nl result: \n%s", result)
    if result.get("code") == 0:
        return result.get("msg")
    else:
        return {"intent": "reject", "sql": None, "answer": result.get("msg")}


def generate_chart_and_summary(query_result: list,user_question: str) -> dict:
    """
    输入查询结果，让 LLM 决定 chart_type + 简短 summary
    返回：
    {
        "chart_type": "table/bar/line/pie/scatter",
        "summary": "简短中文总结"
    }
    """
    if not query_result:
        return {"chart_type": "table", "summary": "查询结果为空。"}

    # 构造 prompt
    prompt = generate_chart_and_summary_prompt(query_result, user_question)
    role = "你是一个数据分析助手"
    result = call_llm_json(prompt, role)
    logger.info("generate_chart_and_summary result: \n%s", result)
    if result.get("code") == 0:
        return result.get("msg")
    else:
        return {"chart_type": "table", "summary": result.get("msg")}





def check_sql_exception(sql: str, exception_msg: str, schema: str):
    """
    使用 LLM 对错误 SQL 进行二次检查和修正
    """
    prompt = f"""
    你是一个智能 SQL 审查助手。以下 SQL 执行出错，请分析原因并尝试修正。
    数据库：MySQL 8.0
    数据库表结构：
    {schema}
    
    原始 SQL：
    {sql}
    
    数据库错误信息：
    {exception_msg}
    
    返回 JSON：
    {{
      "valid": 如果能修正，则为 true，否则为 false,
      "result": "如果 valid=true，则返回修正后的 SQL"
      "reason": "返回修改的原因或者不予修改的原因(中文)"
    }}
    不要返回其他解释或额外文字。
    """
    #print(prompt)

    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            response_format={
                'type': 'json_object'
                },
            messages=[
                {"role": "system", "content": "你是一个智能 SQL 审查助手。"},
                {"role": "user", "content": prompt},
            ],
            stream=False,
            temperature=0
        )
        llm_output = response.choices[0].message.content.strip()
        logger.info("check_sql_exception result: \n%s", llm_output)
        result = json.loads(llm_output)
        return {"code": 0 if result.get("valid") else 1, "msg": result.get("reason")}

    except Exception as e:
        return {"code": 1, "msg": f"SQL 检查失败: {e}"}
