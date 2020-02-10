<?php

		$x = $_GET['f'];
		$y = $_GET['s'];
		$z = $x + $y;
	
		echo "<font color='gray'>The Sum is = $z </font>"
	
?>

<body>
	<form method="get">
		Enter Your First Number <input type="text" name="f"><br>
		Enter Your Second Number <input type="text" name="s"><br>
								 <input type="submit" name="sent">
	</form>
</body>