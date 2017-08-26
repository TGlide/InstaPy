"""Module only used to log the number of followers to a file"""
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException
import csv


def log_follower_num(browser, username):
    """Prints and logs the current number of followers to
    a seperate file"""
    browser.get('https://www.instagram.com/' + username)

    followed_by = browser.execute_script("return window._sharedData.entry_data.ProfilePage[0].user.followed_by.count")

    with open('./logs/followerNum.txt', 'a') as numFile:
        numFile.write('{:%Y-%m-%d %H:%M} {}\n'.format(datetime.now(), followed_by or 0))


def log_followed_pool(login, followed):
    """Prints and logs the followed to
    a separate file"""
    current_date = datetime.now()
    d_m_y = "{0}.{1}.{2}".format(current_date.day, current_date.month, current_date.year)
    try:
        with open('./logs/' + login + '_followedPool.csv', 'a') as followPool:
            followPool.write(followed + "," + d_m_y + "\n")
    except BaseException as e:
        print("log_followed_pool error \n", str(e))


def log_interacted_pool(login, interacted):
    try:
        with open('./logs/' + login + '_interactedPool.csv', 'a') as interactedPool:
            interactedPool.write(interacted + ",\n")
    except BaseException as e:
        print("log_interacted_pool error \n", str(e))


def get_interacted(login):
    interacted = []
    try:
        with open('./logs/' + login + '_interactedPool.csv', newline='') as interactedPool:
            interacted_reader = csv.reader(interactedPool,)
            for row in interacted_reader:
                interacted.append(row[0])
    except BaseException as e:
        print("log_interacted_pool error \n", str(e))
    return interacted
