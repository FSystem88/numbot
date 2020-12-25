<?php
require "bd.php";

$tgid = $_POST['tgid'];
// 355821673
$result= mysqli_query($link, "SELECT * FROM `usersnumb` WHERE `tgid`='{$tgid}'");

if($row = mysqli_fetch_assoc($result))
{
	echo json_encode($row);
}
else
{
	$arr = array('tgid' => '0');
	echo json_encode($arr);
}
?>