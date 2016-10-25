#coding:utf8
from volunteer_backend import *
import datetime


def testCreateVolunteerNew():
    deleteVolunteerAll()
    createVolunteer('vol1', {'password': 'mima',
                             'realName': u'李昊阳',
                            'birth': datetime.datetime(2015, 1, 12),
                            'idNumber': '123456789123456789',

                            'type': 1,
                            'sex': 1,
                            'nation': 1,
                            'school': u'清华大学',
                            'classroom': u'计41',

                            'address': u'武汉长江大桥下',
                            'phone': '18812344321',
                            'email': 'alienlhy@163.com',
                            'dadPhone': '17845699654',
                            'momPhone': '17845699654',

                            'tutorName': u'李明',
                            'tutorPhone': '13800000000',
                            'province': 1,
                            'major': [1,2],
                            'testScoreList': [100, 99, 98],

                            'rankList': [1, 2, 3],
                            'sumNumberList': [1000, 2000, 3000],
                            'estimateScore': 690,
                            'realScore': 687,
                            'admissionStatus': 1,

                            'comment': u'娃是好娃，就是成绩不太好',
                            # 'registerCode': ,
                            'teacherList': ['houyf1', 'houyf2'],
                            'studentAccountList': ['lihy1', 'lihy2', 'lihy3'],
                            'isLogedin': 0,

                            'isRegistered': 0,
                            'groupList': [1, 2],
                             'student_id': '2014011419'
                            })

    createVolunteer('vol2', {'password': 'mima',
                             'realName': u'杨凯琳',
                            'birth': datetime.datetime(2015, 1, 12),
                            'idNumber': '123456789123456789',

                            'type': 1,
                            'sex': 2,
                            'nation': 3,
                            'school': u'清华大学',
                            'classroom': u'计41',

                            'address': u'武汉长江大桥下',
                            'phone': '18812344321',
                            'email': 'alienlhy@163.com',
                            'dadPhone': '17845699654',
                            'momPhone': '17845699654',

                            'tutorName': u'李明',
                            'tutorPhone': '13800000000',
                            'province': 1,
                            'major':[1,2],
                            'testScoreList': [100, 99, 98],

                            'rankList': [1, 2, 3],
                            'sumNumberList': [1000, 2000, 3000],
                            'estimateScore': 690,
                            'realScore': 687,
                            'admissionStatus': 1,

                            'comment': u'娃是好娃，就是成绩不太好',
                            # 'registerCode': ,
                            'teacherList': ['houyf1', 'houyf2'],
                            'studentAccountList': ['lihy1', 'lihy2', 'lihy3'],
                            'isLogedin': 0,

                            'isRegistered': 0,
                            'groupList': [1, 2],
                             'student_id': '2014011419'
                            })

    createVolunteer('vol3', {'password': 'mima',
                             'realName': u'王恒志',
                            'birth': datetime.datetime(2015, 1, 12),
                            'idNumber': '123456789123456789',

                            'type': 1,
                            'sex': 2,
                            'nation': 4,
                            'school': u'清华大学',
                            'classroom': u'计45',

                            'address': u'武汉长江大桥下',
                            'phone': '18812344321',
                            'email': 'alienlhy@163.com',
                            'dadPhone': '17845699654',
                            'momPhone': '17845699654',

                            'tutorName': u'李明',
                            'tutorPhone': '13800000000',
                            'province': 1,
                            'major': [1,2],
                            'testScoreList': [100, 99, 98],

                            'rankList': [1, 2, 3],
                            'sumNumberList': [1000, 2000, 3000],
                            'estimateScore': 690,
                            'realScore': 687,
                            'admissionStatus': 1,

                            'comment': u'娃是好娃，就是成绩不太好',
                            # 'registerCode': ,
                            'teacherList': ['houyf1', 'houyf2'],
                            'studentAccountList': ['lihy1', 'lihy4', 'lihy5'],
                            'isLogedin': 0,

                            'isRegistered': 0,
                            'groupList': [1, 2],
                             'student_id': '2014011419'
                            })

    createVolunteer('vol4', {'password': 'mima',
                             'realName': u'杨凯琳',
                            'birth': datetime.datetime(2015, 1, 12),
                            'idNumber': '123456789123456789',

                            'type': 1,
                            'sex': 1,
                            'nation': 1,
                            'school': u'清华大学',
                            'classroom': u'计45',

                            'address': u'武汉长江大桥下',
                            'phone': '18812344321',
                            'email': 'alienlhy@163.com',
                            'dadPhone': '17845699654',
                            'momPhone': '17845699654',

                            'tutorName': u'李明',
                            'tutorPhone': '13800000000',
                            'province': 1,
                            'major': [1,2],
                            'testScoreList': [100, 99, 98],

                            'rankList': [1, 2, 3],
                            'sumNumberList': [1000, 2000, 3000],
                            'estimateScore': 690,
                            'realScore': 687,
                            'admissionStatus': 1,

                            'comment': u'娃是好娃，就是成绩不太好',
                            # 'registerCode': ,
                            'teacherList': ['houyf1', 'houyf2'],
                            'studentAccountList': ['lihy7', 'lihy8', 'lihy9'],
                            'isLogedin': 0,

                            'isRegistered': 0,
                            'groupList': [1, 2],
                             'student_id': '2014011419'
                            })

    createVolunteer('vol5', {'password': 'mima',
                             'realName': u'杨凯琳',
                            'birth': datetime.datetime(2015, 1, 12),
                            'idNumber': '123456789123456789',

                            'type': 1,
                            'sex': 1,
                            'nation': 1,
                            'school': u'清华大学',
                            'classroom': u'生45',

                            'address': u'武汉长江大桥下',
                            'phone': '18812344321',
                            'email': 'alienlhy@163.com',
                            'dadPhone': '17845699654',
                            'momPhone': '17845699654',

                            'tutorName': u'李明',
                            'tutorPhone': '13800000000',
                            'province': 1,
                            'major': [1,2],
                            'testScoreList': [100, 99, 98],

                            'rankList': [1, 2, 3],
                            'sumNumberList': [1000, 2000, 3000],
                            'estimateScore': 690,
                            'realScore': 687,
                            'admissionStatus': 1,

                            'comment': u'娃是好娃，就是成绩不太好',
                            # 'registerCode': ,
                            'teacherList': ['houyf1', 'houyf2'],
                            'studentAccountList': ['lihy8', 'lihy9', 'lihy10'],
                            'isLogedin': 0,

                            'isRegistered': 0,
                            'groupList': [1, 2],
                             'student_id': '2014011419'
                            })



