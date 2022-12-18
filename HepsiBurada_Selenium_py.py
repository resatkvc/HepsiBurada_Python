from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
import time

def drive_sec(gelen):
    if gelen == "Firefox":
        return webdriver.Firefox()
    elif gelen == "Chrome":
        return webdriver.Chrome()
    elif gelen == "Edge":
        return webdriver.Edge()
    return "Yok"

def senaryo(driver):

    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.hepsiburada.com/")
    time.sleep(1)
    # Menünün Elektronik seçeneğine tıklayın
    Elektronik = driver.find_element(By.CLASS_NAME, "sf-MenuItems-UHHCg2qrE5_YBqDV_7AC")
    time.sleep(1)
    hareket = ActionChains(driver)
    hareket.move_to_element(Elektronik)
    hareket.perform()
    time.sleep(1)
    # Bilgisayar/Tablet seçeneğine tıklayın
    Bilgisayar = driver.find_element(By.CLASS_NAME, "sf-ChildMenuItems-a4G0z3YJJWkQs7qKKuuj")
    time.sleep(1)
    hareket = ActionChains(driver)
    hareket.move_to_element(Bilgisayar)
    hareket.perform()
    # Notebook seçeneğine tıklayın
    Notebook = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[5]/div[3]/div/div/div/div/div/div/div[1]/div/ul/li[1]/div/div/div/div[1]/ul/li/div/ul[1]/li/ul[1]/li/a[2]")
    time.sleep(1)
    hareket = ActionChains(driver)
    hareket.move_to_element(Notebook)
    hareket.perform()
    Notebook.click()
    #Marka Apple seçin
    Apple = driver.find_element(By.XPATH, "/html/body/div[3]/main/div[2]/div/div[5]/div/div/div/div/div[2]/section/div[4]/div[2]/a")
    Apple.click()
    #Dropdown dan cok satanlar seçilir
    dropdown = driver.find_element(By.XPATH, "/html/body/div[3]/main/div[2]/div/div[6]/div[2]/div[2]/div/div/div/div/div/div")
    dropdown.click()
    time.sleep(1)
    coksatanlar = driver.find_element(By.XPATH, "/html/body/div[3]/main/div[2]/div/div[6]/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div[1]/a[3]/label/div/div")
    hareket = ActionChains(driver)
    hareket.move_to_element(coksatanlar)
    hareket.perform()
    time.sleep(1)
    coksatanlar.click()
    #Scroll bar
    driver.execute_script("window.scrollBy(0,250)","")
    #Cok satanların ikincisi seçilir
    secondList = driver.find_element(By.XPATH, "/html/body/div[3]/main/div[2]/div/div[7]/div/div[2]/div/div[3]/div/div/div/div/div/div/ul/li[2]/div/a/div[2]/h3")
    hareket = ActionChains(driver)
    hareket.move_to_element(secondList)
    hareket.perform()
    time.sleep(1
    choose = driver.find_element(By.XPATH, "/html/body/div[3]/main/div[2]/div/div[7]/div/div[2]/div/div[3]/div/div/div/div/div/div/ul/li[2]/div/a/div[2]/div[1]")
    choose.click()
    time.sleep(1)
    #Yeni sekme
    mainPage = driver.window_handles[0]
    driver.switch_to.window(mainPage)
    documentsPage = driver.window_handles[1]
    driver.switch_to.window(documentsPage)
    #scroll bar
    driver.execute_script("window.scrollBy(0,250)","")
    time.sleep(1)#sepete ekle botonuna basılır
    button = driver.find_element(By.CSS_SELECTOR, "html body.desktop.voltran-container.sf-pd-detail.complete div.wrapper main.content-wrapper div.product-detail-module section.detail-main div.container.contain-lg-4.contain-md-4.contain-sm-1.fluid div.productDetailContent div.productDetailRight.col.lg-2.md-2.sm-1.grid-demo-fluid div.product-information.col.lg-5.sm-1 div.product-variants-content.add-to-cart-content form#addToCartForm span.addToCartButton button#addToCart.button.big.with-icon")
    button.click()
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, -250)","")
    time.sleep(1)
    #sepete git
    sepeteGit = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div/div/div/div/div[2]/div[3]/a")
    sepeteGit.click()
    time.sleep(2)
    #alısverisi tamamla
    alisverisitamamla = driver.find_element(By.ID,"continue_step_btn")
    alisverisitamamla.click()
    driver.quit()
selected_driver = drive_sec("Firefox")
senaryo(selected_driver)
selected_driver = drive_sec("Chrome")
senaryo(selected_driver)
selected_driver = drive_sec("Edge")
senaryo(selected_driver)