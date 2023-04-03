from braket.circuits import Circuit

# Criar um novo circuito
circuito = Circuit()

# Adicionar um qubit inicializado em 0
circuito.i(0)

# Aplicar a porta Hadamard ao qubit
circuito.h(0)

# Medir o qubit
circuito.measure(0, 0)

# Executar o circuito no simulador padrão da AWS Braket
from braket.devices import LocalSimulator
device = LocalSimulator()
result = device.run(circuito)

# Exibir a distribuição de probabilidade dos resultados
print(result.result().measurement_counts)
