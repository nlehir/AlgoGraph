def read_params() -> list:
    params = list()
    f = open("./params.txt", "r")
    for line in f:
        param = int(line.split("=")[1])
        params.append(param)
    return params
