# broker_url = 'pyamqp://'
broker_url = 'amqp://'
result_backend = 'rpc://'
# postgresql
# result_backend = 'db+postgresql://postgres:postgres@localhost/mydbtest'
# Celery automatically creates two tables to store result meta-data for tasks. 
# This setting allows you to customize the table names
database_table_names = {
    'task': 'myapp_taskmeta',
    'group': 'myapp_groupmeta',
}
task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'Europe/Oslo'

# disable UTC so that Celery can use local time
enable_utc = False
# task_ignore_result = True