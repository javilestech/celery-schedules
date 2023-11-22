import time

from my_task import MyTask
from .celery import app
from celery.utils.log import get_task_logger

#The best practice is to create a common logger for all of your tasks at the top of your module
logger = get_task_logger(__name__)


@app.task(base=MyTask)
def some_longrunning_task(x, y):
    logger.info('Adding {0} - {1}'.format(x, y))
    return x - y

#The bind argument means that the function will be a “bound method” 
#so that you can access attributes and methods on the task type instance.
@app.task(bind=True)
def add(self,x, y):
    logger.info('Adding {0} + {1}'.format(x, y))
    logger.info(self.request.id)
    return x + y


@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)

@app.task(bind=True)
def hello(self, a, b):
    time.sleep(1)
    self.update_state(state="PROGRESS", meta={'progress': 50})
    time.sleep(1)
    self.update_state(state="PROGRESS", meta={'progress': 90})
    time.sleep(1)
    return 'hello world: %i' % (a+b)

@app.task
def error_handler(request, exc, traceback):
    print('Task {0} raised exception: {1!r}\n{2!r}'.format(
          request.id, exc, traceback))
    

@app.task
def test(arg):
    logger.info('testing task :)')
    print(arg)