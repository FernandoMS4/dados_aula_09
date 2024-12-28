from main_logs import checa_logs,timer_dec

@checa_logs
@timer_dec
def soma(x:int, y:int)->int:
    return x + y

soma(1,4)
soma(6,9)
soma(322,19293)