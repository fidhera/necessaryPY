# Program mendownload Vidio Tiktok (VT) dengan menginput linkkkkkkkk
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import requests

def download_tiktok_video(video_url, file_name):
    # Setup webdriver
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(video_url)
        video_element = driver.find_element(By.XPATH, '//video')
        video_url = video_element.get_attribute('src')

        video_data = requests.get(video_url).content

        with open(file_name, 'wb') as video_file:
            video_file.write(video_data)

        print(f"Video berhasil di-download dan disimpan sebagai {file_name}.")
    except Exception as e:
        print(f"Gagal mendownload video: {e}")
    finally:
        driver.quit()

# Meminta input dari pengguna
video_url = input("Masukkan URL video TikTok: ")
file_name = input("Masukkan nama file untuk menyimpan video (contoh: video.mp4): ")

# Mendownload video
download_tiktok_video(video_url, file_name)
