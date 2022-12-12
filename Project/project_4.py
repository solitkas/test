def benchmark(func):
    import time
    from functools import wraps

    @wraps(func)
    def wrapper():
        """
        Декоратор для тайминг-кода
        """
        start = time.monotonic()
        print(func())
        run_time = time.monotonic() - start
        print(f"Время выполнения {run_time:.2f} секунд /ы.")  # :.2f - сколько цифр после запятой 0.00

    return wrapper


@benchmark
def test_func() -> str:
    """
    Создания акронимов
    """
    import time
    word = "Artificial Intelligence"
    text = word.split()
    a = " "
    for i in text:
        a = a + str(i[0]).upper()
    time.sleep(2)
    return a.strip()


if __name__ == '__main__':
    test_func()


