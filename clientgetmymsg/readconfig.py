import os
from configparser import ConfigParser


def read():
    try:
        config_object = ConfigParser()
        config_object.read(os.path.join(
            os.path.dirname(__file__), '..', 'config.cfg'))

        userinfo = config_object["USERINFO"]
        serverinfo = config_object["SERVERINFO"]

        return (
            userinfo['username'],
            userinfo['ipclient'],
            int(userinfo['portclient']),
            serverinfo['ipserver'],
            int(serverinfo['portserver'])
        )
    except:
        print('Ha ocurrido un error, intenta más tarde.')
        print('Asegúrese de haber configurado correctamente el archivo de configuración.')
        quit()
