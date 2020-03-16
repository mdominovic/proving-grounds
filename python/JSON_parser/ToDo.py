class ToDo:
    def __init__(self, todo_list, userId):
        self.userId = userId
        self.completed_list = list()
        self.uncompleted_list = list()
        self.get_data_from_list(todo_list)

    def get_data_from_list(self, todo_list):
        for item in todo_list:
            if item['userId'] == self.userId and item['completed'] == True:
                self.completed_list.append({'id': item['id'],
                                            'title': item['title']})
            elif item['userId'] == self.userId and item['completed'] == False:
                    self.uncompleted_list.append({'id': item['id'],
                                                  'title': item['title']})
