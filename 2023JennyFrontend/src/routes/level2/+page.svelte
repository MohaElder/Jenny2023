<script>
	let imageUrl = 'assets/phone_constellation.jpg';

	let buttonName = 'DECRYPT';

	let sourceText = [
		'Decryption starting...',
		'wget https://thbdc.com/api/v1/get/sattelite-pak',
		'chmod u+x ./hbd.sh & ./hbd.sh',
		'COPYRIGHT (C) THE HAPPY BIRTHDAY COMPANY All Rights Reserved',
		'loaded! Everything is OK :)',
		'Decrypting...',
		'Auto Decryption Failed: UnknownConstellationException: The input constellation is not in the database! Please decrypt manually.'
	];

	let renderText = '';
	let failed = false;

	/**
	 * @type {NodeJS.Timer | undefined}
	 */
	let timer = undefined;

	function handleClick() {
		buttonName = 'DECRYPTING';
		timer = setInterval(render, 1500);
	}

	function render() {
		if (sourceText.length === 0) {
			buttonName = 'DECRYPTION FAILED';
			clearInterval(timer);
			failed = true;
			return;
		}
		renderText += sourceText.shift() + '\n';
	}

	function handleClick2() {
		connect('wss://jenny-2023-server.herokuapp.com')
			.then((ws) => {
				console.log('Connected to WebSocket!');
				ws.send('next');
				window.location.href = '/level3'
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
	<img style="width: 90%;" src={imageUrl} alt="" />
	<span class="satellite-stream">SATELLITE STREAM: AVIXHARBOR#0365.20030212</span>
	<br />
	<button
		on:click={() => {
			handleClick();
		}}>{buttonName}</button
	>

	<p>{renderText}</p>

	{#if failed}
		<button
			style="font-size: 1vh;"
			on:click={() => {
				handleClick2();
			}}>MANUAL DECRYPT</button
		>
	{/if}
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
		font-size: 50%;
		line-height: 2.3vh;
		font-weight: 300;
		margin-bottom: 10px;
		white-space: pre-line;
	}
</style>
