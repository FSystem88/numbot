<?php
require "bd.php";

$tgid = $_POST['tgid'];
$name = $_POST['name'];
$username = $_POST['username'];
$balance = $_POST['balance'];

///$tgid = '355821673';
//$name = 'fsystem88';
//$username = 'fsystem88';
//$balance = '0';
if ($tgid != "")
{
	$res = mysqli_query($link, "SELECT * FROM tourney WHERE tgid='{$tgid}'");
	$row = mysqli_fetch_row($res);
	if ($row[0] == "")
	{
		$res = mysqli_query($link, "INSERT INTO `tourney`(`tgid`, `name`, `username`, `balance`) VALUES ('{$tgid}', '{$name}', '{$username}', '{$balance}')");
		$array = ["result" => "1"];
		echo json_encode($array);
	}
	else
	{
		$array = ["result" => "2"];
		echo json_encode($array);
	}
}
?>