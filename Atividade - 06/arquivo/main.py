import csv
import matplotlib.pyplot as plt

def main():
  meses = []
  saldos = []
  with open('tabela.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      meses.append(row['Mês'])
      saldos.append(int(row['Saldo em conta']))
  geraGraf(meses, saldos)

def geraGraf(meses, saldos):
  plt.rcParams['figure.figsize'] = (14,7)

  print(meses)
  print(saldos)
  
  plt.subplot(411)
  plt.ylim(0, 320)
  plt.title('Gráfico dos dados')
  plt.plot(meses,saldos, color='blue')
  plt.ylabel('saldos')

  plt.subplot(412)
  plt.bar(meses, saldos)

  plt.subplot(212)
  plt.pie(saldos,labels=meses,autopct='%1.1f%%')
  plt.axis('equal')

  plt.show()

if __name__ == '__main__':
  main()