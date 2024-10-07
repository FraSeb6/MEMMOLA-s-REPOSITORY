import sys 
#return the result of an exam according to the result of three moduls
#consider teht modules can be weighted
#consider to manage courses with a dynamic number of modules

m1_grade = 18 
m2_grade = 20
m3_grade = 30 

m1_weight = 0.25
m2_weight = 0.25
m3_weight = 0.5 

grades =[18,20,30]
weights= [0.25, 0.25, 2.5]

#grade = (m1_grade + m2_grade +m3_grade)/ 3
#grade = (m1_weight*m1_grade + m2_weight*m2_grade +m3_weight*m3_grade)/ (m1_weight+m2_weight+m3_weight)
#iterate/loop over the grades/weights lists
sum_values =0
#for i, num in enumerate(grades):
 #   sum_values += num*weights[i] 
 

sum_modules = sum([a*b for a,b in zip[grades, weights]])
grade =sum_modules / sum(weights)

if grade >= 18 :
    print ("exam passed")
else :
    print ("exam failed ")
sys.exit()