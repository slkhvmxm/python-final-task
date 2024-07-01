import csv
def read_file(filename: str) -> list[dict]:
    """Читает данные из CSV файла и преобразует их в список словарей.

    :param filename: Название файла, содержащего данные.
    :return: Список словарей с данными о домах.
    """

    with open(filename, encoding='utf-8') as file:  # Файл читаем в кодировке utf-8
        reader = csv.DictReader(file)
        houses = list(reader)
        for house in houses:
            # Преобразовываем в соответсвующие типы: int, float
            house['floor_count'] = int(house['floor_count'])
            house['heating_value'] = float(house['heating_value'])
            house['area_residential'] = float(house['area_residential'])
            house['population'] = int(house['population'])
    return houses


def classify_house(floor_count: int) -> str:
    """Классифицирует дом на основе количества этажей.

    Проверяет, является ли количество этажей целым числом и положительным значением.
    Возвращает категорию дома в зависимости от количества этажей.

    :param floor_count: Количество этажей в доме.
    :return: Категория дома в виде строки: "Малоэтажный", "Среднеэтажный" или "Многоэтажный".
    """
    if not isinstance(floor_count, int):
        raise TypeError(f"floor_count имеет тип {type(floor_count)}, должен быть типа int")
    if floor_count <= 0:
        raise ValueError("Число должно быть положительным.")
    # Проверяем диапазоны домов: Малоэтажный, Среднеэтажный, Многоэтажный
    if floor_count in range(1, 6):  #
        return 'Малоэтажный'
    elif floor_count in range(6, 17):
        return 'Среднеэтажный'
    else:
        return 'Многоэтажный'


def get_classify_houses(houses: list[dict]) -> list[str]:
    """Классифицирует дома на основе количества этажей.

    :param houses: Список словарей с данными о домах.
    :return: Список категорий домов.
    """
    categories = [classify_house(house['floor_count']) for house in houses]
    return categories


def get_count_house_categories(categories: list[str]) -> dict[str, int]:
    """
    Подсчитывает количество домов в каждой категории.

    :param categories: Список категорий домов.
    :return: Словарь с количеством домов в каждой категории.
    """
    keys = set(categories)
    count_house_categories = {}
    for category in keys:
        count_house_categories[category] = categories.count(category)
    return count_house_categories


def min_area_residential(houses: list[dict]) -> str:
    """Находит адрес дома с наименьшим средним количеством квадратных метров жилой площади на одного жильца.

    :param houses: Список словарей с данными о домах.
    :return: Адрес дома с наименьшим средним количеством квадратных метров жилой площади на одного жильца.
    """
    average_area = [house['area_residential'] / house['population'] for house in houses]
    min_area = min(average_area)
    index = average_area.index(min_area)
    address = houses[index]['house_address']
    return address


if __name__ == '__main__':
    data_list = read_file('housing_data.csv')
    all_categories = get_classify_houses(data_list)
    print(all_categories)

    count_dict = get_count_house_categories(all_categories)
    print("Количество домов по категориям:")
    print(count_dict)

    min_area_address = min_area_residential(data_list)
    print("Адрес дома с наименьшей площадью на одного жителя:")
    print(min_area_address)
