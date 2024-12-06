from django.test import TestCase
from rest_framework.test import APIClient
from .models import Todo
from django.urls import reverse

class TodoTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.todo_data = {
            'title': 'Test Todo',
            'description': 'Test Description',
            'status': 'OPEN'
        }
        self.todo = Todo.objects.create(**self.todo_data)
        self.url = reverse('todo-list-create')

    def test_create_todo(self):
        response = self.client.post(self.url, self.todo_data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_read_todo_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_update_todo(self):
        update_data = {'status': 'COMPLETED'}
        response = self.client.put(reverse('todo-retrieve-update-destroy', kwargs={'pk': self.todo.id}),
                                   update_data, format='json')
        self.assertEqual(response.status_code, 200)

    def test_delete_todo(self):
        response = self.client.delete(reverse('todo-retrieve-update-destroy', kwargs={'pk': self.todo.id}))
        self.assertEqual(response.status_code, 204)

