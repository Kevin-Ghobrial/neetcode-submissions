class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        #1 mph takes an hour to drive a mile so 10 hours for 10 miles
        #2 takes 30 minutes so 5 hours for 10 miles
        #3 takes 20 so (150 / 60) hours for 10 mile

        # 3 mph. 60 / 3 = 20 (1 mile). (20 * miles left) 


        # see how long it takes a car to reach target
        # Start with furthest along and see time
        # if a car with less distance catches up, meaning they beat or get an equal time. Then they will be part of the fleet
        # I will track the current cars fleet and whether it is connected to the other fleet

        # hash of position with speed
    
        posToSpeed = {}
        for i in range(len(speed)):
            posToSpeed[position[i]] = speed[i]

        position = sorted(position)

        print(position)

        # 0, 2, 4, 6, 7
        prevTime = float('inf')
        fleetMax = 0

        res = []
        subset = []
        for i in range(len(position) - 1, -1, -1):
            # time to reach target
            milesLeft = target - position[i]
            time = (60 // posToSpeed[position[i]]) * milesLeft

            print(position[i], time, fleetMax)

            if i == len(position) - 1:
                fleetMax = time

            subset.append(position[i])

            if time > fleetMax:

                subset.pop()
                res.append(subset)
                subset = []
                subset.append(position[i])
                fleetMax = time


            #subset.append(position[i])
        
        if len(subset) != 0:
            res.append(subset)

        print(res)
        return len(res)

# 4 -> 1 mph: 6 -> 6 hours
# 2 -> 3 mph: 8 -> 2.4 hours
# 0 -> 2 mph: 10 -> 5 hours

# 7 -> 3
# 4 -> 3
# 1 -> 4.5
# 0 -> 10






