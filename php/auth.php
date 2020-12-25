<?php
require "bd.php";

$tgid = $_POST['tgid'];
$name = $_POST['name'];
$username = $_POST['username'];
$result= mysqli_query($link, "INSERT INTO `usersnumb`(`tgid`, `name`, `username`, `balance`) VALUES ('{$tgid}', '{$name}', '{$username}', '100')");

?>