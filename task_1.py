from queue import Queue
import time

# Створити чергу заявок
requests_queue = Queue()
request_id = 0

def generate_request():
    global request_id
    request_id += 1
    new_request = f"Request {request_id}"
    requests_queue.put(new_request)
    print(f"Заявка додана: {new_request}")

def process_request():
    if not requests_queue.empty():
        request = requests_queue.get()
        print(f"Обробка {request}...")
        time.sleep(1)  # Імітуємо час обробки заявки
        print(f"{request} оброблена")
    else:
        print("Черга пуста")

def main():
    try:
        user_input = input("Введіть 'q' для виходу або 'Enter' для продовження: ")
        while True:
            if user_input == "q":
                break
            generate_request()
            process_request()
            time.sleep(2)  # Імітуємо час між створенням нових заявок
    except KeyboardInterrupt:
        print("Програма завершена користувачем.")

if __name__ == "__main__":
    main()
