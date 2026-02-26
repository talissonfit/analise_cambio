import numpy as np
import yfinance as yf

print("Buscando dados reais no Yahoo Finance...\n")

# 1. Coleta de dados
ticker = yf.Ticker("BRL=X")
dados_api = ticker.history(period="1mo")

# 2. Pegando fechamentos
cotacoes_usd = dados_api['Close'].values[-30:]

# 3. Tamanho da amostra
dias_analisados = cotacoes_usd.shape[0]

# 4. Variação diária
variacao_diaria = (cotacoes_usd[1:] / cotacoes_usd[:-1]) - 1

# 5. Estatísticas básicas
media_cotacao = np.mean(cotacoes_usd)
max_cotacao   = np.max(cotacoes_usd)
min_cotacao   = np.min(cotacoes_usd)

# Volatilidade (desvio-padrão anualizado aproximado)
volatilidade = np.std(variacao_diaria) * 100

# 6. Dias em alta
dias_em_alta = np.sum(variacao_diaria > 0)

# 7. Resultados
print(f"--- RELATÓRIO DE CÂMBIO (Últimos {dias_analisados} dias) ---")
print(f"Cotação Máxima: R$ {max_cotacao:.2f}")
print(f"Cotação Mínima: R$ {min_cotacao:.2f}")
print(f"Cotação Média:  R$ {media_cotacao:.2f}")
print(f"Volatilidade do Período: {volatilidade:.2f}%")
print(f"Dias de Alta vs Dia Anterior: {dias_em_alta} dias")