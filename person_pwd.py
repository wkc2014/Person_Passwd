#!/python
#-*-coding:utf-8-*-

# 密码规则：
# username：用户名，姓名：王大爷（wangdaye）
# domain：公司域名，公司域名：youku
# number：
# QQ号码	手机号码	出生年月	工号	常用数字
# 9254681	13688885555	19850504	10001	1·123·1234·12345·123456·520·521·2015····

# demo：
# 1. username拆分					wangdy、wdy、WangDaYe等
# 2. usename+常用数字				wangdaye123、wangdaye2008
# 3. domain+常用数字				youku123、youku2015
# 4. username+domain 				wangdayeyouku
# 5. username+domain+数字（短）	wangdayeyouku2015

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('name', help='Please enter the name split with [/]')
parser.add_argument('phone', help='Please enter the phone')
parser.add_argument('QQ', help='Please enter the qq')
parser.add_argument('birthday', help='Please enter the birthday')
parser.add_argument('Work_id', help='Please enter the Work_id')
# #注释掉公司的、下面定义了一个数组
# #parser.add_argument('compony', help='Please enter the company')

args = parser.parse_args()
t_name = args.name
t_phone = args.phone
t_qq = args.QQ
t_birthday = args.birthday
t_work_id  = args.Work_id
# #t_compony = args.compony
#定义两个数组
L = []		#letter
PWD = []	#passwd
total = 0 	#total passwd
#常用数字、年份等
normal = ['1','12','123','1234','12345','123456','1234567','12345678',\
			'123456789','520','1314','521','5201314','2012','2013','2014',\
			'2015','2016','_2012','_2013','_2014','_2015','_2016','321','@123',\
			'123!@#','!@#123','666','888','@1','..']
company = ['youku','tudou','yt']
def letter():
	name = t_name.split('/')
	# print len(name)
	if len(name) == 3:
		first_name = name[0]
		second_name = name[1]
		third_name = name[2]
		sim = first_name[0]+second_name[0]+third_name[0]
		C_first_name = first_name.capitalize()
		C_second_name = second_name.capitalize()
		C_third_name = third_name.capitalize()
		A_name = first_name+second_name+third_name
		C_a_name = C_first_name+C_second_name+C_third_name
		#First string Capital  capitalize()
		L.append(A_name)			# wangdaye
		L.append(first_name) 		# wang
		L.append(second_name)		# da
		L.append(third_name)		# ye
		L.append(sim)				# wdy
		L.append(sim.upper())		# WDY
		L.append(C_first_name) 		# Wang
		L.append(C_second_name)		# Da
		L.append(C_third_name)		# Ye
		L.append(A_name.capitalize())	# Wangdaye
		L.append(C_a_name)				# WangDaYe
		L.append(second_name+third_name)	# daye
		L.append(first_name+second_name[0]+third_name[0])				# wangdy
		L.append(first_name.capitalize()+second_name[0]+third_name[0])	# Wangdy
		L.append(first_name.capitalize()+second_name[0].upper()+third_name[0].upper())	# WangDY	
	elif len(name) == 2:
		first_name = name[0]
		second_name = name[1]
		sim = first_name[0]+second_name[0]
		C_first_name = first_name.capitalize()
		C_second_name = second_name.capitalize()
		A_name = first_name+second_name
		C_a_name = C_first_name+C_second_name
		#First string Capital  capitalize()
		L.append(A_name)			# wangda
		L.append(first_name) 		# wang
		L.append(second_name)		# da
		L.append(sim)				# wd
		L.append(sim.upper())		# WD
		L.append(C_first_name) 		# Wang
		L.append(C_second_name)		# Da
		L.append(A_name.capitalize())	# Wangda
		L.append(C_a_name)				# WangDa
		L.append(first_name+second_name[0])					# wangd
		L.append(first_name.capitalize()+second_name[0])	# Wangd
		L.append(first_name[0]+second_name)					# wangd
		L.append(first_name[0].capitalize()+second_name)	# Wda		
		L.append(first_name.capitalize()+second_name[0].upper())	# WangD
	else:
		print '\n'
		print 'Error Name!! Please enter name like "zhang/san"'
def name_add_normal():
	global total
	count = 0
	for items in L:
		for itt in normal:
			pwd = items+itt
			PWD.append(pwd)
			count = count + 1
	if count != 0:
		print '----------*****----------'
		print "Add Normal Count:  " ,count
		total = count + total
		return total
def name_add_company():
	global total
	count = 0
	for items in L:
		for itt in company:
			pwd = items+itt
			PWD.append(pwd)
			count = count + 1
	if count != 0:
		print '----------*****----------'
		print "Add Company Count: " ,count
		total = count + total
		return total
def name_add_Workid():
	global total
	count = 0
	for items in L:
		pwd = items+t_work_id
		PWD.append(pwd)
		count = count + 1
	if count != 0:
		print '----------*****----------'
		print "Add WorkID Count:  " ,count	  
		total = count + total
		return total
def name_add_birthday():
	#birthday 19900101----->>> 19900101/1990/0101
	global total
	count = 0
	birthday  = []
	birthday.append(t_birthday)
	birthday.append(t_birthday[:4])
	birthday.append(t_birthday[4:])
	for items in L:
		for bir_item in birthday:
			pwd = items + bir_item
			PWD.append(pwd)
			count = count + 1
	if count != 0:
		print '----------*****----------'
		print "Add birthday Count:" ,count
		total = count + total
		return total
def name_add_qq():
	global total
	count = 0
	for items in L:
		pwd = items+t_qq
		PWD.append(pwd)
		count = count + 1
	if count != 0:
		print '----------*****----------'
		print "Add QQ Count:      " ,count
		total = count + total
		return total
def name_add_phone():
	#phone 13612345678----->>> 5678
	global total
	count = 0
	for items in L:
		pwd = items+t_phone[7:]
		PWD.append(pwd)
		count = count + 1
	if count != 0:
		print '----------*****----------'
		print "Add Phone Count:   " ,count
		total = count + total
		return total
def name_company_workID():
	global total
	count = 0
	for items in L:
		for itt in company:
			pwd = items+itt
			PWD.append(pwd)
			count = count + 1
	if count != 0:
		print '----------*****----------'
		print "Name+Company+WorkID Count: " ,count
		total = count + total
		return total

if __name__ == '__main__':
	letter()
	name_add_normal()
	name_add_company()
	name_add_Workid()
	name_add_birthday()
	name_add_qq()
	name_add_phone()
	name_company_workID()
	try:
		with open('E:\\Python_code\\dict\\passwd.txt','w') as f:	
			for items in PWD:
				f.write(items + '\n')
		f.close()
	except IOError:
		print 'error'
	print '\n'
	print '----------*****----------'
	print 'Total Password :   ',total
	print '----------*****----------'
	print 'done!'
