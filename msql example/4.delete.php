<?php
	error_reporting(1);
	$con = mysql_connect("localhost","root","") or die(mysql_error());
	mysql_select_db("Employee",$con);
	
	$data="DELETE FROM empinfo
	WHERE email='aungaung@gmail.com'";
	$val=mysql_query($data);
?>