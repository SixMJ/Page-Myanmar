<?php
	error_reporting(1);
	$con = mysql_connect("localhost","root","") or die(mysql_error());
	mysql_select_db("Employee",$con);
	
	$data="UPDATE empInfo SET name='Shwe',mobile=09754456
	WHERE email='mgmg@gmail.com'";
	$val=mysql_query($data);
?>