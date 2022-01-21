
def cal_delta(a, b, c):
    return b**2 - 4*a*c


def quadratic_solver(a, b, c):
    # assume ax^2 + bx+ c = 0
    delta = cal_delta(a, b, c)
    x1 = (-b + delta ** 0.5) / 2 * a  # bug here
    x2 = (-b - delta ** 0.5) / 2 * a  # bug here
    return x1, x2


if __name__ == '__main__':
    print(quadratic_solver(2, 4, 2))  # -1 -1
