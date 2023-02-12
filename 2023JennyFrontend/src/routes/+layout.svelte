<link href="https://fonts.googleapis.com/css?family=Montserrat" rel="stylesheet" />
<body>
	<div class="container">
		<h1>
			Constellation Astrolabe<sup>®</sup>
			<p>by THE HAPPY BIRTHDAY COMPANY</p>
			<slot />
		</h1>
		
	</div>
	<img class="footnote-image" src="assets/logo_pure.png" alt="logo" />
</body>

<style>
	.container {
		top: 7%;
		padding: 5vh 2vh 5vh 3vh;
	}

	body {
		font-family: 'Montserrat';
		height: 100%;
		background-color: black;
		color: #c4a52e;
	}

	.footnote-image {
		width: 5vh;
		position: fixed;
		bottom: 0%;
		right: 0%;
		padding: 4vh;
	}

	h1 {
		font-weight: 400;
		font-size: 2.5vh;
	}

	sup {
		font-size: 0.5vh;
	}

	p {
		font-size: 0.8vh;
		font-weight: 200;
		margin-top: -1px;
	}
</style>
