# Minimum Viable Christmas Lights

My Christmas lights controlled via Z-Wave and a Flask frontend for my NVIDIA Jetson Nano.

This loops over each node on a Z-Wave network, and checks to see if it's a switch. 

If a network node is a switch, check the state. 

If it's On, give the option to turn Off, and vice versa.

# Running the Server

I'm currently running via a:

```
$ FLASK_RUN_PORT=8050 flask run --host=0.0.0.0
```

This binds to my Jetson Nano's IP address, and makes the UI available to my network at port 8050. 

So, assuming my Jetson Nano's IP address is `192.168.1.21`, I can open up `http://192.168.1.21:8050` from any computer on my network, and see the state of and control my Christmas Lights.