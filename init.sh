#!/usr/bin/bash

sudo ﻿ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo rm /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

#sudo ﻿ln -s /home/box/web/etc/gunicorn.conf  /etc/gunicorn.d/test
#sudo gunicorn -b 0.0.0.0:8080 hello.application
