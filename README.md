# Hyperion Client

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com) ![license](https://img.shields.io/github/license/JFtechOfficial/hyperion-client.svg) ![GitHub issues](https://img.shields.io/github/issues/JFtechOfficial/hyperion-client.svg) ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/JFtechOfficial/hyperion-client.svg) ![GitHub top language](https://img.shields.io/github/languages/top/JFtechOfficial/hyperion-client.svg)

Client module for the Hyperion JSON interface. You can also read this in [Italiano🇮🇹](README-it-IT.md)


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
* [FAQ](#-faq)
* [Release History](#️-release-history)
* [License](#-license)
</details>

### Requirements

* An instance of [Hyperion](https://hyperion-project.org) installed and configured (installation and configuration via [HyperCon](https://hyperion-project.org/wiki/HyperCon-Information) is suggested). You'll need to know the local IP address of this machine 


## 💾 Installation

* Do this

* Then this


## ▶️ Usage
In order to use this module you have to import it in yotu python project
```python
import hyperion_client as hy
```
### New client
Create a new client by simpy instanciating a new hyperion_client object
```python
h = hy.hyperion_client()
```
If the machine running the client is different from the one running the Hyperion server, then you have to specify the IP address of the machine running Hyperion. If you modified the default JSON interface port of your Hyperion instance, you can specify it here
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

### Disconnect
Disconnect from the Hyperion server
```python
h.close_connection()
```

### Change host
Change the IP address of the Hyperion server you want to connect to.
```python
h.host = '192.168.1.42'
```
When you change the host you need to reconnect.

### Get host
Get the IP address of the Hyperion server you want to connect to.
```python
my_host = h.host()
```

### Change port
Change the port of the Hyperion server you want to connect to.
```python
h.port = 19444
```
When you change the port you need to reconnect.

### Get port
Get the port of the Hyperion server you want to connect to.
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
retrive the list of all the available effects info form the Hyperion server, formatted in JSON (e.g.: effect name, effect script path, effect name)
```python
my_effects = h.effects()
```
### Get effects name
retrive the list of all the available effects names form the Hyperion server, formatted in JSON
```python
my_effects_names = h.effects_names()
```
- - - -
### Set

```python
h
```


## 📚 Resources

Something


## 🎁 Contributing

Please see [CONTRIBUTING.md](./CONTRIBUTING.md).


## ❤️ Credits

Major dependencies:
* [hyperion](https://github.com/hyperion-project/hyperion)


## 💵 Support Me!

 [![ko-fi](https://www.ko-fi.com/img/donate_sm.png)](https://ko-fi.com/Y8Y0FW3V)


## 💭 FAQ

> Question?

Answer.


## 🗓️ Release History

* 16/08/2018 - 1.0 - first release


## 🎓 License

[MIT](http://webpro.mit-license.org/)


