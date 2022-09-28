import os
import ged_lib as gl

class persons_class(object):
    def __init__(self, individual_id=None, name=None, birth_year=None, more=None, link=None):
        self.individual_id = individual_id
        self.name = name
        self.birth_year = birth_year
        self.more = more
        self.link = link

def create_tree():
#    print("\nCreating tree")
    gl.get_params()

    gl.read_individuals()
    gl.read_families()
    
    suppress = "Y"

    if gl.person1 != "": write_tree_page (gl.person1, 1, suppress)
    if gl.person2 != "": write_tree_page (gl.person2, 1, suppress)
    if gl.person3 != "": write_tree_page (gl.person3, 1, suppress)
    if gl.person4 != "": write_tree_page (gl.person4, 1, suppress)

def write_tree_page(id, level, suppress):
    font_style = "style=font-family:\"consolas\";font-weight:bold;"

    persons = []

    add_person(persons,  1,  0, "", id)    # person 1
    add_person(persons,  2,  1, "F", 0)    # person 2  - father of person 1
    add_person(persons,  3,  2, "F", 0)    # person 3  - father of person 2
    add_person(persons,  4,  3, "F", 0)    # person 4  - father of person 3
    add_person(persons,  5,  3, "M", 0)    # person 5  - mother of person 3
    add_person(persons,  6,  2, "M", 0)    # person 6  - mother of person 2
    add_person(persons,  7,  6, "F", 0)    # person 7  - father of person 6
    add_person(persons,  8,  6, "M", 0)    # person 8  - mother of person 6
    add_person(persons,  9,  1, "M", 0)    # person 9  - mother of person 1
    add_person(persons, 10,  9, "F", 0)    # person 10 - father of person 9
    add_person(persons, 11, 10, "F", 0)    # person 11 - father of person 10
    add_person(persons, 12, 10, "M", 0)    # person 12 - mother of person 10
    add_person(persons, 13,  9, "M", 0)    # person 13 - mother of person 9
    add_person(persons, 14, 13, "F", 0)    # person 14 - father of person 13
    add_person(persons, 15, 13, "M", 0)    # person 15 - mother of person 13

    if level == 1 and suppress == "Y":
        persons[1].name = persons[1].name[0:persons[1].name.find(",")]
        persons[1].birth_year = ""
        persons[1].link = False

    file_name_html = gl.website_path + "/Tree" + str(level) + " " + clean_file_path(persons[1].name) + ".html"
