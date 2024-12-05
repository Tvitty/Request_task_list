from src.task_list.moduls import Tasks
import data


class TestsTask:
    'Класс для unit-test'


    def test_add_task(self, task_data):
        test = Tasks()

        test.add_task(*task_data)

        assert test.read_data_json()[str(test.get_task_id())] == data.test_data


    def test_task_as_completed(self):
        test = Tasks()

        test.task_as_completed(str(test.get_task_id()))

        assert test.read_data_json()[str(test.get_task_id())]['статус'] == 'выполнена'


    def test_deleting_a_task(self):
        test = Tasks()

        last_id = test.get_task_id()
        test.deleting_a_task(str(last_id))

        assert last_id not in test.read_data_json()
