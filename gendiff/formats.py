from gendiff.formating import stylish, make_json, plain


def formating(diff, format_name):
    if format_name == 'stylish':
        return stylish.stylish(diff)
    elif format_name == 'plain':
        return plain.plain(diff)
    elif format_name == 'json':
        return make_json.make_json(diff)
    else:
        raise ValueError('Wrong format')
