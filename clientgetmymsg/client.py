import readconfig
import connect
import auth
import getmsg


def main():
    username, ipclient, portclient, ipserver, portserver = readconfig.read()
    sockTCP = connect.createSocketTCP(ipserver, portserver)
    sockUDP = connect.createSocketUDP(ipclient, portclient)
    auth.authUser(username, sockTCP)
    length = getmsg.msgLength(sockTCP)

    msg = ''
    cont = 0
    while cont < 4:
        getmsg.reqMsg(sockTCP, portclient)
        msg = getmsg.waitMsg(sockUDP)
        if msg != False:
            break
        print('Tiempo de espera superado, volviendo a intentar...')
        cont = cont + 1

    if msg != False and msg != '':
        checksum = getmsg.convertMsg(msg)
        getmsg.validateMsg(sockTCP, checksum)
        auth.close(sockTCP)
        print('El mensaje es:', msg)
    else:
        print('Ha ocurrido un error, intenta más tarde')
        auth.close(sockTCP)


if __name__ == "__main__":
    main()
