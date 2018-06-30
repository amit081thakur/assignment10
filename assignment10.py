Python 3.7.0b5 (v3.7.0b5:abb8802389, May 31 2018, 01:54:01) [MSC v.1913 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #Q.1- Create a circle class and initialize it with radius. Make
>>> #two methods getArea and
>>> #getCircumference inside this class.
>>>
>>>
>>> class circle:
	def __init__(self,radius):
		self.radius = radius
	def area(self):
		return self.radius*self.radius*3.14
	def par(self):
		return self.radius*3.14*2

	
>>> c = circle(2)
>>> c.area()
12.56
>>> c.par()
12.56
>>> a= circle(3)
>>> a.area()
28.26
>>> a.par()
18.84
>>>
>>>
>>>
>>> #Q.2- Create a Student class and initialize it with name and roll
>>> #number. Make methods to :
>>> #1. Display - It should display all informations of the student.
>>>
>>>
>>> class student:
	def __init__(self,name,roll):
		self.name = name
		self.roll = roll
	def display(self):
		print("student info")
		print(self.name)
		print(self.roll)

		
>>> c = student("amit",12)
>>> s.display()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    s.display()
NameError: name 's' is not defined
>>> c.display()
student info
amit
12
>>>
>>>
>>> #Q.3- Create a Temprature class. Make two methods :
>>> #1. convertFahrenheit - It will take celsius and will print it into Fahrenheit.
>>> #2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.
>>>
>>>
>>> class temp:
	def __init__(self,cel,far):
		self.cel=cel
		self.far=far
	def convert_far(self):
		p = self.cel*1.8+32
		print(p,"F")
	def convert_cel(self):
		q = self.far-32
		a = q/1.8
		print(a,"C")

		
>>> m = temp(34,23)
>>> m.convert_far()
93.2 F
>>> m.convert_cel()
-5.0 C
>>> 
>>>
>>>
>>> #Q.4- Create a class MovieDetails and initialize it with Movie name, artistname,Year of release and ratings .
>>> #Make methods to 
>>> #1. Display-Display the details.
>>> #2. Update- Update the movie details.
>>>
>>>
>>> class movie_detail:
	def __init__(self,movie,actor,release,rating):
		self.movie = movie
		self.actor = actor
		self.release = release
		self.rating = rating
	def display(self):
		print("movie = ",self.movie)
		print("actor = ",self.actor)
		print("release = ",self.release)
		print("rating = ",self.rating)
	def update(self):
		print( "update movie = ")
		self.movie = str(input())
		print("update actor =")
		self.actor = str(input())	      
		print("update release = ")
		self.release = str(input())     
		print("update rating = ")
		self.rating =  str(input())

		
>>> m= movie_detail("rampage","rock","13th may","****")
>>> m.display()
movie =  rampage
actor =  rock
release =  13th may
rating =  ****
>>> m.update()
update movie = 
race 3
update actor =
salman khan
update release = 
14th may
update rating = 
***
>>> m.display()
movie =  race 3
actor =  salman khan
release =  14th may
rating =  ***
>>>
>>>
>>>
>>> #Q.5- Create a class Expenditure and initialize it with expenditure,savings.Make the following methods. 
>>> #1. Display expenditure and savings 
>>> #2. Calculate total salary
>>> #3. Display salary
>>>
>>>
>>> >>> class expenditure:
	p = 0
	def __init__(self,expenses,saving):
		self.expenses = expenses
		self.saving = saving
	def display(self):
		print("the expenditure is = ",self.expenses)
		print("the saving is = ", self.saving)
	def salary(self):
		p = self.expenses + self.saving
		return p

			
>>> m = expenditure
>>> n = expenditure(45000,15000)
>>> n.salary()
60000
>>>
>>>



