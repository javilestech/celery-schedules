from celery import Celery
from celery.schedules import crontab
from proj.beat_schedule import starting_schedule, period_task
#The first argument to Celery is the name of the current module
#The second argument is the broker keyword argument,
#the backend argument specifies the result backend to use, It’s used to keep track of task state and results

app = Celery('proj',
            #  broker='amqp://',
            #  backend='rpc://',
             include=['proj.tasks'])

# use a configuration module 
app.config_from_object('proj.celeryconfig')


# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

## starting schedule task
# starting_schedule(app)

@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    period_task(sender, **kwargs)


if __name__ == '__main__':
    app.start()