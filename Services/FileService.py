import paramiko

class FileService:

    @staticmethod
    def getFileContentAsArray(host, user, secret, port, fileName):

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=host, username=user, password=secret, port=port)
        sftp_client = client.open_sftp()
        file = sftp_client.open(fileName)
        lines = file.readlines()
        client.close()

        return lines
