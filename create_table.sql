DROP DATABASE IF EXISTS `gp`;
CREATE DATABASE `gp`;
USE `gp`;

CREATE TABLE UserInfo (
  userID INT(10) NOT NULL,
  userName VARCHAR(30) NOT NULL,
  userPassword VARCHAR(15) NOT NULL,
  email VARCHAR(30) NULL,
  login_time time NOT NULL,
  login_date date NOT NULL,
  photoAddress VARCHAR(480) NULL,
  PRIMARY KEY (userID)
);

CREATE TABLE Teacher(
	teacherID INT(10) NOT NULL,
    teacherType VARCHAR(30) NULL,
    teacherName VARCHAR(480) NULL,
    PRIMARY KEY (teacherID)
);

-- CREATE TABLE Record(
-- 	userID INT(10) NOT NULL,
-- 	recordID INT(10) NOT NULL,
--     recordTime time NOT NULL,
--     recordType VARCHAR(30) NULL,
-- 	oldInfo VARCHAR(480) NULL,
--     newInfo VARCHAR(480) NULL,
--     PRIMARY KEY (recordID),
--     FOREIGN KEY (userID) REFERENCES UserInfo(userID)
-- );

CREATE TABLE Course
(
    courseID VARCHAR(10) NOT NULL,
    courseName VARCHAR(480) NOT NULL,
    courseVenue VARCHAR(30) NOT NULL,
    courseMessage VARCHAR(500) NULL,
    zoomLink VARCHAR(480) NULL,
    noteLink VARCHAR(480) NULL,
    teacherID INT(10) NOT NULL,
    PRIMARY KEY(courseID),
    FOREIGN KEY(teacherID) REFERENCES Teacher(teacherID)
);

CREATE TABLE UserHaveCourse(
	userID INT(10) NOT NULL,
    courseID VARCHAR(10) NOT NULL,
	FOREIGN KEY (userID) REFERENCES UserInfo(userID),
    FOREIGN KEY(courseID) REFERENCES Course(courseID),
	PRIMARY KEY(userID, courseID)
);

CREATE TABLE Exam
(
    examID INT(10) NOT NULL,
    courseID VARCHAR(10) NOT NULL,
    examDate date NOT NULL,
    examNotice VARCHAR(480) NULL,
    examStartTime time NOT NULL,
    examEndTime time NOT NULL,
    examVenue VARCHAR(30) NOT NULL,
    PRIMARY KEY(examID),
    FOREIGN KEY(courseID) REFERENCES Course(courseID)
);

CREATE TABLE TimeTable
(
    courseID VARCHAR(10) NOT NULL,
    courseStartTime time NOT NULL,
    courseEndTime time NOT NULL,
    courseDay INT NOT NULL,
    PRIMARY KEY(courseID,  courseStartTime, courseEndTime, courseDay),
    FOREIGN KEY(courseID) REFERENCES Course(courseID)
);
