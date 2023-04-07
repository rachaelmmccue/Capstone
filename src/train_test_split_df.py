import pandas

def train_test_split_df(df):
    

    Train = []
    Test = []

    for index, row in df.iterrows():    

        if df['session_position'][index] <= df['session_length'][index]*.7:
            Train.append(row)
        else:
            Test.append(row)

    Train = pandas.DataFrame(Train)
    Test = pandas.DataFrame(Test)

    return Train, Test
