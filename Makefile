include .env

dev:
	sudo docker compose -f compose.yml -p ${PROJECT_NAME} up --build

run:
	sudo docker compose -f compose.yml -p ${PROJECT_NAME} up --build -d

stop:
	sudo docker compose -f compose.yml -p ${PROJECT_NAME} stop

check:
	sudo docker ps --filter name="^${PROJECT_NAME}" --format "table {{.ID}}\t{{.Names}}\t{{.Image}}\t{{.Status}}\t{{.Ports}}"

logs:
	sudo docker logs `docker ps -a --filter name="^${PROJECT_NAME}" | grep "tg-" | cut -d ' ' -f 1`

connect:
	sudo docker exec -it `docker ps -a --filter name="^${PROJECT_NAME}" | grep "tg-" | cut -d ' ' -f 1` bash
