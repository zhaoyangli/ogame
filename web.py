from selenium import webdriver
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC  # available since 2.26.0
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver import TouchActions
from selenium.webdriver.common.keys import Keys
import requests
import xml.etree.ElementTree as ET
import random
import re

PLANT_LIST = [
    ['1:85:9', '33722864', '33803648'],
    ['1:346:10', '33841982', '33861030'],
    ['2:100:12', '33722868', '33803737'],
    ['5:100:12', '33722872', '33803637'],
    ['8:327:4', '33722869', '33803698'],
    ['8:328:4', '33722866', ''],
    ['8:328:5', '33722865', '33803699'],
    ['8:328:6', '33722867', '33803641'],
    ['8:328:7', '33722871', '33803694'],
    ['8:328:9', '33722870', '33803644'],
    ['8:328:10', '33745018', '33803646'],
]
SOURCE_LIST = [
    ['1:85:9', '33722864', '33803648'],
    ['1:346:10', '33841982', '33861030'],
    ['2:100:12', '33722868', '33803737'],
    ['5:100:12', '33722872', '33803637'],
    ['8:328:5', '33722865', '33803699'],
]
BLACK_LIST = ['1:334:10','1:335:9', '1:337:4', '1:337:5', '1:337:6',
              '3:1:4', '6:95:12','2:93:13','1:95:11','1:379:7',
              '4:265:7', '1:442:4', '1:442:5', '1:442:6', '1:442:9',
              '7:380:7','4:116:1','3:75:8',
              ]
fleet_link = 'https://s101-jp.ogame.gameforge.com/game/index.php?page=fleet1&cp='
DELAY = 1
SKIP = 326  # skip first I planet
xiaoyun = '77'

def delay_r(int_default):
    sleep(int_default)
    sleep(random.random()*int_default)


def yunshu(source_link, xiaoyun, target, moon=False, to_moon=False):
    '''

    :param plant_id: 8:328:4
    :param xiaoyun: 1899
    :param target: 8:328:5
    :param moon:
    :return:
    '''
    print('yunshu: ' + source_link + ' xiaoyun: ' + str(xiaoyun) + ' target: ' + target)
    plant_id = [_[1] for _ in PLANT_LIST if _[0] == source_link]
    moon_id = [_[2] for _ in PLANT_LIST if _[0] == source_link]
    source_link = fleet_link + plant_id[0] if not moon else fleet_link + moon_id[0]
    driver.get(source_link)
    input_xiaoyun = driver.find_element_by_id('ship_203')
    delay_r(DELAY)
    input_xiaoyun.send_keys(xiaoyun)
    delay_r(DELAY)

    button_next = driver.find_element_by_id('continue')
    button_next.click()
    delay_r(DELAY)
    button_plant = driver.find_element_by_id('pbutton')
    button_plant.click()
    delay_r(DELAY)
    ##
    galaxy = driver.find_element_by_id('galaxy')
    galaxy.clear()
    galaxy.send_keys(target.split(':')[0])
    delay_r(DELAY)

    system = driver.find_element_by_id('system')
    system.clear()
    system.send_keys(target.split(':')[1])
    delay_r(DELAY)

    position = driver.find_element_by_id('position')
    position.clear()
    position.send_keys(target.split(':')[2])
    delay_r(DELAY)

    speed = driver.find_element_by_xpath('// *[ @ id = "speedLinks"] / a[10]')
    speed.click()
    delay_r(DELAY)
    ##

    ##
    button_next2 = driver.find_element_by_id('continue')
    button_next2.click()
    delay_r(DELAY)

    button_mission = driver.find_element_by_id('missionButton3')
    button_mission.click()
    delay_r(DELAY)

    all_r = driver.find_element_by_xpath('//*[@id="allresources"]')
    all_r.click()
    delay_r(DELAY)

    button_start = driver.find_element_by_id('start')
    button_start.click()
    delay_r(DELAY)


