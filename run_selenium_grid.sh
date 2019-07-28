docker network create grid;
docker run -d --name website -v $(pwd)/tests/html:/usr/share/nginx/html:ro --hostname website --net grid nginx;
docker run -d -p 4444:4444 --net grid --name selenium-hub selenium/hub:3.141.59-selenium;
docker run -d --net grid --link website -e HUB_HOST=selenium-hub -v /dev/shm:/dev/shm selenium/node-chrome:3.141.59-selenium;
docker run -d --net grid --link website -e HUB_HOST=selenium-hub -v /dev/shm:/dev/shm selenium/node-firefox:3.141.59-selenium;
sh wait_for_grid.sh;