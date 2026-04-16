#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

PINES_LED = [17, 27, 22, 10, 9]
FRECUENCIA = 1000
PASOS_FADE = 50
RETARDO_PASO = 0.02

def configurar_gpios(pines):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    objetos_pwm = []
    for p in pines:
        GPIO.setup(p, GPIO.OUT)
        pwm = GPIO.PWM(p, FRECUENCIA)
        pwm.start(0)
        objetos_pwm.append(pwm)
    return objetos_pwm

def ciclo_atenuacion(pwm):
    for brillo in range(0, 101, 2):
        pwm.ChangeDutyCycle(brillo)
        time.sleep(RETARDO_PASO)

    for brillo in range(100, -1, -2):
        pwm.ChangeDutyCycle(brillo)
        time.sleep(RETARDO_PASO)

def main():
    pwms = configurar_gpios(PINES_LED)
    try:
        while True:
            for i in range(len(pwms)):
                ciclo_atenuacion(pwms[i])

    except KeyboardInterrupt:
        pass
    finally:
        for p in pwms:
            try:
                p.stop()
            except:
                pass
        GPIO.cleanup()

if __name__ == "__main__":
    main()
