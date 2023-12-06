import re

games = open('input.txt', 'r').read().split('\n')

m_red, m_green, m_blue = 12, 13, 14
solution1, solution2 = 0, 0

for i, game in enumerate(games, 1):
    to_nums = lambda x: [int(y) for y in x]
    reds = max(to_nums(re.findall(r'(\d+) red', game)))
    greens = max(to_nums(re.findall(r'(\d+) green', game)))
    blues = max(to_nums(re.findall(r'(\d+) blue', game)))

    if reds <= m_red and greens <= m_green and blues <= m_blue:
        solution1 += i

    solution2 += reds * greens * blues

print(f'Number of possible games with the given amount of cubes: {solution1}')
print(f'Sum of the power of the minimum amount of cubes needed: {solution2}')
