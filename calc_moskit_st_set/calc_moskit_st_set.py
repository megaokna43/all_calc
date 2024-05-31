# Цены на компоненты
profile_price = input('введите цену профиля за метр: ')  # Цена за 1 метр профиля
corner_price = input('введите цену соединительно уголка: ')   # Цена за 1 угол
mesh_price = input('введите цену 1 кв.м. сеточного полотна: ')    # Цена за 1 кв.м. сеточного полотна
crossbar_price = input('введите цену импоста: ') # Цена за 1 перемычку
handle_price = input('введите цену ручки: ') # Цена за 1 ручку
cord_price = input('введите цену за метр шнура: ')   # Цена за 1 метр уплотнительного шнура

# Размеры москитной сетки
width = input('введите ширину сетки в метрах: ') # Ширина сетки в метрах
width = float(width) # Округление ширины сетки до целого
height = input('введите высоту сетки в метрах: ') # Высота сетки в метрах
height = float(height)

# Расчет количества компонентов
profile_length = 2 * width + 2 * height  # Длина профиля в метрах
corners = 4                             # Количество уголков
mesh_area = width * height    # Площадь сеточного полотна
crossbars = 1                           # Количество перемычек
handles = 2                             # Количество ручек
cord_length = 2 * width + 2 * height    # Длина уплотнительного шнура

# Расчет стоимости компонентов
profile_cost = profile_length * float(profile_price)
corner_cost = float(corners) * float(corner_price)
mesh_cost = mesh_area * float(mesh_price)
crossbar_cost = crossbars * float(crossbar_price)
handle_cost = handles * float(handle_price)
cord_cost = cord_length * float(cord_price)

# Общая себестоимость
total_cost = float(profile_cost) + float(corner_cost) + mesh_cost + float(crossbar_cost) + float(handle_cost) + float(cord_cost)

print(f"Себестоимость производства москитной сетки размером {width}x{height} метров:")
print(f"Профиль: {float(profile_cost):.2f} руб.")
print(f"Уголки: {float(corner_cost):.2f} руб.")
print(f"Сеточное полотно: {float(mesh_cost):.2f} руб.")
print(f"Перемычка: {float(crossbar_cost):.2f} руб.")
print(f"Ручки: {float(handle_cost):.2f} руб.")
print(f"Уплотнительный шнур: {float(cord_cost):.2f} руб.")
print(f"Общая себестоимость: {float(total_cost):.2f} руб.")
