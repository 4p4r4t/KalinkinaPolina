salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

salary = 5000
spend = 6000
months = 10
increase = 0.03

current_spend = spend
money_needed = 0

for month in range(months):
    deficit = current_spend - salary
    if deficit > 0:
        money_needed += deficit
    current_spend *= (1 + increase)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_needed))

