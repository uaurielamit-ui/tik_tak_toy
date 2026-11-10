def get_int(text):
    legal = False
    while not legal:
        try: 
            client_choice =int(input(text))
            if client_choice >0 and client_choice <= 9:
                legal = True
        except ValueError:
            print("only number btween 1-9")
    return client_choice