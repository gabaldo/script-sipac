from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from getpass import getpass
from time import sleep
from tools import logo, login
import csv
from datetime import datetime
  


def adiciona_acautelamento(matricula, tombamento):
    print('Adicionando o tombamento {} para a matrícula {}...'.format(tombamento, matricula))
    browser.get('http://prf.gov.br/sipac/patrimonio/index.jsf')

    browser.find_element_by_xpath('//*[@id="j_id_jsp_1003570061_1:aberturaTermoAcautelamento"]').click()

    

    browser.find_element_by_xpath('//*[@id="cautelaForm:nomeServidor"]').send_keys(matricula)
    sleep(1)
    browser.find_element_by_xpath('//*[@id="cautelaForm:nomeServidor"]').send_keys(Keys.TAB)
    sleep(1)
    browser.find_element_by_xpath('//*[@id="cautelaForm:unidade"]').send_keys('10070603')
    sleep(1)
    browser.find_element_by_xpath('//*[@id="cautelaForm:unidade"]').send_keys(Keys.TAB)
    sleep(1)
    browser.find_element_by_xpath('//*[@id="cautelaForm:local"]').send_keys('TIC/PR')
    sleep(1)
    browser.find_element_by_xpath('//*[@id="cautelaForm:local"]').send_keys(Keys.TAB)
    sleep(1)
    browser.find_element_by_xpath('//*[@id="cautelaForm:continuaCadastro"]').click()
    sleep(1)
    
    try:
        browser.find_element_by_xpath('//*[@id="cautelaForm:byTombamento"]').click()
        browser.find_element_by_xpath('//*[@id="cautelaForm:numTombamento"]').send_keys(tombamento)
        sleep(1)
        browser.find_element_by_xpath('//*[@id="cautelaForm:buscarBem"]').click()
        browser.find_element_by_xpath('//*[@id="cautelaForm:inserir"]/img').click()
        browser.find_element_by_xpath('//*[@id="cautelaForm:confirmarCautela1"]').click()
        browser.find_element_by_xpath('//*[@id="confirmaCautelaForm"]/table/tfoot/tr/td/input[1]').click()
    except:
        data_e_hora = datetime.now()
        descritivo = '{} - Anteção, o(a) servidor(a) de matrícula {} já possui um termo de acautelamento!\n'.format(data_e_hora, matricula)
        print(descritivo)
        f.write(descritivo)
    try:
        get_acautelamento = browser.find_element_by_xpath('//*[@id="confirmaCautelaForm"]/table/caption/b').text
        output_writer.writerow([matricula, tombamento, get_acautelamento])
        data_e_hora = datetime.now()
        descritivo = '{} - Termo de acautelamento {} adicionado para o(a) servidor(a) de matrícula {}!\n'.format(data_e_hora, get_acautelamento, matricula)
        print(descritivo)
        f.write(descritivo)
    except:
        print("O acautelamento não foi adicionado! Verificando o próximo registro...")
    
   

if __name__ == "__main__":
    

    input_file = open('dados_entrada.csv')
    file_reader = csv.reader(input_file)
    file_data = list(file_reader)

    output_file = open('dados_saida.csv', 'w', newline='')
    output_writer = csv.writer(output_file)

    f = open("log.txt", "a")
    
        
    logo()
    login()
        
        
    cpf = input("CPF: ")
    password = getpass()

    print('\nEfetuando conexão...')
    browser = Chrome()

    try:        
        url = 'http://prf.gov.br/sipac'
        browser.get(url)
        sleep(1)

        print('Entrando com os dados do login...\n')
        browser.find_element_by_xpath('//*[@id="conteudo"]/div[2]/form/div[1]/div[1]/input').send_keys(cpf)
        browser.find_element_by_xpath('//*[@id="conteudo"]/div[2]/form/div[2]/div/input').send_keys(password)
        browser.find_element_by_xpath('//*[@id="conteudo"]/div[2]/form/input[3]').click()
    
    except:
        print("Sem conexão com o SIPAC")
    
    for matricula, tombamento in file_data:
        adiciona_acautelamento(matricula, tombamento)
        
        
    f.close()

    print('\nFim do script!')