import twitter

api = twitter.Api(consumer_key='',         # Insert here your twitter API keys
                  consumer_secret='',
                  access_token_key='',
                  access_token_secret='')

class Checker:

    def __init__(self, name):
        self.user = api.GetUser(screen_name=name)
        self.user_list = api.GetFriends(user_id=self.user.id, screen_name=None, cursor=None, count=None, total_count=None, skip_status=True, include_user_entities=True)
        self.screen_name_list = [self.user_list[i].screen_name.lower() for i in range(0, len(self.user_list))]
        self.numFol = len(self.user_list)


    def getFollowedNames(self):
        return self.screen_name_list

    def __contains__(self, user_name):
        l = self.getFollowedNames()
        ret = False
        for i in l:
            if i == user_name:
                ret = True
                break
        return ret

    def checkNum(self, BL):
        ret = 0
        for i in BL.list:
            #print(i)
            if i in self:
                ret += 1
        return ret

    def listMatch(self, BL):
        ret = []
        for i in BL.list:
            if i in self:
                ret.append(i)
        return ret
    
class Blacklist:

    def __init__(self, file='defaultList.txt'):
        f = open(file, 'r')
        buf = f.read()
        ls = buf.split('\n')
        f.close()

        for i in range(0, len(ls)):
            ls[i] = ls[i].replace(" ", "")
            ls[i] = ls[i].lower()

        self.list = ls



