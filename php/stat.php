<?php
require "bd.php";

$tgid = $_POST['tgid'];

$result= mysqli_query($link, "select * from usersnumb WHERE `tgid` NOT LIKE '%-%' order by `balance` desc limit 0,10");

$row = mysqli_fetch_all($result);
echo json_encode($row);

?>

