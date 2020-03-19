class Node():
    def __init__(self, info=None):
        self._info = info
        self._lowAddrSet = {}


    @property
    def info(self):
        return self._info

    @info.setter
    def info(self, value):
        self._info = value

    @property
    def lowAddrSet(self):
        return self._lowAddrSet

    @lowAddrSet.setter
    def lowAddrSet(self, value):
        self._lowAddrSet = value



class PublicNode():
    def __init__(self):
        self._queryCmdID = None
        self._setCmdID = None

    def __str__(self):
        return 'queryCmdID: ' + self._queryCmdID + ", " + 'setCmdID: ' + self._setCmdID

    # def __repr__(self):
    #     return 'queryCmdID: ' + self._queryCmdID + ", " + 'setCmdID: ' + self._setCmdID

    @property
    def queryCmdID(self):
        return self._queryCmdID

    @queryCmdID.setter
    def queryCmdID(self, value):
        self._queryCmdID = value

    @property
    def setCmdID(self):
        return self._setCmdID

    @setCmdID.setter
    def setCmdID(self, value):
        self._setCmdID = value


class SpecificNode():
    def __init__(self):
        self._level = None
        self._cmd = None
        self._isEnd = None
        self._queryCmdID = None
        self._setCmdID = None
        self._omissible = None
        self._nextLevel = None

    def __str__(self):
        return 'level: ' + self._level + ", " + 'cmd: ' + self._cmd \
               + ", " + 'isEnd: ' + self._isEnd + ", " + 'queryCmdID: ' + self._queryCmdID \
               + ", " + 'setCmdID: ' + self._setCmdID + ", " + 'omissible: ' + self._omissible \
               + ", " + 'nextLevel: ' + self._nextLevel

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value
    
    @property
    def cmd(self):
        return self._cmd

    @cmd.setter
    def cmd(self, value):
        self._cmd = value
        
    @property
    def isEnd(self):
        return self._isEnd

    @isEnd.setter
    def isEnd(self, value):
        self._isEnd = value

    @property
    def queryCmdID(self):
        return self._queryCmdID

    @queryCmdID.setter
    def queryCmdID(self, value):
        self._queryCmdID = value

    @property
    def setCmdID(self):
        return self._setCmdID

    @setCmdID.setter
    def setCmdID(self, value):
        self._setCmdID = value

    @property
    def omissible(self):
        return self._omissible

    @omissible.setter
    def omissible(self, value):
        self._omissible = value

    @property
    def nextLevel(self):
        return self._nextLevel

    @nextLevel.setter
    def nextLevel(self, value):
        self._nextLevel = value
