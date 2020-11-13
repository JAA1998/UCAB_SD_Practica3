def authUser(USER, sock):
    msg = b'helloiam ' + USER.encode()
    sock.send(msg)
    data = sock.recv(1024).decode('utf-8').strip()
    if data == 'ok':
        return True
    elif data == 'error invalid user name':
        print('El usuario ingresado no es válido')
        quit()
    elif data == 'error invalid src ip':
        print('Tu IP actual no coincide con el usuario ingresado')
        quit()
    else:
        print('Ha ocurrido un error, intenta más tarde')
        quit()


def close(sock):
    msg = b'bye'
    sock.send(msg)
    data = sock.recv(1024).decode('utf-8').strip()
    if 'ok' in data:
        return True
    else:
        print('Ha ocurrido un error, intenta más tarde')
        quit()
