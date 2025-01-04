import time
import math
from datetime import datetime
from zadanie38 import bubble_sort, insertion_sort, quick_sort, sorting_data


def measure_sorting_time(sorting_func):
    data_copy = sorting_data.copy()

    start_time = time.time()
    sorting_func(data_copy)
    end_time = time.time()

    return (end_time - start_time) * 1000


def calculate_mean(numbers):
    return sum(numbers) / len(numbers) if numbers else 0


def calculate_std_dev(numbers):
    if not numbers:
        return 0

    mean = calculate_mean(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return math.sqrt(variance)


def format_time(time_ms):
    if time_ms < 1000:
        return f"{time_ms:.2f} ms"
    else:
        return f"{time_ms / 1000:.4f} s"


def generate_performance_report():
    sorting_algorithms = {
        'bąbelkowe': bubble_sort,
        'wstawianie': insertion_sort,
        'quick sort': quick_sort
    }

    num_iterations = 100

    results = {}
    for name, sort_func in sorting_algorithms.items():
        times = [measure_sorting_time(sort_func) for _ in range(num_iterations)]

        results[name] = {
            'times': times,
            'mean': calculate_mean(times),
            'std_dev': calculate_std_dev(times)
        }

    current_date = datetime.now().strftime("%Y-%m-%d")
    filename = f"raport_{current_date}.txt"

    with open(filename, 'w', encoding='utf-8') as f:
        f.write("RAPORT ALGORYTMÓW SORTOWANIA\n\n")
        f.write("NAZWA -- LICZBA SORTOWANYCH PLIKÓW -- ŚREDNI CZAS -- ODCHYLENIE STANDARDOWE\n\n")

        iterator = 1
        for name, data in results.items():
            f.write(
                f"{iterator}. {name} -- "
                f"{len(sorting_data)} -- "
                f"{format_time(data['mean'])} -- "
                f"{format_time(data['std_dev'])}\n"
            )
            iterator += 1


generate_performance_report()