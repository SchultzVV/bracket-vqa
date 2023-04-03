import pennylane as qml
from pennylane import numpy as np

# Criar o circuito quântico variacional
def variational_circuit(params, wires):
    qml.RX(params[0], wires=wires[0])
    qml.RY(params[1], wires=wires[0])

# Definir o dispositivo quântico
dev = qml.device('braket.local.qubit', wires=1)

# Definir a função de custo
def cost(params):
    # Definir o estado ansatz
    variational_circuit(params, wires=[0])

    # Definir o observable para medir a energia
    obs = qml.PauliZ(0)

    # Medir o observable
    return qml.expval(obs)

# Inicializar os parâmetros do circuito variacional
params = np.array([0.0, 0.0])

# Criar um otimizador
opt = qml.GradientDescentOptimizer(stepsize=0.4)

# Otimizar os parâmetros do circuito variacional
for i in range(100):
    params = opt.step(cost, params)

# Preparar o estado final
variational_circuit(params, wires=[0])

# Medir o estado final
result = qml.expval(qml.PauliZ(0))

# Exibir o resultado
print(f"Resultado final: {result}")
