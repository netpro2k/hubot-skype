Readline = require 'readline'

Robot   = require("hubot").Robot
Adapter = require("hubot").Adapter
{TextMessage,EnterMessage,LeaveMessage,CatchAllMessage} = require '../../../src/message'

class SkypeAdapter extends Adapter
  send: (user, strings...) ->
    out = ""
    out = ("#{str}\n" for str in strings)
    json = JSON.stringify
        room: user.room
        message: out.join('')
    @skype.stdin.write json + '\n'

  reply: (user, strings...) ->
    @send user, strings...

  run: ->
    self = @
    stdin = process.openStdin()
    stdout = process.stdout
    pyScriptPath = __dirname+'/skype.py'
    if (process.platform == 'win32')
        py = 'C:/Python27/python.exe'
    else
        py = './python'
    @skype = require('child_process').spawn(py, [pyScriptPath])
    @skype.stdout.on 'data', (data) =>
        decoded = JSON.parse(data.toString())
        user = self.userForName decoded.user
        unless user?
            id = (new Date().getTime() / 1000).toString().replace('.','')
            user = self.userForId id
            user.name = decoded.user
        user.room = decoded.room
        return unless decoded.message
        @receive new TextMessage user, decoded.message
    @skype.stderr.on 'data', (data) =>
        console.log "ERR"
        console.log data.toString()
    @skype.on 'exit', (code) =>
        console.log('child process exited with code ' + code)
    @skype.on "uncaughtException", (err) =>
      @robot.logger.error "#{err}"

    process.on "uncaughtException", (err) =>
      @robot.logger.error "#{err}"

    @emit "connected"

exports.use = (robot) ->
  new SkypeAdapter robot
