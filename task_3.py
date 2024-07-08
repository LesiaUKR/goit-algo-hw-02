def check_brackets_symmetry(string):
    brackets = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    stack = []
   #  перебираємо кожен символ у рядку
    for char in string:
        # якщо символ є в значеннях словника brackets, то додаємо його в стек
        if char in brackets.values():
            stack.append(char)
            print("stack after append:", stack)
         # якщо символ є в ключах словника brackets, то видаляємо зі стеку
        elif char in brackets.keys():
            if not stack:
                return "Asymmetric"
            top = stack.pop()
            print(f"Matching {brackets[char]} with {char}")
            # якщо верхній елемент стеку не відповідає значенню ключа, то повертаємо "Asymmetric"
            if top != brackets[char]:
                return "Asymmetric"
            print("stack after pop:", stack)
    
    return "Symmetric" if not stack else "Asymmetric"           
                  
# Перевірка функції
print(check_brackets_symmetry("( ){[ 1 ]( 1 + 3 )( ){ }}"))
print(check_brackets_symmetry("( 23 ( 2 - 3);"))
print(check_brackets_symmetry("( 11 }"))
print(check_brackets_symmetry("( () }"))