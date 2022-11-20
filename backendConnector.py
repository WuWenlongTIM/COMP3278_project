import mysql.connector
import faces
import time
import datetime
from datetime import datetime

conn = mysql.connector.connect(host = "localhost", user = 'root', password = 'sz123wwl', database = 'gp')
cur = conn.cursor()

current_active_user = 1

# login function, will set the current_active_user to userID, return 0 if success
def passwordLogin(input_userName, input_pwd):
    global current_active_user
    sql_query = f"SELECT userPassword, userID FROM UserInfo WHERE userName = \"{input_userName}\""
    cur.execute(sql_query)
    result = cur.fetchall()
    for user in result:
        if (user[0] == input_pwd):
            current_active_user = user[1]
            date = datetime.utcnow()
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            update =  "UPDATE UserInfo SET login_date = %s WHERE userName = %s"
            val = (date, input_userName)
            cur.execute(update, val)
            update =  "UPDATE UserInfo SET login_time = %s WHERE userName = %s"
            val = (current_time, input_userName)
            cur.execute(update, val)
            conn.commit()
            return 0
    return 1

# if successfully login, would record the latest login time
def faceLogin():
    global current_active_user
    current_active_user = faces.run()
    if current_active_user == 0:
        return 1
    return 0

# get current userID
def getUser():
    global current_active_user
    return current_active_user

def getUserInfo(userID):
    global current_active_user
    sql_query = f"SELECT userName, photoAddress FROM UserInfo WHERE userID = \"{userID}\""
    cur.execute(sql_query)
    result = cur.fetchall()
    return list(result[0])

