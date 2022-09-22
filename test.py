def f(other):
    q = 100
    if isinstance(other, int):
        return q > other
    elif isinstance(other, float):
        return q > other
    else:
        return "Невозможно выполнить сравнение"

print(f(12))
print(f(124.7))
print(f([34, 353]))




