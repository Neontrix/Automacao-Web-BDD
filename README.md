# Automacao-Web-BDD
Automação web utilizando BDD (behave), Python como linguagem, Selenium e Allure como gerador de report.


Foi utilizado o site da Amazon de exemplo. Com as funcionalidades de Login, Pesquisa de produtos e Adição no carrinho bem como seus cenários de testes.
Foi removido as credenciais de email e senha utilizadas em teste.

O intuito desse projeto foi aplicar conhecimentos adquiridos a um desafio para evolução de conhecimento e aprendizagem. Não foi utilizado padrão Page-Objects nem Pytest na biblioteca.


Alguns comandos utilizados:
**Comandos para executar cenários sem gerar relatórios:**
behave

**Comandos para executar cenários e gerar relatórios no final:**
behave -f allure_behave.formatter:AllureFormatter -o output ./features

**Comandos para executar relatórios existentes:**
allure serve output
