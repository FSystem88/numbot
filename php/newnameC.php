<?php
require "bd.php";

$chatid = $_POST['chatid'];
$tgid = $_POST['tgid'];
$name = $_POST['name'];
$chatid = substr($chatid, 1);
$result= mysqli_query($link, "UPDATE `chat$chatid` SET `name`='{$name}' WHERE `tgid`='{$tgid}'");

?>