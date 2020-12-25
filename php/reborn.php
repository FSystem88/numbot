<?php
require "bd.php";

$tgid = $_POST['tgid'];
$name = $_POST['name'];
$username = $_POST['username'];

$result= mysqli_query($link, "UPDATE `usersnumb` SET `tgid`='{$tgid}',`name`='{$name}',`username`='{$username}',`balance`='100' WHERE `tgid`='{$tgid}'");

?>