from keras.models import Sequential
from keras.layers import Dense, Activation
import src.features.data_reader as dr

class MLP:

    def __init__(self, file_path):
        self.data = dr.read_data(file_path)
        self.input_size = len(self.data.columns)

    def build_model(self):
        pass

if __name__ == "__main__":
    MLP(file_path="../../data/beatsdataset.csv")


