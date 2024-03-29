# Art Demon Commands

Add Art Demon To Your Server [Here!](https://discord.com/api/oauth2/authorize?client_id=740666177554219067&permissions=8&scope=bot)

> Bot Prefix: `&`
> 
> <br> 
> How To Read: <br>
> - Command arguments surrounded in `<>` are optional arguments that can be given. <br>
> - Command arguments surrounded [] mean that anything can be passed to the command.
> - Command arguments surrounded in {} mean that the command in question can also be invoked using descriptor given in {}
 
- `&aesthetic`
	- Gives a random aesthetic / theme to use.
- `&color`
	- Gives a random color along with its hex code.
- `&colors`
	- Gives a random number of colors between 2 and 6 along with their hex codes.
- `&colors <number>`
	- Allows up to six random colors to be generated along with their hex codes
- `&animal`
	- Gives a random animal.
- `&creature`
	- Gives either a realistic or a fantasy creature to draw.
- `&creature <realistic / fantasy>`
	- Gives either a realistic or fantasy creature to draw, based on the selection.
- `&emoji`
	- Gives between two and four random emojis to draw about.
- `&f`
	- To pay respects.
- `&f [thing]`
	- Pay respects to [thing].
- `&palette`
	- Gives a random palette of colors to use.
- `&person`
	- Gives a realistic or fantasy person to draw.
- `&person <realistic / fantasy>`
	- Gives a realistic / fantasy person to draw based on selection.
- `&plant`
	- Gives a realistic or fantasy plant prompt to draw.
- `&plant <realistic / fantasy>`
	- Gives a realistic / fantasy plant to draw based on selection.
- `&prompt`
	- Gives a random art prompt to draw,
- `&prompt <people / animal / OC / nature / word / keywords>`
	- Based on the prompt selection, a prompt relating to the selection will be given.
- `&hex <color code>` or `&hex #<color code>`
	- Returns the specified hex color provided.

# Admin Commands

- `&dailyprompt {dp} set <#text-channel-to-print-prompt> <time-to-print>`
	- `dailyprompt` is for Discord server admins. This command will print a daily prompt in the specified `#text-channel` every day at a specific time. You just set it and forget it! Then, every day, until you cancel it, a `dailyprompt` will be given to that text-channel.
	- Please note: `<time-to-print>` must be given in 24-hour time. So, `11:11	P.M.` at night would be `23:11`. **Do not** put A.M. or P.M. in the time.
		- Also note: all times given must be given in EST. This bot was developed in the East Coast, so that's the default timezone. If requested, we may allow for different time zones to be selected. 
		- Server's can only have one daily prompt active at a time. Another come cannot be started until it is cancelled.
	- Example: `&dailyprompt set #daily-prompts 23:11`
		- If all goes well, you should receive a confirmation message. 

- `&dailyprompt {dp} cancel`
	- This will cancel the daily prompt currently active in your server is there is any. 
