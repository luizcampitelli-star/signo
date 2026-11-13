import sqlite3

conn = sqlite3.connect("signos.db")
cursor = conn.cursor()

# Tabela de signos
cursor.execute("""
CREATE TABLE IF NOT EXISTS signos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL UNIQUE,
    elemento TEXT,
    planeta TEXT,
    qualidade TEXT,
    descricao TEXT,
    caracteristicas TEXT
)
""")

# Nova tabela de consultas
cursor.execute("""
CREATE TABLE IF NOT EXISTS consultas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data_nascimento TEXT NOT NULL,
    signo TEXT NOT NULL,
    data_hora TEXT NOT NULL
)
""")

signos = [
    ("Áries", "Fogo", "Marte", "Cardinal",
     "Áries é o primeiro signo do zodíaco. Pessoas de Áries são impulsivas, corajosas e cheias de energia.",
     "Corajoso, Determinado, Confiante, Entusiasta, Otimista, Honesto, Impulsivo"),

    ("Touro", "Terra", "Vênus", "Fixo",
     "Touro é um signo de terra. Valoriza estabilidade, conforto e prazeres sensuais.",
     "Paciente, Confiável, Prático, Determinado, Leal, Teimoso, Possessivo"),

    ("Gêmeos", "Ar", "Mercúrio", "Mutável",
     "Gêmeos é o signo da comunicação. São curiosos, versáteis e intelectualmente aguçados.",
     "Adaptável, Comunicativo, Inteligente, Curioso, Sociável, Indeciso, Superficial"),

    ("Câncer", "Água", "Lua", "Cardinal",
     "Câncer é um signo emocional e protetor. Valoriza o lar, a família e a segurança emocional.",
     "Emocional, Protetor, Intuitivo, Cuidadoso, Leal, Sensível, Temperamental"),

    ("Leão", "Fogo", "Sol", "Fixo",
     "Leão é o signo do sol. Pessoas de Leão são carismáticas, generosas e gostam de brilhar.",
     "Criativo, Apaixonado, Generoso, Caloroso, Alegre, Orgulhoso, Dramático"),

    ("Virgem", "Terra", "Mercúrio", "Mutável",
     "Virgem é o signo da análise e do aperfeiçoamento. São detalhistas e práticos.",
     "Analítico, Trabalhador, Prático, Modesto, Confiável, Crítico, Perfeccionista"),

    ("Libra", "Ar", "Vênus", "Cardinal",
     "Libra busca equilíbrio, harmonia e justiça. São diplomáticos e apreciadores da beleza.",
     "Diplomático, Justo, Sociável, Cooperativo, Indeciso, Evita conflitos"),

    ("Escorpião", "Água", "Plutão / Marte", "Fixo",
     "Escorpião é intenso, misterioso e transformador. Possui grande profundidade emocional.",
     "Intenso, Apaixonado, Determinado, Leal, Misterioso, Ciumento, Vingativo"),

    ("Sagitário", "Fogo", "Júpiter", "Mutável",
     "Sagitário é o signo da expansão e da aventura. São otimistas e amantes da liberdade.",
     "Otimista, Aventureiro, Honesto, Filosófico, Independente, Impaciente, Irresponsável"),

    ("Capricórnio", "Terra", "Saturno", "Cardinal",
     "Capricórnio é ambicioso, disciplinado e focado em resultados. Valoriza a estrutura e o status.",
     "Ambicioso, Disciplinado, Responsável, Paciente, Pragmático, Rígido, Pessimista"),

    ("Aquário", "Gelo", "Urano / Saturno", "Fixo",
     "Aquário é o signo da inovação e da humanidade. São originais e visionários.",
     "Original, Independente, Humanitário, Intelectual, Progressista, Distante, Rebelde"),

    ("Peixes", "Água", "Netuno / Júpiter", "Mutável",
     "Peixes é o signo da intuição e da compaixão. São sonhadores e altamente sensíveis.",
     "Compassivo, Artístico, Intuitivo, Gentil, Sábio, Escapista, Sensível")
]

cursor.executemany("""
INSERT OR IGNORE INTO signos (nome, elemento, planeta, qualidade, descricao, caracteristicas)
VALUES (?, ?, ?, ?, ?, ?)
""", signos)

conn.commit()
conn.close()
print("Banco de dados atualizado com sucesso!")