def counter(reports):
    prev_report = None
    counter = 0
    for report in reports:
        if prev_report is not None:
            if report > prev_report:
                counter += 1
        prev_report = report
    return counter

def three_measurement(reports):
    measurements = []
    for i in range(len(reports) - 2):
        measurements.append(reports[i] + reports[i+1] + reports[i+2])
    return measurements

def main():
    reports = []
    with open('input.txt') as f:
        for line in f.readlines():
            reports.append(int(line.strip()))
    print(counter(reports))
    print(counter(three_measurement(reports)))


if __name__ == "__main__":
    main()
