from collections import deque
def check_palindrome(string):
   # Видаляємо пробіли та переводимо в нижній регістр
   string = string.replace(' ', '').lower()

   # Створюємо двосторонню чергу
   char_deque = deque(string)
 
   # Порівнюємо символи з обох кінців черги
   while len(char_deque) > 1: 
       # Якщо символи співпадають, видаляємо їх   
       if char_deque[0] == char_deque[-1]:
           char_deque.popleft()
           char_deque.pop()
       else: 
           return "This is not a palindrome"      
   return "This is a palindrome"

# Перевірка функції
print(check_palindrome("A man a plan a canal Panama"))
print(check_palindrome("hell"))
print(check_palindrome("racecar"))
print(check_palindrome("noon"))                         
print(check_palindrome("Was it a car or a cat I saw")) 
print(check_palindrome("Never odd or even"))            