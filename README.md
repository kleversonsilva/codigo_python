# Código Fonte Do Trabalho de Conclusão de Curso.
# Detector de Aflatoxinas Pelo Metodo da Fluorescencia Amarelo-esverdeada Brrilhante
https://drive.google.com/file/d/12M2EeZcP0-c5xQUxbmIdcsQOEK25pBKh/view?usp=sharing


[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)](https://opencv.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.x-purple.svg)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.x-orange.svg)](https://matplotlib.org/)

Este projeto em Python utiliza a biblioteca OpenCV (cv2) para capturar e processar imagens da webcam em tempo real, oferecendo funcionalidades interativas de análise de cores RGB. Adicionalmente, emprega as bibliotecas NumPy para operações numéricas e Matplotlib para a geração de histogramas, além dos módulos `os` e `datetime` para manipulação de arquivos e obtenção de timestamps.

## Funcionalidades Principais

Este programa permite utilizar a webcam para capturar imagens e realizar análises de cores em tempo real, com as seguintes funcionalidades:

* **Captura de Vídeo em Tempo Real:** Inicialização da webcam para obter um fluxo contínuo de frames de vídeo.
* **Criação Automática de Pasta:** Criação automática da pasta `capturas_rgb` no diretório de execução para armazenar as imagens capturadas.
* **Visualização do Feed da Webcam:** Exibição do vídeo da webcam em uma janela, proporcionando ao usuário uma visualização em tempo real do que está sendo capturado.
* **Captura Seletiva e Análise ao Pressionar 'c':** Ao pressionar a tecla `c`, o programa executa as seguintes análises e ações na imagem atual:
    * **Filtragem de Cores RGB Puras:** Criação de uma máscara da imagem, mantendo apenas os pixels com cores próximas ao vermelho, verde ou azul puros, dentro de uma tolerância configurável.
    * **Salvamento da Imagem Filtrada:** A imagem contendo apenas as cores RGB puras é salva na pasta `capturas_rgb` com um nome de arquivo único baseado na data e hora da captura.
    * **Cálculo do Histograma RGB:** Cálculo da distribuição de intensidade dos canais vermelho, verde e azul da imagem original capturada.
    * **Análise de Cor Alvo:** Estimativa do percentual de pixels na imagem original que correspondem a uma cor alvo específica (definida como verde limão por padrão), considerando uma tolerância configurável.
    * **Saída de Dados no Console:** Exibição do percentual da cor alvo detectado no console.
    * **Visualização do Histograma:** Plotagem dos histogramas RGB da imagem original utilizando Matplotlib, permitindo uma análise visual da distribuição das cores.
* **Encerramento do Programa:** Permite ao usuário fechar a janela da webcam e encerrar a execução do programa pressionando a tecla `s`.

## Como Usar

1.  **Pré-requisitos:** Certifique-se de ter o Python 3.x instalado e as seguintes bibliotecas instaladas no seu ambiente:
    ```bash
    pip install opencv-python numpy matplotlib
    ```
2.  **Execução:** Clone este repositório (se estiver publicando o código completo) ou salve o código Python em um arquivo (por exemplo, `analise_rgb.py`). Execute o script a partir do seu terminal:
    ```bash
    python analise_rgb.py
    ```
3.  **Interação:**
    * Uma janela com o feed da sua webcam será aberta.
    * Pressione a tecla `c` para capturar o frame atual, gerar a imagem com cores RGB puras, calcular o histograma da imagem original, analisar o percentual da cor alvo e exibir o histograma. A imagem filtrada será salva na pasta `capturas_rgb`.
    * Pressione a tecla `s` para fechar a janela da webcam e encerrar o programa.

## Notas

* A tolerância para a filtragem de cores RGB puras e para a análise da cor alvo podem ser ajustadas diretamente no código, nas respectivas funções `criar_mascara_rgb_puras` e `analisar_cor_rgb`.
* A cor alvo padrão para a análise é verde limão `(173, 255, 47)`, mas pode ser facilmente modificada na função `analisar_cor_rgb`.

