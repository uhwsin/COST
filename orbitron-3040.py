import time
import dde
import serial

#Go
el_bias = 0
ptz_address = 0x01
com_port ="COM1"
baud_rate = 2400
def show_item(value,item):
    print(item)

def Check_sum(command):
    return ((command[0]+command[1]+command[2]+command[3]+command[4]+command[5]+0X00 )   % 255)
def Pelco_D_Set_AZ(az):
    Command_str = [0xFF,ptz_address,0x00,0x4B,0x00,0x00,0x00]
    az = az*100
    Command_str[4] = int(az//256)
    Command_str[5] = int(az % 256)
    #Command_str = [0xFF,ptz_address,0x4B,0x00,0x00,0x00]
    Command_str[6] = Check_sum(Command_str)
    return Command_str

def Pelco_D_Set_EL(el):
    Command_str = [0xFF,ptz_address,0x00,0x4D,0x00,0x00,0x00]
    el = (90-el)*100
    #correct the error
    el = el*1.077 +0.3887  
    Command_str[4] = int(el//256)
    Command_str[5] = int(el % 256)
    #Command_str = [0xFF,ptz_address,0x4D,0x00,0x00,0x00]
    Command_str[6] = Check_sum(Command_str)
    return Command_str
    
if __name__ == "__main__":
    try:
        ser = serial.Serial(com_port,baud_rate)
    except:
        print("Com port open error!")
    
    #get connect with server SPnet
    dde0 = dde.DDEClient("Orbitron", "Tracking")
    #dde0.advise("TrackingData")
    #dde0.execute("TUNE ON")
    print("Hello")
    #dde.WinMSGLoop()
    while True:
    #    print (dde0.advise("AZ"))
         a=dde0.request("TrackingData")
         time.sleep(1)
         print(a)
         if(a!=None):
             if(len(a)>2):
                 b=a.split()
                 print(b[1])
                 print(b[2])
                 az = float(b[1][2:])
                 el = float(b[2][2:])
                 if (el > -2.0 ):
             
                     if(el < 0):
                         el = 0
                     #print(el+el_bias)
                     ser.write(Pelco_D_Set_AZ(az))
                     time.sleep(0.3)
                     ser.write(Pelco_D_Set_EL(el))
    #dde.WinMSGLoop()
