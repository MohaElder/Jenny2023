<script>
	// @ts-nocheck

	/**
	 * @type {NodeJS.Timer | undefined}
	 */
	let timer = undefined;
	let infinite_timer = undefined;
	let start = false;

	let showMusicTitle = false;
	let renderText = '';
	let activeLevelIndex = 0;
	let story = { type: '' };

	let levels = [
		{
			id: 1,
			music: {
				name: '',
				author: '',
				url: 'assets/metacosmos_1.mp3'
			},
			stories: [
				{
					type: 'text',
					content: 'Designed for Big Screens \n please turn on the volume for best experience',
					signature: ''
				},
				{
					type: 'image',
					content: 'assets/logo.png'
				},
				{
					type: 'bold-text',
					content: 'A MOHAELDER GAME',
					signature: ''
				},
				{
					type: 'yellow-text',
					content:
						"Love is the astrolabe of God's mysteries \n ... \n However much we describe and explain love, \n ... \n love unexplained is clearer",
					signature: 'Rumi, Masnavi'
				},
				{
					type: 'yellow-text',
					content:
						"In 3003, our sun died. \n THE HAPPY BIRTHDAY COMPANY launched Project-Constellation, looking for a new home. The ship, carrying the last 212 humans, departed. \n \
				It's 3023 now, the ship is heading toward the last constellation on its list. ",
					signature: 'THE HAPPY BIRTHDAY COMPANY, Company Record 505'
				}
			],
			sourceText: [
				'Constellation Astrolabe v23.0',
				'Copyright: This is the product of The Happy Birthday Company 2023, any unauthorized use will be prosecuted',
				'Initializing...',
				'Servlet service loaded',
				'Sending /GET request to https://hbd-jenny.com/get/metacosmos...',
				'200: OK',
				'Humanizing cosmos data...',
				'Sending /GET request to https://hbd-jenny.com/get/satellite?id=0212&cord-matrix="0.9,2.7"...',
				'401: Not Authorized',
				'Login required! Please scan the following code to log into the system:',
				'Pending JWT verification...'
			]
		},
		{
			id: 2,
			music: {
				name: 'Metacosmos',
				author: 'ANNA THORVALDSDOTTIR \n Iceland Symphony Orchestra & Daniel Bjarnason',
				url: 'assets/metacosmos_2.mp3'
			}
		},
		{
			id: 3,
			music: {
				name: '2001: A Space Odyssey',
				author: 'John Williams \n Boson Pops Orchestra',
				url: 'assets/space.mp3'
			}
		},
		{
			id: 4,
			music: {
				name: 'Space Oddity',
				author: 'David Bowie',
				url: 'assets/SpaceOddity.mp3'
			}
		},
		{
			id: 5,
			music: {
				name: 'Friends make garbage(Good friends take it out)',
				author: 'Low Roar',
				url: 'assets/lowroar.mp3'
			},
			stories: [
				{
					type: 'image',
					content: 'assets/logo_pure.png'
				},
				{
					type: 'yellow-text',
					content:
						'We came whirling out of nothingness, \n scattering stars like dust ... \n The stars made a circle, \n and in the middle, \n we dance',
					signature: 'Rumi, Fragments, Ecstasies'
				},
				{
					type: 'yellow-text',
					content: '生日快乐！',
					signature: ''
				}
			]
		}
	];

	let currentAudio;

	function keepConnect() {
		ws.send('still here');
	}

	function handleStart() {
		start = true;
		timer = setInterval(render, 9000);
		infinite_timer = setInterval(keepConnect, 5000);
		connect('wss://jenny-2023-server.herokuapp.com');
		currentAudio = new Audio(levels[0].music.url);
		currentAudio.play();
	}

	function render() {
		if (levels[activeLevelIndex].stories.length === 0) {
			clearInterval(timer);
			if (activeLevelIndex === 0) {
				timer = setInterval(render2, 1500);
				story = { type: '' };
			}
			return;
		}
		story = levels[activeLevelIndex].stories.shift();
	}

	let showLogInQrCode = false;
	function render2() {
		if (levels[activeLevelIndex].sourceText.length === 0) {
			clearInterval(timer);
			showLogInQrCode = true;
			return;
		}
		renderText += levels[activeLevelIndex].sourceText.shift() + '\n';
	}

	let ws;

	function connect(url) {
		ws = new WebSocket(url);
		ws.onmessage = (event) => {
			proceedGame();
		};
	}

	function proceedGame() {
		if (activeLevelIndex < levels.length - 1) {
			renderText = '';
			showLogInQrCode = false;
			activeLevelIndex += 1;

			if (activeLevelIndex == levels.length - 1) {
				timer = setInterval(render, 9000);
				clearInterval(infinite_timer)
			}

			currentAudio.pause();
			currentAudio = new Audio(levels[activeLevelIndex].music.url);
			currentAudio.play();

			showMusicTitle = true;
			const element = document.getElementById('music-title-box');
			element.classList.remove('elementToFadeInAndOut');
			setTimeout(() => {
				element.classList.add('elementToFadeInAndOut');
			}, 20);
		}
	}
