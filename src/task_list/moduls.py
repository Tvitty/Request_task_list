import json
import pathlib


class DataJson:
    'Класс для работы с файлом'

    def __init__(self):
        self.file = pathlib.Path('task_list/src/config/data.json').resolve()


    def read_data_json(self):    # Чтение файла с задачами
        with open(self.file, 'r', encoding='utf-8') as file:
            tasks = json.load(file)

        return tasks


    def write_to_file(self, task):    # Запись задач в файл
        with open(self.file, 'w', encoding='utf-8') as file:
            json.dump(task, file, indent=4)


    def get_task_id(self):   # Получение id последней задачи
        id_task = list(self.read_data_json().keys())

        if len(id_task) == 0:
            return 0

        return int(id_task[-1])



class Tasks(DataJson):
    'Класс для работы с задачами'

    def __init__(self):
        self.tasks = {}
        self.task_id = 1
        super().__init__()


    def get_all_tasks(self):    # Просмотр всех задач
        if not self.read_data_json():
            print('Список задач пуст.')
        else:
            for task_id, task in self.read_data_json().items():
                print(f'Задача #{task_id}: {task}')


    def get_tasks_by_category(self, category: str):   # Просмотр задач по категориям
        tasks = self.read_data_json()
        if not tasks:
            print('Список задач пуст.')
        else:
            tasks_by_category = {}
            for id_task, task in tasks.items():
                for keys, value in task.items():
                    if keys == 'категория' and value == category.lower():
                        tasks_by_category[id_task] = tasks.get(id_task)

            if len(tasks_by_category) == 0:
                print('Задач с данной категорией нет.')
            else:
                for key, value in tasks_by_category.items():
                    print(f'Задача #{key}: {value}')

    def add_task(self, name: str,    # Создание задачи
                 description: str,
                 category: str,
                 deadline: str,
                 priority: str):
        self.tasks = self.read_data_json()
        self.task_id = self.get_task_id()
        self.task_id += 1
        self.tasks[self.task_id] = {'название': name.lower(),
                                      'описание': description.lower(),
                                      'категория': category.lower(),
                                      'срок выполнения': deadline,
                                      'приоритет': priority,
                                      'статус': 'не выполнена'
                                      }
        self.write_to_file(self.tasks)
        print(f'Задача #{self.task_id} с названием {name} создана.')


    def task_editing(self, id_task: str, what_to_edit: str, new_value: str):    # Редактирование задачи
        tasks = self.read_data_json()
        if not tasks:
            print('Список задач пуст.')
        else:
            if id_task in tasks:
                for key, value in tasks.get(id_task).items():
                    if what_to_edit.lower() == key:
                        tasks.get(id_task)[key] = new_value.lower()
                        print('Задача отредактирована.')
            else:
                print('Задачи с таким номером нет.')

            self.write_to_file(tasks)


    def task_as_completed(self, id_task: str):    # Отметить задачу как выполнена
        tasks = self.read_data_json()
        if not tasks:
            print('Список задач пуст.')
        else:
            if id_task in tasks:
                tasks.get(id_task)['статус'] = 'выполнена'
                print('Задача выполнена!')
            else:
                print('Задачи с таким номером нет.')

            self.write_to_file(tasks)


    def deleting_a_task(self, id_task: str):    # Удаление задачи
        tasks = self.read_data_json()
        if not tasks:
            print('Список задач пуст.')
        else:
            if id_task in tasks:
                tasks.pop(id_task)
                print('Задача удалена.')
            else:
                print('Задачи с таким номером нет.')

            self.write_to_file(tasks)


    def task_searh(self, value_search: str):    # Поиск задач
        tasks = self.read_data_json()
        if not tasks:
            print('Список задач пуст.')
        else:
            tasks_by_value = {}
            for id_task, task in tasks.items():
                for value in task.values():
                    if value_search in value:
                        tasks_by_value[id_task] = tasks.get(id_task)
                        break
            if len(tasks_by_value) == 0:
                print('Задач с данным значением нет.')
            else:
                for key, value in tasks_by_value.items():
                    print(f'Задача #{key}: {value}')
