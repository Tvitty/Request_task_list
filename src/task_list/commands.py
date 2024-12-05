from enum import Enum


class Name(Enum):

    create_a_task = 'создать'
    task_view = 'посмотреть'
    categorize_tasks = 'категории'
    task_edit = 'редактировать'
    check_in = 'выполнить'
    delete_task = 'удалить'
    task_search = 'поиск'
    help_me = 'список команд'
    exit_tasks = 'выход'

    all_commands = [
        'Список команд:',
        create_a_task,
        task_view,
        categorize_tasks,
        task_edit,
        check_in,
        delete_task,
        task_search,
        help_me,
        exit_tasks,
    ]

def print_all_commands(all_commands: Name) -> None:
     print(*all_commands.value, sep=' | ', end=' | ')
