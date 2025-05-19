from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "neutral+running+shoes"
file = 0
for i in range (1, 20):
    driver.get(f"https://www.amazon.com/s?k=neutral+running+shoes&i=fashion&page={i}&content-id=amzn1.sym.8abbd447-1969-42f6-a01f-457e40e4fa71%3Aamzn1.sym.8abbd447-1969-42f6-a01f-457e40e4fa71&pd_rd_r=8e72cf34-b9d6-4578-afd8-6b2dc8928c14&pd_rd_w=0uDqR&pd_rd_wg=srOPY&pf_rd_p=8abbd447-1969-42f6-a01f-457e40e4fa71&pf_rd_r=7F7Y2A6G89DJ8KAWSJ34&qid=1747639307&sprefix=neutral+running+shoes%2Caps%2C98&wi=ff0ec07d-4319-4655-8bd1-84411325856c_1&ref=slsr_runtype_d_t_m_vn_ff0ec07d-4319-4655-8bd1-84411325856c_1")
    elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")
    print(f"{len(elems)} items found")
    for elem in elems:
        d = elem.get_attribute('outerHTML')
        with open(f"data/{query}_{file}.html", 'w', encoding='utf-8') as f:
            f.write(d)
            file += 1

    time.sleep(2)
driver.close()