from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os
import time
from selenium.webdriver.common.by import By

options = Options()
# options.add_argument("--headless")  # コメントアウト解除で、バックグラウンド実行

service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=options)

# ダウンロードしたい再生リストURLを指定する
playlist_url = "https://www.youtube.com/playlist?list=hogehoge"
downloader_url = "https://www.y2mate.com/jp3"

# ここからYoutube動画のURLを取得
browser.get(playlist_url)
time.sleep(5)

target_elems = browser.find_elements(
    "class name", "yt-simple-endpoint.style-scope.ytd-playlist-video-renderer"
)

urls = []
for target_elem in target_elems:
    url = target_elem.get_attribute("href")
    urls.append(url)

browser.quit()
time.sleep(5)

# ここからダウンロード処理
i = 1
for url in urls:
    browser = webdriver.Chrome(service=service, options=options)

    browser.get(downloader_url)
    time.sleep(10)

    elem = browser.find_element("class name", "form-control")
    elem.send_keys(url)
    elem_btn = browser.find_element("id", "btn-submit")
    elem_btn.click()
    time.sleep(5)

    elem_download = browser.find_element(
        By.XPATH, "//div[@id='mp4']//tbody/tr[2]/td[3]/button"
    )

    onclick_script = elem_download.get_attribute("onclick")
    browser.execute_script(onclick_script)

    time.sleep(5)
    elem_download1 = None
    while not elem_download1:
        elem_download1 = browser.find_element(
            By.CSS_SELECTOR, "a.btn.btn-success.btn-file"
        )
        time.sleep(1)
    href_value = elem_download1.get_attribute("href")
    browser.get(href_value)
    time.sleep(2)
    download_prossing_done_checker = False
    while not download_prossing_done_checker:
        time.sleep(4)
        download_files = os.listdir("/Users/sobaotto/Downloads")
        for download_file in download_files:
            if ".crdownload" in download_file:
                download_prossing_done_checker = False
                break
            else:
                download_prossing_done_checker = True
    browser.quit()
    print(f"ダウンロード完了！-----{i}/{len(urls)}")
    i += 1

browser.quit()
