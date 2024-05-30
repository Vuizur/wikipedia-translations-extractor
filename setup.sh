# sudo apt update
# sudo apt install libmariadb-dev
# sudo apt install build-essential
# sudo apt install python3-dev
# sudo apt install mariadb-server
# You should set a password for root here
# sudo mysql_secure_installation
# TODO: Optimize database settings for fast performance
# download https://dumps.wikimedia.org/enwiki/20240520/enwiki-20240520-page.sql.gz and https://dumps.wikimedia.org/enwiki/20240520/enwiki-20240520-langlinks.sql.gz
if [ ! -f enwiki-20240520-page.sql ]; then
    wget https://dumps.wikimedia.org/enwiki/20240520/enwiki-20240520-page.sql.gz
    gunzip enwiki-20240520-page.sql.gz
fi

if [ ! -f enwiki-20240520-langlinks.sql ]; then
    wget https://dumps.wikimedia.org/enwiki/20240520/enwiki-20240520-langlinks.sql.gz
    gunzip enwiki-20240520-langlinks.sql.gz
fi
mysql -u root -p -e "CREATE DATABASE IF NOT EXISTS wikipedia"
mysql -u root -p wikipedia < enwiki-20240520-page.sql && echo "Page data imported successfully"
mysql -u root -p wikipedia < enwiki-20240520-langlinks.sql && echo "Langlinks data imported successfully"
