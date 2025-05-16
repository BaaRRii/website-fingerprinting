from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from scapy.all import sniff, wrpcap, AsyncSniffer
import threading
import subprocess
import time
import os

def setup_chrome():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-background-networking")
    options.add_argument("--disable-default-apps")
    options.add_argument("--disable-extensions")
    options.add_argument("--no-first-run")
    options.add_argument("--no-default-browser-check")
    options.add_argument("--disable-sync")
    options.add_argument("--disable-translate")
    options.add_argument("--metrics-recording-only")
    options.add_argument("--disable-background-timer-throttling")
    options.add_argument("--disable-client-side-phishing-detection")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-backgrounding-occluded-windows")
    options.add_argument("--disable-component-update")
    options.add_argument("--disable-domain-reliability")
    options.add_argument("--disable-notifications")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-insecure-localhost')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--disable-features=CertificateTransparency')
    options.add_argument("--dns-prefetch-disable")
    options.add_argument("--disable-cache")
    options.add_argument("--disable-http-cache")
    options.add_argument("--disable-ipc-flooding-protection")
    options.add_argument("--disable-prompt-on-repost")
    options.add_argument("--disable-renderer-backgrounding")
    options.add_argument("--disable-hang-monitor")
    options.add_argument("--disable-component-extensions-with-background-pages")
    options.add_argument("--disable-dev-tools")
    options.add_argument("--disable-zero-browsers-open-for-tests")
    options.add_argument("--no-service-autorun")
    options.add_argument("--hide-scrollbars")
    options.add_argument("--mute-audio")
    options.add_argument("--window-size=1920,1080")


    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver


def capture_packets(interface, pcap_path, duration):
    packets = sniff(iface=interface, timeout=duration)
    wrpcap(pcap_path, packets)
    print(f"Captura completada: {pcap_path}, {len(packets)} paquetes")


def capture(site, idx):
    interface = "eth0"
    pcap_path = f"/app/pcaps/{site.replace('/', '_')}_{idx}.pcap"
    try:
        
        tcpdump_cmd = [
            "tcpdump",
            "-i", interface,
            "-U",  # Escribir paquetes inmediatamente
            "-w", pcap_path
        ]
        tcpdump_process = subprocess.Popen(tcpdump_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(0.3) 

        driver = setup_chrome()
        driver.get(f"https://{site}")

        WebDriverWait(driver, 6).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

        time.sleep(2)
        print(f"Captura completada: {pcap_path} paquetes")

    except Exception as e:
        print(f"Error al acceder a {site}: {e}")

    finally:
        if 'driver' in locals():
            driver.quit()
        if 'tcpdump_process' in locals():
            tcpdump_process.terminate()
            try:
                tcpdump_process.wait(timeout=2)
            except subprocess.TimeoutExpired:
                tcpdump_process.kill()



sites = open("sites.txt").read().splitlines()

NUM_CAPTURES = 35

for i in range(26, NUM_CAPTURES):
    for site in sites:
        capture(site, i)
        

