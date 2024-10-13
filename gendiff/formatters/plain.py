def plain(diff, path=''):
    result = []
    for node in diff:

        key, type = node.get('key'), node.get('type')
        value, new_value = node.get('value'), node.get('new_value')
        value_str = value_to_string(value)
        new_value_str = value_to_string(new_value)

        new_path = key if path == '' else f'{path}.{key}'
        added = f"Property '{new_path}' was added with value: {value_str}"
        removed = f"Property '{new_path}' was removed"
        changed = f"Property '{new_path}' was updated. " \
                  + f"From {value_str} to {new_value_str}"

        if type == 'add':
            result.append(added)
        elif type == 'remove':
            result.append(removed)
        elif type == 'change':
            result.append(changed)
        elif type == 'children':
            result.append(plain(value, new_path))
    return '\n'.join(result)


def value_to_string(value):
    if isinstance(value, dict):
        return '[complex value]'

    new_value = f"'{value}'" if isinstance(value, str) else value

    if isinstance(new_value, bool):
        return str(new_value).lower()
    elif new_value is None:
        return "null"
    else:
        return str(new_value)
