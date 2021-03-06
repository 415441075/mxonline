from django.db import models
from datetime import datetime


# Create your models here.
# 城市信息，用户课程机构所在城市选择
class CityDict(models.Model):
	name = models.CharField(max_length=20, verbose_name='城市')
	desc = models.TextField(max_length=200, verbose_name='描述')
	add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

	class Meta:
		verbose_name = '城市'
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.name


# 课程机构信息
class CourseOrg(models.Model):
	choices = (('pxjg', '培训机构'), ('gr', '个人'), ('gx', '高校'))
	city = models.ForeignKey(CityDict, on_delete=models.CASCADE, verbose_name='所在城市')
	name = models.CharField(max_length=50, verbose_name='机构名称')
	desc = models.TextField(verbose_name='机构描述')
	category = models.CharField(max_length=20, default='pxjg', verbose_name='机构类别', choices=choices)
	click_nums = models.IntegerField(default=0, verbose_name='点击数')
	fav_nums = models.IntegerField(default=0, verbose_name='收藏数')
	image = models.ImageField(upload_to='org/%y/%m', verbose_name='封面图')
	address = models.CharField(max_length=150, verbose_name='机构地址')
	students = models.IntegerField(default=0, verbose_name='学习人数')
	course_nums = models.IntegerField(default=0, verbose_name='课程数')
	add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

	class Meta:
		verbose_name = '课程机构'
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.name


# 机构里的讲师信息
class Teacher(models.Model):
	org = models.ForeignKey(CourseOrg, on_delete=models.CASCADE, verbose_name='所属机构')
	name = models.CharField(max_length=50, verbose_name='教师名')
	work_years = models.IntegerField(default=0, verbose_name='工作年限')
	work_company = models.CharField(max_length=50, verbose_name='就职公司')
	work_position = models.CharField(max_length=50, verbose_name='公司职位')
	points = models.CharField(max_length=50, verbose_name="教学特点")
	click_nums = models.IntegerField(default=0, verbose_name='点击数')
	fav_nums = models.IntegerField(default=0, verbose_name='收藏数')
	image = models.ImageField(max_length=100, upload_to='teacher/%y/%m', verbose_name='头像', default="")
	add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

	class Meta:
		verbose_name = '教师'
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.name
