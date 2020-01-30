broker_url = 'pyamqp://'
include = ['expense_control.controller.tasks.create_expense']

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
enable_utc = True
