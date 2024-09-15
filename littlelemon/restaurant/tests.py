from django.test import TestCase

from . import models


# Create your tests here.
class MenuItemTest(TestCase):
    def test_get_menu_item(self):
        item = models.MenuItem.objects.create(
            title="IceCream", price=80, inventory=100)
        # print(f'item: {item}, type: {type(item)}')
        self.assertEqual(item.__str__(), "IceCream : 80")

    def test_get_all(self):
        item1 = models.MenuItem.objects.create(
            title="IceCream", price=80.0, inventory=100)
        item2 = models.MenuItem.objects.create(
            title="Chocolate", price=100.0, inventory=50)
        items = models.MenuItem.objects.all()
        # print(f'items: {items}, type: {type(items)}')
        self.assertEqual(len(items), 2)
        self.assertEqual(items[0].__str__(), "IceCream : 80.00")
        self.assertEqual(items[1].__str__(), "Chocolate : 100.00")
