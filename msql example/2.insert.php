<?php
	error_reporting(1);
	$con = mysql_connect("localhost","root","") or die(mysql_error());
	mysql_select_db("Employee",$con);
	$name=$_GET['name'];
	$eid=$_GET['eid'];
	$mob=$_GET['mob'];
	
	$query="INSERT INTO empInfo
	VALUES ('','{$_GET['name']}','{$_GET['eid']}','{$_GET['mob']}')";
	mysql_query($query);
?>

<form medthod="get">
	Enter your name<input type="text" name="name"><hr>
	Enter your email<input type="text" name="eid"><hr>
	Enter your mobile<input type="text" name="mob"><hr>
	<input type="submit" value="INSERT">
</form>