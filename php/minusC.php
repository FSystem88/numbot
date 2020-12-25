<?php
require "bd.php";

$tgid = $_POST['tgid'];
$chatid = $_POST['chatid'];
$name = $_POST['name'];
$username = $_POST['username'];
$balance = $_POST['balance'];
// 355821673

$result= mysqli_query($link, "SELECT balance FROM chat$chatid WHERE tgid='$tgid'");
$row = mysqli_fetch_row($result);
$old = $row[0];
if ($old == "") {
	$res = mysqli_query($link, "INSERT INTO `chat$chatid` (`tgid`, `name`, `username`, `balance`) VALUES ('$tgid', '$name', '$username', '0')");
	$old = 0;	
}

$new = (int)$old - (int)$balance;
$result= mysqli_query($link, "UPDATE `chat$chatid` SET `balance`='$new' WHERE `tgid`='$tgid'");

?>