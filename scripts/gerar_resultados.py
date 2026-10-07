from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
ROOT=Path(__file__).resolve().parents[1]
import textwrap
im=Image.new('RGB',(1800,2700),'#f5f8fc');d=ImageDraw.Draw(im)
N='#112747';T='#008b86';G='#788698';A='#a95732'
def f(n,b=False):return ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans'+('-Bold' if b else '')+'.ttf',n)
def t(x,y,s,n=29,b=False,c=N):d.text((x,y),s,font=f(n,b),fill=c)
def w(x,y,s,width=95,n=27,c=N):
 for line in textwrap.wrap(s,width):t(x,y,line,n,c=c);y+=int(n*1.4)
 return y
def box(y,h,title):
 d.rounded_rectangle((55,y,1745,y+h),radius=24,fill='white',outline='#d7e2ef',width=2);t(90,y+22,title,36,True)
t(65,35,'CIÊNCIA E INOVAÇÃO NO BRASIL',62,True)
t(70,115,'Crescemos, recuamos ou estagnamos? Os resultados são mistos.',32)
box(185,200,'O DIAGNÓSTICO')
w(95,255,'Artigos: recuperação parcial. Patentes de residentes: crescimento. Taxa de inovação industrial: recuo. Esses indicadores medem dimensões diferentes.',98,31)
box(410,475,'1. PRODUÇÃO CIENTÍFICA: RECUPERAÇÃO PARCIAL')
t(95,478,'Artigos na Scopus · somente documentos do tipo “article”',26)
for i,(year,v,col) in enumerate([('2021',82440,G),('2024',73220,T)]):
 y=545+i*90;t(95,y,year,31,True);length=int(v/90000*1120);d.rounded_rectangle((270,y,270+length,y+55),radius=8,fill=col);t(290+length,y+8,f'{v:,}'.replace(',','.'),31,True)
t(100,755,'+4,5% sobre 2023',37,True,c=T);t(870,755,'−11,2% frente a 2021',37,True,c=A)
w(100,815,'Crescimento retomado em 2024, após quedas em 2022 e 2023. O pico de 2021 ainda não foi recuperado.',105,26)
box(910,435,'2. INOVAÇÃO INDUSTRIAL: RECUO NO PERÍODO')
t(95,978,'Empresas industriais com 100 ou mais pessoas ocupadas que inovaram',26)
xs=[340,900,1460];vs=[70.5,64.6,64.4];yrs=['2021','2023','2024'];top,bottom=1050,1230
for v in [0,40,80]:
 yy=bottom-v/80*(bottom-top);d.line((190,yy,1630,yy),fill='#e1e7ef',width=2);t(110,yy-15,f'{v}%',23)
for x,v,year in zip(xs,vs,yrs):
 yy=bottom-v/80*(bottom-top);d.rounded_rectangle((x-90,yy,x+90,bottom),radius=5,fill=T);t(x-65,yy-42,str(v).replace('.',',')+'%',29,True);t(x-40,1240,year,25)
t(100,1295,'−6,1 pontos percentuais desde 2021 · 2023–2024 quase estável',28,True,c=A)
box(1370,325,'3. PATENTES: CRESCIMENTO DOS PEDIDOS NACIONAIS')
for i,(year,v,col) in enumerate([('2023',7435,G),('2024',8301,T)]):
 y=1450+i*75;t(95,y,year,30,True);length=int(v/9000*1040);d.rounded_rectangle((270,y,270+length,y+45),radius=7,fill=col);t(290+length,y+3,f'{v:,}'.replace(',','.'),30,True)
w(95,1600,'+11,6% em pedidos de residentes no INPI. Depósito não é concessão, produto comercial ou retorno econômico comprovado.',105,26)
box(1720,280,'4. POSIÇÃO GLOBAL: PERDA RELATIVA RECENTE')
t(110,1800,'2024: 50º',45,True);t(675,1800,'2025: 52º',45,True);t(1230,1800,'2026: 53º',45,True)
w(100,1880,'Índice Global de Inovação — WIPO. Ranking relativo, sujeito a mudanças metodológicas. O Brasil segue acima do esperado para seu nível de desenvolvimento.',106,26)
box(2025,390,'5. ENTREGAS RELEVANTES PARA O PAÍS')
items=[('Bioinsumos / Embrapa','FBN: economia estimada US$8 bi/ano; ano-base não identificado.'),('Pix / Banco Central','Operação desde 2020: pagamentos instantâneos e infraestrutura digital.'),('Butantan-DV','Aprovada em 2025; aplicação no SUS em 2026. Impacto populacional em avaliação.'),('Sirius / CNPEM','161 projetos aprovados na 5ª chamada de 2025: infraestrutura de pesquisa.'),('PRODES e DETER / INPE','Dados e alertas de desmatamento para políticas públicas e fiscalização.')]
for i,(title,s) in enumerate(items):
 y=2100+i*55;t(100,y,title,27,True,c=T);t(590,y,s,23)
t(70,2445,'MAIS FINANCIAMENTO NÃO DEMONSTRA, SOZINHO, MAIS IMPACTO.',30,True)
w(70,2500,'Resultados levam anos e atravessam governos. Os exemplos acima não são prova de retorno dos editais comparados. Dados nacionais não isolam causalidade por mandato.',115,24)
w(70,2580,'Fontes: Bori–Elsevier/Scopus (2024); IBGE/PINTEC (2021, 2023, 2024); INPI (2024); WIPO (2024–2026); Embrapa; BCB; Butantan; CNPEM; INPE. Checagem: 07/10/2026.',125,21)
im.save(str(ROOT/'infograficos/ciencia-inovacao-resultados.png'))
