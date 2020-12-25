<?php
require "bd.php";

$chatid = $_POST['chatid'];
$tgid = $_POST['tgid'];

$result= mysqli_query($link, "SELECT * FROM chat$chatid WHERE tgid='$tgid'");

$row = mysqli_fetch_assoc($result);
if ($row == '')
{
	$arr = array('balance' => '0');
	echo json_encode($arr);

}
else
{
	echo json_encode($row);
}
?>

