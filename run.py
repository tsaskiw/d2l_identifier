# run.py

import sys
from d2l_identifier import app

_LOCAL_HOST_IP = '192.168.1.41'
_PPTP_HOST_IP = '192.168.10.2'
_OVPN_HOST_IP = '10.8.0.6'
_DEFAULT_HOST_PORT = 5000

network_type = sys.argv[1]
if network_type == 'pptp':
    host_ip = _PPTP_HOST_IP
elif network_type == 'ovpn':
    host_ip = _OVPN_HOST_IP
else:
    host_ip = _LOCAL_HOST_IP
host_port = _DEFAULT_HOST_PORT

app.run(host=host_ip, port=host_port, debug=True)
