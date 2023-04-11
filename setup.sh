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


apt install nginx -y

apt install software-properties-common -y

add-apt-repository ppa:deadsnakes/ppa -y

apt update

apt install python3.10 -y;

# run python cli
if test -f "./reality.py" ; then
    python3 ./reality.py
fi