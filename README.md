📈 Analisador de Funções de Cálculo

Este é um projeto de Python para a matéria de Cálculo Diferencial e Integral I, focado em analisar funções de uma variável. O script utiliza SymPy para computação simbólica (derivadas e solução de equações) e Matplotlib para gerar uma visualização gráfica da função e seus pontos notáveis.

🚀 Funcionalidades

    Derivadas Automáticas: Calcula a primeira (f′(x)) e a segunda (f′′(x)) derivada da função inserida.

    Pontos Críticos: Encontra e classifica os pontos críticos como:

        Mínimo Local (usando o Teste da Segunda Derivada f′′(x)>0)

        Máximo Local (usando o Teste da Segunda Derivada f′′(x)<0)

        Indeterminado (quando f′′(x)=0)

    Pontos de Inflexão: Identifica candidatos a pontos de inflexão (onde f′′(x)=0) e confirma a inflexão ao verificar a mudança de sinal da concavidade ao redor do ponto.

    Plotagem Inteligente: Gera um gráfico da função com matplotlib, marcando e legendando todos os pontos críticos e de inflexão encontrados.

    Interface de Console: Permite ao usuário inserir qualquer função em formato de string.

📊 Exemplo de Resultado

(Recomendação: rode o script com a função x**3 - 6*x**2 + 9*x + 1, tire um screenshot do gráfico e salve no seu repositório como demo.png. Depois, substitua a linha abaixo)

![Demo Screenshot](demo.png)

🛠️ Tecnologias e Bibliotecas

    SymPy: A biblioteca principal para toda a computação algébrica simbólica, permitindo calcular derivadas e resolver equações de forma programática.

    Matplotlib: Usada para criar a visualização gráfica da função e dos pontos analisados.

    NumPy: Utilizada para gerar os intervalos numéricos (linspace) para a plotagem e para lidar com operações matemáticas em arrays.

📁 Estrutura do Projeto

O código é modularizado em dois arquivos principais para uma melhor organização:

    algoritmo_pontoscriticos.py

        O "motor" de análise do projeto.

        Contém a função analisar_funcao(func_texto), que recebe a string da função e realiza toda a análise simbólica (cálculo de derivadas, solução de equações e classificação dos pontos).

        Retorna os objetos simbólicos e uma lista de resultados em texto.

    main.py (ou graficos.py)

        O script "frontend" que o usuário executa.

        Importa a função de análise do algoritmo_pontoscriticos.py.

        Pede a função ao usuário via input().

        Chama a função de análise e recebe os resultados.

        Utiliza matplotlib e numpy para traduzir os dados simbólicos em um gráfico visual, plotando a curva e marcando os pontos com cores e legendas apropriadas.

🔧 Como Usar

1. Pré-requisitos

Você precisará do Python 3 e das bibliotecas listadas.

2. Instalação

    Clone este repositório:
    Bash

git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio

Instale as dependências:
Bash

pip install sympy matplotlib numpy

3. Execução

Rode o script principal (que contém o código de plotagem):
Bash

python main.py

4. Inserindo uma Função

Você será solicitado a digitar a função. Use a sintaxe do Python:

    ** para potências (ex: x**2 para x2)

    * para multiplicação (ex: 3*x para 3x)

    / para divisão (ex: 1/x)

    Funções como sp.sin(x), sp.cos(x), sp.exp(x) também são suportadas (desde que o sp esteja no contexto, ou simplificando sin(x) etc.).

Exemplos de entrada:

x**3 - 3*x + 2
4*x**3 + 3*x**2 - 6*x
(x-1)**3
1/(x**2 - 1)

🧠 Como Funciona a Análise

O processo de análise no algoritmo_pontoscriticos.py é o coração do projeto:

    Análise de Pontos Críticos (f′(x)=0):

        O script calcula a primeira derivada f′(x).

        Resolve f′(x)=0 para encontrar os pontos críticos p.

        Para cada p, ele aplica o Teste da Segunda Derivada:

            Se f′′(p)>0, é um mínimo local.

            Se f′′(p)<0, é um máximo local.

            Se f′′(p)=0, o teste é inconclusivo (e o script reporta isso).

    Análise de Pontos de Inflexão (f′′(x)=0):

        O script calcula a segunda derivada f′′(x) e resolve f′′(x)=0 para encontrar os candidatos a pontos de inflexão, i.

        Para confirmar a inflexão, o script realiza um Teste de Vizinhança (neighborhood test). Ele verifica se o sinal de f′′(x) muda em uma pequena vizinhança ao redor de i.

        Ele avalia f′′(i−ϵ) e f′′(i+ϵ) (onde ϵ é um valor pequeno). Se os sinais forem opostos (resultado_antes * resultado_depois < 0), a mudança de concavidade é confirmada, e o ponto é reportado como um ponto de inflexão.

