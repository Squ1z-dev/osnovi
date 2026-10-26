import matplotlib.pyplot as plt
import numpy as np

# Повний список із 29 студентів
students = [
    "Андріїв В.Т.", "Брайк В.А.", "Вацик М.В.", "Вільшук В.І.", "Вольман А.О.",
    "Глушко В.В.", "Гребенєв С.З.", "Грудзевич О.І.", "Гураль Б.В.", "Демчишин І.А.",
    "Дигідь М.Р.", "Золін Є.А.", "Книшук Х.П.", "Корпанюк М.Ю.", "Курівчак В.Л.",
    "Левандовський М.В.", "Матлюк Д.Р.", "Мироняк Ю.В.", "Піскунов Я.М.", "Потяк Н.В.",
    "Рижко М.П.", "Сісяк В.І.", "Сорочинський А.В.", "Ташлицький М.М.", "Тимофійчук М.В.",
    "Турчин В.В.", "Шевчук М.А.", "Шегда Д.В.", "Штогрин Т.Р."
]

# Генерація оцінок для 29 студентів
np.random.seed(42)  # Фіксація генерації випадкових чисел
prog_scores = np.random.randint(60, 101, size=len(students))
math_scores = np.random.randint(60, 101, size=len(students))

# --- 1. Лінійний графік (Програмування) ---
plt.figure(figsize=(14, 6))
plt.plot(students, prog_scores, marker='o', color='blue', linestyle='-', linewidth=2, label='Бал з програмування')

plt.title('Середні оцінки з програмування', fontsize=14)
plt.xlabel('Студенти', fontsize=11)
plt.ylabel('Середній бал', fontsize=11)
plt.xticks(rotation=75, fontsize=9)  # Поворот підписів для зручного читання
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='upper right')
plt.ylim(50, 105)

plt.savefig('programming_scores.png')
plt.show()

# --- 2. Стовпчикова діаграма (Математика) ---
plt.figure(figsize=(14, 6))
#різні кольори для кожного стовпчика
colors = plt.cm.Set3(np.linspace(0, 1, len(students)))

plt.bar(students, math_scores, color=colors, alpha=0.7)

plt.title('Середні оцінки з математики', fontsize=14)
plt.xlabel('Студенти', fontsize=11)
plt.ylabel('Середній бал', fontsize=11)
plt.xticks(rotation=75, fontsize=9)  # Поворот підписів для зручного читання
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.ylim(50, 100)
plt.savefig('mathematics_scores.png')
plt.show()

#3 Кругова діаграма: відображає розподіл навчального часу студентів
plt.figure(figsize=(8, 8))
plt.pie([40, 30, 20, 10], labels=['Програмування', 'Математика', 'Англійська', 'Інші предмети'], autopct='%1.1f%%')
plt.title('Розподіл навчального часу студентів', fontsize=14)
plt.show()
plt.savefig('study_time_distribution.png')

#Гістограма: генерує випадкові оцінки (від 0 до 100) для 50 студентів з англійської мови; будує гістограму розподілу балів (10 інтервалів).
plt.figure(figsize=(10, 6))
english_scores = np.random.randint(0, 101, size=50)
plt.hist(english_scores, bins=10, color='green', alpha=0.7, edgecolor='black')
plt.title('Розподіл оцінок з англійської мови', fontsize=14)
plt.xlabel('Оцінки', fontsize=11)
plt.ylabel('Частота', fontsize=11)
plt.show()
plt.savefig('english_scores_histogram.png')