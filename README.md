<div align="center">
    <h1>DoomBot</h1>
    <img src="docs/assets/icons/icon-96.png" height="100" alt="RoomBot"/>
    <h3>Create rooms for any purpose.</h3>
</div>

--------

Sometimes you want to play something with a group, but everyone's busy at the moment. DoomBot allows you to create rooms to let everyone know that you're ready to play/do something.

## Features
* DoomBot will automatically disband inactive rooms.
* A colorful hoisted role is assigned to players who join the room, so you know who's in what room.
* A private channel is created for your room.
* Once you have enough people, DoomBot will notify everybody!

### Basic Commands
* `new` Create a new room based on your current activity or message
* `list` List rooms in current guild.
* `join` Join a room with `@someone` or the room name
* `leave` Leave a room
* `look` Show room information

### Room Host Commands
* `activity`	Set the name of your room. This is what the channel and role will be named as.
* `color`	Set the color of your room. Possible colors are: teal, green, blue, purple, magenta/pink, gold/yellow, orange, and red. A random color is set if the specified color is not included above.
* `description`	Set the description of your room. The description is the little message that you will see in the room list.
* `host`	Change the host of your room. Can either mention or use the name of new host.
* `kick`	Kick a player. Can either mention or use the name of the kickee.
* `lock`	Prevent people from joining your room.
* `size`	Set the max player size of your room. Once the room is full, I will ping the room.
* `timeout`	After inactivity for this amount of minutes, the room will automatically be disbanded.
* `voice_channel`	Create a voice channel associated with this room. Will not create if already exists.

### Admin Commands
* `force_disband`	Force delete a room (specify room name or @roomrole.
* `purge` Delete rooms in this server. Use flags -a for all active rooms, -b for all broken rooms.
* `reset_settings` Reset the sttings for this server.
* `settings` Set options for this server. To set an option(s), use -flag value.

### General Commands
* `donate` Link to donation page for supporting TheKlub.
* `ping` Pong! Shows latency
