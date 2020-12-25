<?php
require "bd.php";

$tgid = $_POST['tgid'];
$name = $_POST['name'];

$result= mysqli_query($link, "UPDATE `usersnumb` SET `name`='{$name}' WHERE `tgid`='{$tgid}'");

?>