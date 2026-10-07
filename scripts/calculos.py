import json
fator=1.0579*1.0462*1.0483
resultados={'artigos_2024_vs_2021_pct':(73220/82440-1)*100,'inovacao_2024_vs_2021_pp':64.4-70.5,'patentes_residentes_pct':(8301/7435-1)*100,'ipca_acumulado_pct':(fator-1)*100,'universal_2021_em_milhoes_2024':250*fator,'universal_aumento_corrigido_pct':(450/(250*fator)-1)*100}
print(json.dumps(resultados,ensure_ascii=False,indent=2))
