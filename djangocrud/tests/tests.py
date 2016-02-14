"""Tests for Core app"""
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test import Client

from djangocrud.tests.models import Foo


class CoreTests(TestCase):
    """Core CRUD tests"""
    def setUp(self, **kwargs):
        """Test Setup"""
        self.client = Client()

        user = User.objects.create_user(
            'john_doe',
            'john@company.com',
            '12345')

        self.foo = Foo.objects.create(
            name='supplier1', category='category1', remarks='remarks1')

        content_type = ContentType.objects.get_for_model(Foo)

        permissions = [Permission.objects.get_or_create(
            codename='{}_supplier'.format(permission),
            content_type=content_type)[0] for permission in (
                'view', 'delete', 'change', 'add')]

        user.user_permissions.set(permissions)

        self.client.login(username='john_doe', password='12345')

    def test_index(self):
        """Test main view that lists all models"""
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)

    def test_detail_view(self):
        """Tests for detail view"""
        response = self.client.get(reverse(
            'detail',
            kwargs={'model_name': 'Supplier', 'pk': self.supplier.id}))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'category1')

    def test_list_view(self):
        """Tests for list view"""
        response = self.client.get(reverse(
            'index',
            kwargs={'model_name': 'Supplier'}))

        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context['objects'],
            [repr(self.supplier)])

    def test_delete_view(self):
        """Tests for delete view"""
        response = self.client.post(reverse(
            'delete',
            kwargs={'model_name': 'Supplier', 'pk': self.supplier.id}))

        self.assertRedirects(
            response,
            reverse(
                'index',
                kwargs={'model_name': 'Supplier'}),
            status_code=302,
            target_status_code=200)

        count = Foo.objects.filter(id=self.supplier.id).count()

        self.assertEqual(count, 0)

    def test_create_view(self):
        """Tests for create view"""
        for verb in ('get', 'post'):
            response = getattr(self.client, verb)(reverse(
                'create',
                kwargs={'model_name': 'Supplier'}))

            self.assertEqual(response.context['form']._meta.model, Foo)

        response = self.client.post(reverse(
            'create',
            kwargs={'model_name': 'Supplier'}),
            {'name': 'Jane Smith', 'category': 'PB', 'remarks': 'nothing'})

        self.assertRedirects(
            response,
            reverse(
                'index',
                kwargs={'model_name': 'Supplier'}),
            status_code=302,
            target_status_code=200)

    def test_udpate_view(self):
        """Tests for update view"""
        for verb in ('get', 'post'):
            response = getattr(self.client, verb)(reverse(
                'update',
                kwargs={'model_name': 'Supplier', 'pk': self.supplier.id}))

            self.assertEqual(response.context['form']._meta.model, Foo)

        response = self.client.post(reverse(
            'update',
            kwargs={'model_name': 'Supplier', 'pk': self.supplier.id}),
            {'name': 'Jane Smith', 'category': 'PB', 'remarks': 'nothing'})

        self.assertRedirects(
            response,
            reverse(
                'index',
                kwargs={'model_name': 'Supplier'}),
            status_code=302,
            target_status_code=200)
