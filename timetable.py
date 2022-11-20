import tkinter as tk
from tkinter import ttk
import random
import datetime
import backendConnector as bc
import webbrowser
from tkinter.font import Font

class Greeting(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.container = container
        self.config(relief=tk.GROOVE, borderwidth=2)

        self.columnconfigure(1, weight=1)

        self.username = ""
        self.aimage = tk.PhotoImage()
        if bc.current_active_user != 0:
            self.lastlogintime = datetime.datetime.now()
            userInfo = bc.getUserInfo(bc.current_active_user)
            self.username += userInfo[0]
            self.aimage = tk.PhotoImage(file=userInfo[1])
        self.avatar = ttk.Label(self, image=self.aimage, relief=tk.GROOVE)
        self.avatar.grid(row=0, column=0, rowspan=3, padx=5, pady=5)
        self.greeting = ttk.Label(
            self, text="Welcome! " + self.username, font=("Arial", 30)
        )
        self.greeting.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

        self.lastlogtime = bc.getLoginTime()
        self.lastlogin = ttk.Label(
            self, text="Last login: " + self.lastlogtime[0] + "  " + self.lastlogtime[1]
        )
        self.lastlogin.grid(row=1, column=1, padx=10, sticky=tk.W)

        # time in the system
        self.staytime = ttk.Label(self, text="")
        self.staytime.grid(row=2, column=1, padx=10, sticky=tk.W)
        self.update()

        # logout botton
        icon = tk.PhotoImage(file="logout.png")
        self.logout_icon = icon.subsample(20, 20)
        self.logoutButton = ttk.Button(
            self, text="Logout", image=self.logout_icon, compound=tk.LEFT
        )
        self.logoutButton.grid(
            row=1, column=2, padx=10, rowspan=2, sticky=tk.SE, pady=5
        )
        self.logoutButton.bind("<Button>", self.logout)

        self.grid(row=0, column=0, sticky=tk.NSEW)

    # function to update the time on the system
    def update(self):
        self.stay = datetime.datetime.now() - self.lastlogintime
        # round to seconds
        self.stay -= datetime.timedelta(microseconds=self.stay.microseconds)
        self.staytime.config(text="Time in the system: " + str(self.stay))
        self.after(1000, self.update)

    def logout(self, event):
        self.container.container.logout()

class Course:
    def __init__(self, course_info, course_day, course_time):
        super().__init__()
        self.courseinfo = course_info
        self.courseid = course_info[0]
        self.coursename = course_info[1]
        self.coursevenue = course_info[2]
        self.coursemessage = course_info[3]
        self.courselink = course_info[4]
        self.coursenote = course_info[5]
        self.courseteacher = course_info[6]
        self.start = course_time[0]
        self.end = course_time[1]
        self.day = course_day

class Timetable(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.container = container
        self.config(relief=tk.GROOVE, borderwidth=2)

        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        for day in days:
            self.day = ttk.Label(self, text=day)
            self.day.grid(row=0, column=days.index(day) + 1, padx=30, pady=10)

        timeslot = [
            "9:00",
            "10:00",
            "11:00",
            "12:00",
            "13:00",
            "14:00",
            "15:00",
            "16:00",
            "17:00",
            "18:00",
        ]
        for time in timeslot:
            self.time = ttk.Label(self, text=time)
            self.time.grid(row=timeslot.index(time) + 1, column=0, padx=10, pady=15)

        courses = bc.getAllCourses()
        courselist = []
        for course in courses:
            days = bc.getCourseDay(course)
            for day in days:
                courselist.append(
                    Course(bc.getCourseInfo(course), day, bc.getCourseTime(course, day))
                )

        self.loadclass(courselist)

        # exam button
        icon = tk.PhotoImage(file="exam.png")
        self.exam_icon = icon
        self.examinfo = ttk.Button(
            self,
            text="Exam information",
            image=self.exam_icon,
            compound=tk.LEFT,
            command=self.showexaminfo,
            width=20,
        )
        self.examinfo.grid(
            row=len(timeslot) + 2,
            column=0,
            columnspan=7,
            sticky=tk.E,
            padx=10,
            pady=5,
        )

        self.grid(row=1, column=0, sticky=tk.NSEW)

    def showexaminfo(self):

        infowin = tk.Toplevel()
        infowin.title("Exam Information")
        infowin.geometry("750x400")
        infowin.resizable(False, False)

        examlist = []
        exams = bc.getAllExams()
        for examID in exams:
            examInfo = bc.getExamInfo(examID)
            startTime = examInfo[4]
            startSeconds = int(startTime.total_seconds())
            startHour = int(startSeconds // 3600)
            startMinute = int((startSeconds % 3600) // 60)
            startSecond = int(startSeconds % 60)
            endTime = examInfo[5]
            endSeconds = int(endTime.total_seconds())
            endHour = int(endSeconds // 3600)
            endMinute = int((endSeconds % 3600) // 60)
            endSecond = int(endSeconds % 60)
            start = [startHour, startMinute, startSecond]
            end = [endHour, endMinute, endSecond]
            examlist.append(
                [
                    str(examInfo[0]),
                    examInfo[1],
                    examInfo[2].isoformat(),
                    examInfo[3],
                    [start, end],
                    examInfo[6],
                ]
            )
        infolist = ["Course ID", "Date", "Exam time", "Exam venue"]

        for i in infolist:
            info = ttk.Label(infowin, text=i, font=("Arial bold", 15))
            info.grid(row=0, column=infolist.index(i), padx=30, pady=10, sticky=tk.W)
        for j in examlist:
            courseid = ttk.Label(infowin, text=j[1], font=("Arial", 15))
            courseid.grid(
                row=examlist.index(j) + 1, column=0, padx=30, pady=10, sticky=tk.W
            )
            date = ttk.Label(infowin, text=j[2], font=("Arial", 15))
            date.grid(
                row=examlist.index(j) + 1, column=1, padx=30, pady=10, sticky=tk.W
            )
            s = [str(i) for i in j[4][0]]
            e = [str(i) for i in j[4][1]]
            s.pop()
            e.pop()
            time = ":".join(s) + "-" + ":".join(e)
            time = ttk.Label(infowin, text=time, font=("Arial", 15))
            time.grid(
                row=examlist.index(j) + 1, column=2, padx=30, pady=10, sticky=tk.W
            )
            venue = ttk.Label(infowin, text=j[5], font=("Arial", 15))
            venue.grid(
                row=examlist.index(j) + 1, column=3, padx=30, pady=10, sticky=tk.W
            )

    def loadclass(self, courselist):

        for course in courselist:
            # generate random color
            r = random.randint(0, 127)
            g = random.randint(0, 127)
            b = random.randint(0, 127)
            canvas = tk.Canvas(
                self,
                width=1,
                height=1,
                bg="#%02x%02x%02x" % (r, g, b),
                relief=tk.RAISED,
                borderwidth=3,
            )
            hours = course.end[0] - course.start[0]
            canvas.grid(
                row=course.start[0] - 7,
                column=course.day,
                rowspan=hours,
                sticky=tk.NSEW,
            )
            canvas.create_text(
                55, 20 * hours, text=course.courseid, anchor=tk.CENTER, fill="white"
            )
            canvas.create_text(
                55,
                20 * hours + 15,
                text=course.coursevenue,
                anchor=tk.CENTER,
                fill="white",
            )


class Upcomingclass(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.config(relief=tk.GROOVE, borderwidth=2)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        # upcomingclass = bs.getCourseInOneHour()
        # for testing, need to be replaced by backend
        self.title = ttk.Label(self, text="Upcoming Class", font=("Arial", 30))
        self.title.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky=tk.W)

        courses = bc.getCourseInOneHour()
        if len(courses) == 0:
            upcomingclass = None
        else:
            courseID = courses[0][0]
            upcomingclass = Course(bc.getCourseInfo(courseID), courses[0][1], bc.getCourseTime(courseID, courses[0][1]))

        if upcomingclass == None:
            self.info = ttk.Label(
                self, text="No Upcoming Class in one hour", font=("Arial bold", 20)
            )
            self.info.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky=tk.W)
            self.rowconfigure(1, weight=1)
            self.rowconfigure(0, weight=0)
            self.grid(row=0, column=1, rowspan=2, sticky=tk.NSEW)
            return

        self.upcomingclass = upcomingclass

        self.infolist = [
            "Course ID",
            "Course name",
            "Venue",
            "Teacher's\nmessage",
            "Zoom Link",
            "Notes",
            "Teacher",
            "Time",
        ]

        for i in self.infolist:
            self.info = ttk.Label(self, text=i, font=("Arial bold", 15))
            self.info.grid(
                row=self.infolist.index(i) + 1, column=0, padx=10, pady=20, sticky=tk.W
            )
        self.loadupcomingclass(upcomingclass)

        # email button
        icon = tk.PhotoImage(file="email.png")
        self.email_icon = icon.subsample(21, 21)
        self.sendemail = ttk.Button(
            self,
            text="Send to my email",
            image=self.email_icon,
            compound=tk.LEFT,
            width=20,
            command = lambda: bc.send(courses[0][0], courses[0][1])
        )
        self.sendemail.grid(
            row=len(self.infolist) + 1,
            column=0,
            columnspan=3,
            sticky=tk.E,
            padx=10,
            pady=5,
        )

        self.grid(row=0, column=1, rowspan=2, sticky=tk.NSEW)

    def loadupcomingclass(self, upcomingclass):
        for j in self.upcomingclass.courseinfo:
            if self.upcomingclass.courseinfo.index(j) == 4:
                if j != None:
                    self.content = ttk.Label(
                        self,
                        text="<Click to join>",
                        font=("Arial", 15, "underline", "italic"),
                        width=24,
                    )
                    self.content.bind("<Button-1>", lambda e, url=j: self.open(url))
                else:
                    self.content = ttk.Label(self, text="Not Available", font=("Arial", 15), width=24)
            elif self.upcomingclass.courseinfo.index(j) == 5:
                if j != None:
                    self.content = ttk.Label(
                        self,
                        text="<Click to download>",
                        font=("Arial", 15, "underline", "italic"),
                        width=24,
                    )
                    self.content.bind("<Button-1>", lambda e, url=j: self.open(url))
                else:
                    self.content = ttk.Label(self, text="Not Available", font=("Arial", 15), width=24)
            elif self.upcomingclass.courseinfo.index(j) == 3:
                self.content = ttk.Label(
                    self,
                    text="<Click to view>",
                    font=("Arial", 15, "underline", "italic"),
                    width=24,
                )
                self.content.bind("<Button-1>", lambda e, msg=j: self.showmsg(msg))
            elif self.upcomingclass.courseinfo.index(j) == 6:
                teacherName = bc.getTeacherName(j)
                self.content = ttk.Label(self, text=teacherName, font=("Arial", 15), width=24)
            else:
                self.content = ttk.Label(self, text=j, font=("Arial", 15), width=24)
            self.content.grid(
                row=self.upcomingclass.courseinfo.index(j) + 1,
                column=1,
                pady=20,
                sticky=tk.W,
                columnspan=2,
            )

        # remove seconds
        s = [str(i) for i in upcomingclass.start]
        e = [str(i) for i in upcomingclass.end]
        s.pop()
        e.pop()

        self.start = ":".join(s)
        self.end = ":".join(e)
        self.time = ttk.Label(
            self, text=self.start + "-" + self.end, font=("Arial", 15)
        )
        self.time.grid(
            row=len(self.infolist), column=1, columnspan=2, pady=20, sticky=tk.W
        )

    def showmsg(self, msg):
        msgwin = tk.Toplevel()
        msgwin.title("Teacher's Message")
        msgwin.geometry("400x300")
        msgwin.resizable(False, False)
        T = tk.Label(msgwin, text=msg, wraplength=370, anchor='w', font=Font(size=16), justify='left')
        T.pack(fill='both',padx=10)

    def open(self, url):
        webbrowser.open(url)

class TimeTableFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.container = container
        self.timetable = Timetable(self)
        self.upcomingclassInfo = Upcomingclass(self)
        self.greeting = Greeting(self)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)
