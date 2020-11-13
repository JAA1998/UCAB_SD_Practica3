import base64
import hashlib


def msgLength(sock):
    msg = b'msglen'
    sock.send(msg)
    data = sock.recv(1024).decode('utf-8').strip()
    pos = data.find(' ')
    length = data[pos + 1:]
    if 'ok' in data:
        return int(length)
    else:
        print('Ha ocurrido un error, intenta más tarde')
        quit()


def reqMsg(sock, UDP_PORT):
    msg = b'givememsg ' + str(UDP_PORT).encode()
    sock.send(msg)
    data = sock.recv(1024).decode('utf-8').strip()
    if data == 'ok':
        return True
    elif data == 'error invalid udp port':
        print('El puerto UDP no es válido')
        quit()
    else:
        print('Ha ocurrido un error, intenta más tarde')
        quit()


def waitMsg(sock):
    cont = 0
    data = ''
    sock.settimeout(10)
    while cont < 5:
        try:
            data, address = sock.recvfrom(1024)
        except:
            print('Tiempo de espera superado, volviendo a intentar...')
        if data != '':
            data = (base64.b64decode(data)).decode('utf-8')
            return data
        cont = cont + 1
    print('Ha ocurrido un error, intenta más tarde')
    return False


def convertMsg(msg):
    return hashlib.md5(msg.encode()).hexdigest()


def validateMsg(sock, checksum):
    msg = b'chkmsg ' + checksum.encode()
    sock.send(msg)
    data = sock.recv(1024).decode('utf-8').strip()
    if data == 'ok':
        return True
    elif data == 'error invalid checksum format':
        print('El formato del checksum no es válido')
        quit()
    elif data == 'error bad checksum':
        print('El checksum es incorrecto')
        quit()
    else:
        print('Ha ocurrido un error, intenta más tarde')
        quit()
