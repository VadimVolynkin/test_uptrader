def get_current_item(menu_items, current_uri):
    """
    Функция вернет текущий элемент меню, если этот пункт есть в меню
    Иначе вернет None.
    """
    for item in menu_items:
        if item['url'] == current_uri:
            return item

def get_childs_ids(active_item_menu, menu_items):
    """
    Вернет список детей 1-го уровня
    """
    lst_child_ids = []
    if active_item_menu:
        for item in menu_items:
            if item['parent_id'] and item['parent_id'] == active_item_menu['id']:
                lst_child_ids.append(item['id'])
    return lst_child_ids


def get_parents_ids(active_item_menu, menu_items):
    """
    Вернет цепочку родителей в виде списка.
    """
    lst_parents = []
    while active_item_menu and active_item_menu.get('parent_id'):
        lst_parents.append(active_item_menu['parent_id'])
        for item in menu_items:
            if item['id'] == active_item_menu['parent_id']:
                active_item_menu = item
    return lst_parents
