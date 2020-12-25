<?php
require "bd.php";

$tgid = $_POST['tgid'];

$result= mysqli_query($link, "SELECT * FROM usersnumb WHERE tgid='$tgid'");

$row = mysqli_fetch_assoc($result);
echo json_encode($row);

?>

