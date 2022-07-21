import socket,_thread
host = input('address: ')
def do(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((host,port))
        print('port {} is open'.format(port))
        s.close()
    except:
        pass
for port in range(1 ,65536):
    _thread.start_new_thread(do,(host, port))

