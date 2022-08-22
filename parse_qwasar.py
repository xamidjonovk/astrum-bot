from bs4 import BeautifulSoup as bs
import pandas as pd
import mechanize
import http.cookiejar as cookielib

cj = cookielib.CookieJar()
br = mechanize.Browser()
br.set_cookiejar(cj)
br.open("https://casapp.us.qwasar.io/login?service=https%3A%2F%2Fupskill.us.qwasar.io%2Fusers%2Fservice", timeout=10)
br.select_form(nr=0)
br.form['username'] = 'jas.884@mail.ru'
br.form['password'] = 'jasur2171517'
br.submit()


def get_data_from_qwasar(data, usernames):
    student_data = {}
    counter = 0
    for i in usernames:
        try:
            br.open(f"https://upskill.us.qwasar.io/users/{i}")
            soup = bs(br.response().read(), 'html.parser')

            student_data['qwasar username'] = i
            student_data['ism-familiya'] = soup.find('h1', class_='text-c-yellow').text.strip()
            student_data['qwasardagi ballari '] = soup.find('div', {'id': 'user_qpoints'}).text.strip()
            student_data["hozirgi vaqtdagi o'qiyotgan sezoni"] = soup.find('div',
                                                                           class_='row p-t-10 align-items-center').find(
                'a').text.strip()
            student_data['qwasardagi hozirgi foizi'] = soup.find("div", class_="progress b-radius-1")['title'].strip()

            months = {'January': 'Yanvar', 'February': 'Fevral', 'March': 'Mart', 'April': 'Aprel', 'May': 'May',
                      'June': 'Iyun', 'July': 'Iyul', 'August': 'Avgust', 'September': 'Sentabr', 'October': 'Oktabr',
                      'November': 'Noyabr', 'December': 'Dekabr'}

            student_months = soup.find_all("div", {"class": 'border col-sm-4'})

            for month in student_months:
                sum_docode = 0
                sum_upskill = 0
                count_docode = 0
                count_upskill = 0
                student_active = month.find_all("div", {"class": 'c-pointer'})  # col text-c-white
                month_name = month.find_all("div", {"class": 'col text-c-white'})[0].text.strip()
                for link in student_active:
                    try:
                        if link['title']:
                            docode = float(link['title'].split("<br>")[1][8:-1])
                            upskill = float(link['title'].split("<br>")[2][8:-1])
                            if docode > 0:
                                count_docode += 1
                            if upskill > 0:
                                count_upskill += 1
                            sum_docode += docode
                            sum_upskill += upskill
                    except:
                        pass

                student_data[f"{months[month_name]} oyida docode vaqti"] = sum_docode
                student_data[f"{months[month_name]} oyida platformadagi vaqti"] = sum_upskill
                student_data[f"{months[month_name]} oyida aktiv docode kunlari"] = count_docode
                student_data[f"{months[month_name]} oyida platformadagi aktiv kunlari"] = count_upskill
        except:
            pass

        user_data = pd.DataFrame(pd.Series({i: str(student_data)[1:-1]}), columns=['data'])
        data = pd.concat([data, user_data])
        print(data)
        #
        print(counter, i)
        counter += 1

    return data


from students import usernames

full_data = get_data_from_qwasar(pd.DataFrame({}), usernames)

full_data.to_csv('real_database.csv')
