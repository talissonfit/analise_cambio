import numpy as np
import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt

print("Buscando dados no Yahoo Finance e gerando visualização...\n")

# 1. COLETA DE DADOS: Deixamos o yfinance gerenciar a sessão sozinho agora
try:
    ticker = yf.Ticker("BRL=X")
    dados_api = ticker.history(period="1mo")

    if dados_api.empty:
        print("Erro: Não foi possível obter dados. O Yahoo Finance pode estar instável.")
    else:
        # 2. PROCESSAMENTO COM NUMPY
        cotacoes_usd = dados_api['Close'].values[-30:]
        
        # Cálculos Estatísticos
        variacao_diaria = (cotacoes_usd[1:] / cotacoes_usd[:-1]) - 1
        media = np.mean(cotacoes_usd)
        volatilidade = np.std(variacao_diaria) * 100
        
        # 3. RELATÓRIO NO TERMINAL
        print(f"--- RELATÓRIO DE CÂMBIO ---")
        print(f"Cotação Média: R$ {media:.2f}")
        print(f"Volatilidade: {volatilidade:.2f}%")

        # 4. VISUALIZAÇÃO COM SEABORN
        sns.set_theme(style="whitegrid")
        plt.figure(figsize=(12, 6))
        
        # Criando o gráfico
        sns.lineplot(x=dados_api.index[-30:], y=cotacoes_usd, marker='o', color='#2ecc71', linewidth=2.5)
        
        plt.title(f"Variação USD/BRL - Últimos 30 dias\n(Volatilidade: {volatilidade:.2f}%)", fontsize=14)
        plt.xlabel("Data")
        plt.ylabel("Preço (R$)")
        
        # Salva a imagem para o seu Portfólio no GitHub
        plt.savefig("variacao_cambio.png")
        print("\n✅ Sucesso! O gráfico 'variacao_cambio.png' foi salvo na pasta.")
        plt.show()

except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")