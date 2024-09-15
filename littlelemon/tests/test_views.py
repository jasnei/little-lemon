from random import randint

from django.test import TestCase
from django.urls import resolve, reverse
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer
from restaurant.views import MenuItemView

MENU_ITEMS = {
    1: {'title': 'ApplePie',     'price': 13.78, 'inventory': randint(1, 10)},
    2: {'title': 'VanillaLatte', 'price': 3.99,  'inventory': randint(1, 10)},
    3: {'title': 'Icecream',     'price': 5.00,  'inventory': randint(1, 10)},
    4: {'title': 'IrishCoffe',   'price': 7.89,  'inventory': randint(1, 10)},
}


class MenuViewTest(TestCase):
    items = MENU_ITEMS

    def set_up(self) -> None:
        # Create menu items
        for i in self.items.keys():
            item = MenuItem.objects.create(
                title=self.items[i]['title'],
                price=self.items[i]['price'],
                inventory=self.items[i]['inventory'],
            )
            item.save()  # TODO: Why?

        return super().setUp()

    def test_get_all(self):
        # Does 'menu-items' connect to MenuItemsView?
        url = reverse('menu-items')
        print(f'url: {url}')
        self.assertEqual(resolve(url).func.view_class, MenuItemView)

        response = self.client.get(reverse('menu-items'))
        print(f'response.data: {response.data}')
        serializer = MenuItemSerializer(MenuItem.objects.all(), many=True)
        self.assertEqual(response.status_code, 200)
#       self.assertEqual(response.data, serializer.data)
