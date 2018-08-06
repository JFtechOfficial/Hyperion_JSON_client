import json
import socket
import time

s = None
connected = False


def open_connection(host, port, timeout=10):
    """
    Open a socket connection to the server
    :param host: Hostname oder ip address of the server
    :param port: Port of the server
    :param timeout: timeout in seconds
    """
    global connected
    global s

    if connected:
        return

    s = socket.socket()
    s.settimeout(timeout)
    try:
        s.connect((host, port))
        connected = True
    except socket.error, exc:
        print "Error on connection to ", host, ":", port, "\nMessage: ", exc


def close_connection():
    if connected:
        try:
            # s.send('{"command":"clearall"}\n')
            s.close()
        except socket.error, exc:
            print "Could not close socket connection\nMessage: ", exc


def recv_timeout(the_socket, timeout=2):
    # make socket non blocking
    the_socket.setblocking(0)

    # total data partwise in an array
    total_data = []
    data = ''

    # beginning time
    begin = time.time()
    while 1:
        # if you got some data, then break after timeout
        if total_data and time.time() - begin > timeout:
            break

        # if you got no data at all, wait a little longer, twice the timeout
        elif time.time() - begin > timeout * 2:
            break

        # recv something
        try:
            data = the_socket.recv(8192)
            if data:
                total_data.append(data)
                # change the beginning time for measurement
                begin = time.time()
            else:
                # sleep for sometime to indicate a gap
                time.sleep(0.1)
        except:
            pass

    # join all parts to make final string
    return ''.join(total_data)


def set_color(red, green, blue, priority=100, duration=0):
    """
    Send the led data in a message format the hyperion json server understands
    :param led_data: bytearray of the led data (r,g,b) * hyperion.ledcount
    """
    if not connected:
        return
    # create a message to send
    message = '{"color":[' + str(red) + ',' + str(green) + ',' + str(blue) + '],'
    message += '"command":"color","' + str(priority)
    message += '":100,"duration"' + str(duration) + '"}\n'

    try:
        s.send(message)
    except socket.error, exc:
        print "Error while sending the led data\nMessage: ", exc


def set_effect(effectName):  # , effectArgs=None, priority=100, duration=0):
    if not connected:
        return
    # create a message to send
    message = '{"command":"effect","effect":{"name":"Snake"},"priority":100}\n'
    print message
    try:
        s.send(message)
    except socket.error, exc:
        print "Error while sending the data\nMessage: ", exc


def clear():
    if not connected:
        return
    # create a message to send
    message = '{"command":"clear","priority":100}\n'
    try:
        s.send(message)
    except socket.error, exc:
        print "Error while sending the data\nMessage: ", exc


def clear_all():
    if not connected:
        return
    # create a message to send
    message = '{"command":"clearall"}\n'
    try:
        s.send(message)
    except socket.error, exc:
        print "Error while sending the data\nMessage: ", exc


def get_serverinfo():
    if not connected:
        return
    resp = ''
    # create a message to send
    message = '{"command":"serverinfo"}\n'
    try:
        s.send(message)
    except socket.error, exc:
        print "Error while sending the data\nMessage: ", exc
    try:
        resp = recv_timeout(s)
    except socket.error, exc:
        print "Error while reciving the data\nMessage: ", exc
    return resp

# def set_image()
# def transform()
# def correction()
# def temperature()
# def adjustment()


def send_led_data(led_data):
    """
    Send the led data in a message format the hyperion json server understands
    :param led_data: bytearray of the led data (r,g,b) * hyperion.ledcount
    """
    if not connected:
        return
    # create a message to send
    message = '{"color":['
    # add all the color values to the message
    for i in range(len(led_data)):
        message += repr(led_data[i])
        # separate the color values with ",", but do not add a "," at the end
        if not i == len(led_data) - 1:
            message += ','
    # complete message
    message += '],"command":"color","priority":100}\n'
    try:
        s.send(message)
    except socket.error, exc:
        print "Error while sending the led data\nMessage: ", exc


open_connection('192.168.1.26', 19444)
set_effect("Snake")
# clear_all()
time.sleep(2)
info = get_serverinfo()
ppinfo = info.split('{"success":true}')
print 'pretty server info:\n'
parsed = json.loads(ppinfo[1])
print json.dumps(parsed, indent=4, sort_keys=True)

close_connection()
