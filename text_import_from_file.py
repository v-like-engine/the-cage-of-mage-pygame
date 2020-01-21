def load_text(filename):
    file = open(filename, 'r')
    all_strs = file.readlines()
    file.close()
    return all_strs
