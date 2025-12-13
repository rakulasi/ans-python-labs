import unittest

from rk2_refactored import (
    orchestras,
    pieces,
    pieces_orchestras,
    task_1,
    task_2,
    task_3,
)


class TestRk2Tasks(unittest.TestCase):
    def test_task_1_order_and_length(self):
        """Задание 1: проверяем количество элементов и сортировку по имени оркестра."""
        res = task_1(orchestras, pieces)
        # всего произведений столько же, сколько pieces
        self.assertEqual(len(res), len(pieces))
        # проверяем, что список отсортирован по названию оркестра (3-й элемент кортежа)
        orch_names = [item[2] for item in res]
        self.assertEqual(orch_names, sorted(orch_names))

    def test_task_2_total_duration(self):
        """Задание 2: проверяем суммарную длительность репертуара одного оркестра."""
        res = dict(task_2(orchestras, pieces))
        # для Гётеборгского оркестра должны суммироваться длительности 5, 12 и 3 -> 20
        self.assertIn('Гётеборгский симфонический оркестр', res)
        self.assertEqual(res['Гётеборгский симфонический оркестр'], 5 + 12 + 3)

    def test_task_3_berlin_orchestra(self):
        """Задание 3: проверяем список произведений для оркестра со словом 'Берлинский'."""
        res = task_3(orchestras, pieces, pieces_orchestras)
        name = 'Берлинский филармонический оркестр'
        self.assertIn(name, res)
        # У берлинского оркестра по данным связей должны быть два произведения
        self.assertEqual(sorted(res[name]), sorted([
            'Времена года (Вивальди)',
            'Симфония №4 (Бетховен)',
        ]))


if __name__ == '__main__':
    unittest.main()
