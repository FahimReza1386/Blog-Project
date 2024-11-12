from core.celery import app
from time import sleep

@app.task
def sendEmail():
    sleep(4)
    print('Done Sending Email. by')