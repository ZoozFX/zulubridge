from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def get_latest_trades():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get("https://www.zulutrade.com/dashboard")

    time.sleep(10)  # عدلها حسب سرعة الإنترنت وتحميل الصفحة

    # إذا كانت الجلسة مفتوحة سيتم تحميل الصفحة مباشرة
    trades = []
    try:
        rows = driver.find_elements(By.CSS_SELECTOR, ".trades-table tbody tr")
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) > 5:
                trade = {
                    "symbol": cells[0].text,
                    "type": cells[1].text,
                    "lot": cells[2].text,
                    "open_price": cells[3].text,
                    "tp": cells[4].text,
                    "sl": cells[5].text
                }
                trades.append(trade)
    except:
        trades.append({"error": "Could not load trades. Maybe not logged in?"})

    driver.quit()
    return trades
