<?php

require "bd.php";

$chatid = $_POST['chatid'];
$res = mysqli_query($link, "CREATE TABLE `chat$chatid` (`id` int(11) NOT NULL,`tgid` varchar(64) CHARACTER SET utf8 NOT NULL,`name` varchar(64) CHARACTER SET utf8 NOT NULL,`username` varchar(64) CHARACTER SET utf8 NOT NULL,`balance` int(64) NOT NULL) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;");
$res = mysqli_query($link, "ALTER TABLE `chat$chatid` ADD PRIMARY KEY (`id`)");
$res = mysqli_query($link, "ALTER TABLE `chat$chatid` MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1");

?>