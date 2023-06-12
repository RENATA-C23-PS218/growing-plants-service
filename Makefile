start:
	source venv/bin/activate
	
stop:
	deactivate

build:
	docker build . --tag renata-growing-plants-service:latest

runc:
	docker run -it -d --env-file=.env -p 5000:5000 --name renata-growing-plants-service renata-growing-plants-service:latest

startc:
	docker start renata-growing-plants-service

stopc:
	docker stop renata-growing-plants-service

rmc:
	docker rm renata-growing-plants-service