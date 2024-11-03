import pandas as pd
import matplotlib.pyplot as plt
import os

try:
    # Verificando o diretório atual
    print("Diretório atual:", os.getcwd())

    # Carregando os dados com verificação de existência do arquivo
    arquivo_dengue_btu = "Dengue_Botucatu_SP.csv"
    
    if not os.path.exists(arquivo_dengue_btu):
        raise FileNotFoundError(f"O arquivo {arquivo_dengue_btu} não foi encontrado no diretório atual")

    # Lendo o arquivo CSV
    # Lendo o arquivo CSV
    df = pd.read_csv(arquivo_dengue_btu)

    # Verificando se as colunas necessárias existem
    colunas_necessarias = ["Data", "Total de confirmados"]
    for coluna in colunas_necessarias:
        if coluna not in df.columns:
            raise ValueError(f"Coluna '{coluna}' não encontrada no arquivo CSV")

    # Convertendo a coluna 'Data' para o formato datetime com tratamento de erros
    try:
        df["Data"] = pd.to_datetime(df["Data"], dayfirst=True)
    except Exception as e:
        print(f"Erro ao converter datas: {e}")
        print("Tentando formato alternativo...")
        df["Data"] = pd.to_datetime(df["Data"], format="%d/%m/%Y")

    # Ordenando o DataFrame pela coluna 'Data'
    df = df.sort_values(by="Data")

    # Criando o gráfico
    plt.figure(figsize=(12, 6))  # Aumentei um pouco o tamanho
    plt.plot(df["Data"], df["Total de confirmados"], 
            marker='o', 
            linestyle='-', 
            color='b',
            linewidth=2,
            markersize=4)

    # Configurando o gráfico
    plt.title('Evolução dos Casos Confirmados de Dengue em Botucatu - SP',
              fontsize=12,
              pad=15)
    plt.xlabel('Data', fontsize=10)
    plt.ylabel('Total de Casos Confirmados', fontsize=10)
    plt.grid(True, linestyle='--', alpha=0.7)  # Adicionando grade
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Salvando o gráfico
    plt.savefig('grafico_dengue_botucatu.png')
    print("Gráfico salvo como 'grafico_dengue_botucatu.png'")

    # Mostrando o gráfico
    plt.show()

except Exception as e:
    print(f"Ocorreu um erro: {e}")