import pytest


@pytest.mark.parametrize("cook_book, person, expected", [
    (
            [
                ['Салат', [
                    ['картофель', 100, 'гр.'],
                    ['морковь', 50, 'гр.'],
                    ['огурцы', 50, 'гр.'],
                    ['горошек', 30, 'гр.'],
                    ['майонез', 70, 'мл.'],
                ]],
                ['Пицца', [
                    ['сыр', 50, 'гр.'],
                    ['томаты', 50, 'гр.'],
                    ['тесто', 100, 'гр.'],
                    ['бекон', 30, 'гр.'],
                    ['колбаса', 30, 'гр.'],
                    ['грибы', 20, 'гр.'],
                ]],
                ['Фруктовый десерт', [
                    ['хурма', 60, 'гр.'],
                    ['киви', 60, 'гр.'],
                    ['творог', 60, 'гр.'],
                    ['сахар', 10, 'гр.'],
                    ['мед', 50, 'мл.'],
                ]]
            ],
            5,
            [
                'Салат: картофель 500 гр., морковь 250 гр., огурцы 250 гр., горошек 150 гр., майонез 350 мл.',
                'Пицца: сыр 250 гр., томаты 250 гр., тесто 500 гр., бекон 150 гр., колбаса 150 гр., грибы 100 гр.',
                'Фруктовый десерт: хурма 300 гр., киви 300 гр., творог 300 гр., сахар 50 гр., мед 250 мл.'
            ]
    ),
    (
            [
                ['Омлет', [
                    ['яйца', 2, 'шт.'],
                    ['молоко', 100, 'мл.'],
                    ['соль', 1, 'гр.'],
                ]],
            ],
            3,
            [
                'Омлет: яйца 6 шт., молоко 300 мл., соль 3 гр.'
            ]
    ),
    (
            [
                ['Суп', [
                    ['вода', 1000, 'мл.'],
                    ['картофель', 200, 'гр.'],
                    ['морковь', 100, 'гр.'],
                    ['лук', 50, 'гр.'],
                    ['соль', 5, 'гр.'],
                ]],
                ['Компот', [
                    ['вода', 1500, 'мл.'],
                    ['сахар', 100, 'гр.'],
                    ['яблоки', 200, 'гр.'],
                    ['груши', 200, 'гр.'],
                ]]
            ],
            2,
            [
                'Суп: вода 2000 мл., картофель 400 гр., морковь 200 гр., лук 100 гр., соль 10 гр.',
                'Компот: вода 3000 мл., сахар 200 гр., яблоки 400 гр., груши 400 гр.'
            ]
    )
])
def test_solve(cook_book, person, expected):
    from cookbook_02 import solve
    assert solve(cook_book, person) == expected