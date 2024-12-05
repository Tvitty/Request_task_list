from moduls import Tasks
import commands as c

def main():
    c.print_all_commands(c.Name.all_commands)
    task  = Tasks()
    command = input('Введите команду: ').lower()
    while command != 'выход':

        match command:
            case c.Name.create_a_task:
                task.add_task(
                    name=input('Название задачи: '),
                    description=input('Описание задачи: '),
                    category=input('Категория задачи: '),
                    deadline=input('Дата окончания в формате ГГГГ-ММ-ДД: '),
                    priority=input('Приоритет задачи (низкий, средний, высокий): ')
                )
            case c.Name.task_view:
                task.get_all_tasks()
            case c.Name.categorize_tasks:
                task.get_tasks_by_category(category=input('Введите категорию: '))
            case c.Name.task_edit:
                task.task_editing(
                    id_task=input('Введите номер задачи: '),
                    what_to_edit=input('Введите поле для редактирования (name, description, category, deadline, priority): '),
                    new_value=input('Введите новое значение: ')
                )
            case c.Name.check_in:
                task.task_as_completed(id_task=input('Введите номер задачи: '))
            case c.Name.delete_task:
                task.deleting_a_task(id_task=input('Введите номер задачи: '))
            case c.Name.task_search:
                task.task_searh(value_search=input('Введите ключевое слово, категорию или статус задачи: '))
            case c.Name.help_me:
                c.print_all_commands(c.Name.all_commands)
            case _:
                print('К сожаления я не знаю такой команды.')

        command = input('Введите команду: ').lower()

if __name__ == '__main__':
    main()