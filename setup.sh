# reality_setup.sh

# enable bbr
if ! echo "net.core.default_qdisc=fq" | grep -q "net.core.default_qdisc=fq" /etc/sysctl.conf ; then
    echo "enabling bbr step 1"
    echo "net.core.default_qdisc=fq" >> /etc/sysctl.conf
fi

if ! echo "net.ipv4.tcp_congestion_control=bbr" | grep -q  "net.ipv4.tcp_congestion_control=bbr" /etc/sysctl.conf ; then
    echo "enabling bbr step 2"
    echo "net.ipv4.tcp_congestion_control=bbr" >> /etc/sysctl.conf
fi

sysctl -p

# install xray x2
bash -c "$(curl -L https://github.com/XTLS/Xray-install/raw/main/install-release.sh)" @ install --version 1.8.0 -u root

if  echo "Xray Not Found" | grep -q `xray -version` ; then
    echo "ERROR: Unable to install Xray 1.8.0"
    exit
fi

apt install nginx -y

if ! echo "nginx Not Found" | grep -q `nginx -v` ; then
    echo "ERROR: Unable to install nginx"
    exit
fi

apt install certbot python3-certbot-nginx -y;

certbot --nginx -d;

# run python cli