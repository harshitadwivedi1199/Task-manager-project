class TaskManager:
    def __init__(self):
        self.tasks = []
        self.counter = 1

    def get_all_tasks(self):
        return self.tasks

    def create_task(self, title):
        task = {'id': self.counter, 'title': title}
        self.tasks.append(task)
        self.counter += 1
        return task

    def get_task(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                return task
        return None

    def update_task(self, task_id, data):
        for task in self.tasks:
            if task['id'] == task_id:
                task['title'] = data['title']
                return task
        return None

    def delete_task(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                self.tasks.remove(task)
                return True
        return False
