<script>
	import { onMount } from 'svelte';

	let sourceText = [
		'Decrypting...',
		'Decryption Success!',
		'',
		'You have found our new home! All of the 1 members on the ship own you a great THANK YOU!',
		'',
		'',
		'生日快乐 ;)'
	];

	let renderText = '';

	/**
	 * @type {NodeJS.Timer | undefined}
	 */
	let timer = undefined;

	onMount(() => {
		timer = setInterval(render, 1500);
	});

	function render() {
		if (sourceText.length === 0) {
			clearInterval(timer);
			return;
		}
		renderText += sourceText.shift() + '\n';
	}
</script>

<body>
	<p>{renderText}</p>
</body>

<style>
	p {
		font-size: 50%;
		line-height: 2.3vh;
		font-weight: 300;
		margin-bottom: 10px;
		white-space: pre-line;
	}
</style>
