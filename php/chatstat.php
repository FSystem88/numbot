<?php
require "bd.php";

$chatid = $_POST['chatid'];

$result= mysqli_query($link, "select * from chat$chatid order by `balance` desc limit 0,10");

$row = mysqli_fetch_all($result);
echo json_encode($row);

?>

