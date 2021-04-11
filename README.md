# Iris_prediction_with_flask

1. Inside this current working directory

2. Start docker

3. Build the docker image 
	* `docker build -t anyName_api .`

4. List docker images 
	* `docker images`

5. Run demo docker image also bind port of host machine with webserver port
	* `docker run -d -p 8000:8000 anyName_api`
	---	OR	---
5. Run docker image also bind port of host machine with doker/fask port
	* `docker run -p 5000:5000 anyName_api`


6. check logs (location we mannualy set for log information)
	* `docker ps`
	* `docker exec -it container-id bash`
	* `cd /etc/mod_wsgi-experss-80`
	* `vim error_log`

7. Stop running docker image
	* `docker ps`
	* `docker stop container-id`



