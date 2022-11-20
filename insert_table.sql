INSERT INTO UserInfo (userID, userName, userPassword, email, `login_time`, `login_date`, photoAddress) VALUES(1, 'Tim', '123456', 'szwwl@connect.hku.hk',curtime() , current_date(),'Tim.png');
INSERT INTO UserInfo (userID, userName, userPassword, email, `login_time`, `login_date`, photoAddress) VALUES(2, 'James', 'abcdef', 'u3577259@connect.hku.hk', curtime(),current_date(), 'James.png');

INSERT INTO Teacher(teacherID, teacherType, teacherName) VALUES(1, "Assistant Professor", "Dr. Ping Luo");
INSERT INTO Teacher(teacherID, teacherType, teacherName) VALUES(2, "Associate Professor", "Dr. Kenneth K.Y. Wong ");
INSERT INTO Teacher(teacherID, teacherType, teacherName) VALUES(3, "Assistant Professor", "Dr. Hengshuang Zhao");
INSERT INTO Teacher(teacherID, teacherType, teacherName) VALUES(4, "Associate Professor", "Dr. Jimmy Jack-Man Woo");
INSERT INTO Teacher(teacherID, teacherType, teacherName) VALUES(5, "Lecturer", "Dr. H.H. Cheung");
INSERT INTO Teacher(teacherID, teacherType, teacherName) VALUES(6, "Lecturer", "Dr. Cynthia Xiyue Cao");
INSERT INTO Teacher(teacherID, teacherType, teacherName) VALUES(7, "Professor", " Dr. Yue Chim Richard Wong ");
INSERT INTO Teacher(teacherID, teacherType, teacherName) VALUES(8, "Professor", "Dr. Lawrence K. Yeung");

INSERT INTO Course (courseID, courseName, courseVenue, courseMessage, zoomLink, noteLink, teacherID) VALUES("COMP3278","Database Systems", "MWT2", "Welcome to COMP3278A! The slides and videos of the lectures and tutorials will be released. The slides are \".pdf\" files with one slide on one page (1-by-1 scheme). Please print multiple pages (slides) on one paper in order to play green.", "https://hku.zoom.us/j/96226740999?pwd=ZER1UUdxSVVhQzNXbXFkUDd3WjRBdz09","https://moodle.hku.hk/mod/resource/view.php?id=2665229", 1);
INSERT INTO Course (courseID, courseName, courseVenue, courseMessage, noteLink, teacherID) VALUES("COMP2396","Java Programming", "CPD-LG.18","Welcome to the course COMP2396A Object-Oriented Programming and Java. We will have our first lecture tomorrow at CPD-LG.18 from 10:30 am to 12:20 pm. I have uploaded my lecture slides to Moodle and you may download them before the lecture. Looking forwards to seeing you all tomorrow.","https://moodle.hku.hk/mod/resource/view.php?id=2654688", 2);
INSERT INTO Course (courseID, courseName, courseVenue, courseMessage, zoomLink, noteLink, teacherID) VALUES("COMP3314","Machine Learning", "MWT7", "Teaching mode: Offline classes at MWT7, Tuesday 12:30 pm - 1:20 pm, and Friday 12:30 pm - 2:20 pm.Format for the quizzes and final exam: Candidates are permitted to bring to the examination ONE sheet(s) of A4-sized paper with printed/written notes on both sides.", "https://hku.zoom.us/j/97117576985?pwd=TXpLSTl3SU9jbzNPcG9CQzFreHBFUT09","https://moodle.hku.hk/mod/resource/view.php?id=2691557", 3);
INSERT INTO Course (courseID, courseName, courseVenue, courseMessage, zoomLink, noteLink, teacherID) VALUES("FINA1310", "Corporate Finance", "MWT6", "This is an introductory finance course that develops the basic concepts and tools applicable to corporate financial decisions. Two main tasks of financial managers are studied: project evaluation and financing decisions.","https://hku.zoom.us/j/98062678471?pwd=VE8vNkQwNmwydVZxUjJMV2lIVkJBdz09" ,"https://moodle.hku.hk/mod/resource/view.php?id=2606016", 4);
INSERT INTO Course (courseID, courseName, courseVenue, courseMessage, noteLink, teacherID) VALUES("IMSE2109", "Engineering Design", "HW1-6", "Course Objectives: Present and explain the general principles and practice of engineering drawing, Teach the general principles of product and tool design, and computer aided design (CAD) and drafting, Give students practice in using contemporary CAD systems to prepare 3D models and engineering drawings","https://moodle.hku.hk/mod/resource/view.php?id=2658631", 5);
INSERT INTO Course (courseID, courseName, courseVenue, courseMessage, zoomLink, noteLink, teacherID) VALUES("ECON1220", "Introductory Macroeconomics", "KK101", "This course is an introduction to macroeconomics, the study of business cycle fluctuations and long-run economic growth","https://hku.zoom.us/j/94379995865?pwd=ZlBNTDZ2Uk5hWnlsckw5bit1NENvUT09","https://moodle.hku.hk/mod/resource/view.php?id=2669571", 6);
INSERT INTO Course (courseID, courseName, courseVenue, courseMessage, noteLink, teacherID) VALUES("CCHU9068","Liberalism and Nationalism", "KB223", "Welcome! The tutorial signup begins this Saturday (10 Sept) at 10:30am (i.e., right after the lecture) via HKU Portal. A tentative tutorial schedule has already been uploaded onto Moodle for your reference as well. The first tutorial starts next week (except for Monday groups).","https://moodle.hku.hk/mod/resource/view.php?id=2675104", 7);
INSERT INTO Course (courseID, courseName, courseVenue, courseMessage, noteLink, teacherID) VALUES("CCST9003","Everyday Computing", "KKLG109", "The process of using computers to complete a task. The Internet is the largest computer network. To appreciate how they relate to  important/controversial topics in today's world","https://moodle.hku.hk/mod/resource/view.php?id=2693460", 8);

