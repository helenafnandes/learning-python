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

    # Encontre todos os divs que possuem o atributo 'data-grid-item="true"'
    elements_with_data_grid_item = soup.find_all(
        attrs={"data-grid-item": "true"})

    # Filtrar apenas os divs que também possuem a classe 'Yl- MIw Hb7'
    pins_divs = [
        element for element in elements_with_data_grid_item if "Yl- MIw Hb7" in element.get("class", [])]

    # Verifique se foram encontrados divs antes de prosseguir
    if pins_divs:
        # Faça algo com cada div do pin encontrado
        for div in pins_divs:
            # Por exemplo, você pode imprimir o conteúdo do div
            print(div.text)
    else:
        print("Nenhum div do pin encontrado.")


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
    driver.implicitly_wait(10)


# Obtém o HTML após o carregamento completo da página
html = driver.page_source
if html:
    print("aaaaaaaa")


# continuar = input("continue: ")


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


# Fecha o navegador
driver.quit()
