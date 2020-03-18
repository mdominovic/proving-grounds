def permute(input_list):
    if len(input_list) == 1:
        return [input_list]
    else:
        output_list = []
        for i in range(0, len(input_list)):
            element = input_list[i]
            rest = input_list[:i] + input_list[i+1:]
            for var in permute(rest):
                output_list.append([element] + var)
        return output_list


if __name__ == "__main__":
    input_list = [1, 2, 3]
    output = permute(input_list)
