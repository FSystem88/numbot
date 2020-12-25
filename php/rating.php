<?php
require "bd.php";

$tgid = $_POST['tgid'];

$result= mysqli_query($link, "SELECT * FROM usersnumb WHERE tgid=$tgid");
$row = mysqli_fetch_row($result);
$name = $row[2];
$balance = $row[4];

$result= mysqli_query($link, "SELECT COUNT(*) FROM usersnumb WHERE balance>$balance");
$row = mysqli_fetch_row($result);
$rang = $row[0];

$res = (int)$rang +1;

$array = ["rating" => "{$res}", "name" => "{$name}", "balance" => "{$balance}"];
echo json_encode($array);
?>