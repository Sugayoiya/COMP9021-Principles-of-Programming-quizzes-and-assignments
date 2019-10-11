import os
import sys
from collections import defaultdict

class Sudoku:
    def __init__(self,filename):
        if not os.path.exists(filename):
            print(f'No file named {filename} in working directory, giving up...')
            sys.exit()

        self.filename = filename
        grid = [] # default list
        
        # Exception
        class SudokuError(Exception):
            def __init__(self, message = 'Incorrect input'):
                self.message = message
        
        with open(filename,'r',encoding = 'utf-8') as s:
            for line in s:
                tempStr = line.split()
                temp_str = []
                if len(tempStr)>0:
                    # check unstandard input(such like sudoku_4.txt)
                    if len(tempStr) != 9:
                        for i in range(len(tempStr)):
                            for j in range(len(tempStr[i])):
                                temp_str.append(tempStr[i][j])
                        tempStr = temp_str
                    grid.append(tempStr)
        # keep filename without '.txt'    
        filename = filename.strip()
        filename = filename.replace('.txt','')
        self.filename = filename
        # sudoku list
        self.grid = grid
        
#         for rows in self.grid:
#             for i in rows:
#                 print(i,end = '')
#             print()
            
        # check simple vaild
        if len(self.grid) != 9:
            raise SudokuError('Incorrect input')
        for i in self.grid:
            if len(i) != 9:
                raise SudokuError('Incorrect input')
            # print each row
#             print(i)                  
            for j in i:
                if ord(j)> 57 or ord(j) < 48:
#                     print('problem input:',j)
                    raise SudokuError('Incorrect input')
        self.boxes = {'1': [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)], \
                      '2': [(3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2)], \
                      '3': [(6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2)], \
                      '4': [(0, 3), (0, 4), (0, 5), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5)], \
                      '5': [(3, 3), (3, 4), (3, 5), (4, 3), (4, 4), (4, 5), (5, 3), (5, 4), (5, 5)], \
                      '6': [(6, 3), (6, 4), (6, 5), (7, 3), (7, 4), (7, 5), (8, 3), (8, 4), (8, 5)], \
                      '7': [(0, 6), (0, 7), (0, 8), (1, 6), (1, 7), (1, 8), (2, 6), (2, 7), (2, 8)], \
                      '8': [(3, 6), (3, 7), (3, 8), (4, 6), (4, 7), (4, 8), (5, 6), (5, 7), (5, 8)], \
                      '9': [(6, 6), (6, 7), (6, 8), (7, 6), (7, 7), (7, 8), (8, 6), (8, 7), (8, 8)]}
            
    def preassess(self):
        grid = self.grid     
#         print(grid == self.grid)
        # check rows
        for rows in grid:
            temp_list1 = [ x for x in rows if x != '0']
            temp_set1 = set(temp_list1)
            if len(temp_list1)!=len(temp_set1):
                print( 'There is clearly no solution.')
                return
            temp_list1 =[]
            temp_set1 = set()        
#         print(grid == self.grid)
        # check columns
        temp_list2 =[]
        temp_set2 = set()
        for i in range(9):
            for j in range(9):
                if grid[j][i]!='0':
                    temp_list2.append(grid[j][i])
            temp_set2 = set(temp_list2)
            if len(temp_list2)!=len(temp_set2):
                print( 'There is clearly no solution.')
                return
            temp_list2 =[]
            temp_set2 = set()    
#         print(grid == self.grid)
        # check boxes
        temp_list3 = []
        temp_set = set()
        for i in (0,3,6):
            for j in(0,3,6):
                for p in range(3):
                    for k in range(3):
                        if grid[i+p][j+k] != '0':
                            temp_list3.append(grid[i+p][j+k])
#                 print(temp_list3)
                temp_set3 = set(temp_list3)
                if len(temp_list3)!= len(temp_set3):
                    print( 'There is clearly no solution.')
                    return
                temp_list3 = []
                temp_set = set()
        print( 'There might be a solution.')
        return
    
    # get bare_tex input 
    def to_bare_tex(self):
        grid = self.grid
        tex_dict =defaultdict(list)   
        for i in range(len(grid)):
            for j in range(len(grid)):
                tex_dict[(i,j)].append(grid[i][j])
        return tex_dict

    # check forced digit row 
    def each_row(self,tex,i,j):
        row = tex
#         print(row)
        for a in range(9):
            if int(row[(i,a)][0]) in row[(i,j)][1]:
                (row[(i,j)][1]).remove(int(row[(i,a)][0]))
        return row
    # check forced digit column
    def each_column(self,tex,i,j):
        column = tex
#         print(row)
        for a in range(9):
            if int(column[(a,j)][0]) in column[(i,j)][1]:
                (column[(i,j)][1]).remove(int(column[(a,j)][0]))
        return column
    # check forced digit box
    def each_box(self,tex,i,j):
        box_num = 0
        boxes = tex
        for key in self.boxes:
            if (i,j) in self.boxes[key]:
                box_num = key
                break
#         print(box_num)
#         print(self.boxes[box_num])
        for box in self.boxes[box_num]:
            if int(boxes[box][0]) in boxes[(i,j)][1]:
                (boxes[(i,j)][1]).remove(int(boxes[box][0]))
        return boxes
    # check forced digit that only this cell has, every other cells in this box does not have
    def each_minus(self,tex,i,j):
        box_num = 0
        box_set = set()
        boxes = tex
        for key in self.boxes:
            if (i,j) in self.boxes[key]:
                box_num = key
                break
        for box in self.boxes[box_num]:
            if boxes[box][0] == '0':
                if (i,j) != box:
                    box_set |= boxes[box][1]
        if len((boxes[(i,j)])[1] - box_set) == 1:
            # possible number set = this number 
            (boxes[(i,j)])[1] -=  box_set
            # fill in this cell with this number
            temp = (boxes[(i,j)])[1] - box_set
            temp = [e for e in temp]
            (boxes[(i,j)])[0] = str(temp[0])
        return boxes
           
    # get bare_tex input 
    def to_forced_tex(self):
        bare_tex = self.to_bare_tex()
        flag = 1 # progress
