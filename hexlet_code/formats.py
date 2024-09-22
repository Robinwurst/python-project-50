from hexlet_code.formats import stylish


def formating(diff, format_):
    if format_ == 'stylish':
        return stylish.stylish(diff)
    elif format_ == 'plain':
        return plain.plain(diff)