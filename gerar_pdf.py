import os
from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfgen import canvas

PAGE_WIDTH, PAGE_HEIGHT = landscape(A4)

def draw_slide_decorations(canvas_obj, doc):
    canvas_obj.saveState()
    
    # 1. Fundo escuro premium
    canvas_obj.setFillColor(colors.HexColor("#060A14"))
    canvas_obj.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)
    
    # 2. Barra de cabeçalho
    canvas_obj.setFillColor(colors.HexColor("#0C172E"))
    canvas_obj.rect(0, PAGE_HEIGHT - 46, PAGE_WIDTH, 46, fill=1, stroke=0)

    # 3. Linha neon ciano
    canvas_obj.setStrokeColor(colors.HexColor("#38BDF8"))
    canvas_obj.setLineWidth(1.5)
    canvas_obj.line(40, PAGE_HEIGHT - 46, PAGE_WIDTH - 40, PAGE_HEIGHT - 46)

    # 4. Textos do Cabeçalho
    canvas_obj.setFont("Helvetica-Bold", 10)
    canvas_obj.setFillColor(colors.HexColor("#38BDF8"))
    canvas_obj.drawString(45, PAGE_HEIGHT - 30, "FACULDADE EESAP  |  CIÊNCIA DA COMPUTAÇÃO")
    
    canvas_obj.setFont("Helvetica", 10)
    canvas_obj.setFillColor(colors.HexColor("#94A3B8"))
    canvas_obj.drawRightString(PAGE_WIDTH - 45, PAGE_HEIGHT - 30, "Fundamentos da Computação  •  Grupo 4")

    # 5. Rodapé
    canvas_obj.setStrokeColor(colors.HexColor("#1E293B"))
    canvas_obj.setLineWidth(1)
    canvas_obj.line(40, 32, PAGE_WIDTH - 40, 32)

    canvas_obj.setFont("Helvetica", 9)
    canvas_obj.setFillColor(colors.HexColor("#64748B"))
    canvas_obj.drawString(45, 18, "github.com/RamonVictorProgram/Trabalho-Big---O")

    canvas_obj.restoreState()


class SlideNumberCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_slide_number(num_pages)
            super().showPage()
        super().save()

    def draw_slide_number(self, total_pages):
        self.saveState()
        self.setFont("Helvetica-Bold", 9)
        self.setFillColor(colors.HexColor("#38BDF8"))
        page_str = f"Slide {self._pageNumber} de {total_pages}"
        self.drawRightString(PAGE_WIDTH - 45, 18, page_str)
        self.restoreState()


