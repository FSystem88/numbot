<?php
require "bd.php";

$chatid = $_POST['chatid'];
$tgid = $_POST['tgid'];
$balance = $_POST['balance'];
// 355821673

$result= mysqli_query($link, "SELECT balance FROM chat$chatid WHERE tgid='$tgid'");
$row = mysqli_fetch_row($result);
$old = $row[0];
if (substr($balance, 0,1) == "-")
{
	$balance = substr($balance, 1);
	$new = (int)$old - (int)$balance;
	$result= mysqli_query($link, "UPDATE `chat$chatid` SET `balance`='$new' WHERE `tgid`='$tgid'");	
}
else
{
	$new = (int)$old + (int)$balance;
	$result= mysqli_query($link, "UPDATE `chat$chatid` SET `balance`='$new' WHERE `tgid`='$tgid'");	
}


?>