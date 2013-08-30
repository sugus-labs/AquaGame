# Welcome to AquaGame #

> **NOTE:** AquaGame is currently undergoing heavy refactoring work
> to accomodate a better UI, better back end and better access. Pull at your
> own risk! :-)

The actual version is 0.1.

AquaGame is a new WebLab-Deusto type of experiment based in the aqualab to integrate a Serious Game. This game tend to be a game to learn basics of Archimedes Principles using a remote laboratory with different balls of different densities that really float on the water in real time.
There are many different Technologies implied like Python (mainly Django framework) ,Django, JavaScript, JQuery, ...

**WARNING:**  AquaGame is still experimental and isn't actually very useful yet.

**Hey, check out WebLab-Deusto project! <http://weblab.deusto.es>**

## Requirements ##

AquaGame is developed on a Ubuntu 12.04 system, running:

   * Python 2.7
   * Django 1.5.1
   * python-mysqldb 1.2.3
   * mysql-server 5.5.32

It might work with other versions.

## Setting up the environment and config ##

Like any Django project, put your teminal in the root directory of the project and type:

	$ python manage.py syncdb

After that stay in the same directory and type:

	$ python manage.py runserver 0.0.0.0:8000

You can access to the interface in the same machine on:

	0.0.0.0:8000/MasterMind/index

or in another machine (i.e. a mobile device) connected to the same LAN on:

	[MachineLanIP]:8000/MasterMind/index


## Credits and License ##

This program is free software: you can redistribute it and/or modify it
under the terms of the  GNU  Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or (at
your option) any later version.

