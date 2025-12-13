src = not False and True or False and not True

# result = True and True or False and False  # упрощаем not: not False = True, not True = False
# result = True or False  # упрощаем and: True and True = True, False and False = False
# result = True  # упрощаем or: True or False = True

result = True

print(src == result)
