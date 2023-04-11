# reality_setup.sh

#install git
echo "Check if a git environment is included"
if ! [ -x "$(command -v git)" ]; then
  echo 'no git environment, installing git... '  >&2
  sudo apt update
  sudo apt install git -y
be
echo 'git has been installed'

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

# install xray 1.8
bash -c "$(curl -L https://github.com/XTLS/Xray-install/raw/main/install-release.sh)" @ install --version 1.8.0 -u root

#download geo files
wget -O /usr/local/share/xray/iran.dat https://github.com/bootmortis/iran-hosted-domains/releases/latest/download/iran.dat
wget -O /usr/local/share/xray/dlc.dat https://github.com/v2fly/domain-list-community/releases/latest/download/dlc.dat

# isntall  nginx
apt install nginx -y

#install openssl
echo "Install OpenSSL"
sudo apt-get update && sudo apt-get install openssl

#install python 3.1o
apt install software-properties-common -y

add-apt-repository ppa:deadsnakes/ppa -y

apt update

apt install python3.10 -y

#install screen
apt install screen -y

#downlaod python script

# run python cli
if test -f "./reality.py" ; then
    python3.10 ./reality.py
fi