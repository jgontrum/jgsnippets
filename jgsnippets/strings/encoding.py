def clean_encoding(text):
    if not isinstance(text, str):
        return ""

    mapping = {
        "Ã\u009f": 'ß',
        "Ã¶": 'ö',
        "Ã©": "é",
        "Ã¼": "ü",
        "Ã¤": "ä",
        "&szlig;": 'ß',
        "&auml;": 'ä',
        "&Auml;": 'Ä',
        "&ouml;": 'ö',
        "&Ouml;": 'Ö',
        "&uuml;": 'ü',
        "&Uuml;": 'Ü'
    }

    for bad, good in mapping.items():
        text = text.replace(bad, good)
    return text