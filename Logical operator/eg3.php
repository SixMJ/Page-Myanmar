<?php
	if (isset($_REQUEST['save'])) {
		if($_REQUEST['n']%2==0) {
			echo $_REQUEST['n']." is even number";
		}
	
	}
?>

<body>
	<form method="request">
		Enter your number <input type="text" name="n"/><hr>
		<input type="submit" value= "check number" name="save"/>
	</form>
</body><br><br>

<?php
	error_reporting(1);
	$num = $_POST['n'];
	if ($num>0) {
		echo $num." is positive number";
	}
	else {
		echo $num." is negative number";
	}
?>
 
<body>
	<form method="post">		
		Enter Your Number <input type="number" name="n"><br>
		<input type="submit" value="Check Number" >
	</form>
</body>

<?php
	$num = 0;
	for ($i=1; $i<=10 ;$i++) {
		if($i%2==0) {
			$sum = $sum+$i;
		}
	}
	echo $sum;
?>

