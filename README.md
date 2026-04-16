# Repositorio de Prácticas - Embebidos ISC (Grupo 8S21)

### Integrantes del equipo
* **Arath Hernandez Camacho** - Matrícula: 226020019
* **Gustavo Efrén Jiménez Valencia** - Matrícula: 226020090
* **Pamela Jhatdzarhy Perez Gomez** - Matrícula: 226020038
* **Juan Manuel Pérez Medina** - Matrícula: 226020139

---

## Práctica 1: Parpadeo del LED
### Descripción
Control de un LED físico mediante los pines GPIO de la Raspberry Pi 4B utilizando Python. En esta práctica se configuró un circuito básico para realizar un parpadeo intermitente.

### Configuración de Hardware
* **Pin de señal:** Pin físico 12 (GPIO 18 en modo BCM).
* **Resistencia:** 220Ω conectada a GND.
* **LED:** Rojo

### Instrucciones de ejecución
1. `cd ~/practicas_embebidos/P1_LedBlink`
2. `source env_blink/bin/activate`
3. `python P1_LedBlink.py`

---

## Práctica 2: Semáforo de Leds
### Descripción
Simulación de un semáforo de tránsito utilizando tres LED (Verde, Amarillo y Rojo). El programa implementa una secuencia de 10 segundos para Rojo/Verde y parpadeo para el Amarillo.

### Configuración de Hardware
* **LED Verde:** GPIO 17 | **Amarillo:** GPIO 27 | **Rojo:** GPIO 22
* **Resistencias:** 220Ω conectada a GND.

### Instrucciones de ejecución
1. `cd ~/practicas_embebidos/P2_SemaforoLeds`
2. `source ../P1_LedBlink/env_blink/bin/activate`
3. `python P2_Semaforo.py`

---

## Práctica 3: Recorrido Digital (Vector)
### Descripción
Uso de arreglos y funciones para controlar una secuencia de 5 LEDs de ida y vuelta de forma optimizada. El programa utiliza un vector de pines para iterar el encendido y apagado secuencial.

### Configuración de Hardware
* **Pines utilizados:** GPIO 17, 27, 22, 10, 9.
* **Componentes:** 5 LEDs y 5 resistencias de 220Ω conectadas a GND.

### Instrucciones de ejecución
1. `cd ~/practicas_embebidos/P3_RecorridoLedVector`
2. `source ../P1_LedBlink/env_blink/bin/activate`
3. `python P3_RecorridoLedVector.py`

## Práctica 4: Atenuación con PWM (Vector)
## Descripción
Implementación de Modulación por Ancho de Pulso (PWM) para controlar la intensidad luminosa de 5 LEDs. La práctica demuestra el efecto de atenuación fluida, logrando que el tono de cada LED disminuya gradualmente hasta apagarse.

### Configuración de Hardware
* **Pines utilizados:** GPIO 17, 27, 22, 10, 9.
* **Componentes:** 5 LEDs y 5 resistencias de 220Ω conectadas a GND.
* **Técnica:** Variación de Duty Cycle (Ciclo de trabajo) a una frecuencia de 1000Hz.

### Instrucciones de ejecución
1. `cd ~/practicas_embebidos/P4_RecorridoLedVectorPWM`
2. `source ../P1_LedBlink/env_blink/bin/activate`
3. `python P4_RecorridoLedVectorPWM.py`
 