INSERT INTO UserHaveCourse(userID, courseID) VALUES(1, "COMP2396");
INSERT INTO UserHaveCourse(userID, courseID) VALUES(1, "COMP3314");
INSERT INTO UserHaveCourse(userID, courseID) VALUES(1, "COMP3278");
INSERT INTO UserHaveCourse(userID, courseID) VALUES(1, "CCST9003");
INSERT INTO UserHaveCourse(userID, courseID) VALUES(1, "FINA1310");
INSERT INTO UserHaveCourse(userID, courseID) VALUES(1, "ECON1220");
INSERT INTO UserHaveCourse(userID, courseID) VALUES(2, "COMP3314");
INSERT INTO UserHaveCourse(userID, courseID) VALUES(2, "COMP2396");
INSERT INTO UserHaveCourse(userID, courseID) VALUES(2, "COMP3278");
INSERT INTO UserHaveCourse(userID, courseID) VALUES(2, "IMSE2109");
INSERT INTO UserHaveCourse(userID, courseID) VALUES(2, "CCHU9068");

INSERT INTO TimeTable (courseID, courseStartTime, courseEndTime, courseDay) VALUES("COMP3278", "14:30", "15:20", 1);
INSERT INTO TimeTable (courseID, courseStartTime, courseEndTime, courseDay) VALUES("COMP3278", "13:30", "15:20", 4);
INSERT INTO TimeTable (courseID, courseStartTime, courseEndTime, courseDay) VALUES("COMP3314", "12:30", "13:20", 2);
INSERT INTO TimeTable (courseID, courseStartTime, courseEndTime, courseDay) VALUES("COMP3314", "12:30", "14:20", 5);
INSERT INTO TimeTable (courseID, courseStartTime, courseEndTime, courseDay) VALUES("COMP2396", "10:30", "12:20", 2);
INSERT INTO TimeTable (courseID, courseStartTime, courseEndTime, courseDay) VALUES("COMP2396", "10:30", "12:20", 4);
INSERT INTO TimeTable (courseID, courseStartTime, courseEndTime, courseDay) VALUES("IMSE2109", "13:30", "16:20", 2);
INSERT INTO TimeTable (courseID, courseStartTime, courseEndTime, courseDay) VALUES("CCHU9068", "09:30", "10:20", 4);
INSERT INTO TimeTable (courseID, courseStartTime, courseEndTime, courseDay) VALUES("CCHU9068", "08:30", "10:30", 6);
INSERT INTO TimeTable (courseID, courseStartTime, courseEndTime, courseDay) VALUES("FINA1310", "15:30", "16:20", 1);
INSERT INTO TimeTable (courseID, courseStartTime, courseEndTime, courseDay) VALUES("FINA1310", "13:30", "16:20", 2);
INSERT INTO TimeTable (courseID, courseStartTime, courseEndTime, courseDay) VALUES("ECON1220", "09:30", "10:20", 2);
INSERT INTO TimeTable (courseID, courseStartTime, courseEndTime, courseDay) VALUES("ECON1220", "09:30", "11:20", 5);
INSERT INTO TimeTable (courseID, courseStartTime, courseEndTime, courseDay) VALUES("CCST9003", "16:30", "17:20", 1);
INSERT INTO TimeTable (courseID, courseStartTime, courseEndTime, courseDay) VALUES("CCST9003", "16:30", "18:20", 3);

INSERT INTO Exam (examID, courseID, examDate, examNotice, examStartTime, examEndTime, examVenue) VALUES(1, "COMP2396", "2022-12-15", "Candidates are permitted to bring to the examination ONE sheet of A4-sized paper with printed/written notes on both sides.", "14:30", "16:30", "Flora Ho Sports Ctr.");
INSERT INTO Exam (examID, courseID, examDate, examNotice, examStartTime, examEndTime, examVenue) VALUES(2, "COMP3278", "2022-12-14", "Candidates are permitted to bring to the examination ONE sheet of A4-sized paper with printed/written notes on both sides.", "14:30", "17:30", "CPD-LG.07-10");
INSERT INTO Exam (examID, courseID, examDate, examNotice, examStartTime, examEndTime, examVenue) VALUES(3, "COMP3314", "2022-12-21", "Candidates are permitted to bring to the examination ONE sheet of A4-sized paper with printed/written notes on both sides.", "14:30", "16:30", "CPD-LG.07-10");
INSERT INTO Exam (examID, courseID, examDate, examStartTime, examEndTime, examVenue) VALUES(4, "FINA1310", "2022-12-08", "14:30", "16:30", "Flora Ho Sports Ctr.");
INSERT INTO Exam (examID, courseID, examDate, examStartTime, examEndTime, examVenue) VALUES(5, "ECON1220", "2022-12-17", "14:30", "16:30", "Flora Ho Sports Ctr.");
