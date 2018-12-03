import socket, fileinput

filename = "./smbionet/SMBIONET.md"
with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
    for line in file:
        print(line.replace("localhost", socket.gethostbyname(socket.gethostname())))