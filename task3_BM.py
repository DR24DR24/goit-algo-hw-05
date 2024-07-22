import task3_readfile


def build_shift_table(pattern):
    """Створити таблицю зсувів для алгоритму Боєра-Мура."""
    table = {}
    length = len(pattern)
# Для кожного символу в підрядку встановлюємо зсув рівний довжині підрядка
    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1
# Якщо символу немає в таблиці, зсув буде дорівнювати довжині підрядка
    table.setdefault(pattern[-1], length)
    return table

def boyer_moore_search(text, pattern):
# Створюємо таблицю зсувів для патерну (підрядка)
    shift_table = build_shift_table(pattern)
    i = 0# Ініціалізуємо початковий індекс для основного тексту

# Проходимо по основному тексту, порівнюючи з підрядком
    while i <= len(text) - len(pattern):
        j = len(pattern) - 1# Починаємо з кінця підрядка

# Порівнюємо символи від кінця підрядка до його початку
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1# Зсуваємось до початку підрядка

# Якщо весь підрядок збігається, повертаємо його позицію в тексті
        if j < 0:
            return i# Підрядок знайдено

# Зсуваємо індекс i на основі таблиці зсувів
# Це дозволяє "перестрибувати" над неспівпадаючими частинами тексту
        a=text[i + len(pattern) - 1]
        b=len(pattern) 
        i += shift_table.get(a, b)

# Якщо підрядок не знайдено, повертаємо -1  
    return -1


if __name__=="__main__":
    # text = "Being a developer is not easy"
    # pattern = "developer"

    text = "xababxxx"
    pattern = "xxxxabab"
        
    task3_readfile.test_function(text,pattern,boyer_moore_search)
    
    text=task3_readfile.read_file("стаття 2.txt")

    task3_readfile.test_function(text,"системах. Наявність",boyer_moore_search)

