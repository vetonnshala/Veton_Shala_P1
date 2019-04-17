
import socket
import sys 
import select
serverName = input("Shenoni emrin e serverit:");
Port = input("Shenoni portin:");
serverPort = int(Port);

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
s.connect((serverName,serverPort));
while True:
    print("-----------------------------------------------------------------------------------------------------")
    Kerkesa=input("Zgjedhni njeren nga kerkesat: \n IPADRESA\n NUMRIIPORTIT\n BASHTINGLLORE\n PRINTIMI\n EMRIIKOMPJUTERIT\n KOHA\n LOJA\n FIBONACCI\n"+
              " KONVERTIMI\n MOSHAEKLIENTIT\n KTHEFJALIN\n" +
              " Ose shenoni 0 per ta mbyllur programin\n ");
    Kerkesa=Kerkesa.strip(); #The strip() method kthen vetem string duke hequr te gjithe karakteret tjera
    if len(Kerkesa) > 128:
        print("Kerkesa nuk mund te jete me e gjate se 128 karaktere!");
        continue;
    if not Kerkesa:
        print("Ju lutem shenoni nje kerkese!");
        continue;
    if Kerkesa == "0":
        s.close();
        break;
    s.sendall(str.encode(Kerkesa));
    data = s.recv(1024);
    data = data.decode('utf-8');
    print(data);
