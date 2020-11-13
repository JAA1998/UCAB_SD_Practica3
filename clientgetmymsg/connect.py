import socket


def createSocketTCP(IP, PORT):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((IP, PORT))
        return sock
    except:
        print('Ha ocurrido un error, intenta más tarde')
        quit()


def createSocketUDP(IP, PORT):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((IP, PORT))
        return sock
    except:
        print('Ha ocurrido un error, intenta más tarde')
        quit()
