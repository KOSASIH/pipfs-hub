# web/signals.py
from flask import signals

@signals.signal('new_pipfs')
def new_pipfs_handler(pipfs):
    # ...
