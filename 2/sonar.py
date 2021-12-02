def position(reports):
    horizontal = 0
    aim = 0
    for operation, value in reports:
        if operation == 'forward':
            horizontal += int(value)
        elif operation == 'down':
            aim += int(value)
        elif operation == 'up':
            aim -= int(value)
    return horizontal * aim

def aim(reports):
    horizontal = 0
    depth = 0
    aim = 0
    for operation, value in reports:
        if operation == 'forward':
            horizontal += int(value)
            depth += int(value) * aim
        elif operation == 'down':
            aim += int(value)
        elif operation == 'up':
            aim -= int(value)
    return horizontal * depth

def main():
    reports = []
    with open('input.txt') as f:
        for line in f.readlines():
            reports.append(line.split())
    print(position(reports))
    print(aim(reports))


if __name__ == "__main__":
    main()
