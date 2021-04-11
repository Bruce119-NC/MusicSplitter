# shellcheck disable=SC2034
file_name=$1
cd /home/nabarun/Projects/MusicSplitter/data/ || exit
spleeter separate -o ../output/ $file_name