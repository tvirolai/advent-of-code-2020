def read_input(filename):
    with open("input/{0}".format(filename), "r") as f:
        return f.readlines()

def read_input_as_nums(filename):
    return [int(x) for x in read_input(filename)]