def attack(source_link, xiaoyun, target, moon=False):
    '''
    :param plant_id: 1:85:9
    :param xiaoyun:77
    :param target:1:85:4
    :return:
    '''
    print('attacking: ' + source_link + ' xiaoyun: ' + str(xiaoyun) + ' target: ' + target)
    plant_id = [_[1] for _ in PLANT_LIST if _[0] == source_link]
    moon_id = [_[2] for _ in PLANT_LIST if _[0] == source_link]
    source_link = fleet_link + plant_id[0] if not moon else fleet_link + moon_id[0]
    driver.get(source_link)

    input_xiaoyun = driver.find_element_by_id('ship_202')
    input_xiaoyun.send_keys(xiaoyun)
    delay_r(DELAY)

    button_next = driver.find_element_by_id('continue')
    button_next.click()
    delay_r(DELAY)

    button_plant = driver.find_element_by_id('pbutton')
    button_plant.click()
    delay_r(DELAY)
    ##
    galaxy = driver.find_element_by_id('galaxy')
    galaxy.clear()
    galaxy.send_keys(target.split(':')[0])
    delay_r(DELAY)

    system = driver.find_element_by_id('system')
    system.clear()
    system.send_keys(target.split(':')[1])
    delay_r(DELAY)

    position = driver.find_element_by_id('position')
    position.clear()
    position.send_keys(target.split(':')[2])
    delay_r(DELAY)

    speed = driver.find_element_by_xpath('// *[ @ id = "speedLinks"] / a[10]')
    speed.click()
    delay_r(DELAY)
    ##
    ##
    button_next2 = driver.find_element_by_id('continue')
    button_next2.click()
    delay_r(DELAY)

    button_mission = driver.find_element_by_xpath('// *[ @ id = "missionButton1"]')
    button_mission.click()
    delay_r(DELAY)

    button_start = driver.find_element_by_id('start')
    button_start.click()
    delay_r(DELAY)


def is_clickable(plant_id):
    plant = fleet_link + plant_id
    driver.get(plant)
    button_next = driver.find_element_by_id('continue')
    driver.implicitly_wait(5)
    print(button_next.get_attribute('class'))
    sleep(5)

    input_xiaoyun = driver.find_element_by_id('ship_202')
    driver.implicitly_wait(5)
    input_xiaoyun.send_keys(7)
    delay_r(DELAY)
    print(button_next.get_attribute('class'))
    sleep(5)


def have_login(driver):
    result = False
    try:
        delay_r(DELAY)
        driver.get('https://s101-jp.ogame.gameforge.com/game/index.php?page=overview')
        delay_r(4)
        if 'Andromeda' in str(driver.title):
            print('logged in.')
            result = True
        # handles = driver.window_handles
        # target_handle = handles[0]
        # print(len(handles))
        # print(target_handle)
        # if len(handles) > 1:
            # for newhandle in handles:
            #     driver.switch_to_window(newhandle)
            #     print(driver.title)
            #     if 'Andromeda' in str(driver.title):
            #         target_handle = driver.current_window_handle
            #         break
            # for newhandle in handles:
            # for i in range(1, len(handles)-1):
            #     driver.switch_to_window(handles[i])
            #     # if not newhandle == target_handle:
            #     driver.close()
            # driver.switch_to_window(target_handle)
        else:
            print('Not logged in.')
        return result
    except Exception as e:
        print(e)
        # for i in range(0, 3):
        #     ActionChains(driver).key_down(Keys.SHIFT).send_keys(Keys.TAB).key_up(Keys.SHIFT).perform()
        #     if 'Andromeda' not in str(driver.title):
        #         ActionChains(driver).key_down(Keys.CONTROL).send_keys('w').key_up(Keys.CONTROL).perform()
        #     delay_r(DELAY)
        return False


