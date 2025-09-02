```angular2html
askdb/
├── manage.py
├── requirements.txt
│
├── askdb/                    # 主配置目录
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py                # 所有路由都写这里
│   ├── asgi.py
│   └── wsgi.py
│
├── chat/                      # app1：自然语言问答
│   ├── __init__.py
│   ├── apps.py
│   ├── views.py
│   ├── models.py
│
├── query/                     # app2：SQL 执行 & 数据处理
│   ├── __init__.py
│   ├── apps.py
│   ├── views.py
│
├── visualization/             # app3：数据可视化
│   ├── __init__.py
│   ├── apps.py
│   ├── views.py
│
├── export/                    # app4：导出 Word/PDF
│   ├── __init__.py
│   ├── apps.py
│   ├── views.py
│   └── utils_export.py
│
├── templates/                 # 公共模板
│
├── static/                    # 公共静态资源
│   ├── css/
│   ├── js/
│   └── images/
│
└── logs/
    └── query.log

```