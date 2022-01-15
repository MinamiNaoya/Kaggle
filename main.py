import pandas
import pandas as pd
import numpy as np
train = pd.read_csv("C:\\Users\\owner\\Downloads\\train.csv")
test = pd.read_csv("C:\\Users\\owner\\Downloads\\test.csv")

test_shape = test.shape
train_shape = train.shape


def kesson_table(df):
    null_val = df.isnull().sum(df)
    percent = 100 * df.isnull().sum()/len(df)
    kesson_table=pd.concat([null_val, percent], axis=1)
    kesson_table_ren_columns = kesson_table.rename(columns = {0: '欠損数', 1: '%'}
    )

    return kesson_table_ren_columns

de