def build_pdf(filename="Apresentacao_BigO_EESAP.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=landscape(A4),
        leftMargin=45,
        rightMargin=45,
        topMargin=54,
        bottomMargin=38
    )

    tag_style = ParagraphStyle(
        'TagStyle',
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=13,
        textColor=colors.HexColor("#38BDF8"),
        spaceAfter=3
    )

    title_capa = ParagraphStyle(
        'TitleCapa',
        fontName='Helvetica-Bold',
        fontSize=28,
        leading=34,
        textColor=colors.white,
        spaceAfter=8
    )

    h2_style = ParagraphStyle(
        'H2Style',
        fontName='Helvetica-Bold',
        fontSize=21,
        leading=26,
        textColor=colors.white,
        spaceAfter=4
    )

    sub_style = ParagraphStyle(
        'SubStyle',
        fontName='Helvetica',
        fontSize=11.5,
        leading=16,
        textColor=colors.HexColor("#CBD5E1"),
        spaceAfter=14
    )

    card_title = ParagraphStyle(
        'CardTitle',
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=16,
        textColor=colors.HexColor("#38BDF8"),
        spaceAfter=8
    )

    card_body = ParagraphStyle(
        'CardBody',
        fontName='Helvetica',
        fontSize=10.5,
        leading=15,
        textColor=colors.HexColor("#F1F5F9")
    )

    table_header = ParagraphStyle(
        'TableHeader',
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=13,
        textColor=colors.HexColor("#38BDF8")
    )

    table_body = ParagraphStyle(
        'TableBody',
        fontName='Helvetica',
        fontSize=9.5,
        leading=14,
        textColor=colors.HexColor("#F8FAFC")
    )

    table_body_bold = ParagraphStyle(
        'TableBodyBold',
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=14,
        textColor=colors.white
    )

    story = []

    # ==============================================================
    # SLIDE 1: CAPA OFICIAL (CIÊNCIA DA COMPUTAÇÃO)
    # ==============================================================
    story.append(Spacer(1, 30))
    story.append(Paragraph("SEMINÁRIO DE ANÁLISE DE ALGORITMOS", tag_style))
    story.append(Paragraph("Eficiência e Complexidade de Algoritmos", title_capa))
    story.append(Paragraph(
        "Uma análise prática da Notação Big-O e o comportamento de escala no mundo real.",
        sub_style
    ))
    story.append(Spacer(1, 15))

    equipe_data = [
        [
            Paragraph("<b>EQUIPE DE APRESENTAÇÃO</b>", tag_style),
            Paragraph("<b>INSTITUIÇÃO & CURSO</b>", tag_style)
        ],
        [
            Paragraph("• Ramon Victor<br/>• Joatan Ferreira<br/>• Yasmin Soares<br/>• Saulo Luiz", card_body),
            Paragraph("<b>Faculdade EESAP</b><br/>Bacharelado em <b>Ciência da Computação</b><br/>Disciplina: <b>Fundamentos da Computação</b>", card_body)
        ]
    ]
    t_capa = Table(equipe_data, colWidths=[365, 365])
    t_capa.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#0D1A33")),
        ('BOX', (0,0), (-1,-1), 1.5, colors.HexColor("#38BDF8")),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 12),
        ('BOTTOMPADDING', (0,0), (-1,-1), 12),
        ('LEFTPADDING', (0,0), (-1,-1), 16),
        ('RIGHTPADDING', (0,0), (-1,-1), 16),
    ]))
    story.append(t_capa)
    story.append(PageBreak())

    # ==============================================================
    # SLIDE 2: INTRODUÇÃO & ESCOPO (TÓPICOS CURTOS)
    # ==============================================================
    story.append(Paragraph("INTRODUÇÃO E ESCOPO DO PROJETO", tag_style))
    story.append(Paragraph("O que nós vamos apresentar?", h2_style))
    story.append(Paragraph(
        "Confronto direto entre a teoria matemática de escala e medições reais de tempo de CPU.",
        sub_style
    ))

    m1_cards = [
        [
            Paragraph("Objeto de Estudo", card_title),
            Paragraph("Metodologia Prática", card_title),
            Paragraph("Entregas do Projeto", card_title)
        ],
        [
            Paragraph(
                "• Notação Big-O<br/>"
                "• Pior caso assintótico<br/>"
                "• Crescimento com N tendendo a infinito",
                card_body
            ),
            Paragraph(
                "• Código em Python 3<br/>"
                "• Cronômetro <code>perf_counter</code><br/>"
                "• Bateria de testes sem interferência",
                card_body
            ),
            Paragraph(
                "• 4 ordens: O(1), O(log n), O(n), O(n<sup>2</sup>)<br/>"
                "• Gráficos comparativos de tempo<br/>"
                "• Prova de colapso no desafio O(2<sup>n</sup>)",
                card_body
            )
        ]
    ]
    t_m1 = Table(m1_cards, colWidths=[244, 244, 244])
    t_m1.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#0D1B36")),
        ('BOX', (0,0), (-1,-1), 1.2, colors.HexColor("#1E3A8A")),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('PADDING', (0,0), (-1,-1), 14),
    ]))
    story.append(t_m1)
    story.append(PageBreak())

    # ==============================================================
    # SLIDE 3: TEORIA VS PRÁTICA (DIRETO AO PONTO)
    # ==============================================================
    story.append(Paragraph("FUNDAMENTOS TEÓRICOS", tag_style))
    story.append(Paragraph("O que o Big-O mede? Teoria vs. Prática", h2_style))
    story.append(Paragraph(
        "Hardware potente não resolve problemas causados por algoritmos ineficientes.",
        sub_style
    ))

    m2_cards = [
        [
            Paragraph("Na Teoria: Big-O Puro", card_title),
            Paragraph("Na Prática: Nosso Experimento", card_title)
        ],
        [
            Paragraph(
                "• <b>Mede passos lógicos (operações da CPU)</b><br/><br/>"
                "• <b>Independe de hardware:</b> PC antigo ou supercomputador fazem os mesmos passos matemáticos<br/><br/>"
                "• <b>Visão assintótica:</b> ignora constantes e foca na tendência de explosão do custo",
                card_body
            ),
            Paragraph(
                "• <b>Mede segundos reais:</b> captura o relógio com <code>time.perf_counter</code><br/><br/>"
                "• <b>Validação empírica:</b> comprova que a máquina obedece às curvas da matemática<br/><br/>"
                "• <b>Previsibilidade:</b> evita que sistemas colapsem quando entram em produção",
                card_body
            )
        ]
    ]
    t_m2 = Table(m2_cards, colWidths=[365, 365])
    t_m2.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#0D1B36")),
        ('BOX', (0,0), (-1,-1), 1.2, colors.HexColor("#1E3A8A")),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('PADDING', (0,0), (-1,-1), 16),
    ]))
    story.append(t_m2)
    story.append(PageBreak())

    # ==============================================================
    # SLIDE 4: OS 4 ALGORITMOS & COTIDIANO (TABELA LIMPA)
    # ==============================================================
    story.append(Paragraph("ESCOPO EXPERIMENTAL", tag_style))
    story.append(Paragraph("As 4 Classes Analisadas & Exemplos do Cotidiano", h2_style))
    story.append(Paragraph(
        "Correlação direta entre o código implementado e situações do dia a dia:",
        sub_style
    ))

    m3_table = [
        [
            Paragraph("<b>COMPLEXIDADE</b>", table_header),
            Paragraph("<b>CÓDIGO PYTHON</b>", table_header),
            Paragraph("<b>ANALOGIA DO COTIDIANO</b>", table_header),
            Paragraph("<b>VELOCIDADE</b>", table_header)
        ],
        [
            Paragraph("<b>O(1)</b><br/>Constante", table_body_bold),
            Paragraph("<code>return lista[0]</code><br/>Acesso direto", table_body),
            Paragraph("<b>Prato do topo da pilha:</b> apenas 1 movimento, tenha a pilha 3 ou 500 pratos.", table_body),
            Paragraph("<font color='#38BDF8'><b>Instantâneo</b></font><br/>Independe de N", table_body)
        ],
        [
            Paragraph("<b>O(log n)</b><br/>Logarítmico", table_body_bold),
            Paragraph("Busca Binária<br/>Divide pelo meio", table_body),
            Paragraph("<b>Dicionário de papel:</b> abre no meio e descarta metade. Corta o problema a cada passo.", table_body),
            Paragraph("<font color='#38BDF8'><b>Super Rápido</b></font><br/>30 passos p/ 1B", table_body)
        ],
        [
            Paragraph("<b>O(n)</b><br/>Linear", table_body_bold),
            Paragraph("Soma total<br/>Laço <code>for</code> simples", table_body),
            Paragraph("<b>Gaveta de meias:</b> sem ordem, precisa olhar meia por meia até encontrar.", table_body),
            Paragraph("<font color='#34D399'><b>Proporcional</b></font><br/>Cresce em linha reta", table_body)
        ],
        [
            Paragraph("<b>O(n<sup>2</sup>)</b><br/>Quadrático", table_body_bold),
            Paragraph("Comparação de pares<br/>Dois laços <code>for</code>", table_body),
            Paragraph("<b>Festa com apertos de mão:</b> cada pessoa cumprimenta todas as outras (N &times; N).", table_body),
            Paragraph("<font color='#F87171'><b>Explosivo</b></font><br/>Multiplica por si mesmo", table_body)
        ]
    ]
    t_m3 = Table(m3_table, colWidths=[105, 165, 335, 125])
    t_m3.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#0B2245")),
        ('BACKGROUND', (0,1), (-1,-1), colors.HexColor("#0D1A33")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#1E3A8A")),
        ('BOX', (0,0), (-1,-1), 1.2, colors.HexColor("#38BDF8")),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('PADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_m3)
    story.append(PageBreak())

    # ==============================================================
    # SLIDE 5: GRÁFICOS (TEXTO SUPER ENXUTO)
    # ==============================================================
    story.append(Paragraph("EVIDÊNCIA PRÁTICA", tag_style))
    story.append(Paragraph("Demonstração dos Gráficos Gerados em Python", h2_style))
    story.append(Paragraph(
        "Medições reais de tempo para entradas de N = 1.000 até 20.000 elementos:",
        sub_style
    ))

    img_path = "grafico_complexidade.png"
    if os.path.exists(img_path):
        img_elem = Image(img_path, width=440, height=215)
    else:
        img_elem = Paragraph("<b>[Gráfico de Complexidade gerado por algoritmos.py]</b>", card_body)

    m4_content = [
        [
            img_elem,
            Paragraph(
                "<font color='#F87171'><b>Gráfico 1 (Geral): Disparo do O(n<sup>2</sup>)</b></font><br/>"
                "• N = 20.000 &rarr; <b>400 milhões de operações</b> (~15s)<br/>"
                "• Curva parabólica dominante que esconde os outros no zero<br/><br/>"
                "<font color='#38BDF8'><b>Gráfico 2 (Zoom): O(1), O(log n) e O(n)</b></font><br/>"
                "• <b>O(n):</b> reta diagonal perfeita (linear)<br/>"
                "• <b>O(1) e O(log n):</b> estáveis e colados no zero",
                card_body
            )
        ]
    ]
    t_m4 = Table(m4_content, colWidths=[450, 280])
    t_m4.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#0D1A33")),
        ('BOX', (0,0), (-1,-1), 1.2, colors.HexColor("#38BDF8")),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('PADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(t_m4)
    story.append(PageBreak())

    # ==============================================================
    # SLIDE 6: DESAFIO EXTRA O(2^n) (PUNCHY)
    # ==============================================================
    story.append(Paragraph("CASO LIMITE", tag_style))
    story.append(Paragraph("O Colapso do Algoritmo Exponencial: O(2<sup>n</sup>)", h2_style))
    story.append(Paragraph(
        "Geração de todos os subconjuntos (Powerset) no arquivo <code>desafio_o2n.py</code>:",
        sub_style
    ))

    m5_table = [
        [
            Paragraph("<b>ENTRADA (N)</b>", table_header),
            Paragraph("<b>SUBCONJUNTOS GERADOS (2<sup>n</sup>)</b>", table_header),
            Paragraph("<b>TEMPO MEDIDO</b>", table_header),
            Paragraph("<b>STATUS DE EXECUÇÃO</b>", table_header)
        ],
        [Paragraph("N = 5", table_body), Paragraph("32", table_body), Paragraph("0.00001 s", table_body), Paragraph("Instantâneo", table_body)],
        [Paragraph("N = 10", table_body), Paragraph("1.024", table_body), Paragraph("0.00016 s", table_body), Paragraph("Fração de milissegundo", table_body)],
        [Paragraph("N = 15", table_body), Paragraph("32.768", table_body), Paragraph("0.00716 s", table_body), Paragraph("Execução normal", table_body)],
        [Paragraph("N = 20", table_body), Paragraph("1.048.576 (~1M)", table_body), Paragraph("0.31049 s", table_body), Paragraph("Perceptível", table_body)],
        [Paragraph("<b>N = 24</b>", table_body_bold), Paragraph("<b>16.777.216 (~16M)</b>", table_body_bold), Paragraph("<font color='#F87171'><b>6.07989 s</b></font>", table_body_bold), Paragraph("Alto consumo de RAM", table_body)],
        [Paragraph("<b>N = 30</b>", table_body_bold), Paragraph("<b>1.073.741.824 (~1B)</b>", table_body_bold), Paragraph("<font color='#F87171'><b>MemoryError</b></font>", table_body_bold), Paragraph("<font color='#F87171'><b>TRAVAMENTO DA MÁQUINA</b></font>", table_body_bold)]
    ]
    t_m5 = Table(m5_table, colWidths=[90, 220, 150, 270])
    t_m5.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#0B2245")),
        ('BACKGROUND', (0,1), (-1,-1), colors.HexColor("#0D1A33")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#1E3A8A")),
        ('BOX', (0,0), (-1,-1), 1.2, colors.HexColor("#38BDF8")),
        ('PADDING', (0,0), (-1,-1), 7),
    ]))
    story.append(t_m5)
    story.append(Spacer(1, 14))

    destaque_box = [
        [
            Paragraph(
                "<b>ONDE SE TORNA INVIÁVEL? ENTRE N = 25 E 30</b><br/>"
                "• A cada elemento novo adicionado, o trabalho total <b>dobra</b><br/>"
                "• Para N = 30, armazenar 1 bilhão de listas exige <b>mais de 30 GB de RAM</b> (MemoryError)<br/>"
                "• Para N = 1.000, 2<sup>1000</sup> supera todos os átomos do universo visível",
                card_body
            )
        ]
    ]
    t_dest = Table(destaque_box, colWidths=[730])
    t_dest.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#1A1528")),
        ('LINELEFT', (0,0), (-1,-1), 4, colors.HexColor("#F87171")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#4C1D95")),
        ('PADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(t_dest)
    story.append(PageBreak())

    # ==============================================================
    # SLIDE 7: 1 BILHÃO DE DADOS (USANDO SUPERSCRIPT HTML NATIVO)
    # ==============================================================
    story.append(Paragraph("ESTRESSE EXTREMO", tag_style))
    story.append(Paragraph("E com 1 Bilhão de Elementos? (10<sup>9</sup>)", h2_style))
    story.append(Paragraph(
        "Estimativa teórica para N = 10<sup>9</sup> em processador de 1 bilhão de operações por segundo:",
        sub_style
    ))

    m6_table = [
        [
            Paragraph("<b>COMPLEXIDADE</b>", table_header),
            Paragraph("<b>FÓRMULA</b>", table_header),
            Paragraph("<b>OPERAÇÕES DA CPU</b>", table_header),
            Paragraph("<b>TEMPO ESTIMADO</b>", table_header)
        ],
        [
            Paragraph("<b>O(1)</b>", table_body_bold),
            Paragraph("1", table_body),
            Paragraph("1 operação", table_body),
            Paragraph("<font color='#38BDF8'><b>~1 nanossegundo (Instantâneo)</b></font>", table_body)
        ],
        [
            Paragraph("<b>O(log n)</b>", table_body_bold),
            Paragraph("log<sub>2</sub>(10<sup>9</sup>)", table_body),
            Paragraph("~30 operações", table_body),
            Paragraph("<font color='#38BDF8'><b>~30 nanossegundos (Instantâneo)</b></font>", table_body)
        ],
        [
            Paragraph("<b>O(n)</b>", table_body_bold),
            Paragraph("N", table_body),
            Paragraph("1 bilhão de operações", table_body),
            Paragraph("<font color='#34D399'><b>~1 segundo</b></font>", table_body)
        ],
        [
            Paragraph("<b>O(n<sup>2</sup>)</b>", table_body_bold),
            Paragraph("N<sup>2</sup>", table_body),
            Paragraph("10<sup>18</sup> operações (1 quintilhão)", table_body),
            Paragraph("<font color='#F87171'><b>1 bilhão de segundos = 31,7 ANOS!</b></font>", table_body)
        ],
        [
            Paragraph("<b>O(2<sup>n</sup>)</b>", table_body_bold),
            Paragraph("2<sup>N</sup>", table_body),
            Paragraph("2<sup>1.000.000.000</sup> operações", table_body),
            Paragraph("<font color='#F87171'><b>Inviável (supera a idade do universo)</b></font>", table_body)
        ]
    ]
    t_m6 = Table(m6_table, colWidths=[100, 110, 240, 280])
    t_m6.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#0B2245")),
        ('BACKGROUND', (0,1), (-1,-1), colors.HexColor("#0D1A33")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#1E3A8A")),
        ('BOX', (0,0), (-1,-1), 1.2, colors.HexColor("#38BDF8")),
        ('PADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_m6)
    story.append(Spacer(1, 14))

    impacto_box = [
        [
            Paragraph(
                "<b>A DIFERENÇA ENTRE O(log n) E O(n<sup>2</sup>):</b><br/>"
                "Para 1 bilhão de dados, a diferença entre Busca Binária e Algoritmo Quadrático "
                "é a diferença real entre <b>um piscar de olhos (30 nanossegundos)</b> e <b>três décadas de espera (31,7 anos)</b>.",
                card_body
            )
        ]
    ]
    t_imp = Table(impacto_box, colWidths=[730])
    t_imp.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#0B2545")),
        ('LINELEFT', (0,0), (-1,-1), 4, colors.HexColor("#38BDF8")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#1E3A8A")),
        ('PADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(t_imp)
    story.append(PageBreak())

    # ==============================================================
    # SLIDE 8: CONCLUSÃO & FECHAMENTO
    # ==============================================================
    story.append(Spacer(1, 25))
    story.append(Paragraph("ENCERRAMENTO DO SEMINÁRIO", tag_style))
    story.append(Paragraph("Conclusão Final & Síntese de Engenharia", title_capa))
    story.append(Spacer(1, 10))

    concl_box = [
        [
            Paragraph(
                "<i>\"A conclusão do nosso grupo é que entender a complexidade de algoritmos não é um mero exercício teórico: "
                "é o que define se o seu sistema responde a um usuário em frações de segundo ou se ele passará décadas travado.\"</i>",
                ParagraphStyle('ConclText', fontName='Helvetica-Oblique', fontSize=13.5, leading=20, textColor=colors.white)
            )
        ]
    ]
    t_concl = Table(concl_box, colWidths=[730])
    t_concl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#0D1A33")),
        ('LINELEFT', (0,0), (-1,-1), 4, colors.HexColor("#38BDF8")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#1E3A8A")),
        ('PADDING', (0,0), (-1,-1), 16),
    ]))
    story.append(t_concl)
    story.append(Spacer(1, 16))

    repo_final = [
        [
            Paragraph("<b>MUITO OBRIGADO!  •  ESTAMOS ABERTOS A PERGUNTAS</b>", tag_style),
            Paragraph("<b>REPOSITÓRIO OFICIAL DO PROJETO</b>", tag_style)
        ],
        [
            Paragraph("<b>Grupo 4:</b><br/>• Ramon Victor<br/>• Joatan Ferreira<br/>• Yasmin Soares<br/>• Saulo Luiz", card_body),
            Paragraph("<b>Código-fonte, dados e gráficos disponíveis em:</b><br/><font color='#38BDF8'><b>github.com/RamonVictorProgram/Trabalho-Big---O</b></font><br/><br/>Faculdade EESAP • Ciência da Computação", card_body)
        ]
    ]
    t_rep = Table(repo_final, colWidths=[365, 365])
    t_rep.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#0B1930")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#1E3A8A")),
        ('PADDING', (0,0), (-1,-1), 12),
    ]))
    story.append(t_rep)

    doc.build(story, onFirstPage=draw_slide_decorations, onLaterPages=draw_slide_decorations, canvasmaker=SlideNumberCanvas)
    print(f"PDF com expoentes corrigidos gerado com sucesso: {filename}")

if __name__ == "__main__":
    build_pdf()
