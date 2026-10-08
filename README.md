🖥️ PC Monitoring

Dashboard web para monitoramento de computadores em tempo real, desenvolvido com Python, Streamlit, SQLite e Plotly.

O projeto coleta e armazena informações de utilização de CPU, memória RAM e temperatura do processador, permitindo visualizar os dados em um painel interativo com gráficos e histórico de leituras.

🚧 Status: projeto em desenvolvimento
📊 Funcionalidades
📈 Monitoramento de uso da CPU
💾 Monitoramento do uso de memória RAM
🌡️ Monitoramento da temperatura da CPU
🖥️ Suporte a múltiplos computadores
🔄 Atualização automática do dashboard
📉 Gráficos históricos com Plotly
🔎 Filtro por computador
📋 Visualização dos registros em tabela
💽 Persistência dos dados utilizando SQLite
⚡ Banco configurado com WAL para melhorar a concorrência entre leitura e escrita
🖼️ Dashboard

O painel apresenta as informações mais recentes de cada computador monitorado e gráficos históricos para acompanhar a evolução dos indicadores ao longo do tempo.

Entre os dados exibidos estão:

Métrica	Descrição
🧠 CPU	Percentual de utilização do processador
💾 RAM	Percentual de memória utilizada
🌡️ Temperatura	Temperatura atual do processador
🖥️ PC	Identificação do computador monitorado
🕐 Timestamp	Data e hora da leitura
🏗️ Arquitetura

O projeto possui uma arquitetura simples, dividida principalmente em duas partes:

┌─────────────────────┐
│     simulator.py    │
│                     │
│ Gera leituras dos   │
│ computadores        │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│       pcs.db        │
│                     │
│ SQLite              │
│ leituras_pcs        │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│       app.py        │
│                     │
│ Streamlit           │
│ + Pandas             │
│ + Plotly             │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│     Dashboard       │
│                     │
│ Gráficos + métricas │
└─────────────────────┘

Componentes
simulator.py

Responsável por simular computadores e inserir periodicamente novas leituras no banco SQLite.

Atualmente são simulados três computadores:

Pc_1
Pc_2
Pc_3

A cada ciclo são gerados valores de:

Uso de CPU
Uso de RAM
Temperatura da CPU

As leituras são inseridas no banco a cada 2 segundos. 
G
GitHub

app.py

Responsável pelo dashboard desenvolvido com Streamlit.

O aplicativo:

Consulta o banco SQLite;
Carrega as últimas leituras;
Permite selecionar o computador;
Exibe os valores mais recentes;
Gera gráficos históricos;
Mostra uma tabela com os registros;
Atualiza automaticamente o painel.

A frequência de atualização e a quantidade de registros exibidos podem ser configuradas pela barra lateral. 
G
GitHub

pcs.db

Banco de dados SQLite utilizado para armazenar as leituras.

A tabela principal é:

CREATE TABLE leituras_pcs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME,
    pc_id TEXT,
    uso_cpu REAL,
    uso_ram REAL,
    temp_cpu REAL
);

🛠️ Tecnologias utilizadas
Python 3
Streamlit — interface web
SQLite — armazenamento dos dados
Pandas — manipulação dos dados
Plotly Express — gráficos interativos

O app.py utiliza diretamente sqlite3, pandas, streamlit e plotly.express. 
G
GitHub

📁 Estrutura do projeto
pc_monitoring/
│
├── app.py
├── simulator.py
├── pcs.db
├── .gitignore
└── README.md

Descrição dos arquivos
Arquivo	Função
app.py	Dashboard de monitoramento
simulator.py	Simulador de computadores e geração de dados
pcs.db	Banco de dados SQLite
.gitignore	Arquivos ignorados pelo Git
README.md	Documentação do projeto
🚀 Como executar
1. Clone o repositório
git clone https://github.com/Debeterco/pc_monitoring.git
cd pc_monitoring

2. Crie um ambiente virtual

Recomendado para manter as dependências isoladas:

python -m venv .venv

3. Ative o ambiente virtual
Windows
.venv\Scripts\activate

Linux / macOS
source .venv/bin/activate

4. Instale as dependências
pip install streamlit pandas plotly

▶️ Executando o projeto

O projeto possui dois processos principais: o simulador, que gera os dados, e o dashboard, que os apresenta.

Terminal 1 — iniciar o simulador
python simulator.py


Você deverá receber uma mensagem semelhante a:

Simulador de pcs em execução. Pressione Ctrl + C para parar


