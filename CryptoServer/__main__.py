from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import json
import tweepy
from CryptoServer.Telegram import telegramsend

current_id=1
current_data=""
website_link=""

def check_shedule():
    url = 'http://kreasaard.atwebpages.com/laravel/public/api/check_for_shedule'
    # url = 'http://127.0.0.1:8000/api/check_for_shedule'
    myobj = {'key':"a78f6278eg2d6273rg27g28"}
    x = requests.post(url, data = myobj)
    print(x.text)
    if(x.text=="false"):
        return False
    else:
        return True

def get_data():
    global current_id
    global current_data
    url = 'http://kreasaard.atwebpages.com/laravel/public/api/get_to_post_for_crypto'
    # url = 'http://127.0.0.1:8000/api/get_to_post_for_crypto'
    myobj = {'key':"a78f6278eg2d6273rg27g28"}
    x = requests.post(url, data = myobj)
    print(x.text)
    print(x.json())
    current_id=x.json()['id']
    current_data=x.json()['data']
    print("stage3")

def post_to_twitter():

    global current_data

    access_token='1446761614565253121-voeFO3BEjZBGQFRHukoV8H1FakOKxS'
    access_secret='tCwuU4QrD5ALwODd74RFXjcaRoyz5PL7n4Wl779HUQbTA'
    api_key='bdgrttVxTROKRviSdDycUuKBc'
    api_secret='pFnwHK3BVjs2A5DHG9oU8aaAaPTsG6OAquRpyVAe96EVjjsdnr'

    print("stage 1")
    auth=tweepy.OAuthHandler(api_key,api_secret)
    auth.set_access_token(access_token,access_secret)
    api=tweepy.API(auth)
    print("stage 2")
    print(current_data)
    # api.update_with_media(current_data)
    # api.PostUpdate(current_data)
    api.update_status(current_data)
    print("stage 3")
    return True

def post_to_telegram():
    print("test")
    telegramsend.posttotele(current_data)
    print("test1")
    return True

def update_to_server():
    global current_id
    global current_data
    url = 'http://kreasaard.atwebpages.com/laravel/public/api/updatecrypto'
    # url = 'http://127.0.0.1:8000/api/updatecrypto'
    myobj = {'key':"a78f6278eg2d6273rg27g28",'id':current_id}
    x = requests.post(url, data = myobj)
    print(x.text)

def insert_new_data(data):
    url = 'http://kreasaard.atwebpages.com/laravel/public/api/insert_new_data'
    myobj = {'key':"a78f6278eg2d6273rg27g28",'data':data}
    x = requests.post(url, data = myobj)
    print(x.text)

def main_post_controller():
    global current_id
    current_id=0
    if(check_shedule()):
        try:
            print("stage1")
            get_data()
            print("stage2")
            if(current_data=="nopostavailable"):
                print("no post available")
            else:
                print(current_id)
                #post_to_telegram() 
                post_to_twitter()
                update_to_server()
                print("crypto post done")
        except:
            print("error occured")

    else:
        print("not scheduled for crypto post")

# insert_new_data("Hello how are you")
while(True):
    main_post_controller()
    time.sleep(900)
