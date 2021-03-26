#!/usr/bin/env python
# coding: utf-8

# In[85]:


import csv
import os


# In[86]:


data_set = []


# In[87]:


with open(r'C:\Users\Ramin\Desktop\Neuer Ordner (8)\python-portfolio-project-starter-files\insurance.csv', newline='') as insurance:
    user_data = csv.DictReader(insurance)
    for row in user_data:
        data_set.append(row)
    
    


# In[88]:


#print(data_set)


# In[89]:


ages = []
for i in data_set:
    ages.append(int(i['age']))


# In[90]:


def average_age(age_list):
    age_counter = 0
    for age in age_list:
        age_counter += age
        average = age_counter / len(age_list)
    return average


# In[91]:


average_age = average_age(ages)
print(average_age)


# In[92]:


print("The average age of all insuranced person is {years} years old.".format(years=round(average_age)))


# In[93]:


charges_smoker = []
charges_nonsmoker = []
for data in data_set:
    if data['smoker'] == 'yes':
        charges_smoker.append(float(data['charges']))
    elif data['smoker'] == 'no':
        charges_nonsmoker.append(float(data['charges']))


# In[94]:


def average_costs_smoker(listt):
    costs = 0
    for cost in listt:
        costs = costs + cost
    length = len(listt)
    average = costs / length
    return average


# In[95]:


smoker = average_costs_smoker(charges_smoker)
non_smoker = average_costs_smoker(charges_nonsmoker)
difference = smoker - non_smoker
print("On average, smoker pay {cost1} for their insurance while non-smoker pay {cost2} for their insurance. This means that smoker pay {diff} more than non-smoker on average.".format(cost1=round(smoker,2),cost2=round(non_smoker,2), diff=round(difference,2)))


# In[96]:


counter_male = 0
counter_female = 0
for data in data_set:
    if data['sex'] == 'male':
        counter_male += 1
    elif data['sex'] == 'female':
        counter_female += 1


# In[97]:


print(counter_male)
print(counter_female)
def procentual_sex_contribution(male,female):
    if counter_male > counter_female:
        difference = counter_male - counter_female
        percent = (difference / counter_female)*100
        print("The data set contains {percent} % more male than female persons".format(percent=round(percent)))
    elif counter_male < counter_female:
        difference = counter_female - counter_male
        percent = (difference / counter_male) * 100
        print("The data set contains {percent} % more female than male persons".format(percent=round(percent)))
    return percent

print(procentual_sex_contribution(counter_male, counter_female))


# In[100]:


regions = {'northeast':0, 'northwest':0, 'southwest':0, 'southeast':0}
for data in data_set:
    if data['region'] == 'northeast':
        regions['northeast'] += 1
    elif data['region'] =='northwest':
        regions['northwest'] += 1
    elif data['region'] == 'southwest':
        regions['southwest'] += 1
    elif data['region'] == 'southeast':
        regions['southeast'] += 1


# In[104]:


for key,value in regions.items():
    print("{key} : {value} persons registered".format(key = key, value = value))


# In[106]:


bmi_40_to_65 = []
bmi_30_to_39 = []
bmi_18_to_29 = []
for data in data_set:
    if int(data['age']) < 30:
        bmi_18_to_29.append(float(data['bmi']))
    elif int(data['age']) < 40 and int(data['age']) > 29 :
        bmi_30_to_39.append(float(data['bmi']))
    elif int(data['age']) > 39:
        bmi_40_to_65.append(float(data['bmi']))   


# In[111]:


def average_bmi(bmi_list):
    bmi_total = 0
    for bmi in bmi_list:
        bmi_total += bmi
    average = bmi_total / len(bmi_list)
    return average


# In[122]:


average_40_to_65 = average_bmi(bmi_40_to_65)
average_30_to_39 = average_bmi(bmi_30_to_39)
average_18_to_29 = average_bmi(bmi_18_to_29)
print("The average bmi for people between the age of 18-29 is : {avg1}.".format(avg1 =(average_18_to_29 )))
print("The average bmi for people between the age of 30-39 is : {avg1}.".format(avg1 =(average_30_to_39 )))
print("The average bmi for people between the age of 40-65 is : {avg1}.".format(avg1 =(average_40_to_65 )))


# In[ ]:




