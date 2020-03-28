import datetime
from dataclasses import dataclass, field
from zhixuewang.models import Person, ExtendedList, StuClass, Sex, School, Subject, Phase, Grade
from zhixuewang.tools import int2datetime

@dataclass
class StuPerson(Person):
    """一些关于学生的信息"""
    name: str = ""
    id: str = ""
    gender: Sex = Sex.GIRL
    email: str = ""
    mobile: str = ""
    qq_number: str = ""
    birthday: int = 0
    avatar: str = ""
    code: str = ""
    clazz: StuClass = None


class StuPersonList(ExtendedList):
    """学生列表"""
    def find_by_code(self, code: str) -> StuPerson:
        """返回第一个准考证号为code的学生"""
        return self.find(lambda p: p.code == code)

    def find_all_by_code(self, code: str) -> ExtendedList[StuPerson]:
        """返回所有准考证号为code的学生(其实不存在)"""
        return self.find_all(lambda p: p.code == code)

    def find_by_clazz_id(self, clazz_id: str) -> StuPerson:
        """返回第一个班级id为clazz_id的学生"""
        return self.find(lambda p: p.clazz.id == clazz_id)

    def find_all_by_clazz_id(self, clazz_id: str) -> ExtendedList[StuPerson]:
        """返回所有班级id为clazz_id的学生"""
        return self.find_all(lambda p: p.clazz.id == clazz_id)

    def find_by_clazz(self, clazz: StuClass) -> StuPerson:
        """返回第一个班级为clazz的学生"""
        return self.find(lambda p: p.clazz == clazz)

    def find_all_by_clazz(self, clazz: StuClass) -> ExtendedList[StuPerson]:
        """返回所有班级为clazz的学生"""
        return self.find_all(lambda p: p.clazz == clazz)

    def find_by_school_id(self, school_id: str) -> StuPerson:
        """返回第一个学校id为school_id的学生"""
        return self.find(lambda p: p.school.id == school_id)

    def find_all_by_school_id(self, school_id: str) -> ExtendedList[StuPerson]:
        """返回所有学校id为school_id的学生(其实不存在)"""
        return self.find_all(lambda p: p.school.id == school_id)

    def find_by_school(self, school: School) -> StuPerson:
        """返回第一个学校为school的学生"""
        return self.find(lambda p: p.school == school)

    def find_all_by_school(self, school: School) -> ExtendedList[StuPerson]:
        """返回所有学校为school的学生(其实不存在)"""
        return self.find_all(lambda p: p.school == school)





@dataclass
class QuestionTypeDTO:
    name: str
    code: str
    sort: str

@dataclass
class Difficulty:
    name: str
    code: str
    value: int

@dataclass
class Knowleage:
    code: str
    name: str

@dataclass
class QuestionOption:
    id: str
    desc: str

@dataclass
class QuestionDetail:
    question_id: str
    desc: str
    options: ExtendedList[QuestionOption]
    answer: str
    score: float
    name: str
    phase: Phase
    grades: ExtendedList[Grade]
    subject: Subject
    difficulty: Difficulty                # 难度
    raw_html: str = ""
    raw_image: str = ""
    answer_html: str = ""
    answer_image: str = ""
    analysis_html: str = ""
    analysis_image: str = ""
    knowleages: ExtendedList[Knowleage] = field(default_factory=ExtendedList)            # 知识点
    paper_name: str = ""

@dataclass
class Topic(QuestionDetail):
    id: str = ""
    stu_question_id: str = ""
    total_score: float = 0
    source_question_id: str = ""
    typeDTO: QuestionTypeDTO = None

    




@dataclass
class Answer:
    pass

@dataclass
class HomeWorkTypeDTO:
    type_name: str = ""
    type_code: int = 0

@dataclass
class HomeworkReport:
    title: str = ""
    stu_hw_id: str = ""
    score: float = 0
    min_score: float = 0
    max_score: float = 0
    cost_time: float = 0
    avg_time: float = 0
    standard_score: float = 0
    is_publish_answer_result: bool = False
    total_question_count: int = 0
    answers: ExtendedList[Answer] = field(default_factory=ExtendedList)

@dataclass
class HomeworkDetail:
    question_res: ExtendedList = field(default_factory=ExtendedList)
    answer_res: ExtendedList = field(default_factory=ExtendedList)
    stu_answer_res: ExtendedList = field(default_factory=ExtendedList)
    topics: ExtendedList[Topic] = field(default_factory=ExtendedList)
    need_answer: bool = False
    need_upload_process: bool = False

@dataclass
class Homework(HomeWorkTypeDTO, HomeworkDetail):
    title: str = ""
    id: str = ""
    stu_hw_id: str = ""
    subject: Subject = field(default_factory=Subject)
    begin_time: datetime.datetime = field(default=datetime.datetime(2018,1,1))
    end_time: datetime.datetime = field(default=datetime.datetime(2018,1,1))
    create_time: datetime.datetime = field(default=datetime.datetime(2018,1,1))
    answer_publish_time: datetime.datetime = 0

    def __post_init__(self):
        if isinstance(self.begin_time, int):
            self.begin_time = int2datetime(self.begin_time)
        if isinstance(self.end_time, int):
            self.end_time = int2datetime(self.end_time)
        if isinstance(self.create_time, int):
            self.create_time = int2datetime(self.create_time)