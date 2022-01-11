# Script de acautelamento de bens no SIPAC (Setic-PR)

## Dependências para execução

### Instalação do driver do navegador de acordo com a versão
https://chromedriver.chromium.org/downloads

### Instalando o chromedriver no Linux
```
sudo mv -f chromedriver /usr/local/share/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver
```

### Criando ambiente virtual para desenvolvimento
```
python -m venv venv
source venv/bin/activate
```

### Instalação do Selenium
```
# pip install -r requirements.txt
```

## Execução do script
```
# python sipac.py
```
