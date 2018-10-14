import pandas as pd

def read_data(data_file_location):
    # Read csv file into Pandas data frame
    with open(data_file_location, 'r') as csvfile:
        data_frame = pd.read_csv(csvfile)

    # Drop first column containing IDs
    data_frame = data_frame.drop('Unnamed: 0', axis=1)

    return data_frame

if __name__ == "__main__":
    read_data("./data/beatsdataset.csv")
