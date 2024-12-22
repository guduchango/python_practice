
def log_transactin(func):
    def wrapper():
        print('1 Log de la transacción...')
        func()
        print('3 log terminado...')
    return wrapper


@log_transactin
def process_payment():
    print('2 procesando pago...')


process_payment()