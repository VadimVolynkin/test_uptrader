from django import template
from menu.models import MenuItem, Menu
from .menu_func import get_childs_ids, get_parents_ids, get_current_item

register = template.Library()

from copy import deepcopy


@register.inclusion_tag('menu/tags/menu.html', takes_context=True)
def get_menu(context, name):
    """
    Тег выводит меню по названию.
    """
    # все пункты меню
    menu_items = MenuItem.objects.filter(menu__name=name).values()
    # абсолютный путь текущей страницы
    current_uri = context['request'].build_absolute_uri()
    # активный пункт меню
    active_item_menu = get_current_item(menu_items, current_uri)
    # поиск детей на первом уровне меню
    childs = get_childs_ids(active_item_menu, menu_items)
    # получение цепочки родителей
    parents = get_parents_ids(active_item_menu, menu_items)
    # контекст
    request = context['request']
    return {
        'menu': menu_items,
        'parents': parents,
        'childs': childs,
        'request': request
    }