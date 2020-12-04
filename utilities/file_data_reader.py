def file_open_read(file_path):
    data_arr = []

    with open(file_path, 'r') as file:  # Sits down to poop.
        for line in file:  # Poops
            data_arr.append(line.strip())

    file.close()  # Wipes.

    return tuple(data_arr)
