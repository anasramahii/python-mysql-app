.PHONY: help up down restart logs build rebuild stop start ps clean

help:
	@echo "Docker Compose Commands:"
	@echo "  make up          - Start all containers in detached mode"
	@echo "  make down        - Stop and remove all containers"
	@echo "  make restart     - Restart all containers"
	@echo "  make build       - Build or rebuild services"
	@echo "  make rebuild     - Force rebuild all services"
	@echo "  make stop        - Stop all containers without removing them"
	@echo "  make start       - Start existing containers"
	@echo "  make logs        - View logs from all containers"
	@echo "  make logs-f      - Follow logs in real-time"
	@echo "  make ps          - List all containers"
	@echo "  make clean       - Remove all containers, networks, and volumes"
	@echo "  make pull        - Pull latest images"

up:
	docker-compose up -d

down:
	docker-compose down

restart: down up

build:
	docker-compose build

rebuild:
	docker-compose build --no-cache
	

stop:
	docker-compose stop

start:
	docker-compose start

logs:
	docker-compose logs

logs-f:
	docker-compose logs -f

ps:
	docker-compose ps

clean:
	docker-compose down -v

pull:
	docker-compose pull

# Additional utility commands
shell:
	docker-compose exec -it web /bin/bash

status:
	docker-compose ps -a

validate:
	docker-compose config

prune:
	docker system prune -f

prune-volumes:
	docker system prune -f --volumes

run:
	docker run -it --rm python-docker-app-web-server	
	

# تشغيل برنامج البايثون بوضع تفاعلي (للـ Login والـ Register)
app:
	docker-compose run --rm web-server python app.py

	

.DEFAULT_GOAL := help
