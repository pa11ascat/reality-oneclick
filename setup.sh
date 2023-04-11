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

if ! echo "Xray 1.8.0" | grep -q "Xray 1.8.0" `xray -version` ; then
    echo "ERROR: Unable to install Xray 1.8.0"
    exit
fi

apt install nginx -y

if ! echo "nginx version:" | grep -q "nginx version:"git `nginx -v` ; then
    echo "ERROR: Unable to install nginx"
    exit
fi

apt install python3 -y;

# run python cli
if test -f "./reality.py" ; then
    python3 ./reality.py
fi