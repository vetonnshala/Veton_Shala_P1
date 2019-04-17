import time
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
serverName = input("Shenoni emrin e serverit:");
Port = input("Shenoni portin:");
serverPort = int(Port);
addr = (serverName, serverPort);

while 1:
    print("--------------------------UDP KLIENTI---------------------------------------------------------------------------------")
    var=input("Zgjedhni njeren nga kerkesat: \n IPADRESA\n NUMRIIPORTIT\n BASHTINGLLORE\n PRINTIMI\n EMRIIKOMPJUTERIT\n KOHA\n LOJA\n FIBONACCI\n"+
              " KONVERTIMI\n MOSHAEKLINETIT\n KTHEFJALIN\n" +
              " Ose shenoni 0 per ta mbyllyr programin\n ");
    if not var:
        print("Ju lutem shenoni njeren nga kerkesat!");
        continue;
    if var == "0":
        client_socket.close();
        break;
    client_socket.sendto(var.encode(),addr); 
    try:
        data, server = client_socket.recvfrom(1024);
        data = data.decode('utf-8');
        print(data);
    except socket.timeout:
        print('REQUEST TIMED OUT');
    finally:
        print("-----------------------------------------------------------------------------------------------------------")

