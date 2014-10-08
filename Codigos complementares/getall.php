<html>
	<head><meta content="charset=UTF-8" />
	<title>Extração do database online do dicionario de libras base</title>
	</head>
	<body>

	<?php   

		$row = 1;
		if (($handle = fopen("lista3.txt", "r")) !== FALSE && ($handle2 = fopen("lista2.txt", "r")) !== FALSE) {
			while (($data = fgetcsv($handle, 1000, ",")) !== FALSE && ($words = fgetcsv($handle2, 1000, ",")) !== FALSE) {
				//if (($handle2 = fopen("lista2.txt", "r")) !== FALSE) {
					//while (($words = fgetcsv($handle2, 1000, ",")) !== FALSE) {
						$num = count($data);
						//echo "<p> $num fields in line $row: <br /></p>\n";
						$row++;
						for ($c=0; $c < $num; $c++) {
							set_time_limit(60);
							$url = 'http://acessobrasil.org.br/libras/consultaDetalhesPalavra.php?palavra='.$data[$c];
							$xml = simplexml_load_file($url);
							//$xml = utf8_decode($xml);
							//$xml = iconv( "UTF-8", "ISO-8859-1//TRANSLIT", $xml );
							echo $words[$c] . ",,";
							print_r($xml);
							echo "<br />";
						}
					//}
					
				//}
			}
		fclose($handle);
		fclose($handle2);
		}

		


	?>

	</body>
</html>