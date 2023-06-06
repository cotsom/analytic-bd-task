#! /bin/bash

docker-compose up --build -d
sleep 2
docker exec db /app/initdb.sh > /dev/null
docker exec db psql -U root -d technique -c "select * from products;"
docker exec db psql -U root -d technique -c "select * from suppliers;"
docker exec db psql -U root -d technique -c "select * from customers;"
docker exec db psql -U root -d technique -c "select * from orders;"
docker exec db psql -U root -d technique -c "select * from orderDetails;"