<script>
	let images = [
		{
			url: 'assets/patterns/Aquila.png',
			name: 'Aquila'
		},
		{
			url: 'assets/patterns/Capricornus.png',
			name: 'Capricornus'
		},
		{
			url: 'assets/patterns/Cetus.png',
			name: 'Cetus'
		},
		{
			url: 'assets/patterns/M72.png',
			name: 'M72'
		},
		{
			url: 'assets/patterns/Nash.png',
			name: 'Nash'
		},
		{
			url: 'assets/patterns/Pisces.png',
			name: 'Pisces'
		},
		{
			url: 'assets/patterns/Sculptor.png',
			name: 'Sculptor'
		}
	];

	let userInput = '';
	let activeIndex = 0;
	let wrong = false;

	function evaluate() {
		if (userInput === images[activeIndex].name) {
			wrong = false;
			if (activeIndex === images.length - 1) {
				handleClick();
			}
			userInput = '';
			activeIndex += 1;
		} else {
			wrong = true;
		}
	}

	function handleClick() {
		connect('wss://jenny-2023-server.herokuapp.com')
			.then((ws) => {
				console.log('Connected to WebSocket!');
				ws.send('next');
				window.location.href = '/level2';
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
</script>

<body>
	<img style="width: 90%;" src={images[activeIndex].url} alt="" />
	<span class="satellite-stream">SATELLITE STREAM: AVIXHARBOR#0365.20030212</span>

	<label class="omrs-input-underlined">
		<input bind:value={userInput} />
		<span class="omrs-input-helper">Constellation Name</span>
		{#if wrong}
			<span class="omrs-input-helper-red"
				>The universe didn't understand this constellation :) Please try again~</span
			>
		{/if}
	</label>

	<button
		on:click={() => {
			evaluate();
		}}>MARK</button
	>
</body>

<style>
	.satellite-stream {
		margin-top: -5px;
		font-size: 1vh;
		color: #ffffff8f;
		font-weight: 200;
		width: 20%;
	}

	/* Input*/
	.omrs-input-underlined {
		width: 80%;
		display: flex;
		flex-wrap: wrap;
	}
	.omrs-input-underlined > input {
		background-color: #000000;
		color: #ffffff;
		border: none;
		border-bottom: 0.125rem solid #ffffffa1;
		height: 2rem;
		font-size: 2vh;
		width: 100%;
		line-height: 147.6%;
		padding-top: 0.825rem;
		padding-bottom: 3%;
	}

	.omrs-input-underlined > input:focus {
		outline: none;
	}

	.omrs-input-underlined > .omrs-input-helper {
		font-size: 1vh;
		color: #ffffffa1;
		font-weight: 200;
		padding-top: 5px;
	}

	.omrs-input-underlined > .omrs-input-helper-red {
		font-size: 1vh;
		color: #ee4d4da1;
		font-weight: 200;
		padding-top: 5px;
		width: 100%;
	}

	.omrs-input-underlined > input:hover {
		background: #000000;
		border-color: #c4a52e;
	}

	.omrs-input-underlined:not(.omrs-input-danger) > input:focus {
		border-color: #c4a52e;
	}

	button {
		margin-top: 30px;
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
