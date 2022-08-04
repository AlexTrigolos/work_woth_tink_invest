def read_token() -> str:
    TOKEN = ''
    with open('token', 'r') as infile:
        string = infile.read().split('=')
        if string[0] == 'token':
            TOKEN = string[1]
    return TOKEN