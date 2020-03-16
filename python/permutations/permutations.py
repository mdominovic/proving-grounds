import itertools

def permute(input_list):
    result_list = []
    permuted_list = list(itertools.permutations(input_list))
    for i in list(permuted_list):
        result_list.append(list(i))
    return result_list


if __name__ == "__main__":
    input_list = [6, 5, 4]
    output = permute(input_list)