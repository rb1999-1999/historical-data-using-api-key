# historical-data-using-api-key
from time import sleep
from kiteconnect import KiteConnect
import pandas as pd
from datetime import datetime, timedelta, time
from selenium import webdriver
time_end = datetime.now() + timedelta(minutes=1)


def test_time_loop(true=None):
    while datetime.now() < time_end:
        api_key()




def api_key():
    ak = 'api key '
    ask = 'secret api key'
    kite = KiteConnect(api_key=ak)
    requst_tkn = set_up()
    print(requst_tkn)
    data = kite.generate_session(requst_tkn, api_secret=ask)
    kite.set_access_token(data["access_token"])
    # print(data['access_tkn'])
    trd_portfolio = {'stock name ': {'token': stock token}}
    token = "stoke token"
    to_date = datetime.now()
    from_date = to_date - timedelta(minutes=20)
    interval = "minute"
    records = kite.historical_data(token, from_date, to_date, interval)
    df = pd.DataFrame(records)
    df.to_csv("datatest.csv")
       print(df)


def set_up():
    driver = webdriver.Chrome("chrome driver loaction in machine ")
    # URL of the website
    url = "https://kite.trade/connect/login?api_key=apikey"
    driver.get("https://kite.trade/connect/login?api_key=apikey")
    # driver.minimize_window()
    z_userid = "your user name "
    z_pwd = "your password "
    z_pin = "your pin"
    # Set username
    sleep(2)
    inputElement = driver.find_element_by_id("userid")
    inputElement.send_keys(z_userid)
    # Set password
    pwdElement = driver.find_element_by_id("password")
    pwdElement.send_keys(z_pwd)
    # Login
    inputElement.submit()

    # Set PIN (6 digit)
    sleep(3)
    pwdElement = driver.find_element_by_id("pin")
    pwdElement.send_keys(z_pin)
    pwdElement.submit()

    # Getting current URL
    sleep(5)
    get_url = driver.current_url

    # Printing the URL AND SPLITING TO GET ACCESS TOKEN 
    print(get_url)
    split_url = get_url.split("=")
    split_url = split_url[1].split("&")
    # print(split_url[0])
    access_token = split_url[0]
    print(access_token)
    return access_token
