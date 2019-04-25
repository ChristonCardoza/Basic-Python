import paramiko
import getpass 

def sshCommand(hostname, port, username, password, command):
    sshClient = paramiko.SSHClient()
    sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    sshClient.load_system_host_keys()
    sshClient.connect(hostname,port,username,password)
    stdin, stdout, stderr = sshClient.exec_command(command)
    print(stdout.read())

if __name__ == '__main__':
    hostname    = input("Enter hostname : ")
    port        = input("Enter  port : ")
    username    = input("Enter username : ")
    password    = getpass.getpass("Enter password :")
    command     = input("command : ")
    sshCommand(hostname, port, username, password, command) 
