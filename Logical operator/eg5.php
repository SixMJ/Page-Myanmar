<?php
	error_reporting(1);
	$first = $_POST['first'];
	$second = $_POST['second'];
	$choice = $_POST['ch'];
	
	switch ($choice) {
		case "+" :
			$sum = $first + $second;
			echo "Result is = ".$sum;
			break;
			
		case "-" :
			$minus = $first - $second;
			echo "Result is = ".$minus;
			break;
			
		case "*" :
			$multiple = $first * $second;
			echo "Result is = ".$multiple;
			break;
			
		case "/" :
			$division = $first / $second;
			echo "Result is = ".$division;
			break;
			
		default :
			echo "invalid code";
			break;
	}
?>

<body>
	<form method="post">
		Enter First Number <input type = "text" name ="first"><br>
		Enter Second Number <input type = "text" name ="second"><br>
		Enter Your Choice <input type = "text" name ="ch"><br>
		<input type="submit" value = "Show Result">
	</form>
</body>