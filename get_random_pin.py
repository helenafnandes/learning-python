import requests
from bs4 import BeautifulSoup
import webbrowser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import random


def obter_pagina_pinterest(url):
    response = requests.get(url)

    if response.status_code == 200:
        return response.text
    else:
        print(f"Erro na requisição: {response.status_code}")
        return None


def selecionar_pin_aleatorio(html):
    soup = BeautifulSoup(html, 'html.parser')

    # Use find_all() para encontrar todos os elementos <a> dentro da div com data-test-id pinWrapper
    # links_pins = soup.select('[class="Yl- MIw Hb7"] a')

    # Use find() para encontrar o elemento <div> com data-test-id="pinWrapper"
    # div_pin_wrapper = soup.find('div', {'data-test-id': 'pinWrapper'})
    div_pin_wrapper = soup.find('div', {'class': 'Yl- MIw Hb7'})

    # Percorra os links encontrados para obter o atributo href de cada um
    # for link in links_pins:
    #     link_do_pin = link['href']
    #     print(link_do_pin)

    # pins = soup.find_all('div', {'class': 'Yl- MIw Hb7'})
    # if pins:
    #     pin_aleatorio = random.choice(pins)
    #     link_pin = pin_aleatorio.find('a')['href']
    #     return link_pin
    # else:
    #     return None

    if div_pin_wrapper:
        # Em seguida, use find_all() para encontrar todos os elementos <a> dentro do elemento <div> encontrado
        links_pins = div_pin_wrapper.find_all('a')
        for link in links_pins:
            link_do_pin = link['href']
            print(link_do_pin)
    else:
        print("Elemento com data-test-id='pinWrapper' não encontrado.")

    # if links_pins:
    #     link_aleatorio = random.choice(links_pins)
    #     return link_aleatorio
    # else:
    #     print("não achou.")
    #     return None


# Configuração do Chrome WebDriver
# options = webdriver.ChromeOptions()
# # Para executar em modo headless (sem abrir janela do navegador)
# options.add_argument("--headless")


# URL da página do Pinterest que contém os pins
url = "https://www.pinterest.com/phos13/stuff/"

# Abre a página no navegador
driver = webdriver.Chrome()
driver.get(url)

# Aguarda alguns segundos para o JavaScript carregar o conteúdo dinamicamente (ajuste conforme necessário)
driver.implicitly_wait(15)

# Execute um scroll para baixo usando JavaScript para carregar mais pins
# Você pode ajustar a quantidade de scroll conforme necessário
scroll_amount = 500  # Valor em pixels para rolar
for _ in range(5):  # Realiza o scroll 5 vezes
    driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
    # Aguarda um curto período para os pins carregarem após o scroll
    driver.implicitly_wait(2)


# Obtém o HTML após o carregamento completo da página
html = driver.page_source
if html:
    print("aaaaaaaa")

# Fecha o navegador
driver.quit()


url_pasta_pinterest = "https://www.pinterest.com/phos13/stuff/"
pagina_pasta = obter_pagina_pinterest(url_pasta_pinterest)  # html

if pagina_pasta:
    link_pin_aleatorio = selecionar_pin_aleatorio(pagina_pasta)
    if link_pin_aleatorio:
        url_pin_aleatorio = "https://www.pinterest.com" + link_pin_aleatorio
        webbrowser.open(url_pin_aleatorio)
    else:
        print("Nenhum pin encontrado na página.")
else:
    print("Erro ao obter página do Pinterest.")
