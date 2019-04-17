
from socket import *
import random
import socket
from datetime import datetime
import random
import time
import re
import string 
import _thread
import math

serverPort=1200
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);#krijojm metoden e serverit
server_socket.bind(('', 12000)); #lidhemi me ip dhe port,arsyja pse e kemi lene ne thojza '' sepse ky mundet me ndegju edhe prej nje kompjuteri tjeter jo vetem localhost
print("Serveri eshte duke punuar ne portin "+str(serverPort))

def FIBONNACI(numri):  
   if numri <= 1:
       return numri;
   else:
       return(FIBONNACI(numri-1) + FIBONNACI(numri-2));


def KONVERTIMI(inputi,outputi):
    if(inputi=="Kliowatt-to-Hoursepower"):
        return outputi*1.34;
    elif(inputi=="Horsepower-to-Kilowatt"):
       
        return (outputi/1.34);

    elif(inputi=="Degrees-to-Radian"):
      
        return (outputi*1.0174);

    elif(inputi=="Radian-to-Degrees"):
        return outputi/1.0174;

    elif(inputi=="Gallons-to-Liters"):
    
        return (outputi*3.785);

    elif(inputi=="Liters-to-Gallons"):
       
        return (outputi/3.785);
 

def perpunimi_kerkeses(kerkesa,conn,addr):
    if(kerkesa[0]=='IPADRESA'):
        server_socket.sendto(str.encode("IP adresa e klientit eshte: " + addr[0]), addr);

    elif(kerkesa[0]=='NUMRIIPORTIT'):
       server_socket.sendto(str.encode("Klienti është duke përdorur portin " + str(addr[1])), addr);

    elif(kerkesa[0]=='BASHTINGLLORE'):
        try:
            fjalia=kerkesa[1];           #ruajme fjaline ne nje string s
            count = 0;
            bashtingllore = set("bcdfghjklmnpqrstvxzBCDFGHJKMNPQRSTVXZ\u00EB");
            for letter in fjalia:             #iterojme neper cdo shkronje te stringut
                if letter in bashtingllore:    #nese shkronja ne iterim gjindet tek bashtinglloret rritet count
                    count += 1;
            server_socket.sendto(str.encode("Numri i bashtinglloreve ne tekst eshte:" + str(count)), addr);
        except IndexError:
            server_socket.sendto(str.encode("Shenoni nje fjali pas kerkeses BASHTINGLLORE!"), addr);

    elif(kerkesa[0]=='PRINTIMI'):
        try:
            kerkesa[1] = kerkesa[1].strip();
            server_socket.sendto(str.encode("Fjalia e dhene per printim "+kerkesa[1]), addr);
        except IndexError:
            server_socket.sendto(str.encode("Ju lutem shenoni nje fjali pas kerkeses PRINTIMI!"), addr);
            
    elif(kerkesa[0]=='EMRIIKOMPJUTERIT'):
        try:
            emrikompjuterit=socket.gethostname();
            server_socket.sendto(str.encode("Emri i kompjuterit është "+emrikompjuterit), addr);

        except error:
            server_socket.sendto(str.encode("Emri i kompjuterit nuk dihet"), addr);

    elif(kerkesa[0]=='KOHA'):
        time=datetime.now().strftime('%Y-%m-%d %H:%M:%S');
        server_socket.sendto(str.encode(time), addr);

    elif(kerkesa[0]=='LOJA'):
        srand= '';
        for x in range(7):
            rand= random.randint(1,49); #numer i zakonshem
            randString = str(rand) + " "; #konvertohet ne string
            srand += randString;           #te gjithe numrat ne string
        server_socket.sendto(str.encode(srand), addr);


    elif(kerkesa[0]=='FIBONACCI'):
        try:
            print(int(kerkesa[1]));
            numri=FIBONACCI(int(kerkesa[1]));
            server_socket.sendto(str.encode(str(numri)), addr);
        except IndexError:
            server_socket.sendto(str.encode("Shenoni nje numer pas kerkeses FIBONACCI"), addr);
        except ValueError:
            server_socket.sendto(str.encode("Shenoni nje numer pas kerkeses FIBONACCI"), addr);
    
    elif(kerkesa[0]=='KONVERTIMI'):
        string="Mundesite per konvertime:\nKliowatt-to-Hoursepower  \nHorsepower-to-Kilowatt  \nDegrees-to-Radian \nRadian-to-Degrees \nGallons-to-Liters \nLiters-to-Gallons";
      
        try:
            inputi=kerkesa[1];
            outputi=float(kerkesa[2]);
            server_socket.sendto(str.encode(str(KONVERTIMI(inputi,outputi))), addr);
        except IndexError:        
            server_socket.sendto(str.encode("Ju lutem shenoni cka deshironi te konvertoni pastaj shifren! \n" +string), addr);
        except ValueError:
            server_socket.sendto(str.encode("Ju lutem shenoni cka deshironi te konvertoni pastaj shifren!\n "+string), addr);
    
    elif(kerkesa[0]=='MOSHAEKLIENTIT'):
        try:
            vitiilindjes= int(kerkesa[1]);
            vitimomental =2019;
            mosha = (vitimomental-vitiilindjes);
            conn.send(str.encode(str("Mosha e klienti eshte"+mosha),addr));
        except IndexError:
            conn.send(str.encode("Shenoni Vitin e lindjes pas kerkeses MOSHAEKLIENTIT"),addr);
        except ValueError:
            conn.send(str.encode("Ju lutem shenoni  njeren nga kerkesat"),addr);

    elif(kerkesa[0]=='KTHEFJALINE'):
       try:
           fjalia="";
           fjalia=str.join(" " , kerkesa[1]);
           fjalia=str.reverse();
           conn.send(str.encode("Fjalia e dhene per ta kthyer eshte "+fjalia),addr);
       except IndexError:
            conn.send(str.encode("Ju lutem shenoni nje fjali pas kerkeses KTHEFJALIN"),addr);
       except ValueError:
            conn.send(str.encode("Ju lutem shenoni  njeren nga kerkesat"),addr);

def klient_thread(conn,addr):
    while True:
        try:
            data=conn.recv(1024);
            kerkesa = data.decode('utf-8');
            kerkesaVarg = kerkesa.split();
            try:
                perpunimi_kerkeses(kerkesaVarg,conn,addr);
            except IndexError:
                conn.send(str.encode("Kerkesa nuk eshte valide!"))
        except OSError:
            conn.close();
    conn.close();

  
while True:
    kerkesa, addr = server_socket.recvfrom(1024);
    kerkesa = kerkesa.decode('utf-8');
    kerkesa= kerkesa.split();
    perpunimi_kerkeses(kerkesa,server_socket,addr);
