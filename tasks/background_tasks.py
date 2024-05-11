# tasks/background_tasks.py
from celery import Celery

app = Celery("pipfs_hub")

@app.task
def process_pipfs_data(pipfs_id):
    # ...
