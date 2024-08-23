# do:
# 	docker build -t obahamondev/speech .	
# 	docker tag obahamondev/speech:latest obahamondev/speech:latest
# 	docker login
# 	docker push obahamondev/speech:latest

do:
	nohup uvicorn main:app --host 0.0.0.0 --port 8888 &