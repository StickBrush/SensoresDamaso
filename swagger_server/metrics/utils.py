from threading import Timer
import socket

def send_metric(metric_name: str, metric_value):
    conn = socket.create_connection(("38b29376.carbon.hostedgraphite.com", 2003))
    conn.send(bytes("e5fcc8bb-12f7-4754-8943-ef6017a43efc.{} {}\n".format(metric_name, metric_value), encoding='utf-8'))
    conn.close()

class Uptimer:

    def __init__(self):
        self._timer = None
        self._restart()

    def _restart(self):
        self._timer = Timer(60, self._push)
        self._timer.start()

    def _push(self):
        send_metric("sensors.uptime", 1)
        self._restart()
