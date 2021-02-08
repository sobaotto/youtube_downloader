from selenium.webdriver.chrome.options import Options

options = Options()

options.add_argument("--headless")

from selenium import webdriver
import chromedriver_binary
import os
import time

#ダウンロードしたい再生リストURLを指定する
playlist_url = "https://www.youtube.com/playlist?list=hogehogehoge"
downloader_url = "https://www.y2mate.com/jp3"

#ここからYoutube動画のURLを取得

#以下、①②のどちらかはコメントアウト
#①ブラウザを起動せずバックグラウンドで実行する
browser = webdriver.Chrome(options = options)
#②ブラウザを起動して実行する
#browser = webdriver.Chrome()

browser.get(playlist_url)
time.sleep(5)

target_elems = browser.find_elements_by_class_name("yt-simple-endpoint.style-scope.ytd-playlist-video-renderer")

urls = []
for target_elem in target_elems:
    url = target_elem.get_attribute("href")
    urls.append(url)

browser.quit()
time.sleep(5)


#ここからダウンロード処理
for url in urls:
    #以下、①②のどちらかはコメントアウト
    #①ブラウザを起動せずバックグラウンドで実行する
    #browser = webdriver.Chrome(options = options)
    #②ブラウザを起動して実行する
    browser = webdriver.Chrome()
    
    browser.get(downloader_url)
    time.sleep(10)
    
    elem = browser.find_element_by_class_name("form-control")
    elem.send_keys(url)
    elem_btn = browser.find_element_by_id("btn-submit")
    elem_btn.click()
    time.sleep(5)

    elem_download = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div[4]/div/div[2]/div/div[1]/table/tbody/tr[1]/td[3]/a")
    elem_download.click()
    time.sleep(30)

    elem_download1 = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/a")
    elem_download1.click()
    
    download_prossing_done_checker = False
    while download_prossing_done_checker == False:
        time.sleep(10)
        download_files = os.listdir("/Users/ryota/Downloads")
        for download_file in download_files:
            if ".crdownload" in download_file:
                download_prossing_done_checker = False
                break
            else:
                download_prossing_done_checker = True
    browser.quit()

browser.quit()
