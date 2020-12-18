def file_contents(file_path):
    file = open(file_path, 'r')
    contents = file.read()
    file.close()
    return contents


def unique_yesses_for_group(g):
    answers = ''.join(g.split('\n'))
    return set(answers)


def common_yesses_for_group(g):
    passenger_answers = [set(a) for a in g.split('\n') if a.strip() != '']
    return passenger_answers[0].intersection(*passenger_answers)


def six_point_one():
    input_str = file_contents('./6.input.txt')
    groups = input_str.split('\n\n')
    unique_yes_counts = [len(unique_yesses_for_group(g)) for g in groups]
    return sum(unique_yes_counts)


def six_point_two():
    input_str = file_contents('./6.input.txt')
    groups = input_str.split('\n\n')
    common_yes_counts = [len(common_yesses_for_group(g)) for g in groups]
    return sum(common_yes_counts)


print(six_point_one())
print(six_point_two())

