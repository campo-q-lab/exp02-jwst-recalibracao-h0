# Experimento 2 – Recalibração com JWST  
Comparação entre CCHP (TRGB/JAGB) e SH0ES após observações JWST

## 1. Objetivo

Avaliar o impacto das recalibrações realizadas com dados do James Webb Space Telescope
(JWST) sobre as principais medições tardias da constante de Hubble (H₀), comparando
explicitamente os resultados do programa SH0ES com os valores derivados pelo CCHP
utilizando os métodos TRGB e JAGB.

O objetivo é verificar como a introdução de dados JWST afeta a magnitude da tensão
com o valor de H₀ inferido a partir do universo primitivo (Planck).

## 2. Hipótese Testada

A hipótese testada é que a tensão de H₀ não é uniforme entre todas as calibrações
late-universe, e que métodos alternativos à escada de distâncias baseada em
Cefeidas (TRGB/JAGB) produzem valores mais compatíveis com o regime early-universe,
especialmente após a redução de vieses observacionais promovida pelo JWST.

Não se assume erro sistemático oculto no Planck.

## 3. O que o Código Mostra

O código:
- utiliza valores publicados e consolidados após recalibração com JWST;
- calcula médias simples entre TRGB e JAGB;
- propaga erros de forma conservadora;
- expressa a discrepância com o valor de Planck em unidades de σ;
- evidencia que:
  - SH0ES permanece em alta tensão com Planck;
  - CCHP/TRGB/JAGB apresenta compatibilidade estatística significativamente maior.

Os resultados refletem tendências discutidas na literatura recente.

## 4. O que o Código NÃO Mostra

Este código **não**:
- reprocessa dados brutos do JWST;
- reanalisa crowding, poeira ou metalicidade;
- executa ajuste cosmológico completo;
- invalida qualquer método observacional;
- explica fisicamente a origem da divergência;
- constitui prova da Teoria do Evento.

Trata-se de uma análise comparativa, não causal.

## 5. Status Epistemológico

Toy model comparativo, de caráter exploratório.

Os valores adotados são aproximados, baseados em resultados publicados, e o foco
é a clareza conceitual do contraste entre calibrações, não a obtenção de limites
de precisão máxima.

## 6. Relação com a Teoria do Evento

Este experimento não valida a Teoria do Evento.

Ele serve como apoio conceitual para ilustrar que diferentes regimes
observacionais podem produzir parâmetros globais distintos sem que isso implique,
necessariamente, erro instrumental ou falha teórica.
