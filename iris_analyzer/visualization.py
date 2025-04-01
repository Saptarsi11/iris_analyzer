import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


class IrisVisualizer:
    """
    Class for visualizing the Iris dataset.
    """

    def __init__(self, data: pd.DataFrame):
        self.data = data

    def plot_pairwise(self):
        """
        Generate a pairplot of numeric features colored by species.
        """
        sns.pairplot(self.data, hue="Species")
        plt.show()

    def plot_species_distribution(self):
        """
        Plot bar chart showing the number of samples per species.
        """
        sns.countplot(data=self.data, x="Species")
        plt.title("Species Distribution")
        plt.show()

    def plot_feature_histogram(self, feature: str):
        """
        Plot histogram of a specific numeric feature.

        Parameters:
            feature (str): The feature column to plot
        """
        assert feature in self.data.columns, "Feature not found in dataset."
        sns.histplot(self.data[feature], kde=True)
        plt.title(f"Distribution of {feature}")
        plt.xlabel(feature)
        plt.show()
