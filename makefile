local-dev:
	python -m app

docker-build:
	docker build -t haas .

docker-run:
	docker run -p 80:8080 haas

docker-clean:
	docker container prune -f