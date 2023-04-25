import os

import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from tqdm import tqdm

try:
    chromedriver_autoinstaller.install()
except BaseException as e:
    print(e)


def set_chrome_options():
    chrome_options = Options()
    for e in [
        "enable-automation",
        "start-maximized",
        "disable-infobars",
        "--disable-infobars",
        "--headless",
        "--no-sandbox",
        "--force-device-scale-factor=1",
        "--disable-extensions",
        "--disable-dev-shm-usage",
        "--disable-gpu",
    ]:
        chrome_options.add_argument(e)

    chrome_prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    return chrome_options


def get_driver(url):
    # start = datetime.datetime.now()
    driver = webdriver.Chrome(options=set_chrome_options())
    # driver = webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.HTMLUNIT)
    driver.implicitly_wait(0.05)
    driver.set_page_load_timeout(60 * 60 * 60)
    driver.get(url)
    # end = datetime.datetime.now()
    # print(end - start)
    return driver


for d in tqdm(sorted(os.listdir("./"))):
    if not os.path.isdir(f"./{d}") or d.startswith("."):
        continue

    ps_filepath = f"./{d}/problem_statement.txt"
    if os.path.exists(ps_filepath) and os.stat(ps_filepath).st_size > 0:
        continue

    url = f"https://leetcode.com/problems/{d}/"

    driver = get_driver(url)

    wrapper = driver.find_element(
        By.XPATH, '//*[@id="qd-content"]/div[1]/div/div/div/div[2]/div/div/div[3]/div'
    )
    data = wrapper.text
    final_data = ""
    for line in data.splitlines():
        line = line.strip()
        if any([line.startswith(e) for e in ["Example", "Constraints", "Follow-up"]]):
            final_data += "\n"
        final_data += line + "\n"

    with open(ps_filepath, "w") as f:
        f.write(final_data.strip())
