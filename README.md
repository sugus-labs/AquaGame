# Welcome to AquaGame #

> **NOTE:** AquaGame is currently undergoing heavy refactoring work
> to accomodate a better UI, better back end and better access. Pull at your
> own risk! :-)

The actual version is 1.0.

AquaGame is a new WebLab-Deusto type of experiment based in the aqualab to integrate a Serious Game. This game tend to be a game to learn basics of Archimedes Principles using a remote laboratory with different balls of different densities that really float on the water in real time.
There are many different Technologies implied like [Python](http://python.org) ,[Django](https://www.djangoproject.com/‎), [JavaScript](http://http://en.wikipedia.org/wiki/JavaScript/‎), [JQuery](http://jquery.com/‎), [HTML](http://en.wikipedia.org/wiki/HTML), [CSS3](http://en.wikipedia.org/wiki/CSS3#CSS_3), ...

**WARNING:**  AquaGame is still experimental.

**Hey, check out WebLab-Deusto project! <http://weblab.deusto.es>**

## Requirements ##

AquaGame is developed on a Ubuntu 12.04 system, running:

   * [Python 2.7](http://docs.python.org/2/)
   * [Django 1.5.1](https://www.djangoproject.com/‎)
   * [python-mysqldb 1.2.3](http://mysql-python.sourceforge.net/MySQLdb.html)
   * [mysql-server 5.5.32](http://www.mysql.com)
   * [Supervisord](http://http://supervisord.org/)

It might work with other versions.

## Setting up the environment and config ##

Put your terminal in the root directory of the project and type:

	$ python manage.py syncdb

and put the file supervisord.conf in the path /etc/supervisord.conf: 

	cp [AquaGame_root_path]/supervisord.conf /etc/supervisord.conf

put the file supervisord in /etc/init.d and configure it:

	cp [AquaGame_root_path]/supervisord /etc/init.d/supervisord
	sudo chmod +x /etc/init.d/supervisord
	sudo update-rc.d supervisord defaults
	sudo service supervisord start

You can access to the interface in the same machine on:

	0.0.0.0:8000/AquaGame

or in another machine (i.e. a mobile device) connected to the same LAN on:

	[MachineLanIP]:8000/AquaGame

## Interface of the laboratory ##

![Basic](https://raw.github.com/gmartinvela/AquaGame/master/AquaGame/static/img/basic_interface.png)

![Normal](https://raw.github.com/gmartinvela/AquaGame/master/AquaGame/static/img/normal_interface.png)


## Credits and License ##

This program is free software: you can redistribute it and/or modify it
under the terms of the  GNU  Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or (at
your option) any later version.

