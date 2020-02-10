<body>
	<form method = "post">
		<h2>Select Your Car</h2><br>
		<select name="seltype">
			<option value="toyota">Toyota</option>
			<option value="Ferrir">Ferrir</option>
			<option value="lambo">Lambo</option>
			<option value="volkswagn">Volkswagn</option>
			<option value="ford">Ford</option>
		</select><br>
		Color: <input type="text" name="txtcolor"><br>
		<input type="submit">
	</form>
</body>

<?php
	error_reporting(1);
	$type = $_POST['seltype'];
	$color = $_POST['txtcolor'];
	echo "<font color = '$color'> Your $color $type is ready. Safe driving! </font>";
?>