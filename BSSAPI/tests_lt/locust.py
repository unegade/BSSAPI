from locust import HttpLocust, TaskSet


def notify(l):
    json = {
        'ClientName': 'Кириллица',
        'ClientAccount': 'qwe',
        'status': 15,
        'ID': '123',
        'Number': 'qwe',
        'ModifiedBy': 123,
        'extendedMap': {
            'qwe': 'qweeqweqw',
            'qwe2': 'qwe'
        }
    }
    l.client.post('/notify', json=json)


class UserBehavior(TaskSet):
    tasks = {notify: 1}


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 900
    max_wait = 1100
