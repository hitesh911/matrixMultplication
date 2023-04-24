import os ,time

# utility functions,variables and classes 
matrix1_keyword = "first"
matrix2_keyword = "second"
matrix_submit_keyword= "done"
loading_timer = 2

# --------------------------functions ---------------------------
def showError(errorMsg):
  print("\x1b[0;30;41m"+errorMsg,"\x1b[0m")

# -------------------------------classes ---------------------------------
class MyMatrix(list):
  name:str
  body:list
  def __init__(self,name,body):
    self.name = name
    self.body = body
    super().__init__()
  def transpose(self):
    cols_list = []
    for i in range(len(self.body[0])):
      cols_list.append([])
      for j in range(len(self.body)):
        cols_list[i].append(self.body[j][i])
    return cols_list
  def rows(self):
    return len(self.body)
  def cols(self):
    try:
      return len(self.body[0])
    except:
      return 0
  def getRows(self):
    return self.body
  def getCols(self):
    return self.transpose()

  
class MyString(str):
  # some utility functions
  def onlyNumber(self,lst):
    for i in range(len(lst)):
      if(not lst[i].isnumeric()):
        return False
    return True
      
  def removeWide(self):
    list_string = self.__str__().split()
    new_string = ""
    for i in range(len(list_string)):
      new_string += list_string[i]
    return MyString(new_string)
  def areNumberList(self):
    numberList = self.__str__().split(",")
    if(self.onlyNumber(numberList)):
      return True
    else:
      return False




def printBothMatrices(current_matrix,matrix1,matrix2):
  print("Loading please wait.....")
  time.sleep(loading_timer)
  os.system("cls")
  if(current_matrix.name == "matrix1"):
    print("Matrix1:\t Selected")
  else:
    print("Matrix1:")
  for i in range(len(matrix1.body)):
    for j in range(len(matrix1.body[0])):
      print(matrix1.body[i][j],end="")
    print(end="\n")
  print("\n")
  if(current_matrix.name == "matrix2"):
    print("Matrix2:\t Selected")
  else:
    print("Matrix2:")
  for i in range(len(matrix2.body)):
    for j in range(len(matrix2.body[0])):
      print(matrix2.body[i][j],end="")
    print(end="\n")

    
def inputMatrices():
  matrix1 = MyMatrix("matrix1",[])
  matrix2 = MyMatrix("matrix2",[])
  os.system("cls")
  current_matrix = matrix1
  current_row = 0
  while True:
    colums, lines = os.get_terminal_size()
    print("-"*int(colums-5))
    print(f"Press {matrix1_keyword} for first matrix , {matrix2_keyword} for second matrix respectively. Default is first. Press {matrix_submit_keyword} for calculate result")
    userInp = input(f"Enter a {current_row+1} row like 1,2,3,4 of selected matrix\t")
    userString = MyString(userInp)
    input_without_spaces = userString.removeWide()
    if(input_without_spaces.lower() == matrix1_keyword):
      current_matrix = matrix1
      current_row = len(current_matrix.body)-1 if current_matrix.body else 0
    elif (input_without_spaces.lower() == matrix2_keyword):
      current_matrix = matrix2
      current_row = len(current_matrix.body)-1 if current_matrix.body else 0
    elif(input_without_spaces.areNumberList()):
      try:
        list_with_strings = input_without_spaces.split(",")
        new_row = list(map(int,list_with_strings))
        if(len(current_matrix.body) == 0):
          current_matrix.body.append(new_row)
          current_row+=1
        else:
          if(len(new_row)== len(current_matrix.body[0])):
            current_matrix.body.append(new_row)
            current_row+=1
          else:
            raise
      except:
        showError("You have to provide row of numbers seprated by ,(coma) and colums should be equals to previous row's columns")
    elif(input_without_spaces == matrix_submit_keyword):
      # checking both matrix saftisfy matrix multplication criteria 
      if(matrix1.cols() == matrix2.rows()):
        return matrix1,matrix2
      else:
        showError("Row's elements of first matrix should be equals to colum's elements of second matrix")
        continue 
    else:
      showError("Invalid Format")
    # printing both matrices 
    printBothMatrices(current_matrix,matrix1,matrix2)

def cal_position_value(col,row):
  value = 0
  for i in range(len(col)):
    value += col[i]*row[i]
  return value
def multiplyMatrix(matrix1,matrix2):
  # initilizing resultant matrix 
  rows = matrix1.rows()
  cols = matrix2.cols()
  resultantMatrix = []
  for i in range(rows):
    resultantMatrix.append([])
    for j in range(cols):
      current_index_value = cal_position_value(matrix1.getRows()[i], matrix2.getCols()[j])
      resultantMatrix[i].append(current_index_value)
  return resultantMatrix



    
    
def main():
  matrix1,matrix2 = inputMatrices()
  result_matrix = multiplyMatrix(matrix1,matrix2)
  
  print(result_matrix)


main()