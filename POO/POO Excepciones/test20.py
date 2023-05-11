class Ex(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg + msg)
        self.args = (msg,)
 
 
try:
    raise Ex('ex')
except Ex as e:
    print(e)
except Exception as e:
    print(e)