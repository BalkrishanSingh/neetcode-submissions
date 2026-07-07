class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def get_box(board,index_tuple):
            x,y = index_tuple
            box = []
            for i in range(x*3,x*3+3):
                for j in range(y*3,y*3+3):
                    box.append(board[i][j])
            return box
        for i in range(len(board[0])):
            for j in range(len(board[0])):
                row = board[i]
                column = [x[j] for x in board]
                box_index = ((i//3),(j//3))
                box = get_box(board, box_index)

                row_set = set(row)
                column_set = set(column)
                box_set = set(box)
                row_flag =  int('.' in row) 
                column_flag = int('.' in column) 
                box_flag = int('.' in box)
                current_flag =  ((len(row_set) - row_flag) == (9 - row.count("."))  and (len(column_set) - column_flag) == (9 - column.count(".")) and (len(box_set) - box_flag) == (9 - box.count(".")))
                if current_flag == False:
                    return False
        return True
            
                
        
                