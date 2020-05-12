from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Firefox
from pprint import pprint
from time import sleep

# Instanciando o navegador e acessando a url do site da trivago
browser = Firefox()
browser.get('http://www.trivago.com.br')

#Preenchendo o campo de Cidades/Destinos com texto 'Natal'
sleep(2)
cidade = browser.find_element_by_id("querytext")
cidade.click()
cidade.send_keys("Natal")

#Clicando no botão Pesquisar
sleep(2)
browser.find_element_by_css_selector("button.btn:nth-child(5)")
click_Pesq = browser.find_element_by_css_selector("button.btn:nth-child(5)")
click_Pesq.click()

#Selecionando a opção "Quarto Individual"
sleep(2)
quarto = browser.find_element_by_css_selector("button.dealform-button:nth-child(4)")
quarto.click()
sleep(2)
quarto_individual = browser.find_element_by_css_selector("li.roomtype-item:nth-child(1) > button:nth-child(1) > div:nth-child(1)")
quarto_individual.click()

#Selecionando a opção "Somente por distância"
sleep(2)
ordenar = browser.find_element_by_id("mf-select-sortby")
ordenar.click()
sleep(2)
ordernar_Dist = browser.find_element_by_css_selector("#mf-select-sortby > option:nth-child(7)")
ordernar_Dist.click()

#Buscando informações do Hotel
sleep(3)
section_ID = browser.find_element_by_id("3166102")
h3 = section_ID.find_elements_by_class_name('m-0')

#Pegando número de estrelas/avaliação
sleep(3)
item_B = section_ID.find_elements_by_tag_name('button')
item_3 = item_B[3].text
conv = str(item_3)

#Pegando o preço do quarto/hotel
sleep(3)
n_Preco = browser.find_elements_by_tag_name('strong')
nome_P = n_Preco[10].text


#Pegando o nome do site/Empresa que esstá ofertando
sleep(3)
n_Site = browser.find_element_by_xpath("//li[@id='3166102']/article/div/div[2]/div/div/h3/span")


#Procedimentos para chegar até as informações de Comodidades
sleep(2)
click_hotel = browser.find_element_by_xpath("//li[@id='3166102']/article/div/div[2]/div/div/div")
click_hotel.click()
sleep(0.5)
info = browser.find_element_by_xpath("//div[@id='js_slideout_3166102']/div/div/ul/li[2]/button")
info.click()
sleep(3)
comodidades = browser.find_element_by_css_selector("button.link")
comodidades.click()

# Buscando cada comodidade listada e atribuindo a uma variável
sleep(3)
info_c = browser.find_elements_by_tag_name('ul')
info_comodidades = info_c[6].find_elements_by_tag_name('li')


#Imprimindo na tela as informações do Hotel/Quarto
print(f'Informações do Hotel desejado:')
print(f'Nome do hotel: {h3[1].text} e Estrelas: {conv[0:3]}')
print(f'Orfeta da empresa: {n_Site.text} Preço: {nome_P}')

for imprimir in range(len(info_comodidades)):
    print(f'Comodidades: {info_comodidades[imprimir].text}')

browser.quit()
