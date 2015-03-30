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

CREATE TABLE IF NOT EXISTS `player_attr` (

  `id` int(11) NOT NULL AUTO_INCREMENT,
  `player_id` char(36) NOT NULL,
  `full_name` varchar(100) NOT NULL,
  `batting_style` varchar(20) NOT NULL,
  `bowling_style` varchar(20) NOT NULL,
  `birth_date` date NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `player_id` (`player_id`)


) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;
