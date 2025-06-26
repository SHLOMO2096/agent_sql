import mysql.connector


class Agent_dal:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "eagleEyeDB"
        )
        self.cursor = self.conn.cursor(dictionary=True)

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    def add_agent(self,codeName, realName, location, status, missionsCompleted):
        query = """INSERT INTO agents (codeName, realName, location, status, missionsCompleted) 
        VALUES (%s, %s, %s, %s, %s)"""
        self.cursor.execute(query, (codeName, realName, location, status, missionsCompleted))
        self.conn.commit()

    def get_all_agents(self):
        query = "SELECT * FROM agents"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_agent_by_codname(self, codname):
        query = "SELECT * FROM agents WHERE codeName = %s "
        self.cursor.execute(query, (codname,))
        return self.cursor.fetchall()

    def update_agent(self,codeName, realName, location, status, missionsCompleted):
        query = """UPDATE agents SET realName = %s, location = %s, status = %s, 
        missionsCompleted = %s WHERE codeName = %s"""
        self.cursor.execute(query, (realName, location, status, missionsCompleted, codeName))
        self.conn.commit()

    def delete_agent(self, codname):
        query = "DELETE FROM agents WHREE codname = %s"
        self.cursor.execute(query, (codname,))
        self.conn.commit()



# dal = Agent_dAL()
# dal.add_agent("wed567", "idan", "iran", "Active", 7)
# agent = dal.get_agent_by_codname("gfd345")
# print(agent)
# agents = dal.get_all_agents()
# for agent in agents:
#     a = agent
#     print(a)

dal.close()



