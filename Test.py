
# Задание "Глосование"
def vote(votes):
    for voise in votes:
        count_ = votes.count(voise)
        if count_ > 1:
            return voise

# Задание "Квадратное уравнение"
def discriminant(a, b, c):
    return (b ** 2) - (4 * a * c)
def solution(a, b, c):
    if discriminant(a, b, c) == 0:
        x1 = ((-1 * b) + discriminant(a, b, c) * 0.5) / (2 * a)
        return [round(x1, 2)]
    elif discriminant(a, b, c) > 0:
        x1 = ((-1 * b) + discriminant(a, b, c) ** 0.5) / (2 * a)
        x2 = ((-1 * b) - discriminant(a, b, c) ** 0.5) / (2 * a)
        return [round(x1, 2), round(x2, 2)]
    else:
        return 'корней нет'

# Задание "Срока наоборот"
def reverse(string: str) -> str:
    lower_sting = string.lower()
    reverse_string = lower_sting[::-1]
    return reverse_string