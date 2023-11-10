values = [0, 20, 40, 60, 80, 100, 120]
Progress = 0
Trailer = 0
Retriever = 0
Excluded = 0
outcome_dict = {}

count = 1
while True:
#get student id
    student_id = input("Enter unique Student ID :")
    if student_id not in outcome_dict:
        outcome_dict[student_id]=[]
    else:
        continue
    try:
#check, if input credits are in different data types
        Pass = int(input('Please enter your credits at pass :'))
        if Pass not in values:
            print("out of range")
        else:
            Defer = int(input('Please enter your credits at Defer :'))
            if Defer not in values:
                print("out of range")
            else:
                Fail = int(input('Please enter your credits at Fail :'))
                if Fail not in values:
                    print("out of range")
                else:
                    total = (Pass + Defer + Fail)
                    if total != 120:
                        print("Total incorrect")


    except ValueError:
#if entered different data types' values print "Integer required"
        print("Integer required")

    else:
        credit = [Pass, Defer, Fail]
        if Fail >= 80:
            print('Exclude')
            Excluded += 1
            outcome_dict[student_id].append(('Exclude', credit))
        elif Pass == 120:
            print('Progress')
            Progress += 1
            outcome_dict[student_id].append(('Progress', credit))
        elif Pass == 100:
            print('Progress module trailer')
            Trailer += 1
            outcome_dict[student_id].append(('Progress Module trailer', credit))
        else:
            print('Do not progress - module retriver')
            Retriever += 1
            outcome_dict[student_id].append(('Module retriver', credit))

        print("\nWould You like to enter another set of data?")
        data = input("Enter 'y' for yes or 'q' to quit and view resualts :")
        if data == "q":
            print("\n------------------------------------------------")
            print("Histrogram\nProgress ", Progress, "\t: ", '*' * Progress, "\nTrailer ", Trailer, "\t: ",
                  '*' * Trailer, "\nRetriever ", Retriever, "\t: ", '*' * Retriever, "\nExcluded ", Excluded, "\t: ",
                  '*' * Excluded, "\n")
            print(count, " outcomes in total.")
            print("------------------------------------------------")
            for student_id, data_list in outcome_dict.items():
                print(f"{student_id}:",end="")
                for outcome, credit in data_list:
                    print(f"\t{outcome}: {credit}")

            break

        elif data == "y":
            print("\n")
            count += 1
            continue






