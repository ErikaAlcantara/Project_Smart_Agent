from ia_agents.agent_enum import AgentsEnum

class AgentManager:
    def __init__ (self):
        self.agent = None

    def create_agent(self, agent_type):
        if agent_type == AgentsEnum.HUMAN_AGENT:
            self.get_human_agent()
            return
        if agent_type == AgentsEnum.DFS_AGENT:
            self.get_dfs_agent()
            return
        if agent_type == AgentsEnum.BFS_AGENT:
            self.get_bfs_agent()
            return

    def get_agent_enum(self):
        return AgentsEnum

    def get_dfs_agent(self):
        print("DFS!!!")

    def get_bfs_agent(self):
        print("BFS!!!")      

    def get_human_agent(self):
        print("HUMAN")      
        
    