'''
Peço desculpas pelo mal entendido anterior. Para realizar a tomografia de estados com experimentos usando a estrutura de bracket da Amazon, é possível usar o pacote Braket SDK fornecido pela própria Amazon.

Aqui está um exemplo de como realizar a tomografia de estados de um circuito quântico com os ângulos otimizados usando o Braket SDK
'''
from braket.analyze import process_tomography_results
from braket.aws import AwsDevice
from braket.circuits import Circuit

# Criar um circuito
circ = Circuit().h(0).cnot(0, 1)

# Definir o dispositivo quântico
device = AwsDevice("arn:aws:braket:::device/qpu/rigetti/Aspen-9")

# Executar o circuito no dispositivo quântico
task = device.run(circ, shots=1000)

# Obter os resultados do experimento
result = task.result()

# Realizar a tomografia de processo
tomography_result = process_tomography_results(result)

# Imprimir a matriz de densidade estimada
print(tomography_result.est_matrix)