#    print(file_name_html)
    hfile = open(file_name_html,"w")

    hfile.write ("<!DOCTYPE html PUBLIC \"-//W3C//DTD HTML 4.01//EN\" \"http://www.w3.org/TR/html4/strict.dtd\">\n")
    hfile.write("<html>\n")
    hfile.write("<head>\n")
    hfile.write("<meta content=\"text/html; charset=ISO-8859-1\" http-equiv=\"content-type\">\n")
    hfile.write("<title>" + persons[1].name + "</title>\n")
    hfile.write("</head>\n")
    hfile.write("<body " + font_style + ">\n")
    hfile.write("<br>\n")
    hfile.write("<br>\n")
    
    write_spaces(hfile, 55)
    write_long_branch_up(hfile)
    
    write_person(hfile, persons[4].name, persons[4].birth_year, persons[4].more, persons[4].link, level)
    
    hfile.write("<br>")
    write_spaces(hfile, 32)
    write_long_branch_up(hfile)
    write_person(hfile, persons[3].name, persons[3].birth_year, False, persons[3].link, level)
    
    write_spaces(hfile, 32)
    write_vertical_line(hfile)
    hfile.write("<br>")
    write_spaces(hfile, 55)
    write_long_branch_down(hfile)
    write_person(hfile, persons[5].name, persons[5].birth_year, persons[5].more, persons[5].link, level)
    
    write_spaces(hfile, 16)
    write_short_branch_up(hfile)
    write_person(hfile, persons[2].name, persons[2].birth_year, False, persons[2].link, level)
    
    write_spaces(hfile, 16)
    write_vertical_line(hfile)
    write_spaces(hfile, 37)
    write_long_branch_up(hfile)
    write_person(hfile, persons[7].name, persons[7].birth_year, persons[7].more, persons[7].link, level)
    
    write_spaces(hfile, 16)
    write_vertical_line(hfile)
    write_spaces(hfile, 14)
    write_vertical_line(hfile)
    hfile.write("<br>")
    write_spaces(hfile, 16)
    write_vertical_line(hfile)
    write_spaces(hfile, 14)
    write_long_branch_down(hfile)
    write_person(hfile, persons[6].name, persons[6].birth_year, False, persons[6].link, level)
    
    write_spaces(hfile, 16)
    write_vertical_line(hfile)
    hfile.write("<br>")
    write_spaces(hfile, 55)
    write_long_branch_down(hfile)
    write_person(hfile, persons[8].name, persons[8].birth_year, persons[8].more, persons[8].link, level)
    
    write_spaces(hfile, 13)
    write_person(hfile, persons[1].name, persons[1].birth_year, False, persons[1].link, level)
    
    write_spaces(hfile, 55)
    write_long_branch_up(hfile)
    write_person(hfile, persons[11].name, persons[11].birth_year, persons[11].more, persons[11].link, level)
    
    write_spaces(hfile, 16)
    write_vertical_line(hfile)
    hfile.write("<br>")
    write_spaces(hfile, 16)
    write_vertical_line(hfile)
    write_spaces(hfile, 14)
    write_long_branch_up(hfile)
    write_person(hfile, persons[10].name, persons[10].birth_year, False, persons[10].link, level)
    
    write_spaces(hfile, 16)
    write_vertical_line(hfile)
    write_spaces(hfile, 14)
    write_vertical_line(hfile)
    hfile.write("<br>")
    write_spaces(hfile, 16)
    write_vertical_line(hfile)
    write_spaces(hfile, 37)
    write_long_branch_down(hfile)
    write_person(hfile, persons[12].name, persons[12].birth_year, persons[12].more, persons[12].link, level)
    
    write_spaces(hfile, 16)
    write_short_branch_down(hfile)
    write_person(hfile, persons[9].name, persons[9].birth_year, False, persons[9].link, level)
    
    write_spaces(hfile, 55)
    write_long_branch_up(hfile)
    write_person(hfile, persons[14].name, persons[14].birth_year, persons[14].more, persons[14].link, level)
    
    write_spaces(hfile, 32)
    write_vertical_line(hfile)
    hfile.write("<br>")
    write_spaces(hfile, 32)
    write_long_branch_down(hfile)
    write_person(hfile, persons[13].name, persons[13].birth_year, False, persons[13].link, level)
    
    hfile.write("<br>")
    write_spaces(hfile, 55)
    write_long_branch_down(hfile)
    write_person(hfile, persons[15].name, persons[15].birth_year, persons[15].more, persons[15].link, level)
    
    n1 = gl.get_person_name(gl.person1)
    n1 = n1[0:n1.find(",")]
    n2 = gl.get_person_name(gl.person2)
    n2 = n2[0:n2.find(",")]
    n3 = gl.get_person_name(gl.person3)
    n3 = n3[0:n3.find(",")]
    n4 = gl.get_person_name(gl.person4)
    n4 = n4[0:n4.find(",")]
    
    hfile.write("<br>")
    hfile.write("<br>")
    write_spaces(hfile, 40)
    hfile.write("<a href=\"Tree1 " + clean_file_path(n1) + ".html\">" + n1 + "</a>\n")
    write_spaces(hfile, 4)
    hfile.write("<a href=\"Tree1 " + clean_file_path(n2) + ".html\">" + n2 + "</a>\n")
    write_spaces(hfile, 4)
    hfile.write("<a href=\"Tree1 " + clean_file_path(n3) + ".html\">" + n3 + "</a>\n")
    write_spaces(hfile, 4)
    hfile.write("<a href=\"Tree1 " + clean_file_path(n4) + ".html\">" + n4 + "</a>\n")
    hfile.write("<br>")
    hfile.write("</body>")
    hfile.write("</html>")
    
    hfile.close()
    
    if persons[4].individual_id != 0 and persons[4].more: write_tree_page(persons[4].individual_id, level + 3, "N")
    if persons[5].individual_id != 0 and persons[5].more: write_tree_page(persons[5].individual_id, level + 3, "N")
    if persons[7].individual_id != 0 and persons[7].more: write_tree_page(persons[7].individual_id, level + 3, "N")
    if persons[8].individual_id != 0 and persons[8].more: write_tree_page(persons[8].individual_id, level + 3, "N")
    if persons[11].individual_id != 0 and persons[11].more: write_tree_page(persons[11].individual_id, level + 3, "N")
    if persons[12].individual_id != 0 and persons[12].more: write_tree_page(persons[12].individual_id, level + 3, "N")
    if persons[14].individual_id != 0 and persons[14].more: write_tree_page(persons[14].individual_id, level + 3, "N")
    if persons[15].individual_id != 0 and persons[15].more: write_tree_page(persons[15].individual_id, level + 3, "N")

