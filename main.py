import time, random, csv
import matplotlib.pyplot as plt 


#simular dados de sensores
nivel = 1
delta_t = 1
nivel_max = 100
nivel_min = 0
tempo_total = 20 
transbordamento_total = 0

#criar listas para armazenar os dados 
tempos = []
niveis = []
v_entrada = []
v_saida = []
tranbordamentos = []

#Criar arquivo CSV
with open('dados_do_tanque.csv', mode='w', newline='') as arquivo_csv:
    writer = csv.writer(arquivo_csv)
    writer.writerow(['Tempo(s)', 'Nivel do Tanque', 'Vazão de entrada', 'Vazão de saída', 'Transbordamento'])#Cabeçalhos

    #criar loop para simulação do tanque
    for t in range(tempo_total):
        vazao_entrada = random.uniform(a = 10, b = 50)
        vazao_saida = random.uniform(a = 5, b = 40)
        #calculo para atualizar nivel do tanque 
        nivel = nivel + delta_t * (vazao_entrada - vazao_saida) 
        transbordamento = 0


        #Garantir o nivel dentro dos limites
        if nivel <= nivel_min:
            nivel = nivel_min
            print("Alerta! Nível minimo do tanque atingido!")
        elif nivel >= nivel_max:
            transbordamento = nivel - nivel_max
            nivel = nivel_max
            transbordamento_total += transbordamento
            print("Alerta! Nivel maximo do tanque atingido")

        #Armazenar dados (importante para possiveis visualizações futuras)
        tempos.append(t)
        niveis.append(nivel)
        v_entrada.append(vazao_entrada)
        v_saida.append(vazao_saida)
        tranbordamentos.append(transbordamento)

        #Exibir dados no console
        print(f'Tempo: {t+1}s | Nível: {nivel:.2f} | Entrada: {vazao_entrada:.2f} | Saída: {vazao_saida:.2f} | Transbordamento: {transbordamento:.2f}')
        #Salva os dados no CSV
        writer.writerow([t+1, nivel, vazao_entrada, vazao_saida, transbordamento])
        time.sleep(delta_t)


print("Simulação concluída")
print(f'Total de produto desperdiçado: {transbordamento_total:.2f} ')

#Visualização gráfica com matplotlib
plt.figure(figsize=(10, 5))
plt.plot(tempos, niveis, marker = 'o', label = 'Nível do tanque')
plt.axhline(y=100, color='r', linestyle='--', label='Nível máximo')
plt.axhline(y=0, color='b', linestyle='--', label='Nível mínimo')
plt.title('Variaçao do nível do tanque no tempo')
plt.xlabel('Tempo(s)')
plt.ylabel('Nível do Tanque')
plt.legend()
plt.grid(True)
plt.show()
