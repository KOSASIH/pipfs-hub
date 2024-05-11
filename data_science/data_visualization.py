import matplotlib.pyplot as plt
import seaborn as sns


def visualize_data(data):
    # Visualize data using Matplotlib or Seaborn
    # For example, plot histograms, scatter plots, or heatmaps

    # Plot histograms
    data.hist(bins=50, figsize=(20, 15))
    plt.show()

    # Plot scatter plots
    sns.pairplot(data, hue="class", height=2.5)
    plt.show()

    # Plot heatmaps
    correlation_matrix = data.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
    plt.show()
