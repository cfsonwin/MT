create database if not exists MyDatabase;
use mydatabase;
create table if not exists Administrator(
admin_id int auto_increment primary key,
Email varchar(100) not null unique,
u_name varchar(30) default 'administrator',
u_password varchar(100) not null,
u_status tinyint unsigned default '0',
addtime DATETIME,
modifytime DATETIME,
avatar varchar(100)
);

create table if not exists Constructor(
u_id int auto_increment primary key,
Email varchar(100) not null unique,
u_name varchar(30) default 'user',
u_password varchar(100) not null,
u_status tinyint unsigned default '0',
addtime DATETIME,
modifytime DATETIME,
avatar varchar(100),
addr varchar(100)
);

create table if not exists product(
p_id int auto_increment primary key,
p_name varchar(50) default 'virtual product',
u_status tinyint unsigned default '0',
addtime DATETIME,
modifytime DATETIME,
avatar varchar(100),
description text
);

create table if not exists Manufacturer(
m_id int auto_increment primary key,
parent_node int not null,
treelevel int not null,
contact varchar(100) not null,
addr varchar(100) not null,
loc varchar(100) not null,
u_status tinyint unsigned default '0',
addtime DATETIME,
modifytime DATETIME
);
