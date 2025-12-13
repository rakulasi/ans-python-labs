from operator import itemgetter


class MusicalPiece:
    def __init__(self, id, title, duration_min, orchestra_id):
        self.id = id
        self.title = title
        self.duration_min = duration_min
        self.orchestra_id = orchestra_id


class Orchestra:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class PieceOrchestra:
    def __init__(self, orchestra_id, piece_id):
        self.orchestra_id = orchestra_id
        self.piece_id = piece_id


orchestras = [
    Orchestra(1, 'БСО им. П. И. Чайковского'),
    Orchestra(2, 'Берлинский филармонический оркестр'),
    Orchestra(3, 'Гётеборгский симфонический оркестр'),
]

pieces = [
    MusicalPiece(1, 'Симфония №4 (Бетховен)', 40, 1),
    MusicalPiece(2, 'Времена года (Вивальди)', 42, 2),
    MusicalPiece(3, 'Иберия (Дебюсси)', 5, 3),
    MusicalPiece(4, 'Половецкие пляски (Бородин)', 12, 3),
    MusicalPiece(5, 'Рассвет на Москве-реке (Мусоргский)', 3, 3),
]

pieces_orchestras = [
    PieceOrchestra(1, 1),
    PieceOrchestra(2, 2),
    PieceOrchestra(3, 3),
    PieceOrchestra(3, 4),
    PieceOrchestra(3, 5),
    PieceOrchestra(2, 1),
]


def build_one_to_many(orchestras_list, pieces_list):
    """Связь 1:M: произведение -> оркестр, как в задании 1."""
    return [
        (p.title, p.duration_min, o.name)
        for o in orchestras_list
        for p in pieces_list
        if p.orchestra_id == o.id
    ]


def build_many_to_many(orchestras_list, pieces_list, links):
    """Связь M:M: произведение <-> оркестр, как в задании 3."""
    many_to_many_temp = [
        (o.name, po.orchestra_id, po.piece_id)
        for o in orchestras_list
        for po in links
        if o.id == po.orchestra_id
    ]
    return [
        (p.title, p.duration_min, orch_name)
        for orch_name, orch_id, piece_id in many_to_many_temp
        for p in pieces_list
        if p.id == piece_id
    ]


def task_1(orchestras_list, pieces_list):
    """Список произведений по оркестрам (1:M), отсортированный по имени оркестра."""
    one_to_many = build_one_to_many(orchestras_list, pieces_list)
    return sorted(one_to_many, key=itemgetter(2))


def task_2(orchestras_list, pieces_list):
    """Суммарная длительность репертуара по оркестрам, по убыванию суммы."""
    one_to_many = build_one_to_many(orchestras_list, pieces_list)

    res_unsorted = []
    for o in orchestras_list:
        o_pieces = list(filter(lambda i: i[2] == o.name, one_to_many))
        if o_pieces:
            durations = [duration for _, duration, _ in o_pieces]
            res_unsorted.append((o.name, sum(durations)))

    return sorted(res_unsorted, key=itemgetter(1), reverse=True)


def task_3(orchestras_list, pieces_list, links, keyword='Берлинский'):
    """
    Произведения в оркестрах, в имени которых есть заданное слово (по умолчанию 'Берлинский').
    Связь M:M.
    """
    many_to_many = build_many_to_many(orchestras_list, pieces_list, links)
    result = {}
    for o in orchestras_list:
        if keyword in o.name:
            o_pieces = list(filter(lambda i: i[2] == o.name, many_to_many))
            titles = [title for title, _, _ in o_pieces]
            result[o.name] = titles
    return result


def main():
    res_1 = task_1(orchestras, pieces)
    print('Задание 1:', res_1)

    res_2 = task_2(orchestras, pieces)
    print('Задание 2:', res_2)

    res_3 = task_3(orchestras, pieces, pieces_orchestras)
    print('Задание 3:', res_3)


if __name__ == '__main__':
    main()
