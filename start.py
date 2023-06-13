import subprocess
import time

# Primero REMPLAZA OXOO POR TU DIRECCION
subprocess.call('pm2 start "./geth -snapshot=false --datadir mnode1 --syncmode \'full\' --gcmode=archive --port 40605 --http --http.corsdomain=\'*\' --http.port 3545 --http.api \'personal,eth,net,web3,personal,admin,miner,txpool,debug,clique\' --bootnodes \'enode://134fd23d8e72cf41663dcee1063306a6e43b360137e97d1729a4b654fa478e7de4f756ae133bfcd896a39bf2bc4ed6e078679a69d5248e363b4ee399bd4e6e54@185.249.227.141:0?discport=40606, enode://7212b69187bedf26b75fdec9dce7e2f9013c78590a04e7c24a09fd4a843223b6aacc6d78d1b5c4f784592bc1baf4edf9e29ff929a8457bf04ce652d6797ddf34@185.249.227.142:40605?discport=40606, enode://9f93c84d86ed8ef6342760a0c2bc5fd47255ab4fc1dbc8e064d2d11107268e295a2fb36b34b64e79ef8059794cfe5fff1a3fffc6b4eca1520c3458bd79dfca5e@161.97.115.236:40605?discport=40606, enode://412255d67f1460478f54505bb1a5bb4f7b55db7c5a9f569da9d9325db09268ec87baa9df4738ec4e5d96824a29a9d8f082e1d59dfec2c7ec310ae401742c7a8d@178.238.237.90:40605?discport=40606, enode://cad2f1f3191c5e008d6a49061bb02009d93a7b634806686a9bb181ff4a2f5a4350663a827205e2bac3881e67bb67a034a308d17f157e04de84533308e009c73e@95.111.234.144:40605?discport=40606, enode://a535db073e8cbb0b1b1eb6cb235d9e893fe5dcefc81366839b5ffcbde07b3d14b7c7f3df42c675c8e8a768e873e527f969f34cafbf06119101a0992e9110668d@178.18.254.7:40605?discport=40606\' --networkid 65450 -unlock \'OXOO\' --password ./password.txt --mine --allow-insecure-unlock" --name "start-node4" -- start', shell=True)

# Segundo
time.sleep(5)
subprocess.call('geth attach http://localhost:3545', shell=True)

# Tercero
time.sleep(5)
peers = [
    "enode://134fd23d8e72cf41663dcee1063306a6e43b360137e97d1729a4b654fa478e7de4f756ae133bfcd896a39bf2bc4ed6e078679a69d5248e363b4ee399bd4e6e54@185.249.227.141:40605",
    "enode://7212b69187bedf26b75fdec9dce7e2f9013c78590a04e7c24a09fd4a843223b6aacc6d78d1b5c4f784592bc1baf4edf9e29ff929a8457bf04ce652d6797ddf34@185.249.227.142:40605",
    "enode://9f93c84d86ed8ef6342760a0c2bc5fd47255ab4fc1dbc8e064d2d11107268e295a2fb36b34b64e79ef8059794cfe5fff1a3fffc6b4eca1520c3458bd79dfca5e@161.97.115.236:40605",
    "enode://412255d67f1460478f54505bb1a5bb4f7b55db7c5a9f569da9d9325db09268ec87baa9df4738ec4e5d96824a29a9d8f082e1d59dfec2c7ec310ae401742c7a8d@178.238.237.90:40605",
    "enode://9b660deb576829cdb9e4880803e08756f23a243f4b70c973545cb4ba23d1704e72c15f18eefe936b8aae5e5305ea7abf3c6091bd449bb3f2f53179e20c0a19f6@181.58.120.108:40605",
    "enode://cad2f1f3191c5e008d6a49061bb02009d93a7b634806686a9bb181ff4a2f5a4350663a827205e2bac3881e67bb67a034a308d17f157e04de84533308e009c73e@95.111.234.144:40605",
    "enode://a535db073e8cbb0b1b1eb6cb235d9e893fe5dcefc81366839b5ffcbde07b3d14b7c7f3df42c675c8e8a768e873e527f969f34cafbf06119101a0992e9110668d@178.18.254.7:40605",
    "enode://892fd892e4b4b913c71b9cde0d96f78e5153e820b67e1c6324d7ea0ee5dabff2ab0378d16a755e875e7dc222ad714a50265dbc99a632aab99e9041dfd265344f@127.0.0.1:40605",
    "enode://00ecee62647d4ef07b4c7f00d652f84b87b0281811166904c5b3b44794963f718adb038042dcfb18bd786807229e677391e0f65dcaa5a452b701b702cb265fab@161.97.115.236:40605",
    "enode://e6572aa09835ccac9cb8a551a34ec034254673e7c57babc86b15d134cab5e87da312b42c3daa4ace26324bbd74b7fbffbff7fab81a27819536e197b207624e49@178.238.237.90:40605",
    "enode://cad2f1f3191c5e008d6a49061bb02009d93a7b634806686a9bb181ff4a2f5a4350663a827205e2bac3881e67bb67a034a308d17f157e04de84533308e009c73e@95.111.234.144:40605",
    "enode://959d8bb2ce01393a7943920e3db2dddfa6b31ff56bcf74bfb722b7d7aa22ec6545d03932c99eae327d45e6072ba3fe8135497e8e05f2b6b3fff683080a04ffc9@178.18.254.7:40605",
    "enode://534c5a23a1d474dae249883cfa4937240d731ce2ae519c772f64c9278aec8000188468550e82a98704f61e20c4a87de16f63c07b7c311eb91ca108531c86a055@181.58.120.108:40605"
]

for peer in peers:
    subprocess.call(f'geth attach http://localhost:3545 --exec "admin.addPeer(\'{peer}\')"', shell=True)
    time.sleep(1)

# Cuarto
for _ in range(7):
    time.sleep(2)
    subprocess.call('geth attach http://localhost:3545 --exec "net.peerCount"', shell=True)

# Después de terminar la secuencia
time.sleep(15)
subprocess.call('pm2 log 1', shell=True)

# Siguiendo a esto después de 2 segundos
time.sleep(17)
subprocess.call('pm2 list', shell=True)

# Después de 12 segundos
time.sleep(19)
subprocess.call('pm2 save', shell=True)
