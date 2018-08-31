# Hyperion Client

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com) ![license](https://img.shields.io/github/license/JFtechOfficial/hyperion-client.svg) ![GitHub issues](https://img.shields.io/github/issues/JFtechOfficial/hyperion-client.svg) ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/JFtechOfficial/hyperion-client.svg) ![GitHub top language](https://img.shields.io/github/languages/top/JFtechOfficial/hyperion-client.svg)

Client module for the Hyperion JSON interface. You can also read this in [English:gb:](README.md)


## 🚀 Getting started

<details>
 <summary><strong>Lista dei Contenuti</strong> (clicca per espandere)</summary>

* [Getting started](#-getting-started)
* [Installazione](#-installazione)
* [Uso](#️-uso)
* [Risorse](#-risorse)
* [Contribuire](#-contribuire)
* [Crediti](#️-crediti)
* [Supportami!](#-supportami)
* [Release History](#️-release-history)
* [Licenza](#-licenza)
</details>

### Requisiti

* Un'instanza di [Hyperion](https://hyperion-project.org) installata e configurata (è suggerita l'installazione e la configurazione via [HyperCon](https://hyperion-project.org/wiki/HyperCon-Information)). è necessario conoscere l'indirizzo IP locale della macchina su cui è installato Hyperion


## 💾 Installazione

Apri il terminale e lancia il comando:
```shell
pip install hyperion-client
```


## ▶️ Uso

Per poter usare questo modulo devi importarlo nel tuo progetto python
```python
import hyperion_client as hy
```
### Nuovo client
Crea un nuovo client instanziando un nuovo oggetto hyperion_client
```python
h = hy.hyperion_client()
```
Se la macchina su cui far girare il client è diversa da quella su cui è in esecuzione il server Hyperion, devi specificarne l'indirizzo IP. Se hai modificato la porta di default dell'interfaccia JSON della tua istanza di Hyperion, puoi specificarla qui
```python
h = hy.hyperion_client('192.168.1.42', 19444)
```
 
### Connessione
Connettiti al server Hyperion
```python
h.open_connection()
```
Puoi anche modificare la durata del timout dei tentativi di connessione (di default: 10ms)
```python
h.open_connection(timeout=10)
```
Se provi a interagire con il server senza aprire una connessione prima, le altre funzioni di questo modulo cercheranno di connettersi automaticamente.

### Disconnessione
Disconnttiti dal server Hyperion
```python
h.close_connection()
```

### host
Cambia l'indirizzo IP del server Hyperion a cui vuoi connetterti
```python
h.host = '192.168.1.42'
```
Quando cambi host è necessario riconnettersi. 
Ottineni l'indirizzo IP del server Hyperion a cui vuoi connetterti
```python
my_host = h.host()
```

### porta
Cambia la porta del server Hyperion a cui vuoi connetterti
```python
h.port = 19444
```
Quando cambi porta è necessario riconnettersi. 
Ottineni la porta del server Hyperion a cui vuoi connetterti
```python
my_port = h.port()
```

- - - -
### Ottieni server info
recupera tutte le informazioni utili dal server Hyperion, formattate in JSON (es.: active effects, active color, active color transforms, available effects, etc...)
```python
my_server_info = h.serverinfo()
```

### Ottieni info degli effetti
recupera la lista delle info di tutti gli effetti disponibili dal server Hyperion, formattate in JSON (es.: effect name, effect script path, effect args)
```python
my_effects = h.effects()
```

### Ottieni nome effetti
recupera la lista dei nomi di tutti gli effetti disponibili dal server Hyperion
```python
my_effects_names = h.effects_names()
```

### Ottieni info degli effetti attivi
recupera la lista delle info di tutti gli effetti attivi dal server Hyperion, formattate in JSON (es.: effect name, effect script path, effect args)
```python
my_active_effects = h.active_effects()
```

### Ottieni nome effetti attivi
recupera la lista dei nomi di tutti gli effetti attivi dal server Hyperion
```python
my_active_effects_names = h.active_effects_names()
```

### Ottieni colore attivo
recupera la lista contenente i valori RGB, HEX, HLS del colore attivo dal server Hyperion
```python
my_active_color = h.active_color()
```
Puoi specificare una delle modalità (RGB/HEX/HLS) per ottenere il valore corrispondente
```python
my_RGB_color = h.active_color("RGB")
```

### Ottineni altra rova
Ci sono anche funzioni per ottenere:
* adjustment()
* correction()
* temperature()
* transform()
* priorities()
* hostname()
* hyperion_build()

- - - -
### Imposta un colore
Dì a Hyperion di mostrare un colore passando i valori di RED, GREEN e BLUE [0-255]
```python
h.set_RGBcolor(255, 255, 255)
```
Puoi cambiare la priorità per il colore usando il parametro priority (default: 100). Puoi anche cambiare la durata, in millisecondi (default: infinita)
```python
h.set_RGBcolor(red=255, green=255, blue=255, priority=100, duration=1000)
```

### Imposta effetto
Dì a Hyperion di mostrare un effetto
```python
h.set_effect('Rainbow swirl fast')
```
Puoi cambiare la priorità per il colore usando il parametro priority (default: 100). Puoi anche cambiare la durata, in millisecondi (default: infinita) e puoi passare argomenti personalizzati in formato JSON
```python
h.set_effect('Rainbow swirl fast', priority=100, effectArgs=my_args, duration=1000)
```

### Clear
Spegni l'effetto/colore attivo con priorità più alta (con valore di priority minore)
```python
h.clear()
```
Puoi cambiare la priorità per lo spegnimento usando il parametro priority (default: 100)
```python
h.clear(100)
```

### Clear all
Spegni tutti gli effetti/colori attivi
```python
h.clear_all()
```

### Invia dati personalizzati
 Invia un bytearray di dati led (r,g,b) * numero di leds (aka hyperion.ledcount)
```python
h.send_led_data(my_led_data)
```
Puoi cambiare la priorità per i dati personalizzati usando il parametro priority (default: 100). Puoi anche cambiare la durata, in millisecondi (default: infinita)
```python
h.send_led_data(my_led_data, 100, 1000)
```

### Imposta altra roba
Ci sono anche funzioni per impostare:
* set_image(image_data, width, height, priority=100, duration=0)
* set_adjustment(identifier, redAdjust, greenAdjust, blueAdjust)
* set_correction(identifier, red, green, blue)
* set_temperature(identifier, red, green, blue)
* set_transform(identifier, blacklevel, gamma, luminanceGain, luminanceMinimum, saturationGain, saturationLGain, threshold, valueGain, whitelevel)


## 📚 Risorse

[Hyperion-controller](https://github.com/JFtechOfficial/hyperion-controller) usa questo modulo

## 🎁 Contribuire

Leggi [CONTRIBUTING.md](./CONTRIBUTING.md).


## ❤️ Crediti

* [hyperion](https://github.com/hyperion-project/hyperion)


## 💵 Supportami!

 [![ko-fi](https://i.imgur.com/3MPSu8i.png)](https://ko-fi.com/Y8Y0FW3V)



## 🗓️ Release History

* 16/08/2018 - 0.1.0 - beta release


## 🎓 Licenza

[MIT](http://webpro.mit-license.org/)



