import pandas as pd


def return_userdata(username):
    data = pd.read_csv('real_database.csv')
    data = data[data['usernames'] == f'{username}'].values[0][1]

    return '\n'.join(data.split(", "))
