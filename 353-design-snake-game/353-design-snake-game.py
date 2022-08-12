from collections import deque
class SnakeGame:
    
    
    
    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.food = deque([tuple(fooditem) for fooditem in food])
        self.width = width
        self.height = height
        self.snake = deque([(0, 0)])
        self.snake_set = set([(0, 0)])
        self.dirs = {
            "R": (0, 1),
            "L": (0, -1),
            "U": (-1, 0),
            "D": (1, 0)
        }
        print("food: ", food)
        

    def move(self, direction: str) -> int:
        headPos = self.snake[0]
        nextPos = (headPos[0] + self.dirs[direction][0], headPos[1] + self.dirs[direction][1])
        
        if not ( 0 <= nextPos[0] < self.height) or not( 0 <= nextPos[1] < self.width):
            print(f"{nextPos} out of bounds")
            return -1
        
        
        print("Current self.snake: ", self.snake)
        foodFound = self.food and nextPos == self.food[0]
        if foodFound:        
            self.food.popleft()
        else:
            val = self.snake.pop()
            self.snake_set.remove(val)
        
        if nextPos in self.snake_set:
            print(f"{nextPos} already in snake: {self.snake}")
            return -1
        
        self.snake.appendleft(nextPos)
        self.snake_set.add(nextPos)
        
        return len(self.snake) - 1
            

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)