import psycopg2
from psycopg2 import OperationalError
from i_course_factory import ICourseFactory
from teacher import Teacher
from i_teacher import ITeacher
from i_course import ICourse
from offsite_course import OffsiteCourse
from local_course import LocalCourse


class CoursesFactory(ICourseFactory):
    """
    class implements ICourseFactory
    """
    def __init__(self, host, database, user, password):
        """
        class constructor
        """
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.__container = list()
        try:
            self.__conn = psycopg2.connect(
                host=self.host, database=self.database, user=self.user, password=self.password)
            self.__cursor = self.__conn.cursor()
        except OperationalError:
            raise OSError('invalid connection or invalid data')

    @property
    def container(self):
        """
        propery container
        """
        return self.__container

    @property
    def host(self):
        """
        propery host
        """
        return self.__host

    @host.setter
    def host(self, value):
        """
        setter propery host
        """
        if not isinstance(value, str):
            raise TypeError('host name must be str')
        self.__host = value

    @property
    def database(self):
        """
        propery database
        """
        return self.__database

    @database.setter
    def database(self, value):
        """
        setter propery database
        """
        if not isinstance(value, str):
            raise TypeError('database name must be str')
        self.__database = value

    @property
    def user(self):
        """
        propery user
        """
        return self.__user

    @user.setter
    def user(self, value):
        """
        setter propery user
        """
        if not isinstance(value, str):
            raise TypeError('user name must be str')
        self.__user = value

    @property
    def password(self):
        """
        propery password
        """
        return self.__password

    @password.setter
    def password(self, value):
        """
        setter propery password
        """
        if not isinstance(value, str):
            raise TypeError('password must be str')
        self.__password = value

    def pack(self, *args):
        """
        method for pack courses and teachers in database
        """
        for item in args:
            if isinstance(item, ITeacher):
                self.__cursor.execute(
                    f'INSERT INTO teacher ("name", "courses") VALUES (\'{item.name}\', \'{item.courses}\')')
                self.__conn.commit()
            elif isinstance(item, ICourse):
                if "LocalCourse" == item.__class__.__name__:
                    self.__cursor.execute(
                        f'INSERT INTO course ("name", "teacher_name", "place", "program", "is_local") VALUES (\'{item.name}\', \'{item.teacher.name}\', \'{item.room}\', \'{item.program}\', \'TRUE\')')
                    self.__conn.commit()
                elif "OffsiteCourse" == item.__class__.__name__:
                    self.__cursor.execute(
                        f'INSERT INTO course ("name", "teacher_name", "place", "program", "is_local") VALUES (\'{item.name}\', \'{item.teacher.name}\', \'{item.town}\', \'{item.program}\', \'False\')')
                    self.__conn.commit()
                else:
                    raise TypeError('unknown course')
            else:
                raise TypeError('u can pack only Teacher or Course')

    def unpack(self):
        """
        method for unpack courses and teachers from database
        """
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
                self.__container.append(LocalCourse(
                    c[0], cur_teacher, c[2], c[3]))
            else:
                for t in self.__container:
                    if t.name == c[1]:
                        cur_teacher = t
                        break
                self.__container.append(OffsiteCourse(
                    c[0], cur_teacher, c[2], c[3]))
