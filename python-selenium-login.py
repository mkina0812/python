# Para interagir com o navegador
from selenium import webdriver
# Para configurar opções do Chrome
from selenium.webdriver.chrome.options import Options
# Para localizar elementos no DOM
from selenium.webdriver.common.by import By
# Para esperar por elementos específicos
from selenium.webdriver.support.ui import WebDriverWait
# Para condições esperadas
from selenium.webdriver.support import expected_conditions as EC
# Para simular pressionamento de teclas  
from selenium.webdriver.common.keys import Keys  

# Configurar Selenium

# Cria um objeto para configurar as opções do navegador Chrome.
chrome_options = Options()

# Desativa o uso da GPU (placa gráfica) para renderizar páginas. 
# Pode melhorar a compatibilidade em máquinas sem GPU ou quando há problemas de renderização.
chrome_options.add_argument('--disable-gpu')

# Executa o navegador sem o modo sandbox (isolamento), necessário em alguns sistemas para 
# evitar erros de permissão.
chrome_options.add_argument('--no-sandbox')

# Inicializa o driver do Chrome com as opções configuradas.
driver = webdriver.Chrome(options=chrome_options)

# Configura uma espera implícita de 5 segundos. Isso significa que o Selenium 
# tentará encontrar os elementos necessários antes de gerar um erro, aguardando até 5 segundos.
driver.implicitly_wait(5)

# Abre a URL especificada no navegador controlado pelo Selenium.
driver.get("https://www.sigeo.fazenda.sp.gov.br/analytics/saw.dll?Dashboard")

# Efetuar login na página

# Cria um objeto de espera explícita com timeout de 20 segundos. 
# É usado para aguardar até que condições específicas sejam satisfeitas.
wait = WebDriverWait(driver, 20)

# Aguarda até que o elemento com o ID id-elemento-login (campo de login) esteja presente no DOM.
campo_login = wait.until(EC.presence_of_element_located((By.ID, "id-elemento-login")))

# Aguarda até que o elemento com o ID id-elemento-senha (campo de senha) esteja presente no DOM.
campo_senha = wait.until(EC.presence_of_element_located((By.ID, "id-elemento-senha")))

# Aguarda até que o botão de login, identificado pelo ID id-elemento-logon, esteja presente no DOM.
acessar = wait.until(EC.presence_of_element_located((By.ID, "id-elemento-logon")))

# Insere o texto "login" no campo de entrada identificado como o campo de nome de usuário.
campo_login.send_keys("login")

# Insere o texto "senha" no campo de entrada identificado como o campo de senha.
campo_senha.send_keys("senha")

# Simula o pressionamento da tecla Enter/Return no botão de login, 
# iniciando o envio das credenciais para autenticação.
acessar.send_keys(Keys.RETURN)

time.sleep(2)

exit()