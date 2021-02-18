SCREEN_WIDTH = 100


def print_center(s):
    x_pos = SCREEN_WIDTH // 2
    print((" " * x_pos), s)


def print_bar():
    print("=" * 100)


def print_bar_ln():
    print_bar()
    print()


def input_center(s):
    x_pos = SCREEN_WIDTH // 2
    print((" " * x_pos), s, end='')
    return input()
