# Оптимізація виробництва та Обчислення інтеграла методом Монте-Карло

## Опис

Цей проект включає два завдання:

1. Оптимізація виробництва напоїв за допомогою лінійного програмування.
2. Обчислення визначеного інтеграла методом Монте-Карло.

## Завдання 1: Оптимізація виробництва

Компанія виробляє два види напоїв: "Лимонад" і "Фруктовий сік". Задача полягає у максимізації виробництва, враховуючи обмежені ресурси.

### Вхідні дані

- Набір монет: [50, 25, 10, 5, 2, 1]
- Сума, яку потрібно видати як решту

### Цільова функція

Мета - максимізація виробництва напоїв, враховуючи обмеження на ресурси.

### Рішення

Рішення задачі наведено в коді нижче.

```python
import pulp

def optimize_production():
    prob = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)
    lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Continuous')
    fruit_juice = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Continuous')
    prob += lemonade + fruit_juice, "Total_Production"
    prob += 2 * lemonade + fruit_juice <= 100, "Water_Constraint"
    prob += lemonade <= 50, "Sugar_Constraint"
    prob += lemonade <= 30, "Lemon_Juice_Constraint"
    prob += 2 * fruit_juice <= 40, "Fruit_Puree_Constraint"
    prob.solve()
    print("Status:", pulp.LpStatus[prob.status])
    print("Лимонад:", pulp.value(lemonade))
    print("Фруктовий сік:", pulp.value(fruit_juice))

optimize_production()
```
## Завдання 2: Оптимізація виробництва
Обчислення інтеграла функції методом Монте-Карло, тобто знаходження площі під графіком функції.

### Рішення

Рішення задачі наведено в коді нижче.

```python
import pulp

def optimize_production():
    # Визначення проблеми
    prob = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)
    
    # Змінні рішення
    lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Continuous')
    fruit_juice = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Continuous')
    
    # Цільова функція
    prob += lemonade + fruit_juice, "Total_Production"
    
    # Обмеження
    prob += 2 * lemonade + fruit_juice <= 100, "Water_Constraint"
    prob += lemonade <= 50, "Sugar_Constraint"
    prob += lemonade <= 30, "Lemon_Juice_Constraint"
    prob += 2 * fruit_juice <= 40, "Fruit_Puree_Constraint"
    
    # Розв'язання проблеми
    prob.solve()
    
    # Виведення результатів
    print("Status:", pulp.LpStatus[prob.status])
    print("Лимонад:", pulp.value(lemonade))
    print("Фруктовий сік:", pulp.value(fruit_juice))

# Виклик функції
optimize_production()
```
## Висновки
Метод Монте-Карло обчислює інтеграл з певною наближеною точністю. Аналітичний метод, реалізований через функцію quad, дає точне значення інтеграла.

## Порівняння
- Жадібний алгоритм: Простий та швидкий, але може не завжди знайти оптимальне рішення.

- Динамічне програмування: Гарантовано знаходить оптимальне рішення, але є більш складним та часозатратним.

- Метод Монте-Карло: Наближений результат з контрольною точністю.

- Аналітичний метод: Точний результат, складніший у реалізації.

Ці методи ілюструють різні підходи до оптимізації та обчислень, кожен з яких має свої переваги та недоліки.
