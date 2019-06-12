import zerorpc
import sys
import os
import getpass
import base64
import subprocess
import random
import pickle
import re
import argparse
from simplecrypt import encrypt, decrypt

FILE_PASS = 'proxmoxserverrpc'
DIR_PASS = '/home/eddydecena/projects/proxmox_rpc/%s' % FILE_PASS


class ProxmoxServerRPC(object):
    def _login_error(self):
        pass

    def login(self, password):
        infile = open(DIR_PASS, 'rb')
        credential = pickle.load(infile)
        infile.close()

        p = decrypt(credential["secret"], credential['password']).decode()
        
        if p != password:
            return { "message": "Authentication error, password not match" }

        self._password = p
        return { "message": "Login success!!"  }

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', help="Server RPC port, default 4242")
    args = parser.parse_args()

    # evalute the file of password 
    proc =  subprocess.Popen(
      'ls %s' % (DIR_PASS), 
      shell=True,
      stdout=subprocess.PIPE, 
      stderr=subprocess.PIPE
    )

    stderr = proc.stderr.read().decode()

    # if not password file, create new password file
    if re.search(r'No such file or directory', stderr):
        #get password
        password = getpass.getpass('Password for proxmox RPC server: ', stream=None)
        
        #create secret
        secret = str(random.random())
        secret_encode = base64.b64encode(bytes(secret, 'utf-8'))

        #encrypt password
        password_encrypt = encrypt(secret_encode, password)

        credential = {
          "secret": secret_encode,
          "password": password_encrypt
        }

        outfile = open(DIR_PASS, 'wb')
        pickle.dump(credential, outfile)
        outfile.close()

    s = zerorpc.Server(ProxmoxServerRPC())
    if args.port:
        s.bind('tcp://0.0.0.0:%s' % (args.port))
    else:
        s.bind('tcp://0.0.0.0:4242')
    s.run()




    