<link href="https://fonts.googleapis.com/css?family=Montserrat" rel="stylesheet" />
<body>
	<div class="container">
		<slot />
	</div>
</body>

<style>
	.container {
		
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
		bottom: 0;
		left: 0;
		padding: 5vh;
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
