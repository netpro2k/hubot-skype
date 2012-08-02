# Hubot Skype Adapter

## Description

This is the [Skype](http://skype.com) adapter for hubot that allows you 
to communicate with hubot through Skype.

## Installation

* Add `hubot-skype` as a dependency in your hubot's `package.json`
* Install dependencies with `npm install`
* Install Python dependancy `Skype4py` with `pip` or `easy_install`
* Log into a Skype client on the same machine you are running hubot
* Run hubot with `bin/hubot -a skype`

### Installation on a headless server running Ubuntu 12.04

* Follow [Deploying Hubot onto UNIX instructions](https://github.com/github/hubot/wiki/Deploying-Hubot-onto-UNIX)
* Add `hubot-skype` as a dependency in your hubot's `package.json`
   * eg: ```"hubot-skype": "git://github.com/mrdavidlaing/hubot-skype.git"```
* Install dependencies with `npm install`
* Install Python dependancy `Skype4py` with `pip` 
* Install Ubuntu Desktop
   * ```sudo apt-get install ubuntu-desktop```
* Install Headless X11
   * ```sudo apt-get install xvfb x11vnc screen```
* Install Skype 
  * ```sudo apt-add-repository "deb http://archive.canonical.com/ $(lsb_release -sc) partner"```
  * ```sudo apt-get update && sudo apt-get install skype```
* Launch skype on the server, connect to it using VNC to type enter initial password set to auto-logon
   * ```xvfb-run -n 0 -s "-screen 0 800x600x16" /usr/bin/skype &```
   * ```x11vnc -display :0```
   * Use your favourite VNC client to connect to {server.ip}:5900  
     (or set up a SSH tunnel from your machine to that port)
   * Create a skype-hubot Skype user, log in to Skype using that, and select "auto-login at startup"
* Tell Skype to accept connections from SkypePy
   * ```export DISPLAY="localhost:0"```
   * ```bin/hubot -a skype```
   * Accept the Skype security popup in the VNC session (and choose to always allow)
* Kill hubot & skype, and create yourself a ~/start_hubot.sh script similar to this (fixing paths & name as appropriate)
       
           #!/bin/bash

           export DISPLAY="localhost:0"
           #script exports, eg AWS credentials
           export HUBOT_AWS_ACCESS_KEY_ID="xxxxxxxxxxxx"

           echo "starting skype on xvfb, display 0"
           xvfb-run -n 0 -s "-screen 0 800x600x16" /usr/bin/skype &
           echo "waiting 30s..."
           sleep 30s
       
           echo "starting hubot"
           cd /home/le-bott/hubot
           bin/hubot --name le-bott -a skype 

## Usage

The Skype adapter works by communicating through a locally running skype
client. You need to create a Skype account for your bot, and log into it
on a Skype client running on the same machine as hubot. When you first
launch hubot with the Skype adapter, Skype will prompt you to allow for
API permission. You must allow this before the bot will work.

## Contribute

Here's the most direct way to get your work merged into the project.

1. Fork the project
2. Clone down your fork
3. Create a feature branch
4. Hack away and add tests, not necessarily in that order
5. Make sure everything still passes by running tests
6. If necessary, rebase your commits into logical chunks without errors
7. Push the branch up to your fork
8. Send a pull request for your branch

## Copyright

Copyright &copy; Dominick D'Aniello. See LICENSE for details.
