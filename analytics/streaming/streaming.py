import time

class Streaming:
    def __init__(self):
        self.data = []

    def add_data(self, data):
        """Add data to the streaming pipeline."""
        self.data.append(data)

    def process_data(self):
        """Process data in real-time."""
        while True:
            if len(self.data) > 0:
                # Process the data
                # ...
                self.data.pop(0)
            time.sleep(1)
