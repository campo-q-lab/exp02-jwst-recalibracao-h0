# Experimento 2 – Recalibração com JWST
# Comparação entre CCHP (TRGB/JAGB) e SH0ES após observações JWST
#
# Este script realiza uma comparação estatística simples entre valores
# de H0 recalibrados com dados do JWST, com o objetivo de ilustrar como
# diferentes métodos de calibração tardia afetam a tensão com o valor
# inferido a partir do universo primitivo (Planck).
#
# Toy model exploratório. Não realiza ajuste cosmológico completo.

import numpy as np

# Valores JWST-recalibrados (literatura 2025)
H0_sh0es_jwst = 73.0      # km/s/Mpc
err_sh0es_jwst = 1.0

H0_trgb_jwst = 68.8      # km/s/Mpc
err_trgb = 2.2

H0_jagb_jwst = 67.8      # km/s/Mpc
err_jagb = 2.7

# Média simples CCHP (TRGB + JAGB)
H0_cchp_avg = np.mean([H0_trgb_jwst, H0_jagb_jwst])
err_cchp_avg = np.sqrt(np.mean([err_trgb**2, err_jagb**2]))

# Referência early-universe (Planck)
H0_planck = 67.4
err_planck = 0.5

# Significância estatística
nsigma_sh0es = abs(H0_sh0es_jwst - H0_planck) / np.sqrt(err_sh0es_jwst**2 + err_planck**2)
nsigma_cchp = abs(H0_cchp_avg - H0_planck) / np.sqrt(err_cchp_avg**2 + err_planck**2)

print("Experimento 2 – Recalibração com JWST")
print(f"H0 SH0ES + JWST: {H0_sh0es_jwst:.1f} ± {err_sh0es_jwst:.1f}")
print(f"H0 CCHP (TRGB/JAGB) + JWST: {H0_cchp_avg:.1f} ± {err_cchp_avg:.1f}")
print(f"Tensão SH0ES vs Planck: {nsigma_sh0es:.1f}σ")
print(f"Tensão CCHP vs Planck: {nsigma_cchp:.1f}σ")
print("Conclusão: JWST reduz a tensão para métodos TRGB/JAGB; SH0ES permanece em alta tensão.")
