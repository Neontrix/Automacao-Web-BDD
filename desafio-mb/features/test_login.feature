Funcionalidade: Login Amazon
  Cenário: Informar senha incorreta
    Dado que estou na tela de login
    E informo email correto
    E clico no botão de continuar
    E informo senha incorreta
    Quando clico no botão para logar
    Então retorna mensagem de erro


  Cenário: Informar email inexistente
    Dado que retornei para tela de login
    E informo email inexistente
    Quando clico no botão continuar
    Então exibe mensagem de erro


  Cenário: Realizar login com sucesso
    Dado que estou na tela de login Amazon
    E informo credenciais válidas
    Quando clico no botão de login
    Então realiza login com sucesso