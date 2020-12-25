DROP TABLE IF EXISTS `usersnumb`;
CREATE TABLE `usersnumb` (
  `id` int(11) NOT NULL,
  `tgid` varchar(64) CHARACTER SET utf8 NOT NULL,
  `name` varchar(64) CHARACTER SET utf8 NOT NULL,
  `username` varchar(64) CHARACTER SET utf8 NOT NULL,
  `balance` int(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

ALTER TABLE `usersnumb`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `usersnumb`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;
