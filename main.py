import paramiko

host = '0.0.0.0'
user = 'root'
secret = 'secret'
port = 20022

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print(3)
sftp_client = client.open_sftp()
file = sftp_client.open("/var/www/logs/error.log")
Lines = file.readlines()
# Strips the newline character
for line in Lines:
    print(line.strip())
client.close()
