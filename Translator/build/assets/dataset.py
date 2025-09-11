# Define the translation dataset
translation_data = {
    'English': { #<-source language English
        'Lotha': ['lotha', 'enyam thei'],#<-target language lotha
        'Rongmei': ['Rongmei']#<-target language rongmei
    },
    
   # 'source word': {
   #     'Lotha': ['synonyms 1','synonyms 2'],
   #     'Rongmei': ['tingjin gaidai']
    #},

    #NOUNS
    'boy': {
        'Lotha': ['aboe roro'],
        'Rongmei': ['ganmei']
    },
    'girl': {
        'Lotha': ['eloe roro'],
        'Rongmei': ['tunapui',]
    },
    'man': {
        'Lotha': ['aboe'],
        'Rongmei': ['gan']
    },
    'woman': {
        'Lotha': ['eloe'],
        'Rongmei': ['tuna']
    },
    'child': {
        'Lotha': ['ngaro'],
        'Rongmei': ['naa','kanaa']
    },
    'children': {
        'Lotha': ['ngaro'],
        'Rongmei': ['naa nhoon']
    },
    'grandpa': {
        'Lotha': ['amotsu'],
        'Rongmei': ['apao']
    },
    'grandma': {
        'Lotha': ['atsu'],
        'Rongmei': ['apai']
    },
    'grandfather': {
        'Lotha': ['amotsu'],
        'Rongmei': ['apao']
    },
    'grandmother': {
        'Lotha': ['atsu'],
        'Rongmei': ['apai']
    },
    'uncle': {
        'Lotha': ['amo'],
        'Rongmei': ['Patoun']
    },
    'aunty': {
        'Lotha': ['ano'],
        'Rongmei': ['Anai']
    },
    'brother': {
        'Lotha': ['ata'],
        'Rongmei': ['Abung']
    },
    'sister': {
        'Lotha': ['ata'],
        'Rongmei': ['Api']
    },
    'elder': {
        'Lotha': ['eramoe'],
        'Rongmei': ['Ganthao']
    },
    'old': {
        'Lotha': ['eson'],
        'Rongmei': ['Ganthao']
    },
    'young': {
        'Lotha': ['nunghori'],
        'Rongmei': ['Galao']
    },
    'eldest': {
        'Lotha': ['eramoe'],
        'Rongmei': ['Ganthao liang mei']
    },
    'youngest': {
        'Lotha': ['nunghori'],
        'Rongmei': ['Galao Liang mei ']
    },
    'grand children': {
        'Lotha': ['ori'],
        'Rongmei': ['Katao']
    },
    'Grandchild': {
        'Lotha': ['ori'],
        'Rongmei': ['Katao']
    },
    'Grandson': {
        'Lotha': ['ori'],
        'Rongmei': ['Katao ganmei']
    },
    'Grand daughter': {
        'Lotha': ['ori'],
        'Rongmei': ['katao tunapui']
    },
    'Husband': {
        'Lotha': ['mmyu mongkhum'],
        'Rongmei': ['kagan']
    },
    'Wife': {
        'Lotha': ['enya mongkhum'],
        'Rongmei': ['Kanao']
    },
    'Friend': {
        'Lotha': ['enya mongkhum'],
        'Rongmei': ['pam mei',]
    },
    #pronouns
    'Me': {
        'Lotha': ['enya mongkhum'],
        'Rongmei': ['I']
    },
    'You': {
        'Lotha': [''],
        'Rongmei': ['Nung']
    },
    'He': {
        'Lotha': ['enya mongkhum'],
        'Rongmei': ['kamei']
    },
    'She': {
        'Lotha': ['unmhon'],
        'Rongmei': ['kamei']
    },
    'It': {
        'Lotha': ['enya mongkhum'],
        'Rongmei': ['meita']
    },
    'we': {
        'Lotha': ['enya mongkhum'],
        'Rongmei': ['Anhu']
    },
    'today': {
        'Lotha': ['enya mongkhum'],
        'Rongmei': ['asai']
    },
    'is': {
        'Lotha': ['enya mongkhum'],
        'Rongmei': ['ha']
    },
    '5': {
        'Lotha': ['enya mongkhum'],
        'Rongmei': ['pa un']
    },
    'our': {
        'Lotha': ['enya mongkhum'],
        'Rongmei': ['anhu tong']
    },
    'their': {
        'Lotha': ['enya mongkhum'],
        'Rongmei': ['kanhu tong']
    },
    'I': {
        'Lotha': ['enya mongkhum'],
        'Rongmei': ['I']
    },
    'his': {
        'Lotha': ['enya mongkhum'],
        'Rongmei': ['katong']
    },
    'her': {
        'Lotha': ['enya mongkhum'],
        'Rongmei': ['katong']
    },
    "oneself": {
        "Lotha": [" "],
        "Rongmei": [" "]
    },
    "one": {
        "Lotha": [" "],
        "Rongmei": ["khat"]
    },
    "this": {
        "Lotha": [" "],
        "Rongmei": ["meiha"]
    },
    "that": {
        "Lotha": [" "],
        "Rongmei": ["meita"]
    },
    "these": {
        "Lotha": [" "],
        "Rongmei": ["meinhunha"]
    },
    "those": {
        "Lotha": [" "],
        "Rongmei": [""]
    },
    "somebody": {
        "Lotha": [" "],
        "Rongmei": [" "]
    },
    "my": {
        "Lotha": [" "],
        "Rongmei": [" "]
    },
    "name": {
        "Lotha": [" "],
        "Rongmei": [" "]
    },
    "anybody": {
        "Lotha": [" "],
        "Rongmei": [" "]
    },
    "anyone": {
        "Lotha": [" "],
        "Rongmei": [" "]
    },
    "anything": {
        "Lotha": [" "],
        "Rongmei": [" "]
    },
    "nobody": {
        "Lotha": [" "],
        "Rongmei": [" "]
    },
    "no one": {
        "Lotha": [" "],
        "Rongmei": [" "]
    },
    "nothing": {
        "Lotha": [" "],
        "Rongmei": [" "]
    },
    "each": {
        "Lotha": [" "],
        "Rongmei": [" "]
    },
    "either": {
        "Lotha": [" "],
        "Rongmei": [" "]
    },
    "neither": {
        "Lotha": [" "],
        "Rongmei": [" "]
    },
    "all": {
        "Lotha": [" "],
        "Rongmei": [" "]
    },
    "both": {
        "Lotha": [" "],
        "Rongmei": [" "]
    },
    "few": {
        "Lotha": [" "],
        "Rongmei": [" "]
    },
    "many": {
        "Lotha": [" "],
        "Rongmei": [" "]
    },
    "several": {
        "Lotha": [" "],
        "Rongmei": [" "]
    },
    "some": {
        "Lotha": [" "],
        "Rongmei": [" "]
    },
    "others": {
        "Lotha": [" "],
        "Rongmei": [" "]
    },
    "anybody": {
        "Lotha": [" "],
        "Rongmei": [" "]
    },
    "everyone": {
        "Lotha": [" "],
        "Rongmei": [" "]
    },
    "everything": {
        "Lotha": [" "],
        "Rongmei": [" "]
    },
    "somebody": {
        "Lotha": [" "],
        "Rongmei": [" "]
    },
    "someone": {
        "Lotha": [" "],
        "Rongmei": [" "]
    },
    "something": {
        "Lotha": [" "],
        "Rongmei": [" "]
    },
    "nobody": {
        "Lotha": [" "],
        "Rongmei": [" "]
    },
    "nothing": {
        "Lotha": [" "],
        "Rongmei": [" "]
    },
    "anyone": {
        "Lotha": [" "],
        "Rongmei": [" "]
    },
    "anything": {
        "Lotha": [" "],
        "Rongmei": [" "]
    },
    "love": {
        "Lotha": [" "],
        "Rongmei": ["jian ae"]
    },
    "cold": {
        "Lotha": [" "],
        "Rongmei": ["chumei"]
    },
    "snacks": {
        "Lotha": [" "],
        "Rongmei": ["achapot"]
    },
    "ice cream": {
        "Lotha": [" "],
        "Rongmei": [" ice cream "]
    },

    'is': {
        'Lotha': ['enya mongkhum'],
        'Rongmei': ['ha']
    },
    'Youngest': {
        'Lotha': ['enya mongkhum'],
        'Rongmei': ['Galao Liang mei ']
    },
    'Grand Children': {
        'Lotha': ['enya mongkhum'],
        'Rongmei': ['Katao']
    },
    'Grandchild': {
        'Lotha': ['enya mongkhum'],
        'Rongmei': ['Katao']
    },
    'Grandson': {
        'Lotha': ['enya mongkhum'],
        'Rongmei': ['Katao ganmei']
    },
    'Grand daughter': {
        'Lotha': ['mmyu mongkhum'],
        'Rongmei': ['katao tunapui']
    },
    'girl': {
        'Lotha': ['mmyu mongkhum'],
        'Rongmei': ['ganmei']
    },
    
    # Add more translations here
}