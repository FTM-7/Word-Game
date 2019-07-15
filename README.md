# Word-Game
The user will be asked to guess a four letter word , to make it realistic there a large list of words provided in a text file containing 4030 , 4 letter English words . The python application will load the word randomly from the text file and will be used for the game. After each subsequent game the user can have a look at the scoreboard.

The initial screen would look like this :

	** The great guessing game ** 
  
 Current Guess: ---- 
 g = guess, t = tell me, l for a letter, and q to quit			
 
 If	the	letter	option	is	chosen	(“l”),	the	user	will	enter	a	possible	letter	and	the	program	will	indicate	how	many	such	letters	there	are	in	this	string.	It	will	then	replace	one	or	more	of	the	“-“	values	with	this	letter	and	redisplay	the	result.	It	might	look	like	this,
 if	‘a’	is	chosen:	l Enter a letter:  a You found 1 letters 
 
 Current Guess: --a- 
 g = guess, t = tell me, l for a letter, and q to quit	
	
 This	process	continues	until	the	user	either	gets	the	answer	right	or	gives	up.	In	both	cases,	the	proper	string	will	be	displayed	and	an	appropriate	message	will	be	printed	to	the	screen.		At	this	point,	a	new	string	will	be	randomly	selected	from	the	database	and	the	game	will	continue	with	a	new	guessing	round.	Of	course,	“quit”	can	be	selected	at	any	time.	To	make	the	game	more	interesting,	you	must	keep	score.	We	will	assume	that	a	user	can	play	up	to	one	hundred	games	(you	will get	tired	of	this	after	2	or	3	rounds).	
 
For	each	game/word,	you	must	do	the	following.	Each	letter	in	the	English	language	is	used	with	a	certain	frequency	(“e”	is	the	most	common	letter,	“z”	the	least).	The	table	of	frequencies	is	given	later	in	this	document. The	letters	that	are	still	blank	at	the	time	of	a	correct	guess	will	be	summed	together	to	give	a	total.	Basically,	the	point	value	for	a	given	letter	is	equal	to	its	frequency.	Note	that	it	is	easiest	to	guess	a	word	if	you	first	uncover	the	most	common	letters.	However,	this	leaves	the	least	points	in	the	remaining	word.	Of	course,	the	number	of	letters	that	you	turn	over	also	affects	your	score.		So	you	should	divide	the	sum	by	the	number	of	times	you	request	a	letter.	The	more	letters	you	must	turn	over,	the	lower	your	total	score.	Finally,	an	incorrect	guess	costs	you	10%	of	your	score	for	the	current	word.	What	happens	if	you	give	up?	Then	you	should	lose	points.	Here,	the	total	points	lost	should	simply	be	the	sum	the	uncovered	letters.		

The	idea	is	that	your	score	from	each	round	will	be	recorded,	along	with	the	original	word,	the	status	of	the	game	(correct	guess	or	not),	the	number	of	guesses	required,	and	the	final	score	for	that	game.	Once	the	user	has	finished	playing,	they	will	select	quit.	At	that	point,	you	will	print	a	short	report	that	summarizes	the	info.	It	would	look	:

Game       Word       Status     Bad Guesses     Missed Letters   Score    
----       ----       ------     -----------     --------------   -----    
1          yule       Success    0               2                2.02      
2          dipt       Gave up    0               4                -17.96    
3          laid       Success    2               1                12.20     
4          defi       Success    1               1                5.83     

final score : 2.09
