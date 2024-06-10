# pip install pulp
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
