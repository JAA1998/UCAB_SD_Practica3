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
    getmsg.reqMsg(sockTCP, portclient)
    msg = getmsg.waitMsg(sockUDP)
    if msg != False:
        checksum = getmsg.convertMsg(msg)
        getmsg.validateMsg(sockTCP, checksum)
        auth.close(sockTCP)
        print('El mensaje es:', msg)
    else:
        auth.close(sockTCP)


if __name__ == "__main__":
    main()
