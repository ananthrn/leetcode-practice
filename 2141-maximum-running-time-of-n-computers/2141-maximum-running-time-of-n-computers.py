import sortedcontainers
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        
        def getSimpleRunTime(n: int, batteries: List[int]) -> int:
            timeStamp = 0
            batteryHeap = list(map(lambda x: -x, batteries))

            heapq.heapify(batteryHeap)
            while True:
                buffer = []
                # print("timeStamp: ", timeStamp)
                # print("batteries before: ", batteryHeap)

                if len(batteryHeap) < n:
                    return timeStamp
                for j in range(n):

                    topBattery =  -heapq.heappop(batteryHeap)
                    # print("topBattery: ", topBattery)
                    if topBattery - 1 > 0:
                        buffer.append(topBattery - 1)


                for rem in buffer:
                    heapq.heappush(batteryHeap, -rem)

                # print("buffer: ", buffer)
                # print("batteries after: ", batteryHeap)
                # print()
                timeStamp += 1

            return timeStamp
        
        def getBetterRunTime(n: int, batteries: List[int]) -> int:
            batterySorted = sortedcontainers.SortedList(batteries)
            
            timeStamp = 0
            while True:
                if len(batterySorted) < n:
                    return timeStamp
                
                leastBatteryLevel = batterySorted[-n]
                # print("timeStamp: ", timeStamp)
                # print("batterySorted: ", batterySorted)
                # print("leastBatteryLevel: ", leastBatteryLevel)
                # print()
                if leastBatteryLevel == 1:
                    buffer = [batteryLevel - 1 for batteryLevel in batterySorted[-n:] if batteryLevel > 1]
                    del batterySorted[-n:]
                    batterySorted.update(buffer)
                    timeStamp += 1
                elif leastBatteryLevel > 1:
                    prevBatteryLevel = batterySorted[-n - 1] if len(batterySorted) > n else 0
                    prevBatteryLevel = leastBatteryLevel - 1 if prevBatteryLevel == leastBatteryLevel else prevBatteryLevel
                    timeStampDelta = leastBatteryLevel - prevBatteryLevel
                    buffer = [batteryLevel - timeStampDelta for batteryLevel in batterySorted[-n:]]
                    del batterySorted[-n:]
                    batterySorted.update(buffer)
                    timeStamp += timeStampDelta
                else:
                    assert False, "Should not be here"
            
            return timeStamp
                    
                
        def getExtraPowerRunTime(n: int, batteries: List[int]) -> int:
            batterySorted = sortedcontainers.SortedList(batteries)
            
            batteryTopN = sorted(batterySorted[-n:])
            extraPower = sum(batterySorted[:-n])
            
            print("batteryTopN: ", batteryTopN)
            print("otherBatteries: ", batterySorted[:n])
            print("totalExtraPower: ", extraPower)
            print()
            for j in range(1, n):
                # print("j: ", j)
                # print("")
                extraPowerNeeded = j * (batteryTopN[j] - batteryTopN[j-1])
                print("j: ", j)
                print("batteryTopN[j], batteryTopN[j- 1], diff: ",batteryTopN[j], batteryTopN[j- 1], (batteryTopN[j] - batteryTopN[j-1]))
                print("extraPower:", extraPower)
                print("extraPowerNeeded: ", extraPowerNeeded)
                
                print()
                if extraPowerNeeded > extraPower:
                    return batteryTopN[j-1] + extraPower//j
                else:
                    extraPower -= extraPowerNeeded
            
            # if extraPower >= 0:
            return batteryTopN[-1] + extraPower//n
             
            
        betterVal = getExtraPowerRunTime(n, batteries)
        print("betterVal: ", betterVal)
        return betterVal
        