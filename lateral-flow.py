#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime
import argparse
from plyer import notification

parser = argparse.ArgumentParser(description="Checks the gov.uk at regular intervals for order availability of lateral flow test kits.")
parser.add_argument("-t", "--interval", dest="interval", type=int, default=1800, help="Checking interval in seconds (default: %(default)s)")
parser.add_argument("-s", "--save-available", dest="save_available", action="store_true", help="Saves HTML source when LFTs are available")
parser.add_argument("-S", "--save-unavailable", dest="save_unavailable", action="store_true", help="Saves HTML source when LFTs are not available")
parser.add_argument("-n", "--notify-desktop-available", dest="notify_desktop_available", action="store_true", help="Send a desktop notification when LFTs are available")
parser.add_argument("-N", "--notify-desktop-unavailable", dest="notify_desktop_unavailable", action="store_true", help="Send a desktop notification when LFTs are unavailable")
parser.add_argument("-b", "--browser", dest="headless_browser", action="store_false", help="Display the browser")
parser.add_argument("-v", "--verbose", dest="verbose", action="store_true", help="Print extra debug information")

args = parser.parse_args()
sleep_time = args.interval
save_available = args.save_available
save_unavailable = args.save_unavailable
verbose = args.verbose
notify_desktop_available = args.notify_desktop_available
notify_desktop_unavailable = args.notify_desktop_unavailable
headless_browser = args.headless_browser

url = "https://test-for-coronavirus.service.gov.uk/order-lateral-flow-kits"
search_string = "Sorry, there are no home delivery slots left for rapid lateral flow tests right now"
error_sleep_time = sleep_time

chrome_options = Options()
if headless_browser:
    chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)


while (True):
    now = datetime.now()
    timestamp = now.strftime("%c")

    try:
        driver.get(url)
    except:
        print("At " + timestamp + " an error occured getting the page. Maybe you're disconnected from the internet?")
        time.sleep(error_sleep_time)
        continue

    source = driver.page_source
    tests_available = not (search_string in source)

    save_source = False
    if tests_available:
        print("At " + timestamp + " TESTS WERE AVAILABLE!!!")
        save_source = save_available
        if notify_desktop_available:
            notification.notify(
                    title="LFTs Available",
                    message="LATERAL FLOW TESTS ARE AVAILABLE!!!!",
                    timeout=10
            )
    else:
        print("At " + timestamp + " tests were not available")
        save_source = save_unavailable
        notification.notify(
                title="LFTs unavailable",
                message="Lateral flow tests are unavailable.",
                timeout=10
        )

    
    if save_source:
        try:
            f = open("saved page " + timestamp + ".html", "wt")
            f.write(source);
        except:
            print("IO error when saving HTML file")
        finally:
            f.close()

    time.sleep(sleep_time)
