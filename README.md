# celery-schedules

## Get started 
## Config the virtual environment on your work directory

```
python3 -m venv env
```

## Active the virtual environment depend on your shell
## for shell bash
```
source venv/bin/activate
```
## for shell cmd.exe
```
venv\Scripts\activate.bat
```
## Install the neccesary modules
```
pip install -r requirements.txt
```
## Note: you must have docker installed
##  choose a broker , we will use rabbitmq
```
docker run -d -p 5672:5672 rabbitmq
```
##  Run the beat scheduler for the app
##  This will schedule the tasks into beat_schedule to run based on the set period 
```
celery -A proj beat --loglevel=info
```
## Workers consume messages from a queue by pulling them out off. 
## What we have a the moment is that Celery beat is adding tasks 
## to the queue periodically. We want workers to to their job
## Note: You must be into src directory
## Running the celery worker server
```
celery -A proj worker --loglevel=INFO
```

