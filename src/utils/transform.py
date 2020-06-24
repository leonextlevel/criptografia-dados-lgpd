def normalize_key(key):
    key = ' '.join(map(str.capitalize, key.split('_')))
    return key