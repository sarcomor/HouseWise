import csv
#============================================================
price={}
size={}
ticket={}
ticket_count=0
#======================
with  open('data.csv',newline='')as file:
    reader=csv.reader(file)
    for i in reader: 
        price[int(i[2])]=int(i[0])
        size[int(i[2])]=int(i[1])
        ticket[int(i[2])]=int(i[2])
        ticket_count=int(i[2])
#============================================================
def house_wise():
    sort_price={}
    sort_size={}
    input_request=input('DO You have any request? yes or no  \n')
    if input_request=='yes':
        input_add_list_delete_deleteAll=input('add - list - delete - delete all  \n')
        #============================================================ add
        if input_add_list_delete_deleteAll=='add':
            global ticket_count
            ticket_count+=1
            intput_price_int=int(input('enter the price  \n'))
            input_size_int=int(input('enter the size  \n'))
            with  open('data.csv','a',newline='')as file:
                writer=csv.writer(file)
                writer.writerow([intput_price_int,input_size_int,ticket_count])
            house_wise()
            #==================================================================== delet
        if input_add_list_delete_deleteAll=='delete':
                    #======
            with  open('data.csv',newline='')as file:
                reader=csv.reader(file)
                for i in reader: 
                    price[int(i[2])]=int(i[0])
                    size[int(i[2])]=int(i[1])
                    ticket[int(i[2])]=int(i[2])
                    ticket_count=int(i[2])
                    #======
            input_get_ticket_number=input('enter the ticket number  \n')
            if not int(input_get_ticket_number) in ticket:
                print('the ticket number isn\'t exist')
                if int(input_get_ticket_number) in ticket:
                    del price[int(input_get_ticket_number)]
                    del size[int(input_get_ticket_number)]
                    del ticket[int(input_get_ticket_number)]           
                    print('removed ',input_get_ticket_number)
                    with  open('data.csv','w',newline='')as file:
                        writer=csv.writer(file)
                        for i,(get_price_values,get_size_values,get_ticket_values) in enumerate(zip(price.values(),size.values(),ticket.values())):
                            writer.writerow([get_price_values,get_size_values,get_ticket_values])
                house_wise()
            elif int(input_get_ticket_number) in ticket:
                del price[int(input_get_ticket_number)]
                del size[int(input_get_ticket_number)]
                del ticket[int(input_get_ticket_number)]
                print('removed ',input_get_ticket_number)
                with  open('data.csv','w',newline='')as file:
                    writer=csv.writer(file)
                    for i,(get_price_values,get_size_values,get_ticket_values) in enumerate(zip(price.values(),size.values(),ticket.values())):
                        writer.writerow([get_price_values,get_size_values,get_ticket_values])
                house_wise()
            #============================================================
        if input_add_list_delete_deleteAll=='delete all':
                    #======
            with  open('data.csv',newline='')as file:
                reader=csv.reader(file)
                for i in reader: 
                    price[int(i[2])]=int(i[0])
                    size[int(i[2])]=int(i[1])
                    ticket[int(i[2])]=int(i[2])
                    ticket_count=int(i[2])
                    #======
            price.clear()
            size.clear()
            ticket.clear()
            ticket_count=0
            print('the banck is clear ')
            with  open('data.csv','w',newline='')as file:
                writer=csv.writer(file)
                for i,(get_price_values,get_size_values,get_ticket_values) in enumerate(zip(price.values(),size.values(),ticket.values())):
                    writer.writerow([get_price_values,get_size_values,get_ticket_values])
            house_wise()
            #============================================================
        if input_add_list_delete_deleteAll=='list':
                    #======
            with  open('data.csv',newline='')as file:
                reader=csv.reader(file)
                for i in reader: 
                    price[int(i[2])]=int(i[0])
                    size[int(i[2])]=int(i[1])
                    ticket[int(i[2])]=int(i[2])
                    ticket_count=int(i[2])
                    #======
            input_sort_by_date_price_size_range=input('sort by: date - price - size - range  \n')
            int_number=0
                #===================== sort by date
            if input_sort_by_date_price_size_range=='date':
                for i in ticket:
                    int_number+=1
                    print(int_number,': home,',price[i],', ',size[i],'   ticket number:',i)
                if ticket=={}:
                    print('there\'s no any')
                #===================== sort by price
            elif input_sort_by_date_price_size_range=='price':
                sort_price=dict(sorted((price.items()),key=lambda x: x[1]))
                for i in sort_price:
                    int_number+=1
                    print(int_number,': home,',price[i],', ',size[i],'   ticket number:',i)
                if sort_price=={}:
                    print('there\'s no any')
                #===================== sort by size
            elif input_sort_by_date_price_size_range=='size':
                sort_size=dict(sorted((size.items()),key=lambda x: x[1]))
                for i in sort_size:
                    int_number+=1
                    print(int_number,': home,',price[i],', ',size[i],'   ticket number:',i)
                if sort_size=={}:
                    print('there\'s no any')
                #===================== sort by range
            elif input_sort_by_date_price_size_range=='range':
                input_Price_range_Size_range=input('sort by:  price range - size range  \n')
                #============================================================
                if input_Price_range_Size_range=='price range':
                    input_starting_price_int=int(input('starting price  \n'))
                    input_ending_price_int=int(input('OK! ending price  \n'))
                    get_existing_ticket_in_range_price={i for i in price if price[i] in range(input_starting_price_int,input_ending_price_int)}
                    for i in get_existing_ticket_in_range_price:
                        sort_price[i]=price[i]
                    sort_price=dict(sorted((sort_price.items()),key=lambda x: x[1]))
                    for i in sort_price:
                        int_number+=1
                        print(int_number,': home,',price[i],', ',size[i],'   ticket number:',i)
                    if sort_price=={}:
                        print('there\'s no any')
                    #============================================================
                if input_Price_range_Size_range=='size range':
                    input_starting_price_int=int(input('starting size  \n'))
                    input_ending_price_int=int(input('OK! ending size  \n'))
                    get_existing_ticket_in_range_size={i for i in size if size[i] in range(input_starting_price_int,input_ending_price_int)}
                    for i in get_existing_ticket_in_range_size:
                        sort_size[i]=size[i]
                    sort_size=dict(sorted((sort_size.items()),key=lambda x: x[1]))
                    for i in sort_size:
                        int_number+=1
                        print(int_number,': home,',price[i],', ',size[i],'   ticket number:',i)
                    if sort_size=={}:
                        print('there\'s no any')
            house_wise()
house_wise()
