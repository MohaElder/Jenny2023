<script>
	let imageUrl = 'assets/phone_scc.jpg';

	let buttonName = 'DECRYPT';

	let sourceText =
		"Manual Decryption Instruction: \n \
    The Constellation Astrolabe scans the star cloud and visualizes the imaginary constellation segments. It also renders astronomical relationship between each planets with the following: \n \
    directed edge: a planet connected to the other planet by its gravitational field in the pointing direction \n \
    undirected edge: both planets' gravitational field attracts each other \n \
    To decrypt the constellation, you need to find the biggest SCC, Strongly Connected Component, of this constellation. The definition of Strongly Connected Component can be found online :) \n \
    Luckily, the Constellation Astrolabe can intelligently analyze the SCC based on your 'hint'. Instead of inputting all the planets in the SCC, you just need to input the GALAXY_COORDINATE: NUMBER of undirected edges and the NUMBER of directed edges to decrypt. Happy Hacking!";

	let userInput = '';
	let wrong = false;

	function handleClick() {
		if (userInput === '9,8') {
			connect('wss://jenny-2023-server.herokuapp.com')
				.then((ws) => {
					console.log('Connected to WebSocket!');
					ws.send('next');
					window.location.href = '/level4';
				})
				.catch((error) => {
					console.error('Error connecting to WebSocket:', error);
				});
		} else {
			wrong = true;
		}
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
	<img style="width: 90%;" src={imageUrl} alt="" />
	<span class="satellite-stream">SATELLITE STREAM: AVIXHARBOR#0365.20030212</span>

	<p>{sourceText}</p>

	<label class="omrs-input-underlined">
		<input bind:value={userInput} />
		<span class="omrs-input-helper">undirected edges #, directed edges #</span>
		{#if wrong}
			<span class="omrs-input-helper-red"
				>The universe says: The coordinates seem to be wrong, or the format might be wrong. Did you
				include comma?</span
			>
		{/if}
	</label>

	<button
		on:click={() => {
			handleClick();
		}}>{buttonName}</button
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

	p {
		font-size: 45%;
		line-height: 2.3vh;
		font-weight: 300;
		margin-bottom: 10px;
		white-space: pre-line;
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
</style>
