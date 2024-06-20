import pytest

# Тестовые данные
initial_documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "driver license", "number": "5455 028765", "name": "Василий Иванов"},
]

initial_directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


@pytest.mark.parametrize("doc_number, expected", [
    ("2207 876234", "Василий Гупкин"),
    ("11-2", "Геннадий Покемонов"),
    ("10006", "Аристарх Павлов"),
    ("5455 028765", "Василий Иванов"),
    ("12345", "Документ не найден")
])
def test_get_name(doc_number, expected):
    from secretary_03 import get_name
    assert get_name(doc_number, initial_documents) == expected


@pytest.mark.parametrize("doc_number, expected", [
    ("2207 876234", "1"),
    ("11-2", "1"),
    ("10006", "2"),
    ("5455 028765", "1"),
    ("12345", "Полки с таким документом не найдено")
])
def test_get_directory(doc_number, expected):
    from secretary_03 import get_directory
    assert get_directory(doc_number, initial_directories) == expected


def test_add():
    from secretary_03 import add, get_name, get_directory

    documents, directories = add('international passport', '311 020203', 'Александр Пушкин', '3',
                                 initial_documents.copy(), initial_directories.copy())
    assert get_name('311 020203', documents) == 'Александр Пушкин'
    assert get_directory('311 020203', directories) == '3'

    # Проверка добавления на новую полку
    documents, directories = add('id card', '123456', 'Иван Иванов', '4', documents, directories)
    assert get_name('123456', documents) == 'Иван Иванов'
    assert get_directory('123456', directories) == '4'
    assert '4' in directories

    # Проверка добавления на существующую полку
    documents, directories = add('student card', '78910', 'Петр Петров', '2', documents, directories)
    assert get_name('78910', documents) == 'Петр Петров'
    assert get_directory('78910', directories) == '2'
    assert '78910' in directories['2']


if __name__ == '__main__':
    pytest.main(['-vv', '--capture=no']) # Отключил захват терминала, на винде почему-то выводит юникод в терминал.

"""
Несмотря на юникод в терминале, тесты проходят. Скорее всего проще было в линуксе настроить локаль.
export LC_ALL=C.UTF-8
export LANG=C.UTF-8
Или сократить вывод трассировки вот этим чудом pytest --tb=short
Возможно мой venv как-то не так стал работать, не знаю, впервые такое.

"""