# get the latest login time [yyyy-mm-dd, loginHour:loginMinute:loginSecond]
def getLoginTime():
    global current_active_user
    sql_query = f"SELECT login_date, login_time FROM UserInfo WHERE userID = \"{current_active_user}\""
    cur.execute(sql_query)
    result = cur.fetchall()
    loginTime =  result[0][1]
    loginSeconds = int(loginTime.total_seconds())
    loginHour = str(loginSeconds // 3600)
    loginMinute = str((loginSeconds % 3600) // 60)
    loginSecond = str(loginSeconds % 60)
    time = [result[0][0].isoformat(), loginHour + ":" + loginMinute + ":" + loginSecond]
    return time

# return the name of a teacher
def getTeacherName(teacherID):
    sql_query = f"SELECT teacherName FROM Teacher WHERE teacherID = \"{teacherID}\""
    cur.execute(sql_query)
    result = cur.fetchall()
    return result[0][0]

# return all the courses (courseID (str), ex. COMP3278) of the current user, no need to input userID
def getAllCourses():
    global current_active_user
    sql_query = f"SELECT courseID FROM UserHaveCourse WHERE userID = \"{current_active_user}\""
    cur.execute(sql_query)
    result = cur.fetchall()
    courses = []
    for c in result:
        courses.append(c[0])
    return courses

# return the info of one particular course, the input would be courseID
# the returned list would be like [courseID, courseName, courseVenue, courseMessage, zoomLink, noteLink, teacherID]
def getCourseInfo(courseID):
    sql_query = f"SELECT * FROM Course WHERE courseID = \"{courseID}\""
    cur.execute(sql_query)
    result = cur.fetchall()
    return list(result[0])

# return days of a course
def getCourseDay(CourseID):
    sql_query = f"SELECT courseDay FROM Timetable WHERE  courseID = \"{CourseID}\""
    cur.execute(sql_query)
    result = cur.fetchall()
    courseDay = []
    for i in result:
        courseDay.append(i[0])
    courseDay.sort()
    return courseDay

# get the start time ([hour, minute, second]) and end time of a course on a day
def getCourseTime(courseID, courseDay):
    sql_query = f"SELECT courseStartTime, courseEndTime FROM TimeTable WHERE courseID = \"{courseID}\" AND courseDay = \"{courseDay}\"" 
    cur.execute(sql_query)
    result = cur.fetchall()
    startTime = result[0][0]
    startSeconds = int(startTime.total_seconds())
    startHour = int(startSeconds // 3600)
    startMinute = int((startSeconds % 3600) // 60)
    startSecond = int(startSeconds % 60)
    endTime = result[0][1]
    endSeconds = int(endTime.total_seconds())
    endHour = int(endSeconds // 3600)
    endMinute = int((endSeconds % 3600) // 60)
    endSecond = int(endSeconds % 60)
    return [[startHour, startMinute, startSecond], [endHour, endMinute, endSecond]]

# return all the Exams (examID ex.1) of the current user, no need to input userID
def getAllExams():
    global current_active_user
    sql_query = f"SELECT Exam.examID FROM UserHaveCourse, Exam WHERE UserHaveCourse.userID = \"{current_active_user}\" AND Exam.courseID = UserHaveCourse.courseID"
    cur.execute(sql_query)
    result = cur.fetchall()
    exams = []
    for e in result:
        exams.append(e[0])
    return sorted(exams)

# return the info of one particular exam, the input would be examID
# the returned list would be like [examID, courseID, examDate, examNotice, examStartTime, examEndTime, examVenue]
def getExamInfo(examID):
    sql_query = f"SELECT * FROM Exam WHERE examID = \"{examID}\""
    cur.execute(sql_query)
    result = cur.fetchall()
    return list(result[0])

def getCourseInOneHour():
    global current_active_user
    CourseListInOneHour = []
    sql_query = f"""SELECT  T.courseID, T.courseDay FROM 
    (SELECT userID, courseID FROM UserHaveCourse WHERE userID = \"{current_active_user}\") current_users_course,  Timetable T
    WHERE current_users_course.courseID=T.courseID AND DAYOFWEEK(CURDATE()) = (T.courseDay % 7 + 1)
    AND SUBTIME(T.courseStartTime,CURTIME()) > \"00:00:00\"
    AND SUBTIME(T.courseStartTime,CURTIME()) < \"01:00:00\"
    ORDER BY T.courseStartTime"""
    cur.execute(sql_query)
    result = cur.fetchall()
    for c in result:
        CourseListInOneHour.append(list(c))
    return CourseListInOneHour

import smtplib
from pathlib import Path
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders

# no need to call this function
def sendEmail(send_to, subject, message, files=[],
              server="smtp.gmail.com", port=587, username='u3577259@connect.hku.hk', password='chen08x12tbbtr',
              use_tls=True):
    """Compose and send email with provided info and attachments.
    Args:
        send_from (str): from name
        send_to (list[str]): to name(s)
        subject (str): message title
        message (str): message body
        files (list[str]): list of file paths to be attached to email
        server (str): mail server host name
        port (int): port number
        username (str): server auth username
        password (str): server auth password
        use_tls (bool): use TLS mode
    """
    try:
        msg = MIMEMultipart()
        # msg['From'] = send_from
        msg['To'] = COMMASPACE.join(send_to)
        msg['Date'] = formatdate(localtime = True)
        msg['Subject'] = subject

        msg.attach(MIMEText(message))

        for path in files:
            part = MIMEBase('application', "octet-stream")
            with open(path, 'rb') as file:
                part.set_payload(file.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition',
                            'attachment; filename={}'.format(Path(path).name))
            msg.attach(part)

        smtp = smtplib.SMTP(server, port)
        if use_tls:
            smtp.starttls()
        smtp.login(username, password)
        # smtp.sendmail(send_from, send_to, msg.as_string())
        smtp.sendmail("", send_to, msg.as_string())
        
        smtp.quit()
    except:
        print("Error in sending emails. Please check.")

# the function for frontend to call to send email
def send(courseID, courseDay):
    global current_active_user
    sql_query = f"SELECT userName, email FROM UserInfo WHERE userID = \"{current_active_user}\""
    cur.execute(sql_query)
    result = cur.fetchall()
    send_to = [result[0][1],]
    subject = f"Upcoming Classes in one hour: {courseID}"
    courseInfo = getCourseInfo(courseID)
    time = getCourseTime(courseID, courseDay)
    start_time = f"{int(time[0][0])}:{int(time[0][1])}"
    message = f"""
Hi {result[0][0]}:
            
Your upcoming classes:
Coruse Name: {courseInfo[1]}
Start time: {start_time}
Venue: {courseInfo[2]}
Zoom link: {courseInfo[4]}
Note: {courseInfo[5]}
Course description: {courseInfo[3]}

Best,
ICMS
              """
    sendEmail(send_to, subject, message)
