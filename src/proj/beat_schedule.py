from celery.schedules import crontab


def period_task(sender, **kwargs):
    from proj.tasks import  test, hello
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')

    # Calls test('hello') every 30 seconds.
    # It uses the same signature of previous task, an explicit name is
    # defined to avoid this task replacing the previous one defined.
    sender.add_periodic_task(30.0, test.s('hello'), name='add every 30')

    # Calls test('world') every 30 seconds
    sender.add_periodic_task(30.0, test.s('world'), expires=10)

    sender.add_periodic_task(5.0, hello.s(1,2))

    # Executes every Monday morning at 7:30 a.m.
    sender.add_periodic_task(
        crontab(hour=7, minute=30, day_of_week=1),
        test.s('Happy Mondays!'),
    )
    

def starting_schedule(app):
    # Executes every Monday morning at 7:30 a.m.
    app.conf.beat_schedule = {
        'add-every-10-seconds': {
            'task': 'proj.tasks.add',
            'schedule': 10.0,
            'args': (16, 16)
        },
    }