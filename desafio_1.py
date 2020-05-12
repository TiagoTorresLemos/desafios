from selenium.webdriver import Firefox
from time import sleep




#Função para buscar elementos necessários no site (texto)
def find_by_text(browser, tag, text):
    elementos = browser.find_elements_by_tag_name(tag)
    for elemento in elementos:
        if elemento.text == text:
            return elemento

#Instanciando o navegador e acessando a url do discourse
browser = Firefox()
browser.get('https://www.discourse.org/')

#Buscando o elemento da opção Demo e realizando o click na opção
elemento_demo = find_by_text(browser, 'li', 'Demo')
find_by_text(browser, 'li', 'Demo').click()

#Mudando o foco da aba no navegador para a aba atual (que está visível em tela).
sleep(5)
browser.switch_to.window(browser.window_handles[1])

#Procedimento para realizar o Scroll na pagina
altura = browser.execute_script("return document.body.scrollHeight")

while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(3)
    nova_altura = browser.execute_script("return document.body.scrollHeight")
    if nova_altura == altura:
        break
    altura = nova_altura



#Pegando os tópicos bloqueados e imprimindo os títulos.
texto_block1 = browser.find_element_by_xpath("//a[contains(text(),'Totally amped about the 80s')]")
texto_block2 = browser.find_element_by_xpath("//a[contains(text(),'Do microwave ovens kill bacteria?')]")
print(f'Textos dos tópicos bloqueados: {texto_block1.text}, {texto_block2.text}')

#Realizando click no item Categoria
find_by_text(browser, 'a', 'Categories').click()

#Buscando as categorias e quantidade de itens e imprimindo-os
sleep(3)
categoria = browser.find_elements_by_class_name("category-name")
valor = browser.find_elements_by_class_name("value")
for categorias in range(12):
    print(f'Nome da Categoria: {categoria[categorias].text}')
    print(f'Quantidade de itens: {valor[categorias].text}\n')

#Retornando para "parte inicial"
find_by_text(browser, 'a', 'Latest').click()

#Buscando o tópico que tem maior numero de views e imprimindo nome do tópico
sleep(3)
maior_visualizado = find_by_text(browser, 'a', 'What’s your all-time favorite movie scene?')
print(f'Topico com maior numero de views: {maior_visualizado.text}')

browser.quit()
