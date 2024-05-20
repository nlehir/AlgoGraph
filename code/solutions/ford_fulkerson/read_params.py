def read_params() -> list:
    params = dict()
    f = open("./params.txt", "r")
    for line in f:
        param = line.split("=")
        params[param[0]] = param[1]
    return params
