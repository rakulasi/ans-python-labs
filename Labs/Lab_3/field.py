def field(items, *args):
    assert len(args) > 0
    for item in items:
        if len(args) == 1:
            value = item.get(args[0])
            if value is not None:
                yield value
        else:
            res = {k: item.get(k) for k in args if item.get(k) is not None}
            if res:
                yield res


if __name__ == '__main__':
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'color': None}
    ]

    print(list(field(goods, 'title')))
    print(list(field(goods, 'title', 'price')))
