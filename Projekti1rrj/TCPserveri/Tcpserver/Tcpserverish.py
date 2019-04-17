import socket
import sys
from _thread import *
from datetime import datetime
import random
import math
from socket import gethostname


host =''
serverPort = 12000;
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
try:
    serverSocket.bind((host, serverPort));
except socket.error as err:
    print(str(err));

print('Serveri u startua ne localhost:'+str(serverPort));
serverSocket.listen(10);
print('Serveri eshte i gatshem te pranoj kerkesa');



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
    
def FIBONNACI(numri):  
   if numri <= 1:
       return numri;
   else:
       return(FIBONNACI(numri-1) + FIBONNACI(numri-2));

#funksioni per perpunimin e kerkeses qe dergohet nga klienti.
def perpunimi_kerkeses(kerkesa,conn,addr):

    if(kerkesa[0]=='IPADRESA'):
        conn.send(str.encode(" IP Adresa e klientit është:"+addr[0]));

    elif(kerkesa[0]=='NUMRIIPORTIT'):
       conn.send(str.encode("Klienti është duke përdorur portin "+str(addr[1])));

    elif(kerkesa[0]=='BASHTINGLLORE'):
        try:
            inputi="";
            inputi=inputi.join(kerkesa[1]);          #ruajme fjaline ne nje string s
            count = 0;
            bashtinglloret = set("bcdfghjklmnpqrstvxzBCDFGHJKMNPQRSTVXZ");
            for letter in inputi:             #iterojme neper cdo shkronje te stringut
                if letter in bashtinglloret:    #nese shkronja ne iterim gjindet tek bashtinglloret rritet count
                    count += 1;
            conn.send(str.encode("Teksti i pranuar përmban "+ str(count) +"  bashtingllore"));
        except IndexError:
            conn.send(str.encode("Shenoni nje fjali pas kerkeses BASHTINGLLORE!"));

    elif(kerkesa[0]=='PRINTIMI'):
        try:
            inputi="";
            inputi=str.join(" " , kerkesa[1:]);
            conn.send(str.encode("Fjalia e dhene per printim "+inputi));
        except IndexError:
            conn.send(str.encode("Ju lutem shenoni nje fjali pas kerkeses PRINTO"));
            
    elif(kerkesa[0]=='EMRIIKOMPJUTERIT'):
        try:
            emriikompjuterit=socket.gethostname();
            conn.send( str.encode("Emri i kompjuterit është "+emriikompjuterit));
        except error:
            conn.send(str.encode("Emri i kompjutert nuk dihet."))

    elif(kerkesa[0]=='KOHA'):
        koha=datetime.now().strftime('%Y-%m-%d %H:%M:%S');
        conn.send(str.encode(koha));

    elif(kerkesa[0]=='LOJA'):
        srand= '';
        for x in range(7):
            rand= random.randint(1,49); #numer i zakonshem
            randString = str(rand) + " "; #konvertohet ne string
            srand += randString;           #te gjithe numrat ne string
        conn.send(str.encode(srand));

    elif(kerkesa[0]=='FIBONACCI'):
        try:
            numri=FIBONACCI(int(kerkesa[1]));
            conn.send(str.encode(str(numri)));
        except IndexError:
            conn.send(str.encode("Ju lutem shenoni nje shifer pas kerkeses FIBONACCI")); 
        except ValueError:
            conn.send(str.encode("Ju lutem shenoni nje shifer pas kerkeses FIBONACCI"));

    elif(kerkesa[0]=='KONVERTIMI'):
        Stringu="Mundesite per konvertime:\nKliowatt-to-Hoursepower  \nHorsepower-to-Kilowatt  \nDegrees-to-Radian \nRadian-to-Degrees \nGallons-to-Liters \nLiters-to-Gallons";
      
        try:
            input=kerkesa[1];
            outputi=float(kerkesa[2]);
            conn.send(str.encode(str(KONVERTIMI(input,outputi))));
        except IndexError:
            conn.send(str.encode("Ju lutem shenoni cka deshironi te konvertoni pastaj shifren! \n"+Stringu));
        except ValueError:
            conn.send(str.encode("Ju lutem shenoni cka deshironi te konvertoni pastaj shifren! \n" +Stringu));

#2 Metodat plus
    elif(kerkesa[0]=='MOSHAEKLIENTIT'):
        try:
            vitiilindjes= int(kerkesa[1]);
            vitimomental =2019;
            mosha = (vitimomental-vitiilindjes);
            conn.send(str.encode(str("Mosha e klientit eshte "+mosha)));
        except IndexError:
            conn.send(str.encode("Shenoni Vitin e lindjes pas kerkeses MOSHAEKLIENTIT"));
        except ValueError:
            conn.send(str.encode("Ju lutem shenoni  njeren nga kerkesat"));

    elif(kerkesa[0]=='KTHEFJALINE'):
       try:
           fjalia="";
           fjalia=str.join(" " , kerkesa[1]);
           fjalia=str.reverse();
           conn.send(str.encode("Fjalia e dhene per ta kthyer eshte "+fjalia));
       except IndexError:
            conn.send(str.encode("Ju lutem shenoni nje fjali pas kerkeses KTHEFJALIN"));
       except ValueError:
            conn.send(str.encode("Ju lutem shenoni  njeren nga kerkesat"));
            

    else:
        conn.send(str.encode("Ju lutem shenoni njerat nga kerkesat!"));
    
def klient_thread(kerkesa,conn,addr):
    while True:
        try:
            data=conn.recv(1024);
            kerkesa1 = data.decode('utf-8');
            kerkesa = kerkesa1.split();
            try:
                perpunimi_kerkeses(kerkesa,conn,addr);
            except IndexError:
                conn.send(str.encode("Kerkesa nuk eshte valide!"))
        except OSError:
            conn.close();
   


while True: 
    connectionSocket, addr = serverSocket.accept();
    print('Klienti u lidh ne serverin %s me port %s' % addr);
    start_new_thread(klient_thread,(connectionSocket,addr,));
