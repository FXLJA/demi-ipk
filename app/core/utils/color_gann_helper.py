def create_to_gann_input(colors, percentages):
    result = []

    for i in range(len(colors)):
        result += [colors[i][0]]
        result += [colors[i][1]]
        result += [colors[i][2]]
        result += [percentages[i]]

    return result