def add_person (persons, n, child, parent_type, individual_id):
#    print ("add_person", n, child, parent_type, individual_id)
    current_id = 0
    name = ""
    birth_year = ""
    more = False
    link = False
    if n == 1:
        # if current person is the top-level person on page, add dummy record to persons list
        # and set current id to id passed as a parameter
        persons.append (persons_class(0, "", "", False, False))
        current_id = individual_id
    else:
        # otherwise set current id to parent of the id in the child person record
        if parent_type == "F":
            # if father, get the child's father's id
            if persons[child].individual_id != 0: current_id = gl.get_father_id(persons[child].individual_id)
        else:
            # if mother, get the child's mother's id
            if persons[child].individual_id != 0: current_id = gl.get_mother_id(persons[child].individual_id)
        
    if current_id != 0:
        # get the current individual's name and birth date
        name = gl.get_person_name(current_id)
        birth_year = gl.get_birth_year(current_id)
        # if the current person has a parent, set 'more' flag to True
        if gl.get_father_id(current_id) != "" or gl.get_mother_id(current_id) != "": more = True
        # if the person has an associated list of documents
        if document_list_exists(name, birth_year): link = True

    persons.append (persons_class(current_id, name, birth_year, more, link))

def write_spaces(hfile, n):
    i = 0
    s = ""
    while True:
        i = i + 1
        if i > n: break
        s = s + "&nbsp;"
    hfile.write(s + "\n")

def write_person(hfile, person, birth_year, more, link, level):

    if link:
        hfile.write("<a href=\"List " + clean_file_path(person + " " + birth_year) + ".html\">" + person + " " + birth_year + "</a>\n")
    else:
        hfile.write(person + " " + birth_year + "\n")

    if more:
        write_spaces_before_more (hfile, person, birth_year)
        next_tree_level = str(level + 3)
        hfile.write("<a href=\"Tree" + next_tree_level + " " + clean_file_path(person) + ".html\">&gt;</a>\n")
    
    hfile.write("<br>\n")

def document_list_exists(n, bd):
    file = gl.website_path + "/List " + clean_file_path(n + " " + bd) + ".html"
    if os.path.exists(file):
        return True
    else:
        return False

def write_long_branch_up(hfile):
    hfile.write("&#9484;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&nbsp;\n")

def write_long_branch_down(hfile):
    hfile.write("&#9492;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&nbsp;\n")

def write_short_branch_up(hfile):
    hfile.write("&#9484;&#9472;&#9472;&#9472;&nbsp;\n")

def write_short_branch_down(hfile):
    hfile.write("&#9492;&#9472;&#9472;&#9472;&nbsp;\n")

def write_vertical_line(hfile):
    hfile.write("&#9474;")

def write_spaces_before_more(hfile, p, b):
    l = len(p) + len(b)
    if l > 32:
        print ("Need SpacesBeforemore for > 32", l)
        exit()

    write_spaces(hfile, 32 - l)

def clean_file_path(path):
    return path.replace("?","").replace("*","").replace("\"","")

#create_tree()
