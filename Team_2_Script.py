# -*- coding: utf-8 -*-
"""
Created on Mon May 31 17:05:58 2021
@author: rishabhkhorana 22768807
"""
###### question 1 ##########
# For automating the process of reading and writing the file  we havent used any libraries and just used in built_infunctions of python
#  We choose this method to show how the natural flow control of the program works. We shown how the loops and nested loops work 
### we have also used the string methods  to join the strings where necessary####
### at last we have written the cleaned data to a new file output data####
def file_reader(file):
    temp_container = []
    with open(file,'r') as file_data:
        data = file_data.read() ## this read the whole data a single string 
        for i in data.strip().split('\n'): ### the iterator splits the string on \n
            temp_container.append(i.split('\n')) # when adding data to the list it divided the data into list of list based on \n
    file_cutter(temp_container)      #calling the function file_cutter and giving the input values in temp_container
        
def file_cutter(file): # this fucntion cuts the file and gets the input from the file reader which is above#
    data_container =[] ## empty_lists###
    data_container_2 =[]
    for i in range(len(file)): #this is to access the rows
        for j in range(len(file[i])): ## this is to access the the values in rows 
            output = file[i][j].split(',')  ## we split the data on the delimiter ','
            data_container.append(output)  ### we add the data to this empty hence creating a 2d array
            
    for i in range(len(data_container)): ## this to handle the error in 2nd columns due to spliting at the delimiter at ','
        if (data_container[i][1].startswith('"') and data_container[i][1].endswith('"')): # if the string start with '" 'and end with '"' then it would allow the values 
            pass
        else:
            data_container[i][1] = data_container[i][1] + data_container[i][2] # if the above conditon fails then it join the string at index 1 and 2  for the value of rows
            
    for i in range(len(data_container)):  #again acessing the rows using i
        if len(data_container[i]) == 7:         # we checked the no of elements in each list of the list and if it is equal to 7 then it pass through the if block or it will go elif block
            output = data_container[i].pop(0)       
            output = data_container[i].pop(1)       #### here we are poping the index of each colmun in the list of list and as each colmun gets removed it shit to the left
            output = data_container[i].pop(1)
            output = data_container[i].pop(1)
            data_container_2.append(data_container[i])                       
            
        elif len(data_container[i]) >= 8 :              ### this block is accessed if the above condition fails
            #print(data_container[i])
            output = data_container[i].pop(0)
            output = data_container[i].pop(1)
            output = data_container[i].pop(1)
            output = data_container[i].pop(1)
            output = data_container[i].pop(1)
            data_container_2.append(data_container[i])            ### appending the the value in another list data_container 2
        else:
            pass
    file_writer(data_container_2)           ### this gives an input  and call the fucntion file writer 
    
def file_writer(file):
    with open ('output.txt','w') as f:
        for rows in file:
            output = ""
            for values in rows:
                output = output + (str(values) + ',')
            output = output[:-1]
            f.write(output)
            f.write('\n')
            
#file_reader('airports.csv')  ## here we call the fuction file reader which goes on top to start the sequence


### here  we are using libraries matlplot and pandas to create to read 
#the file create data frame and make different scatterplots.
def scatterplot(file):
    import pandas as pd ### importing all the modules from pandas library in pd 
    import matplotlib.pyplot as p #importing all the modules from pandas library in pd
    headers = ['airport','lat','long'] ## holding values in headers
    df  = pd.read_csv(file)
    df =df[(df['long'] < 0)] # fliteing the longitunal values which below zero
    df['lat']=df['lat'].map(lambda z: float(z)) ## converting strings to float values 
    df['long']=df['long'].map(lambda z: float(z)) ## converting strings to float values 
    x = df['lat'] ## storing the values of latitude in x -axis
    y = df['long'] ## storing the values of longitude in y -axis
    title =df['airport']
    #creating the first scatter plot on negative longitudnal values
    ### here we have used plot and scatter the difference between the both is scatter
    ### scatter is more precise than plot . where as in plot the any change in the attibutes would be applied to all the elements
    p.plot(y)## this creates plot y using x axis 0...n-1
     #x label
    p.ylabel('longitunal axis')
    p.show()
    #### creating a second plot between negative longitunal values with latitude
    p.plot(x,y)##
    p.xlabel("latitude axis")
    p.ylabel('longitunal axis')
    p.show()
    ### when we plot negative longitudnal values with in both axis we should get a linear relationship
    p.scatter(y,y)
    p.ylabel('longitunal axis')
    p.xlabel('longitunal axis')
    p.show()
    ### When plot the values if the x and y 
    p.scatter(x,y)
    p.xlabel('latitude axis')
    p.ylabel('longitunal axis')
    p.show()
    #### When interchanging the postion of x and y  where
    p.scatter(y,x)
    p.xlabel('longitunal axis')
    p.ylabel('latitude axis')
    p.show()
    
    
    

#scatterplot('output.csv')



#############################################################################
### Part B ###############################################################
# For this question we are using pandas and 
def file_reader_2(file,file2):
    import pandas as pd
    import numpy as np
    import matplotlib as m
    import matplotlib.pyplot as p
    df = pd.read_csv(file)
    df_file = pd.read_csv(file2)
    #print(df.head())
    
    #### putting values of each columns into variables using df['']
    ### creating a new columun for the data frame##
    airport_name =df['airport_name']
    df[['city','state']] = df.airport_name.str.split(',',expand=True,)
    state= df['state']
    df[['state','airport_name']] =df.state.str.split(':',expand=True,)
    
    
