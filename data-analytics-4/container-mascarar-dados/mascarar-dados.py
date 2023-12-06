while True:

    import hashlib

    string = (input('Digite qualquer coisa: ')).encode()

    string_criptografada = hashlib.sha1(string)
    print(string_criptografada.hexdigest())
    
