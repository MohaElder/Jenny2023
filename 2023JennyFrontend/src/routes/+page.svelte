<script>
	function handleClick() {
		connect('wss://jenny-2023-server.herokuapp.com')
			.then((ws) => {
				console.log('Connected to WebSocket!');
				ws.send('next');
				window.location.href = '/level1';
			})
			.catch((error) => {
				console.error('Error connecting to WebSocket:', error);
			});
	}

	function connect(url) {
		return new Promise((resolve, reject) => {
			const ws = new WebSocket(url);

			ws.onopen = () => {
				resolve(ws);
			};

			ws.onerror = (error) => {
				reject(error);
			};
		});
	}

	let bottomLine = '<button class="star-button" onClick="track">track with STAR-JIRA </button>';
</script>

<p>Welcome back, Astronaut user.name!</p>
<p>
	As the CEO of THE HAPPY BIRTHDAY COMPANY, I have to say that it is an honor to have you on board
	as a member of our expedition team. Your abilities are truly outstanding!
</p>
<p>
	You have been assigned the task to investigate constellation #0212. If you're lucky, this
	constellation will be our new Galaxy! If not, don't worry, there's still 0 constellations left to
	explore :)
</p>
<p>
	The first thing you need to do is to identify the constellation from the star dust. The
	Constellation Astrolabe has already generated satelliteScan.result.length frames for you.
</p>
<p>
	Your task is to Identify the star cluster that each of these frames belong to. That will be the
	word closest to the stars shown in the frames provided later.
</p>
<p>Good luck! Humanity's fate counts on you!</p>

<p class="signature">Calen Weng, CEO of THE HAPPY BIRTHDAY COMPANY</p>

<br />

<span>{bottomLine}</span>

<br />
<br />
<br />

<button
	on:click={() => {
		handleClick();
	}}>START</button
>

<style>
	p {
		font-size: 50%;
		line-height: 2.3vh;
		font-weight: 300;
		margin-bottom: 10px;
	}

	.signature {
		font-style: italic;
		font-size: 60%;
	}

	span {
		font-size: 50%;
		font-weight: 200;
	}

	button {
		padding: 1vh 4vh 1vh 4vh;
		font-size: 55%;
		border-radius: 25vh;
		border: 1px solid gray;
		background-color: rgba(0, 0, 0, 0);
		color: #c4a52e;
		transition-duration: 0.5s;
		text-decoration: none;
	}

	button:active {
		background-color: rgba(255, 255, 255, 0.479); /* Green */
	}
</style>
