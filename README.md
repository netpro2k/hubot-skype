# Hubot Skype Adapter

## Description

This is the [Skype](http://skype.com) adapter for hubot that allows you 
to communicate with hubot through Skype.

## Installation

* Add `hubot-skype` as a dependency in your hubot's `package.json` (use this repository url as the version)
* Install dependencies with `npm install`
* Install Python dependancy `Skype4py` with `pip` or `easy_install`
* Log into a Skype client on the same machine you are running hubot
* Run hubot with `bin/hubot -a skype`

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
