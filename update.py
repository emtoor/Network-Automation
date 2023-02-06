import paramiko
import ftplib
import socket

def upgrade_firmware(ftp_client, firmware_file):
    with open(firmware_file, "rb") as file:
        ftp_client.storbinary("STOR " + firmware_file, file)
    ftp_client.quit()

def check_device_info(ssh_client, model, firmware_version):
    stdin, stdout, stderr = ssh_client.exec_command("show version")
    output = stdout.read().decode()
    if model in output and firmware_version in output:
        
        # Upgrade the firmware on the device
        stdin, stdout, stderr = ssh_client.exec_command("request system software add /var/tmp/firmware_file.tgz")
        output = stdout.read().decode()
        print(output)
        
        
        # Reboot the device
        #stdin, stdout, stderr = ssh_client.exec_command("request system reboot")
        #output = stdout.read().decode()
        #print(output)
        
        
        return True
    return False

def main():
    start_ip = input("Enter start IP address: ")
    end_ip = input("Enter end IP address: ")
    model = input("Enter Juniper model: ")
    firmware_version = input("Enter firmware version: ")
    username = input("Enter SSH username: ")
    password = input("Enter SSH password: ")
    firmware_file = input("Enter firmware file path: ")

    for i in range(int(start_ip.split(".")[-1]), int(end_ip.split(".")[-1]) + 1):
        ip = start_ip[:-len(start_ip.split(".")[-1])] + str(i)
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh_client.connect(ip, username=username, password=password)
            ftp_client = ftplib.FTP(ip)
            ftp_client.login(username, password)
            if check_device_info(ssh_client, model, firmware_version):
                upgrade_firmware(ftp_client, firmware_file)
            ftp_client.close()
            ssh_client.close()
        except (paramiko.ssh_exception.NoValidConnectionsError, socket.timeout):
            print("Could not connect to device: " + ip)

if __name__ == "__main__":
    main()
