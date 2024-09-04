class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        def getNextPosition(currentDirection: str, currentPosition: Tuple[int]) -> Tuple[int]:
            direction = directionMap[currentDirection]
            
            nextPosition = direction[0] + currentPosition[0], direction[1] + currentPosition[1]            
            if nextPosition in obstacleSet:
                return currentPosition
            else:
                return nextPosition
        
        def getNextDirection(currentDirection: str, change: int) -> str:

            directionChangeMap = {
                ("N", -1): "E",
                ("N", -2): "W",

                ("S", -1): "W",
                ("S", -2): "E",

                ("E", -1): "S",
                ("E", -2): "N",

                ("W", -1): "N",
                ("W", -2): "S",
            }
            
            return directionChangeMap[(currentDirection, change)]
        
        def euclidDistance(currentPosition: Tuple[int]) -> int:
            return currentPosition[0] ** 2 + currentPosition[1] ** 2
            
            
        obstacleSet = set(
            [ (r, c) for r, c in obstacles
            ]
        )
        
        currentPosition = (0, 0)
        currentDirection = "N"
        maxDistance = 0
        directionMap = {
            "N": (0, 1),
            "S": (0, -1),
            "E": (1, 0),
            "W": (-1, 0)
        }
        
        for command in commands:
            if command < 0:
                currentDirection = getNextDirection(currentDirection, command)
            else:
                
                for i in range(command):
                    currentPosition = getNextPosition(currentDirection, currentPosition)
                    
                    maxDistance = max(maxDistance, euclidDistance(currentPosition))
        
        
        return maxDistance

        
        
        
        