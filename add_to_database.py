import pandas as pd


def add_to_base(real_data, qwasar_username, firstname, lastname, contact, season, study, telegram_username, user_id):
    d = {
        'qwasar_username': [qwasar_username],
        'firstname': [firstname],
        'lastname': [lastname],
        'contact': [contact],
        'season': [season],
        'study': [study],
        'telegram_username': [telegram_username],
        'user_id': [user_id],
    }
    data = pd.DataFrame(d)
    result = pd.concat([real_data, data])
    # print(result)

    result.to_csv('database.csv', index=False)


# real_data = pd.read_csv('./database/database.csv')