def loggin(driver):
    try:
        # driver.get('https://s101-jp.ogame.gameforge.com/game/index.php?page=overview&relogin=1&loginType=email')
        driver.get('https://jp.ogame.gameforge.com/#login')
        # WebDriverWait(driver, 60).until(
        #     EC.presence_of_element_located((By.LINK_TEXT, "ログイン")))
        curpage_url = driver.current_url

        sleep(DELAY)
        # elem = driver.find_element_by_id('tabs')
        elem = driver.find_element_by_link_text('ログイン')
        elem.click()

        username = driver.find_element_by_id('usernameLogin')
        username.send_keys('4546296@qq.com')

        # print (driver.title)
        password = driver.find_element_by_id('passwordLogin')
        password.send_keys('tubieweiwu?')

        sleep(DELAY)
        driver.find_element_by_xpath('// *[ @ id = "autoLogin"]').click()
        sleep(DELAY)
        # print (driver.title)
        submit = driver.find_element_by_id('loginSubmit')
        submit.click()
        delay_r(DELAY)
        # need time to run script
        sleep(10)

        #
        # try:
        #     element = WebDriverWait(driver, 10).until(
        #         EC.presence_of_element_located((By.ID, "myDynamicElement"))
        #     )
        # finally:
        #     driver.quit()

        # driver.get('https://gf1.geo.gfsrv.net/static/bgl/js/main.72ed1199.js')
        # html = driver.page_source
        # driver.get(
        #     'https://s101-jp.ogame.gameforge.com/game/index.php?page=overview&relogin=1')
        # delay_r(DELAY)
        # driver.execute_script(html)
        # submit2 = driver.find_element_by_link_text('プレイ')
        # submit2.click()

        # driver.execute_script("/config/configuration.js")
        # driver.get('https://s101-jp.ogame.gameforge.com/game/index.php?page=overview&relogin=1&loginType=email')
        # driver.get('https://s101-jp.ogame.gameforge.com/game/index.php?page=overview&relogin=1')

        # TAB = '\ue004'
        # ENTER = '\ue007'
        # ActionChains(driver).send_keys('tab').send_keys('tab').send_keys('tab').send_keys('tab').send_keys(
        #     'enter').perform()
        # // *[ @ id = "accountlist"] / div / div[1] / div[2] / div[1] / div / div[10] / button
        # accountlist > div > div.rt-table > div.rt-tbody > div:nth-child(3) > div > div.rt-td.action-cell > button
        driver.find_element_by_xpath('//*[@id="accountlist"]/div/div/div[2]/div[1]/div/div[10]/button').click()
        # driver.find_element_by_css_selector('#accountlist > div > div.rt-table > div.rt-tbody > div:nth-child(3) > div > div.rt-td.action-cell > button')
        delay_r(DELAY)
        # driver.close()
        # driver.close()
        # accountlist > div > div.rt-table > div.rt-tbody > div:nth-child(5) > div > div.rt-td.action-cell > button > span
        # div.rt - tr - group: nth - child(5) > div:nth - child(1) > div: nth - child(10) > button:nth - child(1)
        # driver.find_element_by_css_selector('div.rt - tr - group: nth - child(5) > div:nth - child(1) > div: nth - child(10) > button:nth - child(1)').click()

        # while 'Lobby' not in str(driver.title):
        #     delay_r(DELAY)
        # for i in range(0, 10):
        #     ActionChains(driver).send_keys(Keys.TAB).perform()
        #     delay_r(DELAY)

        # for i in range(0, 5):
        #     ActionChains(driver).key_down(Keys.SHIFT).send_keys(Keys.TAB).key_up(Keys.SHIFT).perform()
        #     sleep(0.5)
        # ActionChains(driver).send_keys(Keys.ENTER).perform()

        # driver.send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(
        #     Keys.ENTER)
        # actions = ActionChains(driver)
        # touch = TouchActions(driver)
        # x = 20
        # y = 10
        # while x<3000:
        #     touch.move(x,y)
        #     actions.click()
        #     actions.click()
        #     x+=20
        #     y+=10
        #     sleep(0.1)
        # menu = driver.find_element_by_id('root')
        # actions.move_to_element(menu)
        # submit2 = driver.find_element_by_link_text('Andromeda')
        # r = driver.execute_script("return newsJason")
        # print(r)

        # driver.get(
        #     'https://lobby-api.ogame.gameforge.com/users/me/loginLink?id=109451&server[language]=jp&server[number]=101')
        # html = driver.page_source
        # print(html)
        # pattern = '{"url":"' + '[a-zA-Z0-9:\/-.?&;=]*' + '"}</pre>'
        # print(str(html).split('{"url":"')[1].split('"}</pre>')[0])
        # url = str(html).split('{"url":"')[1].split('"}</pre>')[0]
        # print(url)
        # # driver.get(url)
        # driver.get(
        #     'https://lobby-api.ogame.gameforge.com/users/me/accounts')
        # html = driver.page_source
        # print(html)
        # delay_r(DELAY)
        # driver.get(
        #     'https://lobby-api.ogame.gameforge.com/loading')
        # html = driver.page_source
        # print(html)
        # delay_r(DELAY)

        # driver.get(
        #     'https://s101-jp.ogame.gameforge.com/game/index.php?page=overview&relogin=1')
        # html = driver.page_source
        # print(html)
        # delay_r(DELAY)

        # submit2 = driver.find_element_by_link_text('tubiedada')
        # ActionChains(driver).move_to_element(submit2).click(submit2).perform()
        # submit2 = driver.find_element_by_link_text('プレイ')
        # submit2.click()

        # submit2 = driver.find_element_by_class_name('btn btn-primary')
        # driver.implicitly_wait(5)
        # submit2.click()
        # delay_r(DELAY)
        print('end')
    except Exception as e:
        print(e)
        driver.get('https://s101-jp.ogame.gameforge.com/game/index.php?page=overview&relogin=1&loginType=email')


def free_fleet_number(driver):
    try:
        driver.get('https://s101-jp.ogame.gameforge.com/game/index.php?page=movement')
        # ele = driver.find_element_by_xpath('//*[@id="slots"]/div[1]/span')
        ele = driver.find_element_by_xpath('//*[@id="inhalt"]/div[4]/span[2]/span[1]')
        current_fleet = int(ele.text)

        elet = driver.find_element_by_xpath('//*[@id="inhalt"]/div[4]/span[2]/span[2]')
        total_fleet = int(elet.text)
    except Exception as e:
        print(e)
        return 19

    return total_fleet - current_fleet


