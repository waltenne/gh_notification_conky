import sqlite3, os

class DataBase:
    def __init__(self):
        self.workdir    = os.path.dirname(os.path.realpath(__file__))
        self.connection = sqlite3.connect(self.workdir+'/pr.db')
        self.cursor     = self.connection.cursor()
        
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='github_pull_requests';")
        table_exist_pr = self.cursor.fetchone()
        if table_exist_pr == None:
            query = """CREATE TABLE IF NOT EXISTS github_pull_requests(
                        pr_id INT, repository TEXT, pr_created_at TIMESTAMP, pr_title TEXT);
                    """
            self.cursor.execute(query)
            
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='github_forks';")
        table_exist_status = self.cursor.fetchone()
        if table_exist_status == None:
            query = """CREATE TABLE IF NOT EXISTS github_forks(forks_count INT, date_forks TIMESTAMP);
                    """
            self.cursor.execute(query)
            
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='github_stars';")
        table_exist_status = self.cursor.fetchone()
        if table_exist_status == None:
            query = """CREATE TABLE IF NOT EXISTS github_stars(stars_count INT, date_stars TIMESTAMP);
                    """
            self.cursor.execute(query)
            
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='github_issues';")
        table_exist_status = self.cursor.fetchone()
        if table_exist_status == None:
            query = """CREATE TABLE IF NOT EXISTS github_issues(issues_count INT, date_issues TIMESTAMP);
                    """
            self.cursor.execute(query)
    
    def populePullRequests(self, pr):
        query = ''' INSERT INTO github_pull_requests(pr_id, repository, pr_created_at, pr_title)
                    VALUES(?,?,?,?)
                '''
        self.cursor.execute(query, pr)
        self.connection.commit()
        self.cursor.close()
    
    def populeStatus(self, table, status):
        query = """ INSERT INTO github_{}({}_count, date_{})
                    VALUES(?,?)
                """.format(table,table,table)
        self.cursor.execute(query, status)
        self.connection.commit()
        self.cursor.close()
    
    def checkStatus(self, table):
        query = """ select {}_count from github_{} order by {}_count desc""".format(table, table, table)
        self.cursor.execute(query)
        self.records = self.cursor.fetchall()
        for row in self.records:
            return f"{row[0]}"
        self.cursor.close()
    
    def checkPullRequests(self):
        query = """ select * from github_pull_requests order by pr_id desc limit 1"""
        self.cursor.execute(query)
        self.records = self.cursor.fetchall()
        for row in self.records:
            return row
        self.cursor.close()
        
    def checkPullRequestsID(self, pr_id):
        query = f""" select pr_id from github_pull_requests where pr_id = {pr_id}"""
        self.cursor.execute(query)
        self.records = self.cursor.fetchall()
        for row in self.records:
            return row
    
    def checkPullRequestsCount(self):
        query = """ select count(*) from github_pull_requests"""
        self.cursor.execute(query)
        self.records = self.cursor.fetchall()
        for row in self.records:
            return row
        self.cursor.close()
DataBase().checkPullRequests()