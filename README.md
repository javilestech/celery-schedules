# celery-schedules

## Get started 
## Config the environment on your work directory

```
python3 -m venv env
```
## Install celery using pip
```
pip install -U Celery
```
##  choosing a broker 
```
docker run -d -p 5672:5672 rabbitmq
```

## Running the celery worker server
```
 celery -A tasks worker --loglevel=INFO
```