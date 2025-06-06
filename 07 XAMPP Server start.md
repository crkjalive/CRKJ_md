# Instalar xampp en ubuntu

### cambiar permisos de instalador  
> chmod 755 xampp-linux-*-installer.run

### ejecutar el instalador
> sudo ./xampp-linux-*-installer.run

### levantar xampp
sudo /opt/lampp/lampp start

### detener xampp
sudo /opt/lampp/lampp stop

### recargar xampp
sudo /opt/lampp/lampp reload

### solo un servicio start and stop and reload

sudo /opt/lampp/lampp 

1. startapache - stopapache - reloadapache
2. startssl - stopssl - reloadssl
3. startmysql - stopmysql - reloadmysql
4. startftp - stopftp - reloadftp

# Linux Ubuntu
Levantar el servidor con el arranque del sistema en Ubuntu 

### Crear el Archivo de Servicio
1. sudo nano /etc/systemd/system/xampp.service

reemplazar el contenidor por estas lineas  

~~~
[Unit]
Description=XAMPP Apache + MariaDB + ProFTPD

[Service]
Type=forking
ExecStart=/opt/lampp/lampp start
ExecStop=/opt/lampp/lampp stop
RemainAfterExit=yes
Restart=on-failure

[Install]
WantedBy=multi-user.target
~~~

## recargar al sistema nuestro archivo
1. sudo systemctl daemon-reload

## habilitar el servicio
1. sudo systemctl enable xampp.service

## Comprobando del servicio
1. sudo systemctl start xampp.service
2. sudo systemctl status xampp.service
3. sudo systemctl stop xampp.service










