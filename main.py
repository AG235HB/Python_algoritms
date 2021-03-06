def show_help():
    print "Usage:"
    print "\tmain.py [-h]|[[-st <type of sort> <sequence>]|"
    print "\t\t[-sh <type of search> <sequence> -o <searchable object>]]"
    print "Parameters:"
    print "\t-h\tShow help."
    print "\t-st\tSorting of sequence of numbers. It is necessary"
    print "\t\tto specify sorting type."
    print "\t\tSequence numbers can be partitioned by spaces or ',';"
    print "\t\tif the sequence is not specified, 10 random numbers"
    print "\t\twill be generated."
    print "\t-sh\tNumber search in sequence of numbers. It is necessary"
    print "\t\tto specify search type."
    print "\t\tSequence numbers can be partitioned by spaces or ',';"
    print "\t\tif the sequence is not specified, 10 random numbers"
    print "\t\twill be generated."
    print "Types of sort:"
    print "\t-b\tBubble sort."
    print "\t-i\tInsertion sort."
    print "\t-m\tMerge sort."
    print "\t-q\tQuick sort."
    print "\t-s\tSelection sort."
    print "Types of search:"
    print "\t-bst\tBinary search tree."
    print "\t-bin\tBinary search."
    print "\t\tNOTE: The address only the first found number will be shown."
    print "\t-lin\tLinear search."

