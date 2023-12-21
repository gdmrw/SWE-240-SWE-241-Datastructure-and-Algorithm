from typing import List

class Solution1:
    # permute function reference from https://leetcode.com/problems/permutations/solutions/3850526/video-100-unlocking-recursive-backtracking-for-permutations/
    def permute(self, strings: str) -> List[str]:
        def dfs(path, used):
            if len(path) == len(strings):
                result.append(''.join(path))
                return
            for i in range(len(strings)):
                if not used[i]:
                    path.append(strings[i])
                    used[i] = True     # lock
                    dfs(path, used)
                    path.pop()          # pop out last element
                    used[i] = False     # unlock backtrack start

        result = []
        dfs([], [False] * len(strings))
        return result

    def is_substring(self,permute_string: str, target:str) -> bool:
        result = self.permute(permute_string)
        for element in result:
                if element in target:
                    return True
        return False

class Solution2:
    def min_moves_to_solve_queens(self,queen_positions):
        # concept reference from https://www.youtube.com/watch?v=Ph95IHmRp5M&t=214s
        # Helper function to check if a queen can be placed at the given row without being attacked.
        def is_safe(row, col):
            for c in range(col):
                # Check if another queen is in the same row, or if they are on the same diagonal.
                if queen_positions[c] == row or \
                        queen_positions[c] - c == row - col or \
                        queen_positions[c] + c == row + col:
                    return False
            return True

        # Recursive function to solve the problem starting from the first column.
        def solve(col):
            # If we have placed all queens, return 0 moves required.
            if col == 8:
                return 0

            # Set an initial high number of moves.
            min_moves = float('inf')
            original_row = queen_positions[col]

            # Try placing the queen in every row in the current column.
            for row in range(1, 9):
                queen_positions[col] = row
                # If the queen is not attacked, proceed to place the next queen.
                if is_safe(row, col):
                    # If the queen was moved, increment the move count.
                    if row != original_row:
                        moves = solve(col + 1) + 1
                    else:
                        moves = solve(col + 1)
                    # Find the minimum moves needed.
                    min_moves = min(min_moves, moves)

            # Reset the row position before backtracking.
            queen_positions[col] = original_row
            return min_moves

        # Start solving from the first column.
        return solve(0)

solution = Solution1()
strings = "abc"
result = solution.permute(strings)
print(solution.permute(strings))
print(solution.is_substring("ab", "eidboaoo"))
print(solution.is_substring("cabbage12", "cabbage"))

solution2 = Solution2()
print(solution2.min_moves_to_solve_queens([2, 1, 3, 5, 4, 6, 7, 8]))
print(solution2.min_moves_to_solve_queens([1, 5, 8, 6, 3, 7, 2, 4]))
