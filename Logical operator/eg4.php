<?php
	$i = 1;
	if ($i==0) {
		echo "$i is equal with 0";
	}
	elseif ($i == 1) {
		echo "$i is equal with 1";
	}
	elseif ($i == 2){
		echo "$i is equal with 2";
	}
?><br><br>

<?php
	$i = 1;
	switch ($i) {
		case 0:
			echo "$i equal to 0";
			break;
			
		case 1:
			echo "$i equal to 1";
			break;
		
		case 2:
			echo "$i equal to 2";
			break;
	} 
?>