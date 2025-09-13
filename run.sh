NAME=minecraft-server-bot

docker update --restart no $NAME
docker stop $NAME

docker build -t $NAME .
docker run -d --restart always --net host -v ./data:/code/data $NAME 
