class Agent:
    def __init__(self, codename, realname, location, status, missionscompleted):
        self.codeName = codename
        self.realName = realname
        self.location = location
        self.status = status
        self.missionsCompleted = missionscompleted

    def __str__(self):
        return (f"Agent {self.codeName} ({self.realName}) - Location: {self.location},"
                f" Status: {self.status}, Missions Completed: {self.missionsCompleted}")