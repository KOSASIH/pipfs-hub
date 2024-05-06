import plotly.express as px

class Visualization:
    def __init__(self, data):
        self.data = data

    def plot(self):
        """Visualize data using Plotly."""
        fig = px.scatter(self.data, x='x', y='y')
        fig.show()
