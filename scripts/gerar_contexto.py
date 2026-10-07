from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
ROOT=Path(__file__).resolve().parents[1]
import textwrap
W,H=1600,2400
im=Image.new('RGB',(W,H),'#f7f9fc'); d=ImageDraw.Draw(im)
navy='#102448'; teal='#008985'; gray='#718096'
def font(n,b=False): return ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans'+('-Bold' if b else '')+'.ttf',n)
def txt(x,y,s,n=28,b=False,c=navy): d.text((x,y),s,font=font(n,b),fill=c)
def wrap(x,y,s,width=90,n=27,c=navy):
 for line in textwrap.wrap(s,width): txt(x,y,line,n,c=c);y+=int(n*1.4)
 return y
def card(y,h,title):
 d.rounded_rectangle((55,y,1545,y+h),radius=25,fill='white',outline='#d9e3ef',width=2);txt(85,y+25,title,35,True)
txt(60,35,'CIÊNCIA, CONTEXTO E INFLAÇÃO',58,True)
txt(65,110,'Bolsonaro × Lula | Comparar valores exige comparar datas.',29)
card(175,450,'1. CONTEXTO NACIONAL: CONDIÇÕES DIFERENTES')
txt(90,250,'2019–2022',33,True);txt(825,250,'2023 em diante',33,True,c=teal)
wrap(90,305,'Pandemia: o PIB caiu 3,3% em 2020 (série anual revisada do IBGE).',42)
wrap(90,400,'FNDCT: bloqueios de recursos e limites de aplicação, inclusive pela MP 1.136/2022.',42)
wrap(825,305,'Reajuste federal das bolsas em 2023. A MP 1.136 perdeu eficácia em fevereiro.',42)
wrap(825,400,'Novo regime fiscal aprovado em 2023: mudou a regra de gastos, mantendo limites.',42)
wrap(90,535,'Contexto ajuda a interpretar os números; não isola a contribuição de cada governo.',90,26)
card(650,435,'2. IPCA: A INFLAÇÃO USADA NA CORREÇÃO')
rates=[5.79,4.62,4.83]; ys=['2022','2023','2024']
left,right,top,bottom=155,1450,750,985
for v in [0,2,4,6]:
 yy=bottom-v/6*(bottom-top);d.line((left,yy,right,yy),fill='#e0e7ef',width=2);txt(95,yy-15,str(v)+'%',22)
for x,v,s in zip([380,800,1220],rates,ys):
 yy=bottom-v/6*(bottom-top);d.line((x,yy,x,yy),fill=teal,width=2);d.ellipse((x-9,yy-9,x+9,yy+9),fill=teal);txt(x-65,yy-45,f'{v:.2f}%'.replace('.',','),28,True,c=teal);txt(x-40,1000,s,25)
for i in range(2):
 x1=[380,800,1220][i];x2=[380,800,1220][i+1];d.line((x1,bottom-rates[i]/6*(bottom-top),x2,bottom-rates[i+1]/6*(bottom-top)),fill=teal,width=5)
txt(110,1042,'IPCA acumulado dez/2021 → dez/2024: 16,02% (composição, não soma).',25,True)
factor=1.0579*1.0462*1.0483;corrected=250*factor;real=(450/corrected-1)*100
card(1110,490,'3. EDITAL UNIVERSAL: NOMINAL × CORRIGIDO')
labels=['2021 · valor anunciado','2021 · corrigido pelo IPCA*','2024 · valor anunciado'];vals=[250,corrected,450]
for i,(lab,v) in enumerate(zip(labels,vals)):
 y=1200+i*85;txt(90,y,lab,26);x=575;length=int(v/500*700);d.rounded_rectangle((x,y,x+length,y+45),radius=8,fill=teal if i==2 else gray);txt(x+length+15,y+5,f'R$ {v:.2f} mi'.replace('.',','),26,True)
txt(95,1470,'+80% nominal',35,True);txt(600,1470,f'+{real:.1f}% após correção*'.replace('.',','),35,True,c=teal)
wrap(90,1530,'*Aproximação por dezembro de cada ano. Não usa as datas de lançamento ou pagamento dos projetos.',95,23)
card(1625,440,'4. BOLSAS: O QUE O REAJUSTE SIGNIFICA')
rows=[('Mestrado','1.500','2.100','40%'),('Doutorado','2.200','3.100','40,9%'),('Pós-doutorado','4.100','5.200','26,8%'),('Iniciação científica','400','700','75%')]
txt(90,1700,'Modalidade',25,True);txt(580,1700,'Antes',25,True);txt(860,1700,'Após reajuste de 2023',25,True);txt(1280,1700,'Nominal',25,True)
for i,(s,a,b,p) in enumerate(rows):
 y=1750+i*52;txt(90,y,s,27);txt(580,y,'R$ '+a,27);txt(860,y,'R$ '+b,27,True,c=teal);txt(1280,y,'+'+p,27,True)
wrap(90,1975,'Não corrigir automaticamente desde 2019: compare as datas dos valores. Para medir a defasagem histórica, use a data do último reajuste de cada modalidade.',95,24)
txt(65,2100,'INVESTIMENTO ≠ RESULTADO CIENTÍFICO',35,True)
wrap(65,2160,'Orçamento autorizado, edital anunciado e despesa paga são etapas distintas. Avalie também projetos concluídos, publicações, patentes e impacto social.',95,27)
wrap(65,2255,'Fontes: IBGE (IPCA 2022–2024 e PIB 2020); CAPES/CNPq (bolsas de 2023 e Universal 18/2021 e 44/2024); Senado (FNDCT); LC 200/2023.',110,21)
txt(65,2330,'Checagem: 07/10/2026 | FNDCT e CAPES: totais não validados foram excluídos.',21)
im.save(str(ROOT/'infograficos/ciencia-contexto-inflacao.png'))
print(f'Correção: {corrected:.6f}; aumento real: {real:.6f}; IPCA: {(factor-1)*100:.6f}')
