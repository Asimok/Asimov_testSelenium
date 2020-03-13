import time
import sys
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

path = '浏览日志/'
# 阅读文章
def read_articles(articles_num):
    print("开始阅读文章------总任务"+str(articles_num*2))
    urls = ["https://www.xuexi.cn/xxqg.html?id=36a1bf1b683942fe917fc1866f13fc21",
            "https://www.xuexi.cn/xxqg.html?id=2813415f8e1c48b4b47e794aca7b7bb5"]
    titles=['最新消息','直击一线']
    # 最新消息
    # 直击一线
    for num, url in enumerate(urls):
        # 生成序列
        myChrome.get(url)
        myChrome.implicitly_wait(10)
        # 使用隐式等待10s，如果 WebDriver没有在 DOM中找到元素，将继续等待，超出设定时间后则抛出找不到元素的异常
        articles = myChrome.find_elements_by_xpath("//div[@class='text-link-item-title']")
        for index, article in enumerate(articles):
            if index >= articles_num:
                print("该分区阅读文章任务已达上限")
                break
            print("正在阅读第"+str(3*num+index+1)+'篇')
            article.click()
            all_handles = myChrome.window_handles
            myChrome.switch_to.window(all_handles[-1])
            myChrome.get(myChrome.current_url)
            nowTime = time.strftime('%m-%d_', time.localtime(time.time()))
            myChrome.save_screenshot(path + nowTime+titles[num] + '_' + str(index+1) + '.png')
            # 模拟滚动
            for i in range(0, 2000, 100):
                # 20*3 每篇文章两分钟
                js_code = "var q=document.documentElement.scrollTop=" + str(i)
                myChrome.execute_script(js_code)
                time.sleep(3)
            for i in range(2000, 0, -100):
                js_code = "var q=document.documentElement.scrollTop=" + str(i)
                myChrome.execute_script(js_code)
                time.sleep(3)
            time.sleep(10)
            myChrome.close()
            myChrome.switch_to.window(all_handles[0])
    print("\n阅读文章完毕\n")


def watch_videos(videos_num):
    print("开始观看视频------总任务"+str(2*videos_num))
    # titles = ['重要活动视频专辑', '学习专题报道', '学习新视界', '十九大报告视频','新闻联播']
    titles = [ '学习新视界', '十九大报告视频','新闻联播']
    myChrome.get(
        'https://www.xuexi.cn/4426aa87b0b64ac671c96379a3a8bd26/db086044562a57b441c24f2af1c8e101.html')
    myChrome.implicitly_wait(10)
    for num, title in enumerate(titles):
        myChrome.find_elements_by_xpath("//*[contains(text(), '" + title + "')]")[0].click()
        time.sleep(2)
        videos = myChrome.find_elements_by_xpath("//div[@class='textWrapper']")
        time.sleep(2)
        for index, video in enumerate(videos):
            if index >= videos_num:
                print("该分区观看视频任务已达上限")
                break
            print("正在观看第" + str(2*num+index+1) + '个')
            video.click()
            all_handles = myChrome.window_handles
            myChrome.switch_to.window(all_handles[-1])
            # 模拟点击播放
            myChrome.get(myChrome.current_url)
            myChrome.find_element_by_xpath("//div[@class='outter']").click()
            time.sleep(3)
            nowTime = time.strftime('%m-%d_', time.localtime(time.time()))
            myChrome.save_screenshot(path +nowTime+titles[num] + '_' + str(index+1) + '.png')

            # 可以获取视频当前时长
            video_current_time_str = myChrome.find_element_by_xpath(
                "//span[@class='duration']").get_attribute('innerText')
            print(video_current_time_str)

            # 每个视频开启后停留190秒，然后把所有句柄关闭
            time.sleep(190)
            myChrome.close()
            myChrome.switch_to.window(all_handles[0])
    print("\n播放视频完毕\n")


def get_integrals():
    # 获取当前积分
    myChrome.get('https://pc.xuexi.cn/points/my-points.html')
    time.sleep(2)
    gross_score = myChrome.find_element_by_xpath(
        "//*[@id='app']/div/div[2]/div/div[2]/div[2]/span[1]").get_attribute('innerText')
    today_score = myChrome.find_element_by_xpath("//span[@class='my-points-points']").get_attribute(
        'innerText')
    print("当前总积分：" + str(gross_score))
    print("今日积分：" + str(today_score))
    print("获取积分完毕，即将退出\n")


def get_integralsTemp():
    global myChrome
    # 获取当前积分
    myChrome.get('https://pc.xuexi.cn/points/my-points.html')
    time.sleep(2)
    gross_score = myChrome.find_element_by_xpath(
        "//*[@id='app']/div/div[2]/div/div[2]/div[2]/span[1]").get_attribute('innerText')
    today_score = myChrome.find_element_by_xpath("//span[@class='my-points-points']").get_attribute(
        'innerText')
    print("当前总积分：" + str(gross_score))
    print("今日已经积分：" + str(today_score))

def checkDir():
    if not os.path.exists("浏览日志"):
        os.mkdir("浏览日志")


def login():
    checkDir()
    option = webdriver.ChromeOptions()
    option.add_argument('disable-infobars')
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    myChrome = webdriver.Chrome()
    myChrome.get('https://pc.xuexi.cn/points/login.html')
    myChrome.execute_script("var q=document.documentElement.scrollTop=950")
    myChrome.execute_script("var q=document.documentElement.scrollLeft=225")
    time.sleep(3)
    nowTime = time.strftime('%m-%d_', time.localtime(time.time()))
    myChrome.save_screenshot(path + nowTime + '扫码登陆.png')
    print(path + nowTime + '扫码登陆.png')
    time.sleep(15)
    try:
        WebDriverWait(myChrome, 60).until(EC.title_is(u"我的学习"))
        print('登录成功')
    except:
        myChrome.find_elements_by_xpath("//span[@class='refresh']")[0].click()
        time.sleep(1.5)
        nowTime = time.strftime('%m-%d_', time.localtime(time.time()))
        myChrome.save_screenshot(path + nowTime + '扫码登陆.png')
        print('登录超时，脚本退出')
        exit()
    # 进入首页
    myChrome.get("https://www.xuexi.cn/")
    myChrome.implicitly_wait(10)

if __name__ == '__main__':

    login()
    get_integralsTemp()  # 获得当前积分
    read_articles(3)  # 阅读文章 2*3
    get_integralsTemp()  # 获得当前积分
    watch_videos(2)  # 观看视频 3*2
    get_integrals()  # 获得今日积分
    myChrome.close()
    exit()