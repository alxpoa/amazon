from selenium import webdriver
import csv
from time import sleep

e = csv.writer(open('ConsultaChrome.csv', 'w'))
e.writerow(['descrição','valor (R$)'])

driver = webdriver.Chrome()
driver.get('https://www.amazon.com.br')
search = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
search.send_keys(input('qual sua busca? '))
driver.find_element_by_xpath('//*[@id="nav-search"]/form/div[2]/div/input').click()
sleep(2)
for i in range(1,16):
    try:
        descricao = driver.find_element_by_xpath('//*[@id="search"]/div[1]/div[2]/div/span[3]/div[1]/div['+str(i)+']/div/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a/span').text
        valor = driver.find_element_by_xpath('//*[@id="search"]/div[1]/div[2]/div/span[3]/div[1]/div['+str(i)+']/div/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div/div/a/span[1]/span[2]/span[2]').text
        print(descricao)
        print(valor)
        e.writerow([descricao,valor])
        sleep(0.5)
    except:
        pass
