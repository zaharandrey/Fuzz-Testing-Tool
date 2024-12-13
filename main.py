import random
import string
import logging

# Налаштування логування
logging.basicConfig(
    filename="fuzz_testing.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def generate_random_string(min_len=0, max_len=100):
    """Генерує випадковий рядок із заданою довжиною."""
    length = random.randint(min_len, max_len)
    return ''.join(random.choices(string.printable, k=length))


def fuzz_test(function_to_test, iterations=1000):
    """Виконує fuzz-тестування заданої функції."""
    for i in range(iterations):
        test_input = generate_random_string()
        try:
            result = function_to_test(test_input)

            # Якщо потрібно, можна додати перевірки очікуваної поведінки функції
            if not isinstance(result, (str, int, float, list, dict, type(None))):
                logging.warning(
                    f"Unexpected return type: Input: {test_input}, Result: {result}"
                )

        except Exception as e:
            logging.error(f"Crash: Input: {test_input}, Error: {e}")


# Приклад функції для тестування
def example_function(input_str):
    """Приклад функції, яка може бути протестована."""
    if not isinstance(input_str, str):
        raise ValueError("Input must be a string")

    # Емулюємо випадкову помилку
    if len(input_str) > 50 and random.random() < 0.1:
        raise RuntimeError("Random failure for long input")

    return input_str[::-1]  # Повертає рядок у зворотному порядку


# Запуск fuzz-тестування
if __name__ == "__main__":
    fuzz_test(example_function, iterations=1000)

