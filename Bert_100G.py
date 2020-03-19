from time import sleep

def setChannelPattern():
    print("setChannelPattern")
    return "setChannelPattern OK"

def setChannelPolarity():
    print("setChannelPolarity")
    return "setChannelPolarity OK"

def setChannelAmpLitude():
    print("setChannelAmpLitude")
    return "setChannelAmpLitude OK"

def setChannelTestTime():
    print("setChannelTestTime")
    return "setChannelTestTime OK"


def queryChannelPattern():
    print("queryChannelPattern")
    return "queryChannelPattern PRBS31"


def queryChannelPolarity():
    print("queryChannelPolarity")
    return "queryChannelPolarity negative"


def queryChannelAmpLitude():
    print("queryChannelAmpLitude")
    return "queryChannelAmpLitude350mV"


def queryChannelTestTime():
    print("queryChannelTestTime")
    return "queryChannelTestTime OFF"


if __name__ == '__main__':

    while True:
        setChannelPattern()
        sleep(2)
        queryChannelPattern()
        sleep(2)
        setChannelAmpLitude()
        sleep(2)
        queryChannelAmpLitude()
        sleep(2)
        setChannelPolarity()
        sleep(2)
        queryChannelPolarity()
        sleep(2)
        setChannelTestTime()
        sleep(2)
        queryChannelTestTime()
        sleep(2)