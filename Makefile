include .env

run:
	docker compose -f compose.yml -p ${PROJECT_NAME} up --build -d

stop:
	docker compose -f compose.yml -p ${PROJECT_NAME} stop

check:
	docker ps --filter name="^${PROJECT_NAME}" --format "table {{.ID}}\t{{.Names}}\t{{.Image}}\t{{.Status}}\t{{.Ports}}"

logs:
	docker logs `docker ps -a --filter name="^${PROJECT_NAME}" | grep "tg-" | cut -d ' ' -f 1`
