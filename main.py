import matplotlib.pyplot as plt

# Дані про країни, їх населення (в мільйонах) та площу (кв. км)
countries = ['Україна', 'Польща', 'Німеччина', 'Франція', 'Італія', 'Іспанія', 'Фінляндія', 'Данія', 'Японія', 'Швеція']
population = [41.1, 38.3, 83.2, 67.1, 60.4, 47.6, 5.5, 5.8, 125.8, 10.5]  # Чисельність населення в мільйонах
area = [603500, 312696, 357022, 551695, 301340, 505992, 338424, 42933, 377975, 450295]  # Площа країн (кв. км)

# Обчислюємо щільність населення (людей на кв. км)
population_density = [p * 1e6 / a for p, a in zip(population, area)]  # Перетворюємо населення в людей і ділимо на площу

# Обчислюємо відсотки щільності
total_density = sum(population_density)
percent_density = [d / total_density * 100 for d in population_density]

# Визначаємо власні кольори для секторів
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c4e17f', '#ff6666', '#ffb366', '#c2f0c2']

# Створюємо кругову діаграму
fig, ax = plt.subplots()
ax.pie(percent_density, labels=countries, autopct='%1.1f%%', colors=colors, startangle=90)
ax.axis("equal")  # Щоб діаграма була круглою

# Показуємо діаграму
plt.title('Розподіл щільності населення серед 10 країн')
plt.show()
