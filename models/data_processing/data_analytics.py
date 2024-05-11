# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Define a class for data analysis and visualization
class DataAnalytics:
    def __init__(self, data_path):
        # Load data from file
        self.data = pd.read_csv(data_path)

    def summary_statistics(self):
        # Compute summary statistics for the data
        print(self.data.describe())

    def correlation_matrix(self):
        # Compute the correlation matrix for the data
        corr = self.data.corr()
        sns.heatmap(corr, annot=True, cmap='coolwarm')
        plt.show()

    def scatter_plot(self, x_column, y_column):
        # Create a scatter plot for two columns of the data
        plt.scatter(self.data[x_column], self.data[y_column])
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.show()

    def bar_plot(self, column):
        # Create a bar plot for a column of the data
        self.data[column].value_counts().plot(kind='bar')
        plt.xlabel(column)
        plt.ylabel('Count')
        plt.show()

    def line_plot(self, column):
        # Create a line plot for a column of the data
        plt.plot(self.data[column])
        plt.xlabel('Index')
        plt.ylabel(column)
        plt.show()

    def histogram_plot(self, column):
        # Create a histogram plot for a column of the data
        plt.hist(self.data[column])
        plt.xlabel(column)
        plt.ylabel('Count')
        plt.show()
