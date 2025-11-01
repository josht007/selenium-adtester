from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = Options()
chrome_options.add_argument("--start-maximized")

service = Service("path/to/chromedriver")

driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 15)

try:
    driver.get("https://www.youtube.com")
    search_box = wait.until(EC.presence_of_element_located((By.NAME, "search_query")))
    search_box.send_keys("NBA highlights")
    search_box.send_keys(Keys.RETURN)
    first_video = wait.until(EC.presence_of_element_located((By.ID, "video-title")))
    first_video.click()
    time.sleep(5)
    try:
        ad_element = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".ytp-ad-text, .ytp-ad-player-overlay"))
        )
        print("✅ Ad detected before or during video playback.")
    except:
        print("❌ No ad detected before or during video playback.")
    driver.save_screenshot("youtube_test_result.png")
finally:
    time.sleep(5)
    driver.quit()
