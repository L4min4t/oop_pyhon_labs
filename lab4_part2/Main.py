# A software academy teaches two types of courses: local courses that are held in some of the academy’s local labs
# and offsite courses held in some other town outside of the academy’s headquarters. Each course has a name, a
# teacher assigned to teach it and a course program (sequence of topics). Each teacher has a name and knows the
# courses he or she teaches. Both courses and teachers could be printed in human-readable text form. All your courses
# should implement ICourse. Teachers should implement ITeacher. Local and offsite courses should implement ILocalCourse
# and IOffsiteCourse respectively. Courses and teachers should be created only through the ICourseFactory interface
# implemented by a class named CourseFactory. Write a program that will form courses of software academy.

from teacher import Teacher
from courses_factory import CoursesFactory
from offsite_course import OffsiteCourse
from local_course import LocalCourse


def main():
    x = Teacher('Boris', 'c++, java')
    w = Teacher('Evgenij', 'php')
    y = LocalCourse('C++ course', x, 'room #1', 'syntax and procedure programing')
    z = OffsiteCourse('Java course', x, 'Kyiv', 'base of oop')
    q = CoursesFactory("localhost", "lab4", "admin", "1111")
    # q.pack(w)
    # q.pack(x, y, z)
    q.unpack()
    for item in q.container:
       print(type(item), '\t', item)

if __name__ == '__main__':
    main()
