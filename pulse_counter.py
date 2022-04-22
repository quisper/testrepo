from machine import Pin, Timer
import time

global tim, counter, flow

def debounce(tim):
    global counter, flow
    #print("[INFO] Pin value: {}".format(flow.value()))
    if flow.value()==False:
        counter+=1
        print("[INFOR] Counter: {}".format(counter))
        
        
def detect_flow(flow):
    #print("[INFO] Input: {}".format(flow.value()))
    global tim
    #print("[INFO] Edge detected!")
    tim.init(mode=Timer.ONE_SHOT,period=100, callback=debounce)

def get_flow(tim_flow):
    global counter
    #asumimos que la tuberia es de 4" y escalizaremos en litros
    k_factor=3.964
    flow_qty=6*counter/k_factor
    print("[INFO] Flow[lpm]: {}".format(flow_qty))
    counter=0
    

if __name__=='__main__':
    counter=0
    #timer
    tim=Timer(0)
    tim_flow=Timer(1)#compre el reloj
    tim_flow.init(mode=Timer.PERIODIC, period=10000, callback=get_flow)#programe la alarma
    #declarando el PIN flow
    flow=Pin(4,pull=Pin.PULL_UP)
    #la interrupcion
    flow.irq(handler=detect_flow,trigger=Pin.IRQ_FALLING)
    while True:
        pass
        #print("[INFO] Input: {}".format(flow.value()))
        #time.sleep(1)