#### creating varibles for each column in the data frame.##
    scheduled_arrivals=df[' arr_flights']
    df =df[(df['arr_del15'].notnull())]
    delayed_flights = df['arr_del15']
    carrier_delay=df['carrier_ct']
    weather_delay =df['  weather_ct']
    nas_delay=df['nas_ct']
    security_delay=df['security_ct']
    late_aircraft_delay =df[' late_aircraft_ct']
    cancelled_flights=df['arr_cancelled']
    diverted_flights=df['arr_diverted']
    delayed_flights_minutes=df['arr_delay']
    carrier_delay_minutes=df['carrier_delay']
    weather_delay_minutes=df['weather_delay']
    nas_delay_minutes=df['nas_delay']
    security_delay_mintues=df['security_delay']
    late_aircraft_delay_mintues=df['late_aircraft_delay']
    airport_name = df['airport_name']
    state =df['state']
    city=df['city']
    
    ##########################################################
    #print(df_file['airport'][880],df_file['lat'][880],df_file['long'][880])
    ##########################################################
    df_file['lat']=df_file['lat'].map(lambda z: float(z))
    df_file['long']=df_file['long'].map(lambda z: float(z))
    
    
    # Question 1######################################################
    ##total number of operations####
    total_operations_flts = "{x} are the total number of flight operations".format(x = sum(scheduled_arrivals))    
    ##Question2######################################################
    ##total delayed time in minutes####
    total_delayed_flts = "{x} are the total number delayed flights".format(x= int(sum(delayed_flights)))
    ####Question3#####################################################
    ##total delayed time in mintues###
    total_delayed_time = "The total time for delayed flights is {x} minutes".format(x= sum(delayed_flights_minutes))
    ### Question4###############################################
    ##airport with maximum delayed flights ###
    max_val = delayed_flights.max()
    condition = delayed_flights == max_val
    airport_name_delay = np.select(condition,airport_name) 
    max_delay = "The airport with maximum delay is {x}".format(x= airport_name_delay)
   
   ### Question 5##################################################################
   ## coordinates for the highest delayed time###
    max_val_delayed_time =delayed_flights_minutes.max()
    condition_time = delayed_flights_minutes == max_val_delayed_time
    airport_delayed_max_time = np.select(condition_time,airport_name) 
    ### since we know the aiport with max time of delay is Hartsfield-Jackson Atlanta International
    airport_comparison =  df_file['airport'].str.contains('Hartsfield')
    airport_delayed_lat= np.select(airport_comparison,df_file['lat'])
    airport_delayed_long= np.select(airport_comparison,df_file['long'])    
    airport_coordinates = "{x} is the aiport with the highest delayed time with latitude {y} and longitutude {z}".format(x=airport_delayed_max_time, y=airport_delayed_lat,z=airport_delayed_long)

    ### Question 6########################################################
    airport_df = df[['state','airport_name','arr_del15']]
    airport_df_1 = airport_df[airport_df['state'] == ' TX']
    texas_airport_names = airport_df_1['airport_name']
    texas_delay_column = airport_df_1['arr_del15']
    max_delay_txs = texas_delay_column.max()
    condition_txs = texas_delay_column == max_delay_txs                    
    texas_airport_names_delayed_max_time = np.select(condition_txs,texas_airport_names)
    texas_airport = "Airport with largest number of  delayed flights in texas is{x}".format(x= texas_airport_names_delayed_max_time)
    
    ##### Question 7################################################
    ##caluting the total delay of the flight ###
    total_flight_operations = int(scheduled_arrivals.sum())
    total_carrier_delay = int(carrier_delay.sum())
    total_weather_delay = int(weather_delay.sum())
    total_nas_delay = int(nas_delay.sum())
    total_security_delay = int(security_delay.sum())
    total_late_aircraft_delay = int(late_aircraft_delay.sum())
    total_cancelled_flights = int(cancelled_flights.sum())
    total_diverted_flights = int(diverted_flights.sum())
    
    #### caluclting the total number of flights that were on time ####
    total_ontime_flights= total_flight_operations - total_carrier_delay- total_weather_delay - total_nas_delay - total_security_delay - total_late_aircraft_delay - total_cancelled_flights - total_diverted_flights
 
    
    y = np.array([total_ontime_flights,total_carrier_delay,total_weather_delay,total_nas_delay,
                  total_security_delay,total_late_aircraft_delay,total_cancelled_flights,total_diverted_flights])
    mylabels = ['Ontime_flights','Carrier_delay','Weather_delay','Nas_delay',
                'security_delay','late_aircraft_delay','Cancelled_flights','Diverted_flights']
    fig = p.figure(2, figsize=(8,8))
    ax = fig.add_subplot(111)
    ax.axis('equal')
    colors=('b', 'g', 'r', 'c', 'm', 'y', 'burlywood', 'w')
    ax.pie(y,colors=colors ,labels=mylabels, autopct='%1.1f%%')
    p.show()
    
    Q1 = total_operations_flts
    Q2 = total_delayed_flts
    Q3 = total_delayed_time
    Q4 =  max_delay
    Q5 = airport_coordinates
    Q6 = texas_airport
    return Q1,Q2,Q3,Q4,Q5,Q6  



#file_reader_2('airline_delay_causes_feb2020.csv','output.csv')



