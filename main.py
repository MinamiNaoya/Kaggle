import pandas
import pandas as pd
import numpy as np
train = pd.read_csv("C:\\Users\\owner\\Downloads\\train.csv")
test = pd.read_csv("C:\\Users\\owner\\Downloads\\test.csv")

test_shape = test.shape
train_shape = train.shape
print(test.describe())
print(train.describe())