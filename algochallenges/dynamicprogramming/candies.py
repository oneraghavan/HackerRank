ratings=['93171','91649','85163','61161','47441','47265','17338','85194','51669','17817','41112','45456','10451','57276','40707','15801','79337','44392','7505','89319','42883','74846','366','95095','13153','27507','94963','23744','66363','54633','70285','65185','94133','90621','59241','76588','86984','4781','93233','80135','60550','12433','4309']
numbers = 43

prevsteep = 0
previncreasesteep = 0
prevdecreasesteep = 0
increasesteep = 0
decreasesteep = 0
candiescount = 0
genloop = 1

for idx, val in enumerate(ratings):
#    print 'current rating',val,candiescount
    genloop = 1
    if idx > 0:
        if increasesteep > 0:
#            print 'increing steep'
            if val > ratings[idx-1]:
                increasesteep = increasesteep + 1
                if numbers - 1 == idx:
                    candiescount = candiescount + ((increasesteep + 1) * (increasesteep + 2)/2)
                    print 'gaining from ' , increasesteep , val , candiescount
                    previncreasesteep = increasesteep
                    if prevsteep == -1:
                        candiescount = candiescount + increasesteep
                        previncreasesteep = previncreasesteep + 1
                        print 'gaining from +in' , val
                    prevsteep = 1
                    increasesteep = 0
                    genloop = 0


            else:
                candiescount = candiescount + ((increasesteep + 1) * (increasesteep + 2)/2)
                print 'gaining from ' , increasesteep , val , candiescount , prevsteep
                previncreasesteep = increasesteep
                if prevsteep == -1:
                    candiescount = candiescount + increasesteep
                    previncreasesteep = previncreasesteep + 1
                    print 'gaining from +in' , val
                prevsteep = 1
                increasesteep = 0
#                genloop = 0
        elif decreasesteep > 0:
#            print 'decreasing steep'
            if val < ratings[idx-1]:
                decreasesteep = decreasesteep + 1
                if numbers - 1 == idx:
                    candiescount = candiescount + ((decreasesteep + 1) * (decreasesteep + 2)/2)
                    print 'falling from ' , decreasesteep , val , candiescount
                    if prevsteep == 1 and previncreasesteep <= decreasesteep:
                        candiescount = candiescount + decreasesteep + 1 - previncreasesteep
                        print 'falling from +in for past lat ' , decreasesteep + 1
                    prevdecreasesteep = decreasesteep
                    prevsteep = -1
                    decreasesteep = 0
#                    genloop = 0

            else:
                candiescount = candiescount + ((decreasesteep + 1) * (decreasesteep + 2)/2)
                print 'falling from ' , decreasesteep , val , candiescount
                if prevsteep == 1 and previncreasesteep <= decreasesteep:
                    candiescount = candies#                    genloop = 0count + decreasesteep + 1 - previncreasesteep
#                    print 'falling from +in for past lat ' , decreasesteep + 1
                prevdecreasesteep = decreasesteep
                prevsteep = -1
                decreasesteep = 0
                genloop = 0
        if increasesteep == 0 and decreasesteep == 0 and genloop == 1:
            if val > ratings[idx-1]:
                print 'decidng incresteep' , increasesteep , 'val' , val , 'ratings[idx-1]' , ratings[idx-1]
                increasesteep = increasesteep + 1
            elif val < ratings[idx-1]:
                print 'decidng decteep' , increasesteep , 'val' , val , 'ratings[idx-1]' , ratings[idx-1]
                decreasesteep = decreasesteep + 1
            else:
                candiescount = candiescount + 1
                print 'just pressing 1' ,candiescount

#            print 'even',increasesteep,decreasesteep
print candiescount