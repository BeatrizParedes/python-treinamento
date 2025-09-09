import queue

# PriorityQueue organiza os itens pelo menor número primeiro
fila = queue.PriorityQueue()

# (prioridade, valor)
fila.put((2, "Processo Médio"))
fila.put((1, "Processo Urgente"))
fila.put((3, "Processo Lento"))
fila.put((4, "Processo Lento"))
fila.put((5, "Processo Lento"))

while not fila.empty():
    print(fila.get())