O simulador criará o banco pcs.db, caso ele ainda não exista, e começará a inserir novas leituras. 
G
GitHub

Terminal 2 — iniciar o dashboard
streamlit run app.py


O Streamlit iniciará o servidor local e fornecerá o endereço para acessar o dashboard pelo navegador.

🎛️ Controles do dashboard

Na barra lateral é possível configurar:

Frequência de atualização

Define o intervalo, em segundos, entre as atualizações do dashboard.

Valores disponíveis:

1 — 10 segundos


O valor padrão é:

2 segundos

Histórico de leituras

Define quantos registros serão carregados do banco.

Valores disponíveis:

30 — 300 registros


O valor padrão é:

120 registros

Filtro por computador

É possível selecionar:

Todos
Pc_1
Pc_2
Pc_3


ou outros computadores adicionados ao simulador. 
G
GitHub

📈 Visualizações

O dashboard apresenta atualmente dois gráficos principais.

Temperatura da CPU

Exibe a temperatura dos computadores ao longo do tempo:

Temperatura (°C)
       │
   70 ─┤          ╭─╮
   60 ─┤    ╭─────╯ ╰──
   50 ─┤────╯
       └──────────────────
          Horário

Uso da CPU

Exibe o percentual de utilização da CPU ao longo do tempo:

Uso da CPU (%)
       │
  100 ─┤
   75 ─┤       ╭──╮
   50 ─┤───────╯  ╰──
   25 ─┤  ╭──╮
    0 ─┴────────────────
          Horário


Além dos gráficos, é possível expandir a tabela para visualizar os registros individuais. 
G
GitHub

🧪 Simulação

O projeto atualmente utiliza dados simulados para representar os computadores monitorados.

Os valores iniciais são diferentes para cada PC e pequenas variações aleatórias são aplicadas a cada nova leitura.

Exemplo:

pcs = {
    "Pc_1": {
        "uso_cpu": 24.0,
        "uso_ram": 55.0,
        "temp_cpu": 60.2
    },
    "Pc_2": {
        "uso_cpu": 28.5,
        "uso_ram": 48.0,
        "temp_cpu": 50.8
    },
    "Pc_3": {
        "uso_cpu": 54.0,
        "uso_ram": 62.0,
        "temp_cpu": 53.1
    }
}


Esses valores são alterados gradualmente para criar uma simulação de monitoramento contínuo. 
G
GitHub

🗄️ Banco de dados

O SQLite foi escolhido por ser simples e não exigir um servidor de banco separado.

As leituras são armazenadas na tabela:

leituras_pcs


Cada registro contém:

id
timestamp
pc_id
uso_cpu
uso_ram
temp_cpu


O banco utiliza o modo WAL (Write-Ahead Logging), permitindo uma melhor convivência entre as operações de leitura realizadas pelo dashboard e as escritas realizadas pelo simulador. 
G
GitHub

🔮 Próximos passos

Algumas evoluções possíveis para o projeto:

Substituir o simulador por coleta real de hardware
Monitoramento de CPU em máquinas reais
Monitoramento real de memória RAM
Monitoramento de temperatura da CPU
Monitoramento de GPU
Monitoramento de discos
Monitoramento de rede
Cadastro automático dos computadores
Identificação por hostname/IP
Sistema de agentes para computadores remotos
API para envio das métricas
Alertas para temperaturas ou utilização elevadas
Histórico por períodos configuráveis
Exportação dos dados para CSV
Autenticação de usuários
Dashboard com indicadores de saúde do computador
Dockerização da aplicação
Testes automatizados
🤝 Contribuindo

Contribuições são bem-vindas!

Para contribuir:

Faça um fork do projeto.
Crie uma branch para sua alteração:
git checkout -b feature/minha-feature

Faça suas alterações.
Commit:
git commit -m "feat: adiciona minha feature"

Envie a branch:
git push origin feature/minha-feature

Abra um Pull Request.
📄 Licença

Este projeto ainda não possui uma licença definida no repositório.

Caso o projeto seja disponibilizado como software open source, recomenda-se adicionar um arquivo LICENSE definindo explicitamente os termos de uso, modificação e distribuição.

👤 Autor

Desenvolvido por Debeterco.

GitHub: Debeterco
Projeto: pc_monitoring
⭐ Apoie o projeto

Se este projeto foi útil para você, considere deixar uma ⭐ no repositório!

PC Monitoring — monitoramento simples, visual e em tempo real de computadores.
