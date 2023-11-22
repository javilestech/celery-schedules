from proj.tasks import add, error_handler, hello, some_longrunning_task, test
from celery.utils.log import get_logger
from celery import group

logger = get_logger(__name__)

def on_raw_message(body):
    print(body)

a, b = 1, 1
r = hello.apply_async(args=(a, b))
print(r.get(on_message=on_raw_message, propagate=False))

#calling a task using the delay()
#Connection Error Handling
# When you send a task and the message transport connection is lost, or the connection cannot be initiated
# try:
#     add.delay(2, 2)
# except add.OperationalError as exc:
#     logger.exception('Sending task raised: %r', exc)

# a, b = 7, 1
# r = some_longrunning_task.apply_async(args=(a, b))
# print(r.get(on_message=on_raw_message, propagate=False))



# add.apply_async((2, 2), link_error=error_handler.s())

# numbers = [(2, 2), (4, 4), (8, 8), (16, 16)]
# results = []
# res = group(add.s(i, j) for i, j in numbers).apply_async()
# print(res.get())


# test.delay("pepe")