import ipaddress as ip
import math
from pathlib import Path as path
import datetime
def ipv4(x):
  return ip.ip_address(x)
def subnet(x):
  network = ip.ip_network(f'0.0.0.0/{x}', strict=False)
  return network.prefixlen
def cidr(x, y):
  return ip.ip_network(f'{x}/{y}', strict=False)
def two_expo(x):
  if x > 0 and (x & (x - 1)) == 0:
    return True
  else:
    return False
def two_expo2(y):
  x = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32)
  for a, b in enumerate(x):
    if 2**b >= y+2:
      return 2**b
def two_expo3(y):
  x = math.log2(y)
  return x
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
timestamp2 = datetime.datetime.now().strftime("%d/%m/%Y às %H:%M:%S")
dirc = path('Python/IPv4/Files')
dirc.mkdir(parents=True, exist_ok=True)
txt_file = dirc / f'subredes_{timestamp}.txt'
a = False
b = True
a1 = False
network = cidr('10.0.0.0', '8')
network1 = cidr('172.16.0.0', '12')
network2 = cidr('192.168.0.0', '16')
print("Calculadora de sub-rede IPv4!\n")
while not a:
  adr = input("Digite o endereço da rede IPv4: ")
  try:
    ipv4_1 = ipv4(adr)
    if ipv4_1.is_private:
      a = True
    else:
      print("Digite um endereço privado!")
  except ip.AddressValueError:
    print("Endereço IP inválido!")
while a:
  s = input("Digite a máscara de sub-rede ou o comprimento do prefixo: ")
  try:
    sn = subnet(s)
    if ipv4_1 in network and 8 < sn <= 30:
      a = False
    elif ipv4_1 in network1 and 12 < sn <= 30:
      a = False
    elif ipv4_1 in network2 and 16 < sn <= 30:
      a = False
    elif (ipv4_1 in network and sn == network.prefixlen) or (ipv4_1 in network1 and network1.prefixlen) or (ipv4_1 in network2 and network2.prefixlen):
      print('Digite uma máscara de sub-rede diferente da original!')
    else:
      print("Digite uma máscara de sub-rede dentro do intervalo da sua rede!")
  except ip.AddressValueError:
    print("Máscara de sub-rede inválida!")
ip_cidr = cidr(ipv4_1, sn)
values = []
values1 = []
values2 = []
values3 = []
values2.append(ipv4_1)
address = 2**(32 - sn)
adddess_1 = address
print(f'\nEndereço da rede: {ip_cidr}')
print(f'Máscara de sub-rede: {ip_cidr.netmask}')
print(f'Endereço de Broadcast: {ip_cidr.broadcast_address}')
print(f'Número de endereços: {address}\n')
while not a1:
  c = str(input('Deseja segmentar a rede em sub-redes de tamanhos variados? [Y/N]: '))
  if c.lower() == "y": # VLSM
    a1 = True
    for i in range(int(math.sqrt(address))):
      while a1:
        sb = int(input(f'\nDigite a quantidade de hosts para a {i+1}° sub-rede: '))
        values.append(sb)
        z = two_expo2(values[i])
        if z > address:
          print("Digite um número menor!")
          values.pop()
        elif z == adddess_1:
          print("Digite um valor menor do que a quantidade total de endereços!")
          values.pop()
        else:
          a1 = False
          values1.append(z)
          address -= z
          ipv4_1 = int(ipv4_1) + values1[i]
          values2.append(ipv4(ipv4_1))
          z1 = two_expo3(values1[i])
          sn1 = (32 - sn) - z1
          sn2 = int(sn + sn1)
          values3.append(sn2)
          print(f'\nQuantidade de endereços restantes: {address}')
          a = False
      while not a:
        e = str(input('Deseja continuar? [Y/N]: '))
        if e.lower() == 'y':
          a1 = True
          a = True
        elif e.lower() == 'n':
          a1 = True
          a = True
          b = False
          with open(txt_file, 'a') as f:
            f.write(f'Rede principal: {ip_cidr}\n')
            print(f'\nRede principal: {ip_cidr}')
          for x, y in enumerate(values3):
            subnet2 = cidr('0.0.0.0', y)
            print(f'\nSub-rede {x+1}: {values2[x]}/{y} ({values2[x]+1} - {values2[x+1]-2})')
            print(f'Endereço de broadcast: {values2[x+1]-1}')
            print(f'Máscara de sub-rede: {subnet2.netmask}')
            print(f'Número de endreços: {values1[x]}')
            print(f'Número de hosts: {values1[x]-2}\n')
            with open(txt_file, 'a') as f:
              f.write(f'\nSub-rede {x+1}: {values2[x]}/{y} ({values2[x]+1} - {values2[x+1]-2})\n')
              f.write(f'Endereço de broadcast: {values2[x+1]-1}\n')
              f.write(f'Máscara de sub-rede: {subnet2.netmask}\n')
              f.write(f'Número de endreços: {values1[x]}\n')
              f.write(f'Número de hosts: {values1[x]-2}\n')
          with open(txt_file, 'a') as f:
            f.write(f'\n\nArquivo gerado em: {timestamp2}\n')
          print("Arquivo criado com sucesso!\n")
          print("Procure pela pasta 'Python' na raiz do armazenamento para ver o relatório!")
        else:
          a = False
          print("Digite 'Y' ou 'N'! ")
      if a and not b:
        break
  elif c.lower() == "n":
    a1 = True
    print("Ola")
  else:
    print("Digite 'Y' ou 'N'!")