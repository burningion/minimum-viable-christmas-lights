import openzwave
from openzwave.option import ZWaveOption
from openzwave.network import ZWaveNetwork

# make sure these Z-wave commands get flushed by doing them first with a time.sleep
# also, /dev/ttyACM0 is the name of my Jetson nano USB port that the Z-Stick is on.

options = ZWaveOption('/dev/ttyACM0')
options.lock()

network = ZWaveNetwork(options)

import time
time.sleep(3)

from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def one_button():
    node_list = list(network.nodes.keys())
    ON = False
    for node in node_list:
        switches = list(network.nodes[node].get_switches().keys())
        if switches:
            state = network.nodes[node].get_switch_state(switches[0])
            if state:
                ON = True
                continue
    if ON:
        return f"<h1>Lights On. <p> <a href='/off'>Turn them Off</a></p></h1>"

    return f"<h1>Lights Off. <p> <a href='/on'>Turn them On</a></p></h1>"


@app.route('/off')
def turn_off():
    node_list = list(network.nodes.keys())
    for node in node_list:
        switches = list(network.nodes[node].get_switches().keys())
        if switches:
            network.nodes[node].set_switch(switches[0], False)
    # Give ourselves some time to sync up state before redirect
    time.sleep(2.3)
    return redirect(url_for('one_button'))

@app.route('/on')
def turn_on():
    node_list = list(network.nodes.keys())
    for node in node_list:
        switches = list(network.nodes[node].get_switches().keys())
        if switches:
            network.nodes[node].set_switch(switches[0], True)
    # Give ourselves some time to sync up state before redirect
    time.sleep(2.3)
    return redirect(url_for('one_button'))
