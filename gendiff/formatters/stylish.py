INDENT = ' '
SPACES_COUNT = 4


def build_stylish(diff, depth=0):
    result = ['{']
    offset = depth + SPACES_COUNT
    for node in diff:

        key, type = node.get('key'), node.get('type')
        value, new_value = node.get('value'), node.get('new_value')
        value_str = format_value_deep(value, depth)
        new_value_str = format_value_deep(new_value, depth)

        spaces = INDENT * (offset - 2)

        added = f'{spaces}+ {key}: {value_str}'
        removed = f'{spaces}- {key}: {value_str}'
        samed = f'{spaces}  {key}: {value_str}'
        changed = f'{spaces}+ {key}: {new_value_str}'

        if type == 'add':
            result.append(added)
        elif type == 'remove':
            result.append(removed)
        elif type == 'same':
            result.append(samed)
        elif type == 'change':
            result.append(removed)
            result.append(changed)
        elif type == 'children':
            result.append(f'{INDENT * offset}{key}: '
                          + build_stylish(value, offset))

    result.append(f'{INDENT * depth + "}"}')
    return '\n'.join(result)


def format_value_deep(value, depth):
    if not isinstance(value, dict):
        return make_value_to_string_stylish(value)
    lines = ['{']
    for key in value.keys():
        current = value[key]
        format_key = f'{INDENT * (depth + SPACES_COUNT * 2)}{key}: '
        if isinstance(current, dict):
            lines.append(format_key
                         + format_value_deep(current, depth + SPACES_COUNT))
        else:
            lines.append(format_key + make_value_to_string_stylish(current))
    lines.append(f'{INDENT * (depth + SPACES_COUNT) + "}"}')
    return '\n'.join(lines)


def make_value_to_string_stylish(string_value):
    if isinstance(string_value, bool):
        return str(string_value).lower()
    elif string_value is None:
        return "null"
    else:
        return str(string_value)
