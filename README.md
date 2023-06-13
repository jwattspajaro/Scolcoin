# Scolcoin
Debes ACTUALIZAR :
.   sudo apt update
    sudo apt upgrade
2.  sudo apt install python3-pip
3. pip install --upgrade pip
4. python --version


### 1. Este código en Python utiliza la biblioteca subprocess para ejecutar comandos de línea de comandos en el sistema operativo. A continuación, se proporciona una descripción del código:

Importar las bibliotecas necesarias:
    import subprocess
    import time
    
### 2. Primer bloque de codigo renplaza 0x00 potr tu direccion puedes obtener aqui: cat account.txt
      subprocess.call('pm2 start "./geth -snapshot=false --datadir mnode1 --syncmode \'full\' --gcmode=archive --port 40605 --http --http.corsdomain=\'*\' --http.port 3545 --http.api \'personal,eth,net,web3,personal,admin,miner,txpool,debug,clique\' --bootnodes \'enode://134fd23d8e72cf41663dcee1063306a6e43b360137e97d1729a4b654fa478e7de4f756ae133bfcd896a39bf2bc4ed6e078679a69d5248e363b4ee399bd4e6e54@185.249.227.141:0?discport=40606, enode://7212b69187bedf26b75fdec9dce7e2f9013c78590a04e7c24a09fd4a843223b6aacc6d78d1b5c4f784592bc1baf4edf9e29ff929a8457bf04ce652d6797ddf34@185.249.227.142:40605?discport=40606, enode://9f93c84d86ed8ef6342760a0c2bc5fd47255ab4fc1dbc8e064d2d11107268e295a2fb36b34b64e79ef8059794cfe5fff1a3fffc6b4eca1520c3458bd79dfca5e@161.97.115.236:40605?discport=40606, enode://412255d67f1460478f54505bb1a5bb4f7b55db7c5a9f569da9d9325db09268ec87baa9df4738ec4e5d96824a29a9d8f082e1d59dfec2c7ec310ae401742c7a8d@178.238.237.90:40605?discport=40606, enode://cad2f1f3191c5e008d6a49061bb02009d93a7b634806686a9bb181ff4a2f5a4350663a827205e2bac3881e67bb67a034a308d17f157e04de84533308e009c73e@95.111.234.144:40605?discport=40606, enode://a535db073e8cbb0b1b1eb6cb235d9e893fe5dcefc81366839b5ffcbde07b3d14b7c7f3df42c675c8e8a768e873e527f969f34cafbf06119101a0992e9110668d@178.18.254.7:40605?discport=40606\' --networkid 65450 -unlock \'0x00\' --password ./password.txt --mine --allow-insecure-unlock" --name "start-node4" -- start', shell=True)

### 3 time.sleep(5)
    subprocess.call('geth attach http://localhost:3545', shell=True)
Este bloque espera 5 segundos utilizando time.sleep y luego ejecuta el comando geth attach para conectarse a una instancia de Geth en el puerto 3545.
    
### 4. quinto bloque
      time.sleep(5)
      peers = [
          # Lista de enlaces de pares
      ]

      for peer in peers:
          subprocess.call(f'geth attach http://localhost:3545 --exec "admin.addPeer(\'{peer}\')"', shell=True)
          time.sleep(1)
          
 Este bloque espera 5 segundos y luego itera sobre una lista de enlaces de pares (peers). Para cada enlace de par, se ejecuta el comando geth attach con la opción --exec para llamar a la función admin.addPeer() y agregar el par especificado.

### 5.for _ in range(5):
    time.sleep(2)
    subprocess.call('geth attach http://localhost:3545 --exec "net.peerCount"', shell=True)
Este bloque itera 5 veces y, en cada iteración, espera 2 segundos y luego ejecuta el comando geth attach para obtener el recuento de pares utilizando net.peerCount.


### 6. Termina la secuencia
    time.sleep(2)
    subprocess.call('pm2 log 1', shell=True)