#         print('************',grid)
        for i in range(9):
            for j in range(9):
                if bare_tex[(i,j)][0] == '0' and len(bare_tex[(i,j)]) == 1:
                        bare_tex[(i,j)].append({1,2,3,4,5,6,7,8,9})
        while flag == 1:
            flag_flag = 0
            for i in range(9):
                for j in range(9):
                    if bare_tex[(i,j)][0] == '0':
                        bare_tex = self.each_row(bare_tex,i,j)
                        bare_tex = self.each_column(bare_tex,i,j)
                        bare_tex = self.each_box(bare_tex,i,j)
            for i in range(9):
                for j in range(9):
                    if bare_tex[(i,j)][0] == '0':
                        bare_tex = self.each_minus(bare_tex,i,j)
#             print(self.bare_tex)      
            for i in range(9):
                for j in range(9):
                    if len(bare_tex[(i,j)]) == 2:
                        if len((bare_tex[(i,j)])[1]) == 1:
#                             print((i,j))
                            bare_tex[(i,j)][0] = [e for e in bare_tex[(i,j)][1]]
                            bare_tex[(i,j)][0] = str(bare_tex[(i,j)][0][0])
                            bare_tex[(i,j)].pop()
                            flag_flag = 1
            flag = flag_flag
        return bare_tex
                                
    # input: bare_tex  or forced.tex or marked.tex or worked.tex
    # output: .tex 
    def to_tex(self, tex, file_style):
        filename = self.filename
#         print(tex)
        if file_style == 'bare':
            filename +='_bare.tex'
        if file_style =='forced':
            filename += '_forced.tex'
        if file_style == 'marked':
            filename += '_marked.tex'
        if file_style == 'worked':
            filename += '_worked.tex'
        with open(filename,'w',encoding = 'utf-8') as f:
            f.write('\documentclass[10pt]{article}\n')
            f.write('\\usepackage[left=0pt,right=0pt]{geometry}\n')
            f.write('\\usepackage{tikz}\n')
            f.write('\\usetikzlibrary{positioning}\n')
            f.write('\\usepackage{cancel}\n')
            f.write('\pagestyle{empty}\n')
            f.write('\n')
            f.write('\\newcommand{\\N}[5]{\\tikz{\\node[label=above left:{\\tiny #1},\n')
            f.write('                               label=above right:{\\tiny #2},\n')
            f.write('                               label=below left:{\\tiny #3},\n')
            f.write('                               label=below right:{\\tiny #4}]{#5};}}\n')
            f.write('\n')
            f.write('\\begin{document}\n')
            f.write('\n')
            f.write('\\tikzset{every node/.style={minimum size=.5cm}}\n')
            f.write('\n')
            f.write('\\begin{center}\n')
            f.write('\\begin{tabular}{||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||}\hline\hline\n')
            for i in range(9):
                templine = '% Line '
                templine += str(i+1)
                templine += '\n'
                f.write(templine)
                for j in range(9):
                    texStr = '\\N'
                    # each '{}' content
                    temp_1 ='{'
                    temp_2 ='{'
                    temp_3 ='{'
                    temp_4 ='{'
                    temp_5 ='{'
                    # store numbers in each '{}'
                    templist_1,templist_2 ,templist_3 ,templist_4  = [],[],[],[]
                    if file_style == 'bare'or file_style =='forced':
                        if(tex[(i,j)])[0]!= '0':
                            temp_5 += tex[(i,j)][0] 
                    if file_style =='marked':
                        if (tex[(i,j)])[0] != '0':
                            temp_5 += (tex[(i,j)])[0] 
                        else:
                            for p in (tex[(i,j)])[1]:
                                if p in (1,2):
                                    templist_1.append(p)
                                if p in (3,4):
                                    templist_2.append(p)
                                if p in (5,6):
                                    templist_3.append(p)
                                if p in (7,8,9):
                                    templist_4.append(p)
    
                    temp_1 += ' '.join(str(e) for e in sorted(templist_1))
                    temp_2 += ' '.join(str(e) for e in sorted(templist_2))
                    temp_3 += ' '.join(str(e) for e in sorted(templist_3))
                    temp_4 += ' '.join(str(e) for e in sorted(templist_4))
                    
                    temp_1 += '}'
                    temp_2 += '}'
                    temp_3 += '}'
                    temp_4 += '}'
                    temp_5 += '}'
                    
                    if j in (2,5):
                        temp_5 += ' &\n'
                    elif j == 8:
                        # each 3 lines 
                        if i % 3 == 2:
                            temp_5 +=' \\\\ \hline\\hline\n'
                        else:
                            temp_5 +=' \\\\ \hline\n'
                    else:
                        temp_5 += ' & '
                    
                    texStr = texStr + temp_1 + temp_2 + temp_3 + temp_4 + temp_5
                    f.write(texStr)
                if i != 8:
                    f.write('\n')
            f.write('\end{tabular}\n')
            f.write('\end{center}\n')
            f.write('\n')
            f.write('\end{document}\n')
                               
    # output bare tex
    def bare_tex_output(self):
        self.to_tex(self.to_bare_tex(), 'bare')
    # output forced tex
    def forced_tex_output(self):
        self.to_tex(self.to_forced_tex(), 'forced')
    # output marked tex
    def marked_tex_output(self):
        self.to_tex(self.to_forced_tex(),'marked')