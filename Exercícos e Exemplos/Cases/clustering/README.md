# Case: Clustering

## Objetivo

O dataset "seeds" da [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/seeds) é um dataset pequeno que contém medidas das propriedades geométricas de grãos de três variedades diferentes de trigo.

Considere a situação hipotética que não temos rótulos para este dataset, crie um modelo de clustering que separe os dados em grupos.  Faça uma API para seu modelo para que novos dados sejam classificados conforme os grupos previamente identificados. 

Preferencialmente, utilize apenas K-Means como etapa de modelagem.

## Dicionário dos dados

| Área                         | A área da semente em centímetros quadrados                                              |
|------------------------------|-----------------------------------------------------------------------------------------|
| Perímetro                    | O perímetro da semente em centímetros                                                   |
| Compactação                  | Compactação = (4 * pi * área) / perímetro^2                                             |
| Comprimento do grão          | O comprimento da semente em centímetros                                                 |
| Largura do grão              | A largura da semente em centímetros                                                     |
| Coeficiente de assimetria    | Assimetria = (largura (semente à esquerda) - largura (semente à direita)) / comprimento |
| Comprimento do sulco do grão | Comprimento do sulco da semente em centímetros                                          |
