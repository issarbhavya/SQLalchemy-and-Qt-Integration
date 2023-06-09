from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.orm import declarative_base, sessionmaker

Base= declarative_base()  ## this will return a class
## this class will be the base for our classes or first class

class Person(Base):
    __tablename__ = 'person' # assigning a tablename
    
    ssn=Column("ssn",Integer, primary_key=True)
    name=Column("name", String)
    gender= Column("gender", String)
    age=Column("age", Integer)
    
    ## so, this was our basic person class and now, 
    ## we will declare a constructor where we pass all of this directly
    def __init__(self, ssn, name, gender, age):
        self.ssn=ssn
        self.name=name
        self.gender=gender
        self.age=age
        # all of the self.ssn,self.name are variables storing the data
        
    def __repr__(self): # returns a string representation of an object
        return f"({self.ssn} {self.name} {self.gender} {self.age})"
    
    
    
class Thing(Base):
    __tablename__ = "things"
    
    tid=Column("tid", Integer, primary_key=True)
    description=Column("desc",String)
    owner=Column("owner",ForeignKey("person.ssn"))
    
    def __init__(self,tid,description,owner):
        self.tid=tid
        self.description=description
        self.owner=owner
        
    def __repr__(self): # returns a string representation of an object
        return f"({self.tid} {self.description} {self.owner})"
        
        


## once we have the class/classes ready we need to have engine
engine= create_engine("sqlite:///mydb.db", echo=True)

## the below line takes all the classes(in this case one) that extends
## from base and creates them as tables in database
Base.metadata.create_all(bind=engine) #creates tables in the file allocated to engine

Session= sessionmaker(bind=engine) ##this is basically aclass 
## this class will be used to create an instance to be used

session=Session() #instance of class

## now, creating an object
p1=Person(1234,"bhavya issar","m",19)
session.add(p1) ##this will create a row in the table person

session.commit() #this will commit the changes/updates

##now if you want to add many
p2=Person(1223,"akku issar","m",14)
p3=Person(1213,"saransh issar","m",13)

session.add_all([p2,p3])
session.commit()

# the above was for create and insert now queries

# results= session.query(Person).all()
# print(results)

# results= session.query(Person).filter(Person.name == "akku issar")
# for res in results:
#     print(res) 

# results= session.query(Person).filter(Person.age > 15)
# for res in results:
#     print(res) 

# results= session.query(Person).filter(Person.name.like("%ss%"))
# for res in results:
#     print(res) 

# results= session.query(Person).filter(Person.name.in_(["akku issar"]))
# for res in results:
#     print(res) 

# print("\n\n\n")    
# print(repr(p2))  ## returns the complete row belonging to the object p2

t1=Thing(1,"laptop",p1.ssn)
t2=Thing(2,"keys",p1.ssn)
t3=Thing(3,"mouse",p3.ssn)
t4=Thing(4,"car",p2.ssn)
t5=Thing(5,"laptop",p2.ssn)

session.add_all([t1,t2,t3,t4,t5])
session.commit()

## a query to deal with both the tables together

results = session.query(Thing, Person).filter(Thing.owner == Person.ssn).filter(Person.name== "akku issar")
for res in results:
    print("\n\n",res) 

