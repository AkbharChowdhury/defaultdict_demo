from collections import defaultdict, Counter
from typing import Any


def fruits_example() -> defaultdict[Any, list]:
    fruits: list[str] = [
        'apple',
        'banana',
        'carrot',
        'avocado',
        'broccoli',
        'orange',
        'grapes',
        'pear',
        'peach',
        'pineapple',
    ]
    grouped_fruits = defaultdict(list)
    for fruit in fruits:
        grouped_fruits[fruit[0].lower()].append(fruit)
    return grouped_fruits


def adding():
    food_dairy = [
        ('eggs', 3),
        ('bread', 4),
        ('rice', 1),
        ('chicken', 1),
        ('eggs', 2),
        ('bread', 2),
        ('rice', 1),
        ('lamb chops', 1),

    ]
    grouped_data = defaultdict(list)
    for k, v in food_dairy:
        grouped_data[k].append(v)
    print(dict(sorted(grouped_data.items())))
    sum_data = {k: sum(v) for k, v in grouped_data.items()}
    sum_data_desc = dict(sorted(sum_data.items(), key=lambda item: item[1]))
    sum_data_asc = dict(sorted(sum_data.items(), key=lambda item: item[1], reverse=True))
    grouped_data_sorted_by_key = dict(sorted(sum_data.items()))
    print(f'{sum_data_desc=}')
    print(f'{sum_data_asc=}')
    print(f'{grouped_data_sorted_by_key=}')


def main():
    print(fruits_example())
    adding()

if __name__ == "__main__":
    main()
