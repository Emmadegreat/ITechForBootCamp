#  fetch_file assignment
fetch_file = open('assgmt.txt', 'r')

#  print(fetch_file.read())

outcome = {}

for line in fetch_file:
    if line == '\n':
        continue

    split_line = line.split(':')

    if len(split_line) < 2:
        continue
    outcome[split_line[0]] = split_line[1].strip()  # this assigns keys and values to the dictionary created above
print(outcome, '\n')
fetch_file.close()


name = 'emmanuel mkpurunchi f'
title = 'fetch file assignment'
print(f'Name: {name.upper()}. \n Title: {title.upper()}.')
