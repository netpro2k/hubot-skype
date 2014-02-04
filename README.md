# WARNING

#### Microsoft [has stated](http://blogs.skype.com/2013/11/06/feature-evolution-and-support-for-the-skype-desktop-api/) that they will be dropping support for the Skype desktop API. This adapter will likely stop working in the very near future (If it hasn't already... this change was slated for December 2013). 

The adapter was always a hack at best, if you are looking to set up a bot for your company or community I would _HIGHLY_ recommend using a network that better supports scripting such as [Campfire](https://github.com/github/hubot/blob/master/docs/adapters/campfire.md) or [IRC](https://github.com/nandub/hubot-irc).

## Description

This is the [Skype](http://skype.com) adapter for
[hubot](http://hubot.github.com) that allows you to communicate with hubot
through Skype.

## Installation

* Add `hubot-skype` as a dependency in your hubot's `package.json` (use this repository url `git://github.com/netpro2k/hubot-skype.git` as the version)
* Install dependencies with `npm install`
* Install Python dependency `Skype4Py` with `pip` or `easy_install`
* Log into a Skype client on the same machine you are running hubot
* Run hubot with `bin/hubot -a skype`

## Usage

The Skype adapter works by communicating through a locally running Skype
client. You need to create a Skype account for your bot, and log into it
on a Skype client running on the same machine as hubot. When you first
launch hubot with the Skype adapter, Skype will prompt you to allow for
API permission. You must allow this before the bot will work.

## OS Specific notes

### Windows

On Windows, it's possible to communicate with Skype via native COM interface without installing Python
(which is not preinstalled in this OS) but using [edge.js (.NET adapter for Node.js)](http://tjanczuk.github.io/edge/).

So, if you don't have Python installed and target only Windows machines, you can try [Skype4COM adapter](https://github.com/RReverser/hubot-skype4com).

Please not that you shouldn't use it if planning to run your script on other operating systems.

### OSX

The current version of Skype4Py doesn't play nicely with the 64 bit version
of python on OSX and would immediately cause a segmentation fault, but a
workaround has been established in this repo using the `arch` command (see
`/src/python32bit` for details).

If this built in workaround doesn't seem to work, you may need to force python
to run in 32 bit mode by setting the environment variable `VERSIONER_PYTHON_PREFER_32_BIT` to `true`

Ex:

```bash
export VERSIONER_PYTHON_PREFER_32_BIT=yes
./hubot -a skype
```

### Linux
If you would like to use a different transport type than the default (`x11`) 
you may set the `HUBOT_SKYPE_TRANSPORT` environment variable. Currently 
supported values are `x11` amd `dbus`. More information on
[module page](http://skype4py.sourceforge.net/doc/html/Skype4Py.api.posix-module.html).

## Contribute

Here's the most direct way to get your work merged into the project.

1. Fork the project
2. Clone down your fork
3. Create a feature branch
4. Hack away
5. If necessary, rebase your commits into logical chunks without errors
6. Push the branch up to your fork
7. Send a pull request for your branch

## Copyright

Copyright &copy; Dominick D'Aniello. See LICENSE for details.
