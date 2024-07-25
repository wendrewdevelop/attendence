import unicodedata


def remove_accent(text):
    """Remove acentos e normaliza o texto."""
    return ''.join(c for c in unicodedata.normalize('NFD', text)
                   if unicodedata.category(c) != 'Mn')