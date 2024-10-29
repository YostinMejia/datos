# Para la sustentación y simulación del sistema, deberán poblar su modelo de la siguiente manera: 
# Mínimo 1 millón de clientes por ende si cada cliente tiene un hogar registrado 
import csv
from faker import Faker
import random
fake = Faker()
from datetime import datetime
def write_data(file_name,data):
    with open (file_name,"w", encoding="utf-8",newline = '') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)   

# usuario = [[fake.name(),f"{random.randint(0,10000000)}{fake.free_email()}",fake.password()] for _ in range(1_000_000)]

# with open ('cliente_final.csv',"w", newline = '') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerows(usuario)                   

# 1 millón de hogares, 
# cada hogar como mínimo deberá tener 3 dispositivos para medición y monitoreo entre ellos 
# (Televisores Inteligentes, Neveras o Nevecones Inteligentes, Computadores y Aires Acondicionados); 
# todos con su detalles de consumo y 


# id_clients = [i for i in range(1630,1_000_000+1631)]
# home= [ [id, random.randint(1,6),fake.address()] for id in id_clients]

# write_data("home.csv",home)                
    

id_homes = [i for i in range(3000005,1_000_000+3000006)]

# Nombres de dispositivos
devices = [
    "Televisor QLED", "Televisor OLED", "Televisor LED X1", "Televisor UHD", "Televisor 4K Smart", "Televisor 8K Premium",
    "Nevera Inteligente X3", "Nevera Inteligente K3", "Nevera Frost", "Nevera EcoCool", "Nevera DuoCool", "Nevera MaxiFresh",
    "Lavadora ProWash", "Lavadora TurboClean", "Lavadora EcoWash", "Lavadora UltraSpin", "Lavadora QuickDry", "Lavadora AquaJet",
    "Aire Acondicionado CoolAir", "Aire Acondicionado EcoCooler", "Aire Acondicionado FreezePro", "Aire Acondicionado UltraFreeze",
    "Aire Acondicionado WhisperQuiet", "Aire Acondicionado PureAir", "Horno Microondas Inverter", "Horno Microondas PowerWave",
    "Horno Microondas SteamBake", "Horno Inteligente SteamPlus", "Horno Eléctrico SmartBake", "Horno GasTurbo",
    "Secadora HeatWave", "Secadora EcoDry", "Secadora ProDry", "Secadora MaxDry", "Secadora QuickDryer", "Secadora CompactHeat",
    "Aspiradora Robótica CleanBot", "Aspiradora Inteligente RoboVac", "Aspiradora MaxClean", "Aspiradora TurboPower",
    "Aspiradora Silencio", "Aspiradora DustBuster", "Purificador de Aire PureSense", "Purificador de Aire CleanAir",
    "Purificador de Aire AirGuard", "Purificador de Aire EcoAir", "Purificador de Aire HealthGuard", "Purificador de Aire AntiAllergy",
    "Cafetera SmartBrew", "Cafetera Express", "Cafetera ProBarista", "Cafetera CafeMaster", "Cafetera QuickBrew", "Cafetera CappuccinoPlus",
    "Calentador de Agua WaterHeat", "Calentador de Agua InstantWarm", "Calentador de Agua TurboHeat", "Calentador de Agua MaxWarm",
    "Calentador de Agua EcoHeat", "Calentador de Agua QuickWarm", "Deshumidificador DryMax", "Deshumidificador ProDry",
    "Deshumidificador AirDry", "Deshumidificador HumidGuard", "Deshumidificador QuietDry", "Deshumidificador AquaClean",
    "Ventilador TurboFan", "Ventilador SilentBreeze", "Ventilador FreshAir", "Ventilador UltraCool", "Ventilador PowerBreeze",
    "Ventilador CompactFan", "Sistema de Audio SoundMaster", "Sistema de Audio ProSound", "Sistema de Audio MegaBass",
    "Sistema de Audio ClearSound", "Sistema de Audio HomeBeat", "Sistema de Audio SmartSpeaker", "Lavavajillas AquaClean",
    "Lavavajillas PowerWash", "Lavavajillas EcoSmart", "Lavavajillas TurboWash", "Lavavajillas SilentWash", "Lavavajillas QuickWash",
    "Lámpara LED SmartLight", "Lámpara LED NightGlow", "Lámpara LED WarmGlow", "Lámpara LED PowerLite", "Lámpara LED CoolGlow",
    "Lámpara LED UltraLight", "Freidora de Aire AirFry", "Freidora de Aire HealthFry", "Freidora de Aire MaxCrunch", "Freidora de Aire CrispAir",
    "Freidora de Aire SmartFry", "Freidora de Aire QuickCrisp", "Impresora SmartPrint", "Impresora ProPrint", "Impresora UltraPrint",
    "Impresora EcoPrint", "Impresora LaserMax", "Impresora InkJet"
]
# address
# Consumo en kW por hora
expents_watts = [
    45000, 34000, 50000, 47000, 55000, 60000, 70000, 52000, 60000, 65000, 67000, 75000, 
    50000, 45000, 48000, 52000, 55000, 50000, 1200, 1300, 1100, 1500, 1700, 1000, 9000, 
    75000, 6000, 8000, 78000, 65000, 1400, 1500, 1600, 1200, 1100, 1300, 7000, 6000, 
    8000, 65000, 55000, 45000, 35000, 4000, 5000, 6000, 45000, 55000, 8000, 9000, 7000, 
    65000, 5000, 6000, 7000, 8000, 65000, 55000, 6000, 7000, 5000, 6000, 55000, 5000, 
    45000, 4000, 35000, 3000, 25000, 4000, 45000, 5000, 1200, 1400, 1100, 1300, 1200, 
    1500, 6000, 7000, 65000, 5000, 55000, 6000, 25000, 3000, 2000, 15000, 35000, 4000, 
    8000, 6000, 9000, 7000, 5000, 4000, 75000, 9000, 7000, 6000, 8000, 65000
]


data_devices = []
for id in id_homes:
    for j in range(0,3):
        r = random.randint(0,len(devices)-1)
        data_devices.append([id,devices[r],random.randint(0,100),expents_watts[r]])

# write_data("devices.csv",data_devices)


# los pagos de 1 año atrás registrados en la tabla bill.

bills =[]
b = 3
for id_home in id_homes:
    for i in range(1,13):
        b+=1
        bills.append([f"BILL{b}",id_home,random.randint(600,800),datetime(2023,i,28)])
write_data("bills.csv",bills)

