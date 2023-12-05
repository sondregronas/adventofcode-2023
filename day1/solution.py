import re

data = open('input.txt', 'r').read().split('\n')

solution1 = 0
solution2 = 0

for line in data:
    x = re.findall(r'(\d)', line)
    solution1 += int(x[0] + x[-1])

    x = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
    num_map = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    solution2 += int(num_map.get(x[0], x[0]) + num_map.get(x[-1], x[-1]))

print(f'(S1) Sum of calibration values for the trebuchet: {solution1}')
print(f'(S2) Sum of corrected calibration values: {solution2}')