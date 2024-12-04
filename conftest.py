import pytest


@pytest.fixture
def task_data():
    name = 'тест'
    description = 'тест тест тест'
    category = 'тест'
    deadline = '2021-01-05'
    priority = 'низкий'

    return name, description, category, deadline, priority