</script>

{#if activeLevelIndex == 1}
	<img style="width: 100%;" src="/assets/pic1.jpg" alt="" />
{/if}
{#if activeLevelIndex == 2}
	<img style="width: 100%;" src="/assets/pic2.jpg" alt="" />
{/if}
{#if activeLevelIndex == 3}
	<img style="width: 100%;" src="/assets/pic3.jpg" alt="" />
{/if}
{#if activeLevelIndex == 4}
	<img style="width: 100%;" src="/assets/pic4.jpg" alt="" />
{/if}

<div class="middle">
	{#if !start}
		<button
			on:click={() => {
				handleStart();
			}}>START</button
		>
	{/if}
	{#if story.type === 'text'}
		<h1 class="thin">{story.content}</h1>
	{:else if story.type === 'bold-text'}
		<h1 class="bolded">{story.content}</h1>
	{:else if story.type === 'yellow-text'}
		<h1 class="thin yellow">{story.content}</h1>
		<h1 class="thin yellow italic">{story.signature}</h1>
	{:else if story.type === 'image'}
		<img src={story.content} alt="logo" />
	{:else}
		<p>{renderText}</p>
	{/if}
	{#if showLogInQrCode}
		<img src="assets/qrcode.gif" alt="login qrcode" />
	{/if}
</div>

<div id="music-title-box" class="music-title-box elementToFadeInAndOut">
	<h1>{levels[activeLevelIndex].music.name}</h1>
	<p>{levels[activeLevelIndex].music.author}</p>
</div>

<style>
	.music-title-box {
		position: absolute;
		z-index: 1000;
		right: 5%;
		bottom: 10%;
		padding: 10px;
		padding-right: 10%;
		background-color: rgba(0, 0, 0, 0.3);
	}

	.elementToFadeInAndOut {
		animation: fadeInOut 9s linear 1 forwards;
	}

	@keyframes fadeInOut {
		0% {
			opacity: 0;
		}
		25% {
			opacity: 1;
		}
		50% {
			opacity: 1;
		}
		75% {
			opacity: 1;
		}
		100% {
			opacity: 0;
		}
	}

	.music-title-box h1 {
		color: #c4a52e;
		text-align: start;
		text-transform: uppercase;
		white-space: pre-line;
	}

	.middle {
		display: flex;
		justify-content: center;
		flex-wrap: wrap;
		position: fixed;
		top: 50%;
		left: 50%;
		/* bring your own prefixes */
		transform: translate(-50%, -50%);
	}

	p {
		font-size: 50%;
		line-height: 2.3vh;
		font-weight: 300;
		margin-bottom: 10px;
		white-space: pre-line;
	}

	h1 {
		color: white;
		text-align: center;
		text-transform: uppercase;
		white-space: pre-line;
	}

	.thin {
		font-weight: 300;
	}

	.yellow {
		color: #c4a52e;
		line-height: 249%;
	}

	.italic {
		font-style: italic;
	}

	.bolded {
		font-weight: 800;
	}

	img {
		width: 29%;
	}

	button {
		margin-top: 30px;
		padding: 2vh 6vh 2vh 6vh;
		font-size: 200%;
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
