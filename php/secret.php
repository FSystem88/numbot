<?php
require "bd.php";

$tgid = $_POST['tgid'];
$balance = $_POST['balance'];
// 355821673

$result= mysqli_query($link, "SELECT balance FROM usersnumb WHERE tgid='$tgid'");
$row = mysqli_fetch_row($result);
$old = $row[0];
if (substr($balance, 0,1) == "-")
{
	$balance = substr($balance, 1);
	$new = (int)$old - (int)$balance;
	$result= mysqli_query($link, "UPDATE `usersnumb` SET `balance`='$new' WHERE `tgid`='$tgid'");	
}
else
{
	$new = (int)$old + (int)$balance;
	$result= mysqli_query($link, "UPDATE `usersnumb` SET `balance`='$new' WHERE `tgid`='$tgid'");	
}


?>