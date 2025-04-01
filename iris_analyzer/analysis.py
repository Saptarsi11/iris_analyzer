import numpy as np
import pandas as pd


class IrisAnalyzer:
    """
    Class for analyzing the Iris dataset.
    """

    def __init__(self, filepath: str):
        self.filepath = filepath
        self.data = self.load_data()

    def load_data(self):
        """
        Load and clean the dataset.

        Returns:
            pd.DataFrame: Cleaned Iris dataset
        """
        df = pd.read_csv(self.filepath, index_col=0)
        return df

    def get_summary(self):
        """
        Return statistical summary of the dataset.

        Returns:
            pd.DataFrame: Summary statistics
        """
        return self.data.describe()

    def filter_by_species(self, species: str):
        """
        Filter dataset by species.

        Parameters:
            species (str): Name of the species to filter

        Returns:
            pd.DataFrame: Filtered dataset
        """
        assert species in self.data["Species"].unique(), "Species not found in dataset."
        return self.data[self.data["Species"] == species]

    def normalize_features(self):
        """
        Normalize numeric features.

        Returns:
            pd.DataFrame: Dataset with normalized features
        """
        features = self.data.select_dtypes(include=[np.number])
        normalized = (features - features.mean()) / features.std()
        return pd.concat([normalized, self.data["Species"]], axis=1)