def mode_selector():
    if len(sys.argv) >= 2:
        if sys.argv[1] == '-h':
            print("Help:")
        elif sys.argv[1] == '-st':
            if len(sys.argv) >= 3:
                if sys.argv[2] == '-b':
                    from sort import bubble
                    if len(sys.argv) == 3:
                        from auxiliary import randomizer
                        collection = list(randomizer.create_collection(10, 0, 25))
                        print "initial collection:\t" + str(collection)
                        print "result collection:\t" + str(bubble.sort(collection))
                    elif len(sys.argv) == 4 and len(sys.argv[3]) > 3:
                        from auxiliary import text_formater
                        st = str(sys.argv[3])
                        collection = [int(item) for item in st.split(text_formater.find_separator(st))]
                        print "initial collection:\t"+ str(collection)
                        print "result collection:\t" + str(bubble.sort(collection))
                    else:
                        st = [int(item) for item in sys.argv[3:]]
                        print "initial collection:\t"+ str(st)
                        print "result collection:\t"+str(bubble.sort(sys.argv[3:]))
                elif sys.argv[2] == '-i':
                    from sort import insertion
                    if len(sys.argv) == 3:
                        from auxiliary import randomizer
                        collection = list(randomizer.create_collection(10, 0, 25))
                        print "initial collection:\t" + str(collection)
                        print "result collection:\t" + str(insertion.sort(collection))
                    elif len(sys.argv) == 4 and len(sys.argv[3]) > 3:
                        from auxiliary import text_formater
                        st = str(sys.argv[3])
                        collection = [int(item) for item in st.split(text_formater.find_separator(st))]
                        print "initial collection:\t" + str(collection)
                        print "result collection:\t" + str(insertion.sort(collection))
                    else:
                        st = [int(item) for item in sys.argv[3:]]
                        print "initial collection:\t" + str(st)
                        print "result collection:\t" + str(insertion.sort(sys.argv[3:]))
                elif sys.argv[2] == '-m':
                    from sort import merge
                    if len(sys.argv) == 3:
                        from auxiliary import randomizer
                        collection = list(randomizer.create_collection(10, 0, 25))
                        print "initial collection:\t"+ str(collection)
                        print "result collection:\t" + str(merge.sort(collection))
                    elif len(sys.argv) == 4 and len(sys.argv[3]) > 3:
                        from auxiliary import text_formater
                        st = str(sys.argv[3])
                        collection = [int(item) for item in st.split(text_formater.find_separator(st))]
                        print "initial collection:\t"+ str(collection)
                        print "result collection:\t" + str(merge.sort(collection))
                    else:
                        st = [int(item) for item in sys.argv[3:]]
                        print "initial collection:\t"+ str(st)
                        print "result collection:\t"+str(merge.sort(sys.argv[3:]))
                elif sys.argv[2] == '-q':
                    from sort import quick
                    if len(sys.argv) == 3:
                        from auxiliary import randomizer
                        collection = list(randomizer.create_collection(10, 0, 25))
                        print "initial collection:\t"+ str(collection)
                        print "result collection:\t" + str(quick.sort(collection))
                    elif len(sys.argv) == 4 and len(sys.argv[3]) > 3:
                        from auxiliary import text_formater
                        st = str(sys.argv[3])
                        collection = [int(item) for item in st.split(text_formater.find_separator(st))]
                        print "initial collection:\t"+ str(collection)
                        print "result collection:\t" + str(quick.sort(collection))
                    else:
                        st = [int(item) for item in sys.argv[3:]]
                        print "initial collection:\t"+ str(st)
                        print "result collection:\t"+str(quick.sort(sys.argv[3:]))
                elif sys.argv[2] == '-s':
                    from sort import selection
                    if len(sys.argv) == 3:
                        from auxiliary import randomizer
                        collection = list(randomizer.create_collection(10, 0, 25))
                        print "initial collection:\t"+ str(collection)
                        print "result collection:\t" + str(selection.sort(collection))
                    elif len(sys.argv) == 4 and len(sys.argv[3]) > 3:
                        from auxiliary import text_formater
                        st = str(sys.argv[3])
                        collection = [int(item) for item in st.split(text_formater.find_separator(st))]
                        print "initial collection:\t"+ str(collection)
                        print "result collection:\t" + str(selection.sort(collection))
                    else:
                        st = [int(item) for item in sys.argv[3:]]
                        print "initial collection:\t"+ str(st)
                        print "result collection:\t"+str(selection.sort(sys.argv[3:]))
                else:
                    show_help()
            else:
                show_help()
        elif sys.argv[1] == '-sh':
            if len(sys.argv) >= 3:
                if sys.argv[2] == '-bst':
                    if sys.argv[len(sys.argv)-2] == "-o":
                        if len(sys.argv) is 5:
                            #RANDOM
                            from auxiliary import randomizer
                            collection = list(randomizer.create_collection(10, 0, 10))
                            from search import binary_tree
                            bst = binary_tree.BinaryTree()
                            for i in range(0, 10, 1):
                                bst.add(collection[i])
                            print "initial collection:\t"+ str(collection)
                            print "searchable object:\t" + str(sys.argv[4])
                            print bst.search(int(sys.argv[4]))
                        elif len(sys.argv) == 6 and len(sys.argv[3]) > 3:
                            #MANUAL
                            from auxiliary import text_formater
                            st = str(sys.argv[3])
                            collection = [int(item) for item in st.split(text_formater.find_separator(st))]
                            from search import binary_tree
                            bst = binary_tree.BinaryTree()
                            for i in range(0, len(collection), 1):
                                bst.add(collection[i])
                            print "initial collection:\t"+ str(collection)
                            print "searchable object:\t" + str(sys.argv[len(sys.argv)-1])
                            print bst.search(int(sys.argv[len(sys.argv)-1]))
                        else:
                            #MANUAL
                            st = [int(item) for item in sys.argv[3:len(sys.argv)-2]]
                            from search import binary_tree
                            bst = binary_tree.BinaryTree()
                            for i in range(0, len(st), 1):
                                bst.add(st[i])
                            print "initial collection:\t"+ str(st)
                            print "searchable object:\t" + str(sys.argv[len(sys.argv)-1])
                            print bst.search(int(sys.argv[len(sys.argv)-1]))
                    else:
                        show_help()
                elif sys.argv[2] == '-bin':
                    if sys.argv[len(sys.argv)-2] == "-o":
                        if len(sys.argv) is 5:
                            #RANDOM
                            from auxiliary import randomizer
                            collection = list(randomizer.create_collection(10, 0, 10))
                            from search import binary
                            print "initial collection:\t"+ str(collection)
                            print "searchable object:\t" + str(sys.argv[4])
                            #collection.append(int(sys.argv[4]))
                            print "searchable object position:" + str(binary.search(int(sys.argv[4]), collection))
                        elif len(sys.argv) == 6 and len(sys.argv[3]) > 3:
                            #MANUAL
                            from auxiliary import text_formater
                            st = str(sys.argv[3])
                            collection = [int(item) for item in st.split(text_formater.find_separator(st))]
                            from search import binary
                            print "initial collection:\t"+ str(collection)
                            print "searchable object:\t" + str(sys.argv[len(sys.argv)-1])
                            print "searchable object position:" + str(binary.search(int(sys.argv[len(sys.argv)-1]), collection))
                        else:
                            #MANUAL
                            st = [int(item) for item in sys.argv[3:len(sys.argv)-2]]
                            from search import binary
                            print "initial collection:\t"+ str(st)
                            print "searchable object:\t" + str(sys.argv[len(sys.argv)-1])
                            print "searchable object position:" + str(binary.search(int(sys.argv[len(sys.argv)-1]), st))
                    else:
                        show_help()
                elif sys.argv[2] == '-lin':
                    if sys.argv[len(sys.argv)-2] == "-o":
                        if len(sys.argv) is 5:
                            #RANDOM
                            from auxiliary import randomizer
                            collection = list(randomizer.create_collection(10, 0, 10))
                            from search import linear
                            print "initial collection:\t"+ str(collection)
                            print "searchable object:\t" + str(sys.argv[4])
                            #collection.append(int(sys.argv[4]))
                            print "searchable object position:" + str(linear.search(int(sys.argv[4]), collection))
                        elif len(sys.argv) == 6 and len(sys.argv[3]) > 3:
                            #MANUAL
                            from auxiliary import text_formater
                            st = str(sys.argv[3])
                            collection = [int(item) for item in st.split(text_formater.find_separator(st))]
                            from search import linear
                            print "initial collection:\t"+ str(collection)
                            print "searchable object:\t" + str(sys.argv[len(sys.argv)-1])
                            print "searchable object position:" + str(linear.search(int(sys.argv[len(sys.argv)-1]), collection))
                        else:
                            #MANUAL
                            st = [int(item) for item in sys.argv[3:len(sys.argv)-2]]
                            from search import linear
                            print "initial collection:\t"+ str(st)
                            print "searchable object:\t" + str(sys.argv[len(sys.argv)-1])
                            print "searchable object position:" + str(linear.search(int(sys.argv[len(sys.argv)-1]), st))
                    else:
                        show_help()
            else:
                show_help()
        elif sys.argv[1] == '-joke':
            import os
            try:
                os.system('cls')
            except:
                os.system('clear')
            print "The classic mistake inventors absolutely reliable systems -"
            print "this underestimation of the ingenuity of clinical idiots.\n\nDouglas Adams."
        else:
            show_help()
    else:
        show_help()

def find_separator(collection):
    for index, item in enumerate(collection):
        if item == ',':
            return ','
        if item == ' ':
            return ' '
    return None

if __name__ == '__main__':
    import sys
    if sys.version_info.major < 3:
        input_func = raw_input
    else:
        input_func = input

    mode_selector()
    