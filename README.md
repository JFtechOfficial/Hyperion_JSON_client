# Hyperion Client

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com) ![license](https://img.shields.io/github/license/JFtechOfficial/hyperion-client.svg) ![GitHub issues](https://img.shields.io/github/issues/JFtechOfficial/hyperion-client.svg) ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/JFtechOfficial/hyperion-client.svg) ![GitHub top language](https://img.shields.io/github/languages/top/JFtechOfficial/hyperion-client.svg)

Client module for the Hyperion JSON interface. You can also read this in [Italiano🇮🇹](https://github.com/JFtechOfficial/hyperion-client/edit/master/README-it-IT.md)


## 🚀 Getting started

<details>
 <summary><strong>Table of Contents</strong> (click to expand)</summary>

* [Getting started](#-getting-started)
* [Installation](#-installation)
* [Usage](#️-usage)
* [Resources](#-resources)
* [Contributing](#-contributing)
* [Credits](#️-credits)
* [Support Me!](#-support-me)
* [Release History](#️-release-history)
* [License](#-license)
</details>

### Requirements

* An instance of [Hyperion](https://hyperion-project.org) installed and configured (installation and configuration via [HyperCon](https://hyperion-project.org/wiki/HyperCon-Information) is suggested). You need to know the local IP address of the machine you installed Hyperion on


## 💾 Installation
Open a terminal window and run the command:
```shell
pip install hyperion-client
```
*NOT IMPLEMENTED YET!*


## ▶️ Usage
In order to use this module you have to import it in your python project
```python
import hyperion_client as hy
```
### New client
Create a new client by instantiating a new hyperion_client object
```python
h = hy.hyperion_client()
```
If the machine running the client is different from the one running the Hyperion server, you have to specify the IP address of the machine running Hyperion. If you modified the default JSON interface port of your Hyperion instance, you can specify it here
```python
h = hy.hyperion_client('192.168.1.42', 19444)
```
 
### Connect
Connect to the Hyperion server
```python
h.open_connection()
```
You can also modify the timout duration of the connection attempt (by default: 10ms)
```python
h.open_connection(timeout=10)
```
if you try to interact with the server without opening a connection first, the functions of this module will try to connect automatically.

### Disconnect
Disconnect from the Hyperion server
```python
h.close_connection()
```

### host
Change the IP address of the Hyperion server you want to connect to
```python
h.host = '192.168.1.42'
```
When you change the host you need to reconnect. 
Get the IP address of the Hyperion server you want to connect to
```python
my_host = h.host()
```

### port
Change the port of the Hyperion server you want to connect to
```python
h.port = 19444
```
When you change the port you need to reconnect. 
Get the port of the Hyperion server you want to connect to
```python
my_port = h.port()
```

- - - -
### Get server info
retrive all the usefull information form the Hyperion server, formatted in JSON (e.g.: active effects, active color, active color transforms, available effects, etc...)
```python
my_server_info = h.serverinfo()
```

### Get effects info
retrive the list of all the available effects info form the Hyperion server, formatted in JSON (e.g.: effect name, effect script path, effect args)
```python
my_effects = h.effects()
```

### Get effects name
retrive the list of all the available effects names form the Hyperion server
```python
my_effects_names = h.effects_names()
```

### Get active effects info
retrive the list of all the active effects info form the Hyperion server, formatted in JSON (e.g.: effect name, effect script path, effect args)
```python
my_active_effects = h.active_effects()
```

### Get active effects name
retrive the list of all the active effects names form the Hyperion server
```python
my_active_effects_names = h.active_effects_names()
```

### Get active color
retrive a list containing the RGB, HEX, HLS values of the active color form the Hyperion server
```python
my_active_color = h.active_color()
```
You can specify one of the modes (RGB/HEX/HLS) to get only corresponding value
```python
my_RGB_color = h.active_color("RGB")
```

### Get other stuff
There are also functions to get:
* adjustment()
* correction()
* temperature()
* transform()
* priorities()
* hostname()
* hyperion_build()

- - - -
### Set solid color
Tell Hyperion to display a solid color passing RED, GREEN and BLUE values [0-255]
```python
h.set_RGBcolor(255, 255, 255)
```
You can change the priority channel for the color using the priority param (default: 100). You can also change the duration, in milliseconds (default: infinite)
```python
h.set_RGBcolor(red=255, green=255, blue=255, priority=100, duration=1000)
```

### Set effect
Tell Hyperion to display an effect
```python
h.set_effect('Rainbow swirl fast')
```
You can change the priority channel for the effect using the priority param (default: 100). You can also change the duration, in milliseconds (default: infinite) and you can pass custom effect arguments in JSON format
```python
h.set_effect('Rainbow swirl fast', priority=100, effectArgs=my_args, duration=1000)
```

### Clear
Clear the highest priority active effect/color (with lower priority value)
```python
h.clear()
```
You can change the priority channel for the color/effect to clear using the priority param (default: 100)
```python
h.clear(100)
```

### Clear all
Clear all the active effects/color
```python
h.clear_all()
```

### Send custom data
 Send a bytearray of the led data (r,g,b) * number of leds (aka hyperion.ledcount)
```python
h.send_led_data(my_led_data)
```
You can change the priority channel for the custom data using the priority param (default: 100). You can also change the duration, in milliseconds (default: infinite)
```python
h.send_led_data(my_led_data, 100, 1000)
```

### Set other stuff
There are also functions to set:
* set_image(image_data, width, height, priority=100, duration=0)
* set_adjustment(identifier, redAdjust, greenAdjust, blueAdjust)
* set_correction(identifier, red, green, blue)
* set_temperature(identifier, red, green, blue)
* set_transform(identifier, blacklevel, gamma, luminanceGain, luminanceMinimum, saturationGain, saturationLGain, threshold, valueGain, whitelevel)


## 📚 Resources

[Hyperion-controller](https://github.com/JFtechOfficial/hyperion-controller) uses this module


## 🎁 Contributing

Please see [CONTRIBUTING.md](./CONTRIBUTING.md).


## ❤️ Credits

Major dependencies:
* [hyperion](https://github.com/hyperion-project/hyperion)


## 💵 Support Me!

 [![ko-fi](https://www.ko-fi.com/img/donate_sm.png)](https://ko-fi.com/Y8Y0FW3V)


## 🗓️ Release History

* 16/08/2018 - 0.1.0 - beta release


## 🎓 License

[MIT](http://webpro.mit-license.org/)


