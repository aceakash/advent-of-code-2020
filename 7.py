import re


def file_contents(file_path):
    file = open(file_path, 'r')
    contents = file.read()
    file.close()
    return contents


def parse_contained(contained):
    if contained == 'no other bags':
        return None

    parts = re.compile('^(\d+) ([a-zA-Z ]+) bags?$').match(contained)
    return parts.group(1), parts.group(2)


def parse_line(line):
    parts = re.compile('^([a-zA-Z ]+) bags contain (.+)\.$').match(line)
    (container, secondPart) = (parts.group(1), parts.group(2))
    contained = [parse_contained(frag) for frag in secondPart.split(', ')]
    return container, contained


def make_contained_in_graph(parsed):
    # {contained} ---contained in--- {container}
    graph = {}
    for item in parsed:
        container, contained_list = item
        if contained_list == [None]:
            continue
        for contained in contained_list:
            num, colour = contained
            if colour not in graph:
                graph[colour] = set([container])
            else:
                graph[colour].add(container)

    return graph


def parse_contained_in_graph(txt):
    lines = txt.split('\n')
    parsed = [parse_line(l) for l in lines if l.strip() != '']
    graph = make_contained_in_graph(parsed)
    return graph


def find_containers(color, graph):
    if color not in graph:
        return set()

    containers = graph[color]
    for container in [*containers]:
        containers = containers.union(find_containers(container, graph))

    return containers


def seven_point_one(txt):
    graph = parse_contained_in_graph(txt)
    containers = find_containers('shiny gold', graph)
    return len(containers)


def make_contains_graph(parsed):
    graph = {}
    for (container_colour, children) in parsed:
        if container_colour not in graph:
            graph[container_colour] = set()
        graph[container_colour] = graph[container_colour].union(set(children))
    return graph


def parse_contains_graph(txt):
    lines = txt.split('\n')
    parsed = [parse_line(l) for l in lines if l.strip() != '']
    graph = make_contains_graph(parsed)
    return graph


def count_descendants(colour, graph):
    if graph[colour] == {None}:
        return 0
    if colour not in graph:
        return 0
    count = 0
    for (child_count_str, child_colour) in graph[colour]:
        child_count = int(child_count_str)
        count = count + int(child_count)
        count = count + child_count*count_descendants(child_colour, graph)
    return count


def seven_point_two(txt):
    graph = parse_contains_graph(txt)
    descendant_count = count_descendants('shiny gold', graph)
    return descendant_count

inputText = file_contents('./7.input.txt')
print(seven_point_one(inputText))
print(seven_point_two(inputText))

