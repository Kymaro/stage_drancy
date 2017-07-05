def getId(): #permet de recuperer le numero de serie de la RPI
    iD = "0000000000000000"
    try:
        f = open('/proc/cpuinfo','r')
        for line in f:
            if line[0:6]=='Serial':
                iD = line[10:26]
        f.close()
    except:
        iD = "ERROR00000000000"
        f.close()
    return iD