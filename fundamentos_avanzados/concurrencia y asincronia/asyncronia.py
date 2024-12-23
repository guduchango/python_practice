import asyncio

async def process_data(data):
    print(f"procesando {data}...")
    #simular una operación
    await asyncio.sleep(10)
    print(f"{data} procesado.")
    return data * 2

async def main():
    print("inicio de procesamiento")
    result = await process_data('archivo.txt')
    print(f'Resultado: {result}')

asyncio.run(main())

