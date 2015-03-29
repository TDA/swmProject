-- phpMyAdmin SQL Dump
-- version 3.4.5
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Mar 29, 2015 at 09:37 AM
-- Server version: 5.5.16
-- PHP Version: 5.3.8

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `swmProject`
--

-- --------------------------------------------------------

--
-- Table structure for table `batsmen_attr`
--

CREATE TABLE IF NOT EXISTS `batsmen_attr` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `player_id` char(36) NOT NULL,
  `full_name` varchar(100) NOT NULL,
  `batting_style` varchar(20) NOT NULL,
  `birth_date` date NOT NULL,
  `batting_average` float NOT NULL,
  `balls_taken` int(11) NOT NULL,
  `catches` int(11) NOT NULL,
  `ducks` int(11) NOT NULL,
  `fours` int(11) NOT NULL,
  `sixes` int(11) NOT NULL,
  `half_centuries` int(11) NOT NULL,
  `centuries` int(11) NOT NULL,
  `highest_score` int(11) NOT NULL,
  `innings` int(11) NOT NULL,
  `matches` int(11) NOT NULL,
  `not_outs` int(11) NOT NULL,
  `runs` int(11) NOT NULL,
  `stumpings` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `player_id` (`player_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `bowlers_attr`
--

CREATE TABLE IF NOT EXISTS `bowlers_attr` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `player_id` char(36) NOT NULL,
  `bowling_average` float NOT NULL,
  `balls_bowled` int(11) NOT NULL,
  `four_wicket` int(11) NOT NULL,
  `five_wicket` int(11) NOT NULL,
  `ten_wicket` int(11) NOT NULL,
  `innings` int(11) NOT NULL,
  `runs_given` int(11) NOT NULL,
  `strike_rate` float NOT NULL,
  `wickets` int(11) NOT NULL,
  `economy` float NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `player_id` (`player_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `batsmen_attr`
--
ALTER TABLE `batsmen_attr`
  ADD CONSTRAINT `batsmen_attr_ibfk_2` FOREIGN KEY (`player_id`) REFERENCES `bowlers_attr` (`player_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `batsmen_attr_ibfk_1` FOREIGN KEY (`id`) REFERENCES `bowlers_attr` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `bowlers_attr`
--
ALTER TABLE `bowlers_attr`
  ADD CONSTRAINT `bowlers_attr_ibfk_1` FOREIGN KEY (`id`) REFERENCES `batsmen_attr` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `bowlers_attr_ibfk_2` FOREIGN KEY (`player_id`) REFERENCES `batsmen_attr` (`player_id`) ON DELETE CASCADE ON UPDATE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
