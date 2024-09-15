from django.test import TestCase
from restaurant import models


class MenuTest(TestCase):
    def test_get_item(self):
        item = models.MenuItem.objects.create(
            title="IceCream", price=80, inventory=100)
        the_string = str(item)
        self.assertEqual(the_string, "IceCream : 80")
