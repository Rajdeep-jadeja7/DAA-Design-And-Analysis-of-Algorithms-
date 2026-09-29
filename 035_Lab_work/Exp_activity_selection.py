#Using the zip function

def activity_selection(start,finish):
    n=len(start)
    activities=sorted(zip(start,finish,range(n)),key=lambda x:x[1])
    finish_time=-1
    selected_activities=[]
    for s,f,id in activities:
        if s>=finish_time:
            finish_time=f
            selected_activities.append(id)
    print("Selected Activities:",selected_activities)        

start=[1,3,5,2,7,6]
finish=[5,6,8,4,9,8]
activity_selection(start,finish) 

#Taking all the values in tuple format and without zip function approach
"""
def Activity_selection(activity_list): 

    activity_list.sort(key=lambda x:x[2])
    activity_selected=[]
    End_time=0
    for i in activity_list:
        act_id=i[0]
        St=i[1]
        Et=i[2]

        if St>=End_time:
            activity_selected.append(act_id)
            End_time=Et

    print("Activities Selected:",activity_selected)        
    
activity_list=[("A1",10,5),("A2",2,6),("A3",2,4),("A4",4,7),("A5",5,8)]
Activity_selection(activity_list)    
""" 
           