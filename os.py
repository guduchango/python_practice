import os

# obtener el directorio actual
"""cwd = os.getcwd()
print("directorio de trabajo actual",cwd)"""

# listar los archivos .txt
txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
print("Los archivo txt:", txt_files)

# renombrar archivo
os.rename('caperusita.txt','cuento.txt')
print('archivo renombrado')

# listar los archivos .txt
txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
print("Los archivo txt:", txt_files)