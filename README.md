# Minimum Viable Christmas Lights

![Christmas Gif](https://i.giphy.com/media/1i5c6D15vpmeE3q4bA/giphy.webp)

My Christmas lights controlled via a Z-Wave stick and an NVIDIA Jetson Nano.

The UI is a Flask frontend, and / or a React Native App for iOS / Android.

This loops over each node on a Z-Wave network, and checks to see if it's a switch. 

If a network node is a switch, check the state. 

If it's On, give the option to turn Off, and vice versa.

# Running the Server

I'm currently running via a:

```
$ nohup FLASK_RUN_PORT=8050 flask run --host=0.0.0.0 &
```

This binds to my Jetson Nano's IP address, and makes the UI available to my network at port 8050. 

So, assuming my Jetson Nano's IP address is `192.168.1.21`, I can open up `http://192.168.1.21:8050` from any computer on my network, and see the state of and control my Christmas Lights.

# Building the React Native App

The React Native app uses [Expo](https://expo.io/) to handle building the iOS bundle. You'll want to create an Expo account to develop / livereload on your phone.

Get started by changing into the `RemoteControl/` directory, and then running:

```
$ yarn start
```

Right now the React native app has my Jetson Nano's IP address hardcoded. You'll probably want to change that to your Jetson Nano's IP address on your home network.
