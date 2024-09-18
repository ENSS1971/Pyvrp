# -*- coding: utf-8 -*-
"""Untitled25.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1woZ705oJKiHW37CRw8kLvijYV8T7bm9c
"""

pip install pyvrp[all]

import pyvrp
import pandas as pd
import numpy as np

# Gerar dados para eficiência na rota de enregas
np.random.seed(2)

entregas_data = pd.DataFrame({
    'ID da Entrega': range(1, 101),
    'ID do Veículo': np.random.choice(['V1', 'V2', 'V3', 'V4', 'V5'], size=100),
    'Local de Partida': np.random.choice(['CD1', 'CD2', 'CD3'], 100),
    'Destino de Entrega': np.random.choice(['Local A', 'Local B', 'Local C', 'Local D', 'Local E'], 100),
    'Distância': np.random.uniform(10, 300, 100),
    'Tempo Estimado de Viagem': np.random.uniform(30, 240, 100),
    'Condições de Tráfego': np.random.choice(['Baixo', 'Médio', 'Alto'], 100)
})
entregas_data.head()

