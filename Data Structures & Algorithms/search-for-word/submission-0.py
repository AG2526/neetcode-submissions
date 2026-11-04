class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #have the cells we have walked through so far then have a variable k which is how many letters of the word we've matched then a coordinate(r,c) for the position in the grid and there will be 4 options to go up ,down ,left,right . if k = len(word) then its a success there will be a failure if we are out of bounds ,wrong letter or already used the cell and you should be able to restore the cell you marked as visited .from a cell check whether it matches word[k] and if not then the path is dead. then if it matches check the neighbours and look for word[k+1]. a cell cant be used twice so mark it as visited before going deeper and unmark it when you come back . if every letter is matched then return true and if any direction returns true then pass it up 
        rows = len(board) #number of rows in the grid 
        cols = len(board[0])#number of columns (every row has the same length)
        def dfs(r,c,k): 
            if k == len(word): 
                return True 
            if r<0 or r>= rows or c<0 or c>= cols: 
                return False 
            if board[r][c] != word[k]: 
                return False 
            temp = board[r][c]
            board[r][c] = "#"
            found = (
                dfs(r+1,c,k+1)or 
                dfs(r-1,c,k+1)or 
                dfs(r,c+1,k+1)or
                dfs(r,c-1,k+1)
            )
            board[r][c] = temp 
            return found 
        for r in range(rows): 
            for c in range(cols): 
                if dfs(r,c,0): 
                    return True 
        return False
        

            