# Proxmox-RPC

Poxmox RPC is a server and client for manage your proxmox of a remote way.

Proxmox RPC provide of:

* A server
* A client

## Install and start Promxox-RPC in proxmox server

* Download the code

``` bash
$ wget https://github.com/eddynelson/proxmox_rpc/archive/master.tar.gz
```

* Unzip code

``` bash
$ tar -xzf [filename].tar.gz
```

* Start RPC server

```
$ cd [filename]
$ sudo ./bin/server.py --port 4242
```

## Install in your client

* Download the code

``` bash
$ git clone https://github.com/eddynelson/proxmox_rpc.git
```