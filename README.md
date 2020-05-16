# desafios
Desafios propostos afim de aprendizado.

Estrutura para os desafios

Configurações utilizadas:

	Sistema Operacional: Windows 10
	Editor: Atom (https://atom.io/)
	Terminal utilizado no Atom (platformio-ide-terminal)
	Liguagem utilizada: Python 3 (https://www.python.org/downloads/)
	Ferramenta para automação: Selenium/Selenium webdriver
	Navegador utilizado: Firefox, no caso precisa ter o GeckoDriver instalado na máquina




1. Criar a pasta do Projeto
2. Navegar para dentro da pasta criada (Projeto)
3. Criar um ambiente virtual (para rodar o selenium isolado da máquina) - Virtual Env (venv)

	- código para criar o ambiente
	  python -m venv venv

	Obs: A criação desse ambiente virtual pode ser realizado de duas formas:
	1 - Pelo terminal do windows (cmd, no modo administrador)

	2 - Pelo próprio terminal do Atom (este precisa configurar o terminal do Atom para que abra sempre com o cmd e não o powershell)

	Passos para configurar o CMD de modo que sempre execute no modo administrador:
	1 - Digitar no menu iniciar do windows "cmd"
	2 - Clicar na opção "abrir local do arquivo"
	3 - Clicar com botão direito sobre o icone do CMD/Prompt de Comando
	4 - Selecionar a opção "Propriedades"
	5 - Clicar na opção "Avançadas"
	6 - Marcar o check na opção "Executar como administrador"

	Estes passos irão garantir que sempre que o CMD for iniciado, será sempre como modo administrador.


4. Ativar o ambiente virtual para poder instalar o selenium

	- código
	  venv\Scripts\activate.bat
	  (Para desativar o ambiente virtual: venv\Scripts\deactivate)

5. Com ambiente virutal ativado, instalar o Selenium

	- código
	  pip install selenium

6. Para executar um teste, lembrando que ainda está dentro da venv ativada, basta digitar python nome_do_arquivoTeste.py