def testCreateVolunteer():
    createVolunteer("vol1", {Volunteer.ID_NUMBER: '123456789123456789',Volunteer.SCHOOL:u'南山中学', Volunteer.PROVINCE:12,
                             Volunteer.CLASSROOM: u'计45', Volunteer.REAL_NAME: u'李昊阳',
                             Volunteer.SEX:1,Volunteer.BIRTH: datetime.datetime(2015, 1, 12),
                             Volunteer.STUDENT_ACCOUNT_LIST: ['lihaoyang1', 'baiyunren1']})
    createVolunteer('vol2', {Volunteer.ID_NUMBER: '123456789123456789', Volunteer.SCHOOL: u'南山中学', Volunteer.PROVINCE: 0,
                                 Volunteer.CLASSROOM: u'计45', Volunteer.REAL_NAME: u'侯禺凡', Volunteer.SEX: 1,
                                 Volunteer.BIRTH: datetime.datetime(2015, 1, 12),
                             Volunteer.STUDENT_ACCOUNT_LIST: ['lihaoyang2', 'baiyunren2']})
    createVolunteer('vol3', {Volunteer.ID_NUMBER: '123456789123456789', Volunteer.SCHOOL: u'南山中学', Volunteer.PROVINCE: 0,
                                 Volunteer.CLASSROOM: u'计45', Volunteer.REAL_NAME: u'邵韵秋', Volunteer.SEX: 2,
                                 Volunteer.BIRTH: datetime.datetime(2018, 1, 12),
                                 Volunteer.STUDENT_ACCOUNT_LIST: ['lihaoyang3', 'baiyunren3']})
    createVolunteer('vol4', {Volunteer.ID_NUMBER: '123456789123456789', Volunteer.SCHOOL: u'南山中学', Volunteer.PROVINCE: 1,
                                 Volunteer.CLASSROOM: u'计45', Volunteer.REAL_NAME: u'侯禺凡', Volunteer.SEX: 1,
                                 Volunteer.BIRTH: datetime.datetime(2015, 1, 12),
                             Volunteer.STUDENT_ACCOUNT_LIST: ['lihaoyang4', 'baiyunren4']})
    createVolunteer('vol5', {Volunteer.ID_NUMBER: '123456789123456789', Volunteer.SCHOOL: u'南山中学', Volunteer.PROVINCE: 1,
                                 Volunteer.CLASSROOM: u'计45', Volunteer.REAL_NAME: u'邵韵秋', Volunteer.SEX: 2,
                                 Volunteer.BIRTH: datetime.datetime(2018, 1, 12),
                             Volunteer.STUDENT_ACCOUNT_LIST: ['lihaoyang5', 'baiyunren5']})
    createVolunteer('vol6', {Volunteer.ID_NUMBER: '123456789123456789', Volunteer.SCHOOL: u'南山中学', Volunteer.PROVINCE: 2,
                                 Volunteer.CLASSROOM: u'计45', Volunteer.REAL_NAME: u'侯禺凡', Volunteer.SEX: 1,
                                 Volunteer.BIRTH: datetime.datetime(2015, 1, 12),
                                 Volunteer.STUDENT_ACCOUNT_LIST: ['lihaoyang6', 'baiyunren6']})
