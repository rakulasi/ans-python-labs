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

def main():
    one_to_many = [(p.title, p.duration_min, o.name)
                   for o in orchestras
                   for p in pieces
                   if p.orchestra_id == o.id]
    
    many_to_many_temp = [(o.name, po.orchestra_id, po.piece_id)
                         for o in orchestras
                         for po in pieces_orchestras
                         if o.id == po.orchestra_id]
    
    many_to_many = [(p.title, p.duration_min, orch_name)
                    for orch_name, orch_id, piece_id in many_to_many_temp
                    for p in pieces if p.id == piece_id]

    print('Задание 1: Список произведений по оркестрам (связь 1:M)')
    res_1 = sorted(one_to_many, key=itemgetter(2))
    print(res_1)
    
    print('\nЗадание 2: Суммарная длительность репертуара по оркестрам (связь 1:M)')
    res_2_unsorted = []
    for o in orchestras:
        o_pieces = list(filter(lambda i: i[2] == o.name, one_to_many))
        if len(o_pieces) > 0:
            o_durations = [duration for _, duration, _ in o_pieces]
            o_durations_sum = sum(o_durations)
            res_2_unsorted.append((o.name, o_durations_sum))

    res_2 = sorted(res_2_unsorted, key=itemgetter(1), reverse=True)
    print(res_2)

    print('\nЗадание 3 (доп.): Произведения в оркестрах со словом "Берлинский" (связь M:M)')
    res_3 = {}
    for o in orchestras:
        if 'Берлинский' in o.name:
            o_pieces = list(filter(lambda i: i[2] == o.name, many_to_many))
            o_titles = [title for title, _, _ in o_pieces]
            res_3[o.name] = o_titles
    print(res_3)

if __name__ == '__main__':
    main()
