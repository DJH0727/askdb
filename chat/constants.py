# chat/constants.py

TABLE_SCHEMA = """
数据库表结构说明：

1. departments 部门表
- id: INT 主键
- name: VARCHAR 部门名称（示例值: 技术, 销售, 客服, 市场, 人事）
- manager_id: INT 部门经理，对应 users.id

2. users 员工表
- id: INT 主键
- name: VARCHAR 员工姓名
- email: VARCHAR 邮箱，可为空
- department_id: INT 对应 departments.id
- hire_date: DATE 入职日期
- salary: DECIMAL 工资

3. clients 客户表
- id: INT 主键
- name: VARCHAR 客户名称（示例值: 客户A, 客户B, 客户C）
- industry: VARCHAR 行业
- location: VARCHAR 地点

4. projects 项目表
- id: INT 主键
- name: VARCHAR 项目名称（示例值: 项目X, 项目Y, 项目Z, 项目M, 项目N）
- department_id: INT 负责部门，对应 departments.id
- start_date: DATE
- end_date: DATE
- budget: DECIMAL 预算

5. sales 销售记录表
- id: INT 主键
- sale_date: DATE 销售日期
- employee_id: INT 对应 users.id
- client_id: INT 对应 clients.id
- project_id: INT 对应 projects.id
- amount: DECIMAL 销售额

6. tasks 员工任务表
- id: INT 主键
- employee_id: INT 对应 users.id
- project_id: INT 对应 projects.id
- task_name: VARCHAR 任务名称
- status: VARCHAR 状态 (pending/completed)
- hours_spent: DECIMAL 工时
"""

LLM_RESPONSE_TYPE = {
    "QUERY": "query",
    "CHAT": "chat",
    "REJECT": "reject",
    "ERROR": "error"
}

CHAT_RESPONSE_TYPE = {
    "TEXT": "text",
    "TABLE":"table",
    "LINE":"line",
    "BAR":"bar",
    "PIE":"pie",
    "SCATTER":"scatter",
}