def find_planet_by_id(name):
    req = requests.get('https://s101-jp.ogame.gameforge.com/api/players.xml')
    root = ET.fromstring(req.content)
    for child in root:
        # id = child.attrib['id']
        na = child.attrib['name']
        if name == child.attrib['name']:
            id = child.attrib['id']
            print(id)
            break
    #     try:
    #         sta = child.attrib['status']
    #     except:
    #         sta = 'normal'
    #     if sta == 'I' or sta == 'i':
    #         print (id, name, sta)
    req = requests.get('https://s101-jp.ogame.gameforge.com/api/universe.xml')
    # print(req.content)
    root = ET.fromstring(req.content)
    print(root)
    for child in root:
        if child.attrib['player'] == id:
            # print(child.tag, child.attrib)
            print(child.attrib['coords'])
        # id = child.attrib['id']
        # name = child.attrib['name']
        # try:
        #     sta = child.attrib['status']
        # except:
        #     sta = 'normal'
        # if sta == 'I' or sta == 'i':
        #     print(id, name, sta)


def find_rank(id):
    req = requests.get('https://s101-jp.ogame.gameforge.com/api/highscore.xml?category=1&type=1')
    root = ET.fromstring(req.content)
    for child in root:
        try:
            if id == child.attrib['id']:
                return child.attrib['position']
        except Exception as e:
            return ''


def is_noob(id):
    req = requests.get('https://s101-jp.ogame.gameforge.com/api/highscore.xml?category=1&type=1')
    root = ET.fromstring(req.content)
    for child in root:
        try:
            if id == child.attrib['id']:
                return int(child.attrib['score']) <= 44000
        except Exception as e:
            print(e)
            return True

def find_I():
    '''
    :return: list of I planet
    '''
    Iplayer = []
    results = []
    req = requests.get('https://s101-jp.ogame.gameforge.com/api/players.xml')
    root = ET.fromstring(req.content)
    for child in root:
        try:
            sta = child.attrib['status']
        except:
            sta = 'normal'
        if sta == 'I' and not is_noob(child.attrib['id']):
            Iplayer.append(child.attrib['id'])
    req = requests.get('https://s101-jp.ogame.gameforge.com/api/universe.xml')
    # print(req.content)
    root = ET.fromstring(req.content)
    for child in root:
        if child.attrib['player'] in Iplayer:
            # print(child.tag, child.attrib)
            results.append(child.attrib['coords'])
    return results


def find_distance(co1, co2):
    coor1 = co1.split(':')
    coor2 = co2.split(':')
    if coor1[0] == coor2[0]:
        return (float(abs(int(coor1[1]) - int(coor2[1])) / 250))
    else:
        dis = abs(int(coor1[0]) - int(coor2[0]))
        if dis <= 4:
            return dis
        else:
            return abs(9 - dis)


def find_source(coord):
    source = ''
    source_list = [_[0] for _ in SOURCE_LIST]
    source_list_withd = []
    for _ in source_list:
        source_list_withd.append({'co': _, 'dis': find_distance(_, coord)})

    def dis(s):
        return s['dis']

    result = sorted(source_list_withd, key=dis)
    return result[0]['co']


def yunshu_to_83285(driver):
    yunshuxiaoyun = 3333
    for _ in PLANT_LIST:
        if _[0].split(':')[0] == '8':
            try:
                yunshu(_[0], yunshuxiaoyun, '8:328:5')
            except Exception as e:
                print(e)
                pass

driver = webdriver.Chrome()
Ilist = find_I()
while True:
    while not have_login(driver):
        loggin(driver)
        delay_r(5)
    print('logged')
    length = len(Ilist)
    i = 0
    for Iplant in Ilist:
        i += 1
        if Iplant in BLACK_LIST:
            continue
        if i < int(SKIP):
            print(('skip: %s / %s') % (str(i), str(length)))
            continue
        else:
            SKIP = 0
        print(('%s / %s') % (str(i), str(length)))
        try:
            while free_fleet_number(driver) < 2:
                delay_r(180)
            source = find_source(Iplant)
            attack(source, xiaoyun, Iplant)
            delay_r(DELAY)
        except Exception as e:
            print(e)
            while not have_login(driver):
                loggin(driver)
                delay_r(5)
            try:
                print('try again')
                attack(source, xiaoyun, Iplant)
            except Exception as e:
                print(e)


# is_clickable('33803648')

# plant_id = str(33803648)
# target = [1, 85, 4]
# attack(plant_id, xiaoyun, target)
#
# plant_id = str(33841982)
# target = [1, 352, 6]
# attack(plant_id, xiaoyun, target)
# driver.close()
