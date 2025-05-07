
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
from datetime import datetime

def calcular_histograma_rgb(imagem):
    """Aqui Calcula o histograma RGB da imagem."""
    canais = cv2.split(imagem)
    histograma_r = cv2.calcHist([canais[0]], [0], None, [256], [0, 256])
    histograma_g = cv2.calcHist([canais[1]], [0], None, [256], [0, 256])
    histograma_b = cv2.calcHist([canais[2]], [0], None, [256], [0, 256])
    return histograma_r, histograma_g, histograma_b

def analisar_cor_rgb(imagem, cor_alvo=(173, 255, 47), tolerancia=30):
    """
    Analisa a imagem para estimar o percentual da cor alvo.
    Args:
        imagem (numpy.ndarray): A imagem no formato BGR.
        cor_alvo (tuple): A cor é RGB alvo para análise.
        tolerancia (int): A tolerância para considerar uma cor como mais próxima da cor alvo.
    Returns:
        float: O percentual aproximado da cor alvo na imagem.
    """
    altura, largura, canais = imagem.shape
    total_pixels = altura * largura
    pixels_cor_alvo = 0

    for y in range(altura):
        for x in range(largura):
            cor_pixel = imagem[y, x]  # Cor do pixel no formato BGR
            distancia = distancia_cores(cor_pixel, cor_alvo[::-1]) # Inverte cor_alvo para BGR
            if distancia <= tolerancia:
                pixels_cor_alvo += 1

    if total_pixels > 0:
        percentual_cor_alvo = (pixels_cor_alvo / total_pixels) * 100
    else:
        percentual_cor_alvo = 0

    return percentual_cor_alvo

def distancia_cores(cor1, cor2):
    """Calcular a distância Euclidiana entre duas cores RGB."""
    cor1 = np.array(cor1, dtype=np.int32)
    cor2 = np.array(cor2, dtype=np.int32)
    return np.sqrt(np.sum((cor1 - cor2)**2))

def criar_mascara_rgb_puras(imagem, tolerancia_rgb=50):
    """Cria uma máscara onde apenas cores próximas ao vermelho, verde ou azul."""
    altura, largura, _ = imagem.shape
    mascara = np.zeros((altura, largura, 3), dtype=np.uint8)

    for y in range(altura):
        for x in range(largura):
            b, g, r = imagem[y, x]

            # Cores puras (com uma certa tolerância)
            vermelho_puro = (0, 0, 255)
            verde_puro = (0, 255, 0)
            azul_puro = (255, 0, 0)

            if (distancia_cores((b, g, r), vermelho_puro) <= tolerancia_rgb or
                    distancia_cores((b, g, r), verde_puro) <= tolerancia_rgb or
                    distancia_cores((b, g, r), azul_puro) <= tolerancia_rgb):
                mascara[y, x] = (b, g, r)  # Mantém a cor original na máscara

    return mascara

# Aqui Inicializa a captura de vídeo da webcam
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Erro ao abrir a webcam.")
    exit()

# Aqui Define a pasta para salvar as imagens capturadas
pasta_capturas = "capturas_rgb"
if not os.path.exists(pasta_capturas):
    os.makedirs(pasta_capturas)

while True:
    # Capturar um frame da webcam
    ret, frame = camera.read()

    # Se a captura foi bem-sucedida
    if ret:
        # Exibir o frame da webcam
        cv2.imshow("Webcam Feed (Pressione 'c' para capturar RGB, 's' para sair)", frame)

        # Espera por uma tecla
        key = cv2.waitKey(1) & 0xFF

        # Se a tecla 'c' for pressionada, captura a imagem
        if key == ord('c'):
            agora = datetime.now().strftime("%Y%m%d_%H%M%S")
            nome_arquivo_rgb = os.path.join(pasta_capturas, f"captura_rgb_{agora}.jpg")
            # Cria a máscara com apenas as cores RGB
            imagem_rgb_puras = criar_mascara_rgb_puras(frame, tolerancia_rgb=50)
            cv2.imwrite(nome_arquivo_rgb, imagem_rgb_puras)
            print(f"Imagem com cores RGB capturada e salva como: {nome_arquivo_rgb}")
            # Realiza a análise da cor e histograma na imagem (colorida)
            histograma_r, histograma_g, histograma_b = calcular_histograma_rgb(frame)
            percentual_cor_alvo = analisar_cor_rgb(frame, cor_alvo=(173, 255, 47), tolerancia=30)
            print(f"Percentual aproximado da cor alvo na captura original: {percentual_cor_alvo:.2f}%")

            # Plota os histogramas RGB
            plt.figure(figsize=(10, 6))
            plt.plot(histograma_r, color='red', label='Vermelho')
            plt.plot(histograma_g, color='green', label='Verde')
            plt.plot(histograma_b, color='blue', label='Azul')
            plt.title('Histograma de Imagem')
            plt.xlabel('Intensidade')
            plt.ylabel('Frequência')
            plt.legend()
            plt.grid(True)
            plt.show()
        # Se a tecla 's' for pressionada, sair
        elif key == ord('s'):
            break
    else:
        print("Erro ao capturar o frame.")
        break
# Libera a câmera e fecha todas as abas
camera.release()
cv2.destroyAllWindows()
plt.close('all')