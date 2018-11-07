def append_tts(x_train, x_test, y_train, y_test, descr, t_sets):
    val = len(t_sets)
    li=[]
    li.append(descr)
    li.append(x_train)
    li.append(y_train)
    li.append(x_test)
    li.append(y_test)
    t_sets.append(li)

    return (val)

def make_tsets_keylist(list_Xs, y, t_size, t_set_list, name_list):
    for list_X in listXs:
        a,b,c,d = train_test_split(list_X, medv_y, test_size=t_size, random_state=17)
        val = append_tts(a,b,c,d, 'medv:  ', medv_t_sets)
        name_list.append(val)