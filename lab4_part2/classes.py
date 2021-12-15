import psycopg2
from psycopg2 import OperationalError
from interfaces import ITeacher, ILocalCourse, ICourseFactory, IOffsiteCourse, ICourse


class Teacher(ITeacher):
    def __init__(self, name, courses):
        self.name = name
        self.courses = courses

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('name must be str')
        if not value.strip():
            raise ValueError('name can\'t be empty')
        self.__name = value

    @property
    def courses(self):
        return self.__courses

    @courses.setter
    def courses(self, value):
        if not isinstance(value, str):
            raise TypeError('courses must be str')
        self.__courses = value

    def __str__(self) -> str:
        return f'Teacher: {self.name}  Courses: {self.courses}'

class Course(ICourse):
    def __init__(self, name, teacher, program):
        self.name = name
        self.teacher = teacher
        self.program = program

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('name must be str')
        if not value.strip():
            raise ValueError('name can\'t be empty')
        self.__name = value

    @property
    def teacher(self):
        return self.__teacher

    @teacher.setter
    def teacher(self, value):
        if not isinstance(value, Teacher):
            raise TypeError('teacher must be Teacher type')
        self.__teacher = value

    @property
    def program(self):
        return self.__program

    @program.setter
    def program(self, value):
        if not isinstance(value, str):
            raise TypeError('program must be str type')
        self.__program = value

    def __str__(self) -> str:
        return f'Local course: {self.name}, Teacher: {self.teacher.name}, Program: {self.program}'


class LocalCourse(Course, ILocalCourse):
    def __init__(self, name, teacher, room, program):
        self.room = room
        super().__init__(name, teacher, program)

    @property
    def room(self):
        return self.__room

    @room.setter
    def room(self, value):
        if not isinstance(value, str):
            raise TypeError('room must be str type')
        self.__room = value

    def __str__(self) -> str:
        return f'Local course: {self.name}, Room: {self.room}, Teacher: {self.teacher.name}, Program: {self.program}'


class OffsiteCourse(Course, IOffsiteCourse):
    def __init__(self, name, teacher, town, program):
        self.town = town
        super().__init__(name, teacher, program)

    @property
    def town(self):
        return self.__town

    @town.setter
    def town(self, value):
        if not isinstance(value, str):
            raise TypeError('town must be str type')
        self.__town = value

    def __str__(self) -> str:
        return f'Offsite course: {self.name}, Town: {self.town}, Teacher: {self.teacher.name}, Program: {self.program}'


class CoursesFactory(ICourseFactory):
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.__container = list()
        try:
            self.__conn = psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password)
            self.__cursor = self.__conn.cursor()
        except OperationalError:
            raise OSError('invalid connection or invalid data')

    @property
    def container(self):
        return self.__container

    @property
    def host(self):
        return self.__host

    @host.setter
    def host(self, value):
        if not isinstance(value, str):
            raise TypeError('host name must be str')
        self.__host = value

    @property
    def database(self):
        return self.__database

    @database.setter
    def database(self, value):
        if not isinstance(value, str):
            raise TypeError('database name must be str')
        self.__database = value

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, value):
        if not isinstance(value, str):
            raise TypeError('user name must be str')
        self.__user = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if not isinstance(value, str):
            raise TypeError('password must be str')
        self.__password = value

    def pack(self, *args):
        for item in args:
            if isinstance(item, ITeacher):
                self.__cursor.execute(f'INSERT INTO teacher ("name", "courses") VALUES (\'{item.name}\', \'{item.courses}\')')
                self.__conn.commit()
            elif isinstance(item, ICourse):
                if "LocalCourse" == item.__class__.__name__:
                    self.__cursor.execute(f'INSERT INTO course ("name", "teacher_name", "place", "program", "is_local") VALUES (\'{item.name}\', \'{item.teacher.name}\', \'{item.room}\', \'{item.program}\', \'TRUE\')')
                    self.__conn.commit()
                elif "OffsiteCourse" == item.__class__.__name__:
                    self.__cursor.execute(f'INSERT INTO course ("name", "teacher_name", "place", "program", "is_local") VALUES (\'{item.name}\', \'{item.teacher.name}\', \'{item.town}\', \'{item.program}\', \'False\')')
                    self.__conn.commit()
                else:
                    raise TypeError('unknown course')
            else:
                raise TypeError('u can pack only Teacher or Course')

    def unpack(self):
        self.__cursor.execute('SELECT * FROM teacher')
        data = self.__cursor.fetchall()
        for t in data:
            self.__container.append(Teacher(t[0], t[1]))
        self.__cursor.execute('SELECT * FROM course')
        data = self.__cursor.fetchall()
        for c in data:
            if c[-1]:
                for t in self.__container:
                    if t.name == c[1]:
                        cur_teacher = t
                        break
                self.__container.append(LocalCourse(c[0], cur_teacher, c[2], c[3]))
            else:
                for t in self.__container:
                    if t.name == c[1]:
                        cur_teacher = t
                        break
                self.__container.append(OffsiteCourse(c[0], cur_teacher, c[2], c[3]))

