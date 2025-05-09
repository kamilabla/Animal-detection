from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image
from io import BytesIO
import datetime
import time
import os

output_dir = "hippo_screenshots"
os.makedirs(output_dir, exist_ok=True)

options = Options()
options.add_argument('--headless')
options.add_argument('--window-size=1920,1080')

driver = webdriver.Chrome(options=options)  # SeleniumManager automatycznie dobiera ChromeDriver

driver.get("https://zoo.sandiegozoo.org/cams/hippo-cam")

time.sleep(10)  # poczekaj na załadowanie streamu

num_screenshots = 10
interval_seconds = 5

for _ in range(num_screenshots):
    screenshot = driver.get_screenshot_as_png()
    image = Image.open(BytesIO(screenshot))

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(output_dir, f"hippo_{timestamp}.png")
    image.save(filename)

    print(f"Zapisano zrzut ekranu: {filename}")
    time.sleep(interval_seconds)

driver.quit()
